---
title: v1.3.0-prerelease3
url: https://docs.getbifrost.ai/changelogs/v1.3.0-prerelease3.md
source: llms
fetched_at: 2026-01-21T19:41:28.590902172-03:00
rendered_js: false
word_count: 168
summary: This document provides the changelog for Bifrost version 1.3.0-prerelease3, detailing bug fixes for string inputs and new features for OpenAI integration.
tags:
    - bifrost
    - release-notes
    - changelog
    - openai-integration
    - bug-fixes
category: other
---

# v1.3.0-prerelease3

> v1.3.0-prerelease3 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.0-prerelease3
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.0-prerelease3
    docker run -p 8080:8080 maximhq/bifrost:v1.3.0-prerelease3
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.0-prerelease3">
  * Fix: Fixes string input support for responses requests.
  * Feat: Adds responses endpoint to openai integration.
</Update>

<Update label="Core" description="v1.3.0-prerelease3">
  * Fix: String inputs tranformat added for responses requests.
</Update>

<Update label="Framework" description="v1.3.0-prerelease3">
  * Chore: core upgrades to 1.2.2
</Update>

<Update label="governance" description="v1.3.0-prerelease3">
  * Chore: using core 1.2.2 and framework 1.1.2
</Update>

<Update label="jsonparser" description="v1.3.0-prerelease3">
  * Upgrade dependency: core to 1.2.2 and framework to 1.1.2
</Update>

<Update label="logging" description="v1.3.0-prerelease3">
  * Upgrade dependency: core to 1.2.2 and framework to 1.1.2
</Update>

<Update label="maxim" description="v1.3.0-prerelease3">
  * Upgrade dependency: core to 1.2.2 and framework to 1.1.2
</Update>

<Update label="mocker" description="v1.3.0-prerelease3">
  * Upgrade dependency: core to 1.2.2 and framework to 1.1.2
</Update>

<Update label="otel" description="v1.3.0-prerelease3">
  * Upgrade dependency: core to 1.2.2 and framework to 1.1.2
</Update>

<Update label="semanticcache" description="v1.3.0-prerelease3">
  * Upgrade dependency: core to 1.2.2 and framework to 1.1.2
</Update>

<Update label="telemetry" description="v1.3.0-prerelease3">
  * Upgrade dependency: core to 1.2.2 and framework to 1.1.2
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt