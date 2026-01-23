---
title: v1.3.9
url: https://docs.getbifrost.ai/changelogs/v1.3.9.md
source: llms
fetched_at: 2026-01-21T19:42:52.077328519-03:00
rendered_js: false
word_count: 37
summary: This document provides the release notes and installation instructions for Bifrost version 1.3.9, including a fix for Azure deployment form validation.
tags:
    - bifrost
    - changelog
    - release-notes
    - azure
    - deployment
    - docker
    - npx
category: other
---

# v1.3.9

> v1.3.9 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.9
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.9
    docker run -p 8080:8080 maximhq/bifrost:v1.3.9
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.9">
  * chore: Fixes form validation for Azure deployments.
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt