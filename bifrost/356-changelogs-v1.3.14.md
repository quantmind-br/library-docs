---
title: v1.3.14
url: https://docs.getbifrost.ai/changelogs/v1.3.14.md
source: llms
fetched_at: 2026-01-21T19:41:42.335806237-03:00
rendered_js: false
word_count: 290
summary: This document provides the release notes for Bifrost version 1.3.14, detailing new features such as dynamic plugins and authentication support alongside various performance improvements and bug fixes.
tags:
    - release-notes
    - changelog
    - bifrost
    - software-update
    - authentication
    - dynamic-plugins
    - deployment
category: reference
---

# v1.3.14

> v1.3.14 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.14
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.14
    docker run -p 8080:8080 maximhq/bifrost:v1.3.14
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.14">
  * chore: version update framework to 1.1.18 and core to 1.2.16
  * feat: Use all keys for list models request
  * fix: handled panic when using gemini models with openai integration responses API requests
  * chore: Added id, object, and model fields to Chat Completion responses from Bedrock and Cohere providers
  * feat: Adds support for dynamic plugins. Note that dynamic plugins are in beta
  * feat: Adds auth support for dashboard, inference APIs and dashboard APIs.
</Update>

<Update label="Core" description="v1.3.14">
  * feat: Use all keys for list models request
  * refactor: Cohere provider to use completeRequest and response pooling for all requests
  * chore: Added id, object, and model fields to Chat Completion responses from Bedrock and Cohere providers
  * feat: Moved all streaming calls to use fasthttp client for efficiency
  * feat: Adds support for auth
</Update>

<Update label="Framework" description="v1.3.14">
  * chore: Upgrades core to 1.2.17
  * feat: Adds dynamic plugins support
  * feat: Adds auth tables in config store
</Update>

<Update label="governance" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>

<Update label="jsonparser" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>

<Update label="logging" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>

<Update label="maxim" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>

<Update label="mocker" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>

<Update label="otel" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>

<Update label="semanticcache" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>

<Update label="telemetry" description="v1.3.14">
  * chore: version update core to 1.2.17 and framework to 1.1.19
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt