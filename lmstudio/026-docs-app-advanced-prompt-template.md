---
title: Prompt Template
url: https://lmstudio.ai/docs/app/advanced/prompt-template
source: sitemap
fetched_at: 2026-04-07T21:29:40.067038121-03:00
rendered_js: false
word_count: 250
summary: This guide explains how users can override and customize the prompt template settings for any model within LM Studio, detailing options like using Jinja templating or manual configuration.
tags:
    - prompt-template
    - lm-studio
    - model-configuration
    - advanced-settings
    - jinja
category: guide
---

`Advanced`

By default, LM Studio will automatically configure the prompt template based on the model file's metadata.

However, you can customize the prompt template for any model.

* * *

### Overriding the Prompt Template for a Specific Model[](#overriding-the-prompt-template-for-a-specific-model)

Head over to the My Models tab and click on the gear ⚙️ icon to edit the model's default parameters.

###### Pro tip: you can jump to the My Models tab from anywhere by pressing `⌘` + `3` on Mac, or `ctrl` + `3` on Windows / Linux.

### Customize the Prompt Template[](#customize-the-prompt-template)

###### 💡 In most cases you don't need to change the prompt template

When a model doesn't come with a prompt template information, LM Studio will surface the `Prompt Template` config box in the **🧪 Advanced Configuration** sidebar.

![undefined](https://lmstudio.ai/assets/docs/prompt-template.png)

The Prompt Template config box in the chat sidebar

You can make this config box always show up by right clicking the sidebar and selecting **Always Show Prompt Template**.

### Prompt template options[](#prompt-template-options)

#### Jinja Template

You can express the prompt template in Jinja.

###### 💡 [Jinja](https://en.wikipedia.org/wiki/Jinja_%28template_engine%29) is a templating engine used to encode the prompt template in several popular LLM model file formats.

#### Manual

You can also express the prompt template manually by specifying message role prefixes and suffixes.

* * *

#### Reasons you might want to edit the prompt template:

- The model's metadata is incorrect, incomplete, or LM Studio doesn't recognize it
- The model does not have a prompt template in its metadata (e.g. custom or older models)
- You want to customize the prompt template for a specific use case