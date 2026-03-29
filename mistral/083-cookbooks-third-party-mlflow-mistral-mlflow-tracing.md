---
title: Observability with Mistral AI and MLflow - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-mlflow-mistral-mlflow-tracing
source: crawler
fetched_at: 2026-01-29T07:33:51.608223747-03:00
rendered_js: false
word_count: 105
summary: A technical guide demonstrating how to integrate Mistral AI models with MLflow for experiment tracking and model observability.
tags:
    - Mistral AI
    - MLflow
    - Observability
    - LLM
    - Experiment Tracking
category: guide
---

This is an example for leveraging MLflow's auto tracing capabilities for Mistral AI.

More information about MLflow Tracing is available [here](https://mlflow.org/docs/latest/llms/tracing/index.html).

## Getting Started

Install `mistralai` and `mlflow` (current versions as of 4-Feb-2025)

## Code

## Tracing

To see the MLflow tracing, open the MLflow UI in the same directory and the same virtualenv where you run this notebook.

### Launch the UI

Open a terminal and run this command:

`mlflow ui`

![Screenshot of launching the MLflow UI via command line](https://docs.mistral.ai/cookbooks/third_party/MLflow/mlflow-ui-launch.png)

### View the traces in the browser

Open your browser and connect to the MLflow UI port (default: [http://localhost:5000](http://localhost:5000))

![GIF animation of browsing a trace in the MLflow UI](https://docs.mistral.ai/cookbooks/third_party/MLflow/mlflow-tracing-chat-complete.gif)