---
title: Config Presets
url: https://lmstudio.ai/docs/app/presets
source: sitemap
fetched_at: 2026-04-07T21:29:22.25552949-03:00
rendered_js: false
word_count: 385
summary: This document explains what Presets are—bundles of system prompts and parameters for reuse—and details how to manage them, including importing from URLs or files, publishing them, and where they are stored on different operating systems.
tags:
    - presets
    - llm-parameters
    - reusable-settings
    - prompt-management
    - importing
    - sharing
category: guide
---

Presets are a way to bundle together a system prompt and other parameters into a single configuration that can be easily reused across different chats.

New in 0.3.15: You can [import](https://lmstudio.ai/docs/app/presets/import) Presets from file or URL, and even [publish](https://lmstudio.ai/docs/app/presets/publish) your own Presets to share with others on to the LM Studio Hub.

* * *

## Saving, resetting, and deselecting Presets[](#saving-resetting-and-deselecting-presets "Link to 'Saving, resetting, and deselecting Presets'")

Below is the anatomy of the Preset manager:

![undefined](https://lmstudio.ai/assets/docs/preset-widget-anatomy.webp)

The anatomy of the Preset manager in the settings sidebar.

## Importing, Publishing, and Updating Downloaded Presets[](#importing-publishing-and-updating-downloaded-presets "Link to 'Importing, Publishing, and Updating Downloaded Presets'")

Presets are JSON files. You can share them by sending around the JSON, or you can share them by publishing them to the LM Studio Hub. You can also import Presets from other users by URL. See the [Import](https://lmstudio.ai/docs/app/presets/import) and [Publish](https://lmstudio.ai/docs/app/presets/publish) sections for more details.

## Example: Build your own Prompt Library[](#example-build-your-own-prompt-library "Link to 'Example: Build your own Prompt Library'")

You can create your own prompt library by using Presets.

Your browser does not support the video tag.

Save collections of parameters as a Preset for easy reuse.

In addition to system prompts, every parameter under the Advanced Configuration sidebar can be recorded in a named Preset.

For example, you might want to always use a certain Temperature, Top P, or Max Tokens for a particular use case. You can save these settings as a Preset (with or without a system prompt) and easily switch between them.

#### The Use Case for Presets

- Save your system prompts, inference parameters as a named `Preset`.
- Easily switch between different use cases, such as reasoning, creative writing, multi-turn conversations, or brainstorming.

## Where Presets are stored[](#where-presets-are-stored "Link to 'Where Presets are stored'")

Presets are stored in the following directory:

#### macOS or Linux

```

~/.lmstudio/config-presets
```

#### Windows

```

%USERPROFILE%\.lmstudio\config-presets
```

### Migration from LM Studio 0.2.* Presets[](#migration-from-lm-studio-02-presets)

- Presets you've saved in LM Studio 0.2.* are automatically readable in 0.3.3 with no migration step needed.
- If you save **new changes** in a **legacy preset**, it'll be **copied** to a new format upon save.
  
  - The old files are NOT deleted.
- Notable difference: Load parameters are not included in the new preset format.
  
  - Favor editing the model's default config in My Models. See [how to do it here](https://lmstudio.ai/docs/configuration/per-model).

* * *

Chat with other LM Studio users, discuss LLMs, hardware, and more on the [LM Studio Discord server](https://discord.gg/aPQfnNkxGC).