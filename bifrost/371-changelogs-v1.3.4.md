---
title: v1.3.4
url: https://docs.getbifrost.ai/changelogs/v1.3.4.md
source: llms
fetched_at: 2026-01-21T19:42:16.627402582-03:00
rendered_js: false
word_count: 259
summary: This document provides the changelog for Bifrost version 1.3.4, detailing updates to the HTTP interface, core engine, and framework modules. Key improvements include enhanced MCP tool management, virtual key support, and updated dependency versions.
tags:
    - changelog
    - release-notes
    - bifrost
    - mcp-tools
    - dependency-update
    - key-management
category: other
---

# v1.3.4

> v1.3.4 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.4
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.4
    docker run -p 8080:8080 maximhq/bifrost:v1.3.4
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.4">
  * Upgrade dependency: core to 1.2.10 and framework to 1.1.10
  * Feat: Added virtual key level support for MCP tools to execute
  * Feat: Added names to keys
  * Fix: provider selection from url params
</Update>

<Update label="Core" description="v1.3.4">
  * Feat: Added key name field to account schema for external key management
  * Feat: Simplified MCP client management by removing toolsToSkip field, allowing wildcard (\*) for all tools, and better tool filtering logic.
</Update>

<Update label="Framework" description="v1.3.4">
  * Upgrade dependency: core to 1.2.10
  * Feat: Added key name column to config keys table
  * Feat: Removed tools\_to\_skip field from MCP client config table
  * Feat: Added virtual\_key\_mcp\_config table to store MCP client configs for virtual keys along with its relationships
</Update>

<Update label="governance" description="v1.3.4">
  * chore: version update core to 1.2.10 and framework to 1.1.10
  * feat: added virtual key level support for MCP tools to execute
</Update>

<Update label="jsonparser" description="v1.3.4">
  * chore: version update core to 1.2.10 and framework to 1.1.10
</Update>

<Update label="logging" description="v1.3.4">
  * chore: version update core to 1.2.10 and framework to 1.1.10
</Update>

<Update label="maxim" description="v1.3.4">
  * chore: version update core to 1.2.10 and framework to 1.1.10
</Update>

<Update label="mocker" description="v1.3.4">
  * chore: version update core to 1.2.10 and framework to 1.1.10
</Update>

<Update label="otel" description="v1.3.4">
  * chore: version update core to 1.2.10 and framework to 1.1.10
</Update>

<Update label="semanticcache" description="v1.3.4">
  * chore: version update core to 1.2.10
</Update>

<Update label="telemetry" description="v1.3.4">
  * chore: version update core to 1.2.10 and framework to 1.1.10
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt