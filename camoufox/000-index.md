---
description: Auto-generated documentation index for Camoufox
generated: 2026-03-09T16:50:00Z
source: https://camoufox.com/sitemap.xml.gz
total_docs: 42
categories: 15
---

# Camoufox Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://camoufox.com/sitemap.xml.gz |
| **Generated** | 2026-03-09T16:50:00Z |
| **Total Documents** | 42 |
| **Categories** | 15 |

---

## Document Index

### 1. Introduction & Overview (001-002)

*Core concepts and feature overview of Camoufox anti-detect browser.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-introduction.md` | Introduction | Camoufox is an open-source, anti-detect browser built on Firefox that focuses on robust, low-level fingerprint injection and rotation to remain invisible to anti-bot systems without resorting to JavaScript tampering. | anti-detect, fingerprint-spoofing, firefox, browser-security, privacy, bot-evasion |
| 002 | `002-features-list.md` | Features List | Lists the features, patches, and optimizations implemented in Camoufox, including fingerprint spoofing, stealth capabilities, anti-font fingerprinting, Playwright support, debloating, addon handling, and Python interface. | browser-hardening, fingerprint-spoofing, stealth-patches, anti-fingerprinting, debloat, playwright-integration |

### 2. Stealth Concepts (003)

*Understanding how Camoufox evades anti-bot detection.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-stealth-overview.md` | Stealth Overview | Explains the internal mechanisms Camoufox uses to evade anti-bot detection by isolating automation code, mimicking realistic user behavior, and rotating consistent browser fingerprints. | anti-bot-evasion, fingerprint-spoofing, javascript-isolation, cdp-alternatives, browserforge, juggler |

### 3. Python Interface - Overview & Setup (004-006)

*Getting started with the Camoufox Python library.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 004 | `004-python-interface.md` | Python Interface | Introduces Camoufox Python library that provides a lightweight wrapper around the Playwright API to automate the injection of unique device characteristics for browser fingerprint spoofing. | playwright-api, browser-fingerprinting, camoufox, device-emulation, python-library |
| 005 | `005-python-installation.md` | Installation | Outlines the initial installation process for the `camoufox` package, including an optional geoip dependency, and provides CLI command reference. | installation, cli-commands, package-management, geoip-optional, camoufox |
| 006 | `006-python-usage.md` | Usage | Details the available configuration parameters for initializing Camoufox with Playwright, covering options for device properties, general configuration, and location settings. | camoufox, playwright, configuration, browser-fingerprinting, initialization-parameters, firefox |

### 4. Python Interface - Configuration (007-011)

*Advanced configuration options for the Python library.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 007 | `007-python-config.md` | Passing Config | Explains how to override or pass custom configuration data, such as WebRTC settings, to the Camoufox client via the 'config' parameter. | camoufox, configuration, custom-settings, webrtc, python-library |
| 008 | `008-python-browserforge.md` | BrowserForge Integration | Explains how Camoufox interacts with BrowserForge fingerprints, covering both the default random generation based on constraints and how to inject custom Fingerprint objects. | camoufox, browserforge, fingerprint, configuration, api-usage |
| 009 | `009-python-geoip.md` | GeoIP & Proxy Support | Explains how to configure Camoufox to automatically use geolocation data from a target IP address for spoofing browser settings like location and language. | camoufox, geoip, spoofing, playwright, web-traffic, proxy |
| 010 | `010-python-virtual-display.md` | Virtual Display | Explains how to run Camoufox headlessly on Linux systems using a virtual display buffer like Xvfb to improve stealthiness. | camoufox, headless-mode, xvfb, virtual-display, linux-setup |
| 011 | `011-python-main-world-eval.md` | Main World Execution | Explains how to control whether JavaScript evaluation runs in an isolated scope (isolated world) or the main browser scope to enable DOM manipulation. | javascript-execution, dom-manipulation, isolated-world, main-world, page-evaluation |

### 5. Python Interface - Advanced (012)

*Experimental and advanced Python features.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 012 | `012-python-remote-server.md` | Remote Server | Explains how to launch Camoufox as a remote websocket server and how clients using the Playwright API can connect to it from other devices or languages. | websocket-server, remote-access, playwright, launching, connecting |

### 6. Fingerprint Injection - Overview (013)

