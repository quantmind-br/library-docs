---
title: Prompt Embed - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/prompt_embed/
source: sitemap
fetched_at: 2026-05-07T21:12:57.928875742-03:00
rendered_js: false
word_count: 319
summary: This document provides examples and best practices for performing inference in vLLM using pre-calculated prompt embeddings instead of raw text inputs.
tags:
    - vllm
    - prompt-embeddings
    - inference
    - openai-api
    - machine-learning
    - embeddings
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/prompt_embed.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/prompt\_embed](https://github.com/vllm-project/vllm/tree/main/examples/features/prompt_embed).

## Prompt Embed Inference With OpenAI Client[¶](#prompt-embed-inference-with-openai-client "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""vLLM OpenAI-Compatible Client with Prompt Embeddings.

This script demonstrates how to:
1. Generate prompt embeddings using Hugging Face Transformers.
2. Encode them in base64 format.
3. Send them to a vLLM server for inference via both:
    - OpenAI-compatible Chat Completions API
    - OpenAI-compatible Completions API

Important distinction between the two APIs:

- Chat Completions API: `prompt_embeds` content parts should encode ONLY
  the user-provided content, not a templated conversation. The server
  renders the surrounding chat template around the embedded content at
  request time, the same way it would for a plain text `content` string.
  Embedding a full templated conversation here would double-apply the
  template and likely produce undesirable results.

- Completions API: the server does NOT apply a chat template to
  `prompt_embeds`. The caller is responsible for producing embeddings for
  the full, already-templated prompt (i.e. apply the chat template first, 
  then embed the resulting token IDs). Anything the model would normally
  need (system prompt, role markers, generation prompt, etc.) must already
  be baked into the embedded tokens.

Run the vLLM server first:
vllm serve meta-llama/Llama-3.2-1B-Instruct \
  --runner generate \
  --max-model-len 4096 \
  --enable-prompt-embeds

Run the client:
python examples/features/prompt_embed/prompt_embed_inference_with_openai_client.py

Model: meta-llama/Llama-3.2-1B-Instruct
Note: This model is gated on Hugging Face Hub.
      You must request access to use it:
      https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

Dependencies:
- transformers
- torch
- openai
"""

importtransformers
fromopenaiimport OpenAI

fromvllm.utils.serial_utilsimport tensor2base64


defrun_chat_completion_prompt_embeds(
    client: OpenAI,
    model_name: str,
    tokenizer: transformers.PreTrainedTokenizerBase,
    embedding_layer,
    messages: list[dict],
) -> None:
"""Run a Chat Completions API request using prompt_embeds content parts.

    This example embeds ONLY the user-provided content of the final user turn, the
    vLLM server applies the chat template around it at request time.
    """
    user_content = messages[-1]["content"]
    content_token_ids = tokenizer(
        user_content, return_tensors="pt", add_special_tokens=False
    ).input_ids
    content_prompt_embeds = embedding_layer(content_token_ids).squeeze(0)
    encoded_embeds = tensor2base64(content_prompt_embeds)

    api_messages = [
        *messages[:-1],
        {
            "role": messages[-1]["role"],
            "content": [{"type": "prompt_embeds", "data": encoded_embeds}],
        },
    ]

    chat_completion = client.chat.completions.create(
        model=model_name,
        max_tokens=6,
        temperature=0.0,
        messages=api_messages,
    )

    print("-" * 30)
    print("Chat Completions API")
    print(chat_completion.choices[0].message.content)
    print("-" * 30)


defrun_completion_prompt_embeds(
    client: OpenAI,
    model_name: str,
    tokenizer: transformers.PreTrainedTokenizerBase,
    embedding_layer,
    messages: list[dict],
) -> None:
"""Run a Completions API request using prompt embeddings.

    The Completions endpoint does not apply a chat template,
    so the caller must apply it and embed the full templated prompt.
    """
    templated_token_ids = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
    ).input_ids
    templated_prompt_embeds = embedding_layer(templated_token_ids).squeeze(0)
    encoded_embeds = tensor2base64(templated_prompt_embeds)

    completion = client.completions.create(
        model=model_name,
        prompt=None,
        max_tokens=6,
        temperature=0.0,
        # NOTE: The OpenAI client allows passing in extra JSON body via the
        # `extra_body` argument.
        extra_body={"prompt_embeds": encoded_embeds},
    )

    print("-" * 30)
    print("Completions API")
    print(completion.choices[0].text)
    print("-" * 30)


defmain() -> None:
    client = OpenAI(
        api_key="EMPTY",
        base_url="http://localhost:8000/v1",
    )

    model_name = "meta-llama/Llama-3.2-1B-Instruct"

    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    transformers_model = transformers.AutoModelForCausalLM.from_pretrained(model_name)
    embedding_layer = transformers_model.get_input_embeddings()

    messages = [
        {"role": "user", "content": "Please tell me about the capital of France."}
    ]

    # Chat Completions API: embed ONLY the user content. The server wraps
    # the embedding in the chat template when it renders the messages.
    run_chat_completion_prompt_embeds(
        client, model_name, tokenizer, embedding_layer, messages
    )

    # Completions API: embed the FULL templated prompt. The caller must
    # apply the chat template up-front.
    run_completion_prompt_embeds(
        client, model_name, tokenizer, embedding_layer, messages
    )


if __name__ == "__main__":
    main()
```

## Prompt Embed Offline[¶](#prompt-embed-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Demonstrates how to generate prompt embeddings using
Hugging Face Transformers  and use them as input to vLLM
for both single and batch inference.

Model: meta-llama/Llama-3.2-1B-Instruct
Note: This model is gated on Hugging Face Hub.
      You must request access to use it:
      https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

Requirements:
- vLLM
- transformers

Run:
    python examples/features/prompt_embed/prompt_embed_offline.py
"""

importtorch
fromtransformersimport AutoModelForCausalLM, AutoTokenizer, PreTrainedTokenizer

fromvllmimport LLM


definit_tokenizer_and_llm(model_name: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    transformers_model = AutoModelForCausalLM.from_pretrained(model_name)
    embedding_layer = transformers_model.get_input_embeddings()
    llm = LLM(model=model_name, enable_prompt_embeds=True)
    return tokenizer, embedding_layer, llm


defget_prompt_embeds(
    chat: list[dict[str, str]],
    tokenizer: PreTrainedTokenizer,
    embedding_layer: torch.nn.Module,
):
    token_ids = tokenizer.apply_chat_template(
        chat, add_generation_prompt=True, return_tensors="pt", return_dict=True
    ).input_ids
    prompt_embeds = embedding_layer(token_ids).squeeze(0)
    return prompt_embeds


defsingle_prompt_inference(
    llm: LLM, tokenizer: PreTrainedTokenizer, embedding_layer: torch.nn.Module
):
    chat = [{"role": "user", "content": "Please tell me about the capital of France."}]
    prompt_embeds = get_prompt_embeds(chat, tokenizer, embedding_layer)

    outputs = llm.generate(
        {
            "prompt_embeds": prompt_embeds,
        }
    )

    print("\n[Single Inference Output]")
    print("-" * 30)
    for o in outputs:
        print(o.outputs[0].text)
    print("-" * 30)


defbatch_prompt_inference(
    llm: LLM, tokenizer: PreTrainedTokenizer, embedding_layer: torch.nn.Module
):
    chats = [
        [{"role": "user", "content": "Please tell me about the capital of France."}],
        [{"role": "user", "content": "When is the day longest during the year?"}],
        [{"role": "user", "content": "Where is bigger, the moon or the sun?"}],
    ]

    prompt_embeds_list = [
        get_prompt_embeds(chat, tokenizer, embedding_layer) for chat in chats
    ]

    outputs = llm.generate([{"prompt_embeds": embeds} for embeds in prompt_embeds_list])

    print("\n[Batch Inference Outputs]")
    print("-" * 30)
    for i, o in enumerate(outputs):
        print(f"Q{i+1}: {chats[i][0]['content']}")
        print(f"A{i+1}: {o.outputs[0].text}\n")
    print("-" * 30)


defmain():
    model_name = "meta-llama/Llama-3.2-1B-Instruct"
    tokenizer, embedding_layer, llm = init_tokenizer_and_llm(model_name)
    single_prompt_inference(llm, tokenizer, embedding_layer)
    batch_prompt_inference(llm, tokenizer, embedding_layer)


if __name__ == "__main__":
    main()
```