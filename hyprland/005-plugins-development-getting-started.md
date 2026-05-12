---
title: Getting started
url: https://wiki.hypr.land/Plugins/Development/Getting-Started/
source: sitemap
fetched_at: 2026-04-26T09:47:17.179991716-03:00
rendered_js: false
word_count: 597
summary: This document provides a foundational guide for developing plugins for the Hyprland compositor using C++, including setup requirements, necessary boilerplate code, and development workflows.
tags:
    - hyprland
    - c-plus-plus
    - plugin-development
    - compositor
    - linux-desktop
    - software-extensibility
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Plugins are dynamic objects loaded by Hyprland with (almost) full access to Hyprland's internals — enabling far more modification than scripts.

## Prerequisites

- Knowledge of C++
- Ability to read
- Rough understanding of Hyprland internals (can learn alongside development)

## Making Your First Plugin

### Setup

**Option A — If you have Hyprland headers:**
Install with `make install`. No further action required.

**Option B — If you don't have Hyprland source cloned:**

```sh
git clone https://github.com/hyprwm/Hyprland
cd Hyprland && make debug && sudo make installheaders && cd ..
```

Then look at simple plugins in the [official plugins repo](https://github.com/hyprwm/hyprland-plugins) (e.g., `csgo-vulkan-fix`, `hyprwinwrap`) or start from scratch.

### Plugin Boilerplate

Include the plugin API:

```cpp
#include <hyprland/src/plugins/PluginAPI.hpp>
```

Create a global handle pointer:

```cpp
inline HANDLE PHANDLE = nullptr;
```

Declare the API version function (do not change this):

```cpp
APICALL EXPORT std::string PLUGIN_API_VERSION() {
    return HYPRLAND_API_VERSION;
}
```

Implement the init and exit functions:

```cpp
APICALL EXPORT PLUGIN_DESCRIPTION_INFO PLUGIN_INIT(HANDLE handle) {
    PHANDLE = handle;
    const std::string COMPOSITOR_HASH = __hyprland_api_get_hash();
    const std::string CLIENT_HASH = __hyprland_api_get_client_hash();
    // ALWAYS add this — prevents crashes from mismatched header versions
    if (COMPOSITOR_HASH != CLIENT_HASH) {
        HyprlandAPI::addNotification(PHANDLE, "[MyPlugin] Mismatched headers! Can't proceed.",
                                     CHyprColor{1.0, 0.2, 0.2, 1.0}, 5000);
        throw std::runtime_error("[MyPlugin] Version mismatch");
    }
    // ... plugin initialization here
    return {"MyPlugin", "An amazing plugin!", "Me", "1.0"};
}

APICALL EXPORT void PLUGIN_EXIT() {
    // ... cleanup here
}
```

Key points:
- `PLUGIN_INIT` is called when the plugin is loaded. Initialize everything here.
- Adding config variables is only allowed in `PLUGIN_INIT`.
- Store the `HANDLE` — required for API calls.
- Return `PLUGIN_DESCRIPTION_INFO` with name, description, author, version.
- `PLUGIN_EXIT` is called when the plugin is unloaded. Not called if plugin committed a fault.
- Hyprland automatically cleans up layouts, config options, dispatchers, window decorations, and hooks — no need to unregister them in the exit function.

## Development Environment

Use a nested debug Hyprland session unless you need real hardware (e.g., trackpad gestures).

See [[090-contributing-and-debugging|Contributing and Debugging]] for setup instructions.

## Loading / Reloading Plugins

```sh
# Load
hyprctl plugin load /absolute/path/to/plugin.so

# Unload
hyprctl plugin unload /absolute/path/to/plugin.so

# Reload (one-liner)
hyprctl plugin unload /absolute/path/to/plugin.so ; hyprctl plugin load /absolute/path/to/plugin.so
```

Normal development cycle: load → check changes → build → unload → load → repeat.

## Further Reading

See `src/plugins/PluginAPI.hpp` for all available methods with comments. For advanced concepts, see [[027-plugins-development-advanced|Advanced]] and [[028-plugins-development-plugin-guidelines|Plugin Guidelines]].