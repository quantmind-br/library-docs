---
title: Leak Debugging | Camoufox
url: https://camoufox.com/development/workflow/
source: crawler
fetched_at: 2026-02-14T14:05:45.45763-03:00
rendered_js: true
word_count: 110
summary: This document outlines a systematic debugging process for identifying browser leaks that trigger WAF detection by incrementally applying Camoufox patches to a vanilla Firefox build.
tags:
    - browser-fingerprinting
    - waf-evasion
    - camoufox
    - firefox-build
    - bot-detection
    - debugging
    - web-scraping
category: guide
---

This is a flow chart demonstrating my process for determining leaks without deobfuscating WAF Javascript. The method incrementally reintroduces Camoufox's features into Firefox's source code until the testing site flags.

This process requires a Linux system and assumes you have Firefox build tools installed (see [here](https://github.com/daijro/camoufox?tab=readme-ov-file#build-cli)).

* * *

## [#](#flowchart)Flowchart

```
YesNoYesNoNoYesNoYesYesNoNoYesStartDoes website flag in the
official Firefox?Likely bad IP/rate-
limiting. If the website
fails on both headless and
headful mode on the official
Firefox distribution, the
issue is not with the browser.Run make ff-dbg(1) and
build(2) a clean
distribution of Firefox.
Does the website flag in
Firefox headless mode(4)?Does the website flag in
headful mode(3) AND
headless mode(4)?Open the developer UI(5),
apply config.patch, then
rebuild(2). Does the
website still flag(3)?Enable privacy.resistFingerprinting
in the config(6). Does the
website still flag(3)?In the config(6), enable
FPP and start omitting
overrides until you find
the one that fixed the leak.If you get to this point,
you may need to deobfuscate
the Javascript behind the website
to identify what it's testing.Open the developer UI,
apply the playwright
bootstrap patch, then
rebuild. Does it still flag?Omit options from
camoufox.cfg(6) and
rerun(3) until you find the
one causing the leak.Juggler needs to be
debugged to locate the leak.The issue has nothing to do
with Playwright. Apply the
rest of the Camoufox patches
one by one until the one
causing the leak is found.
```

* * *

## [#](#cited-commands)Cited Commands

#CommandDescription(1)`make ff-dbg`Setup vanilla Firefox with minimal patches.(2)`make build`Build the source code.(3)`make run`Runs the built browser.(4)`make run args="--headless https://test.com"`Run a URL in headless mode. All redirects will be printed to the console to determine if the test passed.(5)`make edits`Opens the developer UI. Allows the user to apply/undo patches, and see which patches are currently applied.(6)`make edit-cfg`Edit camoufox.cfg in the default system editor.