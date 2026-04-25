---
title: '`lms daemon down`'
url: https://lmstudio.ai/docs/cli/daemon/daemon-down
source: sitemap
fetched_at: 2026-04-07T21:31:22.446828704-03:00
rendered_js: false
word_count: 44
summary: This document explains the purpose and usage of the `lms daemon down` command, specifying that it is used to stop a running llmster daemon but will not affect an actively running GUI instance.
tags:
    - daemon-control
    - llmster-management
    - stopping-service
    - command-line
category: reference
---

The `lms daemon down` command stops the running llmster.

```

lms daemon down
```

Info

`lms daemon down` only works if llmster is running. It will not stop LM Studio if it is running as a GUI app.

### Learn more[](#learn-more)

To find out more about llmster, see [Headless Mode](https://lmstudio.ai/docs/developer/core/headless).