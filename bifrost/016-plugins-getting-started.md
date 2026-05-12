---
title: Getting Started
url: https://docs.getbifrost.ai/plugins/getting-started.md
source: llms
fetched_at: 2026-01-21T19:44:14.051990117-03:00
rendered_js: false
word_count: 522
summary: This document introduces Bifrost's plugin system, explaining how to extend gateway functionality by intercepting and modifying requests and responses using Go shared objects. It details the plugin architecture, building process, platform requirements, and execution lifecycle.
tags:
    - bifrost-gateway
    - go-plugins
    - dynamic-loading
    - shared-objects
    - request-lifecycle
    - middleware
    - plugin-architecture
category: guide
---

# Getting Started

> Learn how to extend Bifrost's functionality by creating custom plugins that intercept and modify requests and responses.

<Note>
  Dynamic plugins require dynamic builds of Bifrost which are not enabled by default to keep Bifrost setup easier. If you want to build and try custom plugins on OSS read [building dynamically linked Bifrost binary](./building-dynamic-binary)
</Note>

## What are Bifrost Plugins?

Bifrost plugins allow you to extend the gateway's functionality by intercepting requests and responses. Plugins can modify, log, validate, or enrich data as it flows through the system, giving you powerful hooks into Bifrost's request lifecycle.

## Use Cases

Custom plugins enable you to:

* **Transform requests and responses** - Modify data before it reaches providers or after it returns
* **Add custom validation** - Enforce business rules on incoming requests
* **Implement custom caching** - Cache responses based on custom logic
* **Integrate with external systems** - Send data to logging, monitoring, or analytics platforms
* **Apply custom transformations** - Parse, filter, or enrich LLM responses

## Plugin Architecture

<img src="https://mintcdn.com/bifrost/CzrSKWBKyCKO7kuB/media/dynamic-plugins-architecture.png?fit=max&auto=format&n=CzrSKWBKyCKO7kuB&q=85&s=93a72f8781c8910d6b281f6a5a403839" alt="architecture" data-og-width="2007" width="2007" data-og-height="936" height="936" data-path="media/dynamic-plugins-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/CzrSKWBKyCKO7kuB/media/dynamic-plugins-architecture.png?w=280&fit=max&auto=format&n=CzrSKWBKyCKO7kuB&q=85&s=29efabddffe6b467d7e88392381772a9 280w, https://mintcdn.com/bifrost/CzrSKWBKyCKO7kuB/media/dynamic-plugins-architecture.png?w=560&fit=max&auto=format&n=CzrSKWBKyCKO7kuB&q=85&s=29a891bb8aff15a74ef2fb43f1d7d473 560w, https://mintcdn.com/bifrost/CzrSKWBKyCKO7kuB/media/dynamic-plugins-architecture.png?w=840&fit=max&auto=format&n=CzrSKWBKyCKO7kuB&q=85&s=a91b7877dd3c10402bc23a439e881414 840w, https://mintcdn.com/bifrost/CzrSKWBKyCKO7kuB/media/dynamic-plugins-architecture.png?w=1100&fit=max&auto=format&n=CzrSKWBKyCKO7kuB&q=85&s=bbbe5d5d63bf68e9a88a74b6b682e734 1100w, https://mintcdn.com/bifrost/CzrSKWBKyCKO7kuB/media/dynamic-plugins-architecture.png?w=1650&fit=max&auto=format&n=CzrSKWBKyCKO7kuB&q=85&s=68d4946efa12ef8fff1e99f87a316b63 1650w, https://mintcdn.com/bifrost/CzrSKWBKyCKO7kuB/media/dynamic-plugins-architecture.png?w=2500&fit=max&auto=format&n=CzrSKWBKyCKO7kuB&q=85&s=6a1744cf4045a6f9a196a903b2a5f24b 2500w" />

Bifrost leverages **Go's native plugin system** to enable dynamic extensibility. Plugins are built as **shared object files** (`.so` files) that are loaded at runtime by the Bifrost gateway.

### How Go Plugins Work

Go plugins use the `plugin` package from the standard library, which allows Go programs to dynamically load code at runtime. Here's what makes this approach powerful:

* **Native Go Integration** - Plugins are written in Go and have full access to Bifrost's type system and interfaces
* **Dynamic Loading** - Plugins can be loaded, unloaded, and reloaded without restarting Bifrost
* **Type Safety** - Go's type system ensures plugin methods match expected signatures
* **Performance** - No IPC overhead; plugins run in the same process as Bifrost

### Building Shared Objects

Plugins must be compiled as shared objects using Go's `-buildmode=plugin` flag:

```bash  theme={null}
go build -buildmode=plugin -o myplugin.so main.go
```

This generates a `.so` file that exports specific functions matching Bifrost's plugin interface:

<Tabs>
  <Tab title="v1.4.x+">
    * `Init(config any) error` - Initialize the plugin with configuration
    * `GetName() string` - Return the plugin name
    * `HTTPTransportPreHook()` - Intercept HTTP requests before they enter Bifrost core (HTTP transport only)
    * `HTTPTransportPostHook()` - Intercept HTTP responses after they exit Bifrost core (HTTP transport only)
    * `PreHook()` - Intercept requests before they reach providers
    * `PostHook()` - Process responses after provider calls
    * `Cleanup() error` - Clean up resources on shutdown
  </Tab>

  <Tab title="v1.3.x">
    * `Init(config any) error` - Initialize the plugin with configuration
    * `GetName() string` - Return the plugin name
    * `TransportInterceptor()` - Modify raw HTTP headers/body (HTTP transport only)
    * `PreHook()` - Intercept requests before they reach providers
    * `PostHook()` - Process responses after provider calls
    * `Cleanup() error` - Clean up resources on shutdown
  </Tab>
</Tabs>

### Platform Requirements

**Important Limitations:**

* **Supported Platforms**: Linux and macOS (Darwin) only
* **No Cross-Compilation**: Plugins must be built on the target platform
* **Architecture Matching**: Plugin and Bifrost must use the same architecture (amd64, arm64)
* **Go Version Compatibility**: Plugin must be built with the same Go version as Bifrost

This means if you're running Bifrost on Linux AMD64, you must build your plugin on Linux AMD64 with the same Go version.

### Plugin Lifecycle

1. **Load** - Bifrost loads the `.so` file using Go's `plugin.Open()`
2. **Initialize** - Calls `Init()` with configuration from `config.json`
3. **Hook Execution** - Calls `PreHook()` and `PostHook()` for each request
4. **Cleanup** - Calls `Cleanup()` when Bifrost shuts down

Plugins execute in a specific order:

<Tabs>
  <Tab title="v1.4.x+">
    1. `HTTPTransportPreHook` - Intercept HTTP requests (HTTP transport only)
    2. `PreHook` - Executes in registration order, can short-circuit requests
    3. Provider call (if not short-circuited)
    4. `PostHook` - Executes in reverse order of PreHooks
    5. `HTTPTransportPostHook` - Intercept HTTP responses (HTTP transport only, reverse order)
  </Tab>

  <Tab title="v1.3.x">
    1. `TransportInterceptor` - Modifies raw HTTP requests (HTTP transport only)
    2. `PreHook` - Executes in registration order, can short-circuit requests
    3. Provider call (if not short-circuited)
    4. `PostHook` - Executes in reverse order of PreHooks
  </Tab>
</Tabs>

## Next Steps

Ready to build your first plugin? Choose your approach:

* **[Writing Go Plugins](./writing-go-plugin)** - Native Go plugins using shared objects (`.so` files). Best for performance and full Go ecosystem access.
* **[Writing WASM Plugins](./writing-wasm-plugin)** - Cross-platform plugins using WebAssembly. Write in TypeScript, Go (TinyGo), or Rust. No version matching required.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt