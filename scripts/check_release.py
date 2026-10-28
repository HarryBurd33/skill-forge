#!/usr/bin/env python3
"""Verify the checked-in public file selection and local links without services."""
import ast
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import zipfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('forge', ROOT/'skills/skill-forge/scripts/forge.py')
forge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(forge)


def clean_first_use():
    """Exercise distributed bytes in temporary host paths, not native host UIs."""
    canonical = ROOT/'skills/skill-forge'
    expected_hash = forge.tree_hash(canonical)
    with tempfile.TemporaryDirectory(prefix='skill-forge-check-') as temporary:
        folder = Path(temporary)/'Café workspace'
        folder.mkdir()
        skill_archive, portable_archive = folder/'skill.zip', folder/'portable.zip'
        forge.package(ROOT, skill_archive, 'skill')
        forge.package(ROOT, portable_archive, 'portable')
        with zipfile.ZipFile(skill_archive) as archive:
            archive.extractall(folder/'extracted')
        extracted = folder/'extracted/skill-forge'
        forge.require(forge.tree_hash(extracted) == expected_hash, 'Extracted skill differs from canonical source')
        installs = 0
        for host, hidden in (('codex', '.agents'), ('claude', '.claude')):
            for scope in ('personal', 'project'):
                destination = folder/host/scope/hidden/'skills/skill-forge'
                process = subprocess.run(
                    [sys.executable, str(extracted/'scripts/forge.py'), 'install', str(extracted), str(destination)],
                    capture_output=True, text=True, encoding='utf-8', check=True,
                )
                result = json.loads(process.stdout)
                forge.require(result['installed_hash'] == expected_hash, 'Installed receipt differs from canonical source')
                forge.require(forge.tree_hash(destination) == expected_hash, 'Installed bytes differ from canonical source')
                forge.validate(destination)
                installs += 1
        with zipfile.ZipFile(portable_archive) as archive:
            forge.require(
                archive.read('skill-forge-prompt.md') == forge.portable_text(extracted).encode('utf-8'),
                'Distributed portable prompt differs from extracted skill resources',
            )
    return {'status': 'pass', 'temporary_install_paths': installs,
            'skill_hash_matches': True, 'portable_bytes_match': True,
            'scope': 'Filesystem/CLI only; native Codex and Claude discovery are separate checks.'}


def validate_skill_packages(root):
    """Validate closures at outermost SKILL boundaries and every nested header.

    Nested adapters may reference their containing package's shared resources.
    They are not standalone distributions, but still need valid metadata and
    matching directory names. Independent examples retain their own closures.
    """
    root = Path(root)
    forge.require(root.is_dir() and not forge.is_link(root), 'Expected a real release root')
    paths = sorted(
        (path for path in root.rglob('SKILL.md')
         if not ({'.git', 'dist'} & set(path.relative_to(root).parts))),
        key=lambda path: (len(path.relative_to(root).parts), path.relative_to(root).as_posix()),
    )
    packages = []
    metadata_records = {}
    for path in paths:
        forge.require(not forge.is_link(path), 'Skill metadata cannot be a symlink/reparse point')
        directory = path.parent
        container = next((package for package in packages
                          if package == directory or package in directory.parents), None)
        if container is None:
            container = directory
            packages.append(container)
            metadata_records[container] = []
        meta = forge.metadata(path.read_text(encoding='utf-8'))
        forge.require(meta['name'] == directory.name,
                      'Frontmatter name must match skill directory name: ' +
                      path.relative_to(root).as_posix())
        if directory != container:
            metadata_records[container].append({
                'path': path.relative_to(container).as_posix(),
                'name': meta['name'],
                'status': 'pass',
            })
    checks = []
    for package in packages:
        # validate traverses all Markdown beneath this boundary, including each
        # nested adapter. Links leaving this package remain rejected, even when
        # their destination is another existing file inside the repository.
        result = forge.validate(package)
        result['package'] = package.relative_to(root).as_posix()
        result['nested_metadata'] = metadata_records[package]
        checks.append(result)
    return checks


def main():
    selection = json.loads((ROOT/'release-manifest.json').read_text(encoding="utf-8"))['files']
    assert len(selection) == len(set(selection)), 'Duplicate manifest entries'
    selected = set(selection)
    links = 0
    for rel in selection:
        path = ROOT/rel
        forge.require(not Path(rel).is_absolute() and '..' not in Path(rel).parts, 'Invalid manifest entry')
        forge.check_public_file(path, Path(rel))
        if path.suffix == '.py':
            ast.parse(path.read_text(encoding="utf-8"), filename=rel)
        if path.suffix == '.json':
            json.loads(path.read_text(encoding="utf-8"))
        if path.suffix == '.md':
            content = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(encoding="utf-8"), flags=re.M|re.S)
            for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
                link = raw.strip().strip('<>')
                if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', link) or link.startswith('#'):
                    continue
                link = unquote(link.split('#',1)[0].split('?',1)[0])
                if not link:
                    continue
                target = (path.parent/link).resolve()
                forge.require(forge.within(target,ROOT), 'Link escapes repository: '+rel+' '+link)
                forge.require(target.exists(), 'Missing link: '+rel+' '+link)
                if target.is_file():
                    forge.require(target.relative_to(ROOT).as_posix() in selected, 'Linked file omitted: '+rel+' '+link)
                links += 1
    skill_checks = validate_skill_packages(ROOT)
    forge.require((ROOT/'portable/skill-forge-prompt.md').read_text(encoding="utf-8") == forge.portable_text(ROOT/'skills/skill-forge'), 'Portable prompt drift')
    first_use = clean_first_use()
    print(json.dumps({'status':'pass','public_files':len(selection),'relative_links':links,
                      'skills':skill_checks,'clean_first_use':first_use},indent=2))

if __name__ == '__main__':
    main()
