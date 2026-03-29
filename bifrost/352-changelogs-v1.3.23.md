---
title: v1.3.23
url: https://docs.getbifrost.ai/changelogs/v1.3.23.md
source: llms
fetched_at: 2026-01-21T19:41:53.551691932-03:00
rendered_js: false
word_count: 331
summary: This document outlines the release notes and changelog for version 1.3.23 of the Bifrost platform, detailing new features, breaking changes, and component updates.
tags:
    - release-notes
    - changelog
    - bifrost
    - mcp-client
    - gemini-integration
    - software-update
category: reference
---

# v1.3.23

> v1.3.23 changelog - 2025-11-10

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.23
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.23
    docker run -p 8080:8080 maximhq/bifrost:v1.3.23
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
  * feat: add headers to MCP client config and provider config
  * feat: adds support for custom path overrides for custom providers
  * feat: adds support for key less authentication for custom providers
  * feat: handles `response_schema` and `response_json_schema` parameter in gemini integration
  * refactor: better mcp client management
  * feat: option to disable content logging
  * feat: key selection and retries info sent in genai traces
  * feat: option to edit and reconnect mcp clients
</Update>

<Update label="Core" description="v1.3.23">
  * feat: add headers to MCP client config and provider config
  * feat: adds support for custom path overrides for custom providers
  * feat: adds support for key less authentication for custom providers
  * feat: handles `response_schema` and `response_json_schema` parameter in gemini integration
  * \[BREAKING] MCP client Public API now takes mcp client ids instead of names
  * refactor: better mcp client management
</Update>

<Update label="Framework" description="v1.3.23">
  * chore: version update core to 1.2.21
  * feat: add headers to MCP client config
  * refactor: mcp clients to use ids instead of names
  * feat: option to disable content logging
</Update>

<Update label="governance" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
</Update>

<Update label="jsonparser" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
</Update>

<Update label="logging" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
  * feat: option to disable content logging
</Update>

<Update label="maxim" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
</Update>

<Update label="mocker" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
</Update>

<Update label="otel" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
  * feat: key selection and retries info sent in genai traces
</Update>

<Update label="semanticcache" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
</Update>

<Update label="telemetry" description="v1.3.23">
  * chore: version update core to 1.2.21 and framework to 1.1.26
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt