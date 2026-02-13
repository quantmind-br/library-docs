---
title: OpenAI SDK
url: https://openrouter.ai/docs/guides/community/openai-sdk.mdx
source: llms
fetched_at: 2026-02-13T15:15:48.140986-03:00
rendered_js: false
word_count: 88
summary: This document provides instructions and code examples for integrating OpenRouter using the official OpenAI SDK in both Python and TypeScript.
tags:
    - openrouter
    - openai-sdk
    - python
    - typescript
    - integration
    - api-client
category: guide
---

***

title: OpenAI SDK
subtitle: Using OpenRouter with OpenAI SDK
headline: OpenAI SDK Integration | OpenRouter SDK Support
canonical-url: '[https://openrouter.ai/docs/guides/community/openai-sdk](https://openrouter.ai/docs/guides/community/openai-sdk)'
'og:site\_name': OpenRouter Documentation
'og:title': OpenAI SDK Integration - OpenRouter SDK Support
'og:description': >-
Integrate OpenRouter using the official OpenAI SDK. Complete guide for OpenAI
SDK integration with OpenRouter for Python and TypeScript.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=OpenAI%20SDK\&description=OpenAI%20SDK%20Integration](https://openrouter.ai/dynamic-og?title=OpenAI%20SDK\&description=OpenAI%20SDK%20Integration)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

## Using the OpenAI SDK

* Using `pip install openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples-python/blob/main/src/openai_test.py).
* Using `npm i openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples/tree/main/typescript).
  <Tip>
    You can also use
    [Grit](https://app.grit.io/studio?key=RKC0n7ikOiTGTNVkI8uRS) to
    automatically migrate your code. Simply run `npx @getgrit/launcher
      openrouter`.
  </Tip>

<CodeGroup>
  ```typescript title="TypeScript"
  import OpenAI from "openai"

  const openai = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: "${API_KEY_REF}",
    defaultHeaders: {
      ${getHeaderLines().join('\n        ')}
    },
  })

  async function main() {
    const completion = await openai.chat.completions.create({
      model: "${Model.GPT_4_Omni}",
      messages: [
        { role: "user", content: "Say this is a test" }
      ],
    })

    console.log(completion.choices[0].message)
  }
  main();
  ```

  ```python title="Python"
  from openai import OpenAI
  from os import getenv

  # gets API Key from environment variable OPENAI_API_KEY
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENROUTER_API_KEY"),
  )

  completion = client.chat.completions.create(
    model="${Model.GPT_4_Omni}",
    extra_headers={
      "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
      "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    # pass extra_body to access OpenRouter-only arguments.
    # extra_body={
      # "models": [
      #   "${Model.GPT_4_Omni}",
      #   "${Model.Mixtral_8x_22B_Instruct}"
      # ]
    # },
    messages=[
      {
        "role": "user",
        "content": "Say this is a test",
      },
    ],
  )
  print(completion.choices[0].message.content)
  ```
</CodeGroup>