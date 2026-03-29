---
title: 'ForgeCode v0.98.0: Integrated Authentication and Developer Experience Improvements'
url: https://forgecode.dev/blog/forge-v0.98.0-release-article/
source: sitemap
fetched_at: 2026-03-29T14:48:10.22538677-03:00
rendered_js: false
word_count: 587
summary: This document explains the new features and changes in ForgeCode v0.98.0, including browser-based authentication, safety limits for tool failures, and enhanced file operations like replace-all functionality.
tags:
    - browser-authentication
    - safety-limits
    - file-operations
    - tool-failures
    - replace-all
    - api-keys
    - automation
    - error-handling
category: reference
---

*July 6, 2025* - ForgeCode v0.98.0 introduces browser-based authentication, tool failure limits, and enhanced file operations to improve reliability and user experience.

### Browser-Based Authentication[​](#browser-based-authentication "Direct link to Browser-Based Authentication")

v0.98.0 replaces manual API key configuration with browser-based authentication that integrates with `app.forgecode.dev`.

#### Setup Process[​](#setup-process "Direct link to Setup Process")

1. Install ForgeCode: `curl -fsSL https://forgecode.dev/cli | sh`
2. Run `forge`
3. ForgeCode opens your browser to `app.forgecode.dev`
4. Sign in with Google or GitHub
5. Authorize the app
6. Return to terminal - authentication is complete

![ForgeCode browser authentication setup - AI coding assistant terminal login process showing seamless Google and GitHub integration](https://forgecode.dev/images/blog/login-newuser.gif)

*Complete authentication setup in under 30 seconds*

The system waits for the authentication server until login completes.

![Terminal Authentication Progress](https://forgecode.dev/images/blog/login-progress.png)

*Terminal shows authentication progress with clear status updates*

#### Migration from API Keys[​](#migration-from-api-keys "Direct link to Migration from API Keys")

**Existing users**: Your current API key configuration will continue working. The browser-based auth is optional and can be used alongside existing setups.

**For automation/CI**: API key authentication remains available for scripts and automated environments where browser access isn't available.

### Safety Limits and Auto-Stop[​](#safety-limits-and-auto-stop "Direct link to Safety Limits and Auto-Stop")

ForgeCode now includes automatic safety limits to prevent infinite loops and runaway processes. There are two separate systems that work together to keep things under control.

#### System 1: Consecutive Tool Failure Limit (Hard Stop)[​](#system-1-consecutive-tool-failure-limit-hard-stop "Direct link to System 1: Consecutive Tool Failure Limit (Hard Stop)")

**What it does:** Tracks tool failures in a row and terminates the conversation when too many happen consecutively.

**Default limit:** 5 consecutive failures **What triggers it:** File permission errors, invalid parameters, network issues - anything that makes tools fail repeatedly **What happens:** ForgeCode asks: "Do you want to continue anyway?"

**Key point:** This counter resets when any tool succeeds. It only cares about failures happening back-to-back.

![Tool Failure Limit Dialog](https://forgecode.dev/images/blog/tool-call-limit.gif)

*Hard stop when consecutive failures hit the limit*

#### System 2: Overall Turn Limits (User Intervention)[​](#system-2-overall-turn-limits-user-intervention "Direct link to System 2: Overall Turn Limits (User Intervention)")

**What it does:** Monitors the total activity in a single conversation turn and asks if you want to continue when limits are hit.

**Default limits:**

- 50 total requests per turn

**What happens:** ForgeCode asks: "Do you want to continue anyway?"

**Configuration in forge.yaml:**

**Problem solved:** Prevents scenarios where agents get stuck in retry cycles due to environmental issues, permission problems, or invalid parameters that require human intervention rather than continued automated attempts.

> *Safety mechanism activates when operational limits are reached*

### Enhanced File Operations[​](#enhanced-file-operations "Direct link to Enhanced File Operations")

#### Replace-All Patch Operation[​](#replace-all-patch-operation "Direct link to Replace-All Patch Operation")

The file patching system now supports `replace_all` operations for comprehensive refactoring tasks.

**Previous behavior**: `replace` operation only modified the first occurrence **New behavior**: `replace_all` operation modifies all occurrences in the target file

![Replace All Operation Demo](https://forgecode.dev/images/blog/replace-all.gif)

Replace-all operation updating multiple function names across a file

This is particularly useful for:

- Variable and function renaming
- Import statement updates
- Consistent refactoring across large files

**None**. v0.98.0 maintains backward compatibility with existing API key configurations.

### Authentication Issues[​](#authentication-issues "Direct link to Authentication Issues")

**Browser doesn't open**: Manually navigate to the URL displayed in the terminal **Login timeout**: Check network connectivity and retry **Permission errors**: Ensure ForgeCode has permission to write to config directory

### Safety Limits and Auto-Stop[​](#safety-limits-and-auto-stop-1 "Direct link to Safety Limits and Auto-Stop")

**Frequent limit hits**: Check file permissions. **Need higher limits**: Adjust configuration in `forge.yaml` **Unexpected failures**: Review error messages for specific tool issues

### New Users[​](#new-users "Direct link to New Users")

*Complete setup experience for first-time users*

### Existing Users[​](#existing-users "Direct link to Existing Users")

*Smooth transition options for users with existing API key setups*

### Automation/CI[​](#automationci "Direct link to Automation/CI")

Continue using API key authentication for automated environments:

- [Documentation](https://forgecode.dev/docs/) - Setup guides and API reference
- [GitHub Repository](https://github.com/antinomyhq/forge) - Source code and issues
- [Discord Community](https://discord.gg/kRZBPpkgwq) - Support and discussions
- [Release Notes](https://github.com/antinomyhq/forge/releases/tag/v0.98.0) - Complete changelog

* * *

v0.98.0 focuses on reliability and ease of use while maintaining the flexibility developers need for various workflows. The browser-based authentication removes setup friction for new users while preserving API key support for automation and power users.