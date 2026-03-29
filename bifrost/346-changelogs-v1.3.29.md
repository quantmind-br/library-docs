---
title: v1.3.29
url: https://docs.getbifrost.ai/changelogs/v1.3.29.md
source: llms
fetched_at: 2026-01-21T19:42:02.064131779-03:00
rendered_js: false
word_count: 282
summary: This document provides the release notes and changelog for version 1.3.29 of the Bifrost platform, detailing bug fixes and new features across various core components and plugins.
tags:
    - changelog
    - release-notes
    - bifrost
    - metrics
    - opentelemetry
    - bug-fixes
category: reference
---

# v1.3.29

> v1.3.29 changelog - 2025-11-18

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.29
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.29
    docker run -p 8080:8080 maximhq/bifrost:v1.3.29
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.29">
  * fix: properly set bifrost version in metrics
  * feat: added team\_id, team\_name, customer\_id and customer\_name labels to otel metrics
  * fix: skip adding google/ prefix for custom fine-tuned models in vertex provider (for genai integration)
  * fix: deep copy inputs in semantic cache plugin to not mutate the original request
</Update>

<Update label="Core" description="1.2.26">
  * fix: skip adding google/ prefix for custom fine-tuned models in vertex provider
  * feat: added DeepCopy functions to schemas package
</Update>

<Update label="Framework" description="1.1.32">
  chore: update core version to 1.2.26
</Update>

<Update label="governance" description="1.3.33">
  chore: update core version to 1.2.26 and framework version to 1.1.32
</Update>

<Update label="jsonparser" description="1.3.33">
  chore: update core version to 1.2.26 and framework version to 1.1.32
</Update>

<Update label="logging" description="1.3.33">
  chore: update core version to 1.2.26 and framework version to 1.1.32
</Update>

<Update label="maxim" description="1.4.32">
  chore: update core version to 1.2.26 and framework version to 1.1.32
</Update>

<Update label="mocker" description="1.3.32">
  chore: update core version to 1.2.26 and framework version to 1.1.32
</Update>

<Update label="otel" description="1.0.32">
  * chore: update core version to 1.2.26 and framework version to 1.1.32
  * fix: properly set bifrost version in metrics
  * feat: added team\_id, team\_name, customer\_id and customer\_name labels to otel metrics
</Update>

<Update label="semanticcache" description="1.3.32">
  * chore: update core version to 1.2.26 and framework version to 1.1.32
  * fix: deep copy inputs to not mutate the original request
</Update>

<Update label="telemetry" description="1.3.32">
  * chore: update core version to 1.2.26 and framework version to 1.1.32
  * feat: added filter for custom labels that are already default labels
  * feat: added team\_id, team\_name, customer\_id and customer\_name labels to telemetry metrics
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt