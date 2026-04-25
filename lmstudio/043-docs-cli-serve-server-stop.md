---
title: '`lms server stop`'
url: https://lmstudio.ai/docs/cli/serve/server-stop
source: sitemap
fetched_at: 2026-04-07T21:28:21.716753498-03:00
rendered_js: false
word_count: 34
summary: This document explains how to gracefully stop a running LM Studio server using the dedicated command.
tags:
    - server-control
    - stop-command
    - lms-studio
    - api-management
category: guide
---

The `lms server stop` command gracefully stops the running LM Studio server.

```

lms server stop
```

Example output:

```

Stopped the server on port 1234.
```

Any active request will be terminated when the server is stopped. You can restart the server using [`lms server start`](https://lmstudio.ai/docs/cli/serve/server-start).