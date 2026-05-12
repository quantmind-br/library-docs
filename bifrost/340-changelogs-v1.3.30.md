---
title: v1.3.30
url: https://docs.getbifrost.ai/changelogs/v1.3.30.md
source: llms
fetched_at: 2026-01-21T19:42:05.133106241-03:00
rendered_js: false
word_count: 138
summary: This document outlines the changes in version 1.3.30 of Bifrost, including database migrations for the provider column and framework updates across multiple modules.
tags:
    - changelog
    - release-notes
    - bifrost
    - database-migration
    - version-update
category: other
---

# v1.3.30

> v1.3.30 changelog - 2025-11-18

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.30
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.30
    docker run -p 8080:8080 maximhq/bifrost:v1.3.30
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.30">
  * feat: adds migration for missing provider column in key table

  <Warning>
    "keys" in "provider\_config" in `config.json` file requires unique name. If there is any collision, Bifrost wont be able to boot.
  </Warning>
</Update>

<Update label="Framework" description="1.1.33">
  feat: add migration for missing provider column in key table
</Update>

<Update label="governance" description="1.3.34">
  chore: update framework version to 1.1.33
</Update>

<Update label="jsonparser" description="1.3.34">
  chore: update framework version to 1.1.33
</Update>

<Update label="logging" description="1.3.34">
  chore: update framework version to 1.1.33
</Update>

<Update label="maxim" description="1.4.33">
  chore: update framework version to 1.1.33
</Update>

<Update label="mocker" description="1.3.33">
  chore: update framework version to 1.1.33
</Update>

<Update label="otel" description="1.0.33">
  chore: update framework version to 1.1.33
</Update>

<Update label="semanticcache" description="1.3.33">
  chore: update framework version to 1.1.33
</Update>

<Update label="telemetry" description="1.3.33">
  chore: update framework version to 1.1.33
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt