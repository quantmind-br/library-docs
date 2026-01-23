---
title: Gradio Chatbot + LiteLLM Tutorial | liteLLM
url: https://docs.litellm.ai/docs/tutorials/gradio_integration
source: sitemap
fetched_at: 2026-01-21T19:55:27.439693235-03:00
rendered_js: false
word_count: 26
summary: This document provides a brief tutorial on integrating LiteLLM streaming completion calls into a Gradio-based chatbot interface.
tags:
    - litellm
    - gradio
    - chatbot
    - streaming
    - python
    - llm-integration
category: tutorial
---

Simple tutorial for integrating LiteLLM completion calls with streaming Gradio chatbot demos

Remember to set `model` and `api_base` as expected by the server hosting your LLM.

```
definference(message, history):
try:
        flattened_history =[item for sublist in history for item in sublist]
        full_message =" ".join(flattened_history +[message])
        messages_litellm =[{"role":"user","content": full_message}]# litellm message format
        partial_message =""
for chunk in litellm.completion(model="huggingface/meta-llama/Llama-2-7b-chat-hf",
                                        api_base="x.x.x.x:xxxx",
                                        messages=messages_litellm,
                                        max_new_tokens=512,
                                        temperature=.7,
                                        top_k=100,
                                        top_p=.9,
                                        repetition_penalty=1.18,
                                        stream=True):
            partial_message += chunk['choices'][0]['delta']['content']# extract text from streamed litellm chunks
yield partial_message
except Exception as e:
print("Exception encountered:",str(e))
yieldf"An Error occurred please 'Clear' the error and try your question again"
```

```
gr.ChatInterface(
    inference,
    chatbot=gr.Chatbot(height=400),
    textbox=gr.Textbox(placeholder="Enter text here...", container=False, scale=5),
    description=f"""
    CURRENT PROMPT TEMPLATE: {model_name}.
    An incorrect prompt template will cause performance to suffer.
    Check the API specifications to ensure this format matches the target LLM.""",
    title="Simple Chatbot Test Application",
    examples=["Define 'deep learning' in once sentence."],
    retry_btn="Retry",
    undo_btn="Undo",
    clear_btn="Clear",
    theme=theme,
).queue().launch()
```