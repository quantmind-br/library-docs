---
title: Droid Control - Factory Documentation
url: https://docs.factory.ai/cli/features/droid-control
source: sitemap
fetched_at: 2026-04-15T09:00:41.767019324-03:00
rendered_js: false
word_count: 536
summary: This document provides installation instructions, command usage, and architectural details for the Droid Control plugin, which enables autonomous agents to perform software testing, UI interaction, and video demonstration generation.
tags:
    - droid-control
    - automation
    - software-testing
    - video-rendering
    - plugin-configuration
    - ai-agents
category: guide
---

Droid Control is a plugin that enables Droids to *operate* software: launch apps, type commands, click buttons, record what happens, and produce polished video evidence of it. Built by Droids, for Droids.

## Install

- UI
- CLI

Run `/plugins` in a Droid session, go to the Browse tab, find **droid-control**, and install it.

```
# Add the Factory plugins marketplace (if not already registered)
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins

# Install the plugin
droid plugin install droid-control@factory-plugins --scope user
```

For video rendering, Remotion dependencies need a one-time install. After installing the plugin, run `npm install` in its `remotion/` directory:

```
# Find the plugin install path
droid plugin list --scope user

# Then install Remotion deps (adjust path to match your install)
cd <plugin-path>/remotion && npm install
```

## Commands

Droid Control adds three slash commands. Each one handles the full workflow end-to-end: planning, execution, recording, and reporting.

### `/verify`

Test a specific behavior claim and report findings with evidence.

```
/verify "ESC cancels streaming in bash mode"
```

Droid launches the app, attempts the claim, and reports what actually happened, with screenshots and text snapshots as evidence. The droid is framed as an investigator, not an advocate. If the claim is false, that’s a valid finding. Anti-fabrication rules prevent staging evidence to match expected outcomes.

### `/qa-test`

Run automated QA against terminal CLIs or web/Electron apps.

```
/qa-test https://app.example.com -- login, create a project, invite a member
```

Droid drives the browser (or terminal) through the flow, captures each step, and reports pass/fail with annotated screenshots.

### `/demo`

Record a demo video of a feature or PR.

Droid reads the PR, scripts interactions that prove the change works, records both branches in parallel, and renders a side-by-side comparison video. Add “showcase” for cinematic polish, “keys” for keystroke overlay.

```
/demo pr-1847 -- showcase, keys
```

**What it does:**

#### Example output

Every video below was planned, recorded, and rendered entirely by a Droid.

- CLI: single-branch
- CLI: before/after
- Web app: single-branch
- Web app: before/after

## Drivers

Droid Control supports three automation backends. The right one is selected automatically based on what you’re targeting.

## Video rendering

Demo and showcase videos are rendered using [Remotion](https://www.remotion.dev/), a React-based video engine. The plugin includes 22 visual components and 6 presets. **Automatic layers** (always present, intensity varies by preset):

- Warm radial backgrounds, floating particles, film grain overlay, color grading
- Motion blur title-to-content transition
- Animated window chrome with traffic lights and glassmorphic borders
- Auto-scaled title/subtitle text

**Effect layers** (selected by the droid at compose time):

- Spotlight overlays to highlight specific regions
- Directed zoom for small text or details
- Keystroke pills showing user actions
- Section headers and transition sweeps

PresetLookBest for`factory`Warm black, traffic lights, amber glowOfficial Factory content`factory-hero`Same + gradient backgroundLanding pages, social`hero`Cool gradient, generous marginsNon-Factory marketing`macos`Dark, clean frameGeneral-purpose demos`presentation`Black, generous marginsSlide decks, talks`minimal`No window bar, tight marginsDocs embeds, inline clips

## How it works

The plugin uses a composition architecture with three layers:

- **Orchestrator** routes each request through three independent lookups (target, stage, artifact) to determine which skills to load
- **10 atom skills** are self-contained background knowledge loaded on demand, split into drivers, targets, stages, and polish
- **3 commands** parse arguments into commitments, then delegate to atoms via hybrid handoffs

Every workflow flows through **capture → compose → verify**. Commands declare *what* to produce; atoms own *how*. Skills chain through explicit handoffs rather than hardcoded pipelines, so the droid follows the flow naturally. For a deeper look at the design decisions, see [ARCHITECTURE.md](https://github.com/Factory-AI/factory-plugins/blob/master/plugins/droid-control/ARCHITECTURE.md) on GitHub.

## Prerequisites

Only install what you need for your use case. Terminal demos need tuistory, asciinema, agg, and ffmpeg. Web/Electron automation just needs agent-browser.

ComponentPlatformRequired toolstuistoryAll`tuistory`, `asciinema`, `agg`true-inputLinux/Wayland`cage`, `wtype`, Wayland terminaltrue-inputWindows (KVM)`libvirt`, `qemu`, KVM VM with SSHtrue-inputmacOS (QEMU)`qemu`, `socat`, macOS VM with SSHagent-browserAll`agent-browser`composeAll`ffmpeg`, `ffprobe`, `agg`showcaseAllNode.js (&gt;= 18), Chrome/Chromium

```
npm install -g tuistory                              # virtual PTY driver
pip install asciinema                                 # terminal recording
cargo install --git https://github.com/asciinema/agg   # .cast → .gif converter
sudo apt-get install -y ffmpeg                        # video processing
agent-browser install                                 # browser automation (downloads Chromium)
```

## Learn more