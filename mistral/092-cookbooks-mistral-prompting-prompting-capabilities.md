---
title: Prompting Capabilities with Mistral AI - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-prompting-prompting_capabilities
source: crawler
fetched_at: 2026-01-29T07:34:00.289064853-03:00
rendered_js: false
word_count: 748
summary: A comprehensive guide from the Mistral AI Cookbook detailing various prompting techniques and capabilities for Mistral AI models.
tags:
    - Mistral AI
    - Prompt Engineering
    - LLM
    - Tutorial
category: guide
---

When you first start using Mistral models, your first interaction will revolve around prompts. The art of crafting effective prompts is essential for generating desirable responses from Mistral models or other LLMs. This guide will walk you through example prompts showing four different prompting capabilities.

- Classification
- Summarization
- Personalization
- Evaluation

## Classification

Mistral models can easily categorize text into distinct classes. In this example prompt, we can define a list of predefined categories and ask Mistral models to classify user inquiry.

### Strategies we used:

- **Few shot learning**: Few-shot learning or in-context learning is when we give a few examples in the prompts, and the LLM can generate corresponding output based on the example demonstrations. Few-shot learning can often improve model performance especially when the task is difficult or when we want the model to respond in a specific manner.
- **Delimiter**: Delimiters like ### &lt;&lt;&lt; &gt;&gt;&gt; specify the boundary between different sections of the text. In our example, we used ### to indicate examples and &lt;&lt;&lt;&gt;&gt;&gt; to indicate customer inquiry.
- **Role playing**: Providing LLM a role (e.g., "You are a bank customer service bot.") adds personal context to the model and often leads to better performance.

## Summarization

Summarization is a common task for LLMs due to their natural language understanding and generation capabilities. Here is an example prompt we can use to generate interesting questions about an essay and summarize the essay.

## Strategies we used:

- **Step-by-step instructions**: This strategy is inspired by the chain-of-thought prompting that enables LLMs to use a series of intermediate reasoning steps to tackle complex tasks. It's often easier to solve complex problems when we decompose them into simpler and small steps and it's easier for us to debug and inspect the model behavior. In our example, we break down the task into three steps: summarize, generate interesting questions, and write a report. This helps the language to think in each step and generate a more comprehensive final report.
- **Example generation**: We can ask LLMs to automatically guide the reasoning and understanding process by generating examples with the explanations and steps. In this example, we ask the LLM to generate three questions and provide detailed explanations for each question.
- **Output formatting**: We can ask LLMs to output in a certain format by directly asking "write a report in the Markdown format".

## Personlization

LLMs excel at personalization tasks as they can deliver content that aligns closely with individual users. In this example, we create personalized email responses to address customer questions.

### Strategies we used:

- Providing facts: Incorporating facts into prompts can be useful for developing customer support bots. It’s important to use clear and concise language when presenting these facts. This can help the LLM to provide accurate and quick responses to customer queries.

## Evaluation

There are many ways to evaluate LLM outputs. Here are three approaches for your reference: include a confidence score, introduce an evaluation step, or employ another LLM for evaluation.

## Include a confidence score

We can include a confidence score along with the generated output in the prompt.

### Strategies we used:

- JSON output: For facilitating downstream tasks, JSON format output is frequently preferred. We can enable the JSON mode by setting the response\_format to `{"type": "json_object"}` and specify in the prompt that “You will only respond with a JSON object with the key Summary and Confidence.” Specifying these keys within the JSON object is beneficial for clarity and consistency.
- Higher Temperature: In this example, we increase the temperature score to encourage the model to be more creative and output three generated summaries that are different from each other.

## Introduce an evaluation step

We can also add a second step in the prompt for evaluation.

## Employ another LLM for evaluation

In production systems, it is common to employ another LLM for evaluation so that the evaluation step can be separate from the generation step.

- Step 1: use the first LLM to generate three summaries

<!--THE END-->

- Step 2: use another LLM to rate the generated summaries

### Strategies we used:

- **LLM chaining**: In this example, we chain two LLMs in a sequence, where the output from the first LLM serves as the input for the second LLM. The method of chaining LLMs can be adapted to suit your specific use cases. For instance, you might choose to employ three LLMs in a chain, where the output of two LLMs is funneled into the third LLM. While LLM chaining offers flexibility, it's important to consider that it may result in additional API calls and potentially increased costs.