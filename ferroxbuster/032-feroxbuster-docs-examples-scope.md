---
title: Scope
url: https://epi052.github.io/feroxbuster-docs/examples/scope
source: github_pages
fetched_at: 2026-02-06T10:56:13.378298278-03:00
rendered_js: true
word_count: 285
summary: This document explains how to use the --scope option in feroxbuster to define and manage authorized domains for scanning, link extraction, and redirection. It covers automatic scope population, wildcard subdomain matching, and configuration via command-line arguments or files.
tags:
    - feroxbuster
    - web-fuzzing
    - scope-management
    - security-testing
    - command-line-options
    - subdomain-matching
category: guide
---

The `--scope` option allows you to specify additional domains that should be considered “in-scope” during feroxbuster scans. This can help you avoid accidentally attacking endpoints or hosts that you don’t have permission to test.

```

feroxbuster-uhttps://example.com--scopeother-example.comexample-sibling.com
```

By default, feroxbuster automatically includes the target URL’s domain in the scope list. When you specify additional URLs via `--scope`, they are added to this internal scope list along with the original target.

A URL is considered **in-scope** if:

1. It belongs to the same domain as any URL in the scope list, OR
2. It belongs to a subdomain of any domain in the scope list

So, any domain added to the scope is effectively wildcarded for subdomains, e.g. `example.com` =&gt; `example.com || *.example.com`

### Automatic Scope Population

[Section titled “Automatic Scope Population”](#automatic-scope-population)

The scope list is automatically populated with:

- The target URL from `--url` (or URLs from `--stdin`)
- Any domains/URLs you specify with `--scope`

## Scope Application

[Section titled “Scope Application”](#scope-application)

The scope checking applies to:

- **Redirect following** (when `--redirects` is enabled)
- **Link extraction** (assuming `--dont-extract-links` is false, which is the default)
- **Recursive directory scanning**

URLs that fall outside the defined scope are automatically filtered out to prevent accidental scanning of unauthorized targets.

## Configuration File

[Section titled “Configuration File”](#configuration-file)

You can also specify scope in your `ferox-config.toml`:

```

scope = ["example.com", "dev-example.com", "partner.otherdomain.com"]
```

### Single Additional Domain

[Section titled “Single Additional Domain”](#single-additional-domain)

```

feroxbuster-uhttps://example.com--scopedev-example.com
```

**In-scope URLs:**

- `example.com` and all its subdomains (from target URL)
- `dev-example.com` and all its subdomains (from —scope)

```

feroxbuster-uhttps://example.com--scopedev-example.compartner.otherdomain.com
```

**In-scope URLs:**

- `example.com` and all its subdomains
- `dev-example.com` and all its subdomains
- `partner.otherdomain.com` and all its subdomains

```

feroxbuster-uhttps://example.com--scopedev-example.com--redirects
```

Now if `example.com/login` redirects to `dev-example.com/auth/login`, feroxbuster will follow the redirect because `dev-example.com` is in scope.

- `--dont-scan`: Use this to exclude specific URLs/domains (deny list)
- `--redirects`: Enable redirect following (scope applies to redirect targets)