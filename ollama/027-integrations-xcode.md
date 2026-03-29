---
title: Xcode
url: https://docs.ollama.com/integrations/xcode.md
source: llms
fetched_at: 2026-02-04T11:34:50.369342565-03:00
rendered_js: false
word_count: 200
summary: This document provides instructions for integrating Ollama with Xcode, covering setup for both locally hosted models and internet-hosted connections using API keys.
tags:
    - xcode
    - ollama
    - apple-intelligence
    - setup-guide
    - macos
    - api-keys
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xcode

## Install

Install [XCode](https://developer.apple.com/xcode/)

## Usage with Ollama

<Note> Ensure Apple Intelligence is setup and the latest XCode version is v26.0 </Note>

1. Click **XCode** in top left corner > **Settings**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-intelligence-window.png?fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=61d8115b15ca2e451d99a66dd30df4e0" alt="Xcode Intelligence window" width="50%" data-og-width="1430" data-og-height="646" data-path="images/xcode-intelligence-window.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-intelligence-window.png?w=280&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=dccb7de9b697de5b3528b247d3ef7ced 280w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-intelligence-window.png?w=560&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=1a47354c940bb3579a5cfc2bd0383100 560w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-intelligence-window.png?w=840&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=f4f2791bdde6f5f07ec8a4604d7958ee 840w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-intelligence-window.png?w=1100&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=0a2aeaddc3e1ce236c0da0de517982f1 1100w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-intelligence-window.png?w=1650&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=c2dd9fb0df13083c6214a22c7a10c21d 1650w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-intelligence-window.png?w=2500&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=2d47484eb926b98d696d2e16a498bd03 2500w" />
</div>

2. Select **Locally Hosted**, enter port **11434** and click **Add**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-locally-hosted.png?fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=05886457701f4809015cbdfe9da765a2" alt="Xcode settings" width="50%" data-og-width="1018" data-og-height="732" data-path="images/xcode-locally-hosted.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-locally-hosted.png?w=280&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=709a77fcd7626725397b07d6702e85b2 280w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-locally-hosted.png?w=560&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=993cfc03618df1b7e38b59d054af7693 560w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-locally-hosted.png?w=840&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=77adf13ef4ed9be895f418795c3ca095 840w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-locally-hosted.png?w=1100&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=8ca7e015c0563bbacb3ed887803ea7e2 1100w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-locally-hosted.png?w=1650&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=c26ef88d1645deb4d577b34c05f0ef08 1650w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-locally-hosted.png?w=2500&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=c4f02b4ae584eca16242a14d4ea3346e 2500w" />
</div>

3. Select the **star icon** on the top left corner and click the **dropdown**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-chat-icon.png?fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=b4e39af73fd7e80ac04f8211cd25c844" alt="Xcode settings" width="50%" data-og-width="920" data-og-height="562" data-path="images/xcode-chat-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-chat-icon.png?w=280&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=538f334cf2091a439b3783eeafbb5fb5 280w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-chat-icon.png?w=560&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=6924aaf4b3c1765c77aad690b9291931 560w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-chat-icon.png?w=840&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=999a3428fbd4dad7b0459cc078f24969 840w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-chat-icon.png?w=1100&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=1000eb4de086153ff772319c6da31d37 1100w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-chat-icon.png?w=1650&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=fd8df7f3f5a6fefa5f4305e06f95ddca 1650w, https://mintcdn.com/ollama-9269c548/ibktA29M6ZTyqWFA/images/xcode-chat-icon.png?w=2500&fit=max&auto=format&n=ibktA29M6ZTyqWFA&q=85&s=5308a627658024ecf6200e004db503e5 2500w" />
</div>

4. Click **My Account** and select your desired model

## Connecting to ollama.com directly

1. Create an [API key](https://ollama.com/settings/keys) from ollama.com
2. Select **Internet Hosted** and enter URL as `https://ollama.com`
3. Enter your **Ollama API Key** and click **Add**