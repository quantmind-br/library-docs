---
title: v1.3.40
url: https://docs.getbifrost.ai/changelogs/v1.3.40.md
source: llms
fetched_at: 2026-01-21T19:42:16.715840693-03:00
rendered_js: false
word_count: 39
summary: This document outlines the release notes and update instructions for Bifrost version 1.3.40, featuring critical security patches for React and Next.js.
tags:
    - release-notes
    - bifrost
    - security-update
    - docker
    - npx
    - v1-3-40
category: reference
---

# v1.3.40

> v1.3.40 changelog - 2025-12-04

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.40
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.40
    docker run -p 8080:8080 maximhq/bifrost:v1.3.40
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.40">
  * security: upgrades React and Next against [CVE-2025-66478](https://nextjs.org/blog/CVE-2025-66478)
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt