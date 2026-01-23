---
title: Predicted Outputs | liteLLM
url: https://docs.litellm.ai/docs/completion/predict_outputs
source: sitemap
fetched_at: 2026-01-21T19:44:37.638957781-03:00
rendered_js: false
word_count: 20
summary: This document demonstrates how to use the litellm library to refactor C# code using the prediction parameter for efficient model completions.
tags:
    - litellm
    - code-refactoring
    - python
    - llm-prediction
    - gpt-4o-mini
category: tutorial
---

In this example we want to refactor a piece of C# code, and convert the Username property to Email instead:

```
import litellm
os.environ["OPENAI_API_KEY"]="your-api-key"
code ="""
/// <summary>
/// Represents a user with a first name, last name, and username.
/// </summary>
public class User
{
    /// <summary>
    /// Gets or sets the user's first name.
    /// </summary>
    public string FirstName { get; set; }

    /// <summary>
    /// Gets or sets the user's last name.
    /// </summary>
    public string LastName { get; set; }

    /// <summary>
    /// Gets or sets the user's username.
    /// </summary>
    public string Username { get; set; }
}
"""

completion = litellm.completion(
    model="gpt-4o-mini",
    messages=[
{
"role":"user",
"content":"Replace the Username property with an Email property. Respond only with code, and with no markdown formatting.",
},
{"role":"user","content": code},
],
    prediction={"type":"content","content": code},
)

print(completion)
```