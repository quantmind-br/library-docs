---
title: v1.3.20
url: https://docs.getbifrost.ai/changelogs/v1.3.20.md
source: llms
fetched_at: 2026-01-21T19:41:51.641741008-03:00
rendered_js: false
word_count: 43
summary: This document provides release notes and installation instructions for Bifrost version 1.3.20, including a bug fix for configuration store handling in session and plugin handlers.
tags:
    - bifrost
    - release-notes
    - changelog
    - bug-fix
    - docker
    - npx
category: reference
---

# v1.3.20

> v1.3.20 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.20
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.20
    docker run -p 8080:8080 maximhq/bifrost:v1.3.20
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.20">
  * fix: handle case when config store is nil in session and plugins handlers
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt