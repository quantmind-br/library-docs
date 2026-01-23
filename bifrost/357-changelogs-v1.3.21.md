---
title: v1.3.21
url: https://docs.getbifrost.ai/changelogs/v1.3.21.md
source: llms
fetched_at: 2026-01-21T19:41:53.402022225-03:00
rendered_js: false
word_count: 51
summary: This document details the changelog and deployment commands for Bifrost version 1.3.21, including bug fixes for session handlers and new integration tests.
tags:
    - bifrost
    - changelog
    - version-update
    - http-proxy
    - bug-fix
    - docker
    - npx
category: reference
---

# v1.3.21

> v1.3.21 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.21
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.21
    docker run -p 8080:8080 maximhq/bifrost:v1.3.21
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.21">
  * fix: handle case when config store is nil in session and plugins handlers
  * chore: adds integration tests for different config combinations
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt