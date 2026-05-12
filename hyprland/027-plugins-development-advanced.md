---
title: Advanced
url: https://wiki.hypr.land/Plugins/Development/Advanced/
source: sitemap
fetched_at: 2026-04-26T09:47:44.564453461-03:00
rendered_js: false
word_count: 433
summary: Advanced Hyprland Plugin API techniques covering member access manipulation, function hooking for interception, and config value management.
tags:
    - hyprland
    - plugin-api
    - cpp
    - function-hooking
    - configuration-management
    - linux-compositor
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

This page documents advanced techniques in the Hyprland Plugin API.

## Accessing private members[](#accessing-private-members)

Use a macro to change visibility to public for Hyprland class members. If STL includes break, add the offensive STL import before the Hyprland include.

```cpp
#define private public
#include <hyprland/src/plugins/PluginAPI.hpp>
#include <hyprland/src/render/OpenGL.hpp>
#include <hyprland/src/desktop/Window.hpp>
#include <hyprland/src/layout/IHyprLayout.hpp>
#undef private
```

## Using Function Hooks[](#using-function-hooks)

> [!warning]
> Function hooks are only available on `AMD64` (`x86_64`). Hooking on other architectures is silently ignored.

Function hooks intercept any call to a hooked function, allowing you to run code before/after, modify inputs/results, or block execution entirely.

### Basic hook example[](#basic-hook-example)

```cpp
void Events::listener_monitorFrame(void* owner, void* data)
```

`Events::` is a namespace, so this is a plain function.

```cpp
// global instance of the hook class
inline CFunctionHook* g_pMonitorFrameHook = nullptr;
// pointer typedef for the hooked function
typedef void (*origMonitorFrame)(void*, void*);
// hook handler
void hkMonitorFrame(void* owner, void* data) {
    (*(origMonitorFrame)g_pMonitorFrameHook->m_pOriginal)(owner, data);
}
APICALL EXPORT PLUGIN_DESCRIPTION_INFO PLUGIN_INIT(HANDLE handle) {
    // create the hook
    static const auto METHODS = HyprlandAPI::findFunctionsByName(PHANDLE, "listener_monitorFrame");
    g_pMonitorFrameHook = HyprlandAPI::createFunctionHook(handle, METHODS[0].address, (void*)&hkMonitorFrame);
    g_pMonitorFrameHook->hook();
}
```

Whenever Hyprland calls `Events::listener_monitorFrame`, the hook runs instead.

`CFunctionHook` supports `unhook()` and `hook()` to toggle at runtime.

### Member functions[](#member-functions)

For member functions like `CCompositor::focusWindow(CWindow*, wlr_surface*)`, add the `thisptr` argument:

```cpp
typedef void (*origFocusWindow)(void*, CWindow*, wlr_surface*);
void hkFocusWindow(void* thisptr, CWindow* pWindow, wlr_surface* pSurface) {
    // call original
    (*(origFocusWindow)g_pFocusWindowHook->m_pOriginal)(thisptr, pWindow, pSurface);
}
APICALL EXPORT PLUGIN_DESCRIPTION_INFO PLUGIN_INIT(HANDLE handle) {
    static const auto METHODS = HyprlandAPI::findFunctionsByName(PHANDLE, "focusWindow");
    g_pFocusWindowHook = HyprlandAPI::createFunctionHook(handle, METHODS[0].address, (void*)&hkFocusWindow);
    g_pFocusWindowHook->hook();
}
```

> [!warning]
> Method lookups are slow. Entries never change at runtime, so make lookups `static`.

### Why use findFunctionsByName?[](#why-use-findfunctionsbyname)

1. **Resilience** — address may become invalid after Hyprland updates; `findFunctionsByName` stays valid as long as the function exists.
2. **Error handling** — method array contains signatures to verify you got the right function.

## Using the config[](#using-the-config)

Register config values in `PLUGIN_INIT`:

```cpp
APICALL EXPORT PLUGIN_DESCRIPTION_INFO PLUGIN_INIT(HANDLE handle) {
    HyprlandAPI::addConfigValue(PHANDLE, "plugin:example:exampleInt", SConfigValue{.intValue = 1});
}
```

Plugin variables **must** be in the `plugins:` category. Group variables under a subcategory named for your plugin: `plugins:myPlugin:variable1`.

Retrieve values with `HyprlandAPI::getConfigValue`. The pointer never changes after `PLUGIN_INIT`, so make it static for performance:

```cpp
static auto* const MYVAR = &HyprlandAPI::getConfigValue(PHANDLE, "plugin:myPlugin:variable1")->intValue;
```

## Further[](#further)

Read the API at `src/plugins/PluginAPI.hpp` and check out the [official plugins](https://github.com/hyprwm/hyprland-plugins).

Have fun!