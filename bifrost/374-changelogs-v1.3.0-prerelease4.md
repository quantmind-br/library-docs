---
title: v1.3.0-prerelease4
url: https://docs.getbifrost.ai/changelogs/v1.3.0-prerelease4.md
source: llms
fetched_at: 2026-01-21T19:41:29.387196149-03:00
rendered_js: false
word_count: 188
summary: This document outlines the changes and installation steps for Bifrost version 1.3.0-prerelease4, featuring a new LiteLLM fallback for Groq and various core component upgrades.
tags:
    - bifrost
    - changelog
    - release-notes
    - groq
    - litellm
    - version-update
    - docker
category: reference
---

# v1.3.0-prerelease4

> v1.3.0-prerelease4 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.0-prerelease4
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.0-prerelease4
    docker run -p 8080:8080 maximhq/bifrost:v1.3.0-prerelease4
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.0-prerelease4">
  * Feat: A new config called `Enable LiteLLM Fallback` that enables text\_completion calls to fall back to chat\_completions calls for the Groq provider. This is an anti-pattern, but we are adding this to help users migrate from LiteLLM easily. Reach out to us if you want us to enable any other quirky patterns LiteLLM has.
</Update>

<Update label="Core" description="v1.3.0-prerelease4">
  * Feat: Adds litellm-specific fallbacks for text completion for Groq. This enables users with codebases stuck in this antipattern out-of-the-box.
</Update>

<Update label="Framework" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="governance" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="jsonparser" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="logging" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="maxim" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="mocker" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="otel" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="semanticcache" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>

<Update label="telemetry" description="v1.3.0-prerelease4">
  * Chore: core upgrades to 1.2.3
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt