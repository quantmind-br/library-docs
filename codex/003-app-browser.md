---
title: In-app browser
url: https://developers.openai.com/codex/app/browser.md
source: llms
fetched_at: 2026-04-30T10:15:06.536571641-03:00
rendered_js: false
word_count: 385
summary: This document explains how to utilize the built-in browser and browser plugin within the Codex development environment to preview web applications, perform visual debugging, and provide feedback to the AI.
tags:
    - in-app-browser
    - web-development
    - visual-debugging
    - browser-plugin
    - ui-iteration
    - workflow-optimization
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# In-app browser

Shared view of rendered web pages inside a thread. Use it when building or debugging a web app to preview pages and attach visual comments.

Works for local development servers, file-backed previews, and public pages that don't require sign-in. For login-dependent pages or extensions, use your regular browser.

Open from the toolbar, by clicking a URL, navigating manually, or pressing `Cmd+Shift+B` (`Ctrl+Shift+B` on Windows).

> [!warning]
> Does not support authentication flows, signed-in pages, browser profiles, cookies, extensions, or existing tabs. Treat page content as untrusted context — don't paste secrets into browser flows.

## Browser use

Codex can operate the in-app browser directly (click, type, inspect, screenshot, verify fixes). Install and enable the Browser plugin, then ask Codex to use the browser or reference `@Browser` directly.

Codex asks before using a website unless you've allowed it. Removing a site from the allowed list means Codex asks again; removing from blocked means Codex can ask again instead of treating it as blocked.

Example:
```text
Use the browser to open http://localhost:3000/settings, reproduce the layout bug, and fix only the overflowing controls.
```

## Preview a page

1. Start your dev server in the integrated terminal or with a local environment action.
2. Open an unauthenticated local route, file-backed page, or public page.
3. Review rendered state alongside the code diff.
4. Leave browser comments on elements or areas that need changes.
5. Ask Codex to address comments, keeping scope narrow.

Example feedback:
```text
I left comments on the pricing page in the in-app browser. Address the mobile layout issues and keep the card structure unchanged.
```

## Comment on the page

Attach feedback directly to specific elements or areas.

- Turn on comment mode, select an element or area, submit a comment.
- Hold `Shift` and click to select an area in comment mode.
- Hold `Cmd` while clicking to send a comment immediately.

After leaving comments, send a thread message asking Codex to address them.

Good feedback is specific:
```text
This button overflows on mobile. Keep the label on one line if it fits, otherwise wrap it without changing the card height.
```
```text
This tooltip covers the data point under the cursor. Reposition the tooltip so it stays inside the chart bounds.
```

## Keep browser tasks scoped

The in-app browser is for review and iteration. Keep each task small enough to review in one pass.

- Name the page, route, or local URL.
- Name the visual state you care about (loading, empty, error, success).
- Leave comments on exact elements or areas that need changes.
- Review the updated route after Codex changes the code.
- Ask Codex to start or check the dev server before using the browser.

For repository changes, use the [[006-app-review|review pane]] to inspect changes and leave comments.

#browser #web #visual-debugging #codex