*Understanding fingerprint injection at the C++ level.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 013 | `013-fingerprint-injection.md` | Fingerprint Injection | Explains how to use Camoufox to spoof browser fingerprint properties by passing configuration data, with interception at the C++ implementation level making changes undetectable through JavaScript inspection. | fingerprinting, spoofing, python-interface, browser-configuration, c++-implementation |

### 7. Fingerprint Properties - Browser APIs (014-017)

*Spoofing browser API objects (Navigator, Screen, Window, Document).*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 014 | `014-fingerprint-navigator.md` | Navigator | Outlines the capabilities and safety of spoofing Navigator properties in Firefox, noting specific behaviors and potential leakage points when emulating Chrome. | navigator-properties, firefox-spoofing, user-agent, privacy-settings, webdriver |
| 015 | `015-fingerprint-screen.md` | Screen | Lists and describes the properties available on the JavaScript 'screen' object, which provide information about the user's display characteristics. | javascript, screen-object, display-properties, window-metrics, browser-api |
| 016 | `016-fingerprint-window.md` | Window | Details a set of properties that allow for the spoofing or modification of various window metrics, including dimensions, scroll positions, and history length. | window-properties, spoofing, browser-metrics, scroll-offsets, viewport, history |
| 017 | `017-fingerprint-document.md` | Document | Details the properties available on the document.body object used for determining the client dimensions and borders of the HTML body element. | document-body, client-dimensions, html-elements, client-width, client-height |

### 8. Fingerprint Properties - Network & Location (018-020)

*Spoofing network identifiers and geolocation.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 018 | `018-fingerprint-geolocation.md` | Geolocation & Intl | Describes various properties available for configuration, detailing their types, descriptions, and associated required keys for functionality. | configuration-properties, geolocation, locale-settings, timezone, data-types |
| 019 | `019-fingerprint-headers.md` | HTTP Headers | Lists the specific network headers that Camoufox is capable of overriding within its configuration settings. | camoufox, network-headers, user-agent, accept-language, accept-encoding, configuration |
| 020 | `020-fingerprint-webrtc.md` | WebRTC IP | Details the specific properties used by Camoufox to configure WebRTC IP spoofing by modifying ICE candidates and SDP. | webrtc, ip-spoofing, ice-candidates, sdp, configuration, properties |

### 9. Fingerprint Properties - Media & Graphics (021-023)

*Spoofing media devices and graphics capabilities.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 021 | `021-fingerprint-webgl.md` | WebGL | Describes the Camoufox WebGL research initiative and provides access to a demo site used for generating WebGL fingerprints from various devices. | webgl, gpu-research, fingerprinting, demo-site, browser-parameters |
| 022 | `022-fingerprint-media-audio.md` | Media & Audio | Details properties used to spoof or fake the available media devices (microphones, webcams, speakers) and parameters of the AudioContext for testing purposes. | media-devices, spoofing, audiocontext, microphone-faking, webcam-faking, testing |
| 023 | `023-fingerprint-voices.md` | Voices | Discusses methods for spoofing voices within the Web Speech API, noting a limitation with the `voices:fakeCompletion` feature. | web-speech-api, voice-spoofing, tts, browser-api, bot-detection |

### 10. Fingerprint Properties - Other (024-027)

*Additional fingerprint spoofing options.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 024 | `024-fingerprint-fonts.md` | Fonts | Comprehensive list of font names, including various system, UI, and specialized font families available or referenced. | font-names, typeface-listing, system-fonts, unicode-fonts, apple-fonts, noto-fonts |
| 025 | `025-fingerprint-addons.md` | Addons | Explains how to load custom browser extensions using the `addons` parameter in the Camoufox Python library, and how to exclude default extensions like uBlock Origin. | camoufox, addons, extension-loading, python-library, default-addons, ublock-origin |
| 026 | `026-fingerprint-cursor-movement.md` | Cursor Movement | Explains the configuration and properties available for enabling and customizing human-like cursor movement within the Camoufox framework. | cursor-movement, humanization, configuration, properties, highlighter |
| 027 | `027-fingerprint-miscellaneous.md` | Miscellaneous | Details properties used to spoof or simulate battery status information and the availability of a PDF viewer within a browser environment. | spoofing, battery-status, pdf-viewer, navigator-properties, headless-detection |

### 11. Development - Overview (028-029)

