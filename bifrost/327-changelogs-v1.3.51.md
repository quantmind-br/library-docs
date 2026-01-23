---
title: v1.3.51
url: https://docs.getbifrost.ai/changelogs/v1.3.51.md
source: llms
fetched_at: 2026-01-21T19:42:31.398723788-03:00
rendered_js: false
word_count: 286
summary: This document outlines the changes, bug fixes, and new features introduced in version 1.3.51 of Bifrost, including HuggingFace provider support and proxy enhancements.
tags:
    - release-notes
    - changelog
    - bifrost
    - huggingface
    - bug-fixes
    - proxy-support
    - mcp-tools
category: other
---

# v1.3.51

> v1.3.51 changelog - 2025-12-19

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.51
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.51
    docker run -p 8080:8080 maximhq/bifrost:v1.3.51
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.51">
  * fix: ensure properties field is always set for mcp tools - [@CryptoFewka](https://github.com/CryptoFewka)
  * fix: correct search\_domain\_filter json tag in perplexity provider - [@hnoguchigr](https://github.com/hnoguchigr)
  * feat: added HuggingFace provider
  * fix: bedrock empty ARN issue causing request to fail
  * fix: anthropic single context block in response converted to string instead for chat completions
  * fix: added auth support in HTTP proxies
  * feat: added custom CA certificate support in proxies
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="Core" description="1.2.40">
  * fix: ensure properties field is always set for mcp tools - [@CryptoFewka](https://github.com/CryptoFewka)
  * fix: correct search\_domain\_filter json tag in perplexity provider - [@hnoguchigr](https://github.com/hnoguchigr)
  * feat: added HuggingFace provider
  * fix: bedrock empty ARN issue causing request to fail
  * fix: anthropic single context block in response converted to string instead for chat completions
  * fix: added auth support in HTTP proxies
  * feat: added custom CA certificate support in proxies
</Update>

<Update label="Framework" description="1.1.50">
  * chore: bump core to 1.2.40
</Update>

<Update label="governance" description="1.3.51">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="jsonparser" description="1.3.51">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="logging" description="1.3.51">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="maxim" description="1.4.51">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="mocker" description="1.3.50">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="otel" description="1.0.50">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="semanticcache" description="1.3.50">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>

<Update label="telemetry" description="1.3.50">
  * chore: bump core to 1.2.40 and framework to 1.1.50
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt