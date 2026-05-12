---
title: Full-screen apps | Warp
url: https://docs.warp.dev/terminal/more-features/full-screen-apps
source: sitemap
fetched_at: 2026-04-29T15:03:07.694827977-03:00
rendered_js: false
word_count: 209
summary: Configure mouse/scroll reporting and full-screen app padding in Warp.
tags:
    - warp-terminal
    - mouse-reporting
    - scroll-reporting
    - terminal-configuration
    - ui-customization
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Full-Screen Apps

Configure mouse/scroll reporting and padding surrounding full-screen applications.

## Mouse and Scroll Reporting

Forward mouse and scroll events to the running app (e.g., `vim`) or handle them in Warp.

> [!info]
> Mouse reporting must be enabled first to toggle scroll reporting. When enabled, Warp uses ANSI escape sequences to communicate mouse events to the app. Hold `SHIFT` to send a mouse event to Warp instead (e.g., for text selection).

### Enable

- **Settings** → **Features** → **Terminal** → **Enable Mouse Reporting** → toggle **Scroll Reporting** (after enabling mouse reporting)
- [[101-terminal-command-palette|Command Palette]] → search "Toggle Mouse Reporting"
- macOS Menu → **View** → **Toggle Mouse Reporting**

![Mouse and Scroll Reporting Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-example%252Fmouse-scroll-demo.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=example&sv=2)

## Padding

Configure padding around full-screen apps. Default is `0px`. Warp allows scaling by fractions of a cell width/height; extra space appears as padding on the right/bottom.

### Configure

- **Settings** → **Appearance** → **Full-screen Apps** (or [[101-terminal-command-palette|Command Palette]] → "Appearance")
  - **Use custom padding in alt-screen**: enabled by default — disable to match [[224-terminal-blocks|Blocklist]] padding
  - **Uniform padding (px)**: default `0px`

> [!warning]
> Some full-screen applications don't behave well when resizing. If you experience rendering issues, turn this setting off so full-screen apps don't need to resize on startup.

![Alt-screen padding setting](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-f389a59e0d72e737fdf978fe65e59ef32ad2ceeb%252Fpadding-settings.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a46b883d&sv=2)
