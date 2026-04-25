---
title: '`lms login`'
url: https://lmstudio.ai/docs/cli/develop-and-publish/login
source: sitemap
fetched_at: 2026-04-07T21:27:53.92625669-03:00
rendered_js: false
word_count: 90
summary: This document details the methods for authenticating a Command Line Interface (CLI) connection with the LM Studio Hub, providing options for both interactive browser sign-in and using pre-authenticated key pairs suitable for CI/CD environments.
tags:
    - lms-login
    - cli-authentication
    - key-management
    - ci-cd
    - command-line
category: guide
---

Use `lms login` to authenticate the CLI with LM Studio Hub.

### Sign in with the browser[](#sign-in-with-the-browser)


The CLI opens a browser window for authentication. If a browser cannot be opened automatically, copy the printed URL into your browser.

### "CI style" login with pre-authenticated keys[](#ci-style-login-with-pre-authenticated-keys)

```

lms login --with-pre-authenticated-keys \
  --key-id <KEY_ID> \
  --public-key <PUBLIC_KEY> \
  --private-key <PRIVATE_KEY>
```

### Advanced Flags[](#advanced-flags)

--with-pre-authenticated-keys (optional) : flag

Authenticate using pre-generated keys (CI/CD). Requires --key-id, --public-key, and --private-key.

--key-id (optional) : string

Key ID to use with --with-pre-authenticated-keys

--public-key (optional) : string

Public key to use with --with-pre-authenticated-keys

--private-key (optional) : string

Private key to use with --with-pre-authenticated-keys