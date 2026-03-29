---
title: Observability with Mistral AI and Maxim - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-maxim-cookbook_maxim_mistral_integration
source: crawler
fetched_at: 2026-01-29T07:33:45.763894881-03:00
rendered_js: false
word_count: 214
summary: A tutorial on integrating Mistral AI models with the Maxim platform for observability, evaluation, and monitoring of LLM applications.
tags:
    - Mistral AI
    - Maxim
    - observability
    - monitoring
    - LLM
category: guide
---

In this cookbook, we show you how to use [Maxim](https://www.getmaxim.ai/), to observe Mistral LLM calls & metrics.

## What is Maxim?

Maxim AI provides comprehensive observability for your Mistral based AI applications. With Maxim's one-line integration, you can easily trace and analyse LLM calls, metrics, and more.

**Pros:**

- Performance Analytics: Track latency, tokens consumed, and costs
- Advanced Visualisation: Understand agent trajectories through intuitive dashboards

## Install and Import Required Modules

You need to install `mistralai` and `maxim-py` packages from [pypy](https://pypy.org/)

## Set the environment variables

You can sign up on [Maxim](https://getmaxim.ai/signup) and create a new Api Key from Settings. After that go to Logs section and create a new Log Repository, you will receive a Log Repository Id. Get ready with your Mistral Api Key also.

## Initialize logger

Create an instance of Maxim Logger

## Make LLM calls using MaximMistralClient

Make a call to Mistral via Mistral Api Client provided by Maxim, define the model you want to use and list of messages.

To check the logs shared by Mistral SDK with Maxim -

1. Go to Logs section in Maxim Platform
2. Go to the respective Log Repository you created.
3. Switch to `Logs` from top tab view and analyse the traces received

![Gif](https://raw.githubusercontent.com/akmadan/platform-docs-public/docs/observability-maxim-provider/static/img/guides/maxim_traces.gif)

## Async LLM call

## Feedback

* * *

If you have any feedback or requests, please create a GitHub [Issue](https://github.com/maximhq/maxim-docs).