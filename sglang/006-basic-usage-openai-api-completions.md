---
title: OpenAI APIs - Completions — SGLang
url: https://docs.sglang.io/basic_usage/openai_api_completions.html
source: crawler
fetched_at: 2026-02-04T08:47:34.000381187-03:00
rendered_js: false
word_count: 1129
summary: This document explains how to use SGLang's OpenAI-compatible APIs for chat and text completions, including server setup and client implementation.
tags:
    - sglang
    - openai-api
    - chat-completions
    - text-completions
    - llm-serving
    - self-hosted-models
category: tutorial
---

## OpenAI APIs - Completions[#](#OpenAI-APIs---Completions "Link to this heading")

SGLang provides OpenAI-compatible APIs to enable a smooth transition from OpenAI services to self-hosted local models. A complete reference for the API is available in the [OpenAI API Reference](https://platform.openai.com/docs/api-reference).

This tutorial covers the following popular APIs:

- `chat/completions`
- `completions`

Check out other tutorials to learn about [vision APIs](https://docs.sglang.io/basic_usage/openai_api_vision.html) for vision-language models and [embedding APIs](https://docs.sglang.io/basic_usage/openai_api_embeddings.html) for embedding models.

## Launch A Server[#](#Launch-A-Server "Link to this heading")

Launch the server in your terminal and wait for it to initialize.

```
fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport wait_for_server, print_highlight, terminate_process

server_process, port = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct --host 0.0.0.0 --log-level warning"
)

wait_for_server(f"http://localhost:{port}")
print(f"Server started on http://localhost:{port}")
```

```
[2026-02-04 11:26:42] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:42] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:42] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
[2026-02-04 11:26:49] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:49] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:49] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:52] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:26:52] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:26:58] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:58] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:58] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:58] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:58] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:58] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:27:04] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:04] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:27:04] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:27:04] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.68it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.67it/s]

Capturing batches (bs=1 avail_mem=76.29 GB): 100%|██████████| 3/3 [00:00<00:00,  3.76it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

```
Server started on http://localhost:33888
```

## Chat Completions[#](#Chat-Completions "Link to this heading")

### Usage[#](#Usage "Link to this heading")

The server fully implements the OpenAI API. It will automatically apply the chat template specified in the Hugging Face tokenizer, if one is available. You can also specify a custom chat template with `--chat-template` when launching the server.

```
importopenai

client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)

print_highlight(f"Response: {response}")
```

**Response: ChatCompletion(id='6d3fa1795eb6435ea4256487a5dba32e', choices=\[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Sure, here are three countries and their respective capitals:\\n\\n1. \*\*United States\** - Washington, D.C.\\n2. \*\*Canada\** - Ottawa\\n3. \*\*Australia\** - Canberra', refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=None, reasoning\_content=None), matched\_stop=151645)], created=1770204433, model='qwen/qwen2.5-0.5b-instruct', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=39, prompt\_tokens=37, total\_tokens=76, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

### Model Thinking/Reasoning Support[#](#Model-Thinking/Reasoning-Support "Link to this heading")

Some models support internal reasoning or thinking processes that can be exposed in the API response. SGLang provides unified support for various reasoning models through the `chat_template_kwargs` parameter and compatible reasoning parsers.

#### Supported Models and Configuration[#](#Supported-Models-and-Configuration "Link to this heading")

#### Basic Usage[#](#Basic-Usage "Link to this heading")

To enable reasoning output, you need to:

1. Launch the server with the appropriate reasoning parser
2. Set the model-specific parameter in `chat_template_kwargs`
3. Optionally use `separate_reasoning: False` to not get reasoning content separately (default to `True`)

**Note for Qwen3-Thinking models:** These models always generate thinking content and do not support the `enable_thinking` parameter. Use `--reasoning-parser qwen3-thinking` or `--reasoning-parser qwen3` to parse the thinking content.

#### Example: Qwen3 Models[#](#Example:-Qwen3-Models "Link to this heading")

```
# Launch server:
# python3 -m sglang.launch_server --model Qwen/Qwen3-4B --reasoning-parser qwen3

fromopenaiimport OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url=f"http://127.0.0.1:30000/v1",
)

model = "Qwen/Qwen3-4B"
messages = [{"role": "user", "content": "How many r's are in 'strawberry'?"}]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    extra_body={
        "chat_template_kwargs": {"enable_thinking": True},
        "separate_reasoning": True
    }
)

print("Reasoning:", response.choices[0].message.reasoning_content)
print("-"*100)
print("Answer:", response.choices[0].message.content)
```

**ExampleOutput:**

```
Reasoning: Okay, so the user is asking how many 'r's are in the word 'strawberry'. Let me think. First, I need to make sure I have the word spelled correctly. Strawberry... S-T-R-A-W-B-E-R-R-Y. Wait, is that right? Let me break it down.

Starting with 'strawberry', let's write out the letters one by one. S, T, R, A, W, B, E, R, R, Y. Hmm, wait, that's 10 letters. Let me check again. S (1), T (2), R (3), A (4), W (5), B (6), E (7), R (8), R (9), Y (10). So the letters are S-T-R-A-W-B-E-R-R-Y.
...
Therefore, the answer should be three R's in 'strawberry'. But I need to make sure I'm not counting any other letters as R. Let me check again. S, T, R, A, W, B, E, R, R, Y. No other R's. So three in total. Yeah, that seems right.

----------------------------------------------------------------------------------------------------
Answer: The word "strawberry" contains **three** letters 'r'. Here's the breakdown:

1. **S-T-R-A-W-B-E-R-R-Y**
   - The **third letter** is 'R'.
   - The **eighth and ninth letters** are also 'R's.

Thus, the total count is **3**.

**Answer:** 3.
```

**Note:** Setting `"enable_thinking": False` (or omitting it) will result in `reasoning_content` being `None`. Qwen3-Thinking models always generate reasoning content and don’t support the `enable_thinking` parameter.

#### Logit Bias Support[#](#Logit-Bias-Support "Link to this heading")

SGLang supports the `logit_bias` parameter for both chat completions and completions APIs. This parameter allows you to modify the likelihood of specific tokens being generated by adding bias values to their logits. The bias values can range from -100 to 100, where:

- **Positive values** (0 to 100) increase the likelihood of the token being selected
- **Negative values** (-100 to 0) decrease the likelihood of the token being selected
- **-100** effectively prevents the token from being generated

The `logit_bias` parameter accepts a dictionary where keys are token IDs (as strings) and values are the bias amounts (as floats).

#### Getting Token IDs[#](#Getting-Token-IDs "Link to this heading")

To use `logit_bias` effectively, you need to know the token IDs for the words you want to bias. Here’s how to get token IDs:

```
# Get tokenizer to find token IDs
importtiktoken

# For OpenAI models, use the appropriate encoding
tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")  # or your model

# Get token IDs for specific words
word = "sunny"
token_ids = tokenizer.encode(word)
print(f"Token IDs for '{word}': {token_ids}")

# For SGLang models, you can access the tokenizer through the client
# and get token IDs for bias
```

**Important:** The `logit_bias` parameter uses token IDs as string keys, not the actual words.

#### Example: DeepSeek-V3 Models[#](#Example:-DeepSeek-V3-Models "Link to this heading")

DeepSeek-V3 models support thinking mode through the `thinking` parameter:

```
# Launch server:
# python3 -m sglang.launch_server --model deepseek-ai/DeepSeek-V3.1 --tp 8  --reasoning-parser deepseek-v3

fromopenaiimport OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url=f"http://127.0.0.1:30000/v1",
)

model = "deepseek-ai/DeepSeek-V3.1"
messages = [{"role": "user", "content": "How many r's are in 'strawberry'?"}]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    extra_body={
        "chat_template_kwargs": {"thinking": True},
        "separate_reasoning": True
    }
)

print("Reasoning:", response.choices[0].message.reasoning_content)
print("-"*100)
print("Answer:", response.choices[0].message.content)
```

**Example Output:**

```
Reasoning: First, the question is: "How many r's are in 'strawberry'?"

I need to count the number of times the letter 'r' appears in the word "strawberry".

Let me write out the word: S-T-R-A-W-B-E-R-R-Y.

Now, I'll go through each letter and count the 'r's.
...
So, I have three 'r's in "strawberry".

I should double-check. The word is spelled S-T-R-A-W-B-E-R-R-Y. The letters are at positions: 3, 8, and 9 are 'r's. Yes, that's correct.

Therefore, the answer should be 3.
----------------------------------------------------------------------------------------------------
Answer: The word "strawberry" contains **3** instances of the letter "r". Here's a breakdown for clarity:

- The word is spelled: S-T-R-A-W-B-E-R-R-Y
- The "r" appears at the 3rd, 8th, and 9th positions.
```

**Note:** DeepSeek-V3 models use the `thinking` parameter (not `enable_thinking`) to control reasoning output.

```
# Example with logit_bias parameter
# Note: You need to get the actual token IDs from your tokenizer
# For demonstration, we'll use some example token IDs
response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[
        {"role": "user", "content": "Complete this sentence: The weather today is"}
    ],
    temperature=0.7,
    max_tokens=20,
    logit_bias={
        "12345": 50,  # Increase likelihood of token ID 12345
        "67890": -50,  # Decrease likelihood of token ID 67890
        "11111": 25,  # Slightly increase likelihood of token ID 11111
    },
)

print_highlight(f"Response with logit bias: {response.choices[0].message.content}")
```

**Response with logit bias: privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy**

### Parameters[#](#Parameters "Link to this heading")

The chat completions API accepts OpenAI Chat Completions API’s parameters. Refer to [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create) for more details.

SGLang extends the standard API with the `extra_body` parameter, allowing for additional customization. One key option within `extra_body` is `chat_template_kwargs`, which can be used to pass arguments to the chat template processor.

```
response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[
        {
            "role": "system",
            "content": "You are a knowledgeable historian who provides concise responses.",
        },
        {"role": "user", "content": "Tell me about ancient Rome"},
        {
            "role": "assistant",
            "content": "Ancient Rome was a civilization centered in Italy.",
        },
        {"role": "user", "content": "What were their major achievements?"},
    ],
    temperature=0.3,  # Lower temperature for more focused responses
    max_tokens=128,  # Reasonable length for a concise response
    top_p=0.95,  # Slightly higher for better fluency
    presence_penalty=0.2,  # Mild penalty to avoid repetition
    frequency_penalty=0.2,  # Mild penalty for more natural language
    n=1,  # Single response is usually more stable
    seed=42,  # Keep for reproducibility
)

print_highlight(response.choices[0].message.content)
```

**The ancient Roman civilization was renowned for its contributions to art, architecture, philosophy, law, and science. Some of their major achievements include:**

**1. Architecture: The Romans were known for their innovative architectural designs, which included the use of concrete and the construction of monumental buildings like the Colosseum and the Pantheon.**

**2. Art: Roman art was highly regarded, with a focus on sculpture, painting, and pottery. Famous works include the Venus de Milo and the marble statue of Nerva.**

**3. Philosophy: Roman philosophers such as Cicero, Seneca, and Quintus Ennius made significant contributions to philosophy, particularly**

Streaming mode is also supported.

#### Logit Bias Support[#](#id1 "Link to this heading")

The completions API also supports the `logit_bias` parameter with the same functionality as described in the chat completions section above.

```
stream = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

```
Yes, that is a test. I am Qwen, an artificial intelligence created by Alibaba Cloud. I am here to assist you with any questions or tasks you might have. If you have any questions or need help with anything, feel free to ask!
```

#### Returning Routed Experts (MoE Models)[#](#Returning-Routed-Experts-%28MoE-Models%29 "Link to this heading")

For MoE models, set `return_routed_experts: true` in `extra_body` to return expert routing data. Requires `--enable-return-routed-experts` server flag. The `routed_experts` field will be returned in the `sgl_ext` object on each choice, containing base64-encoded int32 expert IDs as a flattened array with logical shape `[num_tokens, num_layers, top_k]`.

```
# Example with logit_bias parameter for completions API
# Note: You need to get the actual token IDs from your tokenizer
# For demonstration, we'll use some example token IDs
response = client.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    prompt="The best programming language for AI is",
    temperature=0.7,
    max_tokens=20,
    logit_bias={
        "12345": 75,  # Strongly favor token ID 12345
        "67890": -100,  # Completely avoid token ID 67890
        "11111": -25,  # Slightly discourage token ID 11111
    },
)

print_highlight(f"Response with logit bias: {response.choices[0].text}")
```

**Response with logit bias: privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy privacy**

## Completions[#](#Completions "Link to this heading")

### Usage[#](#id2 "Link to this heading")

Completions API is similar to Chat Completions API, but without the `messages` parameter or chat templates.

```
response = client.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    prompt="List 3 countries and their capitals.",
    temperature=0,
    max_tokens=64,
    n=1,
    stop=None,
)

print_highlight(f"Response: {response}")
```

**Response: Completion(id='60ac37b908ae444686cfbc4d70a2f576', choices=\[CompletionChoice(finish\_reason='length', index=0, logprobs=None, text=' 1. United States - Washington D.C.\\n2. Canada - Ottawa\\n3. France - Paris\\n4. Germany - Berlin\\n5. Japan - Tokyo\\n6. Italy - Rome\\n7. Spain - Madrid\\n8. United Kingdom - London\\n9. Australia - Canberra\\n10. New Zealand', matched\_stop=None)], created=1770204434, model='qwen/qwen2.5-0.5b-instruct', object='text\_completion', system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=64, prompt\_tokens=8, total\_tokens=72, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

### Parameters[#](#id3 "Link to this heading")

The completions API accepts OpenAI Completions API’s parameters. Refer to [OpenAI Completions API](https://platform.openai.com/docs/api-reference/completions/create) for more details.

Here is an example of a detailed completions request:

```
response = client.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    prompt="Write a short story about a space explorer.",
    temperature=0.7,  # Moderate temperature for creative writing
    max_tokens=150,  # Longer response for a story
    top_p=0.9,  # Balanced diversity in word choice
    stop=["\n\n", "THE END"],  # Multiple stop sequences
    presence_penalty=0.3,  # Encourage novel elements
    frequency_penalty=0.3,  # Reduce repetitive phrases
    n=1,  # Generate one completion
    seed=123,  # For reproducible results
)

print_highlight(f"Response: {response}")
```

**Response: Completion(id='d6a0d16e6563420d8653670b0786e030', choices=\[CompletionChoice(finish\_reason='stop', index=0, logprobs=None, text=' Once upon a time, there was a space explorer named Dr. Sarah Reeves. She had always been fascinated by the stars and the mysteries of the universe. She spent her days traveling through space, exploring new planets and galaxies, and uncovering new knowledge about the cosmos.', matched\_stop='\\n\\n')], created=1770204434, model='qwen/qwen2.5-0.5b-instruct', object='text\_completion', system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=54, prompt\_tokens=9, total\_tokens=63, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

#### Returning Routed Experts (MoE Models)[#](#id4 "Link to this heading")

For MoE models, set `return_routed_experts: true` in `extra_body` to return expert routing data. Requires `--enable-return-routed-experts` server flag. The `routed_experts` field will be returned in the `sgl_ext` object on each choice, containing base64-encoded int32 expert IDs as a flattened array with logical shape `[num_tokens, num_layers, top_k]`.

## Structured Outputs (JSON, Regex, EBNF)[#](#Structured-Outputs-%28JSON,-Regex,-EBNF%29 "Link to this heading")

For OpenAI compatible structured outputs API, refer to [Structured Outputs](https://docs.sglang.io/advanced_features/structured_outputs.html) for more details.

## Using LoRA Adapters[#](#Using-LoRA-Adapters "Link to this heading")

SGLang supports LoRA (Low-Rank Adaptation) adapters with OpenAI-compatible APIs. You can specify which adapter to use directly in the `model` parameter using the `base-model:adapter-name` syntax.

**Server Setup:**

```
python-msglang.launch_server\
--model-pathqwen/qwen2.5-0.5b-instruct\
--enable-lora\
--lora-pathsadapter_a=/path/to/adapter_aadapter_b=/path/to/adapter_b
```

For more details on LoRA serving configuration, see the [LoRA documentation](https://docs.sglang.io/advanced_features/lora.html).

**API Call:**

(Recommended) Use the `model:adapter` syntax to specify which adapter to use:

```
response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct:adapter_a",  # ← base-model:adapter-name
    messages=[{"role": "user", "content": "Convert to SQL: show all users"}],
    max_tokens=50,
)
```

**Backward Compatible: Using \`\`extra\_body\`\`**

The old `extra_body` method is still supported for backward compatibility:

```
# Backward compatible method
response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[{"role": "user", "content": "Convert to SQL: show all users"}],
    extra_body={"lora_path": "adapter_a"},  # ← old method
    max_tokens=50,
)
```

**Note:** When both `model:adapter` and `extra_body["lora_path"]` are specified, the `model:adapter` syntax takes precedence.

```
terminate_process(server_process)
```