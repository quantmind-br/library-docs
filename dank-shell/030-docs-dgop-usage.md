---
title: Usage | Dank Linux
url: https://danklinux.com/docs/dgop/usage
source: sitemap
fetched_at: 2026-04-26T08:39:39.951840479-03:00
rendered_js: false
word_count: 230
summary: This document provides an overview of the dgop system monitoring tool, detailing its command-line interface, API server capabilities, and cursor-based sampling methods for accurate metric collection.
tags:
    - system-monitoring
    - cli-tools
    - api-documentation
    - performance-metrics
    - process-management
    - json-output
category: guide
optimized: true
optimized_at: 2026-04-26T12:00:00Z
---

```
██████╗  ██████╗  ██████╗ ██████╗
██╔══██╗██╔════╝ ██╔═══██╗██╔══██╗
██║  ██║██║  ███╗██║   ██║██████╔╝
██║  ██║██║   ██║██║   ██║██╔═══╝
██████╔╝╚██████╔╝╚██████╔╝██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝

```

## API Usage

The `dgop` API provides a documentation endpoint with a full OpenAPI 3.1 specification available at `http://localhost:63484/docs`.

![DGOP API Documentation](https://danklinux.com/img/dgopdoclight.png) ![DGOP API Documentation](https://danklinux.com/img/dgopdoc.png)

Interactive OpenAPI documentation interface.

It's guaranteed to be up to date so it's the best way to reference API usage.

## CLI Usage

DGOP provides a comprehensive command-line interface for querying system metrics. All commands support JSON output via the `--json` flag for easy integration with scripts and applications.

### Basic Commands

```bash
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

### Advanced Commands

```bash
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

### Process Management

The `processes` command provides detailed process information with sorting and filtering options:

```bash
# List top processes by CPU usage
dgop processes --sort cpu --limit 20
# List processes by memory usage
dgop processes --sort memory --limit 10
# Disable CPU calculation for faster listing
dgop processes --no-cpu
```

### Meta Command

The `meta` command is designed for efficient polling by requesting multiple modules in a single call:

```bash
# Query multiple metrics at once
dgop meta --modules cpu,memory,network
# Get all metrics with specific GPU monitoring
dgop meta --modules all --gpu-pci-ids 0000:01:00.0
# Efficient CPU monitoring with cursor-based sampling
dgop meta --modules cpu --cpu-cursor <previous-cursor>
# Process monitoring with cursor for accurate percentages
dgop meta --modules processes --proc-cursor <previous-cursor> --limit 100
```

#### Cursor-Based Sampling

For accurate CPU and process metrics over time, DGOP supports cursor-based sampling. The meta command returns cursor values that should be passed back on subsequent calls:

```bash
# First call - no cursor needed
dgop meta --modules cpu,processes --json
# Subsequent calls - use returned cursors for accurate deltas
dgop meta --modules cpu,processes --cpu-cursor abc123 --proc-cursor def456 --json
```

This ensures CPU percentages reflect actual usage between samples rather than system-wide averages.

### Interactive Monitor

Launch a real-time, interactive system monitor, similar to top, htop:

### API Server

Start the HTTP API server for programmatic access:

```bash
# Start server on default port (63484)
dgop server
# Access OpenAPI documentation at http://localhost:63484/docs
```

### Output Formats

All commands support JSON output for integration with other tools:

```bash
# Get CPU info in JSON format
dgop cpu --json
# Pipe to jq for parsing
dgop memory --json | jq '.usage'
```

### Common Flags

- `--json` - Output results in JSON format
- `--no-cpu` - Disable CPU calculation in process listing for better performance
- `--help` - Show help for any command

### List Available Modules

See which metric modules are available: