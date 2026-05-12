---
title: Browser | Firecrawl
url: https://docs.firecrawl.dev/features/browser
source: sitemap
fetched_at: 2026-03-23T07:24:53.77062-03:00
rendered_js: false
word_count: 854
summary: Firecrawl Browser Sandbox provides a secure, managed environment for AI agents to perform complex web interactions like form submission, authentication, and navigation without local infrastructure requirements.
tags:
    - browser-automation
    - ai-agents
    - headless-browser
    - playwright
    - web-scraping
    - sandbox-environment
category: concept
---

Firecrawl Browser Sandbox gives your agents a secure browser environment where agents can interact with the web. Fill out forms, click buttons, authenticate, and more. No local setup, no Chromium installs, no driver compatibility issues. Agent browser and playwright are pre-installed. Available via [API](https://docs.firecrawl.dev/api-reference/endpoint/browser-create), [CLI](https://docs.firecrawl.dev/sdks/cli#browser) (Bash / agent-browser, Python, Node), [Node SDK](https://docs.firecrawl.dev/sdks/node#browser), [Python SDK](https://docs.firecrawl.dev/sdks/python#browser), [Vercel AI SDK](https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk), and [MCP Server](https://docs.firecrawl.dev/mcp-server). To add browser support to an AI coding agent (Claude Code, Codex, Open Code, Cursor, etc.), install the Firecrawl skill:

```
npx -y firecrawl-cli@latest init --all --browser
```

Each session runs in an isolated, disposable or persistent sandbox that scales without managing infrastructure.

## Quick Start

Create a session, execute code, and close it:

- **No Driver Installation** - No Chromium binary, no `playwright install`, no driver compatibility issues
- **Python, JavaScript & Bash** - Send code via API, CLI, or SDK and get results back. All three languages run remotely in the sandbox
- **agent-browser** - Pre-installed CLI with 60+ commands. AI agents write simple bash commands instead of Playwright code
- **Playwright loaded** - Playwright comes pre-installed in the sandbox. Agents can write Playwright code if they prefer.
- **CDP Access** - Connect your own Playwright instance over WebSocket when you need full control
- **Live View** - Watch sessions in real time via embeddable stream URL
- **Interactive Live View** - Let users interact with the browser directly through an embeddable interactive stream

## Launch a Session

Returns a session ID, CDP URL, and live view URL.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

## Execute Code

Run Python, JavaScript, or bash code in your session. Output is returned via `stdout`; for Node.js, the last expression value is also available in `result`.

```
{
  "success": true,
  "stdout": "",
  "result": "Example Domain",
  "stderr": "",
  "exitCode": 0,
  "killed": false
}
```

### Handling File Downloads

Files downloaded inside a session can be captured and returned as base64. Use Playwright’s download API via the execute endpoint:

## agent-browser (Bash Mode)

[agent-browser](https://github.com/vercel-labs/agent-browser) is a headless browser CLI pre-installed in every sandbox. Instead of writing Playwright code, agents send simple bash commands. The CLI auto-injects `--cdp` so agent-browser connects to your active session automatically.

### Shorthand

The fastest way to use browser. Both the shorthand and `execute` send commands to agent-browser automatically. The shorthand just skips `execute` and auto-launches a session if needed:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

### CLI

The explicit form uses `execute`. Commands are sent to agent-browser automatically — you don’t need to type `agent-browser` or use `--bash`:

### API & SDK

Use `language: "bash"` to run agent-browser commands via the API or SDKs:

## Session Management

### Persistent Sessions

By default, each browser session starts with a clean slate. With `profile`, you can save and reuse browser state across sessions. This is useful for staying logged in and preserving preferences. To save or select a profile, use the `profile` parameter when creating a session.

ParameterDefaultDescription`name`—A name for the persistent profile. Sessions with the same name share storage.`saveChanges``true`When `true`, browser state is saved back to the profile on close. Set to `false` to load existing data without writing — useful when you need multiple concurrent readers.

The browser session state only saves when the session is closed. So we recommend closing the browser session when you are done with it so it can be reused. Once a session is closed, its session ID is no longer valid — you cannot reuse it. Instead, create a new session with the same profile name and use the new session ID returned in the response. To save and close it:

### List Sessions

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
      "liveViewUrl": "https://liveview.firecrawl.dev/...",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
      "createdAt": "2025-01-15T10:30:00Z",
      "lastActivity": "2025-01-15T10:35:00Z"
    }
  ]
}
```

### TTL Configuration

Sessions have two TTL controls:

ParameterDefaultDescription`ttl`600s (10 min)Maximum session lifetime (30-3600s)`activityTtl`300s (5 min)Auto-close after inactivity (10-3600s)

### Close a Session

## Live View

Every session returns a `liveViewUrl` in the response that you can embed to watch the browser in real time. Useful for debugging, demos, or building browser-powered UIs.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}

<iframe src="LIVE_VIEW_URL" width="100%" height="600" />
```

### Interactive Live View

The response also includes an `interactiveLiveViewUrl`. Unlike the standard live view which is view-only, the interactive live view allows users to click, type, and interact with the browser session directly through the embedded stream. This is useful for building user-facing browser UIs, collaborative debugging, or any scenario where the viewer needs to control the browser.

```
<iframe src="INTERACTIVE_LIVE_VIEW_URL" width="100%" height="600" />
```

## Connecting via CDP

Every session exposes a CDP WebSocket URL. The execute API and `--bash` flag cover most use cases, but if you need full local control you can connect directly.

## When to Use Browser

Use CaseRight ToolExtract content from a known URL[Scrape](https://docs.firecrawl.dev/features/scrape)Search the web and get results[Search](https://docs.firecrawl.dev/features/search)Navigate pagination, fill forms, click through flows**Browser**Multi-step workflows with interaction**Browser**Parallel browsing across many sites**Browser** (each session is isolated)

## Use Cases

- **Competitive intelligence** - Browse competitor sites, navigate search forms and filters, extract pricing and features into structured data
- **Knowledge base ingestion** - Navigate help centers, docs, and support portals that require clicks, pagination, or authentication
- **Market research** - Launch parallel browser sessions to build datasets from job boards, real estate listings, or legal databases

## Pricing

Pricing is straightforward: 2 credits per browser minute. Free users get 5 hours of free usage.

## Rate limits

For the initial launch, we allow all plans up to have up to 20 concurrent browser sessions.

## API Reference

- [Create Browser Session](https://docs.firecrawl.dev/api-reference/endpoint/browser-create)
- [Execute Browser Code](https://docs.firecrawl.dev/api-reference/endpoint/browser-execute)
- [List Browser Sessions](https://docs.firecrawl.dev/api-reference/endpoint/browser-list)
- [Delete Browser Session](https://docs.firecrawl.dev/api-reference/endpoint/browser-delete)

* * *

Have feedback or need help? Email [help@firecrawl.com](mailto:help@firecrawl.com) or reach out on [Discord](https://discord.gg/firecrawl).

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.