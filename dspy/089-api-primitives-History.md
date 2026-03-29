---
title: History - DSPy
url: https://dspy.ai/api/primitives/History/
source: sitemap
fetched_at: 2026-01-23T08:02:37.169129087-03:00
rendered_js: false
word_count: 69
summary: This document describes the dspy.History class, which is used to represent and manage conversation history within dspy signatures and predictive models.
tags:
    - dspy
    - conversation-history
    - signature-fields
    - prompt-engineering
    - language-models
category: reference
---

Bases: `BaseModel`

Class representing the conversation history.

The conversation history is a list of messages, each message entity should have keys from the associated signature. For example, if you have the following signature:

```
class MySignature(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()
```

Then the history should be a list of dictionaries with keys "question" and "answer".

Example

```
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class MySignature(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

history = dspy.History(
    messages=[
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the capital of Germany?", "answer": "Berlin"},
    ]
)

predict = dspy.Predict(MySignature)
outputs = predict(question="What is the capital of France?", history=history)
```

Example of capturing the conversation history

```
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class MySignature(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

predict = dspy.Predict(MySignature)
outputs = predict(question="What is the capital of France?")
history = dspy.History(messages=[{"question": "What is the capital of France?", **outputs}])
outputs_with_history = predict(question="Are you sure?", history=history)
```

### Attributes[¶](#dspy.History-attributes "Permanent link")

#### `messages: list[dict[str, Any]]` `instance-attribute` [¶](#dspy.History.messages "Permanent link")

#### `model_config = pydantic.ConfigDict(frozen=True, str_strip_whitespace=True, validate_assignment=True, extra='forbid')` `class-attribute` `instance-attribute` [¶](#dspy.History.model_config "Permanent link")