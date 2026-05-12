---
title: v1.4.0
url: https://docs.getbifrost.ai/changelogs/v1.4.0.md
source: llms
fetched_at: 2026-01-21T19:42:52.409729189-03:00
rendered_js: false
word_count: 244
summary: This document outlines the version 1.4.0 changelog for Bifrost, detailing new features, bug fixes, and dependency updates across its core components and plugins.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - software-maintenance
category: reference
---

# v1.4.0

> v1.4.0 changelog - 2026-01-18

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0">
  * feat: allowed provider config to use in-memory usage tracking for expired counters
  * feat: added retries on network lookup errors
</Update>

<Update label="Core" description="1.3.10">
  * feat: added retries on network lookup errors
  * fix: properly propagate cost details for openrouter responses
  * fix: removes litellm fallback handling on provider level. moved that logic to plugin
</Update>

<Update label="Framework" description="1.2.11">
  * fix: properly propagate cost details in responses accumulator
  * feat: added refine model util function to model catalog
  * chore: upgrades to core 1.3.10
</Update>

<Update label="governance" description="1.4.12">
  * fix: edge case when usage is reset to 0 on updating config
  * feat: allowed provider config to use in-memory usage tracking for expired counters
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>

<Update label="jsonparser" description="1.4.11">
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>

<Update label="litellmcompat" description="0.0.1">
  * feat: hello world
</Update>

<Update label="logging" description="1.4.11">
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>

<Update label="maxim" description="1.5.10">
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>

<Update label="mocker" description="1.4.11">
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>

<Update label="otel" description="1.1.11">
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>

<Update label="semanticcache" description="1.4.11">
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>

<Update label="telemetry" description="1.4.12">
  * chore: updates core to 1.3.10 and framework to 1.2.11
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt