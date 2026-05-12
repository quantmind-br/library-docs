---
title: v1.3.48
url: https://docs.getbifrost.ai/changelogs/v1.3.48.md
source: llms
fetched_at: 2026-01-21T19:42:28.120535999-03:00
rendered_js: false
word_count: 40
summary: This document outlines the release notes and deployment instructions for Bifrost version 1.3.48, featuring security patches for Next.js and React.
tags:
    - release-notes
    - bifrost
    - security-patch
    - docker
    - npx
    - changelog
category: other
---

# v1.3.48

> v1.3.48 changelog - 2025-12-12

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.48
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.48
    docker run -p 8080:8080 maximhq/bifrost:v1.3.48
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.48">
  * chore: security patches 2 to next + react
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt