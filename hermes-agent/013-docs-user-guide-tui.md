---
title: TUI | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/tui
source: crawler
fetched_at: 2026-04-24T17:00:10.547309167-03:00
rendered_js: false
word_count: 1001
summary: This document details the TUI (Text User Interface) for Hermes, outlining how to launch it via CLI commands or environment variables, describing its numerous advantages over the classic interface, and providing comprehensive guides on configuration options, keybindings, and specific command behaviors.
tags:
    - hermes-tui
    - terminal-interface
    - cli-frontend
    - user-guide
    - configuration
    - keybindings
    - slash-commands
category: guide
---

The TUI is the modern front-end for Hermes — a terminal UI backed by the same Python runtime as the [Classic CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli). Same agent, same sessions, same slash commands; a cleaner, more responsive surface for interacting with them.

It's the recommended way to run Hermes interactively.

## Launch[​](#launch "Direct link to Launch")

```bash
# Launch the TUI
hermes --tui

# Resume the latest TUI session (falls back to the latest classic session)
hermes --tui-c
hermes --tui--continue

# Resume a specific session by ID or title
hermes --tui-r 20260409_000000_aa11bb
hermes --tui--resume"my t0p session"

# Run source directly — skips the prebuild step (for TUI contributors)
hermes --tui--dev
```

You can also enable it via env var:

```bash
exportHERMES_TUI=1
hermes          # now uses the TUI
hermes chat     # same
```

The classic CLI remains available as the default. Anything documented in [CLI Interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli) — slash commands, quick commands, skill preloading, personalities, multi-line input, interrupts — works in the TUI identically.

## Why the TUI[​](#why-the-tui "Direct link to Why the TUI")

- **Instant first frame** — the banner paints before the app finishes loading, so the terminal never feels frozen while Hermes is starting.
- **Non-blocking input** — type and queue messages before the session is ready. Your first prompt sends the moment the agent comes online.
- **Rich overlays** — model picker, session picker, approval and clarification prompts all render as modal panels rather than inline flows.
- **Live session panel** — tools and skills fill in progressively as they initialize.
- **Mouse-friendly selection** — drag to highlight with a uniform background instead of SGR inverse. Copy with your terminal's normal copy gesture.
- **Alternate-screen rendering** — differential updates mean no flicker when streaming, no scrollback clutter after you quit.
- **Composer affordances** — inline paste-collapse for long snippets, `Cmd+V` / `Ctrl+V` text paste with clipboard-image fallback, bracketed-paste safety, and image/file-path attachment normalization.

Same [skins](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins) and [personalities](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality) apply. Switch mid-session with `/skin ares`, `/personality pirate`, and the UI repaints live. See [Skins & Themes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins) for the full list of customizable keys and which ones apply to classic vs TUI — the TUI honors the banner palette, UI colors, prompt glyph/color, session display, completion menu, selection bg, `tool_prefix`, and `help_header`.

## Requirements[​](#requirements "Direct link to Requirements")

- **Node.js** ≥ 20 — the TUI runs as a subprocess launched from the Python CLI. `hermes doctor` verifies this.
- **TTY** — like the classic CLI, piping stdin or running in non-interactive environments falls back to single-query mode.

On first launch Hermes installs the TUI's Node dependencies into `ui-tui/node_modules` (one-time, a few seconds). Subsequent launches are fast. If you pull a new Hermes version, the TUI bundle is rebuilt automatically when sources are newer than the dist.

### External prebuild[​](#external-prebuild "Direct link to External prebuild")

Distributions that ship a prebuilt bundle (Nix, system packages) can point Hermes at it:

```bash
exportHERMES_TUI_DIR=/path/to/prebuilt/ui-tui
hermes --tui
```

The directory must contain `dist/entry.js` and an up-to-date `node_modules`.

## Keybindings[​](#keybindings "Direct link to Keybindings")

Keybindings match the [Classic CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli#keybindings) exactly. The only behavioral differences:

- **Mouse drag** highlights text with a uniform selection background.
- **`Cmd+V` / `Ctrl+V`** first tries normal text paste, then falls back to OSC52/native clipboard reads, and finally image attach when the clipboard or pasted payload resolves to an image.
- **`/terminal-setup`** installs local VS Code / Cursor / Windsurf terminal bindings for better `Cmd+Enter` and undo/redo parity on macOS.
- **Slash autocompletion** opens as a floating panel with descriptions, not an inline dropdown.

## Slash commands[​](#slash-commands "Direct link to Slash commands")

All slash commands work unchanged. A few are TUI-owned — they produce richer output or render as overlays rather than inline panels:

CommandTUI behavior`/help`Overlay with categorized commands, arrow-key navigable`/sessions`Modal session picker — preview, title, token totals, resume inline`/model`Modal model picker grouped by provider, with cost hints`/skin`Live preview — theme change applies as you browse`/details`Toggle verbose tool-call details (global or per-section)`/usage`Rich token / cost / context panel

Every other slash command (including installed skills, quick commands, and personality toggles) works identically to the classic CLI. See [Slash Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/slash-commands).

## Status line[​](#status-line "Direct link to Status line")

The TUI's status line tracks agent state in real time:

StatusMeaning`starting agent…`Session ID is live; tools and skills still coming online. You can type — messages queue and send when ready.`ready`Agent is idle, accepting input.`thinking…` / `running…`Agent is reasoning or running a tool.`interrupted`Current turn was cancelled; press Enter to send again.`forging session…` / `resuming…`Initial connect or `--resume` handshake.

The per-skin status-bar colors and thresholds are shared with the classic CLI — see [Skins](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins) for customization.

## Configuration[​](#configuration "Direct link to Configuration")

The TUI respects all standard Hermes config: `~/.hermes/config.yaml`, profiles, personalities, skins, quick commands, credential pools, memory providers, tool/skill enablement. No TUI-specific config file exists.

A handful of keys tune the TUI surface specifically:

```yaml
display:
skin: default              # any built-in or custom skin
personality: helpful
details_mode: collapsed    # hidden | collapsed | expanded — global accordion default
sections:# optional: per-section overrides (any subset)
thinking: expanded       # always open
tools: expanded          # always open
activity: collapsed      # opt back IN to the activity panel (hidden by default)
mouse_tracking:true# disable if your terminal conflicts with mouse reporting
```

Runtime toggles:

- `/details [hidden|collapsed|expanded|cycle]` — set the global mode
- `/details <section> [hidden|collapsed|expanded|reset]` — override one section (sections: `thinking`, `tools`, `subagents`, `activity`)

**Default visibility**

The TUI ships with opinionated per-section defaults that stream the turn as a live transcript instead of a wall of chevrons:

- `thinking` — **expanded**. Reasoning streams inline as the model emits it.
- `tools` — **expanded**. Tool calls and their results render open.
- `subagents` — falls through to the global `details_mode` (collapsed under chevron by default — stays quiet until a delegation actually happens).
- `activity` — **hidden**. Ambient meta (gateway hints, terminal-parity nudges, background notifications) is noise for most day-to-day use. Tool failures still render inline on the failing tool row; ambient errors/warnings surface via a floating-alert backstop when every panel is hidden.

Per-section overrides take precedence over both the section default and the global `details_mode`. To reshape the layout:

- `display.sections.thinking: collapsed` — put thinking back under a chevron
- `display.sections.tools: collapsed` — put tool calls back under a chevron
- `display.sections.activity: collapsed` — opt the activity panel back in
- `/details <section> <mode>` at runtime

Anything set explicitly in `display.sections` wins over the defaults, so existing configs keep working unchanged.

## Sessions[​](#sessions "Direct link to Sessions")

Sessions are shared between the TUI and the classic CLI — both write to the same `~/.hermes/state.db`. You can start a session in one, resume in the other. The session picker surfaces sessions from both sources, with a source tag.

See [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions) for lifecycle, search, compression, and export.

## Reverting to the classic CLI[​](#reverting-to-the-classic-cli "Direct link to Reverting to the classic CLI")

Launching `hermes` (without `--tui`) stays on the classic CLI. To make a machine prefer the TUI, set `HERMES_TUI=1` in your shell profile. To go back, unset it.

If the TUI fails to launch (no Node, missing bundle, TTY issue), Hermes prints a diagnostic and falls back — rather than leaving you stuck.

## See also[​](#see-also "Direct link to See also")

- [CLI Interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli) — full slash command and keybinding reference (shared)
- [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions) — resume, branch, and history
- [Skins & Themes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins) — theme the banner, status bar, and overlays
- [Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode) — works in both interfaces
- [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) — all config keys