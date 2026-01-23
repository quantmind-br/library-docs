---
title: v1.3.63
url: https://docs.getbifrost.ai/changelogs/v1.3.63.md
source: llms
fetched_at: 2026-01-21T19:42:47.749549144-03:00
rendered_js: false
word_count: 172
summary: This document details the changelog for version 1.3.63 of Bifrost, covering bug fixes for authentication and provider mappings alongside component updates across the framework.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - bug-fixes
    - deployment
category: reference
---

# v1.3.63

> v1.3.63 changelog - 2026-01-07

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.63
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.63
    docker run -p 8080:8080 maximhq/bifrost:v1.3.63
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.63">
  * fix: disable auth on inference routes not working correctly
  * fix: fixes Anthropic to Azure/OpenAI for input\_text/output\_text
</Update>

<Update label="Core" description="1.2.49">
  * fix: fixes Anthropic to Azure/OpenAI for input\_text/output\_text
</Update>

<Update label="Framework" description="1.1.61">
  * chore: updates core to 1.2.49
</Update>

<Update label="governance" description="1.3.62">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>

<Update label="jsonparser" description="1.3.62">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>

<Update label="logging" description="1.3.62">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>

<Update label="maxim" description="1.4.63">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>

<Update label="mocker" description="1.3.60">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>

<Update label="otel" description="1.0.61">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>

<Update label="semanticcache" description="1.3.61">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>

<Update label="telemetry" description="1.3.61">
  * chore: updates core to 1.2.49 and framework to 1.1.61
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt