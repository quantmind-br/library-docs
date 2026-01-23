---
title: v1.2.21
url: https://docs.getbifrost.ai/changelogs/v1.2.21.md
source: llms
fetched_at: 2026-01-21T19:41:18.271782117-03:00
rendered_js: false
word_count: 121
summary: This document outlines the changes in Bifrost version 1.2.21, including fixes for pricing computation with nested model names and framework upgrades across several modules.
tags:
    - bifrost
    - changelog
    - release-notes
    - bug-fix
    - pricing-module
    - framework-upgrade
category: reference
---

# v1.2.21

> v1.2.21 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.2.21
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.2.21
    docker run -p 8080:8080 maximhq/bifrost:v1.2.21
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.2.21">
  * Fixes pricing computation for nested model names i.e. groq/openai/gpt-oss-20b.
</Update>

<Update label="Framework" description="v1.2.21">
  * Pricing module now accommodates nested model names i.e. groq/openai/gpt-oss-20b was getting skipped while computing costs.
</Update>

<Update label="governance" description="v1.2.21">
  * Upgrades framework to 1.0.23
</Update>

<Update label="jsonparser" description="v1.2.21">
  * Upgrades framework to 1.0.23
</Update>

<Update label="logging" description="v1.2.21">
  * Upgrades framework to 1.0.23
  * Fixes pricing computation for nested model names.
</Update>

<Update label="maxim" description="v1.2.21">
  * Upgrades framework to 1.0.23
</Update>

<Update label="mocker" description="v1.2.21">
  * Upgrades framework to 1.0.23
</Update>

<Update label="semanticcache" description="v1.2.21">
  * Upgrades framework to 1.0.23
</Update>

<Update label="telemetry" description="v1.2.21">
  * Upgrades framework to 1.0.23
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt