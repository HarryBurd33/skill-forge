"""Fixed public evaluator for a narrow question-retrieval change, not LLM quality."""
import importlib.util
import json
from pathlib import Path
import sys

# Load the fixed baseline helper, not candidate executable code.
spec = importlib.util.spec_from_file_location('fixed_forge', sys.argv[1])
forge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(forge)
skill = Path(sys.argv[2])
queries = {'destination': 'spreadsheet', 'constraints': 'constraints',
           'evidence': 'meta-analysis', 'csv': 'CSV', 'repository': 'repository'}
hits = {key: forge.search_questions(skill, query, 'accepted') for key, query in queries.items()}
checks = {}
for key, rows in hits.items():
    if key in ('destination', 'csv', 'repository'):
        checks[key] = any('destination' in row['affects'] for row in rows)
    else:
        expected = 'q-constraints' if key == 'constraints' else 'q-evidence'
        checks[key] = any(row['id'] == expected for row in rows)
questions = forge.question_entries(forge.read_json(skill / 'questions/questions.json'))
purposes = [' '.join(row['purpose'].lower().split()) for row in questions if row['status'] in ('accepted','revised')]
checks['deduplication'] = len(purposes) == len(set(purposes))
print(json.dumps({'checks': checks, 'hits': {key: [row['id'] for row in rows] for key, rows in hits.items()},
                 'destination_queries_supported': sum(checks[k] for k in ('destination','csv','repository'))}, indent=2))
