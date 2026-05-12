---
title: v1.3.0-prerelease7
url: https://docs.getbifrost.ai/changelogs/v1.3.0-prerelease7.md
source: llms
fetched_at: 2026-01-21T19:41:33.345502964-03:00
rendered_js: false
word_count: 239
summary: Detailed changelog for Bifrost v1.3.0-prerelease7, highlighting new streaming capabilities, telemetry fixes, and core dependency upgrades.
tags:
    - bifrost
    - release-notes
    - changelog
    - streaming
    - telemetry
    - bedrock
category: reference
---

# v1.3.0-prerelease7

> v1.3.0-prerelease7 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.0-prerelease7
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.0-prerelease7
    docker run -p 8080:8080 maximhq/bifrost:v1.3.0-prerelease7
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
  * Added Responses streaming across all providers.
  * Fixed bedrock chat streaming decoding issues.
  * Added raw response support for all streaming requests.
  * Removed last token's accumulated latency from inter token latency metric.
</Update>

<Update label="Core" description="v1.3.0-prerelease7">
  * Feat: Responses streaming added across all providers.
  * Fix: Bedrock chat streaming decoding fixes.
  * Feat: Added raw response support for all streaming requests.
</Update>

<Update label="Framework" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6
  * Feat: Moved the migrator package to a more general location and added database migrations for the logstore to standardize object type values.
</Update>

<Update label="governance" description="v1.3.0-prerelease7">
  * Chore: using core 1.2.6 and framework 1.1.6
</Update>

<Update label="jsonparser" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
</Update>

<Update label="logging" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
</Update>

<Update label="maxim" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
</Update>

<Update label="mocker" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
</Update>

<Update label="otel" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
</Update>

<Update label="semanticcache" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
</Update>

<Update label="telemetry" description="v1.3.0-prerelease7">
  * Upgrade dependency: core to 1.2.6 and framework to 1.1.6
  * Fix: Removed last token's accumulated latency from inter token latency metric.
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt