---
title: v1.4.0-prerelease3
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease3.md
source: llms
fetched_at: 2026-01-21T19:42:57.155054068-03:00
rendered_js: false
word_count: 263
summary: This document outlines the updates and bug fixes for the v1.4.0-prerelease3 release, covering provider-specific improvements and authentication enhancements across the Bifrost ecosystem.
tags:
    - changelog
    - release-notes
    - bifrost
    - bug-fixes
    - azure-entra-id
    - anthropic
    - gemini
category: other
---

# v1.4.0-prerelease3

> v1.4.0-prerelease3 changelog - 2026-01-02

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease3
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease3
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease3
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease3">
  * chore: added max\_tokens -> max\_completion\_tokens mapping for chat completions
  * fix: empty string handling in Anthropic provider to prevent sending empty content blocks in chat requests
  * fix: Gemini/Vertex tool conversion to append all function declarations to a single Tool object
  * feat: added Azure Entra ID (Service Principal) authentication support to the Azure provider
  * fix: tracing flow overriding request id which resulted in breaking streaming responses
</Update>

<Update label="Core" description="1.3.2">
  fix: empty string handling in Anthropic provider to prevent sending empty content blocks in chat requests
  fix: Gemini/Vertex tool conversion to append all function declarations to a single Tool object
  feat: added Azure Entra ID (Service Principal) authentication support to the Azure provider
</Update>

<Update label="Framework" description="1.2.2">
  fix: fixed tracer overriding the requestId flows
  chore: upgrades core to 1.3.2
</Update>

<Update label="governance" description="1.4.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>

<Update label="jsonparser" description="1.4.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>

<Update label="logging" description="1.4.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>

<Update label="maxim" description="1.5.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>

<Update label="mocker" description="1.4.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>

<Update label="otel" description="1.1.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>

<Update label="semanticcache" description="1.4.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>

<Update label="telemetry" description="1.4.2">
  * chore: upgrade core to 1.3.2 and framework to 1.2.2
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt