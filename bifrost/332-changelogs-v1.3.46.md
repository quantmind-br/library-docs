---
title: v1.3.46
url: https://docs.getbifrost.ai/changelogs/v1.3.46.md
source: llms
fetched_at: 2026-01-21T19:42:25.171301606-03:00
rendered_js: false
word_count: 39
summary: This document provides the release notes and update instructions for Bifrost version 1.3.46, which includes critical security hotfixes for React and Next.js.
tags:
    - changelog
    - release-notes
    - security-patch
    - hotfix
    - bifrost
    - version-update
category: reference
---

# v1.3.46

> v1.3.46 changelog - 2025-12-12

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.46
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.46
    docker run -p 8080:8080 maximhq/bifrost:v1.3.46
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.46">
  * hotfix: security patches for [react](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components) and [nextjs](https://nextjs.org/blog/security-update-2025-12-11)
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt