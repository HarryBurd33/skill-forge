#!/usr/bin/env python3
"""Frozen real subprocess comparator for the optional Claude metadata profile."""
import argparse,hashlib,json,pathlib,platform,subprocess,sys,tempfile,time
parser=argparse.ArgumentParser()
parser.add_argument('--baseline',type=pathlib.Path,required=True)
parser.add_argument('--candidate',type=pathlib.Path,required=True)
parser.add_argument('--cases',type=pathlib.Path,nargs='+',required=True)
parser.add_argument('--output',type=pathlib.Path,required=True)
a=parser.parse_args()
cases=[]
for path in a.cases: cases+=json.loads(path.read_text())['cases']
rows=[];metrics={};start=time.monotonic()
for label,root in [('baseline',a.baseline),('candidate',a.candidate)]:
 script=root/'scripts/forge.py'
 help_result=subprocess.run([sys.executable,str(script),'validate','--help'],capture_output=True,text=True)
 profile_supported='--profile' in help_result.stdout
 current=[];invalid_rejected=0
 for c in cases:
  with tempfile.TemporaryDirectory(prefix='forge-metadata-case-') as d:
   folder=pathlib.Path(d)/c['folder'];folder.mkdir();(folder/'SKILL.md').write_text(c['text'],encoding='utf-8')
   cmd=[sys.executable,str(script),'validate',str(folder)]
   effective=c['profile']
   if c['profile']!='generic':
    if profile_supported or c['profile']=='unknown': cmd+=['--profile',c['profile']]
    else: effective='generic (baseline profile unavailable)'
   r=subprocess.run(cmd,capture_output=True,text=True)
   accepted=r.returncode==0
   diagnostic_ok=not c.get('diagnostic') or c['diagnostic'].lower() in (r.stdout+r.stderr).lower()
   ok=accepted==c['expected_accept'] and diagnostic_ok
   if not c['expected_accept'] and not accepted and diagnostic_ok and c['profile']!='unknown': invalid_rejected+=1
   current.append({'id':c['id'],'kind':c['kind'],'result':'pass' if ok else 'fail','returncode':r.returncode,'accepted':accepted,'expected_accept':c['expected_accept'],'diagnostic_ok':diagnostic_ok,'effective_profile':effective,'stdout':r.stdout,'stderr':r.stderr})
 metrics[label]=invalid_rejected
 rows.append({'label':label,'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'profile_supported':profile_supported,'cases':current})
by={v['label']:{c['id']:c for c in v['cases']} for v in rows}
result={'schema_version':1,'execution_kind':'script_execution','host':platform.platform()+' Python '+platform.python_version(),'model':'not-applicable','elapsed_seconds':time.monotonic()-start,'case_files':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in a.cases],'runs':rows,'results':[{'id':c['id'],'baseline':by['baseline'][c['id']]['result'],'candidate':by['candidate'][c['id']]['result'],'artifact':a.output.name} for c in cases],'benefit':{'metric':'invalid_metadata_cases_correctly_rejected',**metrics},'limits':'Deterministic helper metadata validation only; no claim of downstream model quality, full YAML validity or native Claude execution.'}
a.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'candidate_pass':sum(c['result']=='pass' for c in by['candidate'].values()),'cases':len(cases),'benefit':result['benefit']}))
