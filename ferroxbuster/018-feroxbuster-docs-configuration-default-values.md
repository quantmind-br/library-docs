---
title: Default Values
url: https://epi052.github.io/feroxbuster-docs/configuration/default-values
source: github_pages
fetched_at: 2026-02-06T10:54:47.207174949-03:00
rendered_js: true
word_count: 79
summary: This document lists the default configuration settings and built-in values for the feroxbuster web discovery tool.
tags:
    - feroxbuster
    - configuration-defaults
    - web-security
    - directory-fuzzing
    - scanning-parameters
category: configuration
---

Configuration begins with the following built-in default values baked into the binary:

- **timeout**: `7` seconds
- **follow redirects**: `false`
- **wordlist**: `/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt`
- **threads**: `50`
- **verbosity**: `0` (no logging enabled)
- **scan\_limit**: `0` (no limit imposed on concurrent scans)
- **rate\_limit**: `0` (no limit imposed on requests per second)
- **status\_codes**: All valid status codes
- **user\_agent**: `feroxbuster/VERSION`
- **recursion depth**: `4`
- **auto-filter wildcards**: `true`
- **output**: `stdout`
- **save\_state**: `true` (create a state file in cwd when `Ctrl+C` is received)
- **backup\_extensions**: `["~", ".bak", ".bak2", ".old", ".1"]`
- **protocol**: `https`