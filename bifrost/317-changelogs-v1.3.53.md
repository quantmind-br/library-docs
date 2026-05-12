---
title: v1.3.53
url: https://docs.getbifrost.ai/changelogs/v1.3.53.md
source: llms
fetched_at: 2026-01-21T19:42:33.691563555-03:00
rendered_js: false
word_count: 232
summary: This document outlines the changes and bug fixes introduced in Bifrost version 1.3.53, including improvements to Anthropic and Bedrock provider integrations.
tags:
    - changelog
    - release-notes
    - bifrost
    - bug-fixes
    - anthropic
    - bedrock
    - version-update
category: other
---

# v1.3.53

> v1.3.53 changelog - 2025-12-23

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.53
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.53
    docker run -p 8080:8080 maximhq/bifrost:v1.3.53
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.53">
  * fix: thought signature handling in anthropic converters
  * fix: added support for the reasoning\_max\_tokens parameter in chat completions
  * fix: reasoning effort calculation in Bedrock provider by using default max tokens when inference config max tokens is not provided.
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="Core" description="1.2.42">
  * fix: thought signature handling in anthropic converters
  * fix: added support for the reasoning\_max\_tokens parameter in chat completions
  * fix: reasoning effort calculation in Bedrock provider by using default max tokens when inference config max tokens is not provided.
</Update>

<Update label="Framework" description="1.1.52">
  * chore: bumped core to 1.2.42
</Update>

<Update label="governance" description="1.3.53">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="jsonparser" description="1.3.53">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="logging" description="1.3.53">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="maxim" description="1.4.53">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="mocker" description="1.3.52">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="otel" description="1.0.52">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="semanticcache" description="1.3.52">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>

<Update label="telemetry" description="1.3.52">
  * chore: bumped core to 1.2.42 and framework to 1.1.52
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt