---
title: Guides Predicted Outputs
url: https://docs.fireworks.ai/guides/predicted-outputs
source: sitemap
fetched_at: 2026-04-27T20:18:28.022080938-03:00
rendered_js: false
word_count: 128
summary: This document explains the concept of Predicted Outputs for improving LLM generation speeds when large parts of the expected output are known beforehand, detailing how to implement it using the Fireworks API.
tags:
    - predicted-outputs
    - llm-generation
    - fireworks-api
    - speed-optimization
    - prompting-techniques
    - api-feature
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Predicted Outputs improves LLM generation speed when large parts of the expected output are known in advance (e.g., editing or rewriting documents or code). Provide strong "guesses" of what the output may look like via the `prediction` field.

## Usage

Set the `prediction` field in the Fireworks API with the predicted output. Example: editing a survey to add a "Text Message" option:

```python
from fireworks.client import Fireworks

code = """{
"questions": [
    {"question": "Name", "type": "text"},
    {"question": "Age", "type": "number"},
    {"question": "Feedback", "type": "text_area"},
    {"question": "How to Contact", "type": "multiple_choice", "options": ["Email", "Phone"], "optional": true}
  ]
}"""

client = Fireworks(api_key="<FIREWORKS_API_KEY>")

response = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-70b-instruct",
    messages=[
        {"role": "user", "content": "Edit the How to Contact question to add an option called Text Message. Output the full edited code, with no markdown or explanations."},
        {"role": "user", "content": code}
    ],
    temperature=0,
    prediction={"type": "content", "content": code}
)

print(response.choices[0].message.content)
```

## Notes

- **Cost**: Using Predicted Outputs is free
- **Temperature**: Set `temperature=0` for best results in most use cases; quality is not impacted
- **Max length**: Limited by `max_tokens` (default 2048); increase if your prediction is longer
- **Performance**: If the prediction diverges significantly from the actual output, generation speed may decrease
- **On-demand deployments**: Set `rewrite_speculation=True` for potentially faster output generation

#predicted-outputs #speed-optimization #llm-generation
