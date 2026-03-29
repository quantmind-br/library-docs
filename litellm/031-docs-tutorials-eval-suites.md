---
title: Evaluate LLMs - MLflow Evals, Auto Eval | liteLLM
url: https://docs.litellm.ai/docs/tutorials/eval_suites
source: sitemap
fetched_at: 2026-01-21T19:55:17.271152921-03:00
rendered_js: false
word_count: 334
summary: This document explains how to integrate LiteLLM with evaluation tools like MLflow and AutoEvals to benchmark and test large language models using a unified OpenAI-compatible proxy.
tags:
    - litellm
    - mlflow
    - autoevals
    - llm-evaluation
    - model-testing
    - openai-proxy
category: tutorial
---

## Using LiteLLM with MLflow[​](#using-litellm-with-mlflow "Direct link to Using LiteLLM with MLflow")

MLflow provides an API `mlflow.evaluate()` to help evaluate your LLMs [https://mlflow.org/docs/latest/llms/llm-evaluate/index.html](https://mlflow.org/docs/latest/llms/llm-evaluate/index.html)

### Pre Requisites[​](#pre-requisites "Direct link to Pre Requisites")

### Step 1: Start LiteLLM Proxy on the CLI[​](#step-1-start-litellm-proxy-on-the-cli "Direct link to Step 1: Start LiteLLM Proxy on the CLI")

LiteLLM allows you to create an OpenAI compatible server for all supported LLMs. [More information on litellm proxy here](https://docs.litellm.ai/docs/simple_proxy)

```
$ litellm --model huggingface/bigcode/starcoder

#INFO: Proxy running on http://0.0.0.0:8000
```

**Here's how you can create the proxy for other supported llms**

- Bedrock
- Huggingface (TGI)
- Anthropic
- VLLM
- OpenAI Compatible Server
- TogetherAI
- Replicate
- Petals
- Palm
- Azure OpenAI
- AI21
- Cohere

```
$ export AWS_ACCESS_KEY_ID=""
$ export AWS_REGION_NAME="" # e.g. us-west-2
$ export AWS_SECRET_ACCESS_KEY=""
```

```
$ litellm --model bedrock/anthropic.claude-v2
```

### Step 2: Run MLflow[​](#step-2-run-mlflow "Direct link to Step 2: Run MLflow")

Before running the eval we will set `openai.api_base` to the litellm proxy from Step 1

```
openai.api_base ="http://0.0.0.0:8000"
```

```
import openai
import pandas as pd
openai.api_key ="anything"# this can be anything, we set the key on the proxy
openai.api_base ="http://0.0.0.0:8000"# set api base to the proxy from step 1


import mlflow
eval_data = pd.DataFrame(
{
"inputs":[
"What is the largest country",
"What is the weather in sf?",
],
"ground_truth":[
"India is a large country",
"It's cold in SF today"
],
}
)

with mlflow.start_run()as run:
    system_prompt ="Answer the following question in two sentences"
    logged_model_info = mlflow.openai.log_model(
        model="gpt-3.5",
        task=openai.ChatCompletion,
        artifact_path="model",
        messages=[
{"role":"system","content": system_prompt},
{"role":"user","content":"{question}"},
],
)

# Use predefined question-answering metrics to evaluate our model.
    results = mlflow.evaluate(
        logged_model_info.model_uri,
        eval_data,
        targets="ground_truth",
        model_type="question-answering",
)
print(f"See aggregated evaluation results below: \n{results.metrics}")

# Evaluation result for each data record is available in `results.tables`.
    eval_table = results.tables["eval_results_table"]
print(f"See evaluation table below: \n{eval_table}")


```

### MLflow Output[​](#mlflow-output "Direct link to MLflow Output")

```
{'toxicity/v1/mean': 0.00014476531214313582, 'toxicity/v1/variance': 2.5759661361262862e-12, 'toxicity/v1/p90': 0.00014604929747292773, 'toxicity/v1/ratio': 0.0, 'exact_match/v1': 0.0}
Downloading artifacts: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 1890.18it/s]
See evaluation table below:
                        inputs              ground_truth                                            outputs  token_count  toxicity/v1/score
0  What is the largest country  India is a large country   Russia is the largest country in the world in...           14           0.000146
1   What is the weather in sf?     It's cold in SF today   I'm sorry, I cannot provide the current weath...           36           0.000143
```

## Using LiteLLM with AutoEval[​](#using-litellm-with-autoeval "Direct link to Using LiteLLM with AutoEval")

AutoEvals is a tool for quickly and easily evaluating AI model outputs using best practices. [https://github.com/braintrustdata/autoevals](https://github.com/braintrustdata/autoevals)

### Pre Requisites[​](#pre-requisites-1 "Direct link to Pre Requisites")

### Quick Start[​](#quick-start "Direct link to Quick Start")

In this code sample we use the `Factuality()` evaluator from `autoevals.llm` to test whether an output is factual, compared to an original (expected) value.

**Autoevals uses gpt-3.5-turbo / gpt-4-turbo by default to evaluate responses**

See autoevals docs on the [supported evaluators](https://www.braintrustdata.com/docs/autoevals/python#autoevalsllm) - Translation, Summary, Security Evaluators etc

```
# auto evals imports 
from autoevals.llm import*
###################
import litellm

# litellm completion call
question ="which country has the highest population"
response = litellm.completion(
    model ="gpt-3.5-turbo",
    messages =[
{
"role":"user",
"content": question
}
],
)
print(response)
# use the auto eval Factuality() evaluator
evaluator = Factuality()
result = evaluator(
    output=response.choices[0]["message"]["content"],# response from litellm.completion()
    expected="India",# expected output
input=question                                          # question passed to litellm.completion
)

print(result)
```

#### Output of Evaluation - from AutoEvals[​](#output-of-evaluation---from-autoevals "Direct link to Output of Evaluation - from AutoEvals")

```
Score(
    name='Factuality', 
    score=0, 
    metadata=
        {'rationale': "The expert answer is 'India'.\nThe submitted answer is 'As of 2021, China has the highest population in the world with an estimated 1.4 billion people.'\nThe submitted answer mentions China as the country with the highest population, while the expert answer mentions India.\nThere is a disagreement between the submitted answer and the expert answer.", 
        'choice': 'D'
        }, 
    error=None
)
```