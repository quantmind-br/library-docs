---
title: Sampling Parameters - SGLang Documentation
url: https://docs.sglang.io/docs/basic_usage/sampling_params
source: sitemap
fetched_at: 2026-05-11T05:49:02.851908512-03:00
rendered_js: false
word_count: 1141
summary: This document provides a technical reference for the /generate endpoint parameters and sampling configurations within the SGLang runtime.
tags:
    - sglang
    - runtime
    - api-reference
    - sampling-parameters
    - constrained-decoding
    - llm-inference
category: reference
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This doc describes the sampling parameters of the SGLang Runtime. It is the low-level endpoint of the runtime. If you want a high-level endpoint that can automatically handle chat templates, consider using the [OpenAI Compatible API](https://docs.sglang.io/docs/basic_usage/openai_api_completions).

## `/generate` Endpoint

The `/generate` endpoint accepts the following parameters in JSON format. For detailed usage, see the [native API doc](https://docs.sglang.io/docs/basic_usage/native_api). The object is defined at `io_struct.py::GenerateReqInput`. You can also read the source code to find more arguments and docs.

ArgumentType/DefaultDescriptiontext`Optional[Union[List[str], str]] = None`The input prompt. Can be a single prompt or a batch of prompts.input\_ids`Optional[Union[List[List[int]], List[int]]] = None`The token IDs for text; one can specify either text or input\_ids.input\_embeds`Optional[Union[List[List[List[float]]], List[List[float]]]] = None`The embeddings for input\_ids; one can specify either text, input\_ids, or input\_embeds.image\_data`Optional[Union[List[List[ImageDataItem]], List[ImageDataItem], ImageDataItem]] = None`The image input. Supports three formats: (1) **Raw images**: PIL Image, file path, URL, or base64 string; (2) **Processor output**: Dict with `format: "processor_output"` containing HuggingFace processor outputs; (3) **Precomputed embeddings**: Dict with `format: "precomputed_embedding"` and `feature` containing pre-calculated visual embeddings. Can be a single image, list of images, or list of lists of images. See [Multimodal Input Formats](#multimodal-input-formats) for details.audio\_data`Optional[Union[List[AudioDataItem], AudioDataItem]] = None`The audio input. Can be a file name, URL, or base64 encoded string.sampling\_params`Optional[Union[List[Dict], Dict]] = None`The sampling parameters as described in the sections below.rid`Optional[Union[List[str], str]] = None`The request ID.return\_logprob`Optional[Union[List[bool], bool]] = None`Whether to return log probabilities for tokens.logprob\_start\_len`Optional[Union[List[int], int]] = None`If return\_logprob, the start location in the prompt for returning logprobs. Default is “-1”, which returns logprobs for output tokens only.top\_logprobs\_num`Optional[Union[List[int], int]] = None`If return\_logprob, the number of top logprobs to return at each position.token\_ids\_logprob`Optional[Union[List[List[int]], List[int]]] = None`If return\_logprob, the token IDs to return logprob for.return\_text\_in\_logprobs`bool = False`Whether to detokenize tokens in text in the returned logprobs.stream`bool = False`Whether to stream output.lora\_path`Optional[Union[List[Optional[str]], Optional[str]]] = None`The path to the LoRA.custom\_logit\_processor`Optional[Union[List[Optional[str]], str]] = None`Custom logit processor for advanced sampling control. Must be a serialized instance of `CustomLogitProcessor` using its `to_str()` method. For usage see below.return\_hidden\_states`Union[List[bool], bool] = False`Whether to return hidden states.return\_routed\_experts`bool = False`Whether to return routed experts for MoE models. Requires `--enable-return-routed-experts` server flag. With the default `routed_experts_start_len=0`, returns the full available sequence `[0, seqlen - 1)` because RL workflows need routed experts for the full sequence. The result is base64-encoded int32 expert IDs as a flattened array with logical shape `[num_tokens, num_layers, top_k]`.routed\_experts\_start\_len`int = 0`If `return_routed_experts`, the absolute start position for returned routed-experts rows. `0` preserves the default full sequence; set it to an accumulated prefix length to return only `[routed_experts_start_len, seqlen - 1)`. For example, in multi-turn RL rollouts, routed experts for tokens from previous turns have already been collected, so setting this value avoids unnecessary transfer that cause bottlenecks. Must be in `[0, prompt_tokens]`.

The object is defined at `sampling_params.py::SamplingParams`. You can also read the source code to find more arguments and docs.

### Note on defaults

By default, SGLang initializes several sampling parameters from the model’s `generation_config.json` (when the server is launched with `--sampling-defaults model`, which is the default). To use SGLang/OpenAI constant defaults instead, start the server with `--sampling-defaults openai`. You can always override any parameter per request via `sampling_params`.

```
# Use model-provided defaults from generation_config.json (default behavior)
python -m sglang.launch_server --model-path <MODEL> --sampling-defaults model

# Use SGLang/OpenAI constant defaults instead
python -m sglang.launch_server --model-path <MODEL> --sampling-defaults openai
```

### Core parameters

ArgumentType/DefaultDescriptionmax\_new\_tokens`int = 128`The maximum output length measured in tokens.stop`Optional[Union[str, List[str]]] = None`One or multiple [stop words](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stop). Generation will stop if one of these words is sampled.stop\_token\_ids`Optional[List[int]] = None`Provide stop words in the form of token IDs. Generation will stop if one of these token IDs is sampled.stop\_regex`Optional[Union[str, List[str]]] = None`Stop when hitting any of the regex patterns in this listtemperature`float (model default; fallback 1.0)`[Temperature](https://platform.openai.com/docs/api-reference/chat/create#chat-create-temperature) when sampling the next token. `temperature = 0` corresponds to greedy sampling, a higher temperature leads to more diversity.top\_p`float (model default; fallback 1.0)`[Top-p](https://platform.openai.com/docs/api-reference/chat/create#chat-create-top_p) selects tokens from the smallest sorted set whose cumulative probability exceeds `top_p`. When `top_p = 1`, this reduces to unrestricted sampling from all tokens.top\_k`int (model default; fallback -1)`[Top-k](https://developer.nvidia.com/blog/how-to-get-better-outputs-from-your-large-language-model/#predictability_vs_creativity) randomly selects from the `k` highest-probability tokens.min\_p`float (model default; fallback 0.0)`[Min-p](https://github.com/huggingface/transformers/issues/27670) samples from tokens with probability larger than `min_p * highest_token_probability`.

### Penalizers

ArgumentType/DefaultDescriptionfrequency\_penalty`float = 0.0`Penalizes tokens based on their frequency in generation so far. Must be between `-2` and `2` where negative numbers encourage repeatment of tokens and positive number encourages sampling of new tokens. The scaling of penalization grows linearly with each appearance of a token.presence\_penalty`float = 0.0`Penalizes tokens if they appeared in the generation so far. Must be between `-2` and `2` where negative numbers encourage repeatment of tokens and positive number encourages sampling of new tokens. The scaling of the penalization is constant if a token occurred.repetition\_penalty`float = 1.0`Scales the logits of previously generated tokens to discourage (values &gt; 1) or encourage (values &lt; 1) repetition. Valid range is `[0, 2]`; `1.0` leaves probabilities unchanged.min\_new\_tokens`int = 0`Forces the model to generate at least `min_new_tokens` until a stop word or EOS token is sampled. Note that this might lead to unintended behavior, for example, if the distribution is highly skewed towards these tokens.

### Constrained decoding

Please refer to our dedicated guide on [constrained decoding](https://docs.sglang.io/docs/advanced_features/structured_outputs) for the following parameters.

ArgumentType/DefaultDescriptionjson\_schema`Optional[str] = None`JSON schema for structured outputs.regex`Optional[str] = None`Regex for structured outputs.ebnf`Optional[str] = None`EBNF for structured outputs.structural\_tag`Optional[str] = None`The structal tag for structured outputs.

### Other options

ArgumentType/DefaultDescriptionn`int = 1`Specifies the number of output sequences to generate per request. (Generating multiple outputs in one request (n &gt; 1) is discouraged; repeating the same prompts several times offers better control and efficiency.)ignore\_eos`bool = False`Don’t stop generation when EOS token is sampled.skip\_special\_tokens`bool = True`Remove special tokens during decoding.spaces\_between\_special\_tokens`bool = True`Whether or not to add spaces between special tokens during detokenization.no\_stop\_trim`bool = False`Don’t trim stop words or EOS token from the generated text.custom\_params`Optional[List[Optional[Dict[str, Any]]]] = None`Used when employing `CustomLogitProcessor`. For usage, see below.

## Examples

### Normal

Launch a server:

```
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct --port 30000
```

Send a request:

```
import requests

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

Detailed example in [send request](https://docs.sglang.io/docs/basic_usage/send_request).

### Streaming

Send a request and stream the output:

```
import requests, json

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

Detailed example in [openai compatible api](https://docs.sglang.io/docs/basic_usage/openai_api_completions).

### Multimodal

Launch a server:

```
python3 -m sglang.launch_server --model-path lmms-lab/llava-onevision-qwen2-7b-ov
```

Download an image:

```
curl -o example_image.png -L https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true
```

Send a request:

```
import requests

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

The `image_data` can be a file name, a URL, or a base64 encoded string. See also `python/sglang/srt/utils.py:load_image`. Streaming is supported in a similar manner as [above](#streaming). Detailed example in [OpenAI API Vision](https://docs.sglang.io/docs/basic_usage/openai_api_vision).

### Structured Outputs (JSON, Regex, EBNF)

You can specify a JSON schema, regular expression or [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) to constrain the model output. The model output will be guaranteed to follow the given constraints. Only one constraint parameter (`json_schema`, `regex`, or `ebnf`) can be specified for a request. SGLang supports two grammar backends:

- [XGrammar](https://github.com/mlc-ai/xgrammar) (default): Supports JSON schema, regular expression, and EBNF constraints.
  
  - XGrammar currently uses the [GGML BNF format](https://github.com/ggerganov/llama.cpp/blob/master/grammars/README).
- [Outlines](https://github.com/dottxt-ai/outlines): Supports JSON schema and regular expression constraints.

If instead you want to initialize the Outlines backend, you can use `--grammar-backend outlines` flag:

```
python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-8B-Instruct \
--port 30000 --host 0.0.0.0 --grammar-backend [xgrammar|outlines] # xgrammar or outlines (default: xgrammar)

import json
import requests

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

Detailed example in [structured outputs](https://docs.sglang.io/docs/advanced_features/structured_outputs).

### Custom logit processor

Launch a server with `--enable-custom-logit-processor` flag on.

```
python -m sglang.launch_server \
  --model-path meta-llama/Meta-Llama-3-8B-Instruct \
  --port 30000 \
  --enable-custom-logit-processor
```

Define a custom logit processor that will always sample a specific token id.

```
from sglang.srt.sampling.custom_logit_processor import CustomLogitProcessor

class DeterministicLogitProcessor(CustomLogitProcessor):
    """A dummy logit processor that changes the logits to always
    sample the given token id.
    """

    def __call__(self, logits, custom_param_list):
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
import requests

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
import openai
from sglang.utils import print_highlight

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