---
title: Llava — Large Language and Vision Assistant | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-llava
source: crawler
fetched_at: 2026-04-24T17:01:25.910115816-03:00
rendered_js: false
word_count: 50
summary: This document explains the functionality and usage of LLava, an open-source vision-language model designed for image-based conversations. It provides code examples demonstrating visual question answering, instruction following across multiple turns, and deployment using frameworks like Gradio.
tags:
    - vision-language
    - llava-model
    - conversational-chat
    - image-understanding
    - instruction-tuning
    - pytorch-example
category: tutorial
---

Large Language and Vision Assistant. Enables visual instruction tuning and image-based conversations. Combines CLIP vision encoder with Vicuna/LLaMA language models. Supports multi-turn image chat, visual question answering, and instruction following. Use for vision-language chatbots or image understanding tasks. Best for conversational image analysis.

Open-source vision-language model for conversational image understanding.

```python
from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path, process_images, tokenizer_image_token
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN
from llava.conversation import conv_templates
from PIL import Image
import torch

# Load model
model_path ="liuhaotian/llava-v1.5-7b"
tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=get_model_name_from_path(model_path)
)

# Load image
image = Image.open("image.jpg")
image_tensor = process_images([image], image_processor, model.config)
image_tensor = image_tensor.to(model.device, dtype=torch.float16)

# Create conversation
conv = conv_templates["llava_v1"].copy()
conv.append_message(conv.roles[0], DEFAULT_IMAGE_TOKEN +"\nWhat is in this image?")
conv.append_message(conv.roles[1],None)
prompt = conv.get_prompt()

# Generate response
input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).to(model.device)

with torch.inference_mode():
    output_ids = model.generate(
        input_ids,
        images=image_tensor,
        do_sample=True,
        temperature=0.2,
        max_new_tokens=512
)

response = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
print(response)
```

```python
# Load different models
model_7b ="liuhaotian/llava-v1.5-7b"
model_13b ="liuhaotian/llava-v1.5-13b"
model_34b ="liuhaotian/llava-v1.6-34b"

# 4-bit quantization for lower VRAM
load_4bit =True# Reduces VRAM by ~4×
```

```python
# Initialize conversation
conv = conv_templates["llava_v1"].copy()

# Turn 1
conv.append_message(conv.roles[0], DEFAULT_IMAGE_TOKEN +"\nWhat is in this image?")
conv.append_message(conv.roles[1],None)
response1 = generate(conv, model, image)# "A dog playing in a park"

# Turn 2
conv.messages[-1][1]= response1  # Add previous response
conv.append_message(conv.roles[0],"What breed is the dog?")
conv.append_message(conv.roles[1],None)
response2 = generate(conv, model, image)# "Golden Retriever"

# Turn 3
conv.messages[-1][1]= response2
conv.append_message(conv.roles[0],"What time of day is it?")
conv.append_message(conv.roles[1],None)
response3 = generate(conv, model, image)
```

```python
question ="Describe this image in detail."
response = ask(model, image, question)
```

```python
question ="How many people are in the image?"
response = ask(model, image, question)
```

```python
question ="List all the objects you can see in this image."
response = ask(model, image, question)
```

```python
question ="What is happening in this scene?"
response = ask(model, image, question)
```

```python
question ="What is the main topic of this document?"
response = ask(model, document_image, question)
```

```python
# 4-bit quantization
tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path="liuhaotian/llava-v1.5-13b",
    model_base=None,
    model_name=get_model_name_from_path("liuhaotian/llava-v1.5-13b"),
    load_4bit=True# Reduces VRAM ~4×
)

# 8-bit quantization
load_8bit=True# Reduces VRAM ~2×
```

```python
from langchain.llms.base import LLM

classLLaVALLM(LLM):
def_call(self, prompt, stop=None):
# Custom LLaVA inference
return response

llm = LLaVALLM()
```

```python
import gradio as gr

defchat(image, text, history):
    response = ask_llava(model, image, text)
return response

demo = gr.ChatInterface(
    chat,
    additional_inputs=[gr.Image(type="pil")],
    title="LLaVA Chat"
)
demo.launch()
```