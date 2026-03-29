---
title: v1.3.41
url: https://docs.getbifrost.ai/changelogs/v1.3.41.md
source: llms
fetched_at: 2026-01-21T19:42:17.791988311-03:00
rendered_js: false
word_count: 75
summary: This document provides the release notes for version 1.3.41, detailing a critical fix for Docker segmentation faults and refactored tag management for the Maxim plugin.
tags:
    - release-notes
    - bifrost
    - docker-fix
    - plugin-update
    - version-history
    - bug-fix
category: other
---

# v1.3.41

> v1.3.41 changelog - 2025-12-05

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.41
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.41
    docker run -p 8080:8080 maximhq/bifrost:v1.3.41
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.41">
  * fix: remove UPX binary compression from Docker build to resolve segmentation faults when combined with PIE (Position Independent Executable)
</Update>

<Update label="maxim" description="1.4.43">
  chore: Refactored the Maxim plugin to move tag handling from pre-hook to post-hook, improving the tag management process for generations.
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt