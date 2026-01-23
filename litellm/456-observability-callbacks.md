---
title: Callbacks | liteLLM
url: https://docs.litellm.ai/observability/callbacks
source: sitemap
fetched_at: 2026-01-21T19:41:09.351590259-03:00
rendered_js: false
word_count: 55
summary: This document explains how to configure success and failure callbacks in liteLLM to automatically send completion data and error reports to external monitoring and logging providers.
tags:
    - litellm
    - callbacks
    - monitoring
    - logging
    - observability
    - error-tracking
category: guide
---

## Use Callbacks to send Output Data to Posthog, Sentry etc[​](#use-callbacks-to-send-output-data-to-posthog-sentry-etc "Direct link to Use Callbacks to send Output Data to Posthog, Sentry etc")

liteLLM provides `success_callbacks` and `failure_callbacks`, making it easy for you to send data to a particular provider depending on the status of your responses.

liteLLM supports:

- [Lunary](https://lunary.ai/docs)
- [Helicone](https://docs.helicone.ai/introduction)
- [Sentry](https://docs.sentry.io/platforms/python/)
- [PostHog](https://posthog.com/docs/libraries/python)
- [Slack](https://slack.dev/bolt-python/concepts)

### Quick Start[​](#quick-start "Direct link to Quick Start")

```
from litellm import completion

# set callbacks
litellm.success_callback=["posthog","helicone","lunary"]
litellm.failure_callback=["sentry","lunary"]

## set env variables
os.environ['SENTRY_DSN'], os.environ['SENTRY_API_TRACE_RATE']=""
os.environ['POSTHOG_API_KEY'], os.environ['POSTHOG_API_URL']="api-key","api-url"
os.environ["HELICONE_API_KEY"]=""

response = completion(model="gpt-3.5-turbo", messages=messages)
```

- [Use Callbacks to send Output Data to Posthog, Sentry etc](#use-callbacks-to-send-output-data-to-posthog-sentry-etc)
  
  - [Quick Start](#quick-start)