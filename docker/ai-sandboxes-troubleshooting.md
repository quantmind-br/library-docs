---
title: Troubleshooting
url: https://docs.docker.com/ai/sandboxes/troubleshooting/
source: llms
fetched_at: 2026-01-24T14:14:27.568912936-03:00
rendered_js: false
word_count: 336
summary: This document provides solutions for common errors and configuration issues encountered when running Claude Code within a Docker-based local sandbox environment.
tags:
    - docker
    - claude-code
    - sandboxing
    - troubleshooting
    - authentication
    - docker-desktop
category: guide
---

Table of contents

* * *

Availability: Experimental

Requires: Docker Desktop [4.50](https://docs.docker.com/desktop/release-notes/#4500) or later

This guide helps you resolve common issues when sandboxing Claude Code locally.

## ['sandbox' is not a docker command](#sandbox-is-not-a-docker-command)

When you run `docker sandbox`, you see an error saying the command doesn't exist.

This means the CLI plugin isn't installed or isn't in the correct location. To fix:

1. Verify the plugin exists:
   
   ```
   $ ls -la ~/.docker/cli-plugins/docker-sandbox
   ```
   
   The file should exist and be executable.
2. If using Docker Desktop, restart it to detect the plugin.

## ["Experimental Features" needs to be enabled by your administrator](#experimental-features-needs-to-be-enabled-by-your-administrator)

You see an error about beta features being disabled when trying to use sandboxes.

This happens when your Docker Desktop installation is managed by an administrator who has locked settings. If your organization uses [Settings Management](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/), ask your administrator to [allow beta features](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/#beta-features):

```
{
  "configurationFileVersion": 2,
  "allowBetaFeatures": {
    "locked": false,
    "value": true
  }
}
```

## [Authentication failure](#authentication-failure)

Claude can't authenticate, or you see API key errors.

The API key is likely invalid, expired, or not configured correctly. How to fix depends on your credential mode:

If using `--credentials=sandbox` (the default):

1. Remove the stored credentials:
   
   ```
   $ docker volume rm docker-claude-sandbox-data
   ```
2. Start a new sandbox and complete the authentication workflow:
   
   ```
   $ docker sandbox run claude
   ```

## [Workspace contains API key configuration](#workspace-contains-api-key-configuration)

You see a warning about conflicting credentials when starting a sandbox.

This happens when your workspace has a `.claude.json` file with a `primaryApiKey` field. Choose one of these approaches:

- Remove the `primaryApiKey` field from your `.claude.json`:
  
  ```
  {
    "apiKeyHelper": "/path/to/script",
    "env": {
      "ANTHROPIC_BASE_URL": "https://api.anthropic.com"
    }
  }
  ```
- Or proceed with the warning - workspace credentials will be ignored in favor of sandbox credentials.

## [Permission denied when accessing workspace files](#permission-denied-when-accessing-workspace-files)

Claude or commands fail with "Permission denied" errors when accessing files in the workspace.

This usually means the workspace path isn't accessible to Docker, or file permissions are too restrictive.

If using Docker Desktop:

1. Check File Sharing settings at Docker Desktop → **Settings** → **Resources** → **File Sharing**.
2. Ensure your workspace path (or a parent directory) is listed under Virtual file shares.
3. If missing, click "+" to add the directory containing your workspace.
4. Restart Docker Desktop.

For all platforms, verify file permissions:

Ensure files are readable. If needed:

```
$ chmod -R u+r <workspace>
```

Also verify the workspace path exists: