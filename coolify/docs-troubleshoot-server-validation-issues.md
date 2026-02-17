---
title: Server Validation Issues
url: https://coolify.io/docs/troubleshoot/server/validation-issues.md
source: llms
fetched_at: 2026-02-17T14:41:57.343404-03:00
rendered_js: false
word_count: 52
summary: This document explains how to resolve a 'libcrypto' server validation error in Coolify by ensuring the SSH private key is correctly formatted with the required header and footer.
tags:
    - coolify
    - server-validation
    - ssh-keys
    - libcrypto-error
    - troubleshooting
    - private-key
category: guide
---

# Server Validation Issues

You cannot validate your server because of a validation error.

## Symptoms

* During validation you receive a `error in libcrypto` error.

## Solution

Check your private key added to Coolify if it is correct, it is probably missing a few things, like `-----BEGIN OPENSSH PRIVATE KEY-----` and `-----END OPENSSH PRIVATE KEY-----`.