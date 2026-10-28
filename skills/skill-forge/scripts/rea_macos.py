#!/usr/bin/env python3
"""Explicit, guarded process-local workaround for duplicate SwiftBridging maps.

No package acquisition, Apple-file edits, cache removal or ownership bypass.
Python 3.9+. Cold Swift compilation can take several minutes.
"""
import argparse
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time


class Refused(RuntimeError):
    pass


class Unsettled(Refused):
    pass


class Runner:
    def __init__(self):
        self.interrupted = None
        self.last_started = False
        self.last_forced_stop = False

    def on_signal(self, signum, frame):
        self.interrupted = signum

    @staticmethod
    def group_alive(pid):
        try:
            os.killpg(pid, 0)
            return True
        except ProcessLookupError:
            return False
        except PermissionError:
            return True

    def process(self, argv, env, timeout, capture=False, timeout_signal=signal.SIGTERM):
        """Settle the owned root group; escaped native jobs remain unverified."""
        self.last_started = False
        self.last_forced_stop = False
        if self.interrupted:
            return -self.interrupted, "", ""
        child = subprocess.Popen(argv, env=env, shell=False, start_new_session=True,
                                 stdout=subprocess.PIPE if capture else None,
                                 stderr=subprocess.PIPE if capture else None,
                                 text=True)
        self.last_started = True
        start = time.monotonic()
        reason = None
        output = (None, None)
        error = None
        try:
            while True:
                if self.interrupted:
                    reason = -self.interrupted
                    break
                if time.monotonic() - start >= timeout:
                    reason = 124
                    break
                try:
                    output = child.communicate(timeout=min(.1, timeout))
                    break
                except subprocess.TimeoutExpired:
                    pass
        except BaseException as exc:
            # Even an I/O/decode failure must not skip owned-process settlement.
            error = exc
        # Pipe closure/leader exit alone is insufficient even for the root group.
        # Native jobs may escape it; execute() retains state on unsuccessful paths.
        if child.poll() is None or self.group_alive(child.pid):
            self.last_forced_stop = True
            first_signal = self.interrupted or (timeout_signal if reason == 124 else signal.SIGTERM)
            for sig, grace in ((first_signal, 2.0), (signal.SIGKILL, 2.0)):
                try:
                    os.killpg(child.pid, sig)
                except ProcessLookupError:
                    pass
                deadline = time.monotonic() + grace
                while time.monotonic() < deadline:
                    try:
                        output = child.communicate(timeout=.1)
                    except subprocess.TimeoutExpired:
                        continue
                    except (OSError, UnicodeError):
                        try:
                            child.wait(timeout=.1)
                        except subprocess.TimeoutExpired:
                            continue
                    if not self.group_alive(child.pid):
                        break
                    time.sleep(.02)
                if child.poll() is not None and not self.group_alive(child.pid):
                    break
            else:
                raise Unsettled("owned process group could not be confirmed settled; temporary state retained")
        if error is not None:
            raise error
        if reason == 124:
            print("rea-macos: command timed out", file=sys.stderr)
        return reason if reason is not None else child.returncode, output[0] or "", output[1] or ""


def module_definition(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"/\*.*?\*/|//[^\n]*", "", text, flags=re.S)
    # Intentionally recognize only the known redundant map, no other declarations.
    if not re.fullmatch(r'\s*module\s+SwiftBridging\s*\{\s*header\s+"bridging"\s+export\s+\*\s*\}\s*', text):
        raise Refused("modulemap is not the sole known SwiftBridging definition: " + str(path))
    return re.sub(r"\s+", "", text)


def diagnostic_matches(text):
    # JSON captures are accepted by recursively inspecting strings, never executing them.
    try:
        value = json.loads(text)
    except ValueError:
        value = text
    def strings(item):
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            for val in item.values():
                yield from strings(val)
        elif isinstance(item, list):
            for val in item:
                yield from strings(val)
    return any(re.search(r"\berror:\s*redefinition of module ['\"]SwiftBridging['\"]", s)
               for s in strings(value))


def discover(runner, env):
    found = []
    for args in (("--find", "swiftc"), ("--show-sdk-path",)):
        status, out, err = runner.process(["/usr/bin/xcrun", *args], env, 10, True)
        if status:
            raise Refused("xcrun discovery failed: " + err.strip())
        path = Path(out.strip())
        if not path.is_absolute():
            raise Refused("xcrun did not return an absolute path")
        found.append(path)
    compiler, sdk = found
    if not compiler.is_file() or not os.access(compiler, os.X_OK) or not sdk.is_dir():
        raise Refused("selected swiftc executable or SDK is absent")
    maps = compiler.parent.parent / "include" / "swift"
    redundant, retained = maps / "module.modulemap", maps / "bridging.modulemap"
    if module_definition(redundant) != module_definition(retained):
        raise Refused("SwiftBridging modulemap definitions do not match")
    return compiler, sdk, redundant


