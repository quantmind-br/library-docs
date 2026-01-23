---
title: Langsmith - Logging LLM Input/Output | liteLLM
url: https://docs.litellm.ai/docs/observability/langsmith_integration
source: sitemap
fetched_at: 2026-01-21T19:46:13.776406726-03:00
rendered_js: false
word_count: 61
summary: This document explains how to integrate LiteLLM with LangSmith for automated logging and tracing of LLM responses across different providers.
tags:
    - litellm
    - langsmith
    - logging
    - observability
    - callbacks
    - llm-monitoring
category: tutorial
---

Use just 2 lines of code, to instantly log your responses **across all providers** with Langsmith

Set `langsmith_batch_size=1` when testing locally, to see logs land quickly.

```
import litellm
import os

os.environ["LANGSMITH_API_KEY"]=""
# LLM API Keys
os.environ['OPENAI_API_KEY']=""

# set langsmith as a callback, litellm will send the data to langsmith
litellm.success_callback =["langsmith"]

response = litellm.completion(
    model="gpt-3.5-turbo",
     messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
],
    metadata={
"run_name":"litellmRUN",# langsmith run name
"project_name":"litellm-completion",# langsmith project name
"run_id":"497f6eca-6276-4993-bfeb-53cbbbba6f08",# langsmith run id
"parent_run_id":"f8faf8c1-9778-49a4-9004-628cdb0047e5",# langsmith run parent run id
"trace_id":"df570c03-5a03-4cea-8df0-c162d05127ac",# langsmith run trace id
"session_id":"1ffd059c-17ea-40a8-8aef-70fd0307db82",# langsmith run session id
"tags":["model1","prod-2"],# langsmith run tags
"metadata":{# langsmith run metadata
"key1":"value1"
},
"dotted_order":"20240429T004912090000Z497f6eca-6276-4993-bfeb-53cbbbba6f08"
}
)
print(response)
```

If you're using a custom LangSmith instance, you can set the `LANGSMITH_BASE_URL` environment variable to point to your instance. For example, you can make LiteLLM Proxy log to a local LangSmith instance with this config: