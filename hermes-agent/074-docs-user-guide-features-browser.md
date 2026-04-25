---
title: Browser Automation | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/features/browser
source: crawler
fetched_at: 2026-04-24T17:00:08.39902908-03:00
rendered_js: false
word_count: 2180
summary: This document outlines the various methods Hermes Agent supports for browser automation, detailing options like using cloud providers (Browserbase, Browser Use, Firecrawl), connecting to local Chrome via CDP, and utilizing self-hosted Camofox for local anti-detection browsing.
tags:
    - browser-automation
    - hermes-agent
    - cloud-browsing
    - local-chrome
    - cdp-integration
    - camofox
    - scrapers
category: guide
---

Hermes Agent includes a full browser automation toolset with multiple backend options:

- **Browserbase cloud mode** via [Browserbase](https://browserbase.com) for managed cloud browsers and anti-bot tooling
- **Browser Use cloud mode** via [Browser Use](https://browser-use.com) as an alternative cloud browser provider
- **Firecrawl cloud mode** via [Firecrawl](https://firecrawl.dev) for cloud browsers with built-in scraping
- **Camofox local mode** via [Camofox](https://github.com/jo-inc/camofox-browser) for local anti-detection browsing (Firefox-based fingerprint spoofing)
- **Local Chrome via CDP** — connect browser tools to your own Chrome instance using `/browser connect`
- **Local browser mode** via the `agent-browser` CLI and a local Chromium installation

In all modes, the agent can navigate websites, interact with page elements, fill forms, and extract information.

## Overview[​](#overview "Direct link to Overview")

Pages are represented as **accessibility trees** (text-based snapshots), making them ideal for LLM agents. Interactive elements get ref IDs (like `@e1`, `@e2`) that the agent uses for clicking and typing.

Key capabilities:

- **Multi-provider cloud execution** — Browserbase, Browser Use, or Firecrawl — no local browser needed
- **Local Chrome integration** — attach to your running Chrome via CDP for hands-on browsing
- **Built-in stealth** — random fingerprints, CAPTCHA solving, residential proxies (Browserbase)
- **Session isolation** — each task gets its own browser session
- **Automatic cleanup** — inactive sessions are closed after a timeout
- **Vision analysis** — screenshot + AI analysis for visual understanding

## Setup[​](#setup "Direct link to Setup")

Nous Subscribers

If you have a paid [Nous Portal](https://portal.nousresearch.com) subscription, you can use browser automation through the [**Tool Gateway**](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway) without any separate API keys. Run `hermes model` or `hermes tools` to enable it.

### Browserbase cloud mode[​](#browserbase-cloud-mode "Direct link to Browserbase cloud mode")

To use Browserbase-managed cloud browsers, add:

```bash
# Add to ~/.hermes/.env
BROWSERBASE_API_KEY=***
BROWSERBASE_PROJECT_ID=your-project-id-here
```

Get your credentials at [browserbase.com](https://browserbase.com).

### Browser Use cloud mode[​](#browser-use-cloud-mode "Direct link to Browser Use cloud mode")

To use Browser Use as your cloud browser provider, add:

```bash
# Add to ~/.hermes/.env
BROWSER_USE_API_KEY=***
```

Get your API key at [browser-use.com](https://browser-use.com). Browser Use provides a cloud browser via its REST API. If both Browserbase and Browser Use credentials are set, Browserbase takes priority.

### Firecrawl cloud mode[​](#firecrawl-cloud-mode "Direct link to Firecrawl cloud mode")

To use Firecrawl as your cloud browser provider, add:

```bash
# Add to ~/.hermes/.env
FIRECRAWL_API_KEY=fc-***
```

Get your API key at [firecrawl.dev](https://firecrawl.dev). Then select Firecrawl as your browser provider:

```bash
hermes setup tools
# → Browser Automation → Firecrawl
```

Optional settings:

```bash
# Self-hosted Firecrawl instance (default: https://api.firecrawl.dev)
FIRECRAWL_API_URL=http://localhost:3002

# Session TTL in seconds (default: 300)
FIRECRAWL_BROWSER_TTL=600
```

### Camofox local mode[​](#camofox-local-mode "Direct link to Camofox local mode")

[Camofox](https://github.com/jo-inc/camofox-browser) is a self-hosted Node.js server wrapping Camoufox (a Firefox fork with C++ fingerprint spoofing). It provides local anti-detection browsing without cloud dependencies.

```bash
# Install and run
git clone https://github.com/jo-inc/camofox-browser &&cd camofox-browser
npminstall&&npm start   # downloads Camoufox (~300MB) on first run

# Or via Docker
docker run -d--networkhost-eCAMOFOX_PORT=9377 jo-inc/camofox-browser
```

Then set in `~/.hermes/.env`:

```bash
CAMOFOX_URL=http://localhost:9377
```

Or configure via `hermes tools` → Browser Automation → Camofox.

When `CAMOFOX_URL` is set, all browser tools automatically route through Camofox instead of Browserbase or agent-browser.

#### Persistent browser sessions[​](#persistent-browser-sessions "Direct link to Persistent browser sessions")

By default, each Camofox session gets a random identity — cookies and logins don't survive across agent restarts. To enable persistent browser sessions, add the following to `~/.hermes/config.yaml`:

```yaml
browser:
camofox:
managed_persistence:true
```

Then fully restart Hermes so the new config is picked up.

Nested path matters

Hermes reads `browser.camofox.managed_persistence`, **not** a top-level `managed_persistence`. A common mistake is writing:

```yaml
# ❌ Wrong — Hermes ignores this
managed_persistence:true
```

If the flag is placed at the wrong path, Hermes silently falls back to a random ephemeral `userId` and your login state will be lost on every session.

##### What Hermes does[​](#what-hermes-does "Direct link to What Hermes does")

- Sends a deterministic profile-scoped `userId` to Camofox so the server can reuse the same Firefox profile across sessions.
- Skips server-side context destruction on cleanup, so cookies and logins survive between agent tasks.
- Scopes the `userId` to the active Hermes profile, so different Hermes profiles get different browser profiles (profile isolation).

##### What Hermes does not do[​](#what-hermes-does-not-do "Direct link to What Hermes does not do")

- It does not force persistence on the Camofox server. Hermes only sends a stable `userId`; the server must honor it by mapping that `userId` to a persistent Firefox profile directory.
- If your Camofox server build treats every request as ephemeral (e.g. always calls `browser.newContext()` without loading a stored profile), Hermes cannot make those sessions persist. Make sure you are running a Camofox build that implements userId-based profile persistence.

##### Verify it's working[​](#verify-its-working "Direct link to Verify it's working")

1. Start Hermes and your Camofox server.
2. Open Google (or any login site) in a browser task and sign in manually.
3. End the browser task normally.
4. Start a new browser task.
5. Open the same site again — you should still be signed in.

If step 5 logs you out, the Camofox server isn't honoring the stable `userId`. Double-check your config path, confirm you fully restarted Hermes after editing `config.yaml`, and verify your Camofox server version supports persistent per-user profiles.

##### Where state lives[​](#where-state-lives "Direct link to Where state lives")

Hermes derives the stable `userId` from the profile-scoped directory `~/.hermes/browser_auth/camofox/` (or the equivalent under `$HERMES_HOME` for non-default profiles). The actual browser profile data lives on the Camofox server side, keyed by that `userId`. To fully reset a persistent profile, clear it on the Camofox server and remove the corresponding Hermes profile's state directory.

#### VNC live view[​](#vnc-live-view "Direct link to VNC live view")

When Camofox runs in headed mode (with a visible browser window), it exposes a VNC port in its health check response. Hermes automatically discovers this and includes the VNC URL in navigation responses, so the agent can share a link for you to watch the browser live.

### Local Chrome via CDP (`/browser connect`)[​](#local-chrome-via-cdp-browser-connect "Direct link to local-chrome-via-cdp-browser-connect")

Instead of a cloud provider, you can attach Hermes browser tools to your own running Chrome instance via the Chrome DevTools Protocol (CDP). This is useful when you want to see what the agent is doing in real-time, interact with pages that require your own cookies/sessions, or avoid cloud browser costs.

note

`/browser connect` is an **interactive-CLI slash command** — it is not dispatched by the gateway. If you try to run it inside a WebUI, Telegram, Discord, or other gateway chat, the message will be sent to the agent as plain text and the command will not execute. Start Hermes from the terminal (`hermes` or `hermes chat`) and issue `/browser connect` there.

In the CLI, use:

```text
/browser connect              # Connect to Chrome at ws://localhost:9222
/browser connect ws://host:port  # Connect to a specific CDP endpoint
/browser status               # Check current connection
/browser disconnect            # Detach and return to cloud/local mode
```

If Chrome isn't already running with remote debugging, Hermes will attempt to auto-launch it with `--remote-debugging-port=9222`.

tip

To start Chrome manually with CDP enabled, use a dedicated user-data-dir so the debug port actually comes up even if Chrome is already running with your normal profile:

```bash
# Linux
google-chrome \
  --remote-debugging-port=9222\
  --user-data-dir=$HOME/.hermes/chrome-debug \
  --no-first-run \
  --no-default-browser-check &

# macOS
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"\
  --remote-debugging-port=9222\
  --user-data-dir="$HOME/.hermes/chrome-debug"\
  --no-first-run \
  --no-default-browser-check &
```

Then launch the Hermes CLI and run `/browser connect`.

**Why `--user-data-dir`?** Without it, launching Chrome while a regular Chrome instance is already running typically opens a new window on the existing process — and that existing process was not started with `--remote-debugging-port`, so port 9222 never opens. A dedicated user-data-dir forces a fresh Chrome process where the debug port actually listens. `--no-first-run --no-default-browser-check` skips the first-launch wizard for the fresh profile.

When connected via CDP, all browser tools (`browser_navigate`, `browser_click`, etc.) operate on your live Chrome instance instead of spinning up a cloud session.

### Local browser mode[​](#local-browser-mode "Direct link to Local browser mode")

If you do **not** set any cloud credentials and don't use `/browser connect`, Hermes can still use the browser tools through a local Chromium install driven by `agent-browser`.

### Optional Environment Variables[​](#optional-environment-variables "Direct link to Optional Environment Variables")

```bash
# Residential proxies for better CAPTCHA solving (default: "true")
BROWSERBASE_PROXIES=true

# Advanced stealth with custom Chromium — requires Scale Plan (default: "false")
BROWSERBASE_ADVANCED_STEALTH=false

# Session reconnection after disconnects — requires paid plan (default: "true")
BROWSERBASE_KEEP_ALIVE=true

# Custom session timeout in milliseconds (default: project default)
# Examples: 600000 (10min), 1800000 (30min)
BROWSERBASE_SESSION_TIMEOUT=600000

# Inactivity timeout before auto-cleanup in seconds (default: 120)
BROWSER_INACTIVITY_TIMEOUT=120
```

### Install agent-browser CLI[​](#install-agent-browser-cli "Direct link to Install agent-browser CLI")

```bash
npminstall-g agent-browser
# Or install locally in the repo:
npminstall
```

info

The `browser` toolset must be included in your config's `toolsets` list or enabled via `hermes config set toolsets '["hermes-cli", "browser"]'`.

### `browser_navigate`[​](#browser_navigate "Direct link to browser_navigate")

Navigate to a URL. Must be called before any other browser tool. Initializes the Browserbase session.

```text
Navigate to https://github.com/NousResearch
```

tip

For simple information retrieval, prefer `web_search` or `web_extract` — they are faster and cheaper. Use browser tools when you need to **interact** with a page (click buttons, fill forms, handle dynamic content).

### `browser_snapshot`[​](#browser_snapshot "Direct link to browser_snapshot")

Get a text-based snapshot of the current page's accessibility tree. Returns interactive elements with ref IDs like `@e1`, `@e2` for use with `browser_click` and `browser_type`.

- **`full=false`** (default): Compact view showing only interactive elements
- **`full=true`** : Complete page content

Snapshots over 8000 characters are automatically summarized by an LLM.

### `browser_click`[​](#browser_click "Direct link to browser_click")

Click an element identified by its ref ID from the snapshot.

```text
Click @e5 to press the "Sign In" button
```

### `browser_type`[​](#browser_type "Direct link to browser_type")

Type text into an input field. Clears the field first, then types the new text.

```text
Type "hermes agent" into the search field @e3
```

### `browser_scroll`[​](#browser_scroll "Direct link to browser_scroll")

Scroll the page up or down to reveal more content.

```text
Scroll down to see more results
```

### `browser_press`[​](#browser_press "Direct link to browser_press")

Press a keyboard key. Useful for submitting forms or navigation.

```text
Press Enter to submit the form
```

Supported keys: `Enter`, `Tab`, `Escape`, `ArrowDown`, `ArrowUp`, and more.

### `browser_back`[​](#browser_back "Direct link to browser_back")

Navigate back to the previous page in browser history.

### `browser_get_images`[​](#browser_get_images "Direct link to browser_get_images")

List all images on the current page with their URLs and alt text. Useful for finding images to analyze.

### `browser_vision`[​](#browser_vision "Direct link to browser_vision")

Take a screenshot and analyze it with vision AI. Use this when text snapshots don't capture important visual information — especially useful for CAPTCHAs, complex layouts, or visual verification challenges.

The screenshot is saved persistently and the file path is returned alongside the AI analysis. On messaging platforms (Telegram, Discord, Slack, WhatsApp), you can ask the agent to share the screenshot — it will be sent as a native photo attachment via the `MEDIA:` mechanism.

```text
What does the chart on this page show?
```

Screenshots are stored in `~/.hermes/cache/screenshots/` and automatically cleaned up after 24 hours.

### `browser_console`[​](#browser_console "Direct link to browser_console")

Get browser console output (log/warn/error messages) and uncaught JavaScript exceptions from the current page. Essential for detecting silent JS errors that don't appear in the accessibility tree.

```text
Check the browser console for any JavaScript errors
```

Use `clear=True` to clear the console after reading, so subsequent calls only show new messages.

### `browser_cdp`[​](#browser_cdp "Direct link to browser_cdp")

Raw Chrome DevTools Protocol passthrough — the escape hatch for browser operations not covered by the other tools. Use for native dialog handling, iframe-scoped evaluation, cookie/network control, or any CDP verb the agent needs.

**Only available when a CDP endpoint is reachable at session start** — meaning `/browser connect` has attached to a running Chrome, or `browser.cdp_url` is set in `config.yaml`. The default local agent-browser mode, Camofox, and cloud providers (Browserbase, Browser Use, Firecrawl) do not currently expose CDP to this tool — cloud providers have per-session CDP URLs but live-session routing is a follow-up.

**CDP method reference:** [https://chromedevtools.github.io/devtools-protocol/](https://chromedevtools.github.io/devtools-protocol/) — the agent can `web_extract` a specific method's page to look up parameters and return shape.

Common patterns:

```text
# List tabs (browser-level, no target_id)
browser_cdp(method="Target.getTargets")

# Handle a native JS dialog on a tab
browser_cdp(method="Page.handleJavaScriptDialog",
            params={"accept": true, "promptText": ""},
            target_id="<tabId>")

# Evaluate JS in a specific tab
browser_cdp(method="Runtime.evaluate",
            params={"expression": "document.title", "returnByValue": true},
            target_id="<tabId>")

# Get all cookies
browser_cdp(method="Network.getAllCookies")
```

Browser-level methods (`Target.*`, `Browser.*`, `Storage.*`) omit `target_id`. Page-level methods (`Page.*`, `Runtime.*`, `DOM.*`, `Emulation.*`) require a `target_id` from `Target.getTargets`. Each stateless call is independent — sessions do not persist between calls.

**Cross-origin iframes:** pass `frame_id` (from `browser_snapshot.frame_tree.children[]` where `is_oopif=true`) to route the CDP call through the supervisor's live session for that iframe. This is how `Runtime.evaluate` inside a cross-origin iframe works on Browserbase, where stateless CDP connections would hit signed-URL expiry. Example:

```text
browser_cdp(
  method="Runtime.evaluate",
  params={"expression": "document.title", "returnByValue": True},
  frame_id="<frame_id from browser_snapshot>",
)
```

Same-origin iframes don't need `frame_id` — use `document.querySelector('iframe').contentDocument` from a top-level `Runtime.evaluate` instead.

### `browser_dialog`[​](#browser_dialog "Direct link to browser_dialog")

Responds to a native JS dialog (`alert` / `confirm` / `prompt` / `beforeunload`). Before this tool existed, dialogs would silently block the page's JavaScript thread and subsequent `browser_*` calls would hang or throw; now the agent sees pending dialogs in `browser_snapshot` output and responds explicitly.

**Workflow:**

1. Call `browser_snapshot`. If a dialog is blocking the page, it shows up as `pending_dialogs: [{"id": "d-1", "type": "alert", "message": "..."}]`.
2. Call `browser_dialog(action="accept")` or `browser_dialog(action="dismiss")`. For `prompt()` dialogs, pass `prompt_text="..."` to supply the response.
3. Re-snapshot — `pending_dialogs` is empty; the page's JS thread has resumed.

**Detection happens automatically** via a persistent CDP supervisor — one WebSocket per task that subscribes to Page/Runtime/Target events. The supervisor also populates a `frame_tree` field in the snapshot so the agent can see the iframe structure of the current page, including cross-origin (OOPIF) iframes.

**Availability matrix:**

BackendDetection via `pending_dialogs`Response (`browser_dialog` tool)Local Chrome via `/browser connect` or `browser.cdp_url`✓✓ full workflowBrowserbase✓✓ full workflow (via injected XHR bridge)Camofox / default local agent-browser✗✗ (no CDP endpoint)

**How it works on Browserbase.** Browserbase's CDP proxy auto-dismisses real native dialogs server-side within ~10ms, so we can't use `Page.handleJavaScriptDialog`. The supervisor injects a small script via `Page.addScriptToEvaluateOnNewDocument` that overrides `window.alert`/`confirm`/`prompt` with a synchronous XHR. We intercept those XHRs via `Fetch.enable` — the page's JS thread stays blocked on the XHR until we call `Fetch.fulfillRequest` with the agent's response. `prompt()` return values round-trip back into page JS unchanged.

**Dialog policy** is configured in `config.yaml` under `browser.dialog_policy`:

PolicyBehavior`must_respond` (default)Capture, surface in snapshot, wait for explicit `browser_dialog()` call. Safety auto-dismiss after `browser.dialog_timeout_s` (default 300s) so a buggy agent can't stall forever.`auto_dismiss`Capture, dismiss immediately. Agent still sees the dialog in `browser_state` history but doesn't have to act.`auto_accept`Capture, accept immediately. Useful when navigating pages with aggressive `beforeunload` prompts.

**Frame tree** inside `browser_snapshot.frame_tree` is capped to 30 frames and OOPIF depth 2 to keep payloads bounded on ad-heavy pages. A `truncated: true` flag surfaces when limits were hit; agents needing the full tree can use `browser_cdp` with `Page.getFrameTree`.

## Practical Examples[​](#practical-examples "Direct link to Practical Examples")

### Filling Out a Web Form[​](#filling-out-a-web-form "Direct link to Filling Out a Web Form")

```text
User: Sign up for an account on example.com with my email john@example.com

Agent workflow:
1. browser_navigate("https://example.com/signup")
2. browser_snapshot()  → sees form fields with refs
3. browser_type(ref="@e3", text="john@example.com")
4. browser_type(ref="@e5", text="SecurePass123")
5. browser_click(ref="@e8")  → clicks "Create Account"
6. browser_snapshot()  → confirms success
```

### Researching Dynamic Content[​](#researching-dynamic-content "Direct link to Researching Dynamic Content")

```text
User: What are the top trending repos on GitHub right now?

Agent workflow:
1. browser_navigate("https://github.com/trending")
2. browser_snapshot(full=true)  → reads trending repo list
3. Returns formatted results
```

## Session Recording[​](#session-recording "Direct link to Session Recording")

Automatically record browser sessions as WebM video files:

```yaml
browser:
record_sessions:true# default: false
```

When enabled, recording starts automatically on the first `browser_navigate` and saves to `~/.hermes/browser_recordings/` when the session closes. Works in both local and cloud (Browserbase) modes. Recordings older than 72 hours are automatically cleaned up.

## Stealth Features[​](#stealth-features "Direct link to Stealth Features")

Browserbase provides automatic stealth capabilities:

FeatureDefaultNotesBasic StealthAlways onRandom fingerprints, viewport randomization, CAPTCHA solvingResidential ProxiesOnRoutes through residential IPs for better accessAdvanced StealthOffCustom Chromium build, requires Scale PlanKeep AliveOnSession reconnection after network hiccups

note

If paid features aren't available on your plan, Hermes automatically falls back — first disabling `keepAlive`, then proxies — so browsing still works on free plans.

## Session Management[​](#session-management "Direct link to Session Management")

- Each task gets an isolated browser session via Browserbase
- Sessions are automatically cleaned up after inactivity (default: 2 minutes)
- A background thread checks every 30 seconds for stale sessions
- Emergency cleanup runs on process exit to prevent orphaned sessions
- Sessions are released via the Browserbase API (`REQUEST_RELEASE` status)

## Limitations[​](#limitations "Direct link to Limitations")

- **Text-based interaction** — relies on accessibility tree, not pixel coordinates
- **Snapshot size** — large pages may be truncated or LLM-summarized at 8000 characters
- **Session timeout** — cloud sessions expire based on your provider's plan settings
- **Cost** — cloud sessions consume provider credits; sessions are automatically cleaned up when the conversation ends or after inactivity. Use `/browser connect` for free local browsing.
- **No file downloads** — cannot download files from the browser