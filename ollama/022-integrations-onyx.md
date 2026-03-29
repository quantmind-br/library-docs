---
title: Onyx
url: https://docs.ollama.com/integrations/onyx.md
source: llms
fetched_at: 2026-02-04T11:34:38.117601437-03:00
rendered_js: false
word_count: 292
summary: This document introduces Onyx, a self-hostable chat interface, and provides instructions on how to connect it with Ollama for features like RAG and agentic workflows.
tags:
    - onyx
    - ollama
    - chat-ui
    - self-hosted
    - rag
    - llm-integration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ollama.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Onyx

## Overview

[Onyx](http://onyx.app/) is a self-hostable Chat UI that integrates with all Ollama models. Features include:

* Creating custom Agents
* Web search
* Deep Research
* RAG over uploaded documents and connected apps
* Connectors to applications like Google Drive, Email, Slack, etc.
* MCP and OpenAPI Actions support
* Image generation
* User/Groups management, RBAC, SSO, etc.

Onyx can be deployed for single users or large organizations.

## Install Onyx

Deploy Onyx with the [quickstart guide](https://docs.onyx.app/deployment/getting_started/quickstart).

<Info>
  Resourcing/scaling docs [here](https://docs.onyx.app/deployment/getting_started/resourcing).
</Info>

## Usage with Ollama

1. Login to your Onyx deployment (create an account first).

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-login.png?fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=5850db0abbfca50c1b6eb5029648ae89" alt="Onyx Login Page" width="75%" data-og-width="1042" data-og-height="1174" data-path="images/onyx-login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-login.png?w=280&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=5088b73d1da8902a03fbb75ef58775f2 280w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-login.png?w=560&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=fcaa0a552584366d72838ccee250b602 560w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-login.png?w=840&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=1f6397ac7b144042e7eabf225a17e742 840w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-login.png?w=1100&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=68ee5850ea4a167896a8e8321306d541 1100w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-login.png?w=1650&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=8adfbd131c4f19be8d4d1c2328467f97 1650w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-login.png?w=2500&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=637b7072a3e278ffd6dd629f21af45c4 2500w" />
</div>

2. In the set-up process select `Ollama` as the LLM provider.

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-llm.png?fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=399b5938d0d0d18b359845529dd9408b" alt="Onyx Set Up Form" width="75%" data-og-width="1676" data-og-height="1278" data-path="images/onyx-ollama-llm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-llm.png?w=280&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=530bd27c54055cb76a85fc9e1181d12c 280w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-llm.png?w=560&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=2dbf7cd530c6205d556cfec4156626b8 560w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-llm.png?w=840&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=a11855aa45c3e283b1021e0ffd67cb73 840w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-llm.png?w=1100&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=871c407d1207631516f8a107589104e7 1100w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-llm.png?w=1650&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=fb3ce5e3867b08096a476cd777b82c22 1650w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-llm.png?w=2500&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=2423616af0d516cfdd133baeac736268 2500w" />
</div>

3. Provide your **Ollama API URL** and select your models.
   <Note>If you're running Onyx in Docker, to access your computer's local network use `http://host.docker.internal` instead of `http://127.0.0.1`.</Note>

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-form.png?fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=f675da3f8a399614b549f72d6adaa798" alt="Selecting Ollama Models" width="75%" data-og-width="1676" data-og-height="1278" data-path="images/onyx-ollama-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-form.png?w=280&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=831c11fdb4845c25306388f54f1a9c8b 280w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-form.png?w=560&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=a00038193163e44b847a9d4259861373 560w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-form.png?w=840&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=c8f09a50d2c3539386e7fcd4ebc29b37 840w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-form.png?w=1100&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=fab9e9521c1838961d39b857df3ddb05 1100w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-form.png?w=1650&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=0b1d114865ec21d16dc418d2573eeb39 1650w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-ollama-form.png?w=2500&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=6f66979be90cfdc0331923e1e699bfe4 2500w" />
</div>

You can also easily connect up Onyx Cloud with the `Ollama Cloud` tab of the setup.

## Send your first query

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <img src="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-query.png?fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=3e7b6e38fb14b288d72bcd828cdd91d9" alt="Onyx Query Example" width="75%" data-og-width="1322" data-og-height="1760" data-path="images/onyx-query.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-query.png?w=280&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=fff0dff5e6bb5ce3c46fa2b96f5db9ba 280w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-query.png?w=560&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=c5973bdf6cdeecb9138c8ac0b5aa20b7 560w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-query.png?w=840&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=ba2c183519e6e1ea016b2cf8ba21a5aa 840w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-query.png?w=1100&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=88b8cf609049b2b5df41dad825d08f07 1100w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-query.png?w=1650&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=5cf1cc53a898754f944371ccd17d3538 1650w, https://mintcdn.com/ollama-9269c548/rqi257JWXmZRsZn4/images/onyx-query.png?w=2500&fit=max&auto=format&n=rqi257JWXmZRsZn4&q=85&s=626f829d87a364c6ba557e7a66a37da2 2500w" />
</div>