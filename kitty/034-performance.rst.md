---
title: Performance
url: https://github.com/kovidgoyal/kitty/blob/master/docs/performance.rst
source: git
fetched_at: 2026-05-04T15:58:19.440689016-03:00
rendered_js: false
word_count: 410
summary: kitty's performance architecture — glyph caching, threaded rendering, SIMD parsing, GPU-accelerated screen updates, and benchmarks against other terminal emulators.
tags:
    - terminal-emulator
    - performance-optimization
    - latency-benchmarking
    - system-resource-usage
    - rendering-optimization
category: concept
optimized: true
optimized_at: 2026-05-04T20:30:00Z
---
# Performance

kitty optimizes for: user-perceived typing latency, scroll smoothness, and CPU usage.

**Key techniques:**
- Glyph cache in video RAM (font rendering is never a bottleneck)
- Child process interaction in a separate thread from rendering
- SIMD vector instructions for byte stream parsing
- Screen updates sent as small GPU commands

Tunable via `repaint_delay`, `input_delay`, and `sync_to_monitor` in `conf-kitty-performance`.

## Benchmarks

Three axes: energy usage, keyboard-to-screen latency, and throughput.

### Keyboard-to-screen latency

Measured with Typometer or hardware. kitty achieves best-in-class latency on both macOS and Linux.

For minimum latency (at the cost of more energy):

```conf
input_delay 0
repaint_delay 2
sync_to_monitor no
wayland_enable_ime no
```

Hardware measurements on macOS show kitty and Apple Terminal.app tied for best latency. Typometer measurements on Linux show kitty far ahead of all tested terminals.

### Throughput

Measured with `kitten __benchmark__` (kitty binary). Suppresses rendering by default (`--render` to include it). kitty is twice as fast as the next best terminal.

Tested on AMD Ryzen 7 PRO 5850U, same font/size/window, default settings, Linux/X11:

| Terminal | ASCII | Unicode | CSI | Images | Average |
|----------|-------|---------|-----|--------|---------|
| kitty 0.33 | 121.8 | 105.0 | 59.8 | 251.6 | **134.55** |
| gnome-terminal 3.50.1 | 33.4 | 55.0 | 16.1 | 142.8 | 61.83 |
| alacritty 0.13.1 | 43.1 | 46.5 | 32.5 | 94.1 | 54.05 |
| wezterm 20230712 | 16.4 | 26.0 | 11.1 | 140.5 | 48.5 |
| xterm 389 | 47.7 | 18.3 | 0.6 | 56.3 | 30.72 |
| konsole 23.08.04 | 25.2 | 37.7 | 23.6 | 23.4 | 27.48 |
| alacritty+tmux | 30.3 | 7.8 | 14.7 | 46.1 | 24.73 |

CSI = typical formatting escape codes + ASCII text.

> [!NOTE]
> foot, iterm2, and Terminal.app excluded (don't run under X11). alacritty+tmux shows the cost of a multiplexer (halves throughput).

> [!NOTE]
> konsole, gnome-terminal, and xterm don't support Synchronized update escape codes. With support, their numbers would improve 20–50%.

### Energy usage

CPU usage while scrolling a file continuously in less (X + terminal process):

| Terminal | CPU usage |
|----------|-----------|
| kitty | 6–8% |
| xterm | 5–7% (scrolling very janky) |
| termite | 10–13% |
| urxvt | 12–14% |
| gnome-terminal | 15–17% |
| konsole | 29–31% |

kitty uses far less CPU than all terminals except xterm, with far better scrolling smoothness.

## Instrumenting kitty

Profile with gperftools:

```bash
make profile  # build with profiling
# Run kitty and perform the task
# KCachegrind displays function call stats on quit
```

Best done on Linux where KCachegrind is readily available.

#terminal-emulator #performance-optimization #latency-benchmarking
