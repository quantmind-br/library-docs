---
title: marimo
url: https://docs.ollama.com/integrations/marimo.md
source: llms
fetched_at: 2026-02-04T11:34:33.610810692-03:00
rendered_js: false
word_count: 357
summary: This document provides instructions on how to install marimo and configure it to use Ollama as an AI provider for notebook chats and code completion.
tags:
    - marimo
    - ollama
    - ai-integration
    - setup-guide
    - python-notebooks
    - code-completion
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# marimo

## Install

Install [marimo](https://marimo.io). You can use `pip` or `uv` for this. You
can also use `uv` to create a sandboxed environment for marimo by running:

```
uvx marimo edit --sandbox notebook.py
```

## Usage with Ollama

1. In marimo, go to the user settings and go to the AI tab. From here
   you can find and configure Ollama as an AI provider. For local use you
   would typically point the base url to `http://localhost:11434/v1`.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-settings.png?fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=33007ad4867ca8258854eab513da81ff" alt="Ollama settings in marimo" width="50%" data-og-width="1584" data-og-height="1192" data-path="images/marimo-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-settings.png?w=280&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=88f9975f40532ec6c5a05d46a4dfc66b 280w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-settings.png?w=560&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=c5f2fb812e3cdc37da833cb8dbd19fc9 560w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-settings.png?w=840&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=34cc16d2887d433412dee3a8a5b5e48e 840w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-settings.png?w=1100&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=25f4303c64cac397270887af6d31a790 1100w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-settings.png?w=1650&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=a2f14024f512f0b4b708a01b0dc10d82 1650w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-settings.png?w=2500&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=34414f11928772bb874efedba5717126 2500w" />
</div>

2. Once the AI provider is set up, you can turn on/off specific AI models you'd like to access.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-models.png?fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=61acca69dfc3d32e1eb524095c42e4a0" alt="Selecting an Ollama model" width="50%" data-og-width="1583" data-og-height="944" data-path="images/marimo-models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-models.png?w=280&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=c0e7013e5063350ea6d104e50d80db18 280w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-models.png?w=560&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=705c941975b8c832754d3751e1e91013 560w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-models.png?w=840&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=e4b46bfe8e27abe773ac4683d441ea80 840w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-models.png?w=1100&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=77eca4748400ae47019adc2c0ec1e35d 1100w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-models.png?w=1650&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=27f794ec8a4828cb2d026517067d4665 1650w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-models.png?w=2500&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=2dcb07fbf5c49c8bcbfe44ac00d2f064 2500w" />
</div>

3. You can also add a model to the list of available models by scrolling to the bottom and using the UI there.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-add-model.png?fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=c3a2dfa7cba1a6565cc726bbbe0ea079" alt="Adding a new Ollama model" width="50%" data-og-width="1593" data-og-height="1018" data-path="images/marimo-add-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-add-model.png?w=280&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=f3fed685d9a7f059f3a234fb6d36a0ac 280w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-add-model.png?w=560&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=ccee568229e5c39358a7c9851ac3adf3 560w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-add-model.png?w=840&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=e192f55a8240368506191676a9b42c06 840w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-add-model.png?w=1100&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=ae2357d28eb9561494367e28147c1dbd 1100w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-add-model.png?w=1650&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=eb60d79b8e74814090fd50f1e546af49 1650w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-add-model.png?w=2500&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=45fe2d14d550c11a61ef8ea05286233a 2500w" />
</div>

4. Once configured, you can now use Ollama for AI chats in marimo.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-chat.png?fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=03cd217cf60765a00da87e6dc7a07f53" alt="Configure code completion" width="50%" data-og-width="1187" data-og-height="761" data-path="images/marimo-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-chat.png?w=280&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=7f28dd7d2d8c64d4e84b014d77995c25 280w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-chat.png?w=560&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=f3dff746ee0f9e8a116084a4ed4d170b 560w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-chat.png?w=840&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=ae91ab595e9bfd6fb8f29c915790deb0 840w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-chat.png?w=1100&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=b7043c063681c3e9c475d4c4e6929abf 1100w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-chat.png?w=1650&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=f962e691bf3c18c722858899ef05c208 1650w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-chat.png?w=2500&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=c5557c61ead1650ab84a0decfaf25dc0 2500w" />
</div>

4. Alternatively, you can now use Ollama for **inline code completion** in marimo. This can be configured in the "AI Features" tab.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-code-completion.png?fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=2cd6ad42b810642a90d41b7fd3515278" alt="Configure code completion" width="50%" data-og-width="1790" data-og-height="888" data-path="images/marimo-code-completion.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-code-completion.png?w=280&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=7b2e318446b88494ad5fde5aec9f1b15 280w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-code-completion.png?w=560&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=34628628420259c867834f94b3326197 560w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-code-completion.png?w=840&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=0814863d8bcc82e0406e54466cb82c88 840w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-code-completion.png?w=1100&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=b3f6206fb2713d1b6e9e6621f8f8796e 1100w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-code-completion.png?w=1650&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=a00ca3349572edc72e24dec9aa6e433a 1650w, https://mintcdn.com/ollama-9269c548/sniSFOOyehzMt2RV/images/marimo-code-completion.png?w=2500&fit=max&auto=format&n=sniSFOOyehzMt2RV&q=85&s=f5dbff538f1533c23bc9716d848cedb0 2500w" />
</div>

## Connecting to ollama.com

1. Sign in to ollama cloud via `ollama signin`
2. In the ollama model settings add a model that ollama hosts, like `gpt-oss:120b`.
3. You can now refer to this model in marimo!