---
title: v1.3.61
url: https://docs.getbifrost.ai/changelogs/v1.3.61.md
source: llms
fetched_at: 2026-01-21T19:42:45.028532833-03:00
rendered_js: false
word_count: 204
summary: This document outlines the updates for Bifrost version 1.3.61, including bug fixes for Gemini chat converters and various component version upgrades.
tags:
    - changelog
    - release-notes
    - bifrost
    - gemini-integration
    - version-update
category: other
---

# v1.3.61

> v1.3.61 changelog - 2026-01-07

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.61
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.61
    docker run -p 8080:8080 maximhq/bifrost:v1.3.61
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.61">
  * fix: image url and input audio handling in gemini chat converters
  * fix: support both responseJsonSchema and responseSchema for JSON response formatting in gemini
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="Core" description="1.2.48">
  * fix: image url and input audio handling in gemini chat converters
  * fix: support both responseJsonSchema and responseSchema for JSON response formatting in gemini
</Update>

<Update label="Framework" description="1.1.60">
  * chore: upgrades core to v1.2.48
</Update>

<Update label="governance" description="1.3.61">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="jsonparser" description="1.3.61">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="logging" description="1.3.61">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="maxim" description="1.4.62">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="mocker" description="1.3.59">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="otel" description="1.0.60">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="semanticcache" description="1.3.60">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>

<Update label="telemetry" description="1.3.60">
  * chore: upgrades core to v1.2.48 and framework to 1.1.60
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt