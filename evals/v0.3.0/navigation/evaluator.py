"""Fixed navigation-only evaluator. Does not assert model behavior."""
import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HEADINGS = ['Private sessions', 'Freeze an improvement before evaluating it',
            'Supply actual evidence and adopt automatically', 'Managed copies', 'Release packages']
def slug(text):
    return re.sub(r'[^a-z0-9 -]', '', text.lower()).replace(' ', '-')
BLOCK = '\n<!-- skill-forge-contents:start -->\n**Contents**\n\n' + ''.join(
    '- [{}](#{})\n'.format(h, slug(h)) for h in HEADINGS
) + '<!-- skill-forge-contents:end -->\n'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def inventory(root):
    return {p.relative_to(root).as_posix(): sha(p) for p in root.rglob('*') if p.is_file()
            and not any(v in {'.git', '__pycache__', '.pytest_cache'} for v in p.relative_to(root).parts)
            and p.name != '.skill-forge-managed.json' and p.suffix not in ('.pyc', '.pyo')}

def evaluate(baseline, candidate, repo):
    spec = importlib.util.spec_from_file_location('fixed_forge', baseline/'scripts/forge.py')
    forge = importlib.util.module_from_spec(spec); spec.loader.exec_module(forge)
    assert forge.tree_hash(baseline) == '323f3aff35e785a8c53b7db06bbf40ad5d028e1a2f59c952f318637862f28dab'
    before = (baseline/'references/helpers.md').read_bytes()
    after = (candidate/'references/helpers.md').read_bytes()
    baseline_bundle = forge.portable_text(baseline)
    candidate_bundle = forge.portable_text(candidate)
    text = after.decode('utf-8')
    links = re.findall(r'\[[^\]]+\]\(#([^)]*)\)', text)
    wanted = [slug(h) for h in HEADINGS]
    nav1 = all(links.count(a) == 1 for a in wanted) and all(
        text.count('## '+h+'\n') == candidate_bundle.count('## '+h+'\n') == 1 for h in HEADINGS)
    old_files, new_files = inventory(baseline), inventory(candidate)
    helper = 'references/helpers.md'
    body_preserved = after.count(BLOCK.encode()) <= 1 and after.replace(BLOCK.encode(), b'', 1) == before
    other_files_preserved = {k:v for k,v in old_files.items() if k != helper} == {k:v for k,v in new_files.items() if k != helper}
    normalize = lambda s: re.sub(r'^Source SHA-256: `[0-9a-f]+`$', 'Source SHA-256: `<generated>`', s, flags=re.M)
    bundle_preserved = normalize(candidate_bundle.replace(BLOCK, '', 1)) == normalize(baseline_bundle)
    nav2 = body_preserved and other_files_preserved and bundle_preserved
    main = (candidate/'SKILL.md').read_text(encoding='utf-8')
    references = sorted((candidate/'references').glob('*.md'))
    long_refs = [p for p in references if len(p.read_text(encoding='utf-8').splitlines()) > 100]
    nav3 = len(main.splitlines()) < 500 and all('references/'+p.name in main for p in references) and all(
        re.search(r'(?im)^(?:\*\*contents\*\*|## contents|contents:)\s*$', p.read_text(encoding='utf-8')) for p in long_refs)
    errors = []
    try:
        forge.validate(candidate)
        assert forge.tree_hash(repo/'skills/skill-forge') == forge.tree_hash(candidate), 'Staged repository source mismatch'
        assert (repo/'portable/skill-forge-prompt.md').read_text(encoding='utf-8') == candidate_bundle, 'Portable drift'
    except Exception as exc:
        errors.append(str(exc))
    check = subprocess.run([sys.executable, str(repo/'scripts/check_release.py')], cwd=repo, text=True, capture_output=True)
    nav4 = not errors and check.returncode == 0
    checks = {k: 'pass' if v else 'fail' for k,v in [('NAV-1',nav1),('NAV-2',nav2),('NAV-3',nav3),('NAV-4',nav4)]}
    return {'kind':'script_execution', 'checks':checks, 'state':'pass' if all(v=='pass' for v in checks.values()) else 'fail',
            'baseline_hash':forge.tree_hash(baseline), 'candidate_hash':forge.tree_hash(candidate),
            'benefit':{'metric':'navigable_helper_section_links','value':sum(links.count(a)==1 for a in wanted)},
            'body_preserved':body_preserved,'other_core_files_preserved':other_files_preserved,'bundle_preserved':bundle_preserved,
            'main_lines':len(main.splitlines()),'long_references':[p.name for p in long_refs],
            'package_check':{'exit_code':check.returncode,'stdout':check.stdout,'stderr':check.stderr,'errors':errors},
            'limitation':'Navigation and byte preservation only; no new behavioral or native-host claim.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--baseline',type=Path,required=True)
    parser.add_argument('--candidate',type=Path,required=True); parser.add_argument('--repo',type=Path,required=True)
    args = parser.parse_args()
    print(json.dumps(evaluate(args.baseline.resolve(),args.candidate.resolve(),args.repo.resolve()),indent=2))
