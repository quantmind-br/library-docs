---
title: Size, opacity, & blurring | Warp
url: https://docs.warp.dev/terminal/appearance/size-opacity-blurring
source: sitemap
fetched_at: 2026-04-29T15:02:54.829876916-03:00
rendered_js: false
word_count: 235
summary: Configure Warp window dimensions, transparency, and background blur on macOS, Windows, and Linux.
tags:
    - terminal-settings
    - window-customization
    - ui-configuration
    - warp-terminal
    - desktop-app-settings
    - troubleshooting
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Size, Opacity, & Blurring

Customize Warp window dimensions, background transparency, and blur effects.

## Window Size

- **Settings** → **Appearance** → **Window** → enable **Open new windows with custom size**, then set columns and rows.

> [!info]
> If [[247-terminal-sessions-session-restoration|Session Restoration]] is enabled, Warp restores the last closed window's size. Ensure the custom-sized window is the last one closed, or disable Session Restoration.

![Window Size Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-79a7d9b64b98fad12b103e20f755d20d59d1f88c%252Fwindow_size_demo.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=267cc58b&sv=2)

## Window Opacity

- **Settings** → **Appearance** → **Window** → set opacity slider (`1`–`100`; `100` = fully opaque).

## Window Blurring

After lowering opacity below `100`:

- **macOS**: Use the blur slider to increase blur radius on the background image.
- **Windows**: Toggle Acrylic background texture on/off.
- **Linux**: Window blurring is not supported.

> [!warning]
> Large blur radii on macOS may affect performance, especially on Retina displays.

![Window Opacity and Blurring Demo](https://docs.warp.dev/~gitbook/image?url=https%3A%2F%2F4009768362-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPsjNxoJ0NFCXW6rRdHH3%252Fuploads%252Fgit-blob-example%252Fopacity-blur-demo.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=example&sv=2)

## Troubleshooting Transparency on Windows

> [!warning]
> Window opacity does **not work** on Windows when:
> - Using DirectX 12 as the rendering backend.
> - Using any backend with an Nvidia GPU when "Auto" or "Prefer layered" is selected for "Vulkan/OpenGL present method" in **NVIDIA Control Panel** → **Manage 3D Settings**.

### Solutions

- Select **Vulkan** or **OpenGL** as the preferred graphics backend: **Settings** → **Features** → **System** → **Preferred graphics backend**.
- Prefer integrated GPU rendering: **Settings** → **Features** → **System** → **Prefer rendering new windows with integrated GPU (low power)**.
