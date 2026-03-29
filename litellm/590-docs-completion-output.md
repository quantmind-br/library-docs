---
title: Output | liteLLM
url: https://docs.litellm.ai/docs/completion/output
source: sitemap
fetched_at: 2026-01-21T19:44:36.009725467-03:00
rendered_js: false
word_count: 43
summary: This document defines the standardized JSON response structure and data types for LiteLLM completion calls across different models. It outlines available fields such as message content, token usage, and latency, while noting compatibility with dictionary and class-based access.
tags:
    - litellm
    - api-response
    - json-schema
    - llm-integration
    - completion-endpoint
    - metadata
category: reference
---

Here's the exact json output and type you can expect from all litellm `completion` calls for all models

```
{
'choices':[
{
'finish_reason':str,# String: 'stop'
'index':int,# Integer: 0
'message':{# Dictionary [str, str]
'role':str,# String: 'assistant'
'content':str# String: "default message"
}
}
],
'created':str,# String: None
'model':str,# String: None
'usage':{# Dictionary [str, int]
'prompt_tokens':int,# Integer
'completion_tokens':int,# Integer
'total_tokens':int# Integer
}
}

```

You can access the response as a dictionary or as a class object, just as OpenAI allows you

```
{
'choices':[
{
'finish_reason':'stop',
'index':0,
'message':{
'role':'assistant',
'content':" I'm doing well, thank you for asking. I am Claude, an AI assistant created by Anthropic."
}
}
],
'created':1691429984.3852863,
'model':'claude-instant-1',
'usage':{'prompt_tokens':18,'completion_tokens':23,'total_tokens':41}
}
```

You can also access information like latency.