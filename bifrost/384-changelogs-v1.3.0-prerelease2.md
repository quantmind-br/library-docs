---
title: v1.3.0-prerelease2
url: https://docs.getbifrost.ai/changelogs/v1.3.0-prerelease2.md
source: llms
fetched_at: 2026-01-21T19:41:27.8747263-03:00
rendered_js: false
word_count: 271
summary: This document outlines the release notes and installation instructions for Bifrost version 1.3.0-prerelease2, highlighting new features such as text completion streaming and improved error handling.
tags:
    - release-notes
    - bifrost
    - text-completion
    - streaming-support
    - error-handling
    - changelog
category: reference
---

# v1.3.0-prerelease2

> v1.3.0-prerelease2 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.0-prerelease2
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.0-prerelease2
    docker run -p 8080:8080 maximhq/bifrost:v1.3.0-prerelease2
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.0-prerelease2">
  * Added specific error handling for timeout scenarios (context.Canceled, context.DeadlineExceeded, fasthttp.ErrTimeout) across all providers
  * Created a dedicated error message for timeouts that guides users to adjust the timeout setting
  * Fixed validation in HTTP handlers for embeddings, speech, and text completion requests
  * Improved CORS wildcard pattern matching to support domain patterns like \*.example.com
  * Fixed issues in the logging plugin to properly handle text completion responses
  * Enhanced UI form handling for network configuration with proper default values
  * Feat: Adds Text Completion Streaming support
</Update>

<Update label="Core" description="v1.3.0-prerelease2">
  * Added specific error handling for timeout scenarios (context.Canceled, context.DeadlineExceeded, fasthttp.ErrTimeout) across all providers
  * Created a dedicated error message for timeouts that guides users to adjust the timeout setting
  * Added Text Completion Streaming support
</Update>

<Update label="Framework" description="v1.3.0-prerelease2">
  * Feat: Adds Text Completion Streaming support
</Update>

<Update label="governance" description="v1.3.0-prerelease2">
  * Chore: using core 1.2.1 and framework 1.1.1
</Update>

<Update label="jsonparser" description="v1.3.0-prerelease2">
  * Upgrade dependency: core to 1.2.1 and framework to 1.1.1
</Update>

<Update label="logging" description="v1.3.0-prerelease2">
  * Feat: Adds Text Completion Streaming support
  * Upgrade dependency: core to 1.2.1 and framework to 1.1.1
</Update>

<Update label="maxim" description="v1.3.0-prerelease2">
  * Upgrade dependency: core to 1.2.1 and framework to 1.1.1
</Update>

<Update label="mocker" description="v1.3.0-prerelease2">
  * Upgrade dependency: core to 1.2.1 and framework to 1.1.1
</Update>

<Update label="otel" description="v1.3.0-prerelease2">
  * Upgrade dependency: core to 1.2.1 and framework to 1.1.1
</Update>

<Update label="semanticcache" description="v1.3.0-prerelease2">
  * Feat: Adds Text Completion Streaming support
  * Upgrade dependency: core to 1.2.1 and framework to 1.1.1
</Update>

<Update label="telemetry" description="v1.3.0-prerelease2">
  * Upgrade dependency: core to 1.2.1 and framework to 1.1.1
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt