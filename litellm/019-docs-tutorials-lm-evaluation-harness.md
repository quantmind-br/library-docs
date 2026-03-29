---
title: Benchmark LLMs - LM Harness, FastEval, Flask | liteLLM
url: https://docs.litellm.ai/docs/tutorials/lm_evaluation_harness
source: sitemap
fetched_at: 2026-01-21T19:55:36.062741857-03:00
rendered_js: false
word_count: 290
summary: This document provides step-by-step instructions for running various LLM benchmarks using the LiteLLM proxy server to enable compatibility with OpenAI-based evaluation tools.
tags:
    - llm-benchmarking
    - litellm-proxy
    - lm-eval-harness
    - fasteval
    - flask-evaluation
    - model-evaluation
category: tutorial
---

## LM Harness Benchmarks[​](#lm-harness-benchmarks "Direct link to LM Harness Benchmarks")

Evaluate LLMs 20x faster with TGI via litellm proxy's `/completions` endpoint.

This tutorial assumes you're using the `big-refactor` branch of [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/big-refactor)

NOTE: LM Harness has not updated to using `openai 1.0.0+`, in order to deal with this we will run lm harness in a venv

**Step 1: Start the local proxy** see supported models [here](https://docs.litellm.ai/docs/simple_proxy)

```
$ litellm --model huggingface/bigcode/starcoder
```

Using a custom api base

```
$ export HUGGINGFACE_API_KEY=my-api-key #[OPTIONAL]
$ litellm --model huggingface/tinyllama --api_base https://k58ory32yinf1ly0.us-east-1.aws.endpoints.huggingface.cloud
```

OpenAI Compatible Endpoint at [http://0.0.0.0:8000](http://0.0.0.0:8000)

**Step 2: Create a Virtual Env for LM Harness + Use OpenAI 0.28.1** We will now run lm harness with a new virtual env with openai==0.28.1

```
python3 -m venv lmharness 
source lmharness/bin/activate
```

Pip install openai==0.28.01 in the venv

```
pip install openai==0.28.01
```

**Step 3: Set OpenAI API Base & Key**

```
$ export OPENAI_BASE_URL=http://0.0.0.0:8000
```

LM Harness requires you to set an OpenAI API key `OPENAI_API_SECRET_KEY` for running benchmarks

```
export OPENAI_API_SECRET_KEY=anything
```

**Step 4: Run LM-Eval-Harness**

pip install lm harness dependencies in venv

```
python3 -m pip install -e .
```

```
python3 -m lm_eval \
  --model openai-completions \
  --model_args engine=davinci \
  --task crows_pairs_english_age

```

## FastEval[​](#fasteval "Direct link to FastEval")

**Step 1: Start the local proxy** see supported models [here](https://docs.litellm.ai/docs/simple_proxy)

```
$ litellm --model huggingface/bigcode/starcoder
```

**Step 2: Set OpenAI API Base & Key**

```
$ export OPENAI_BASE_URL=http://0.0.0.0:8000
```

Set this to anything since the proxy has the credentials

```
export OPENAI_API_KEY=anything
```

**Step 3 Run with FastEval**

**Clone FastEval**

```
# Clone this repository, make it the current working directory
git clone --depth 1 https://github.com/FastEval/FastEval.git
cd FastEval
```

**Set API Base on FastEval**

On FastEval make the following **2 line code change** to set `OPENAI_BASE_URL`

[https://github.com/FastEval/FastEval/pull/90/files](https://github.com/FastEval/FastEval/pull/90/files)

```
try:
    api_base = os.environ["OPENAI_BASE_URL"]#changed: read api base from .env
if api_base ==None:
        api_base ="https://api.openai.com/v1"
    response =await self.reply_two_attempts_with_different_max_new_tokens(
        conversation=conversation,
        api_base=api_base,# #changed: pass api_base
        api_key=os.environ["OPENAI_API_KEY"],
        temperature=temperature,
        max_new_tokens=max_new_tokens,
```

**Run FastEval** Set `-b` to the benchmark you want to run. Possible values are `mt-bench`, `human-eval-plus`, `ds1000`, `cot`, `cot/gsm8k`, `cot/math`, `cot/bbh`, `cot/mmlu` and `custom-test-data`

Since LiteLLM provides an OpenAI compatible proxy `-t` and `-m` don't need to change `-t` will remain openai `-m` will remain gpt-3.5

```
./fasteval -b human-eval-plus -t openai -m gpt-3.5-turbo
```

## FLASK - Fine-grained Language Model Evaluation[​](#flask---fine-grained-language-model-evaluation "Direct link to FLASK - Fine-grained Language Model Evaluation")

Use litellm to evaluate any LLM on FLASK [https://github.com/kaistAI/FLASK](https://github.com/kaistAI/FLASK)

**Step 1: Start the local proxy**

```
$ litellm --model huggingface/bigcode/starcoder
```

**Step 2: Set OpenAI API Base & Key**

```
$ export OPENAI_BASE_URL=http://0.0.0.0:8000
```

**Step 3 Run with FLASK**

```
git clone https://github.com/kaistAI/FLASK
```

Run the eval

```
python gpt4_eval.py -q '../evaluation_set/flask_evaluation.jsonl'
```

## Debugging[​](#debugging "Direct link to Debugging")

### Making a test request to your proxy[​](#making-a-test-request-to-your-proxy "Direct link to Making a test request to your proxy")

This command makes a test Completion, ChatCompletion request to your proxy server