"""Executed resource guard checks; no model-quality or containment claims."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/skill-forge/scripts/evaluation_resources.py'
SPEC = importlib.util.spec_from_file_location('evaluation_resources', SCRIPT)
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


class Resources(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.fixtures = self.root / 'fixtures'
        self.fixtures.mkdir()
        for name in ('one.txt', 'two.txt'):
            (self.fixtures / name).write_text('public synthetic test fixture\n')
        self.spec = {'schema_version': 1, 'evaluation_id': 'comparison-1', 'execution': 'external',
                     'allowed_roots': [str(self.fixtures)], 'files': [
                         {'path': str(self.fixtures / name), 'classification': 'synthetic',
                          'sharing': 'external-approved',
                          'provenance': {'source': 'authored test fixture', 'revision': 'v1'}}
                         for name in ('one.txt', 'two.txt')]}
        self.pinned = guard.freeze(self.spec)
        self.evidence = {'schema_version': 1, 'evaluation_id': 'comparison-1',
                         'manifest_sha256': 'manifest-hash', 'capture': {
                             'complete': True, 'scope': 'all-file-reads', 'method': 'test instrumentation',
                             'reads': [{'path': e['path'], 'sha256': e['sha256']} for e in self.pinned['files']]}}

    def tearDown(self):
        self.temp.cleanup()

    def audit(self, evidence=None):
        return guard.audit(self.pinned, self.evidence if evidence is None else evidence, 'manifest-hash')

    def test_valid_two_files_and_metadata_only(self):
        self.assertEqual(guard.check(self.pinned)['status'], 'PASS')
        self.assertEqual(self.audit()['status'], 'PASS')
        self.assertNotIn('public synthetic test fixture', json.dumps(self.pinned))
        self.assertEqual(len(self.pinned['files'][0]['sha256']), 64)

    def test_drift_and_missing(self):
        path = Path(self.pinned['files'][0]['path'])
        path.write_text('changed')
        with self.assertRaisesRegex(guard.ResourceError, 'drift'):
            guard.check(self.pinned)
        self.assertEqual(self.audit()['status'], 'FAIL')
        path.unlink()
        with self.assertRaisesRegex(guard.ResourceError, 'missing'):
            guard.check(self.pinned)

    def test_undeclared_inside_and_outside(self):
        for path in (self.fixtures / 'unlisted.txt', self.root / 'outside.txt'):
            path.write_text('private sentinel')
            evidence = copy.deepcopy(self.evidence)
            evidence['capture']['reads'].append({'path': str(path), 'sha256': guard.digest(path)})
            self.assertEqual(self.audit(evidence)['status'], 'FAIL')
            evidence['capture']['complete'] = False
            self.assertEqual(self.audit(evidence)['status'], 'FAIL')

    def test_missing_partial_malformed_and_unbound_capture(self):
        self.assertEqual(guard.audit(self.pinned, None, 'manifest-hash')['status'], 'INCONCLUSIVE')
        for change in ({'complete': False}, {'scope': 'shell-log-regex'}, {'method': ''}, {'reads': None}):
            evidence = copy.deepcopy(self.evidence)
            evidence['capture'].update(change)
            self.assertEqual(self.audit(evidence)['status'], 'INCONCLUSIVE')
        for key in ('evaluation_id', 'manifest_sha256'):
            evidence = copy.deepcopy(self.evidence)
            evidence[key] = 'another-run'
            self.assertEqual(self.audit(evidence)['status'], 'INCONCLUSIVE')
        evidence = copy.deepcopy(self.evidence)
        del evidence['capture']['reads'][0]['sha256']
        self.assertEqual(self.audit(evidence)['status'], 'INCONCLUSIVE')

    def test_sharing_and_provenance(self):
        for edit in ({'classification': 'private', 'sharing': 'local-only'},
                     {'classification': 'private'}, {'provenance': {'source': 'fixture'}},
                     {'sharing': 'anything'}):
            spec = copy.deepcopy(self.spec)
            spec['files'][0].update(edit)
            with self.assertRaises(guard.ResourceError):
                guard.freeze(spec)
        spec = copy.deepcopy(self.spec)
        spec['files'][0].update(classification='private', approval_reference='user permission record 7')
        self.assertEqual(guard.check(guard.freeze(spec))['status'], 'PASS')

    def test_prefix_sibling_and_symlinks(self):
        sibling = self.root / 'fixtures-other'
        sibling.mkdir()
        (sibling / 'outside.txt').write_text('outside')
        spec = copy.deepcopy(self.spec)
        spec['files'][0]['path'] = str(sibling / 'outside.txt')
        with self.assertRaisesRegex(guard.ResourceError, 'outside'):
            guard.freeze(spec)
        link = self.fixtures / 'link.txt'
        link.symlink_to(self.fixtures / 'one.txt')
        spec['files'][0]['path'] = str(link)
        with self.assertRaisesRegex(guard.ResourceError, 'symlink'):
            guard.freeze(spec)
        directory_link = self.root / 'linked-root'
        directory_link.symlink_to(self.fixtures, target_is_directory=True)
        spec = copy.deepcopy(self.spec)
        spec['allowed_roots'] = [str(directory_link)]
        with self.assertRaisesRegex(guard.ResourceError, 'symlink'):
            guard.freeze(spec)

    def test_captured_hash_mismatch(self):
        self.evidence['capture']['reads'][0]['sha256'] = '0' * 64
        self.assertEqual(self.audit()['status'], 'FAIL')

    def test_cli_freeze_check_audit_exit_codes(self):
        manifest = self.root / 'manifest.json'
        manifest.write_text(json.dumps(self.spec))
        def run(*args):
            return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)
        frozen = run('freeze', manifest)
        self.assertEqual(frozen.returncode, 0, frozen.stdout)
        manifest.write_text(frozen.stdout)
        self.assertEqual(run('check', manifest).returncode, 0)
        self.assertEqual(run('audit', manifest).returncode, 2)
        evidence = self.root / 'capture.json'
        self.evidence['manifest_sha256'] = guard.digest(manifest)
        evidence.write_text(json.dumps(self.evidence))
        self.assertEqual(run('audit', manifest, evidence).returncode, 0)
        Path(self.pinned['files'][0]['path']).write_text('secret changed fixture')
        failed = run('check', manifest)
        self.assertEqual(failed.returncode, 1)
        self.assertNotIn('secret changed fixture', failed.stdout)


if __name__ == '__main__':
    unittest.main()
