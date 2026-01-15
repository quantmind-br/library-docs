---
title: Codex Models
url: https://developers.openai.com/codex/models.md
source: llms
fetched_at: 2026-01-13T18:59:53.862871473-03:00
rendered_js: false
word_count: 295
summary: This document provides a comparative overview and specification of various Codex and GPT models, detailing their capabilities, speed, and supported features such as SDK, CLI, and API access.
tags:
    - codex
    - gpt-models
    - model-selection
    - ai-agents
    - machine-learning
    - sdk
    - api-access
category: reference
---

# Codex Models

## Recommended models

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  <ModelDetails
    client:load
    name="gpt-5.2-codex"
    slug="gpt-5.2-codex"
    wallpaperUrl="/images/codex/gpt-5.2-codex.png"
    description="Most advanced agentic coding model for real-world engineering."
    data={{
      features: [
        {
          title: "Capability",
          value: "",
          icons: [
            "openai.SparklesFilled",
            "openai.SparklesFilled",
            "openai.SparklesFilled",
            "openai.SparklesFilled",
            "openai.SparklesFilled",
          ],
        },
        {
          title: "Speed",
          value: "",
          icons: [
            "openai.Flash",
            "openai.Flash",
            "openai.Flash",
            "openai.Flash",
          ],
        },
        {
          title: "Codex CLI & SDK",
          value: true,
        },
        { title: "Codex IDE extension", value: true },
        {
          title: "Codex Cloud",
          value: true,
        },
        { title: "ChatGPT Credits", value: true },
        { title: "API Access", value: false },
      ],
    }}
  />
  <ModelDetails
    client:load
    name="gpt-5.1-codex-max"
    slug="gpt-5.1-codex-max"
    description="Optimized for long-horizon, agentic coding tasks in Codex."
    data={{
      features: [
        {
          title: "Capability",
          value: "",
          icons: [
            "openai.SparklesFilled",
            "openai.SparklesFilled",
            "openai.SparklesFilled",
            "openai.SparklesFilled",
          ],
        },
        {
          title: "Speed",
          value: "",
          icons: [
            "openai.Flash",
            "openai.Flash",
            "openai.Flash",
            "openai.Flash",
          ],
        },
        {
          title: "Codex CLI & SDK",
          value: true,
        },
        { title: "Codex IDE extension", value: true },
        {
          title: "Codex Cloud",
          value: false,
        },
        { title: "ChatGPT Credits", value: true },
        { title: "API Access", value: true },
      ],
    }}
  />
  <ModelDetails
    client:load
    name="gpt-5.1-codex-mini"
    slug="gpt-5.1-codex-mini"
    description="Smaller, more cost-effective, less-capable version of GPT-5.1-Codex."
    data={{
      features: [
        {
          title: "Capability",
          value: "",
          icons: [
            "openai.SparklesFilled",
            "openai.SparklesFilled",
            "openai.SparklesFilled",
          ],
        },
        {
          title: "Speed",
          value: "",
          icons: [
            "openai.Flash",
            "openai.Flash",
            "openai.Flash",
            "openai.Flash",
            "openai.Flash",
          ],
        },
        {
          title: "Codex CLI & SDK",
          value: true,
        },
        { title: "Codex IDE extension", value: true },
        {
          title: "Codex Cloud",
          value: false,
        },
        { title: "ChatGPT Credits", value: true },
        { title: "API Access", value: true },
      ],
    }}
  />
</div>

## Alternative models

<div class="not-prose grid gap-4 md:grid-cols-2 xl:grid-cols-3">

{" "}

<ModelDetails
  client:load
  name="gpt-5.2"
  slug="gpt-5.2"
  description="Our best general agentic model for tasks across industries and domains."
  collapsible
  data={{
    features: [
      {
        title: "Capability",
        value: "",
        icons: [
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
        ],
      },
      {
        title: "Speed",
        value: "",
        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
      },
      {
        title: "Codex CLI & SDK",
        value: true,
      },
      { title: "Codex IDE extension", value: true },
      {
        title: "Codex Cloud",
        value: false,
      },
      { title: "ChatGPT Credits", value: true },
      { title: "API Access", value: true },
    ],
  }}
/>

<ModelDetails
  client:load
  name="gpt-5.1"
  description="Great for for coding and agentic tasks across domains. Succeeded by GPT-5.2."
  slug="gpt-5.1"
  collapsible
  data={{
    features: [
      {
        title: "Capability",
        value: "",
        icons: [
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
        ],
      },
      {
        title: "Speed",
        value: "",
        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
      },
      {
        title: "Codex CLI & SDK",
        value: true,
      },
      { title: "Codex IDE extension", value: true },
      {
        title: "Codex Cloud",
        value: false,
      },
      { title: "ChatGPT Credits", value: true },
      { title: "API Access", value: true },
    ],
  }}
/>
<ModelDetails
  client:load
  name="gpt-5.1-codex"
  slug="gpt-5.1-codex"
  description="Optimized for long-running, agentic coding tasks in Codex. Succeeded by GPT-5.1-Codex-Max."
  collapsible
  data={{
    features: [
      {
        title: "Capability",
        value: "",
        icons: [
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
        ],
      },
      {
        title: "Speed",
        value: "",
        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
      },
      {
        title: "Codex CLI & SDK",
        value: true,
      },
      { title: "Codex IDE extension", value: true },
      {
        title: "Codex Cloud",
        value: true,
      },
      { title: "ChatGPT Credits", value: true },
      { title: "API Access", value: true },
    ],
  }}
/>
<ModelDetails
  client:load
  name="gpt-5-codex"
  slug="gpt-5-codex"
  description="Version of GPT-5 tuned for long-running, agentic coding tasks. Succeeded by GPT-5.1-Codex."
  collapsible
  data={{
    features: [
      {
        title: "Capability",
        value: "",
        icons: [
          "openai.SparklesFilled",
          "openai.SparklesFilled",
          "openai.SparklesFilled",
        ],
      },
      {
        title: "Speed",
        value: "",
        icons: ["openai.Flash", "openai.Flash", "openai.Flash"],
      },
      {
        title: "Codex CLI & SDK",
        value: true,
      },
      { title: "Codex IDE extension", value: true },
      {
        title: "Codex Cloud",
        value: false,
      },
      { title: "ChatGPT Credits", value: true },
      { title: "API Access", value: true },
    ],
  }}
/>

    <ModelDetails
      client:load
      name="gpt-5-codex-mini"
      slug="gpt-5-codex"
      description="Smaller, more cost-effective version of GPT-5-Codex. Succeeded by GPT-5.1-Codex-Mini."
      collapsible
      data={{
        features: [
          {
            title: "Capability",
            value: "",
            icons: [
              "openai.SparklesFilled",
              "openai.SparklesFilled",
            ],
          },
          { title: "Speed", value: "", icons: ["openai.Flash", "openai.Flash", "openai.Flash", "openai.Flash"] },
          {
            title: "Codex CLI & SDK",
            value: true,
          },
          { title: "Codex IDE extension", value: true },
          {
            title: "Codex Cloud",
            value: false,
          },
          { title: "ChatGPT Credits", value: true },
          { title: "API Access", value: false },
        ],
      }}
    />

    <ModelDetails
      client:load
      name="gpt-5"
      slug="gpt-5"
      description="Reasoning model for coding and agentic tasks across domains. Succeeded by GPT-5.1."
      collapsible
      data={{
        features: [
          {
            title: "Capability",
            value: "",
            icons: [
              "openai.SparklesFilled",
              "openai.SparklesFilled",
              "openai.SparklesFilled",
            ],
          },
          { title: "Speed", value: "", icons: ["openai.Flash", "openai.Flash", "openai.Flash"] },
          {
            title: "Codex CLI & SDK",
            value: true,
          },
          { title: "Codex IDE extension", value: true },
          {
            title: "Codex Cloud",
            value: false,
          },
          { title: "ChatGPT Credits", value: true },
          { title: "API Access", value: true },
        ],
      }}
    />

  </div>

## Other models

Codex works best with the models listed above.

You can also point Codex at any model and provider that supports either the [Chat Completions](https://platform.openai.com/docs/api-reference/chat) or [Responses APIs](https://platform.openai.com/docs/api-reference/responses) to fit your specific use case.

<DocsTip>
  Support for the Chat Completions API is deprecated and will be removed in
  future releases of Codex.
</DocsTip>

## Configuring models

### Configure your default local model

The Codex CLI and IDE extension use the same `config.toml` [configuration file](https://developers.openai.com/codex/config-basic). To specify a model, add a `model` entry to your configuration file. If no model is specified, the Codex CLI or IDE extension will default to a recommended model.

```toml
model = "gpt-5.2"
```

### Choosing a different local model temporarily

In the Codex CLI, you can use the `/model` command during an active thread to change the model. In the IDE extension, you can use the model selector below the input box to choose your model.

To start a new Codex CLI thread with a specific model or to specify the model for `codex exec` you can use the `--model`/`-m` flag:

```bash
codex -m gpt-5.1-codex-mini
```

### Choosing your model for cloud tasks

There is currently no way to change the default model for Codex Cloud tasks.