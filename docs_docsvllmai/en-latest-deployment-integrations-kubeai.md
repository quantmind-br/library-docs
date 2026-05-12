---
title: KubeAI - vLLM
url: https://docs.vllm.ai/en/latest/deployment/integrations/kubeai/
source: sitemap
fetched_at: 2026-05-07T21:12:02.049307329-03:00
rendered_js: false
word_count: 82
summary: This document introduces KubeAI as a Kubernetes operator for deploying and managing vLLM models with features like autoscaling and caching.
tags:
    - kubernetes
    - vllm
    - model-deployment
    - container-orchestration
    - autoscaling
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/integrations/kubeai.md "Edit this page")

[KubeAI](https://github.com/substratusai/kubeai) is a Kubernetes operator that enables you to deploy and manage AI models on Kubernetes. It provides a simple and scalable way to deploy vLLM in production. Functionality such as scale-from-zero, load based autoscaling, model caching, and much more is provided out of the box with zero external dependencies.

Please see the Installation Guides for environment specific instructions:

- [Any Kubernetes Cluster](https://www.kubeai.org/installation/any/)
- [AKS](https://www.kubeai.org/installation/aks/)
- [EKS](https://www.kubeai.org/installation/eks/)
- [GKE](https://www.kubeai.org/installation/gke/)

Once you have KubeAI installed, you can [configure text generation models](https://www.kubeai.org/how-to/configure-text-generation-models/) using vLLM.