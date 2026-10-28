# Guarded REA macOS compiler workaround

Use only after actual `error: redefinition of module 'SwiftBridging'` blocks an authorized installed REA analysis. Ordinary complete-source inspection still uses file/search tools. This Python 3.9+ utility refuses other errors, non-Darwin hosts, missing/mismatching maps, additional map declarations, absent executables, and existing nonempty `REA_DARWIN_SWIFTC_PATH` or `SDKROOT`. It discovers the selected compiler and SDK using `/usr/bin/xcrun`. Without `--diagnostic`, it first runs a bounded Foundation compiler probe; a supplied file must contain actual stderr or JSON capturing that known error.

From the skill directory:

```text
python3 scripts/rea_macos.py --diagnostic /absolute/path/actual-stderr.txt -- /absolute/path/to/rea analyze-javascript-application /absolute/path/to/extracted-app --format json
```

Only when package acquisition is separately authorized, the pinned package runner may be the command:

```text
python3 scripts/rea_macos.py --diagnostic /absolute/path/actual-stderr.txt -- npm exec --yes --package=node@24.22.1 --package=rea-agents@6.8.0 -- rea analyze-javascript-application /absolute/path/to/extracted-app --format json
```

No package acquisition occurs in the utility itself. Inspect the installed version/help and REA's supported Node requirements first. Native inspection still requires the host's actual process-inspection permissions. This does not change security policy, install providers, or promise to repair other compiler/REA errors.

The runner verifies both selected-toolchain maps are solely the matching known SwiftBridging definition, then overlays only redundant `module.modulemap` with a unique owned empty file. It retains `bridging.modulemap`. A generated Python executable forwards real compiler argv using `os.execv`, with `-vfsoverlay FILE -Xcc -ivfsoverlay -Xcc FILE`; the short `/usr/bin/env python3` launcher avoids space/length limits in the calling interpreter path. Keep the intended Python 3 on PATH. Apple files and REA's native ownership helper remain unchanged. Child-only `REA_DARWIN_SWIFTC_PATH` and `SDKROOT` select that compiler; no global environment/configuration is written.

All other environment values, including custom `REA_DARWIN_MODULE_CACHE_PATH` and `CLANG_MODULE_CACHE_PATH`, pass unchanged. REA itself may suppress `CLANG_MODULE_CACHE_PATH` when its supported cache selector is empty. The utility never removes caches. Default REA caches can persist as REA normally manages them.

Stdout/stderr stream directly, preserving REA JSON stdout. Nonzero exits and signals remain failures. `--timeout` defaults to 600 seconds; `--probe-timeout` to 60 (each accepts at most 3600). Cold Swift startup can take minutes, so raise the explicit probe limit if needed. Discovery is bounded at 10 seconds per command. On interruption/timeout, only the owned root process group is signaled, with two bounded settlement waits of two seconds; compiler-probe timeout starts with SIGINT. REA documents Swift frontend jobs using separate process groups, so disappearance of the root group cannot establish native descendant settlement. On failed/interrupted/timed-out or forcibly stopped analyzer runs, the utility preserves its unique temporary state and explicitly reports that native descendant settlement remains unverified, while preserving the original failure or signal. A forced-stop path cannot report success. Any nonzero compiler-probe exit also leaves native descendant settlement unverified, including a recognized duplicate error. Its dependent state is retained; if the later analyzer succeeds, unresolved probe uncertainty still makes the utility exit nonzero. A supplied actual diagnostic avoids launching that probe. Probe forced-stop paths and any exception after compiler launch retain their state as well, even when the compiler leader has already exited. It never guesses or signals escaped process groups. A normal REA exit zero retains REA's native ownership/cleanup behavior; confirm its actual cleanup evidence before claiming success. Cleanup errors remain visible failures. No custom caches or foreign files are deleted. Retained state can be removed only after separately establishing that the native work has ended.

Static REA output does not prove runtime execution. Verify actual imports/functions/source hashes and ranges; a source-backed ternary interpretation is not an invented REA branch edge or resolved inter-module call. Preserve unknown-call and static-only limits.

Overlay strategy reference: [Tobias Franks's pinned build.sh](https://github.com/tobias-x/screentime-archive/blob/27fb07e3edb0f715c1e187fc41e6cb0458d63ab1/build.sh), [MIT license at the same commit](https://github.com/tobias-x/screentime-archive/blob/27fb07e3edb0f715c1e187fc41e6cb0458d63ab1/LICENSE). This utility is independently implemented; the complete notice is [retained conservatively](rea-macos-license.txt).
