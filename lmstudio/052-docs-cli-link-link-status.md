---
title: '`lms link status`'
url: https://lmstudio.ai/docs/cli/link/link-status
source: sitemap
fetched_at: 2026-04-07T21:28:07.837061446-03:00
rendered_js: false
word_count: 101
summary: This document explains the functionality of the `lms link status` command, which reports the operational status of LM Link on a device, including connected peers and their loaded models.
tags:
    - lm-link
    - status-check
    - cli-command
    - device-connection
    - model-listing
category: reference
---

The `lms link status` command shows whether LM Link is enabled on this device, and lists connected peers and their loaded models.

### Flags[](#flags)

--json (optional) : flag

Output the status in JSON format

## Check status[](#check-status "Link to 'Check status'")


Displays this device's name, connection state, and a list of connected peers with their currently loaded models.

### JSON output[](#json-output)

For scripting or automation:


### Enable or disable LM Link[](#enable-or-disable-lm-link)

- [`lms link enable`](https://lmstudio.ai/docs/cli/link/link-enable) — enable LM Link on this device.
- [`lms link disable`](https://lmstudio.ai/docs/cli/link/link-disable) — disable LM Link on this device.

### Learn more[](#learn-more)

See the [LM Link documentation](https://lmstudio.ai/docs/lmlink) for a full overview of LM Link.