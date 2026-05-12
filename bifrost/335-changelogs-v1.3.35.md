---
title: v1.3.35
url: https://docs.getbifrost.ai/changelogs/v1.3.35.md
source: llms
fetched_at: 2026-01-21T19:42:10.747706903-03:00
rendered_js: false
word_count: 225
summary: This document outlines the updates and bug fixes for Bifrost version 1.3.35, including new support for Qdrant Vector Search and various streaming response improvements.
tags:
    - changelog
    - release-notes
    - qdrant
    - vector-search
    - bug-fixes
    - streaming
category: reference
---

# v1.3.35

> v1.3.35 changelog - 2025-11-24

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.35
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.35
    docker run -p 8080:8080 maximhq/bifrost:v1.3.35
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.35">
  * feat: Qdrant Vector Search Support (#893)
  * fix: bedrock responses streaming last chunk indicator fixes
  * fix: gemini nil content check fixes
  * fix: handle responses.incomplete event in openai responses streaming
  * fix: stream accumulator nil content check fixes
</Update>

<Update label="Core" description="1.2.30">
  * fix: bedrock responses streaming last chunk indicator fixes
  * fix: gemini nil content check fixes
  * fix: handle responses.incomplete event in openai responses streaming
  * enhancements: provider tests enhancements
</Update>

<Update label="Framework" description="1.1.38">
  * feat: Qdrant Vector Search Support (#893)
  * fix: stream accumulator nil content check fixes
  * enhancement: added transactions on provider config updates
</Update>

<Update label="governance" description="1.3.39">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>

<Update label="jsonparser" description="1.3.39">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>

<Update label="logging" description="1.3.39">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>

<Update label="maxim" description="1.4.38">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>

<Update label="mocker" description="1.3.38">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>

<Update label="otel" description="1.0.38">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>

<Update label="semanticcache" description="1.3.38">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>

<Update label="telemetry" description="1.3.38">
  * chore: upgrades core to 1.2.30 and framework to 1.1.38
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt