---
title: '`lms daemon up`'
url: https://lmstudio.ai/docs/cli/daemon/daemon-up
source: sitemap
fetched_at: 2026-04-07T21:28:17.676311898-03:00
rendered_js: false
word_count: 84
summary: This documentation explains the `lms daemon up` command, which is used to start the llmster daemon, reporting its status or process ID depending on whether it is already running.
tags:
    - daemon-management
    - llmster
    - command-line
    - api-status
    - service-control
category: guide
---

The `lms daemon up` command starts llmster

### Flags[](#flags)

--json (optional) : flag

Output the result in JSON format

## Start the daemon[](#start-the-daemon "Link to 'Start the daemon'")


If the daemon is not already running, this starts it and prints the PID. If it is already running, it reports the current status.

### JSON output[](#json-output)

For scripting or automation:


Example output:

```

{"status":"running","pid":26754,"isDaemon":true,"version":"0.4.4+1"}
```

### Check the daemon status[](#check-the-daemon-status)

See [`lms daemon status`](https://lmstudio.ai/docs/cli/daemon/daemon-status) to check whether the daemon is running.

### Learn more[](#learn-more)

To find out more about llmster, see [Headless Mode](https://lmstudio.ai/docs/developer/core/headless).