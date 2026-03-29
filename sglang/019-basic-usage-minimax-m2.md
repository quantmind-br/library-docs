---
title: MiniMax M2.1/M2 Usage — SGLang
url: https://docs.sglang.io/basic_usage/minimax_m2.html
source: crawler
fetched_at: 2026-02-04T08:47:39.817386361-03:00
rendered_js: false
word_count: 174
summary: This document provides instructions for deploying and testing the MiniMax-M2 and M2.1 large language models, covering system requirements and SGLang server configuration.
tags:
    - minimax-m2
    - model-deployment
    - gpu-requirements
    - sglang
    - mixture-of-experts
    - llm-inference
category: guide
---

## MiniMax M2.1/M2 Usage[#](#minimax-m2-1-m2-usage "Link to this heading")

[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1) and [MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2) are advanced large language models created by [MiniMax](https://www.minimax.io/).

MiniMax-M2 series redefines efficiency for agents. It’s a compact, fast, and cost-effective MoE model (230 billion total parameters with 10 billion active parameters) built for elite performance in coding and agentic tasks, all while maintaining powerful general intelligence. With just 10 billion activated parameters, MiniMax-M2 provides the sophisticated, end-to-end tool use performance expected from today’s leading models, but in a streamlined form factor that makes deployment and scaling easier than ever.

## Supported Models[#](#supported-models "Link to this heading")

This guide applies to the following models. You only need to update the model name during deployment. The following examples use **MiniMax-M2**:

- [MiniMaxAI/MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)
- [MiniMaxAI/MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2)

## System Requirements[#](#system-requirements "Link to this heading")

The following are recommended configurations; actual requirements should be adjusted based on your use case:

- 4x 96GB GPUs: Supported context length of up to 400K tokens.
- 8x 144GB GPUs: Supported context length of up to 3M tokens.

## Deployment with Python[#](#deployment-with-python "Link to this heading")

4-GPU deployment command:

```
python-msglang.launch_server\
--model-pathMiniMaxAI/MiniMax-M2\
--tp-size4\
--tool-call-parserminimax-m2\
--reasoning-parserminimax-append-think\
--host0.0.0.0\
--trust-remote-code\
--port8000\
--mem-fraction-static0.85
```

8-GPU deployment command:

```
python-msglang.launch_server\
--model-pathMiniMaxAI/MiniMax-M2\
--tp-size8\
--ep-size8\
--tool-call-parserminimax-m2\
--reasoning-parserminimax-append-think\
--host0.0.0.0\
--trust-remote-code\
--port8000\
--mem-fraction-static0.85
```

## Testing Deployment[#](#testing-deployment "Link to this heading")

After startup, you can test the SGLang OpenAI-compatible API with the following command:

```
curlhttp://localhost:8000/v1/chat/completions\
-H"Content-Type: application/json"\
-d'{
        "model": "MiniMaxAI/MiniMax-M2",
        "messages": [
            {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}]},
            {"role": "user", "content": [{"type": "text", "text": "Who won the world series in 2020?"}]}
        ]
    }'
```