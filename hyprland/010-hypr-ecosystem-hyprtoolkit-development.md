---
title: Development
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprtoolkit/development/
source: sitemap
fetched_at: 2026-04-26T09:49:34.550556018-03:00
rendered_js: false
word_count: 652
summary: This document provides an introduction to the Hyprtoolkit C++ GUI framework, covering its retained-mode architecture, layout system, and event handling processes.
tags:
    - c-plus-plus
    - gui-framework
    - hyprland
    - retained-mode
    - layout-management
    - event-loop
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Hyprtoolkit is a pure C++ toolkit using modern C++ in the Hyprland style (with hyprutils). Familiarity with C++ is recommended.

> [!tip]
> For examples, see the `tests/` directory in the hyprtoolkit repo.

## Getting Started

Create a backend and open a window:

```cpp
using namespace Hyprtoolkit;
auto backend = CBackend::create();
auto window = CWindowBuilder::begin()->appTitle("Hello")->appClass("hyprtoolkit")->commence();
```

Hyprtoolkit is a retained mode toolkit — define your layout in C++ and forget about it.

Add a background rectangle using the palette:

```cpp
window->m_rootElement->addChild(CRectangleBuilder::begin()->color([] { return backend->getPalette()->m_colors.background; })->commence());
```

> [!note]
> Use the palette so your app adheres to the user's theme.

Add a column layout with buttons:

```cpp
auto layout = CColumnLayoutBuilder::begin()->size({CDynamicSize::HT_SIZE_PERCENT, CDynamicSize::HT_SIZE_PERCENT, {1.F, 1.F}})->commence();
layout->setMargin(3);
window->m_rootElement->addChild(layout);
layout->addChild(CButtonBuilder::begin()
                       ->label("Do something")
                       ->onMainClick([](SP<CButtonElement> el) { std::println("Did something!"); })
                       ->size({CDynamicSize::HT_SIZE_AUTO, CDynamicSize::HT_SIZE_AUTO, {1, 1}})
                       ->commence()
                );
layout->addChild(CButtonBuilder::begin()
                       ->label("Do something else")
                       ->onMainClick([](SP<CButtonElement> el) { std::println("Did something else!"); })
                       ->size({CDynamicSize::HT_SIZE_AUTO, CDynamicSize::HT_SIZE_AUTO, {1, 1}})
                       ->commence()
                );
```

Buttons have automatic sizing and fit their contents.

Add a close callback, open the window, and enter the main loop:

```cpp
window->m_events.closeRequest.listenStatic([w = WP<IWindow>{window}] {
    w->close();
    backend->destroy();
});
window->open();
backend->enterLoop();
```

## Layout System

The layout system uses absolute and layout positioning modes.

### Absolute Mode

Triggered when the parent is not a `ColumnLayout` or `RowLayout`. Children are positioned within their parent according to their position mode:

| Mode | Behavior |
|---|---|
| `CENTER` via `setPositionMode` | Centers child inside parent |
| `ABSOLUTE` via `setPositionMode` | Places child in top-left corner |
| `setAbsolutePosition({200, 200})` | Moves child 200 layout px down and right from parent's top-left |

### Layout Mode

Triggered when the parent is a layout (ColumnLayout or RowLayout). Positions children similarly to CSS `flex` or Qt's `RowLayout`/`ColumnLayout`, but without wrapping. Overflowing elements that cannot shrink disappear.

- `RowLayout` — positions elements side-by-side
- `ColumnLayout` — positions elements top-to-bottom

### Size

All elements carry a `SizeType` that tells the layout system how to size the element:

| SizeType | Behavior |
|---|---|
| `ABSOLUTE` | Takes layout px as size, element is rigid |
| `PERCENT` | Takes `(0, 0) - (1, 1)` percentage of parent size |
| `AUTO` | Attempts to contain children (ignores passed vector) |

> [!note]
> Some elements force their own sizing (e.g., `Text`). Leave those `AUTO` to avoid confusion.

## Elements

Most elements are self-explanatory — browse their builder functions for styling and behavior options.

Each element uses a `Builder` for ABI stability. Calling `->commence()` returns an `SP` to the newly created object.

- Rebuild at any time with `->rebuild()` (remember to call `->commence()` after changes)
- You do not need to keep the `SP` after adding the element to the tree with `addChild`

## System Icons

Use `CBackend::systemIcons()` to get an `ISystemIconFactory` for querying system icons by name. Check if the icon was found, then attach the result to an `ImageElement`.

## Additional FDs

hyprtoolkit is strictly single-threaded for layout and rendering — you cannot edit the layout from another thread.

For apps depending on other loops (pipewire, dbus, etc.), use `CBackend::addFd()` to add a file descriptor to the loop with a callback function. The callback is called from the main thread when the fd is readable.