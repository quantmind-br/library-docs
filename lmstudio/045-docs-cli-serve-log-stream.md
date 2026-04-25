---
title: '`lms log stream`'
url: https://lmstudio.ai/docs/cli/serve/log-stream
source: sitemap
fetched_at: 2026-04-07T21:28:19.442802561-03:00
rendered_js: false
word_count: 102
summary: This document explains how to use the `lms log stream` command to inspect the exact communication strings between LM Studio and language models, useful for debugging various operations.
tags:
    - logging
    - debugging
    - lm-studio
    - model-io
    - server-logs
category: guide
---

`lms log stream` lets you inspect the exact strings LM Studio sends to and receives from models, and (new in 0.3.26) stream server logs. This is useful for debugging prompt templates, model IO, and server operations.

### Flags[](#flags)

-s, --source (optional) : string

Source of logs: model or server (default: model)

--stats (optional) : flag

Print prediction stats when available

--filter (optional) : string

Filter for model source: input, output, or both

--json (optional) : flag

Output logs as JSON (newline separated)

### Quick start[](#quick-start)

Stream model IO (default):


Stream server logs:

```

lms log stream --source server
```

### Filter model logs[](#filter-model-logs)

```

# Only the formatted user input
lms log stream --source model --filter input

# Only the model output (emitted once the message completes)
lms log stream --source model --filter output

# Both directions
lms log stream --source model --filter input,output
```

### JSON output and stats[](#json-output-and-stats)

Emit JSON:

```

lms log stream --source model --filter input,output --json
```

Include prediction stats:

```

lms log stream --source model --filter output --stats
```