def execute(args, runner, env=None):
    env = dict(os.environ if env is None else env)
    if platform.system() != "Darwin":
        raise Refused("this workaround requires Darwin")
    for key in ("REA_DARWIN_SWIFTC_PATH", "SDKROOT"):
        if env.get(key):
            raise Refused("refusing existing nonempty " + key + "; rerun in an intentionally configured environment")
    if not args.command or shutil.which(args.command[0], path=env.get("PATH")) is None:
        raise Refused("command executable is absent")
    if shutil.which("python3", path=env.get("PATH")) is None:
        raise Refused("python3 launcher is absent from PATH")
    compiler, sdk, redundant = discover(runner, env)
    # Unique owned state only. Never remove a caller cache or a shared directory.
    root = Path(tempfile.mkdtemp(prefix="rea-macos-"))
    result = 125
    uncertain = False
    phase = "guard"
    try:
        if args.diagnostic:
            diagnostic = Path(args.diagnostic).read_text(encoding="utf-8")
        else:
            source = root / "probe.swift"
            source.write_text("import Foundation\n", encoding="utf-8")
            phase = "probe"
            status, out, diagnostic = runner.process(
                [str(compiler), "-sdk", str(sdk), "-typecheck", str(source)],
                env, args.probe_timeout, True, timeout_signal=signal.SIGINT)
            # Even a recognized compiler failure does not establish that its
            # separate-group native jobs released the probe source/state.
            if status != 0 or runner.last_forced_stop:
                uncertain = True
            if status <= 0 or status == 124 or runner.last_forced_stop:
                raise Refused("selected compiler probe did not establish the known duplicate diagnostic")
        if runner.interrupted:
            return -runner.interrupted
        if not diagnostic_matches(diagnostic):
            raise Refused("diagnostic is not the known SwiftBridging redefinition error")
        empty = root / "empty.modulemap"
        empty.write_text("", encoding="utf-8")
        overlay = root / "overlay.json"
        overlay.write_text(json.dumps({"version": 0, "roots": [
            {"type": "file", "name": str(redundant), "external-contents": str(empty)}]}), encoding="utf-8")
        trampoline = root / "swiftc"
        # A short PATH-based Python shebang avoids kernel shebang limits and spaces
        # in sys.executable. Compiler and all forwarded arguments remain argv data.
        trampoline.write_text("#!/usr/bin/env python3\nimport os, sys\nos.execv(" +
                              repr(str(compiler)) + ", [" + repr(str(compiler)) +
                              ", '-vfsoverlay', " + repr(str(overlay)) +
                              ", '-Xcc', '-ivfsoverlay', '-Xcc', " + repr(str(overlay)) +
                              "] + sys.argv[1:])\n", encoding="utf-8")
        trampoline.chmod(0o700)
        selected = dict(env, REA_DARWIN_SWIFTC_PATH=str(trampoline), SDKROOT=str(sdk))
        phase = "analyzer"
        result, _, _ = runner.process(args.command, selected, args.timeout)
        # REA documents Swift frontends with separate process groups. Root-group
        # disappearance is not proof that native descendants released this state.
        if result != 0 or runner.last_forced_stop:
            uncertain = True
        if uncertain and result == 0:
            result = 125
    except BaseException as exc:
        if (isinstance(exc, Unsettled) or (phase == "analyzer" and runner.last_started)
                or (phase == "probe" and runner.last_started)):
            uncertain = True
        raise
    finally:
        if not uncertain:
            try:
                shutil.rmtree(root)
            except OSError as exc:
                print("rea-macos: cleanup failed; state retained at " + str(root) + ": " + str(exc), file=sys.stderr)
                # A finally exception ensures an earlier return cannot report success.
                raise Refused("temporary-state cleanup failed") from exc
        else:
            print("rea-macos: native descendant settlement is unverified; temporary state retained at " + str(root), file=sys.stderr)
    return result


def positive_seconds(value):
    number = float(value)
    if not math.isfinite(number) or not 0 < number <= 3600:
        raise argparse.ArgumentTypeError("timeout must be finite and between 0 and 3600 seconds")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostic", metavar="FILE", help="known actual stderr or JSON capture; otherwise bounded Foundation probe")
    parser.add_argument("--timeout", type=positive_seconds, default=600, help="command seconds (default 600; cold Swift startup can take minutes)")
    parser.add_argument("--probe-timeout", type=positive_seconds, default=60, help="probe seconds (default 60)")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="-- COMMAND ARGS (already installed/authorized command)")
    args = parser.parse_args(argv)
    if args.command[:1] == ["--"]:
        args.command = args.command[1:]
    runner = Runner()
    saved = {sig: signal.signal(sig, runner.on_signal) for sig in (signal.SIGINT, signal.SIGTERM)}
    try:
        try:
            result = execute(args, runner)
        except (OSError, Refused) as exc:
            print("rea-macos: " + str(exc), file=sys.stderr)
            result = 125
        return -runner.interrupted if runner.interrupted else result
    finally:
        for sig, handler in saved.items():
            signal.signal(sig, handler)


if __name__ == "__main__":
    code = main()
    if code < 0:
        sig = -code
        signal.signal(sig, signal.SIG_DFL)
        os.kill(os.getpid(), sig)
    sys.exit(code)
