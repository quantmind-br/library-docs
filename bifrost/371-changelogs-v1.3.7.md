---
title: v1.3.7
url: https://docs.getbifrost.ai/changelogs/v1.3.7.md
source: llms
fetched_at: 2026-01-21T19:42:48.780428186-03:00
rendered_js: false
word_count: 158
summary: This document provides the release notes and changelog for Bifrost version 1.3.7, detailing installation instructions and bug fixes across various system modules.
tags:
    - release-notes
    - changelog
    - version-update
    - bug-fixes
    - bifrost-deployment
category: reference
---

# v1.3.7

> v1.3.7 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.7
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.7
    docker run -p 8080:8080 maximhq/bifrost:v1.3.7
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.7">
  * chore: version update framework to 1.1.13
  * bug: fixed config store init issue when using postgres
  * fix: allow http on pricing data url
</Update>

<Update label="Core" description="v1.3.7">
  * fix: responses tool message output struct overlapping fields fixed
</Update>

<Update label="Framework" description="v1.3.7">
  * bug: fixed config store init issue when using postgres
</Update>

<Update label="governance" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>

<Update label="jsonparser" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>

<Update label="logging" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>

<Update label="maxim" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>

<Update label="mocker" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>

<Update label="otel" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>

<Update label="semanticcache" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>

<Update label="telemetry" description="v1.3.7">
  * chore: version update framework to 1.1.13
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt