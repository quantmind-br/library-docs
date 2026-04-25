---
title: '`lms link set-preferred-device`'
url: https://lmstudio.ai/docs/cli/link/link-set-preferred-device
source: sitemap
fetched_at: 2026-04-07T21:28:03.510303007-03:00
rendered_js: false
word_count: 98
summary: This document explains how to use the `lms link set-preferred-device` command to designate a specific device as the primary source when an AI model is accessible through multiple connected devices.
tags:
    - lms
    - link-management
    - device-selection
    - cli-command
    - model-routing
category: reference
---

The `lms link set-preferred-device` command sets which device on the link is used when a model is available on multiple connected devices.

## Set a preferred device[](#set-a-preferred-device "Link to 'Set a preferred device'")

Run the command without arguments to pick from an interactive list of connected devices:

```

lms link set-preferred-device
```

Or pass the device identifier directly to skip the prompt:

```

lms link set-preferred-device <deviceIdentifier>
```

Device identifiers are listed in the output of [`lms link status`](https://lmstudio.ai/docs/cli/link/link-status).

See [Using LM Link with the REST API](https://lmstudio.ai/docs/developer/core/lmlink) for more on how preferred devices affect model routing.

### Learn more[](#learn-more)

See the [LM Link documentation](https://lmstudio.ai/docs/lmlink) for a full overview of LM Link.