#!/usr/bin/env python3
"""Verify the checked-in public file selection and local links without services."""
import ast
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('forge', ROOT/'skills/skill-forge/scripts/forge.py')
forge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(forge)

def main():
    selection = json.loads((ROOT/'release-manifest.json').read_text())['files']
    assert len(selection) == len(set(selection)), 'Duplicate manifest entries'
    selected = set(selection)
    links = 0
    for rel in selection:
        path = ROOT/rel
        forge.require(not Path(rel).is_absolute() and '..' not in Path(rel).parts, 'Invalid manifest entry')
        forge.check_public_file(path, Path(rel))
        if path.suffix == '.py':
            ast.parse(path.read_text(), filename=rel)
        if path.suffix == '.json':
            json.loads(path.read_text())
        if path.suffix == '.md':
            content = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M|re.S)
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
    skill_checks = []
    for path in ROOT.rglob('SKILL.md'):
        if '.git' not in path.parts and 'dist' not in path.parts:
            skill_checks.append(forge.validate(path.parent))
    forge.require((ROOT/'portable/skill-forge-prompt.md').read_text() == forge.portable_text(ROOT/'skills/skill-forge'), 'Portable prompt drift')
    print(json.dumps({'status':'pass','public_files':len(selection),'relative_links':links,'skills':skill_checks},indent=2))

if __name__ == '__main__':
    main()
