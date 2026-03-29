---
title: Scan Directory Listings
url: https://epi052.github.io/feroxbuster-docs/examples/scan-dir-listings
source: github_pages
fetched_at: 2026-02-06T10:56:09.155973001-03:00
rendered_js: true
word_count: 127
summary: This document explains how to use the --scan-dir-listings and --thorough flags in feroxbuster to ensure exhaustive scanning of directories even when directory listings are present.
tags:
    - feroxbuster
    - directory-scanning
    - web-security
    - reconnaissance
    - cli-options
category: guide
---

## Force scans to recurse into directory listings

[Section titled “Force scans to recurse into directory listings”](#force-scans-to-recurse-into-directory-listings)

Version 2.11.0 allows users to force feroxbuster to scan directory listings. Prior to 2.11.0, when feroxbuster encountered a directory listing, it would simply parse the `<a>` tags, report the results, queue any additional folders found in the `<a>` tags, and then move onto its next objective.

Not scanning directory listings makes sense, generally, but web servers can be configured to both allow directory listing while also hiding files/folders from that listing. That’s where `--scan-dir-listings` comes in. When `--scan-dir-listings` is used, feroxbuster will perform it’s typical `<a>` tag parsing et. al., but will also perform a scan of that directory.

```

feroxbuster -u https://some-example-site.com --scan-dir-listings
```

## Example (`--thorough`)

[Section titled “Example (--thorough)”](#example---thorough)

The `--thorough` meta-option also sets `--scan-dir-listings`

```

feroxbuster -u https://some-example-site.com --thorough
```