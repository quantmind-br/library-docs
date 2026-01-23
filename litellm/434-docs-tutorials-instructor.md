---
title: Instructor | liteLLM
url: https://docs.litellm.ai/docs/tutorials/instructor
source: sitemap
fetched_at: 2026-01-21T19:55:30.83929352-03:00
rendered_js: false
word_count: 38
summary: This document explains how to integrate LiteLLM with the instructor library to generate validated structured outputs using Pydantic models with support for retries.
tags:
    - litellm
    - instructor-library
    - pydantic
    - structured-outputs
    - python
    - validation
    - error-handling
category: tutorial
---

Combine LiteLLM with [jxnl's instructor library](https://github.com/jxnl/instructor) for more robust structured outputs. Outputs are automatically validated into Pydantic types and validation errors are provided back to the model to increase the chance of a successful response in the retries.

```
import instructor
from litellm import completion
from pydantic import BaseModel


client = instructor.from_litellm(completion)


classUser(BaseModel):
    name:str
    age:int


defextract_user(text:str):
return client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=User,
        messages=[
{"role":"user","content": text},
],
        max_retries=3,
)

user = extract_user("Jason is 25 years old")

assertisinstance(user, User)
assert user.name =="Jason"
assert user.age ==25
print(f"{user=}")
```

```
import asyncio

import instructor
from litellm import acompletion
from pydantic import BaseModel


client = instructor.from_litellm(acompletion)


classUser(BaseModel):
    name:str
    age:int


asyncdefextract(text:str)-> User:
returnawait client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=User,
        messages=[
{"role":"user","content": text},
],
        max_retries=3,
)

user = asyncio.run(extract("Alice is 30 years old"))

assertisinstance(user, User)
assert user.name =="Alice"
assert user.age ==30
print(f"{user=}")
```