---
title: Core Features
url: https://epi052.github.io/feroxbuster-docs/examples/core-features
source: github_pages
fetched_at: 2026-02-06T10:55:10.630919014-03:00
rendered_js: true
word_count: 154
summary: This document provides practical examples and explanations for using various command-line options in feroxbuster, including multi-value arguments, proxy settings, and stdin integration.
tags:
    - feroxbuster
    - cli-usage
    - web-discovery
    - proxy-configuration
    - enumeration-tools
    - command-line-interface
category: guide
---

Options that take multiple values are very flexible. Consider the following ways of specifying extensions:

```

./feroxbuster -u http://127.1 -x pdf -x js,html -x php txt json,docx
```

The command above adds .pdf, .js, .html, .php, .txt, .json, and .docx to each url

All of the methods above (multiple flags, space separated, comma separated, etc…) are valid and interchangeable. The same goes for urls, headers, status codes, queries, and size filters.

```

./feroxbuster -u http://127.1 -H Accept:application/json "Authorization: Bearer {token}"
```

**Note**: to include a header containing a comma, use [ferox-config.toml](https://epi052.github.io/feroxbuster-docs/configuration/ferox-config-toml// "related [discussion](https://github.com/epi052/feroxbuster/issues/653")

### IPv6, non-recursive scan with INFO-level logging enabled

[Section titled “IPv6, non-recursive scan with INFO-level logging enabled”](#ipv6-non-recursive-scan-with-info-level-logging-enabled)

```

./feroxbuster -u http://[::1] --no-recursion -vv
```

### Read urls from STDIN; pipe only resulting urls out to another tool

[Section titled “Read urls from STDIN; pipe only resulting urls out to another tool”](#read-urls-from-stdin-pipe-only-resulting-urls-out-to-another-tool)

```

cat targets | ./feroxbuster --stdin --silent -s 200 301 302 --redirects -x js | fff -s 200 -o js-files
```

### Proxy traffic through Burp

[Section titled “Proxy traffic through Burp”](#proxy-traffic-through-burp)

```

./feroxbuster -u http://127.1 --insecure --proxy http://127.0.0.1:8080
```

### Proxy traffic through a SOCKS proxy (including DNS lookups)

[Section titled “Proxy traffic through a SOCKS proxy (including DNS lookups)”](#proxy-traffic-through-a-socks-proxy-including-dns-lookups)

```

./feroxbuster -u http://127.1 --proxy socks5h://127.0.0.1:9050
```

### Pass auth token via query parameter

[Section titled “Pass auth token via query parameter”](#pass-auth-token-via-query-parameter)

```

./feroxbuster -u http://127.1 --query token=0123456789ABCDEF
```