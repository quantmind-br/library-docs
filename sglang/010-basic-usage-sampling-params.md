---
title: Sampling Parameters — SGLang
url: https://docs.sglang.io/basic_usage/sampling_params.html
source: crawler
fetched_at: 2026-02-04T08:46:43.206362436-03:00
rendered_js: false
word_count: 362
summary: This document explains the sampling parameters and usage of the SGLang Runtime /generate endpoint, including configuration for constrained decoding, multimodal inputs, and custom logit processors.
tags:
    - sglang
    - sampling-parameters
    - inference-api
    - constrained-decoding
    - structured-outputs
    - llm-inference
category: api
---

## Sampling Parameters[#](#sampling-parameters "Link to this heading")

This doc describes the sampling parameters of the SGLang Runtime. It is the low-level endpoint of the runtime. If you want a high-level endpoint that can automatically handle chat templates, consider using the [OpenAI Compatible API](https://docs.sglang.io/basic_usage/openai_api_completions.html).

## `/generate` Endpoint[#](#generate-endpoint "Link to this heading")

The `/generate` endpoint accepts the following parameters in JSON format. For detailed usage, see the [native API doc](https://docs.sglang.io/basic_usage/native_api.html). The object is defined at `io_struct.py::GenerateReqInput`. You can also read the source code to find more arguments and docs.

## Sampling parameters[#](#id1 "Link to this heading")

The object is defined at `sampling_params.py::SamplingParams`. You can also read the source code to find more arguments and docs.

### Note on defaults[#](#note-on-defaults "Link to this heading")

By default, SGLang initializes several sampling parameters from the model’s `generation_config.json` (when the server is launched with `--sampling-defaults model`, which is the default). To use SGLang/OpenAI constant defaults instead, start the server with `--sampling-defaults openai`. You can always override any parameter per request via `sampling_params`.

```
# Use model-provided defaults from generation_config.json (default behavior)
python-msglang.launch_server--model-path<MODEL>--sampling-defaultsmodel

# Use SGLang/OpenAI constant defaults instead
python-msglang.launch_server--model-path<MODEL>--sampling-defaultsopenai
```

### Core parameters[#](#core-parameters "Link to this heading")

### Penalizers[#](#penalizers "Link to this heading")

### Constrained decoding[#](#constrained-decoding "Link to this heading")

Please refer to our dedicated guide on [constrained decoding](https://docs.sglang.io/advanced_features/structured_outputs.html) for the following parameters.

### Other options[#](#other-options "Link to this heading")

## Examples[#](#examples "Link to this heading")

### Normal[#](#normal "Link to this heading")

Launch a server:

```
python-msglang.launch_server--model-pathmeta-llama/Meta-Llama-3-8B-Instruct--port30000
```

Send a request:

```
importrequests

response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "The capital of France is",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 32,
        },
    },
)
print(response.json())
```

Detailed example in [send request](https://docs.sglang.io/basic_usage/send_request.html).

### Streaming[#](#streaming "Link to this heading")

Send a request and stream the output:

```
importrequests,json

response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "The capital of France is",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 32,
        },
        "stream": True,
    },
    stream=True,
)

prev = 0
for chunk in response.iter_lines(decode_unicode=False):
    chunk = chunk.decode("utf-8")
    if chunk and chunk.startswith("data:"):
        if chunk == "data: [DONE]":
            break
        data = json.loads(chunk[5:].strip("\n"))
        output = data["text"].strip()
        print(output[prev:], end="", flush=True)
        prev = len(output)
print("")
```

Detailed example in [openai compatible api](https://docs.sglang.io/basic_usage/openai_api_completions.html).

### Multimodal[#](#multimodal "Link to this heading")

Launch a server:

```
python3-msglang.launch_server--model-pathlmms-lab/llava-onevision-qwen2-7b-ov
```

Download an image:

```
curl-oexample_image.png-Lhttps://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true
```

Send a request:

```
importrequests

response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
                "<|im_start|>user\n<image>\nDescribe this image in a very short sentence.<|im_end|>\n"
                "<|im_start|>assistant\n",
        "image_data": "example_image.png",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 32,
        },
    },
)
print(response.json())
```

The `image_data` can be a file name, a URL, or a base64 encoded string. See also `python/sglang/srt/utils.py:load_image`.

Streaming is supported in a similar manner as [above](#streaming).

Detailed example in [OpenAI API Vision](https://docs.sglang.io/basic_usage/openai_api_vision.html).

### Structured Outputs (JSON, Regex, EBNF)[#](#structured-outputs-json-regex-ebnf "Link to this heading")

You can specify a JSON schema, regular expression or [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) to constrain the model output. The model output will be guaranteed to follow the given constraints. Only one constraint parameter (`json_schema`, `regex`, or `ebnf`) can be specified for a request.

SGLang supports two grammar backends:

- [XGrammar](https://github.com/mlc-ai/xgrammar) (default): Supports JSON schema, regular expression, and EBNF constraints.
  
  - XGrammar currently uses the [GGML BNF format](https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md).
- [Outlines](https://github.com/dottxt-ai/outlines): Supports JSON schema and regular expression constraints.

If instead you want to initialize the Outlines backend, you can use `--grammar-backend outlines` flag:

```
python-msglang.launch_server--model-pathmeta-llama/Meta-Llama-3.1-8B-Instruct\
--port30000--host0.0.0.0--grammar-backend[xgrammar|outlines]# xgrammar or outlines (default: xgrammar)
```

```
importjson
importrequests

json_schema = json.dumps({
    "type": "object",
    "properties": {
        "name": {"type": "string", "pattern": "^[\\w]+$"},
        "population": {"type": "integer"},
    },
    "required": ["name", "population"],
})

# JSON (works with both Outlines and XGrammar)
response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "Here is the information of the capital of France in the JSON format.\n",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 64,
            "json_schema": json_schema,
        },
    },
)
print(response.json())

# Regular expression (Outlines backend only)
response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "Paris is the capital of",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 64,
            "regex": "(France|England)",
        },
    },
)
print(response.json())

# EBNF (XGrammar backend only)
response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "Write a greeting.",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 64,
            "ebnf": 'root ::= "Hello" | "Hi" | "Hey"',
        },
    },
)
print(response.json())
```

Detailed example in [structured outputs](https://docs.sglang.io/advanced_features/structured_outputs.html).

### Custom logit processor[#](#custom-logit-processor "Link to this heading")

Launch a server with `--enable-custom-logit-processor` flag on.

```
python-msglang.launch_server\
--model-pathmeta-llama/Meta-Llama-3-8B-Instruct\
--port30000\
--enable-custom-logit-processor
```

Define a custom logit processor that will always sample a specific token id.

```
fromsglang.srt.sampling.custom_logit_processorimport CustomLogitProcessor

classDeterministicLogitProcessor(CustomLogitProcessor):
"""A dummy logit processor that changes the logits to always
    sample the given token id.
    """

    def__call__(self, logits, custom_param_list):
        # Check that the number of logits matches the number of custom parameters
        assert logits.shape[0] == len(custom_param_list)
        key = "token_id"

        for i, param_dict in enumerate(custom_param_list):
            # Mask all other tokens
            logits[i, :] = -float("inf")
            # Assign highest probability to the specified token
            logits[i, param_dict[key]] = 0.0
        return logits
```

Send a request:

```
importrequests

response = requests.post(
    "http://localhost:30000/generate",
    json={
        "text": "The capital of France is",
        "custom_logit_processor": DeterministicLogitProcessor().to_str(),
        "sampling_params": {
            "temperature": 0.0,
            "max_new_tokens": 32,
            "custom_params": {"token_id": 5},
        },
    },
)
print(response.json())
```

Send an OpenAI chat completion request:

```
importopenai
fromsglang.utilsimport print_highlight

client = openai.Client(base_url="http://127.0.0.1:30000/v1", api_key="None")

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0.0,
    max_tokens=32,
    extra_body={
        "custom_logit_processor": DeterministicLogitProcessor().to_str(),
        "custom_params": {"token_id": 5},
    },
)

print_highlight(f"Response: {response}")
```