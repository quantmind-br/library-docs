---
title: v1.3.2
url: https://docs.getbifrost.ai/changelogs/v1.3.2.md
source: llms
fetched_at: 2026-01-21T19:41:49.581166367-03:00
rendered_js: false
word_count: 241
summary: This document outlines the changes in Bifrost version 1.3.2, including major refactoring of context keys, bug fixes for trace identification, and dependency updates across core modules.
tags:
    - release-notes
    - changelog
    - bifrost
    - version-update
    - bug-fix
    - refactoring
category: reference
---

# v1.3.2

> v1.3.2 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.2
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.2
    docker run -p 8080:8080 maximhq/bifrost:v1.3.2
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.2">
  * Refactor: Moves all context key types to schemas.BifrostContextKey
  * Fix: Fixes Maxim plugin bug where external traceId were blocking new trace creations
</Update>

<Update label="Core" description="v1.3.2">
  * Chore: Now schema.BifrostContextKey is the only valid ctx key type throughout the project
</Update>

<Update label="Framework" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
  * Chore: Adds new logs table migration to avoid missing any required columns in the DB
</Update>

<Update label="governance" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
</Update>

<Update label="jsonparser" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
</Update>

<Update label="logging" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
</Update>

<Update label="maxim" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
  * Fix: Fixes a bug where external trace id was blocking new trace creation
</Update>

<Update label="mocker" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
</Update>

<Update label="otel" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
</Update>

<Update label="semanticcache" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
</Update>

<Update label="telemetry" description="v1.3.2">
  * Upgrade dependency: core to 1.2.8
  * Chore: Moves all context key types to schemas.BifrostContextKey
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt