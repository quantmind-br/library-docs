---
title: JetBrains
url: https://docs.ollama.com/integrations/jetbrains.md
source: llms
fetched_at: 2026-02-04T11:34:31.769993463-03:00
rendered_js: false
word_count: 205
summary: This document provides step-by-step instructions for configuring JetBrains IDEs to use local LLMs via the Ollama integration.
tags:
    - jetbrains
    - intellij
    - ollama
    - ide-integration
    - local-llm
    - ai-assistant
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JetBrains

<Note>This example uses **IntelliJ**; same steps apply to other JetBrains IDEs (e.g., PyCharm).</Note>

## Install

Install [IntelliJ](https://www.jetbrains.com/idea/).

## Usage with Ollama

<Note>
  To use **Ollama**,  you will need a [JetBrains AI Subscription](https://www.jetbrains.com/ai-ides/buy/?section=personal\&billing=yearly).
</Note>

1. In Intellij, click the **chat icon** located in the right sidebar

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-chat-sidebar.png?fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=3744faa4bdfb6e817ad68d7da792bf18" alt="Intellij Sidebar Chat" width="50%" data-og-width="668" data-og-height="476" data-path="images/intellij-chat-sidebar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-chat-sidebar.png?w=280&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=b8b775ae96fdf260c9f9ffb001dee5f5 280w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-chat-sidebar.png?w=560&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=7636af78546e0de3a1ba1f0895d512b9 560w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-chat-sidebar.png?w=840&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=98ceeb48201d4c25a70ae3c723f394a4 840w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-chat-sidebar.png?w=1100&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=cfb6f2e863bef8b1cee3aad638a4bf7a 1100w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-chat-sidebar.png?w=1650&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=30a37f1fcebc59171c937ad65f222202 1650w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-chat-sidebar.png?w=2500&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=9a35c626ad3352cfc65846c756633ddd 2500w" />
</div>

2. Select the **current model** in the sidebar, then click **Set up Local Models**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-current-model.png?fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=cc42c11b23f4a9b57b3e7c69ae42b60b" alt="Intellij model bottom right corner" width="50%" data-og-width="778" data-og-height="546" data-path="images/intellij-current-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-current-model.png?w=280&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=48a6ec059b1eb155c1ebcf9059642c91 280w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-current-model.png?w=560&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=7b416430af08c499ca30b92aad33f71a 560w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-current-model.png?w=840&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=5c3d156e7ce892035a7c753893decd9a 840w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-current-model.png?w=1100&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=3f41f2e81f918d6ad424d317f86be381 1100w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-current-model.png?w=1650&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=dcc25dd0a711f5bd3d304c7cdea45617 1650w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-current-model.png?w=2500&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=47d24cfabf9aefb42d44a2438b0e4285 2500w" />
</div>

3. Under **Third Party AI Providers**, choose **Ollama**
4. Confirm the **Host URL** is `http://localhost:11434`, then click **Ok**
5. Once connected, select a model under **Local models by Ollama**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-local-models.png?fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=0cc866166e1d6af65b3d8a16c3f396f5" alt="Zed star icon in bottom right corner" width="50%" data-og-width="522" data-og-height="602" data-path="images/intellij-local-models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-local-models.png?w=280&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=cef5847f7b97a11ed6bc785d93181062 280w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-local-models.png?w=560&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=9c64e22cc5cc3db1d5dfd160450aeede 560w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-local-models.png?w=840&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=c2e29b300a2630189df542906012b957 840w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-local-models.png?w=1100&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=10a5578b086d21b104caf3a2d415a181 1100w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-local-models.png?w=1650&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=91a64e8e4e91a53dac2a3ff057c2b212 1650w, https://mintcdn.com/ollama-9269c548/YbLeuKjU_QVFWOuC/images/intellij-local-models.png?w=2500&fit=max&auto=format&n=YbLeuKjU_QVFWOuC&q=85&s=243144901c8988b937ead0dd1579f98a 2500w" />
</div>