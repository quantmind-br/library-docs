---
title: Response Size Limit
url: https://epi052.github.io/feroxbuster-docs/examples/response-size-limit
source: github_pages
fetched_at: 2026-02-06T10:56:02.923000818-03:00
rendered_js: true
word_count: 544
summary: This document explains how to use and configure the response size limit in feroxbuster to prevent out-of-memory errors when scanning targets with large response bodies.
tags:
    - feroxbuster
    - memory-management
    - response-size-limit
    - web-scanning
    - cli-configuration
    - performance-optimization
category: guide
---

## Limit Response Body Size

[Section titled “Limit Response Body Size”](#limit-response-body-size)

Version 2.12.0 introduces the `--response-size-limit` flag to prevent out-of-memory errors when scanning targets that return very large response bodies. This feature is particularly useful when encountering servers that serve large files such as backups, database dumps, or media files that could exhaust system memory.

By default, feroxbuster sets a 4MB (4,194,304 bytes) limit on response body reading, which provides protection against unexpected memory issues while still allowing most legitimate web content to be processed fully.

The response size limiting mechanism:

- Reads only the first N bytes of each HTTP response body
- Prevents memory exhaustion from unexpectedly large responses
- Allows normal processing for responses under the size limit
- Works seamlessly with all other feroxbuster features (filtering, extraction, etc.)
- Does not affect HTTP status codes, headers, or other response metadata

The `--response-size-limit` flag is especially beneficial when:

- **Large File Exposure**: Servers accidentally expose backup files, database dumps, or archives
- **Memory-Constrained Environments**: Running feroxbuster on systems with limited RAM
- **Automated Scanning**: Preventing scans from failing due to unexpected large responses
- **CI/CD Pipelines**: Ensuring consistent memory usage in automated security testing
- **Shared Infrastructure**: Preventing resource exhaustion on shared systems

Set a custom response size limit:

```

feroxbuster -u https://example.com/ --response-size-limit 1048576
```

*Limits response reading to 1MB (1,048,576 bytes)*

### Conservative Memory Usage

[Section titled “Conservative Memory Usage”](#conservative-memory-usage)

Use a smaller limit for memory-constrained environments:

```

feroxbuster -u https://example.com/ --response-size-limit 512000
```

*Limits response reading to 500KB*

### Large Content Scanning

[Section titled “Large Content Scanning”](#large-content-scanning)

Increase the limit when expecting larger legitimate responses:

```

feroxbuster -u https://example.com/ --response-size-limit 10485760
```

*Limits response reading to 10MB*

### Combined with Other Limits

[Section titled “Combined with Other Limits”](#combined-with-other-limits)

Use alongside other resource management options:

```

feroxbuster -u https://example.com/ --response-size-limit 2097152 --rate-limit 50 --threads 10
```

*Combines 2MB response limit with rate limiting and thread control*

## Configuration File

[Section titled “Configuration File”](#configuration-file)

The response size limit can also be configured via the configuration file:

```

response_size_limit = 2097152# 2MB in bytes
```

## Size Calculations

[Section titled “Size Calculations”](#size-calculations)

Common size values for reference:

SizeBytesUse Case512KB524,288Conservative, minimal memory usage1MB1,048,576Light scanning, embedded systems4MB4,194,304**Default** - Balanced protection and functionality8MB8,388,608Large page content, rich applications16MB16,777,216Very large responses, media content

When the response size limit differs from the default (4MB), it will be displayed in the scan banner:

```

───────────────────────────────────────────────────────────────────────────
🎯  Target Url            │ https://example.com/
🚀  Threads               │ 50
📖  Wordlist              │ /wordlists/common.txt
📏  Response Size Limit   │ 2097152 bytes
───────────────────────────────────────────────────────────────────────────
```

## Behavior with Large Responses

[Section titled “Behavior with Large Responses”](#behavior-with-large-responses)

When a response exceeds the size limit:

- ✅ Status code, headers, and metadata are fully processed
- ✅ First N bytes of content are available for filtering and extraction
- ✅ Response is still reported and logged normally
- ⚠️ Content beyond the limit is truncated and not processed
- ⚠️ Word/line counts may be lower than actual values for truncated responses

Response that exceeds the size limit:

```

200      GET       45l      123w     4194304c https://example.com/backup.sql  (truncated to size limit)
```

*Note: The content length (4MB) shows the bytes actually read and processed, not the full response size*

## Performance Considerations

[Section titled “Performance Considerations”](#performance-considerations)

- **Memory Protection**: Prevents unexpected OOM errors from large responses
- **Scan Reliability**: Ensures scans complete even when encountering large files
- **Processing Speed**: May slightly improve performance by avoiding large content processing

The response size limit:

- Works with all scan modes (recursive, single-target, etc.)
- Compatible with all filtering options
- Functions normally with extraction and link following
- Integrates with similarity and unique response filtering
- Maintains full compatibility with output formats

## Implementation Notes

[Section titled “Implementation Notes”](#implementation-notes)

- Uses chunked reading to implement the size limit efficiently
- Limit applies only to response body content, not headers or metadata
- Very large limits may still cause memory issues on constrained systems