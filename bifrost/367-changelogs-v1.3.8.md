---
title: v1.3.8
url: https://docs.getbifrost.ai/changelogs/v1.3.8.md
source: llms
fetched_at: 2026-01-21T19:42:49.453167878-03:00
rendered_js: false
word_count: 208
summary: Detailed release notes for Bifrost version 1.3.8, highlighting bug fixes for OpenAI and Gemini providers and a breaking change regarding JSON schema fields.
tags:
    - release-notes
    - bifrost
    - changelog
    - bug-fixes
    - breaking-changes
    - openai
    - gemini
category: other
---

# v1.3.8

> v1.3.8 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.8
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.8
    docker run -p 8080:8080 maximhq/bifrost:v1.3.8
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
  * fix: openai specific parameters filtered for openai compatibile providers
  * fix: error response unmarshalling for gemini provider
</Update>

<Update label="Core" description="v1.3.8">
  * fix: openai specific parameters filtered for openai compatibile providers
  * fix: error response unmarshalling for gemini provider
  * BREAKING FIX: json\_schema field correctly renamed to schema; ResponsesTextConfigFormatJSONSchema restructured
</Update>

<Update label="Framework" description="v1.3.8">
  * chore: version update core to 1.2.12
</Update>

<Update label="governance" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>

<Update label="jsonparser" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>

<Update label="logging" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>

<Update label="maxim" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>

<Update label="mocker" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>

<Update label="otel" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>

<Update label="semanticcache" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>

<Update label="telemetry" description="v1.3.8">
  * chore: version update core to 1.2.12 and framework to 1.1.14
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt