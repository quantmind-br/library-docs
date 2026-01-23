---
title: v1.3.60
url: https://docs.getbifrost.ai/changelogs/v1.3.60.md
source: llms
fetched_at: 2026-01-21T19:42:44.149082769-03:00
rendered_js: false
word_count: 150
summary: This document outlines the version 1.3.60 release notes for the Bifrost platform, detailing updates to authentication, documentation workflows, and framework dependencies.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - software-maintenance
category: other
---

# v1.3.60

> v1.3.60 changelog - 2026-01-07

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.60
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.60
    docker run -p 8080:8080 maximhq/bifrost:v1.3.60
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.60">
  * feat: remove restart required for auth config changes
  * fix: resolved issue where new auth configs were not being created
  * ci: added workflow to auto-generate openapi.json documentation when openapi yaml files change
</Update>

<Update label="Framework" description="1.1.59">
  * feat: added flush session functionality to config store to clear all existing sessions
</Update>

<Update label="governance" description="1.3.60">
  * chore: update framework version to 1.1.59
</Update>

<Update label="jsonparser" description="1.3.60">
  * chore: update framework version to 1.1.59
</Update>

<Update label="logging" description="1.3.60">
  * chore: update framework version to 1.1.59
</Update>

<Update label="maxim" description="1.4.61">
  * chore: update framework version to 1.1.59
</Update>

<Update label="otel" description="1.0.59">
  * chore: update framework version to 1.1.59
</Update>

<Update label="semanticcache" description="1.3.59">
  * chore: update framework version to 1.1.59
</Update>

<Update label="telemetry" description="1.3.59">
  * chore: update framework version to 1.1.59
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt