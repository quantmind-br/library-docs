---
title: Stealth Overview | Camoufox
url: https://camoufox.com/stealth/
source: crawler
fetched_at: 2026-02-14T14:05:26.836323-03:00
rendered_js: true
word_count: 937
summary: This document explains the technical mechanisms Camoufox uses to evade anti-bot detection, including its use of sandboxing, C++ level fingerprint spoofing, and isolated browser protocols.
tags:
    - camoufox
    - anti-bot-evasion
    - browser-fingerprinting
    - playwright
    - automation-stealth
    - web-scraping
category: concept
---

* * *

## [#](#explanation)Explanation

### [#](#how-camoufox-hides-its-automation-library)How Camoufox hides its automation library

In Camoufox, all of Playwright's internal Page Agent's code is sandboxed and isolated. This makes it impossible for a page to detect the presence of Playwright through Javascript inspection.

Normally, Playwright injects some JavaScript into the page such as `window.__playwright__binding__` and to perform actions like querying elements, evaluating javascript, or running init scripts, which can be detected by websites. In Camoufox, these actions are handled in an isolated scope outside of the page. In other words, websites can no longer "see" any JavaScript that Playwright would typically inject. This prevents traces of Playwright altogether.

However, even with hiding its automation library, Camoufox is not immune to inconsistencies in fingerprint rotation. This still requires maintenance to spot and fix.

#### [#](#page-interactions)Page Interactions

Anti-bot systems also run client-side scripts to monitor your behavior. For example, they look for patterns in mouse movements, clicks, scrolling, and the timing between actions.

Camoufox tries its best with its human-like mouse movement algorithm. The natural motion algorithm was originally from [riflosnake's HumanCursor](https://github.com/riflosnake/HumanCursor) and has been rewritten in C++ and modified for more distance-aware trajectories.

However, this isn't perfect. It may still be detected with sophisticated enough analysis. (WIP for the future)

* * *

### [#](#how-camoufox-rotates-identities)How Camoufox rotates identities

In addition to hiding the automation library, your identity must be randomized in each instance as well to avoid rate limiting and detection. Rotating your IP address means nothing if it's obviously you each time. There are thousands of things that create a unique **fingerprint** of you. Right now, any website you visit can see you are using Chrome on macOS, running on Intel Iris.

Even if you are rotating your IP for each running bot instance, web access firewalls can still use machine learning to analyze incoming web traffic to detect if it's abnormal. If the Linux market share was 5%, then suddenly it's 20%, it's a red flag. They will unconditionally require all Linux users to complete a captcha.

Camoufox uses [BrowserForge](https://github.com/daijro/browserforge)'s fingerprint generator to mimic the statistical distribution of device data in real-world traffic. For example, Camoufox will make your browser look like a Linux user 5% of the time. Of that 5%, it will spoof a 2560x1440 screen resolution 9.5% of the time and an Intel HD GPU 27.5% of the time.

### [#](#how-can-camoufox-be-detected)How can Camoufox be detected?

Camoufox can spoof fingerprints with a correct market share. However, **fingerprints must also be internally consistent.** A Windows user agent with an Apple M1 GPU, a MacOS user agent with a Windows DirectX renderer, and a mobile device with a desktop screen resolution are all impossible, and will be flagged for being suspicious.

Of the thousands of possible datapoints that must be changed to create a believable spoofed fingerprint, where each change must be consistent with the others, Camoufox doesn't always succeed. Anti-bot providers test Camoufox over and over again to find even 1 unique inconsistency, then they immediately update their background scripts to test for it.

* * *

## [#](#how-does-camoufox-compare-to-other-solutions)How does Camoufox compare to other solutions?

* * *

### [#](#javascript-based-solutions)JavaScript-based solutions

In the past, developers tried injecting JavaScript to spoof these values, but it doesn't work reliably since JavaScript can't spoof everything. Incomplete coverage causes inconsistent fingerprints. For example, an anti-bot system will flag you if your network request's User Agent doesn't match your navigator's User Agent.

Additionally, all injected JavaScript is detectable in some way. Anti-bot systems can check if `Object.getOwnPropertyDescriptor` reveals an overwritten property, if a function's `toString()` no longer returns `[native code]` (revealing it was hijacked), or if data in the window context doesn't match the worker thread context. Workarounds only take you so far, but there will always be a way to detect JS injection if you search deep enough.

#### [#](#camoufoxs-approach)Camoufox's approach

Since Camoufox intercepts calls in the browser's C++ implementation level, all of the hijacked objects and properties appear native. There is no JavaScript hijacking to be detected.

Camoufox also attempts to generate consistent and believable fingerprints with Browserforge as well. However, this can still be detected by complex fingerprint detection methods like mismatching data (as described earlier).

* * *

### [#](#cdp-based-libraries)CDP-based libraries

CDP (Chrome DevTools Protocol) is an automation protocol built into Chromium and Firefox. However, CDP makes no effort to hide the fact that it's an automation protocol and exposes much of its functionality in the page scope. Some common methods are checking if `navigator.webdriver` is true, catching it reading the stack debugger, checking for variables that ChromeDriver injects into the document object for internal communication, and more.

#### [#](#camoufoxs-approach-1)Camoufox's approach

While Playwright uses CDP to control Chromium, it uses *Juggler* for Firefox. Juggler is a custom protocol developed before Firefox supported CDP ([original repo](https://github.com/puppeteer/juggler) ). It is a distinct module within Firefox, and not part of its core browser. This makes it easier to edit and control what's revealed to the page.

Camoufox patches Juggler to give it its own isolated "copy" of the page to work with. Playwright can read and edit its own version of the page freely. Everything appears to work normally to it, but the real page is completely unaffected by these changes. The page also can't detect when things are being read (through tricks like hijacking getters) or listeners being added to watch elements.

Additionally, Juggler sends its inputs directly through the Firefox's original user input handlers, meaning they are handled the exact same way as if you were using the browser normally. Camoufox also patches Firefox's headless mode to appear the same as if it were running in a normal window. But as a fallback, the Python library can run Camoufox in a [virtual display](https://camoufox.com/python/virtual-display/) if headless mode ever leaks.

* * *

Thanks for reading.  
\- daijro. 2026