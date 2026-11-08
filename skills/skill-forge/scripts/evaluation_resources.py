#!/usr/bin/env python3
"""Optional metadata-only resource preflight and supplied access-evidence audit.

Not a sandbox, trace collector, authorization service or model evaluator.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys


class ResourceError(ValueError):
    pass


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(65536), b''):
            value.update(block)
    return value.hexdigest()


def require(condition, message):
    if not condition:
        raise ResourceError(message)


def label(value, name):
    require(isinstance(value, str) and bool(value.strip()), name + ' must be nonempty text')
    return value


def safe_path(value):
    label(value, 'path')
    path = Path(value)
    require(path.is_absolute() and '..' not in path.parts, 'path must be absolute without ..')
    for part in [path, *path.parents]:
        require(not part.is_symlink(), 'symlink path rejected: ' + str(path))
    require(path.exists(), 'missing path: ' + str(path))
    return path


def within(path, roots):
    return any(path == root or root in path.parents for root in roots)


def structure(data, pinned=True):
    require(isinstance(data, dict) and data.get('schema_version') == 1, 'schema_version must be 1')
    label(data.get('evaluation_id'), 'evaluation_id')
    require(data.get('execution') in ('local', 'external'), 'execution must be local or external')
    roots_data = data.get('allowed_roots')
    require(isinstance(roots_data, list) and bool(roots_data), 'allowed_roots must be nonempty')
    roots = [safe_path(root) for root in roots_data]
    require(all(root.is_dir() for root in roots), 'allowed roots must be directories')
    require(len(set(roots)) == len(roots), 'duplicate allowed root')
    entries = data.get('files')
    require(isinstance(entries, list) and bool(entries), 'files must be nonempty')
    seen = set()
    for item in entries:
        require(isinstance(item, dict), 'file must be an object')
        path = safe_path(item.get('path'))
        require(path.is_file(), 'resource must be a regular file: ' + str(path))
        require(within(path, roots), 'resource outside allowed roots: ' + str(path))
        require(path not in seen, 'duplicate resource: ' + str(path))
        seen.add(path)
        provenance = item.get('provenance')
        require(isinstance(provenance, dict), 'provenance must be an object')
        label(provenance.get('source'), 'provenance.source')
        label(provenance.get('revision'), 'provenance.revision')
        require(item.get('classification') in ('public', 'synthetic', 'private'), 'invalid classification')
        require(item.get('sharing') in ('local-only', 'external-approved'), 'invalid sharing constraint')
        if data['execution'] == 'external':
            require(item['sharing'] == 'external-approved', 'external execution requires external-approved sharing')
            if item['classification'] == 'private':
                label(item.get('approval_reference'), 'private external approval_reference')
        if pinned:
            sha = item.get('sha256')
            require(isinstance(sha, str) and len(sha) == 64 and all(c in '0123456789abcdef' for c in sha), 'invalid sha256')
    return roots


def freeze(data):
    structure(data, pinned=False)
    result = json.loads(json.dumps(data))
    for entry in result['files']:
        entry['sha256'] = digest(Path(entry['path']))
    # Revalidate after reads. This is a point-in-time check, not race containment.
    check(result)
    return result


def check(data):
    structure(data)
    for entry in data['files']:
        require(digest(Path(entry['path'])) == entry['sha256'], 'resource hash drift: ' + entry['path'])
    return {'status': 'PASS', 'evaluation_id': data['evaluation_id'], 'checked_files': len(data['files'])}


def audit(data, evidence, manifest_sha256):
    findings = []
    try:
        structure(data)
    except (ResourceError, OSError, TypeError) as error:
        return {'status': 'FAIL', 'findings': [str(error)], 'capture_complete': False}
    try:
        check(data)
    except (ResourceError, OSError) as error:
        findings.append(str(error))
    # Continue recording observed access violations even with incomplete capture.
    capture = evidence.get('capture') if isinstance(evidence, dict) else None
    bound = (isinstance(evidence, dict) and evidence.get('schema_version') == 1
             and evidence.get('evaluation_id') == data.get('evaluation_id')
             and evidence.get('manifest_sha256') == manifest_sha256)
    complete = (bound and isinstance(capture, dict) and capture.get('complete') is True
                and capture.get('scope') == 'all-file-reads'
                and isinstance(capture.get('method'), str) and bool(capture['method'].strip())
                and isinstance(capture.get('reads'), list))
    entries = {entry['path']: entry['sha256'] for entry in data.get('files', [])}
    reads = capture.get('reads', []) if isinstance(capture, dict) else []
    if not isinstance(reads, list):
        reads = []
        complete = False
    for event in reads:
        if not isinstance(event, dict) or not isinstance(event.get('path'), str):
            complete = False
            continue
        path = event['path']
        if path not in entries:
            findings.append('undeclared read: ' + path)
        elif event.get('sha256') != entries[path]:
            if 'sha256' not in event:
                complete = False
            else:
                findings.append('captured hash mismatch: ' + path)
    if not bound:
        complete = False
    status = 'FAIL' if findings else ('PASS' if complete else 'INCONCLUSIVE')
    return {'status': status, 'evaluation_id': data.get('evaluation_id'), 'findings': findings,
            'capture_complete': bool(complete), 'limitation': 'Supplied evidence only; unseen reads and authorization are not verified.'}


def read_json(path):
    # JSON data, never fixture contents, is emitted by this utility.
    return json.loads(Path(path).read_text(encoding='utf-8'))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('freeze', 'check', 'audit'):
        child = commands.add_parser(name)
        child.add_argument('manifest')
        if name == 'audit':
            child.add_argument('evidence', nargs='?')
    args = parser.parse_args(argv)
    try:
        data = read_json(args.manifest)
        if args.command == 'freeze':
            result = freeze(data)
        elif args.command == 'check':
            result = check(data)
        else:
            try:
                evidence = read_json(args.evidence) if args.evidence else None
            except (OSError, ValueError):
                evidence = None
            result = audit(data, evidence, digest(Path(args.manifest)))
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if args.command == 'freeze' or result['status'] == 'PASS' else (2 if result['status'] == 'INCONCLUSIVE' else 1)
    except (ResourceError, OSError, ValueError, TypeError, KeyError) as error:
        print(json.dumps({'status': 'FAIL', 'error': str(error)}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
