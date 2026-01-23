---
title: Argilla | liteLLM
url: https://docs.litellm.ai/docs/observability/argilla
source: sitemap
fetched_at: 2026-01-21T19:45:51.865082117-03:00
rendered_js: false
word_count: 74
summary: This document provides instructions on how to configure and create a dataset in Argilla using the Python client for collaborative AI data annotation.
tags:
    - argilla
    - dataset-creation
    - python-client
    - data-annotation
    - configuration
category: tutorial
---

Argilla is a collaborative annotation tool for AI engineers and domain experts who need to build high-quality datasets for their projects.

To log the data to Argilla, first you need to deploy the Argilla server. If you have not deployed the Argilla server, please follow the instructions [here](https://docs.argilla.io/latest/getting_started/quickstart/).

Next, you will need to configure and create the Argilla dataset.

```
import argilla as rg

client = rg.Argilla(api_url="<api_url>", api_key="<api_key>")

settings = rg.Settings(
    guidelines="These are some guidelines.",
    fields=[
        rg.ChatField(
            name="user_input",
),
        rg.TextField(
            name="llm_output",
),
],
    questions=[
        rg.RatingQuestion(
            name="rating",
            values=[1,2,3,4,5,6,7],
),
],
)

dataset = rg.Dataset(
    name="my_first_dataset",
    settings=settings,
)

dataset.create()
```

To just log a sample of calls to argilla, add `ARGILLA_SAMPLING_RATE` to your env vars.