*Building and contributing to Camoufox.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 028 | `028-development.md` | Development | Provides an overview of the procedures for building Camoufox from scratch and the necessary steps and tools for developing and debugging patches for the software. | camoufox, building, development, debugging, patching, cli, docker |
| 029 | `029-development-build-system.md` | Build System | Presents a textual diagram illustrating the structure and associated make commands of a software build system, noting its origin from the LibreWolf build system. | build-system, make-commands, software-development, diagram, librewolf |

### 12. Development - Building (030-031)

*Build instructions for different platforms.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-development-buildcli.md` | Building in CLI | Outlines the command-line options available for executing a multi-platform build script, specifying targets and architectures. | command-line, build-system, target-platforms, architectures, options, script-execution |
| 031 | `031-development-docker.md` | Building in Docker | Outlines the steps required to build Camoufox patches on non-Linux systems using Docker, including how to build the image and execute the build process. | camoufox, docker, building, compilation, cross-platform |

### 13. Development - Tools & Debugging (032-033)

*Developer tools and troubleshooting.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 032 | `032-development-tools.md` | Development Tools | Explains how to use the included developer UI script to create, manage, and modify patches by resetting the workspace and writing changes back to a patch file. | developer-ui, patch-management, workspace-reset, scripting, development-workflow |
| 033 | `033-development-leak-debugging.md` | Leak Debugging | Provides a step-by-step flowchart and associated build commands for incrementally isolating a website flagging issue caused by Camoufox features within a custom Firefox build. | debugging, fingerprinting-resistance, firefox-build, waf-testing, troubleshooting, camoufox |

### 14. About & Legal (034-035)

*Project information and legal notices.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 034 | `034-about.md` | About Me | Personal page for a security researcher, detailing their current status, hobbies like homelab work and tool development, and contact information. | personal-page, security-researcher, homelab, contact-information, pgp-key, donations |
| 035 | `035-legal.md` | Liability Disclaimer | Explicitly states that the software provides no liability or warranty and outlines restrictions on acceptable use, prohibiting illegal or malicious activities. | disclaimer, liability-waiver, acceptable-use, terms-of-service, legal-notice |

### 15. Test Pages (036-042)

*Empty test/placeholder documents from the website.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 036 | `036-tests-buttonclick.md` | - | Empty document - test page placeholder. | empty-document, no-content, placeholder |
| 037 | `037-tests-canvas.md` | - | Empty document - test page placeholder. | empty-document, no-content |
| 038 | `038-tests-shadowdom.md` | - | Empty document - test page placeholder. | empty-document, no-content |
| 039 | `039-tests-webgl.md` | - | Empty document - test page placeholder. | empty-document, no-content |
| 040 | `040-tests-shapetests.md` | - | Empty document - test page placeholder. | empty-document, no-content |
| 041 | `041-tests-private-canvas-low-entropy.md` | - | Empty document - test page placeholder. | empty-document, no-content |
| 042 | `042-assets-fpgen-tree.md` | - | Empty document - test page placeholder. | empty-document, no-content |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-006 |
| **Python Configuration** | 007-012 |
| **Fingerprint Injection** | 013-027 |
| **Development** | 028-033 |
| **Legal/About** | 034-035 |
| **Test Pages** | 036-042 |

### By Concept

| Concept | Files |
|---------|-------|
| **Browser APIs** | 014, 015, 016, 017 |
| **Network Spoofing** | 019, 020 |
| **Geolocation** | 009, 018 |
| **WebGL/Graphics** | 021, 039 |
| **Media Devices** | 022, 023 |
| **Humanization** | 026 |
| **Proxy/IP** | 009, 020 |
| **Build System** | 028, 029, 030, 031 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read **001-002** for introduction and feature overview
- Complete **003** for stealth concepts
- Read **004-006** for Python interface basics and setup

### Level 2: Core Configuration
- Learn configuration from **007-011**
- Understand BrowserForge integration in **008**
- Set up GeoIP/proxy with **009**

### Level 3: Fingerprint Spoofing
- Understand fingerprint injection in **013**
- Configure Navigator spoofing with **014**
- Set up Screen/Window/Document properties with **015-017**
- Configure network spoofing with **018-020**

### Level 4: Advanced Fingerprinting
- Master WebGL spoofing in **021**
- Configure media devices with **022-023**
- Set up fonts, addons, and cursor movement with **024-026**

### Level 5: Development & Debugging
- Review development overview in **028-029**
- Build from source with **030-031**
- Use developer tools and debug leaks with **032-033**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the Camoufox documentation structure.*