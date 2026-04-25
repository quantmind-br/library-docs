---
title: '`lms daemon update`'
url: https://lmstudio.ai/docs/cli/daemon/daemon-update
source: sitemap
fetched_at: 2026-04-07T21:28:13.701478108-03:00
rendered_js: false
word_count: 73
summary: This document explains the procedure for updating the lms daemon to fetch and install either the latest stable or beta release of llmster.
tags:
    - lms-daemon
    - update-procedure
    - llmster
    - beta-release
    - command-line
category: guide
---

The `lms daemon update` command fetches and installs the latest version of llmster.

### Flags[](#flags)

--beta (optional) : flag

Update to the latest beta release

## Update the daemon[](#update-the-daemon "Link to 'Update the daemon'")

Stop the daemon first:

```

lms daemon down
```

Then run the update:

```

lms daemon update
```

Fetches the latest stable release and installs it.

### Update to the beta channel[](#update-to-the-beta-channel)

```

lms daemon update --beta
```

### After updating[](#after-updating)

Start the daemon again to use the new version:

```

lms daemon up
```

To find out more about llmster, see [Headless Mode](https://lmstudio.ai/docs/developer/core/headless).