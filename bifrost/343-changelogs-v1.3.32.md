---
title: v1.3.32
url: https://docs.getbifrost.ai/changelogs/v1.3.32.md
source: llms
fetched_at: 2026-01-21T19:42:07.064060757-03:00
rendered_js: false
word_count: 279
summary: This document outlines the version 1.3.32 changelog for Bifrost, detailing new features for Anthropic and Gemini providers alongside various bug fixes and component updates.
tags:
    - release-notes
    - changelog
    - bifrost
    - anthropic-integration
    - gemini-integration
    - version-update
    - bug-fixes
category: reference
---

# v1.3.32

> v1.3.32 changelog - 2025-11-20

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.32
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.32
    docker run -p 8080:8080 maximhq/bifrost:v1.3.32
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.32">
  * feat: support added for structured output Anthropic provider
  * fix: Gemini thought signature preservation for multi-turn function calling (#879)
  * fix: responses API stream lifecycle events fixes
  * fix: embedding models usage with vertex provider using gemini integration
  * feat: support for anthropic passthrough in streaming for claude code
  * fix: lookup for virtual key in authorization and x-api-key headers for provider routing
  * fix: added responses stream passthrough for codex in openai integration
</Update>

<Update label="Core" description="1.2.28">
  * feat: support added for structured output Anthropic provider
  * fix: Gemini thought signature preservation for multi-turn function calling (#879)
  * fix: responses API stream lifecycle events fixes
  * feat: support for anthropic passthrough in streaming for claude code
</Update>

<Update label="Framework" description="1.1.35">
  chore: update core version to 1.2.28
</Update>

<Update label="governance" description="1.3.36">
  * chore: update core version to 1.2.28 and framework version to 1.1.35
  * fix: lookup for virtual key in authorization and x-api-key headers
</Update>

<Update label="jsonparser" description="1.3.36">
  chore: update core version to 1.2.28 and framework version to 1.1.35
</Update>

<Update label="logging" description="1.3.36">
  chore: update core version to 1.2.28 and framework version to 1.1.35
</Update>

<Update label="maxim" description="1.4.35">
  chore: update core version to 1.2.28 and framework version to 1.1.35
</Update>

<Update label="mocker" description="1.3.35">
  chore: update core version to 1.2.28 and framework version to 1.1.35
</Update>

<Update label="otel" description="1.0.35">
  chore: update core version to 1.2.28 and framework version to 1.1.35
</Update>

<Update label="semanticcache" description="1.3.35">
  chore: update core version to 1.2.28 and framework version to 1.1.35
</Update>

<Update label="telemetry" description="1.3.35">
  chore: update core version to 1.2.28 and framework version to 1.1.35
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt