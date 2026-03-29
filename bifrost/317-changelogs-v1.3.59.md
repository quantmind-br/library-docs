---
title: v1.3.59
url: https://docs.getbifrost.ai/changelogs/v1.3.59.md
source: llms
fetched_at: 2026-01-21T19:42:40.718227244-03:00
rendered_js: false
word_count: 246
summary: This document outlines the changes, bug fixes, and new features introduced in Bifrost version 1.3.59, including improved structured output support for AI providers and core framework updates.
tags:
    - release-notes
    - changelog
    - bifrost
    - gemini
    - anthropic
    - structured-outputs
    - bug-fixes
category: reference
---

# v1.3.59

> v1.3.59 changelog - 2026-01-05

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.59
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.59
    docker run -p 8080:8080 maximhq/bifrost:v1.3.59
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.59">
  * feat: added support for multiple types in gemini and anthropic structured outputs properties
  * fix: added missing logs filter checks in ui for live updates
  * fix: ensure request ID is consistently set in context before PreHooks are executed
  * docs: updated docs for xai provider
  * fix: correct conversion of thinking level to thinking budget and vice versa in gemini
</Update>

<Update label="Core" description="1.2.47">
  * feat: added support for multiple types in gemini and anthropic structured outputs properties
  * fix: ensure request ID is consistently set in context before PreHooks are executed
  * fix: correct conversion of thinking level to thinking budget and vice versa in gemini
</Update>

<Update label="Framework" description="1.1.58">
  * chore: upgrades core to 1.2.47
</Update>

<Update label="governance" description="1.3.59">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>

<Update label="jsonparser" description="1.3.59">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>

<Update label="logging" description="1.3.59">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>

<Update label="maxim" description="1.4.60">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>

<Update label="mocker" description="1.3.58">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>

<Update label="otel" description="1.0.58">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>

<Update label="semanticcache" description="1.3.58">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>

<Update label="telemetry" description="1.3.58">
  * chore: upgrades core to 1.2.47  and framework to 1.1.58
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt