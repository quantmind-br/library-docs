---
title: Comparing LLMs on a Test Set using LiteLLM | liteLLM
url: https://docs.litellm.ai/docs/tutorials/compare_llms_2
source: sitemap
fetched_at: 2026-01-21T19:55:11.337489267-03:00
rendered_js: false
word_count: 20
summary: This document demonstrates how to use the LiteLLM library to call multiple large language models using a unified completion function format.
tags:
    - litellm
    - multi-model
    - python-sdk
    - api-standardization
    - llm-integration
category: tutorial
---

## Calling gpt-3.5-turbo and claude-2 on the same questions[​](#calling-gpt-35-turbo-and-claude-2-on-the-same-questions "Direct link to Calling gpt-3.5-turbo and claude-2 on the same questions")

## LiteLLM `completion()` allows you to call all LLMs in the same format[​](#litellm-completion-allows-you-to-call-all-llms-in-the-same-format "Direct link to litellm-completion-allows-you-to-call-all-llms-in-the-same-format")

```
results =[]# for storing results

models =['gpt-3.5-turbo','claude-2']# define what models you're testing, see: https://docs.litellm.ai/docs/providers
for question in questions:
    row =[question]
for model in models:
print("Calling:", model,"question:", question)
      response = completion(# using litellm.completion
            model=model,
            messages=[
{'role':'system','content': prompt},
{'role':'user','content': question}
]
)
      answer = response.choices[0].message['content']
      row.append(answer)
print(print("Calling:", model,"answer:", answer))

    results.append(row)# save results

```