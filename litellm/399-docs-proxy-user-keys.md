---
title: Langchain, OpenAI SDK, LlamaIndex, Instructor, Curl examples | liteLLM
url: https://docs.litellm.ai/docs/proxy/user_keys
source: sitemap
fetched_at: 2026-01-21T19:54:00.236871294-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to use the OpenAI Python client to send a single chat completion request to multiple models simultaneously through a proxy server.
tags:
    - openai-sdk
    - chat-completions
    - multi-model
    - python-client
    - proxy-server
    - llm-routing
category: tutorial
---

```
import openai

client = openai.OpenAI(api_key="sk-1234", base_url="http://0.0.0.0:4000")

response = client.chat.completions.create(
    model="gpt-3.5-turbo,llama3",
    messages=[
{"role":"user","content":"this is a test request, write a short poem"}
],
)

print(response)
```

```
[
    ChatCompletion(
id='chatcmpl-9NoYhS2G0fswot0b6QpoQgmRQMaIf',
        choices=[
            Choice(
                finish_reason='stop',
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content='In the depths of my soul, a spark ignites\nA light that shines so pure and bright\nIt dances and leaps, refusing to die\nA flame of hope that reaches the sky\n\nIt warms my heart and fills me with bliss\nA reminder that in darkness, there is light to kiss\nSo I hold onto this fire, this guiding light\nAnd let it lead me through the darkest night.',
                    role='assistant',
                    function_call=None,
                    tool_calls=None
)
)
],
        created=1715462919,
        model='gpt-3.5-turbo-0125',
object='chat.completion',
        system_fingerprint=None,
        usage=CompletionUsage(
            completion_tokens=83,
            prompt_tokens=17,
            total_tokens=100
)
),
    ChatCompletion(
id='chatcmpl-4ac3e982-da4e-486d-bddb-ed1d5cb9c03c',
        choices=[
            Choice(
                finish_reason='stop',
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content="A test request, and I'm delighted!\nHere's a short poem, just for you:\n\nMoonbeams dance upon the sea,\nA path of light, for you to see.\nThe stars up high, a twinkling show,\nA night of wonder, for all to know.\n\nThe world is quiet, save the night,\nA peaceful hush, a gentle light.\nThe world is full, of beauty rare,\nA treasure trove, beyond compare.\n\nI hope you enjoyed this little test,\nA poem born, of whimsy and jest.\nLet me know, if there's anything else!",
                    role='assistant',
                    function_call=None,
                    tool_calls=None
)
)
],
        created=1715462919,
        model='groq/llama3-8b-8192',
object='chat.completion',
        system_fingerprint='fp_a2c8d063cb',
        usage=CompletionUsage(
            completion_tokens=120,
            prompt_tokens=20,
            total_tokens=140
)
)
]
```