---
title: '`lms server status`'
url: https://lmstudio.ai/docs/cli/serve/server-status
source: sitemap
fetched_at: 2026-04-07T21:28:24.090830064-03:00
rendered_js: false
word_count: 113
summary: This document explains the usage and available flags for the `lms server status` command, detailing how to check the local server's operational status in various formats.
tags:
    - server-status
    - command-line
    - logging
    - api-usage
category: reference
---

The `lms server status` command displays the current status of the LM Studio local server, including whether it's running and its configuration.

### Flags[](#flags)

--json (optional) : flag

Output the status in JSON format

--verbose (optional) : flag

Enable detailed logging output

--quiet (optional) : flag

Suppress all logging output

--log-level (optional) : string

The level of logging to use. Defaults to 'info'

## Check server status[](#check-server-status "Link to 'Check server status'")

Get the basic status of the server:


Example output:

```

The server is running on port 1234.
```

### Example usage[](#example-usage)

```

➜  ~ lms server start
Starting server...
Waking up LM Studio service...
Success! Server is now running on port 1234

➜  ~ lms server status
The server is running on port 1234.
```

### JSON output[](#json-output)

Get the status in machine-readable JSON format:

```

lms server status --json --quiet
```

Example output:

```

{"running":true,"port":1234}
```

### Control logging output[](#control-logging-output)

Adjust logging verbosity:

```

lms server status --verbose
lms server status --quiet
lms server status --log-level debug
```

You can only use one logging control flag at a time (`--verbose`, `--quiet`, or `--log-level`).