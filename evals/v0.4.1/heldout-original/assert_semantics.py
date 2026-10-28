import json,sys,pathlib,hashlib
result=json.loads(pathlib.Path(sys.argv[1]).read_text())
fixture=pathlib.Path(sys.argv[2])
e=json.loads(pathlib.Path(sys.argv[3]).read_text())
n=result['normalized_result']; g=n['graph']; s=n['semantic_graph']
assert g['schema']=='JavaScriptApplicationGraph'
assert s['schema']=='JavaScriptSemanticRelationGraph'
assert not n['integrity_contradictions']
assert n['root_artifact_sha256']==s['root_artifact_sha256']
assert g['graph_id']==s['application_graph_id']
contexts={c['context_id']:c for c in s['evidence_contexts']}
def bound(node):
    ident=node['identity']; path=ident['module_path']; data=(fixture/path).read_bytes()
    assert hashlib.sha256(data).hexdigest()==ident['artifact_sha256']
    ev=node['evidence']; ctx=contexts[ev['context_id']]
    assert ctx['authority']=='ast-static-analysis' and ctx['state']=='observed'
    assert ctx['artifact']['sha256']==ident['artifact_sha256']
    loc=ev['location']; assert loc['available']; loc=loc['value']
    assert loc['source']==path and loc['kind']=='source-range'
    lines=data.decode().splitlines(keepends=True);a,b=loc['start'],loc['end']
    if a['line']==b['line']:return lines[a['line']-1][a['column']:b['column']]
    return lines[a['line']-1][a['column']:]+''.join(lines[a['line']:b['line']-1])+lines[b['line']-1][:b['column']]
imports=[x for x in g['edges'] if x['relation']=='imports' and x['properties'].get('resolved_path')==e['import_target'] and x['properties'].get('resolution_status')=='resolved' and x['properties'].get('specifier')==e['specifier'] and x['properties'].get('imported_name')==e['imported_name'] and x['properties'].get('local_name')==e['local_name']]
assert imports
assert any(x['evidence']['location']['value'].get('source')==e['import_source'] and x['evidence']['artifact']['sha256']==hashlib.sha256((fixture/e['import_source']).read_bytes()).hexdigest() for x in imports)
for path,name in e['functions'].items():
    nodes=[x for x in s['nodes'] if x['kind']=='function' and x['identity']['module_path']==path and x['properties'].get('name')==name]
    assert nodes and all(name in bound(x) for x in nodes)
returns=[x for x in s['nodes'] if x['kind']=='return-site' and x['identity']['module_path']==e['branch_source']]
assert any(e['branch_text'] in bound(x) for x in returns)
limits=' '.join(result['limitations']+s['limitations']).lower()
assert 'never executed' in limits and 'does not claim runtime execution' in limits
assert s['unknowns'] and s['coverage'] # preserve conservative uncertainty, not complete runtime claims
print(json.dumps({'semantic_facts_pass':True,'branch_authority':'source excerpt anchored by REA static return-site evidence','runtime_execution_proven':False}))
