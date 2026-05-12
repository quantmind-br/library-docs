---
title: Streamlit - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/streamlit/
source: sitemap
fetched_at: 2026-05-07T21:11:56.472346748-03:00
rendered_js: false
word_count: 88
summary: This document provides instructions on integrating the vLLM inference engine with Streamlit to create interactive chat applications using the OpenAI-compatible API.
tags:
    - vllm
    - streamlit
    - llm-deployment
    - chatbot
    - api-integration
    - python
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/streamlit.md "Edit this page")

[Streamlit](https://github.com/streamlit/streamlit) lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps.

It can be quickly integrated with vLLM as a backend API server, enabling powerful LLM inference via API calls.

## Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM environment by installing all required packages:

```
pipinstallvllmstreamlitopenai
```

## Deploy[¶](#deploy "Permanent link")

1. Start the vLLM server with a supported chat completion model, e.g.
   
   ```
   vllmserveQwen/Qwen1.5-0.5B-Chat
   ```
2. Use the script: [examples/online\_serving/streamlit\_openai\_chatbot\_webserver.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/streamlit_openai_chatbot_webserver.py)
3. Start the streamlit web UI and start to chat:
   
   ```
   streamlitrunstreamlit_openai_chatbot_webserver.py
   
   # or specify the VLLM_API_BASE or VLLM_API_KEY
   VLLM_API_BASE="http://vllm-server-host:vllm-server-port/v1"\
   streamlitrunstreamlit_openai_chatbot_webserver.py
   
   # start with debug mode to view more details
   streamlitrunstreamlit_openai_chatbot_webserver.py--logger.level=debug
   ```
   
   [![Chat with vLLM assistant in Streamlit](https://docs.vllm.ai/en/latest/assets/deployment/streamlit-chat.png)](https://docs.vllm.ai/en/latest/assets/deployment/streamlit-chat.png)