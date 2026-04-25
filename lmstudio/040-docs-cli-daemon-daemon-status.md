---
title: '`lms daemon status`'
url: https://lmstudio.ai/docs/cli/daemon/daemon-status
source: sitemap
fetched_at: 2026-04-07T21:28:15.768525818-03:00
rendered_js: false
word_count: 73
summary: This document explains how to check the operational status of the lms daemon using the `lms daemon status` command, and details related commands for starting or stopping the service.
tags:
    - daemon-status
    - cli-command
    - llmster
    - system-management
    - json-output
category: reference
---

The `lms daemon status` command reports whether llmster is currently running.

### Flags[](#flags)

--json (optional) : flag

Output the status in JSON format

## Check daemon status[](#check-daemon-status "Link to 'Check daemon status'")

```

lms daemon status
```

### JSON output[](#json-output)

For scripting or automation:

```

lms daemon status --json
```

Example output when running:

```

{"status":"running","pid":12345,"isDaemon":true}
```

Example output when not running:

```

{"status":"not-running"}
```

### Start or stop the daemon[](#start-or-stop-the-daemon)

- [`lms daemon up`](https://lmstudio.ai/docs/cli/daemon/daemon-up) — start the daemon.
- [`lms daemon down`](https://lmstudio.ai/docs/cli/daemon/daemon-down) — stop the daemon.

To find out more about llmster, see [Headless Mode](https://lmstudio.ai/docs/developer/core/headless).