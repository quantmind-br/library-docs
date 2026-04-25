---
title: '`lms link enable`'
url: https://lmstudio.ai/docs/cli/link/link-enable
source: sitemap
fetched_at: 2026-04-07T21:28:11.399018232-03:00
rendered_js: false
word_count: 108
summary: This document explains how to manage the LM Link feature using its command-line interface (CLI), covering enabling, checking status, and disabling the connection.
tags:
    - lm-link
    - cli-command
    - device-connection
    - lms-login
    - status-checking
category: guide
---

The `lms link enable` command enables LM Link on this device, allowing it to connect with other devices on the same link.

LM Link requires an LM Studio account. Run `lms login` first if you haven't already.

## Enable LM Link[](#enable-lm-link "Link to 'Enable LM Link'")


After enabling, the CLI waits for a connection to be established. If there are issues, the relevant next step is printed.

### Check the connection status[](#check-the-connection-status)

See [`lms link status`](https://lmstudio.ai/docs/cli/link/link-status) to verify the connection and see connected peers.

### Disable LM Link[](#disable-lm-link)

See [`lms link disable`](https://lmstudio.ai/docs/cli/link/link-disable) to turn LM Link off.

### Learn more[](#learn-more)

See the [LM Link documentation](https://lmstudio.ai/docs/lmlink) for a full overview of LM Link.