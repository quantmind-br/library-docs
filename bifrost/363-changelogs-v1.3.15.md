---
title: v1.3.15
url: https://docs.getbifrost.ai/changelogs/v1.3.15.md
source: llms
fetched_at: 2026-01-21T19:41:43.402082901-03:00
rendered_js: false
word_count: 179
summary: This document provides the release notes and changelog for version v1.3.15 of the Bifrost platform, detailing installation methods and module-specific updates.
tags:
    - release-notes
    - changelog
    - bifrost
    - version-update
    - docker-installation
    - backend-framework
category: reference
---

# v1.3.15

> v1.3.15 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.15
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.15
    docker run -p 8080:8080 maximhq/bifrost:v1.3.15
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
  * enhancement: provider lookup enhancements in modelcatelog
</Update>

<Update label="Core" description="v1.3.15">
  * refactor: minor until changes
</Update>

<Update label="Framework" description="v1.3.15">
  * chore: Upgrades core to 1.2.18
  * enhancement: provider lookup enhancements
</Update>

<Update label="governance" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>

<Update label="jsonparser" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>

<Update label="logging" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>

<Update label="maxim" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>

<Update label="mocker" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>

<Update label="otel" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>

<Update label="semanticcache" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>

<Update label="telemetry" description="v1.3.15">
  * chore: version update core to 1.2.18 and framework to 1.1.21
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt