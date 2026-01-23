---
title: v1.3.10
url: https://docs.getbifrost.ai/changelogs/v1.3.10.md
source: llms
fetched_at: 2026-01-21T19:41:36.289241247-03:00
rendered_js: false
word_count: 400
summary: This document provides the version 1.3.10 changelog for Bifrost, detailing new features, performance improvements, and bug fixes across core modules and provider integrations.
tags:
    - release-notes
    - changelog
    - bifrost
    - otel
    - vertex-api
    - version-update
    - bug-fixes
category: other
---

# v1.3.10

> v1.3.10 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.10
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.10
    docker run -p 8080:8080 maximhq/bifrost:v1.3.10
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
  * feat: added headers support for OTel configuration. Value prefixed with env will be fetched from environment variables (`env.ENV_VAR_NAME`)
  * feat: emission of OTel resource spans is completely async - this brings down inference overhead to \< 1µsecond
  * fix: added latency calculation for vertex native requests
  * feat: added cached tokens and reasoning tokens to the usage in ui
  * fix: cost calculation for vertex requests
  * feat: added global region support for vertex API
  * fix: added filter for extra fields in chat completions request for Mistral provider
  * fix: added wildcard validation for allowed origins in UI security settings
  * fix: fixed code field in pending\_safety\_checks for Responses API
</Update>

<Update label="Core" description="v1.3.10">
  * bug: fixed embedding request not being handled in `GetExtraFields()` method of `BifrostResponse`
  * fix: added latency calculation for vertex native requests
  * feat: added cached tokens and reasoning tokens to the usage metadata for chat completions
  * feat: added global region support for vertex API
  * fix: added filter for extra fields in chat completions request for Mistral provider
  * fix: fixed ResponsesComputerToolCallPendingSafetyCheck code field
</Update>

<Update label="Framework" description="v1.3.10">
  * chore: version update core to 1.2.13
  * feat: added support for vertex provider/model format in pricing lookup
</Update>

<Update label="governance" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
</Update>

<Update label="jsonparser" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
</Update>

<Update label="logging" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
</Update>

<Update label="maxim" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
</Update>

<Update label="mocker" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
  * feat: added support for responses request
  * feat: added "skip-mocker" context key to skip mocker plugin per request
</Update>

<Update label="otel" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
  * feat: added headers support for OTel configuration. Value prefixed with env will be fetched from environment variables (`env.ENV_VAR_NAME`)
  * feat: emission of OTel resource spans is completely async - this brings down inference overhead to \< 1µsecond
</Update>

<Update label="semanticcache" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
  * tests: added mocker plugin to all chat/responses tests
</Update>

<Update label="telemetry" description="v1.3.10">
  * chore: version update core to 1.2.13 and framework to 1.1.15
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt