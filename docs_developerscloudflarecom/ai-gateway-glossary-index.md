---
title: Header Glossary · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/glossary/index.md
source: llms
fetched_at: 2026-01-24T14:01:23.542335233-03:00
rendered_js: false
word_count: 425
summary: This document provides a comprehensive list of supported HTTP headers for AI Gateway, detailing how they control request retries, caching, logging, and metadata. It also explains the configuration hierarchy for applying these settings at the provider, request, and gateway levels.
tags:
    - ai-gateway
    - http-headers
    - request-configuration
    - caching
    - logging
    - error-handling
category: reference
---

AI Gateway supports a variety of headers to help you configure, customize, and manage your API requests. This page provides a complete list of all supported headers, along with a short description

| Term | Definition |
| - | - |
| cf-aig-backoff | Header to customize the backoff type for [request retries](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries) of a request. |
| cf-aig-cache-key | The [cf-aig-cache-key-aig-cache-key](https://developers.cloudflare.com/ai-gateway/features/caching/#custom-cache-key-cf-aig-cache-key) let you override the default cache key in order to precisely set the cacheability setting for any resource. |
| cf-aig-cache-status | [Status indicator for caching](https://developers.cloudflare.com/ai-gateway/features/caching/#default-configuration), showing if a request was served from cache. |
| cf-aig-cache-ttl | Specifies the [cache time-to-live for responses](https://developers.cloudflare.com/ai-gateway/features/caching/#cache-ttl-cf-aig-cache-ttl). |
| cf-aig-collect-log | The [cf-aig-collect-log](https://developers.cloudflare.com/ai-gateway/observability/logging/#collect-logs-cf-aig-collect-log) header allows you to bypass the default log setting for the gateway. |
| cf-aig-custom-cost | Allows the [customization of request cost](https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/#custom-cost) to reflect user-defined parameters. |
| cf-aig-event-id | [cf-aig-event-id](https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/#3-retrieve-the-cf-aig-log-id) is a unique identifier for an event, used to trace specific events through the system. |
| cf-aig-log-id | The [cf-aig-log-id](https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/#3-retrieve-the-cf-aig-log-id) is a unique identifier for the specific log entry to which you want to add feedback. |
| cf-aig-max-attempts | Header to customize the number of max attempts for [request retries](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries) of a request. |
| cf-aig-metadata | [Custom metadata](https://developers.cloudflare.com/ai-gateway/configuration/custom-metadata/)allows you to tag requests with user IDs or other identifiers, enabling better tracking and analysis of your requests. |
| cf-aig-request-timeout | Header to trigger a fallback provider based on a [predetermined response time](https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/#request-timeouts) (measured in milliseconds). |
| cf-aig-retry-delay | Header to customize the retry delay for [request retries](https://developers.cloudflare.com/ai-gateway/configuration/request-handling/#request-retries) of a request. |
| cf-aig-skip-cache | Header to [bypass caching for a specific request](https://developers.cloudflare.com/ai-gateway/features/caching/#skip-cache-cf-aig-skip-cache). |
| cf-aig-step | [cf-aig-step](https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/#response-headercf-aig-step) identifies the processing step in the AI Gateway flow for better tracking and debugging. |
| cf-cache-ttl | Deprecated: This header is replaced by `cf-aig-cache-ttl`. It specifies cache time-to-live. |
| cf-skip-cache | Deprecated: This header is replaced by `cf-aig-skip-cache`. It bypasses caching for a specific request. |

## Configuration hierarchy

Settings in AI Gateway can be configured at three levels: **Provider**, **Request**, and **Gateway**. Since the same settings can be configured in multiple locations, the following hierarchy determines which value is applied:

1. **Provider-level headers**: Relevant only when using the [Universal Endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/), these headers take precedence over all other configurations.
2. **Request-level headers**: Apply if no provider-level headers are set.
3. **Gateway-level settings**: Act as the default if no headers are set at the provider or request levels.

This hierarchy ensures consistent behavior, prioritizing the most specific configurations. Use provider-level and request-level headers for more fine-tuned control, and gateway settings for general defaults.