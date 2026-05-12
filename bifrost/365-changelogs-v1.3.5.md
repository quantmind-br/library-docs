---
title: v1.3.5
url: https://docs.getbifrost.ai/changelogs/v1.3.5.md
source: llms
fetched_at: 2026-01-21T19:42:28.346508861-03:00
rendered_js: false
word_count: 186
summary: This document outlines the release notes and changelog for Bifrost version 1.3.5, detailing new features, bug fixes, and framework updates across various components.
tags:
    - changelog
    - release-notes
    - bifrost
    - software-update
    - database-migration
    - mcp-client
category: reference
---

# v1.3.5

> v1.3.5 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.5
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.5
    docker run -p 8080:8080 maximhq/bifrost:v1.3.5
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.5">
  * chore: version update framework to 1.1.11
  * fix: added missing migration for `cost` and `cache_debug` columns in logs table for old databases.
</Update>

<Update label="Core" description="v1.3.5">
  * Feat: Added key name field to account schema for external key management
  * Feat: Simplified MCP client management by removing toolsToSkip field, allowing wildcard (\*) for all tools, and better tool filtering logic.
</Update>

<Update label="Framework" description="v1.3.5">
  * Fix: Added missing migration for `cost` and `cache_debug` columns in logs table for old databases.
</Update>

<Update label="governance" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>

<Update label="jsonparser" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>

<Update label="logging" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>

<Update label="maxim" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>

<Update label="mocker" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>

<Update label="otel" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>

<Update label="semanticcache" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>

<Update label="telemetry" description="v1.3.5">
  * chore: version update framework to 1.1.11
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt