---
title: n8n
url: https://docs.ollama.com/integrations/n8n.md
source: llms
fetched_at: 2026-02-04T11:34:35.68876764-03:00
rendered_js: false
word_count: 293
summary: This document provides instructions for integrating Ollama with n8n, covering local deployment via Docker and connecting to the ollama.com API.
tags:
    - n8n
    - ollama
    - workflow-automation
    - llm-integration
    - docker-configuration
    - local-ai
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# n8n

## Install

Install [n8n](https://docs.n8n.io/choose-n8n/).

## Using Ollama Locally

1. In the top right corner, click the dropdown and select **Create Credential**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-credential-creation.png?fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=5b7f955f792e8b9899f3b0b3a1846d06" alt="Create a n8n Credential" width="75%" data-og-width="896" data-og-height="436" data-path="images/n8n-credential-creation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-credential-creation.png?w=280&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=ca26ff9b910a94d1120a0df887424072 280w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-credential-creation.png?w=560&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=f0209dbb3aa364c2801d8c02bf2c834e 560w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-credential-creation.png?w=840&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=9d291f0dca191861c5eebc5236985bdd 840w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-credential-creation.png?w=1100&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=5bc5d64f6eb7398e83c264382064879f 1100w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-credential-creation.png?w=1650&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=c866783cc5819354b4f69f0e7e8acded 1650w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-credential-creation.png?w=2500&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=a4b7c6e4cf3d38e6898901f64556e16a 2500w" />
</div>

2. Under **Add new credential** select **Ollama**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-ollama-form.png?fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=46c5ec6678b7323405a1ca98d9f88af0" alt="Select Ollama under Credential" width="75%" data-og-width="1014" data-og-height="580" data-path="images/n8n-ollama-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-ollama-form.png?w=280&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=969d64d58c346578b68028e051ecee33 280w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-ollama-form.png?w=560&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=b5f84f26821ad5dbf1b05e01ce03fbcc 560w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-ollama-form.png?w=840&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=8f8b5b1301e0cc3e81ab32c839c52a89 840w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-ollama-form.png?w=1100&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=163156b985eca789a4cf2f441cf2b461 1100w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-ollama-form.png?w=1650&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=812d4591c0a3ebe160b6c78884ad487c 1650w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-ollama-form.png?w=2500&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=1ec83dd378b05cd17ac60bd9a4522e6c 2500w" />
</div>

3. Confirm Base URL is set to `http://localhost:11434` if running locally or `http://host.docker.internal:11434` if running through docker and click **Save**

<Note>
  In environments that don't use Docker Desktop (ie, Linux server installations), `host.docker.internal` is not automatically added.

  Run n8n in docker with `--add-host=host.docker.internal:host-gateway`

  or add the following to a docker compose file:

  ```yaml  theme={"system"}
  extra_hosts:
    - "host.docker.internal:host-gateway"
  ```
</Note>

You should see a `Connection tested successfully` message.

4. When creating a new workflow, select **Add a first step** and select an **Ollama node**

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-chat-node.png?fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=78c15518fa96d509096af63307063ae6" alt="Add a first step with Ollama node" width="75%" data-og-width="822" data-og-height="674" data-path="images/n8n-chat-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-chat-node.png?w=280&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=66a5f3201aae6a8ff315efe181fe5a36 280w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-chat-node.png?w=560&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=241b695dc152e97bc9992d2389c4c0cf 560w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-chat-node.png?w=840&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=be8484e52dab096ef1a2178a4d24e934 840w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-chat-node.png?w=1100&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=1be199b1714e4413d1d85fb5d679d6a1 1100w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-chat-node.png?w=1650&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=df82f732f724dd0079d62e39b519713a 1650w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-chat-node.png?w=2500&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=9f235598a4fade17b04c967e478f26a4 2500w" />
</div>

5. Select your model of choice (e.g. `qwen3-coder`)

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-models.png?fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=45e705696dc7c8f40112e1c6dbee0e7e" alt="Set up Ollama credentials" width="75%" data-og-width="1088" data-og-height="1058" data-path="images/n8n-models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-models.png?w=280&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=b0e7aede75a0098d023db708a37f9966 280w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-models.png?w=560&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=5786bf38961730b03e7415f9255c06d7 560w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-models.png?w=840&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=2182809e057f870dbf8f5b30b4069fe5 840w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-models.png?w=1100&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=6635c63c203627d6def2c398d22efeba 1100w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-models.png?w=1650&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=5715ed9f2bcf4157a29f77b59b0c69ae 1650w, https://mintcdn.com/ollama-9269c548/AZjkMSgDaM1B-WFi/images/n8n-models.png?w=2500&fit=max&auto=format&n=AZjkMSgDaM1B-WFi&q=85&s=cbb012310cc5a74f7e2616423bc4f902 2500w" />
</div>

## Connecting to ollama.com

1. Create an [API key](https://ollama.com/settings/keys) on **ollama.com**.
2. In n8n, click **Create Credential** and select **Ollama**
3. Set the **API URL** to `https://ollama.com`
4. Enter your **API Key** and click **Save**