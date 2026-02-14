---
title: Features List | Camoufox
url: https://camoufox.com/features/
source: crawler
fetched_at: 2026-02-14T14:05:33.278153-03:00
rendered_js: true
word_count: 496
summary: This document outlines the features and technical patches of Camoufox, a modified Firefox browser designed for anti-fingerprinting, stealth automation, and performance optimization.
tags:
    - camoufox
    - anti-fingerprinting
    - stealth-browsing
    - web-automation
    - playwright
    - privacy-tools
    - browser-spoofing
category: reference
---

Below is a list of patches and features implemented in Camoufox.

* * *

### [#](#fingerprint-spoofing)Fingerprint spoofing

- Navigator properties spoofing (device, browser, locale, etc.)
- Support for emulating screen size, resolution, etc.
- Spoof WebGL parameters, supported extensions, context attributes, and shader precision formats.
- Spoof inner and outer window viewport sizes
- Spoof AudioContext sample rate, output latency, and max channel count
- Spoof device voices & playback rates
- Spoof the amount of microphones, webcams, and speakers available.
- Network headers (Accept-Languages and User-Agent) are spoofed to match the navigator properties
- WebRTC IP spoofing at the protocol level
- Geolocation, timezone, and locale spoofing
- Battery API spoofing
- etc.

### [#](#stealth-patches)Stealth patches

- Avoids main world execution leaks. All page agent javascript is sandboxed
- Avoids frame execution context leaks
- Fixes `navigator.webdriver` detection
- Fixes Firefox headless detection via pointer type ([#26](https://github.com/daijro/camoufox/issues/26))
- Removed potentially leaking anti-zoom/meta viewport handling patches
- Uses non-default screen & window sizes
- Re-enable fission content isolations
- Re-enable PDF.js
- Other leaking config properties changed
- Human-like cursor movement

### [#](#anti-font-fingerprinting)Anti font fingerprinting

- Automatically uses the correct system fonts for your User Agent
- Bundled with Windows, Mac, and Linux system fonts
- Prevents font metrics fingerprinting by randomly offsetting letter spacing

### [#](#playwright-support)Playwright support

- Custom implementation of Playwright for the latest Firefox
- Various config patches to evade bot detection

### [#](#debloatoptimizations)Debloat/Optimizations

- Stripped out/disabled *many, many* Mozilla services. Runs faster than the original Mozilla Firefox, and uses less memory (200mb)
- Patches from LibreWolf & Ghostery to help remove telemetry & bloat
- Debloat config from PeskyFox, LibreWolf, and others
- Speed & network optimizations from FastFox
- Removed all CSS animations
- Minimalistic theming
- etc.

### [#](#addons)Addons

- Load Firefox addons without a debug server by passing a list of paths to the `addons` property
- Added uBlock Origin with custom privacy filters
- Addons are not allowed to open tabs
- Addons are automatically enabled in Private Browsing mode
- Addons are automatically pinned to the toolbar
- Fixes DNS leaks with uBO prefetching

### [#](#python-interface)Python Interface

- Automatically generates & injects unique device characteristics into Camoufox based on their real-world distribution
- WebGL fingerprint injection & rotation
- Uses the correct system fonts and subpixel antialiasing & hinting based on your target OS
- Avoid proxy detection by calculating your target geolocation, timezone, & locale from your proxy's target region
- Calculate and spoof the browser's language based on the distribution of language speakers in the proxy's target region
- Remote server hosting to use Camoufox with other languages that support Playwright
- Built-in virtual display buffer to run Camoufox headfully on a headless server
- Toggle image loading, WebRTC, and WebGL
- etc.

* * *

### [#](#thanks-heart)Thanks ❤️

The design and implementation of Camoufox was inspired by the following projects:

Debloating & references:

- [**LibreWolf**](https://gitlab.com/librewolf-community/browser/source) - Telemetry patches [](https://github.com/daijro/camoufox/tree/main/patches/librewolf)and build system inspiration
- [**BetterFox**](https://github.com/yokoffing/BetterFox) - Speed & debloat preferences
- [**Ghostery**](https://github.com/ghostery/user-agent-desktop) - Small patch to disable FF onboarding[](https://github.com/daijro/camoufox/blob/main/patches/ghostery/Disable-Onboarding-Messages.patch)

Driver:

- [**Playwright**](https://github.com/microsoft/playwright/tree/main/browser_patches/firefox) - Original implementation of Juggler[](https://github.com/daijro/camoufox/tree/main/additions/juggler)
- [**riflosnake/HumanCursor**](https://github.com/riflosnake/HumanCursor) - Original human-like cursor movement algorithm, ported to C++[](https://github.com/daijro/camoufox/tree/main/additions/human_cursor)

Interface:

- [**Jamir-boop/minimalisticfox**](https://github.com/Jamir-boop/minimalisticfox) - Helped with css theming[](https://github.com/daijro/camoufox/blob/main/settings/chrome.css)
- [**nicoth-in/Dark-Space-Theme**](https://github.com/nicoth-in/Dark-Space-Theme) - Black color theme[](https://github.com/daijro/camoufox/blob/main/additions/browser/themes/addons/dark/manifest.json)

Cool stuff:

- [CreepJS](https://github.com/abrahamjuliot/creepjs), [Browserleaks](https://browserleaks.com), [BrowserScan](https://www.browserscan.net/) - Valuable leak testing sites
- [*The Design and Implementation of the Tor Browser \[DRAFT\]*](https://2019.www.torproject.org/projects/torbrowser/design/) - Anti fingerprinting writeup