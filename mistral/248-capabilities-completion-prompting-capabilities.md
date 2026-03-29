---
title: Prompting | Mistral Docs
url: https://docs.mistral.ai/capabilities/completion/prompting_capabilities
source: crawler
fetched_at: 2026-01-29T07:33:34.900241638-03:00
rendered_js: false
word_count: 897
---

When you first start using Mistral models, your initial interaction will revolve around **prompts**. Mastering the art of crafting effective prompts is essential for generating high-quality responses from Mistral models or other LLMs.

## Main Concepts

### The Art of Crafting Prompts

Below, we cover the core concepts of prompting and how to craft effective prompts to maximize the capabilities of our models.

When providing instructions, there are two levels of input you can give the model: `system` and `user`.

- The **`system` prompt** is provided at the beginning of the conversation. It sets the general context and instructions for the model’s behavior and is typically managed by the developer.
- The **`user` prompt** is provided during the conversation to give the model specific context or instructions for the current interaction.

As a developer, you can still use `user` prompts to provide additional context or instructions during the conversation if needed. If you cannot control the `system` prompt, you can still include the general context and instructions in the `user` prompt by concatenating them with the actual query. **Role-Separated Example:**

**Concatenated Example:**

Also called Roleplaying, it's the first step in crafting a prompt and corresponds to defining a **clear purpose**. A common approach is to start with a concise role and task definition, such as: *"You are a &lt;role&gt;, your task is to &lt;task&gt;."* This simple yet powerful technique helps steer the model toward a specific vertical and task, ensuring it quickly understands the context and expected output. When giving instructions, **organize them hierarchically or with a clear structure**, such as dividing them into clear sections and subsections. **The prompt should be clear and complete.** A useful rule of thumb is to **imagine you’re writing for someone with no prior context**—they should be able to understand and execute the task solely by reading the prompt. Example of a Well-Structured Prompt: Formatting is critical for crafting effective prompts. It allows you to **explicitly highlight** different sections, making the structure intuitive for both the model and developers. **Markdown** and/or **XML-style tags** are ideal because they are:

- **Readable**: Easy for humans to scan.
- **Parsable**: Simple to extract information programmatically.
- **Familiar**: Likely seen massively during the model’s training. Good formatting not only helps the model understand the prompt but also makes it **easier for developers to iterate and maintain** the application.

Example prompting is a technique where you provide a **few task examples** to improve the model’s understanding, accuracy and specially the **output format**. A specific example of this is **few-shot prompting**, where artificial interactions between the user and model are included in the conversation history. In contrast, **zero-shot prompting** involves no examples. Direct Example in a Prompt:

Standard Few-Shot Prompting Structure:

With your prompt ready, you can now focus on the output. To ensure the model generates structured and predictable responses, we provide the ability of enforcing a specific JSON output format. This is particularly useful for tasks requiring a **consistent structure** that can be easily parsed and processed programmatically. If used in the example above, this technique would ensure that the model’s responses are consistent in terms of formating and also allows to enforce the categories to be used. If you are interested, for more details on how to use structured outputs, you can refer to the [Structured Outputs](https://docs.mistral.ai/capabilities/completion/structured_output) docs. When building a prompt, it is important to stay flexible and experiment, different models from different labs, and even a simple update, can change the model behaviour and a consistent prompt may be impacted by these changes. Hence, do not hesitate to revisit your prompts and see the impact, similar to how you would iterate on your code and model training, you should iterate on your prompts and evaluate the impact of your changes.

### What you should Avoid

Below we provide a list of "good to know" advice about what to avoid doing. The list is not exhaustive and can depend on your use case - but these points are good to keep in mind while building your prompts.

- Avoid blurry quantitative adjectives: “too long”, “too short”, “many”, “few”, etc.
  
  - Instead, provide objective measures.
- Avoid blurry words like “things”, “stuff”, “write an *interesting* report”, “make it *better*”, etc.
  
  - Instead, state exactly what you mean by “interesting”, “better”, etc.

As your system prompt gets long, slight contradictions may appear.  
Example:

- “If the new data is related to an existing database record, update this record.”
- “If the data is new, create a new record.”
- This is unclear because new data could either update an existing record or create a new one.

Instead, use a decision tree:

- Avoid: “If the record is too long, split it into multiple records.”
- Avoid: “If the record is longer than 100 characters, split it into multiple records.”
- Instead, provide character counts as input:

Models are faster at ingesting tokens than generating them. If using structured outputs, only ask the model to generate what is strictly necessary.  
Bad Examples:

- Generating full record content for a `NO_OP` operation.
- Generating an entire book in one shot.

Only generate the update or necessary data.

If you need a model to rate something, use a worded scale for better performance.  
**Avoid:**

**Use:**

You can convert this worded scale to a numeric one if needed.

Below we walk you through example prompts showing four different prompting capabilities:

- Classification
- Summarization
- Personalization
- Evaluation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/prompting/prompting_capabilities.ipynb)

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.