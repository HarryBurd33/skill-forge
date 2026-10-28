"""Behavior checks for the guarded REA compiler utility (stdlib only)."""
import concurrent.futures
import importlib.util
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock

HERE = Path(__file__).resolve().parent
SCRIPT = Path(os.environ.get('REA_MACOS_SCRIPT', HERE / 'candidate/skill-forge/scripts/rea_macos.py'))
if not SCRIPT.is_file():
    SCRIPT = HERE.parent / 'skills/skill-forge/scripts/rea_macos.py'
spec = importlib.util.spec_from_file_location('rea_macos', SCRIPT)
rea = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rea)
REAL_POPEN = subprocess.Popen
MAP = 'module SwiftBridging { header "bridging" export * }\n'
DIAG = "some/path/module.modulemap:13:8: error: redefinition of module 'SwiftBridging'\n"


@unittest.skipUnless(os.name == 'posix', 'process tests require POSIX shebangs, sessions, and killpg')
class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='rea tests $; ')
        self.root = Path(self.temp.name)
        self.tool = self.root / "tool 'chain$;"
        maps = self.tool / 'usr/include/swift'
        maps.mkdir(parents=True)
        self.maps = maps
        for name in ('module.modulemap', 'bridging.modulemap'):
            (maps / name).write_text(MAP)
        self.compiler = self.tool / 'usr/bin/swiftc'
        self.compiler.parent.mkdir()
        self.compiler.write_text('''#!/usr/bin/env python3
import json,os,sys
from pathlib import Path
Path(os.environ['COMPILER_LOG']).write_text(json.dumps(sys.argv[1:]))
''')
        self.compiler.chmod(0o700)
        self.sdk = self.root / 'SDK ; $ test'
        self.sdk.mkdir()
        self.xcrun = self.root / 'xcrun'
        self.xcrun.write_text('''#!/usr/bin/env python3
import os,sys
print(os.environ['FAKE_COMPILER'] if sys.argv[1:] == ['--find','swiftc'] else os.environ['FAKE_SDK'])
''')
        self.xcrun.chmod(0o700)
        self.analyzer = self.root / 'analyzer'
        self.analyzer.write_text('''#!/usr/bin/env python3
import json,os,sys,time,subprocess
from pathlib import Path
root = str(Path(os.environ['REA_DARWIN_SWIFTC_PATH']).parent)
Path(os.environ['ANALYZER_LOG']).write_text(json.dumps({'argv':sys.argv[1:],'env':dict(os.environ),'root':root,'pid':os.getpid()}))
if os.environ.get('WAIT_FILE'):
 while not Path(os.environ['WAIT_FILE']).exists(): time.sleep(.02)
if os.environ.get('SIGNAL_CHILD'):
 import signal
 os.kill(os.getpid(), signal.SIGTERM)
subprocess.run([os.environ['REA_DARWIN_SWIFTC_PATH'],*sys.argv[1:]],check=True)
sys.exit(int(os.environ.get('ANALYZER_EXIT','0')))
''')
        self.analyzer.chmod(0o700)
        self.diag = self.root / 'diagnostic.json'
        self.diag.write_text(json.dumps({'stderr': DIAG}))
        self.env = dict(os.environ)
        for key in ('SDKROOT','REA_DARWIN_SWIFTC_PATH'):
            self.env.pop(key, None)
        self.env.update(FAKE_COMPILER=str(self.compiler),FAKE_SDK=str(self.sdk),
                        COMPILER_LOG=str(self.root/'compiler.json'), ANALYZER_LOG=str(self.root/'analyzer.json'))
        self.calls = []
        self.owned_roots = set()
        self.before_maps = {p:p.read_bytes() for p in maps.iterdir()}

    def tearDown(self):
        for p,data in self.before_maps.items():
            if p.exists() and p.name != getattr(self,'changed_map',''):
                self.assertEqual(p.read_bytes(),data)
        for owned in self.owned_roots:
            if owned.exists():
                shutil.rmtree(owned)
        self.temp.cleanup()

    def popen(self, argv, **kwargs):
        self.calls.append((list(argv),dict(kwargs)))
        if argv[0] == str(self.analyzer):
            self.owned_roots.add(Path(kwargs['env']['REA_DARWIN_SWIFTC_PATH']).parent)
        self.assertIs(kwargs['shell'],False)
        self.assertIs(kwargs['start_new_session'],True)
        if argv[0] == '/usr/bin/xcrun':
            argv = [str(self.xcrun),*argv[1:]]
        return REAL_POPEN(argv,**kwargs)

    def args(self, *tail):
        return type('Args',(),dict(command=[str(self.analyzer),*tail],diagnostic=str(self.diag),timeout=10,probe_timeout=2))()

    def run_case(self,args=None,env=None,runner=None):
        original_make=rea.tempfile.mkdtemp
        def make(*a,**kw):
            root=original_make(*a,**kw); self.owned_roots.add(Path(root)); return root
        with mock.patch.object(rea.platform,'system',return_value='Darwin'), mock.patch.object(rea.subprocess,'Popen',side_effect=self.popen), mock.patch.object(rea.tempfile,'mkdtemp',side_effect=make):
            return rea.execute(args or self.args(), runner or rea.Runner(), env or self.env)

    def wait_log(self,path):
        end=time.monotonic()+5
        while time.monotonic()<end:
            try: return json.loads(Path(path).read_text())
            except (OSError,ValueError): time.sleep(.02)
        self.fail('child log did not arrive')

    def test_exact_argv_overlay_and_cache_preservation(self):
        cache=self.root/'custom cache'; cache.mkdir(); sentinel=cache/'sentinel'; sentinel.write_text('keep')
        self.env.update(REA_DARWIN_MODULE_CACHE_PATH=str(cache), CLANG_MODULE_CACHE_PATH=str(cache/'clang'))
        args=['space arg', "quote'\"",'$HOME;$(touch bad)']
        self.assertEqual(self.run_case(self.args(*args)),0)
        log=self.wait_log(self.env['ANALYZER_LOG']); compiler=json.loads(Path(self.env['COMPILER_LOG']).read_text())
        self.assertEqual(log['argv'],args)
        self.assertEqual(compiler[0],'-vfsoverlay'); self.assertEqual(compiler[2:5],['-Xcc','-ivfsoverlay','-Xcc'])
        self.assertEqual(compiler[1],compiler[5]); self.assertEqual(compiler[6:],args)
        for key,value in self.env.items():
            self.assertEqual(log['env'][key],value)
        self.assertEqual(log['env']['SDKROOT'],str(self.sdk))
        self.assertFalse(Path(log['root']).exists()); self.assertEqual(sentinel.read_text(),'keep')
        self.assertEqual([c[0] for c in self.calls[:2]],[['/usr/bin/xcrun','--find','swiftc'],['/usr/bin/xcrun','--show-sdk-path']])

    def test_overlay_exactly_one_owned_empty_mapping(self):
        release=self.root/'release'; self.env['WAIT_FILE']=str(release)
        with concurrent.futures.ThreadPoolExecutor() as pool:
            future=pool.submit(self.run_case)
            log=self.wait_log(self.env['ANALYZER_LOG']); root=Path(log['root'])
            overlay=json.loads((root/'overlay.json').read_text())
            self.assertEqual(overlay['version'],0); self.assertEqual(len(overlay['roots']),1)
            item=overlay['roots'][0]; self.assertEqual(item['name'],str(self.maps/'module.modulemap'))
            self.assertEqual(Path(item['external-contents']).parent,root)
            self.assertEqual(Path(item['external-contents']).read_bytes(),b'')
            release.touch(); self.assertEqual(future.result(timeout=5),0)
        self.assertFalse(root.exists())

    def test_rejects_non_darwin(self):
        with mock.patch.object(rea.platform,'system',return_value='Linux'), mock.patch.object(rea,'discover') as discovery:
            with self.assertRaisesRegex(rea.Refused,'Darwin'): rea.execute(self.args(),rea.Runner(),self.env)
            discovery.assert_not_called()

    def test_refuses_custom_selectors_before_discovery(self):
        for key in ('SDKROOT','REA_DARWIN_SWIFTC_PATH'):
            with self.subTest(key=key), mock.patch.object(rea.platform,'system',return_value='Darwin'), mock.patch.object(rea,'discover') as discovery:
                with self.assertRaisesRegex(rea.Refused,key): rea.execute(self.args(),rea.Runner(),dict(self.env,**{key:'custom'}))
                discovery.assert_not_called()

    def test_rejects_absent_executable(self):
        args=self.args(); args.command=['/does/not/exist']
        with self.assertRaisesRegex(rea.Refused,'executable'): self.run_case(args)
        self.assertEqual(self.calls,[])

    def test_refuses_missing_selected_compiler_or_sdk(self):
        for key in ('FAKE_COMPILER','FAKE_SDK'):
            env=dict(self.env,**{key:str(self.root/'absent')})
            with self.subTest(key=key), self.assertRaisesRegex(rea.Refused,'absent'):
                self.run_case(env=env)
        self.assertFalse(Path(self.env['ANALYZER_LOG']).exists())

    def test_io_failure_settles_root_retains_uncertain_state(self):
        original=self.popen; roots=[]; children=[]
        def popen(argv,**kwargs):
            child=original(argv,**kwargs)
            if argv[0]==str(self.analyzer):
                roots.append(Path(kwargs['env']['REA_DARWIN_SWIFTC_PATH']).parent)
                children.append(child)
                communicate=child.communicate
                first=[True]
                def fail_once(*a,**kw):
                    if first:
                        first.pop()
                        raise OSError('injected pipe failure')
                    return communicate(*a,**kw)
                child.communicate=fail_once
            return child
        with mock.patch.object(rea.platform,'system',return_value='Darwin'),mock.patch.object(rea.subprocess,'Popen',side_effect=popen):
            with self.assertRaisesRegex(OSError,'pipe failure'):
                rea.execute(self.args(),rea.Runner(),dict(self.env,WAIT_FILE=str(self.root/'never')))
        self.assertIsNotNone(children[0].poll()); self.assertTrue(roots[0].exists())
        self.assertFalse(rea.Runner.group_alive(children[0].pid))

    def test_diagnostic_requires_exact_error(self):
        for text in ('could not build Foundation', "note: redefinition of module 'SwiftBridging'", "error: redefinition of module 'Other'",''):
            self.diag.write_text(text)
            with self.assertRaisesRegex(rea.Refused,'diagnostic'): self.run_case()
            self.assertFalse(Path(self.env['ANALYZER_LOG']).exists())

    def test_refuses_missing_or_extra_or_different_map(self):
        path=self.maps/'module.modulemap'; self.changed_map=path.name
        for text in (MAP+'module Other {}',MAP.replace('bridging','other'), MAP+'extern module Other "x"'):
            path.write_text(text)
            with self.assertRaises(rea.Refused): self.run_case()
        path.unlink()
        with self.assertRaises(OSError): self.run_case()
        self.assertFalse(Path(self.env['ANALYZER_LOG']).exists())

    def test_probe_signature_and_timeout_fail_closed(self):
        args=self.args(); args.diagnostic=None
        for status,diag in ((1,DIAG),(1,'error: Foundation missing'),(124,DIAG),(0,DIAG)):
            runner=rea.Runner(); original=runner.process
            def process(argv,env,timeout,capture=False,**kwargs):
                if '-typecheck' in argv: return status,'',diag
                return original(argv,env,timeout,capture,**kwargs)
            runner.process=process
            if status==1 and diag==DIAG:
                self.assertEqual(self.run_case(args,runner=runner),125)
                self.assertTrue(any(root.exists() for root in self.owned_roots))
            else:
                with self.assertRaises(rea.Refused): self.run_case(args,runner=runner)

    def test_nonzero_and_child_signal(self):
        self.assertEqual(self.run_case(env=dict(self.env,ANALYZER_EXIT='23')),23)
        self.assertEqual(self.run_case(env=dict(self.env,SIGNAL_CHILD='1')),-signal.SIGTERM)

    def test_spawn_failure_cleans_own_state(self):
        original=self.popen; roots=[]
        def popen(argv,**kwargs):
            if argv[0]==str(self.analyzer):
                roots.append(Path(kwargs['env']['REA_DARWIN_SWIFTC_PATH']).parent)
                raise OSError('injected spawn failure')
            return original(argv,**kwargs)
        with mock.patch.object(rea.platform,'system',return_value='Darwin'),mock.patch.object(rea.subprocess,'Popen',side_effect=popen):
            with self.assertRaisesRegex(OSError,'spawn'): rea.execute(self.args(),rea.Runner(),self.env)
        self.assertEqual(len(roots),1); self.assertFalse(roots[0].exists())

    def test_cleanup_error_is_visible_non_success(self):
        roots=[]; original=rea.shutil.rmtree
        def fail(path): roots.append(Path(path)); raise OSError('injected cleanup failure')
        with mock.patch.object(rea.shutil,'rmtree',side_effect=fail):
            with self.assertRaisesRegex(rea.Refused,'cleanup'): self.run_case()
        self.assertTrue(roots[0].exists()); original(roots[0])

    def test_uncertain_settlement_retains_owned_state(self):
        runner=rea.Runner(); original=runner.process
        def process(argv,env,timeout,capture=False,**kwargs):
            if argv[0]==str(self.analyzer): raise rea.Unsettled('injected uncertain group')
            return original(argv,env,timeout,capture,**kwargs)
        runner.process=process; roots=[]; original_mkdtemp=rea.tempfile.mkdtemp
        def make(*a,**kw):
            path=original_mkdtemp(*a,**kw); roots.append(Path(path)); return path
        with mock.patch.object(rea.tempfile,'mkdtemp',side_effect=make):
            with self.assertRaises(rea.Unsettled): self.run_case(runner=runner)
        self.assertTrue(roots[0].exists()); rea.shutil.rmtree(roots[0])

    def test_concurrent_live_roots_disjoint_foreign_survives(self):
        release=self.root/'release'; sentinel=self.root/'foreign'; sentinel.write_text('untouched')
        envs=[dict(self.env,WAIT_FILE=str(release),ANALYZER_LOG=str(self.root/('log'+str(i))),COMPILER_LOG=str(self.root/('comp'+str(i)))) for i in range(2)]
        # One shared patch; independent real subprocesses overlap behind release.
        with mock.patch.object(rea.platform,'system',return_value='Darwin'),mock.patch.object(rea.subprocess,'Popen',side_effect=self.popen),concurrent.futures.ThreadPoolExecutor() as pool:
            futures=[pool.submit(rea.execute,self.args(),rea.Runner(),env) for env in envs]
            roots=[Path(self.wait_log(env['ANALYZER_LOG'])['root']) for env in envs]
            self.assertNotEqual(roots[0],roots[1]); self.assertTrue(all(r.exists() for r in roots))
            release.touch(); self.assertEqual([f.result(timeout=5) for f in futures],[0,0])
        self.assertTrue(all(not r.exists() for r in roots)); self.assertEqual(sentinel.read_text(),'untouched')

    def test_actual_caller_sigint_settles_root_retains_uncertain_state(self):
        helper=self.root/'entry.py'
        helper.write_text('''import importlib.util,os,platform,runpy,subprocess,sys
real=subprocess.Popen
def popen(argv,**kw):
 if argv[0]=='/usr/bin/xcrun': argv=[os.environ['FAKE_XCRUN'],*argv[1:]]
 return real(argv,**kw)
subprocess.Popen=popen
platform.system=lambda:'Darwin'
runpy.run_path(sys.argv.pop(1),run_name='__main__')
''')
        env=dict(self.env,FAKE_XCRUN=str(self.xcrun),WAIT_FILE=str(self.root/'never-release'))
        proc=REAL_POPEN([sys.executable,str(helper),str(SCRIPT),'--diagnostic',str(self.diag),'--',str(self.analyzer)],env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            log=self.wait_log(env['ANALYZER_LOG']); root=Path(log['root']); self.owned_roots.add(root)
            os.kill(proc.pid,signal.SIGINT); out,err=proc.communicate(timeout=8)
            self.assertEqual(proc.returncode,-signal.SIGINT,(out,err)); self.assertTrue(root.exists())
            self.assertIn('native descendant settlement is unverified',err)
            with self.assertRaises(ProcessLookupError): os.kill(log['pid'],0)
        finally:
            if proc.poll() is None: proc.kill(); proc.wait()

    def test_escaped_native_group_survives_failure_state_is_retained(self):
        escaped=self.root/'escaped.py'
        escaped.write_text("import os,sys,time\nfrom pathlib import Path\nPath(sys.argv[1]).write_text(str(os.getpid()))\nwhile True: time.sleep(.1)\n")
        pidfile=self.root/'escaped-pid'
        # An analyzer-spawned native job deliberately starts another session.
        self.analyzer.write_text("#!/usr/bin/env python3\nimport os,subprocess,sys,time,json\nfrom pathlib import Path\n"+
            "child=subprocess.Popen([sys.executable,"+repr(str(escaped))+","+repr(str(pidfile))+"], start_new_session=True, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)\n"+
            "while not Path("+repr(str(pidfile))+").exists(): time.sleep(.01)\n"+
            "Path(os.environ['ANALYZER_LOG']).write_text(json.dumps({'root':str(Path(os.environ['REA_DARWIN_SWIFTC_PATH']).parent),'pid':os.getpid(),'escaped_pid':child.pid}))\n"+
            "sys.exit(19)\n")
        try:
            self.assertEqual(self.run_case(),19)
            log=self.wait_log(self.env['ANALYZER_LOG']); root=Path(log['root'])
            self.assertTrue(root.exists()); self.assertTrue((root/'overlay.json').exists())
            os.kill(log['escaped_pid'],0)  # Actual surviving separate-group job.
            with self.assertRaises(ProcessLookupError): os.kill(log['pid'],0)
        finally:
            # Test owns the exact stub PID; production never guesses escaped jobs.
            if pidfile.exists():
                try: os.kill(int(pidfile.read_text()),signal.SIGKILL)
                except ProcessLookupError: pass

    def test_probe_decode_error_retains_source_for_actual_escaped_child(self):
        marker=self.root/'decode-observation.json'; pidfile=self.root/'decode-child-pid'
        child_code=("import json,os,time,sys; from pathlib import Path; time.sleep(.5); "
                    "Path("+repr(str(marker))+").write_text(json.dumps({'probe_source_exists':Path(sys.argv[1]).exists(),'pid':os.getpid()}))")
        # The compiler leader exits and closes pipes while a separate-session job
        # still needs probe.swift; invalid output causes communicate() to decode-fail.
        self.compiler.write_text("#!/usr/bin/env python3\nimport os,subprocess,sys\nfrom pathlib import Path\n"+
            "child=subprocess.Popen([sys.executable,'-c',"+repr(child_code)+",sys.argv[-1]],start_new_session=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)\n"+
            "Path("+repr(str(pidfile))+").write_text(str(child.pid))\nos.write(1,b'\\xff')\n")
        args=self.args(); args.diagnostic=None; runner=rea.Runner()
        try:
            with self.assertRaises(UnicodeDecodeError): self.run_case(args,runner=runner)
            self.assertTrue(runner.last_started); self.assertFalse(runner.last_forced_stop)
            self.assertTrue(self.owned_roots)
            self.assertTrue(all((root/'probe.swift').exists() for root in self.owned_roots))
            observed=self.wait_log(marker)
            self.assertTrue(observed['probe_source_exists'])
            self.assertFalse(Path(self.env['ANALYZER_LOG']).exists())
        finally:
            # Only the exact test-owned escaped stub, never a guessed process.
            if pidfile.exists():
                try: os.kill(int(pidfile.read_text()),signal.SIGKILL)
                except ProcessLookupError: pass

    def test_compiler_probe_timeout_uses_sigint_and_retains_state(self):
        args=self.args(); args.diagnostic=None
        self.compiler.write_text("#!/usr/bin/env python3\nimport os,signal,time\nfrom pathlib import Path\nsignal.signal(signal.SIGINT,lambda *a: (Path(os.environ['COMPILER_LOG']).write_text('SIGINT'),exit(3)))\nwhile True: time.sleep(.02)\n")
        args.probe_timeout=.3
        with self.assertRaises(rea.Refused): self.run_case(args)
        self.assertEqual(Path(self.env['COMPILER_LOG']).read_text(),'SIGINT')
        self.assertTrue(any(root.exists() for root in self.owned_roots))
        self.assertFalse(Path(self.env['ANALYZER_LOG']).exists())

    def test_timeout_settles_root_and_retains_uncertain_state(self):
        args=self.args(); args.timeout=.2
        self.assertEqual(self.run_case(args,dict(self.env,WAIT_FILE=str(self.root/'never'))),124)
        log=self.wait_log(self.env['ANALYZER_LOG']); self.assertTrue(Path(log['root']).exists())
        with self.assertRaises(ProcessLookupError): os.kill(log['pid'],0)


class PortableGuardTests(unittest.TestCase):
    """No shebang execution, sessions, killpg or platform executables required."""
    def args(self):
        return type('Args',(),dict(command=[sys.executable], diagnostic=None, timeout=1,probe_timeout=1))()

    def test_os_refusal_precedes_any_process_or_temp_state(self):
        with mock.patch.object(rea.platform,'system',return_value='Windows'), mock.patch.object(rea,'discover') as discover, mock.patch.object(rea.tempfile,'mkdtemp') as make:
            with self.assertRaisesRegex(rea.Refused,'Darwin'):
                rea.execute(self.args(),rea.Runner(),{})
            discover.assert_not_called(); make.assert_not_called()

    def test_custom_selectors_refused_before_discovery(self):
        for key in ('REA_DARWIN_SWIFTC_PATH','SDKROOT'):
            with self.subTest(key=key), mock.patch.object(rea.platform,'system',return_value='Darwin'),mock.patch.object(rea,'discover') as discover:
                with self.assertRaisesRegex(rea.Refused,key):
                    rea.execute(self.args(),rea.Runner(),{key:'custom'})
                discover.assert_not_called()

    def test_precise_diagnostic_and_nested_json(self):
        self.assertTrue(rea.diagnostic_matches(DIAG))
        self.assertTrue(rea.diagnostic_matches(json.dumps({'nested':[{'stderr':DIAG}]})))
        for text in ('Foundation failed', "note: redefinition of module 'SwiftBridging'", "error: redefinition of module 'Other'"):
            self.assertFalse(rea.diagnostic_matches(text))

    def test_module_parser_rejects_additional_declarations(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'module.modulemap'; path.write_text('// harmless comment\n'+MAP)
            self.assertTrue(rea.module_definition(path))
            for text in (MAP+'module Other {}',MAP.replace('bridging','other'),MAP+'extern module Other "x"'):
                path.write_text(text)
                with self.assertRaises(rea.Refused): rea.module_definition(path)

    def test_finite_bounded_timeouts(self):
        self.assertEqual(rea.positive_seconds('60'),60)
        for text in ('0','-1','nan','inf','3601'):
            with self.assertRaises(rea.argparse.ArgumentTypeError): rea.positive_seconds(text)


if __name__=='__main__': unittest.main()
