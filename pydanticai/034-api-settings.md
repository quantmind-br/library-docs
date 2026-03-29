---
title: pydantic_ai.settings - Pydantic AI
url: https://ai.pydantic.dev/api/settings/
source: sitemap
fetched_at: 2026-01-22T22:24:16.661890143-03:00
rendered_js: false
word_count: 509
summary: This document defines the ModelSettings TypedDict, which provides common configuration parameters such as temperature, token limits, and penalties for various LLM providers.
tags:
    - pydantic-ai
    - llm-configuration
    - model-settings
    - api-reference
    - python
category: api
---

Bases: `TypedDict`

Settings to configure an LLM.

Here we include only settings which apply to multiple models / model providers, though not all of these settings are supported by all models.

Source code in `pydantic_ai_slim/pydantic_ai/settings.py`

```
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
```

```
classModelSettings(TypedDict, total=False):
"""Settings to configure an LLM.

    Here we include only settings which apply to multiple models / model providers,
    though not all of these settings are supported by all models.
    """

    max_tokens: int
"""The maximum number of tokens to generate before stopping.

    Supported by:

    * Gemini
    * Anthropic
    * OpenAI
    * Groq
    * Cohere
    * Mistral
    * Bedrock
    * MCP Sampling
    * Outlines (all providers)
    * xAI
    """

    temperature: float
"""Amount of randomness injected into the response.

    Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to a model's
    maximum `temperature` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    Supported by:

    * Gemini
    * Anthropic
    * OpenAI
    * Groq
    * Cohere
    * Mistral
    * Bedrock
    * Outlines (Transformers, LlamaCpp, SgLang, VLLMOffline)
    * xAI
    """

    top_p: float
"""An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.

    So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    You should either alter `temperature` or `top_p`, but not both.

    Supported by:

    * Gemini
    * Anthropic
    * OpenAI
    * Groq
    * Cohere
    * Mistral
    * Bedrock
    * Outlines (Transformers, LlamaCpp, SgLang, VLLMOffline)
    * xAI
    """

    timeout: float | Timeout
"""Override the client-level default timeout for a request, in seconds.

    Supported by:

    * Gemini
    * Anthropic
    * OpenAI
    * Groq
    * Mistral
    * xAI
    """

    parallel_tool_calls: bool
"""Whether to allow parallel tool calls.

    Supported by:

    * OpenAI (some models, not o1)
    * Groq
    * Anthropic
    * xAI
    """

    seed: int
"""The random seed to use for the model, theoretically allowing for deterministic results.

    Supported by:

    * OpenAI
    * Groq
    * Cohere
    * Mistral
    * Gemini
    * Outlines (LlamaCpp, VLLMOffline)
    """

    presence_penalty: float
"""Penalize new tokens based on whether they have appeared in the text so far.

    Supported by:

    * OpenAI
    * Groq
    * Cohere
    * Gemini
    * Mistral
    * Outlines (LlamaCpp, SgLang, VLLMOffline)
    * xAI
    """

    frequency_penalty: float
"""Penalize new tokens based on their existing frequency in the text so far.

    Supported by:

    * OpenAI
    * Groq
    * Cohere
    * Gemini
    * Mistral
    * Outlines (LlamaCpp, SgLang, VLLMOffline)
    * xAI
    """

    logit_bias: dict[str, int]
"""Modify the likelihood of specified tokens appearing in the completion.

    Supported by:

    * OpenAI
    * Groq
    * Outlines (Transformers, LlamaCpp, VLLMOffline)
    """

    stop_sequences: list[str]
"""Sequences that will cause the model to stop generating.

    Supported by:

    * OpenAI
    * Anthropic
    * Bedrock
    * Mistral
    * Groq
    * Cohere
    * Google
    * xAI
    """

    extra_headers: dict[str, str]
"""Extra headers to send to the model.

    Supported by:

    * OpenAI
    * Anthropic
    * Groq
    * xAI
    """

    extra_body: object
"""Extra body to send to the model.

    Supported by:

    * OpenAI
    * Anthropic
    * Groq
    * Outlines (all providers)
    """
```

#### max\_tokens `instance-attribute`

The maximum number of tokens to generate before stopping.

Supported by:

- Gemini
- Anthropic
- OpenAI
- Groq
- Cohere
- Mistral
- Bedrock
- MCP Sampling
- Outlines (all providers)
- xAI

#### temperature `instance-attribute`

Amount of randomness injected into the response.

Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to a model's maximum `temperature` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

Supported by:

- Gemini
- Anthropic
- OpenAI
- Groq
- Cohere
- Mistral
- Bedrock
- Outlines (Transformers, LlamaCpp, SgLang, VLLMOffline)
- xAI

#### top\_p `instance-attribute`

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass.

So 0.1 means only the tokens comprising the top 10% probability mass are considered.

You should either alter `temperature` or `top_p`, but not both.

Supported by:

- Gemini
- Anthropic
- OpenAI
- Groq
- Cohere
- Mistral
- Bedrock
- Outlines (Transformers, LlamaCpp, SgLang, VLLMOffline)
- xAI

#### timeout `instance-attribute`

Override the client-level default timeout for a request, in seconds.

Supported by:

- Gemini
- Anthropic
- OpenAI
- Groq
- Mistral
- xAI

#### parallel\_tool\_calls `instance-attribute`

```
parallel_tool_calls: bool
```

Whether to allow parallel tool calls.

Supported by:

- OpenAI (some models, not o1)
- Groq
- Anthropic
- xAI

#### seed `instance-attribute`

The random seed to use for the model, theoretically allowing for deterministic results.

Supported by:

- OpenAI
- Groq
- Cohere
- Mistral
- Gemini
- Outlines (LlamaCpp, VLLMOffline)

#### presence\_penalty `instance-attribute`

Penalize new tokens based on whether they have appeared in the text so far.

Supported by:

- OpenAI
- Groq
- Cohere
- Gemini
- Mistral
- Outlines (LlamaCpp, SgLang, VLLMOffline)
- xAI

#### frequency\_penalty `instance-attribute`

Penalize new tokens based on their existing frequency in the text so far.

Supported by:

- OpenAI
- Groq
- Cohere
- Gemini
- Mistral
- Outlines (LlamaCpp, SgLang, VLLMOffline)
- xAI

#### logit\_bias `instance-attribute`

Modify the likelihood of specified tokens appearing in the completion.

Supported by:

- OpenAI
- Groq
- Outlines (Transformers, LlamaCpp, VLLMOffline)

#### stop\_sequences `instance-attribute`

Sequences that will cause the model to stop generating.

Supported by:

- OpenAI
- Anthropic
- Bedrock
- Mistral
- Groq
- Cohere
- Google
- xAI

Extra headers to send to the model.

Supported by:

- OpenAI
- Anthropic
- Groq
- xAI

#### extra\_body `instance-attribute`

Extra body to send to the model.

Supported by:

- OpenAI
- Anthropic
- Groq
- Outlines (all providers)