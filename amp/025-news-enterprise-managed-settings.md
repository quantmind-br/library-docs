---
title: Enterprise Managed Settings
url: https://ampcode.com/news/enterprise-managed-settings
source: crawler
fetched_at: 2026-02-06T02:08:32.883665106-03:00
rendered_js: false
word_count: 118
summary: This document explains how system administrators can implement organization-wide managed settings in Amp to enforce security and standardization across Enterprise accounts. It details the configurable parameters and provides the specific file paths required for different operating systems.
tags:
    - amp-enterprise
    - managed-settings
    - system-administration
    - organization-wide-configuration
    - security-policy
category: configuration
---

Amp now allows system administrators to configure organization-wide settings that override individual settings for Enterprise Amp customers. These settings can help ensure security, standardization, and best practices across an organization. Managed settings can be used, for example, to do the following:

- Set MCP servers to those that work well in your organization (`amp.mcpServers`)
- Allow or block MCP servers (`amp.mcpPermissions`)
- Allow or block Bash commands that match specified patterns (`amp.permissions`)
- Override any other Amp setting

To use managed settings, system administrators should ensure the settings are defined in the following files:

- **macOS**: `/Library/Application Support/ampcode/managed-settings.json`
- **Linux**: `/etc/ampcode/managed-settings.json`
- **Windows**: `C:\ProgramData\ampcode\managed-settings.json`

Settings in these files use the same schema as individual settings.

You can read more about managed settings [in the manual.](https://ampcode.com/manual?internal#enterprise-managed-policy-settings)