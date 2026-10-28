#!/usr/bin/env python3
"""Proposed deterministic integration tests; run with python3 FILE CANDIDATE_SKILL.
Browser visual checks remain separate. Tests create only owned temporary trees.
"""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

SKILL = Path(__file__).resolve().parents[1] / 'skills' / 'skill-forge'
spec = importlib.util.spec_from_file_location('candidate_forge', SKILL/'scripts/forge.py')
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)

def snapshot(root):
    return {str(p.relative_to(root)): ('link',str(p.readlink())) if p.is_symlink() else ('dir',) if p.is_dir() else ('file',p.read_bytes()) for p in root.rglob('*')}

class Attachment(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='anatomy-contract-')
        self.root = Path(self.temp.name).resolve()
        self.target = self.root/'pressure-rig-explainer'
        self.target.mkdir()
        (self.target/'SKILL.md').write_text('---\nname: pressure-rig-explainer\ndescription: Explain pressure using a physical test rig.\n---\n\n# Pressure rig\n')
    def tearDown(self):
        self.temp.cleanup()
    def test_attach_complete_idempotent_and_other_files_preserved(self):
        (self.target/'assets').mkdir()
        (self.target/'assets'/'user.txt').write_text('untouched')
        skill_bytes=(self.target/'SKILL.md').read_bytes()
        result=f.attach_anatomy(self.target)
        self.assertEqual(result['status'],'attached')
        self.assertEqual(len(result['files']),7)
        self.assertEqual((self.target/'SKILL.md').read_bytes(),skill_bytes)
        self.assertEqual((self.target/'assets'/'user.txt').read_text(),'untouched')
        before=snapshot(self.target)
        self.assertEqual(f.attach_anatomy(self.target)['status'],'unchanged')
        self.assertEqual(snapshot(self.target),before)
    def test_partial_and_customized_conflicts_unchanged(self):
        dest=self.target/'assets'/'anatomy'
        dest.mkdir(parents=True)
        (dest/'custom.txt').write_text('user customization')
        before=snapshot(self.target)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.target)
        self.assertEqual(snapshot(self.target),before)
        shutil.rmtree(dest)
        f.attach_anatomy(self.target)
        (dest/'model.mjs').write_text('custom model')
        before=snapshot(self.target)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.target)
        self.assertEqual(snapshot(self.target),before)
    def test_failure_cleanup_assets_absent_and_present(self):
        for existing in [False,True]:
            if existing: (self.target/'assets').mkdir()
            before=snapshot(self.target)
            with patch.object(f,'rename_directory_exclusive',side_effect=OSError('injected publication failure')):
                with self.assertRaises(OSError): f.attach_anatomy(self.target)
            self.assertEqual(snapshot(self.target),before)
        original=Path.write_bytes
        writes=[0]
        def fail_copy(path,data):
            if '.forge-anatomy-stage-' in str(path):
                writes[0]+=1
                if writes[0]==3: raise OSError('injected third file failure')
            return original(path,data)
        before=snapshot(self.target)
        with patch.object(Path,'write_bytes',fail_copy):
            with self.assertRaises(OSError): f.attach_anatomy(self.target)
        self.assertEqual(snapshot(self.target),before)
    def test_invalid_metadata_missing_target_and_file_collision(self):
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.root/'missing')
        (self.target/'SKILL.md').write_text('invalid metadata')
        before=snapshot(self.target)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.target)
        self.assertEqual(snapshot(self.target),before)
    def test_assets_file_and_destination_race_preserved(self):
        (self.target/'assets').write_text('user-owned asset file')
        before=snapshot(self.target)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.target)
        self.assertEqual(snapshot(self.target),before)
        (self.target/'assets').unlink()
        original=f.rename_directory_exclusive
        def race(source,destination):
            destination.mkdir()
            (destination/'concurrent-user.txt').write_text('preserve')
            original(source,destination)
        with patch.object(f,'rename_directory_exclusive',race):
            with self.assertRaises(OSError): f.attach_anatomy(self.target)
        self.assertEqual((self.target/'assets'/'concurrent-user.txt').read_text(),'preserve')
        self.assertEqual(sorted(p.name for p in self.target.iterdir()),['SKILL.md','assets'])
    def test_symlink_escape_and_parent_traversal_refused(self):
        outside=self.root/'outside'; outside.mkdir()
        (outside/'keep').write_text('safe')
        (self.target/'assets').symlink_to(outside,target_is_directory=True)
        before=snapshot(self.root)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.target)
        self.assertEqual(snapshot(self.root),before)
        (self.target/'assets').unlink()
        linked=self.root/'linked';linked.symlink_to(self.target,target_is_directory=True)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(linked)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.target/'..'/self.target.name)
        (self.target/'assets').mkdir()
        (self.target/'assets'/'anatomy').symlink_to(outside,target_is_directory=True)
        before=snapshot(self.root)
        with self.assertRaises(f.ForgeError): f.attach_anatomy(self.target)
        self.assertEqual(snapshot(self.root),before)
    def test_exclusive_publication_preserves_even_empty_directory(self):
        a=self.root/'a';b=self.root/'b';a.mkdir();b.mkdir()
        (a/'owned').write_text('data')
        with self.assertRaises(OSError): f.rename_directory_exclusive(a,b)
        self.assertTrue((a/'owned').exists()); self.assertEqual(list(b.iterdir()),[])
    def test_relocated_build_model_and_browser_closure(self):
        f.attach_anatomy(self.target)
        relocated=self.root/'relocated'/'pressure-rig-explainer'
        relocated.parent.mkdir()
        shutil.move(str(self.target),str(relocated))
        r=relocated/'assets'/'anatomy'
        output=subprocess.check_output(['node',str(r/'build.mjs'),'250','200'],cwd=str(self.root),text=True)
        record=json.loads(output);self.assertEqual(record['forceN'],50)
        self.assertGreaterEqual(record['solids'],40)
        ET.fromstring((r/'figure.svg').read_text())
        html=(r/'figure.html').read_text()
        self.assertNotIn(str(SKILL),html)
        self.assertNotIn('<script src=',html)
        self.assertIn((r/'vendor/iso.css').read_text(),html)
        self.assertIn('Copyright (c) 2026 Ryan',html)
        script=html.split('<script>',1)[1].rsplit('</script>',1)[0]
        scriptfile=self.root/'inline-script.js';scriptfile.write_text(script)
        subprocess.check_call(['node','--check',str(scriptfile)])
        # Execute inline browser code in a DOM stand-in to check its real import
        # closure and model coupling. Actual keyboard/layout checks need Chrome.
        probe=self.root/'probe.cjs'
        probe.write_text("const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');const elements={};for(const id of ['pressure','area','force','rig','travel','pressure-value','error','theme'])elements[id]={value:id==='pressure'?'250':id==='area'?'200':'',validity:{valid:true},textContent:'',innerHTML:'',listeners:{},addEventListener(type,fn){this.listeners[type]=fn;}};const readout={textContent:''};const document={getElementById:id=>elements[id],querySelector:()=>readout,body:{dataset:{theme:'dark'}}};vm.runInNewContext(fs.readFileSync(process.argv[2],'utf8'),{document});assert.equal(elements.force.textContent,'50.00 N');const before=elements.rig.innerHTML;elements.pressure.value='0';elements.pressure.listeners.input();assert.equal(elements.force.textContent,'0.00 N');assert.equal(readout.textContent,'0.00 N');assert.notEqual(elements.rig.innerHTML,before);elements.area.value='-1';elements.area.validity.valid=false;elements.area.listeners.input();assert.ok(elements.error.textContent);console.log('inline-browser model coupling passed');")
        subprocess.check_call(['node',str(probe),str(scriptfile)])
        js="import {pressureRig} from "+json.dumps((r/'model.mjs').as_uri())+"; import assert from 'node:assert/strict';assert.equal(pressureRig(0,200).forceN,0);assert.equal(pressureRig(250,200).forceN,50);assert.equal(pressureRig(250,200).strokeMm,5);for(const v of [-1,NaN,Infinity,'2']){assert.throws(()=>pressureRig(v,200));assert.throws(()=>pressureRig(200,v));}assert.throws(()=>pressureRig(Number.MAX_VALUE,Number.MAX_VALUE));"
        subprocess.check_call(['node','--input-type=module','-e',js])
        subprocess.check_call(['node',str(r/'build.mjs'),'0','200','--light'])
        self.assertIn('data-theme="light"',(r/'figure.html').read_text())
        fail=subprocess.run(['node',str(r/'build.mjs'),'-1','200'],capture_output=True)
        self.assertNotEqual(fail.returncode,0)


class ReleasePackageBoundaries(unittest.TestCase):
    """Nested metadata is independent; nested link closure belongs to its package."""
    @classmethod
    def setUpClass(cls):
        release_path = SKILL.parents[1] / 'scripts' / 'check_release.py'
        release_spec = importlib.util.spec_from_file_location('candidate_release_check', release_path)
        cls.release = importlib.util.module_from_spec(release_spec)
        release_spec.loader.exec_module(cls.release)
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='release-boundaries-')
        self.root = Path(self.temp.name).resolve()
        self.package = self.root / 'skills' / 'skill-forge'
        self.anatomy = self.package / 'subskills' / 'anatomy'
        self.finder = self.package / 'subskills' / 'skill-finder'
        self.example = self.root / 'examples' / 'example-rig'
        for directory in [self.package, self.anatomy, self.finder, self.example]:
            directory.mkdir(parents=True, exist_ok=True)
            self.skill(directory)
        shared = self.package / 'resources' / 'anatomy' / 'README.md'
        shared.parent.mkdir(parents=True)
        shared.write_text('Shared renderer guidance.\n', encoding='utf-8')
        self.append(self.anatomy, '[shared](../../resources/anatomy/README.md)')
        self.append(self.finder, '[adapter](../anatomy/SKILL.md)')
    def tearDown(self):
        self.temp.cleanup()
    def skill(self, directory, name=None):
        (directory/'SKILL.md').write_text(
            '---\nname: '+(name or directory.name)+'\ndescription: Fixture contract.\n---\n\n# Fixture\n',
            encoding='utf-8')
    def append(self, directory, text):
        path=directory/'SKILL.md'
        path.write_text(path.read_text(encoding='utf-8')+'\n'+text+'\n', encoding='utf-8')
    def test_containing_package_shared_links_and_independent_example_pass(self):
        results=self.release.validate_skill_packages(self.root)
        by_package={item['package']:item for item in results}
        self.assertEqual(set(by_package), {'skills/skill-forge','examples/example-rig'})
        nested=by_package['skills/skill-forge']['nested_metadata']
        self.assertEqual({item['name'] for item in nested}, {'anatomy','skill-finder'})
        self.assertTrue(all(item['status']=='pass' for item in nested))
        self.assertGreaterEqual(by_package['skills/skill-forge']['relative_links'],2)
        self.assertEqual(by_package['examples/example-rig']['nested_metadata'],[])
    def test_invalid_nested_metadata_and_directory_mismatch_rejected(self):
        (self.anatomy/'SKILL.md').write_text('not frontmatter', encoding='utf-8')
        with self.assertRaisesRegex(self.release.forge.ForgeError, 'frontmatter'):
            self.release.validate_skill_packages(self.root)
        self.skill(self.anatomy, name='wrong-name')
        with self.assertRaisesRegex(self.release.forge.ForgeError, 'match skill directory'):
            self.release.validate_skill_packages(self.root)
    def test_nested_link_cannot_escape_containing_package(self):
        # This file exists inside the release root, but outside Forge's package.
        (self.root/'outside.md').write_text('Must not become a runtime dependency.', encoding='utf-8')
        self.append(self.anatomy, '[escape](../../../../outside.md)')
        with self.assertRaisesRegex(self.release.forge.ForgeError, 'escapes skill package'):
            self.release.validate_skill_packages(self.root)
    def test_independent_example_retains_its_own_closure(self):
        self.append(self.example, '[another package](../../skills/skill-forge/SKILL.md)')
        with self.assertRaisesRegex(self.release.forge.ForgeError, 'escapes skill package'):
            self.release.validate_skill_packages(self.root)

if __name__=='__main__': unittest.main(verbosity=2)
