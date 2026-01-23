---
title: v1.4.0-prerelease6
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease6.md
source: llms
fetched_at: 2026-01-21T19:43:02.113248487-03:00
rendered_js: false
word_count: 294
summary: This document provides the release notes for Bifrost version 1.4.0-prerelease6, documenting various bug fixes, feature enhancements, and dependency updates across the platform's components.
tags:
    - release-notes
    - changelog
    - bifrost
    - software-updates
    - version-history
category: reference
---

# v1.4.0-prerelease6

> v1.4.0-prerelease6 changelog - 2026-01-07

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease6
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease6
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease6
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease6">
  * feat: remove restart required for auth config changes
  * fix: resolved issue where new auth configs were not being created
  * ci: added workflow to auto-generate openapi.json documentation when openapi yaml files change
  * fix: tracer lifecycle management fixes
  * fix: stream accumulator deduplication fixes
  * fix: image url and input audio handling in gemini chat converters
  * fix: support both responseJsonSchema and responseSchema for JSON response formatting in gemini
  * fix: disable auth on inference routes not working correctly
  * fix: fixes Anthropic to Azure/OpenAI for input\_text/output\_text
</Update>

<Update label="Core" description="1.3.5">
  * fix: tracer lifecycle management fixes
  * fix: image url and input audio handling in gemini chat converters
  * fix: support both responseJsonSchema and responseSchema for JSON response formatting in gemini
  * fix: fixes Anthropic to Azure/OpenAI for input\_text/output\_text
</Update>

<Update label="Framework" description="1.2.5">
  * feat: added flush session functionality to config store to clear all existing sessions
  * fix: stream accumulator reference count management fixes
  * fix: stream accumulator deduplication fixes
</Update>

<Update label="governance" description="1.4.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
</Update>

<Update label="jsonparser" description="1.4.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
</Update>

<Update label="logging" description="1.4.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
  * fix: streaming tracer cleanup fixes
</Update>

<Update label="maxim" description="1.5.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
  * fix: streaming tracer cleanup fixes
</Update>

<Update label="mocker" description="1.4.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
</Update>

<Update label="otel" description="1.1.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
</Update>

<Update label="semanticcache" description="1.4.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
</Update>

<Update label="telemetry" description="1.4.5">
  * chore: upgrades core to v1.3.4 and framework to 1.2.4
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt