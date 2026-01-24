---
title: Usage | Dank Linux
url: https://danklinux.com/docs/dgop/usage
source: sitemap
fetched_at: 2026-01-24T13:36:18.866582958-03:00
rendered_js: false
word_count: 230
summary: This document provides a comprehensive overview of the dgop tool's command-line interface and API for monitoring system metrics, hardware details, and process management.
tags:
    - dgop
    - system-monitoring
    - cli-reference
    - api-usage
    - process-management
    - metrics-collection
    - openapi
category: guide
---

```
██████╗  ██████╗  ██████╗ ██████╗
██╔══██╗██╔════╝ ██╔═══██╗██╔══██╗
██║  ██║██║  ███╗██║   ██║██████╔╝
██║  ██║██║   ██║██║   ██║██╔═══╝
██████╔╝╚██████╔╝╚██████╔╝██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝
                                
```

## API Usage[​](#api-usage "Direct link to API Usage")

The `dgop` API provides a documentation endpoint, with a full openapi 3.1 specification available at `http://localhost:63484/docs`

![DGOP API Documentation](https://danklinux.com/img/dgopdoclight.png)![DGOP API Documentation](https://danklinux.com/img/dgopdoc.png)

Interactive OpenAPI documentation interface

It is guaranteed to be up to date so it's the best way to reference API usage.

## CLI Usage[​](#cli-usage "Direct link to CLI Usage")

DGOP provides a comprehensive command-line interface for querying system metrics. All commands support JSON output via the `--json` flag for easy integration with scripts and applications.

### Basic Commands[​](#basic-commands "Direct link to Basic Commands")

Get quick system information using individual commands:

```
# View CPU usage and information
dgop cpu

# Check memory usage
dgop memory

# Monitor network interfaces
dgop network

# View disk information
dgop disk

# List running processes
dgop processes

# Get general system information
dgop system
```

### Advanced Commands[​](#advanced-commands "Direct link to Advanced Commands")

For more specialized monitoring:

```
# Monitor disk I/O rates in real-time
dgop disk-rate

# Track network transfer rates
dgop net-rate

# View GPU information
dgop gpu

# Get GPU temperature readings
dgop gpu-temp

# Display hardware details (motherboard, BIOS)
dgop hardware

# Get all metrics at once
dgop all
```

### Process Management[​](#process-management "Direct link to Process Management")

The `processes` command provides detailed process information with sorting and filtering options:

```
# List top processes by CPU usage
dgop processes --sort cpu --limit20

# List processes by memory usage
dgop processes --sort memory --limit10

# Disable CPU calculation for faster listing
dgop processes --no-cpu
```

### Meta Command[​](#meta-command "Direct link to Meta Command")

The `meta` command is designed for efficient polling by requesting multiple modules in a single call:

```
# Query multiple metrics at once
dgop meta --modules cpu,memory,network

# Get all metrics with specific GPU monitoring
dgop meta --modules all --gpu-pci-ids 0000:01:00.0

# Efficient CPU monitoring with cursor-based sampling
dgop meta --modules cpu --cpu-cursor <previous-cursor>

# Process monitoring with cursor for accurate percentages
dgop meta --modules processes --proc-cursor <previous-cursor>--limit100
```

#### Cursor-Based Sampling[​](#cursor-based-sampling "Direct link to Cursor-Based Sampling")

For accurate CPU and process metrics over time, DGOP supports cursor-based sampling. The meta command returns cursor values that should be passed back on subsequent calls:

```
# First call - no cursor needed
dgop meta --modules cpu,processes --json

# Subsequent calls - use returned cursors for accurate deltas
dgop meta --modules cpu,processes --cpu-cursor abc123 --proc-cursor def456 --json
```

This ensures CPU percentages reflect actual usage between samples rather than system-wide averages.

### Interactive Monitor[​](#interactive-monitor "Direct link to Interactive Monitor")

Launch a real-time, interactive system monitor, similar to top, htop:

### API Server[​](#api-server "Direct link to API Server")

Start the HTTP API server for programmatic access:

```
# Start server on default port (63484)
dgop server

# Access OpenAPI documentation at http://localhost:63484/docs
```

### Output Formats[​](#output-formats "Direct link to Output Formats")

All commands support JSON output for integration with other tools:

```
# Get CPU info in JSON format
dgop cpu --json

# Pipe to jq for parsing
dgop memory --json| jq '.usage'
```

### Common Flags[​](#common-flags "Direct link to Common Flags")

- `--json` - Output results in JSON format
- `--no-cpu` - Disable CPU calculation in process listing for better performance
- `--help` - Show help for any command

### List Available Modules[​](#list-available-modules "Direct link to List Available Modules")

See which metric modules are available: