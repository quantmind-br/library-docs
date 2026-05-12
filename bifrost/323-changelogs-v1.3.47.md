---
title: v1.3.47
url: https://docs.getbifrost.ai/changelogs/v1.3.47.md
source: llms
fetched_at: 2026-01-21T19:42:26.979647947-03:00
rendered_js: false
word_count: 280
summary: This document outlines the version 1.3.47 release notes for Bifrost, detailing new features such as raw request logging, reasoning support in chat completions, and migration to the Gemini native API.
tags:
    - changelog
    - bifrost
    - release-notes
    - chat-completions
    - api-updates
    - logging
category: reference
---

# v1.3.47

> v1.3.47 changelog - 2025-12-12

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.47
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.47
    docker run -p 8080:8080 maximhq/bifrost:v1.3.47
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.47">
  * feat: support for raw response accumulation for streaming
  * feat: support for raw request logging and sending back in response
  * feat: added support for reasoning in chat completions
  * feat: enhanced reasoning support in responses api
  * enhancement: improved internal inter provider conversions for integrations
  * feat: switched to gemini native api
</Update>

<Update label="Core" description="1.2.37">
  * feat: send back raw request in extra fields
  * feat: added support for reasoning in chat completions
  * feat: enhanced reasoning support in responses api
  * enhancement: improved internal inter provider conversions for integrations
  * feat: switched to gemini native api
  * feat: fallback to supported request type for custom models used in integration
</Update>

<Update label="Framework" description="1.1.47">
  * feat: support raw response accumulation in stream accumulator
  * feat: support raw request configuration and logging
  * feat: added support for reasoning accumulation in stream accumulator
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="governance" description="1.3.48">
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="jsonparser" description="1.3.48">
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="logging" description="1.3.48">
  * feat: support for raw request logging
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="maxim" description="1.4.48">
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="mocker" description="1.3.47">
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="otel" description="1.0.47">
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="semanticcache" description="1.3.47">
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>

<Update label="telemetry" description="1.3.47">
  * chore: updating core to 1.2.37 and framework to 1.1.47
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt