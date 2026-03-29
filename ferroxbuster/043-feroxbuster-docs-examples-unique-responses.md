---
title: Unique Responses
url: https://epi052.github.io/feroxbuster-docs/examples/unique-responses
source: github_pages
fetched_at: 2026-02-06T10:56:18.529103999-03:00
rendered_js: true
word_count: 284
summary: This document explains how to use the --unique flag in feroxbuster to automatically filter out duplicate and near-duplicate HTTP responses using simhash fingerprinting.
tags:
    - feroxbuster
    - web-scanning
    - response-filtering
    - simhash
    - noise-reduction
    - cli-tools
category: guide
---

## Show Only Unique Responses

[Section titled “Show Only Unique Responses”](#show-only-unique-responses)

Version 2.12.0 introduces the `--unique` flag to automatically filter out duplicate and (very) near-duplicate responses during scanning. This feature is particularly useful when dealing with WAFs, load balancers, or applications with wildcard routing that generate many identical responses, reducing output noise and making results easier to analyze.

When `--unique` is enabled, feroxbuster uses an intelligent similarity detection algorithm (simhash) to identify and filter out responses that are substantially similar to previously seen responses.

The unique filtering mechanism:

- Analyzes response content using simhash fingerprinting
- Compares new responses against previously seen responses
- Filters out responses that are highly similar (stricter than `--filter-similar-to`)
- Automatically adds similarity filters on-the-fly as new unique responses are discovered

The `--unique` flag is especially beneficial when:

- **WAF Interference**: When Web Application Firewalls return identical responses for multiple blocked requests
- **Wildcard Routing**: Applications that serve the same content for non-existent paths (e.g., SPA routing)
- **Load Balancer Behavior**: When load balancers return consistent error pages
- **Parameter Fuzzing**: When multiple parameter values trigger identical responses
- **Large Wordlists**: Reducing noise when using comprehensive dictionaries

Enable unique response filtering for a standard scan:

```

feroxbuster -u https://example.com/ --unique
```

### Combined with Status Code Filtering

[Section titled “Combined with Status Code Filtering”](#combined-with-status-code-filtering)

Use unique filtering alongside traditional filters:

```

feroxbuster -u https://example.com/ --unique --filter-status 404,403
```

## Configuration File

[Section titled “Configuration File”](#configuration-file)

The unique filtering can also be enabled via configuration file:

## Example Output Comparison

[Section titled “Example Output Comparison”](#example-output-comparison)

### Without `--unique`:

[Section titled “Without --unique:”](#without---unique)

```

404      GET        5l       12w      150c https://example.com/admin
404      GET        5l       12w      150c https://example.com/admins
404      GET        5l       12w      150c https://example.com/administrator
404      GET        5l       12w      150c https://example.com/adminpanel
200      GET       25l       89w     1247c https://example.com/login
404      GET        5l       12w      150c https://example.com/manage
404      GET        5l       12w      150c https://example.com/management
```

```

404      GET        5l       12w      150c https://example.com/admin
200      GET       25l       89w     1247c https://example.com/login
```

## Implementation Notes

[Section titled “Implementation Notes”](#implementation-notes)

- Uses the same simhash algorithm as similarity filtering but with a much stricter cutoff
- Filters are applied dynamically as new responses are encountered
- Works in conjunction with existing filtering mechanisms
- First occurrence of each unique response pattern is always shown