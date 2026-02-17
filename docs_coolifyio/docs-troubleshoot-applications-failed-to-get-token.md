---
title: Failed To Get Access Token
url: https://coolify.io/docs/troubleshoot/applications/failed-to-get-token.md
source: llms
fetched_at: 2026-02-17T14:41:44.343563-03:00
rendered_js: false
word_count: 54
summary: Explains how to resolve a deployment failure caused by GitHub access token errors specifically related to NTP time synchronization issues.
tags:
    - github-integration
    - ntp-sync
    - access-token
    - troubleshooting
    - deployment-error
category: guide
---

# Failed To Get Access Token

Your deployment failed because it cannot get the access token from GitHub.

The error is usually related to NTP time synchronization issue.

## Error

`'Issued at' claim (iat) must be an Integer representing the time that assertion issued.`

## Solution

You must do the same as the [2FA Stopped Working](/troubleshoot/server/two-factor-stopped-working) solution.