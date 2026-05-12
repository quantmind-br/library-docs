---
title: v1.4.0-prerelease10
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease10.md
source: llms
fetched_at: 2026-01-21T19:42:54.882654216-03:00
rendered_js: false
word_count: 495
summary: This document provides the release notes for Bifrost version 1.4.0-prerelease10, detailing new features such as image generation support, web search tools, and various bug fixes across its core components.
tags:
    - release-notes
    - bifrost
    - changelog
    - image-generation
    - llm-gateway
    - web-search
category: other
---

# v1.4.0-prerelease10

> v1.4.0-prerelease10 changelog - 2026-01-15

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease10
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease10
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease10
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease10">
  * feat: added http handlers for image generation endpoints
  * feat: improved model validation for provider-prefixed model configurations
  * fix: added support for model lookup in Google GenAI integration by path parameter (fixes using VK provider routing for GenAI integration)
  * chore: added case-insensitive helper methods for header and query parameter lookups in HTTPRequest
  * feat: add raw request data to bifrost error responses
  * fix: add support for AdditionalProperties structures (both boolean and object types)
  * fix: improve thought signature handling in gemini for function calls
  * fix: enhance citations structure to support multiple citation types
  * fix: anthropic streaming events through integration
  * feat: adds env variable indicators on UI
  * feat: introduces new EnvVar for env backed config fields
  * fix: missing request type in error response for anthropic SDK integration
  * feat: added support for web search tools in Openai, Anthropic and Gemini
  * fix: turn JSON array tool result into JSON object for Bedrock Converse API - [@Hieu Hoang](https://github.com/hhieuu)
  * fix: remove the configuration to clear usages on update when new max limit \< current usage
</Update>

<Update label="Core" description="1.3.9">
  * feat: added image generation request and response support
  * chore: added case-insensitive helper methods for header and query parameter lookups in HTTPRequest
  * feat: added support for path parameter lookups in HTTPRequest
  * fix: missing request type in error response for anthropic SDK integration
  * feat: add raw request data to bifrost error responses
  * fix: add support for AdditionalProperties structures (both boolean and object types)
  * fix: improve thought signature handling in Gemini for function calls
  * fix: enhance citations structure to support multiple citation types
  * fix: anthropic streaming events through integration
  * feat: added support for web search tools in OpenAI, Anthropic and Gemini
  * fix: turn JSON array tool result into JSON object for Bedrock Converse API
</Update>

<Update label="Framework" description="1.2.10">
  * feat: add image generation streaming accumulation support
  * feat: Improved model matching to support provider-prefixed model names (e.g., "openai/gpt-4")
  * feat: Adds rdb backed distributed locks
</Update>

<Update label="governance" description="1.4.11">
  * feat: fixed weighted provider routing to correctly match provider-prefixed models in allowed lists
  * fix: added support for model lookup in Google GenAI integration by path parameter
  * chore: updated core to v1.3.9 and framework to v1.2.10
  * fix: remove the configuration to clear usages on update when new max limit \< current usage
</Update>

<Update label="jsonparser" description="1.4.10">
  * chore: updated core to v1.3.9 and framework to v1.2.10
</Update>

<Update label="logging" description="1.4.10">
  * chore: updated core to v1.3.9 and framework to v1.2.10
</Update>

<Update label="maxim" description="1.5.9">
  * chore: updated core to v1.3.9 and framework to v1.2.9
</Update>

<Update label="mocker" description="1.4.10">
  * chore: updated core to v1.3.9 and framework to v1.2.10
</Update>

<Update label="otel" description="1.1.10">
  * chore: updated core to v1.3.9 and framework to v1.2.10
</Update>

<Update label="semanticcache" description="1.4.10">
  * feat: added semantic caching support for image generation
  * chore: updated core to v1.3.9 and framework to v1.2.10
</Update>

<Update label="telemetry" description="1.4.11">
  * chore: updated core to v1.3.9 and framework to v1.2.10
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt