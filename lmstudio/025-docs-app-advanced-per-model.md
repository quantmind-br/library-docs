---
title: Per-model Defaults
url: https://lmstudio.ai/docs/app/advanced/per-model
source: sitemap
fetched_at: 2026-04-07T21:29:38.412384394-03:00
rendered_js: false
word_count: 270
summary: This document explains how to configure default loading parameters for specific models within LM Studio by accessing settings in the My Models tab or by making and saving changes during the model loading process.
tags:
    - lm-studio
    - model-settings
    - default-parameters
    - gpu-offload
    - advanced-topics
category: guide
---

`Advanced`

You can set default load settings for each model in LM Studio.

When the model is loaded anywhere in the app (including through [`lms load`](https://lmstudio.ai/docs/cli#load-a-model-with-options)) these settings will be used.

* * *

### Setting default parameters for a model[](#setting-default-parameters-for-a-model)

Head to the My Models tab and click on the gear ⚙️ icon to edit the model's default parameters.

![undefined](https://lmstudio.ai/assets/docs/model-settings-gear.webp)

Click on the gear icon to edit the default load settings for a model.

This will open a dialog where you can set the default parameters for the model.

Your browser does not support the video tag.

You can set the default parameters for a model in this dialog.

Next time you load the model, these settings will be used.

#### Reasons to set default load parameters (not required, totally optional)

- Set a particular GPU offload settings for a given model
- Set a particular context size for a given model
- Whether or not to utilize Flash Attention for a given model

## Advanced Topics[](#advanced-topics "Link to 'Advanced Topics'")

### Changing load settings before loading a model[](#changing-load-settings-before-loading-a-model)

When you load a model, you can optionally change the default load settings.

![undefined](https://lmstudio.ai/assets/docs/load-model.png)

You can change the load settings before loading a model.

### Saving your changes as the default settings for a model[](#saving-your-changes-as-the-default-settings-for-a-model)

If you make changes to load settings when you load a model, you can save them as the default settings for that model.

![undefined](https://lmstudio.ai/assets/docs/save-load-changes.png)

If you make changes to load settings when you load a model, you can save them as the default settings for that model.

* * *

Chat with other LM Studio power users, discuss configs, models, hardware, and more on the [LM Studio Discord server](https://discord.gg/aPQfnNkxGC).