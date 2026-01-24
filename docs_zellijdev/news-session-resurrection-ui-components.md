---
title: 'Zellij 0.39.0: Session Resurrection, Cross-Language UI Components, load Plugins from the Web'
url: https://zellij.dev/news/session-resurrection-ui-components/
source: sitemap
fetched_at: 2026-01-24T15:52:42.908567161-03:00
rendered_js: false
word_count: 331
summary: This document announces new features for the Zellij terminal multiplexer, including session resurrection, cross-language UI components for plugins, web-based plugin loading, and the ability to rename sessions.
tags:
    - zellij
    - terminal-multiplexer
    - session-management
    - plugin-development
    - ui-components
    - release-notes
category: other
---

2023-11-07

![Zellij session manager resurrection screen](https://zellij.dev/img/zellij-session-manager-resurrection.png)

## Session Resurrection

Zellij now includes built-in session resurrection capabilities. This means that Zellij sessions can be restored after reboots or graceful quits. Attaching to an exited session will resurrect it, allowing users to keep long-running named workspaces. Sessions are serialized as Human readable Zellij layouts, so they can also be shared across machines or between friends.

[Read more](http://zellij.dev/documentation/session-resurrection.html)

*Special thanks to [@AlixBernard](https://github.com/AlixBernard) for implementing the serialization algorithm, as well as to [@alekspickle](https://github.com/alekspickle) for helping integrate the algorithm with our code base. Without them this feature would not have come to be.*

## Cross-Language UI Components

![Cross platform ui components](https://zellij.dev/img/cross-language-ui-components.png)

This release gives Zellij plugins the ability to render beautiful and consistent UI components to build their visual layer. These components are cross-language, being serialized as private ANSI escape codes. Indeed, the Session Resurrection screen from the section above was developed exclusively with these components.

[Read more](http://zellij.dev/documentation/plugin-ui-rendering.html)

## Load Plugins from the Web

This release allows users to load Zellij plugins from the web with an `http(s)` prefix. This prefix will work inside layouts as well as when loading plugins at runtime.

This release also adds a `zellij plugin` CLI command, allowing users to eg.

```
zellij plugin -- https://example.com/plugin.wasm
```

or indeed

```
zellij plugin --floating -- https://example.com/plugin.wasm
```

*Special thanks to [@jaeheonji](https://github.com/jaeheonji) for designing and implementing this feature.*

## Allow Renaming Sessions

![Allow renaming sessions](https://zellij.dev/img/allow-renaming-sessions.png)

One of the most requested features after the recently added `session-manager` allowed users to switch between sessions was the ability to rename sessions.

This release adds this ability, both as a CLI command:

```
zellij action rename-session my-fantastic-session-new
```

or from the session-manager inside a running session: (`Ctrl o` + `w`).

## Do you like Zellij?

Me too! So much so that I spend 100% of my time developing and maintaining it and have no other income.

Zellij will always be free and open-source. Zellij will never contain ads.

So if the tool gives you value and you are able, please consider [a recurring monthly donation](https://github.com/sponsors/imsnif) of 5-10$ to help me pay my bills. There are Zellij stickers in it for you!