---
title: '`lms link disable`'
url: https://lmstudio.ai/docs/cli/link/link-disable
source: sitemap
fetched_at: 2026-04-07T21:28:09.902669394-03:00
rendered_js: false
word_count: 247
summary: This documentation provides a command-line interface (CLI) reference for managing various aspects of LM Studio, including local model operations, server management, daemon control, and the enabling or disabling of the LM Link feature.
tags:
    - cli
    - local-models
    - server
    - daemon
    - lm-link
    - documentation
category: reference
---

Documentation

[![lmstudio icon](https://lmstudio.ai/_next/static/media/mcp-install.b2052392.svg)  
\
App](https://lmstudio.ai/docs/app)

[![developer logo](https://lmstudio.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdev-logo.7a6f42a1.jpg&w=48&q=75)  
\
Developer Docs](https://lmstudio.ai/docs/developer)[LM Link](https://lmstudio.ai/docs/lmlink)[lmstudio-js](https://lmstudio.ai/docs/typescript)[lmstudio-python](https://lmstudio.ai/docs/python)[CLI](https://lmstudio.ai/docs/cli)[Integrations](https://lmstudio.ai/docs/integrations)

[Introduction](https://lmstudio.ai/docs/cli)

[Contributing](https://lmstudio.ai/docs/cli/contributing)

Local Models

[`lms chat`](https://lmstudio.ai/docs/cli/local-models/chat)

[`lms get`](https://lmstudio.ai/docs/cli/local-models/get)

[`lms load`](https://lmstudio.ai/docs/cli/local-models/load)

[`lms ls`](https://lmstudio.ai/docs/cli/local-models/ls)

[`lms ps`](https://lmstudio.ai/docs/cli/local-models/ps)

[`lms import`](https://lmstudio.ai/docs/cli/local-models/import)

serve

[`lms server start`](https://lmstudio.ai/docs/cli/serve/server-start)

[`lms server status`](https://lmstudio.ai/docs/cli/serve/server-status)

[`lms server stop`](https://lmstudio.ai/docs/cli/serve/server-stop)

[`lms log stream`](https://lmstudio.ai/docs/cli/serve/log-stream)

daemon

[`lms daemon up`](https://lmstudio.ai/docs/cli/daemon/daemon-up)

[`lms daemon down`](https://lmstudio.ai/docs/cli/daemon/daemon-down)

[`lms daemon status`](https://lmstudio.ai/docs/cli/daemon/daemon-status)

[`lms daemon update`](https://lmstudio.ai/docs/cli/daemon/daemon-update)

link

[`lms link enable`](https://lmstudio.ai/docs/cli/link/link-enable)

[`lms link disable`](https://lmstudio.ai/docs/cli/link/link-disable)

[`lms link status`](https://lmstudio.ai/docs/cli/link/link-status)

[`lms link set-device-name`](https://lmstudio.ai/docs/cli/link/link-set-device-name)

[`lms link set-preferred-device`](https://lmstudio.ai/docs/cli/link/link-set-preferred-device)

runtime

[`lms runtime`](https://lmstudio.ai/docs/cli/runtime/runtime)

Develop and Publish (Beta)

[`lms clone`](https://lmstudio.ai/docs/cli/develop-and-publish/clone)

[`lms push`](https://lmstudio.ai/docs/cli/develop-and-publish/push)

[`lms dev`](https://lmstudio.ai/docs/cli/develop-and-publish/dev)

[`lms login`](https://lmstudio.ai/docs/cli/develop-and-publish/login)

[Introduction](https://lmstudio.ai/docs/cli)

[Contributing](https://lmstudio.ai/docs/cli/contributing)

Local Models

[`lms chat`](https://lmstudio.ai/docs/cli/local-models/chat)

[`lms get`](https://lmstudio.ai/docs/cli/local-models/get)

[`lms load`](https://lmstudio.ai/docs/cli/local-models/load)

[`lms ls`](https://lmstudio.ai/docs/cli/local-models/ls)

[`lms ps`](https://lmstudio.ai/docs/cli/local-models/ps)

[`lms import`](https://lmstudio.ai/docs/cli/local-models/import)

serve

[`lms server start`](https://lmstudio.ai/docs/cli/serve/server-start)

[`lms server status`](https://lmstudio.ai/docs/cli/serve/server-status)

[`lms server stop`](https://lmstudio.ai/docs/cli/serve/server-stop)

[`lms log stream`](https://lmstudio.ai/docs/cli/serve/log-stream)

daemon

[`lms daemon up`](https://lmstudio.ai/docs/cli/daemon/daemon-up)

[`lms daemon down`](https://lmstudio.ai/docs/cli/daemon/daemon-down)

[`lms daemon status`](https://lmstudio.ai/docs/cli/daemon/daemon-status)

[`lms daemon update`](https://lmstudio.ai/docs/cli/daemon/daemon-update)

link

[`lms link enable`](https://lmstudio.ai/docs/cli/link/link-enable)

[`lms link disable`](https://lmstudio.ai/docs/cli/link/link-disable)

[`lms link status`](https://lmstudio.ai/docs/cli/link/link-status)

[`lms link set-device-name`](https://lmstudio.ai/docs/cli/link/link-set-device-name)

[`lms link set-preferred-device`](https://lmstudio.ai/docs/cli/link/link-set-preferred-device)

runtime

[`lms runtime`](https://lmstudio.ai/docs/cli/runtime/runtime)

Develop and Publish (Beta)

[`lms clone`](https://lmstudio.ai/docs/cli/develop-and-publish/clone)

[`lms push`](https://lmstudio.ai/docs/cli/develop-and-publish/push)

[`lms dev`](https://lmstudio.ai/docs/cli/develop-and-publish/dev)

[`lms login`](https://lmstudio.ai/docs/cli/develop-and-publish/login)

link

Disable LM Link on this device from the CLI.

The `lms link disable` command disables LM Link on this device. The device will no longer connect to or be visible to other devices on the link.

## Disable LM Link[](#disable-lm-link "Link to 'Disable LM Link'")

```

lms link disable
```

You can re-enable LM Link at any time with [`lms link enable`](https://lmstudio.ai/docs/cli/link/link-enable).

### Learn more[](#learn-more)

See the [LM Link documentation](https://lmstudio.ai/docs/lmlink) for a full overview of LM Link.

This page's source is available on [GitHub](https://github.com/lmstudio-ai/docs/blob/main/3_cli/3_link/link-disable.md)

On this page

Disable LM Link

Learn more

[Page Source](https://github.com/lmstudio-ai/docs/blob/main/3_cli/3_link/link-disable.md "View source on GitHub")[Edit on GitHub](https://github.com/lmstudio-ai/docs/edit/main/3_cli/3_link/link-disable.md "Edit this page")