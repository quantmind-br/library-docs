---
title: Integrations with other tools
title: Integrations with other tools
word_count: 644
summary: Curated list of third-party tools integrating with kitty via graphics and remote-control protocols.
category: reference
optimized: true
optimized_at: 2026-05-04T20:46:03Z
---
# Integrations with other tools

kitty provides powerful interfaces: [[028-remote-control|remote-control]], [[008-kittens-custom|custom kittens]], and [[014-kittens-icat|icat]] for seamless tool integration.

## Image and document viewers

Powered by kitty's [[049-graphics-protocol|graphics protocol]], these tools view images/docs directly in the terminal, even over SSH.

| Tool | Description |
|------|-------------|
| [bookokrat](https://github.com/bugzmanov/bookokrat) | Terminal PDF/EPUB viewer |
| [termpdf.py](https://github.com/dsanson/termpdf.py) | Terminal PDF/DJVU/CBR viewer |
| [tdf](https://github.com/itsjunetime/tdf) | Terminal PDF viewer |
| [fancy-cat](https://github.com/freref/fancy-cat) | Terminal PDF viewer |
| [meowpdf](https://github.com/monoamine11231/meowpdf) | PDF viewer with GUI-like usage, Vim keybindings (Rust) |
| [mcat](https://github.com/Skardyy/mcat) | Display files with images, formatted |
| [dawn](https://github.com/andrewmd5/dawn) | Markdown editor using text-sizing + graphics protocols |
| [presenterm](https://github.com/mfontanini/presenterm) | Markdown slides with images |
| [mdfried](https://github.com/benjajaja/mdfried) | Markdown viewer with text-sizing + graphics |
| [term-image](https://github.com/AnonymouX47/term-image) | Browse images in terminal |
| [koneko](https://github.com/twenty5151/koneko) | Browse pixiv artist images |
| [viu](https://github.com/atanunq/viu) | View images in terminal |
| [nb](https://github.com/xwmx/nb) | CLI note-taking/bookmarking with graphics |
| [w3m](https://github.com/tats/w3m) | Text WWW browser with graphics support |
| [awrit](https://github.com/chase/awrit) | Chromium-based web browser in terminal |
| [chawan](https://sr.ht/~bptato/chawan/) | Text WWW browser with graphics support |
| [mpv](https://github.com/mpv-player/mpv) | Video player in terminal |

```bash
mpv --profile=sw-fast --vo=kitty --vo-kitty-use-shm=yes --really-quiet video.mkv
```

| Tool | Description |
|------|-------------|
| [timg](https://github.com/hzeller/timg) | Terminal image/video viewer, multi-threaded, JPEG exif, webcam |

## File managers

| Manager | Features |
|---------|----------|
| [ranger](https://github.com/ranger/ranger) | Preview content via graphics protocol |
| [nnn](https://github.com/jarun/nnn/) | Preview content via graphics protocol |
| [Yazi](https://github.com/sxyazi/yazi) | Fast, built-in kitty graphics (Classic + Unicode placeholders) |
| [clifm](https://github.com/leo-arch/clifm) | Shell-like, uses graphics + keyboard protocols |
| [hunter](https://github.com/rabite0/hunter) | Preview content via graphics protocol |
| [far2l](https://github.com/elfmz/far2l) | Dual panel file manager + terminal emulator |

## System and data visualization

| Tool | Description |
|------|-------------|
| [neofetch](https://github.com/dylanaraps/neofetch) | System info with graphics |
| [matplotlib-backend-kitty](https://github.com/jktr/matplotlib-backend-kitty) | Matplotlib backend |
| [kitcat](https://github.com/mil-ad/kitcat) | Matplotlib backend |
| [KittyTerminalImages.jl](https://github.com/simonschoelly/KittyTerminalImages.jl) | Julia image display |
| [euporie](https://github.com/joouha/euporie) | Jupyter notebooks TUI with plots |
| [gnuplot](http://www.gnuplot.info/) | Graphics with kittygd/kittycairo backends |
| [k-nine](https://github.com/talwrii/kitty-plotnine) | Plotnine wrapper for bash one-liners |
| [tgutui](https://github.com/tgu-ltd/tgutui) | Terminal operating test hardware |
| [onefetch](https://github.com/o2sh/onefetch) | Git repo info |
| [patat](https://github.com/jaspervdj/patat) | Pandoc presentations |
| [wttr.in](https://github.com/chubin/wttr.in) | Weather in terminal |
| [wl-clipboard-manager](https://github.com/maximbaz/wl-clipboard-manager) | Wayland clipboard under kitty |
| [NEMU](https://github.com/nemuTUI/nemu) | QEMU TUI, displays VM via graphics |

## Editor integration

Split windows, previews, REPLs via kitty native windows.

| Editor | Integration |
|--------|-------------|
| [kakoune](https://kakoune.org/) | Native kitty windows for panels/REPLs |
| [vim-slime](https://github.com/jpalardy/vim-slime#kitty) | kitty RC for Lisp REPL |
| [vim-kitty-navigator](https://github.com/knubie/vim-kitty-navigator) | Navigate vim/kitty splits |
| [vim-test](https://github.com/vim-test/vim-test) | Run tests in terminal |

### Image plugins

- [snacks.nvim](https://github.com/folke/snacks.nvim) - Inline images in neovim
- [image.nvim](https://github.com/3rd/image.nvim) - Images in neovim
- [image_preview.nvim](https://github.com/adelarsq/image_preview.nvim/) - Image preview for neovim
- [hologram.nvim](https://github.com/edluffy/hologram.nvim) - View images in neovim
- [kitty-graphics.el](https://github.com/cashmeredev/kitty-graphics.el) - View images in emacs

## Scrollback manipulation

| Tool | Description |
|------|-------------|
| [kitty-scrollback.nvim](https://github.com/mikesmithgh/kitty-scrollback.nvim) | Browse scrollback with Neovim |
| [kitty-search](https://github.com/trygveaa/kitty-kitten-search) | Live incremental scrollback search |
| [kitty-grab](https://github.com/yurikhan/kitty_grab) | Keyboard text selection for scrollback |

## Desktop panels

| Panel | Description |
|-------|-------------|
| [kitty panel](https://github.com/5hubham5ingh/kitty-panel) | Real-time system metrics |
| [pawbar](https://github.com/codelif/pawbar) | kitten-panel based desktop panel |

## Password managers

| Manager | Integration |
|---------|-------------|
| [1password](https://github.com/mm-zacharydavison/kitty-kitten-1password) | Inject passwords from 1Password |
| [BitWarden](https://github.com/dnanhkhoa/kitty-password-manager) | Inject passwords from BitWarden |

## Miscellaneous

| Tool | Description |
|------|-------------|
| [terminal-doom](https://github.com/cryptocode/terminal-doom) | Play DOOM in kitty |
| [actually-doom.nvim](https://github.com/seandewar/actually-doom.nvim) | DOOM inside neovim inside kitty |
| [gattino](https://github.com/salvozappa/gattino) | LLM for plain language → shell commands |
| [kitty-smart-tab](https://github.com/yurikhan/kitty-smart-tab) | Control tabs or pass to apps |
| [kitty-smart-scroll](https://github.com/yurikhan/kitty-smart-scroll) | Scroll or pass to apps |
| [kitti3](https://github.com/LandingEllipse/kitti3) | Drop-down terminal under i3 |
| [weechat-hints](https://github.com/GermainZ/kitty-weechat-hints) | URL hints for WeeChat |
| [glkitty](https://github.com/michaeljclark/glkitty) | OpenGL shaders in terminal (glgears demo) |

#kitty-terminal #graphics-protocol #remote-control #cli-tools
