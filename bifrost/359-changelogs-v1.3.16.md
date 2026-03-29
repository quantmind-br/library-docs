---
title: v1.3.16
url: https://docs.getbifrost.ai/changelogs/v1.3.16.md
source: llms
fetched_at: 2026-01-21T19:41:43.944531474-03:00
rendered_js: false
word_count: 223
summary: This document details the updates in version 1.3.16 of Bifrost, highlighting new provider support for Perplexity and MistralAI, and enhancements to Anthropic stream handling.
tags:
    - changelog
    - bifrost
    - release-notes
    - perplexity
    - mistralai
    - anthropic
    - vertex-ai
category: other
---

# v1.3.16

> v1.3.16 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.16
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.16
    docker run -p 8080:8080 maximhq/bifrost:v1.3.16
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.16">
  * chore: version update core to 1.2.18 and framework to 1.1.21
  * feat: added Perplexity provider support
  * chore: version update core to 1.2.19 and framework to 1.1.22
  * feat: support for mistralai publisher endpoint in vertex provider
  * enhancement: Anthropic's computer tool in the Responses API stream handling,
</Update>

<Update label="Core" description="v1.3.16">
  * feat: support for mistralai publisher endpoint in vertex provider
  * enhancement: Anthropic's computer tool in the Responses API stream handling,
  * feat: added Perplexity provider support
</Update>

<Update label="Framework" description="v1.3.16">
  * chore: Upgrades core to 1.2.19
</Update>

<Update label="governance" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>

<Update label="jsonparser" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>

<Update label="logging" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>

<Update label="maxim" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>

<Update label="mocker" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>

<Update label="otel" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>

<Update label="semanticcache" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>

<Update label="telemetry" description="v1.3.16">
  * chore: version update core to 1.2.19 and framework to 1.1.22
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt