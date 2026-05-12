---
title: v1.4.0-prerelease5
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease5.md
source: llms
fetched_at: 2026-01-21T19:42:58.448329731-03:00
rendered_js: false
word_count: 47
summary: This document provides the release notes for Bifrost version 1.4.0-prerelease5, detailing bug fixes for LLM integration and UI stability.
tags:
    - release-notes
    - bifrost
    - changelog
    - bug-fixes
    - installation
category: reference
---

# v1.4.0-prerelease5

> v1.4.0-prerelease5 changelog - 2026-01-05

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease5
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease5
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease5
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease5">
  fix: non-streaming integration LLM calls requiring virtual keys
  fix: UI crash when disabling new plugin
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt