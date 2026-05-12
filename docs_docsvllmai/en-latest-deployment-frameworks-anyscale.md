---
title: Anyscale - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/anyscale/
source: sitemap
fetched_at: 2026-05-07T21:11:35.866004103-03:00
rendered_js: false
word_count: 99
summary: This document provides an overview of using the Anyscale platform to manage Ray clusters and deploy vLLM for production-ready model inference and fine-tuning tasks.
tags:
    - anyscale
    - ray-cluster
    - model-deployment
    - llm-inference
    - cloud-infrastructure
    - batch-processing
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/anyscale.md "Edit this page")

[Anyscale](https://www.anyscale.com) is a managed, multi-cloud platform developed by the creators of Ray.

Anyscale automates the entire lifecycle of Ray clusters in your AWS, GCP, or Azure account, delivering the flexibility of open-source Ray without the operational overhead of maintaining Kubernetes control planes, configuring autoscalers, managing observability stacks, or manually managing head and worker nodes with helper scripts like [examples/ray\_serving/run\_cluster.sh](https://github.com/vllm-project/vllm/blob/main/examples/ray_serving/run_cluster.sh).

When serving large language models with vLLM, Anyscale can rapidly provision [production-ready HTTPS endpoints](https://docs.anyscale.com/examples/deploy-ray-serve-llms) or [fault-tolerant batch inference jobs](https://docs.anyscale.com/examples/ray-data-llm).

## Production-ready vLLM on Anyscale quickstarts[¶](#production-ready-vllm-on-anyscale-quickstarts "Permanent link")

- [Offline batch inference](https://console.anyscale.com/template-preview/llm_batch_inference?utm_source=vllm_docs)
- [Deploy vLLM services](https://console.anyscale.com/template-preview/llm_serving?utm_source=vllm_docs)
- [Curate a dataset](https://console.anyscale.com/template-preview/audio-dataset-curation-llm-judge?utm_source=vllm_docs)
- [Finetune an LLM](https://console.anyscale.com/template-preview/entity-recognition-with-llms?utm_source=vllm_docs)