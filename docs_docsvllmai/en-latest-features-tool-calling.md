---
title: Tool Calling - vLLM
url: https://docs.vllm.ai/en/latest/features/tool_calling/
source: sitemap
fetched_at: 2026-05-07T21:14:18.866522206-03:00
rendered_js: false
word_count: 2391
summary: This document explains how to implement and configure tool calling functionality in vLLM, including support for automatic, required, named, and disabled tool selection modes.
tags:
    - vllm
    - tool-calling
    - function-calling
    - api-integration
    - structured-outputs
    - llm-inference
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/tool_calling.md "Edit this page")

vLLM currently supports named function calling, as well as the `auto`, `required` (as of `vllm>=0.8.3`), and `none` options for the `tool_choice` field in the chat completion API.

## Quickstart[¶](#quickstart "Permanent link")

Start the server with tool calling enabled. This example uses Meta's Llama 3.1 8B model, so we need to use the `llama3_json` tool calling chat template from the vLLM examples directory:

```
vllmservemeta-llama/Llama-3.1-8B-Instruct\
--enable-auto-tool-choice\
--tool-call-parserllama3_json\
--chat-templateexamples/tool_chat_template_llama3.1_json.jinja
```

Next, make a request that triggers the model to use the available tools:

Code

```
fromopenaiimport OpenAI
importjson

client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

defget_weather(location: str, unit: str):
    return f"Getting the weather for {location} in {unit}..."
tool_functions = {"get_weather": get_weather}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location", "unit"],
            },
        },
    },
]

response = client.chat.completions.create(
    model=client.models.list().data[0].id,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=tools,
    tool_choice="auto",
)

tool_call = response.choices[0].message.tool_calls[0].function
print(f"Function called: {tool_call.name}")
print(f"Arguments: {tool_call.arguments}")
print(f"Result: {tool_functions[tool_call.name](**json.loads(tool_call.arguments))}")
```

Example output:

```
Function called: get_weather
Arguments: {"location": "San Francisco, CA", "unit": "fahrenheit"}
Result: Getting the weather for San Francisco, CA in fahrenheit...
```

This example demonstrates:

- Setting up the server with tool calling enabled
- Defining an actual function to handle tool calls
- Making a request with `tool_choice="auto"`
- Handling the structured response and executing the corresponding function

You can also specify a particular function using named function calling by setting `tool_choice={"type": "function", "function": {"name": "get_weather"}}`. Note that this will use the structured outputs backend - so the first time this is used, there will be several seconds of latency (or more) as the FSM is compiled for the first time before it is cached for subsequent requests.

Remember that it's the caller's responsibility to:

1. Define appropriate tools in the request
2. Include relevant context in the chat messages
3. Handle the tool calls in your application logic

For more advanced usage, including parallel tool calls and different model-specific parsers, see the sections below.

## Named Function Calling[¶](#named-function-calling "Permanent link")

vLLM supports named function calling in the chat completion API by default. This should work with most structured outputs backends supported by vLLM. You are guaranteed a validly-parsable function call - not a high-quality one.

vLLM will use structured outputs to ensure the response matches the tool parameter object defined by the JSON schema in the `tools` parameter. For best results, we recommend ensuring that the expected output format / schema is specified in the prompt to ensure that the model's intended generation is aligned with the schema that it's being forced to generate by the structured outputs backend.

To use a named function, you need to define the functions in the `tools` parameter of the chat completion request, and specify the `name` of one of the tools in the `tool_choice` parameter of the chat completion request.

## Required Function Calling[¶](#required-function-calling "Permanent link")

vLLM supports the `tool_choice='required'` option in the chat completion API. Similar to the named function calling, it also uses structured outputs, so this is enabled by default and will work with any supported model. However, support for alternative decoding backends are on the [roadmap](https://docs.vllm.ai/en/latest/usage/v1_guide/#features) for the V1 engine.

When tool\_choice='required' is set, the model is guaranteed to generate one or more tool calls based on the specified tool list in the `tools` parameter. The number of tool calls depends on the user's query. The output format strictly follows the schema defined in the `tools` parameter.

## None Function Calling[¶](#none-function-calling "Permanent link")

vLLM supports the `tool_choice='none'` option in the chat completion API. When this option is set, the model will not generate any tool calls and will respond with regular text content only, even if tools are defined in the request.

Note

When tools are specified in the request, vLLM includes tool definitions in the prompt by default, regardless of the `tool_choice` setting. To exclude tool definitions when `tool_choice='none'`, use the `--exclude-tools-when-tool-choice-none` option.

## Constrained Decoding Behavior[¶](#constrained-decoding-behavior "Permanent link")

Whether vLLM enforces the tool parameter schema during generation depends on the `tool_choice` mode:

`tool_choice` value Schema-constrained decoding Behavior Named function Yes (via structured outputs backend) Arguments are guaranteed to be valid JSON conforming to the function's parameter schema. `"required"` Yes (via structured outputs backend) Same as named function. The model must produce at least one tool call. `"auto"` No The model generates freely. A tool-call parser extracts tool calls from the raw text. Arguments may be malformed or not match the schema. `"none"` N/A No tool calls are produced.

When schema conformance matters, prefer `tool_choice="required"` or named function calling over `"auto"`.

### Strict Mode (`strict` parameter)[¶](#strict-mode-strict-parameter "Permanent link")

The [OpenAI API](https://platform.openai.com/docs/guides/function-calling#strict-mode) supports a `strict` field on function definitions. When set to `true`, OpenAI uses constrained decoding to guarantee that tool-call arguments match the function schema, even in `tool_choice="auto"` mode.

vLLM **does not implement** `strict` mode today. The `strict` field is accepted in requests (to avoid breaking clients that set it), but it has no effect on decoding behavior. In auto mode, argument validity depends entirely on the model's output quality and the parser's extraction logic.

Tracking issues: [#15526](https://github.com/vllm-project/vllm/issues/15526), [#16313](https://github.com/vllm-project/vllm/issues/16313).

## Automatic Function Calling[¶](#automatic-function-calling "Permanent link")

To enable this feature, you should set the following flags:

- `--enable-auto-tool-choice` -- **mandatory** Auto tool choice. It tells vLLM that you want to enable the model to generate its own tool calls when it deems appropriate.
- `--tool-call-parser` -- select the tool parser to use (listed below). Additional tool parsers will continue to be added in the future. You can also register your own tool parsers in the `--tool-parser-plugin`.
- `--tool-parser-plugin` -- **optional** tool parser plugin used to register user defined tool parsers into vllm, the registered tool parser name can be specified in `--tool-call-parser`.
- `--chat-template` -- **optional** for auto tool choice. It's the path to the chat template which handles `tool`-role messages and `assistant`-role messages that contain previously generated tool calls. Hermes, Mistral and Llama models have tool-compatible chat templates in their `tokenizer_config.json` files, but you can specify a custom template. This argument can be set to `tool_use` if your model has a tool use-specific chat template configured in the `tokenizer_config.json`. In this case, it will be used per the `transformers` specification. More on this [here](https://huggingface.co/docs/transformers/en/chat_templating#why-do-some-models-have-multiple-templates) from HuggingFace; and you can find an example of this in a `tokenizer_config.json` [here](https://huggingface.co/NousResearch/Hermes-2-Pro-Llama-3-8B/blob/main/tokenizer_config.json).

If your favorite tool-calling model is not supported, please feel free to contribute a parser & tool use chat template!

Note

With `tool_choice="auto"`, tool-call arguments are extracted from the model's raw text output by the selected parser. No schema-level constraint is applied during decoding, so arguments may occasionally be malformed or violate the function's parameter schema. See [Constrained Decoding Behavior](#constrained-decoding-behavior) for details.

### Hermes Models (`hermes`)[¶](#hermes-models-hermes "Permanent link")

All Nous Research Hermes-series models newer than Hermes 2 Pro should be supported.

- `NousResearch/Hermes-2-Pro-*`
- `NousResearch/Hermes-2-Theta-*`
- `NousResearch/Hermes-3-*`

*Note that the Hermes 2 **Theta** models are known to have degraded tool call quality and capabilities due to the merge step in their creation*.

Flags: `--tool-call-parser hermes`

### Mistral Models (`mistral`)[¶](#mistral-models-mistral "Permanent link")

Supported models:

- `mistralai/Mistral-7B-Instruct-v0.3` (confirmed)
- Additional Mistral function-calling models are compatible as well.

Known issues:

1. Mistral 7B struggles to generate parallel tool calls correctly.
2. **For Transformers tokenization backend only**: Mistral's `tokenizer_config.json` chat template requires tool call IDs that are exactly 9 digits, which is much shorter than what vLLM generates. Since an exception is thrown when this condition is not met, the following additional chat templates are provided:
   
   - [examples/tool\_chat\_template\_mistral.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_mistral.jinja) - this is the "official" Mistral chat template, but tweaked so that it works with vLLM's tool call IDs (provided `tool_call_id` fields are truncated to the last 9 digits)
   - [examples/tool\_chat\_template\_mistral\_parallel.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_mistral_parallel.jinja) - this is a "better" version that adds a tool-use system prompt when tools are provided, that results in much better reliability when working with parallel tool calling.

Recommended flags:

1. To use the official Mistral AI's format:
   
   `--tool-call-parser mistral`
2. To use the Transformers format when available:
   
   `--tokenizer_mode hf --config_format hf --load_format hf --tool-call-parser mistral --chat-template examples/tool_chat_template_mistral_parallel.jinja`

Note

Models officially released by Mistral AI have two possible formats:

1. The official format that is used by default with `auto` or `mistral` arguments:
   
   `--tokenizer_mode mistral --config_format mistral --load_format mistral` This format uses [mistral-common](https://github.com/mistralai/mistral-common), the Mistral AI's tokenizer backend.
2. The Transformers format, when available, that is used with `hf` arguments:
   
   `--tokenizer_mode hf --config_format hf --load_format hf --chat-template examples/tool_chat_template_mistral_parallel.jinja`

### Llama Models (`llama3_json`)[¶](#llama-models-llama3_json "Permanent link")

Supported models:

All Llama 3.1, 3.2 and 4 models should be supported.

- `meta-llama/Llama-3.1-*`
- `meta-llama/Llama-3.2-*`
- `meta-llama/Llama-4-*`

The tool calling that is supported is the [JSON-based tool calling](https://llama.meta.com/docs/model-cards-and-prompt-formats/llama3_1/#json-based-tool-calling). For [pythonic tool calling](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/text_prompt_format.md#zero-shot-function-calling) introduced by the Llama-3.2 models, see the `pythonic` tool parser below. As for Llama 4 models, it is recommended to use the `llama4_pythonic` tool parser.

Other tool calling formats like the built-in python tool calling or custom tool calling are not supported.

Known issues:

1. Parallel tool calls are not supported for Llama 3, but it is supported in Llama 4 models.
2. The model can generate parameters in an incorrect format, such as generating an array serialized as string instead of an array.

VLLM provides two JSON-based chat templates for Llama 3.1 and 3.2:

- [examples/tool\_chat\_template\_llama3.1\_json.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama3.1_json.jinja) - this is the "official" chat template for the Llama 3.1 models, but tweaked so that it works better with vLLM.
- [examples/tool\_chat\_template\_llama3.2\_json.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama3.2_json.jinja) - this extends upon the Llama 3.1 chat template by adding support for images.

Recommended flags: `--tool-call-parser llama3_json --chat-template {see_above}`

VLLM also provides a pythonic and JSON-based chat template for Llama 4, but pythonic tool calling is recommended:

- [examples/tool\_chat\_template\_llama4\_pythonic.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama4_pythonic.jinja) - this is based on the [official chat template](https://www.llama.com/docs/model-cards-and-prompt-formats/llama4/) for the Llama 4 models.

For Llama 4 model, use `--tool-call-parser llama4_pythonic --chat-template examples/tool_chat_template_llama4_pythonic.jinja`.

### IBM Granite[¶](#ibm-granite "Permanent link")

Supported models:

- `ibm-granite/granite-4.0-h-small` and other Granite 4.0 models
  
  Recommended flags: `--tool-call-parser granite4`
- `ibm-granite/granite-3.0-8b-instruct`
  
  Recommended flags: `--tool-call-parser granite --chat-template examples/tool_chat_template_granite.jinja`
  
  [examples/tool\_chat\_template\_granite.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_granite.jinja): this is a modified chat template from the original on Hugging Face. Parallel function calls are supported.
- `ibm-granite/granite-3.1-8b-instruct`
  
  Recommended flags: `--tool-call-parser granite`
  
  The chat template from Huggingface can be used directly. Parallel function calls are supported.
- `ibm-granite/granite-20b-functioncalling`
  
  Recommended flags: `--tool-call-parser granite-20b-fc --chat-template examples/tool_chat_template_granite_20b_fc.jinja`
  
  [examples/tool\_chat\_template\_granite\_20b\_fc.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_granite_20b_fc.jinja): this is a modified chat template from the original on Hugging Face, which is not vLLM-compatible. It blends function description elements from the Hermes template and follows the same system prompt as "Response Generation" mode from [the paper](https://arxiv.org/abs/2407.00121). Parallel function calls are supported.

### InternLM Models (`internlm`)[¶](#internlm-models-internlm "Permanent link")

Supported models:

- `internlm/internlm2_5-7b-chat` (confirmed)
- Additional internlm2.5 function-calling models are compatible as well

Known issues:

- Although this implementation also supports InternLM2, the tool call results are not stable when testing with the `internlm/internlm2-chat-7b` model.

Recommended flags: `--tool-call-parser internlm --chat-template examples/tool_chat_template_internlm2_tool.jinja`

### Jamba Models (`jamba`)[¶](#jamba-models-jamba "Permanent link")

AI21's Jamba-1.5 models are supported.

- `ai21labs/AI21-Jamba-1.5-Mini`
- `ai21labs/AI21-Jamba-1.5-Large`

Flags: `--tool-call-parser jamba`

### xLAM Models (`xlam`)[¶](#xlam-models-xlam "Permanent link")

The xLAM tool parser is designed to support models that generate tool calls in various JSON formats. It detects function calls in several different output styles:

1. Direct JSON arrays: Output strings that are JSON arrays starting with `[` and ending with `]`
2. Thinking tags: Using `<think>...</think>` tags containing JSON arrays
3. Code blocks: JSON in code blocks (`json ...`)
4. Tool calls tags: Using `[TOOL_CALLS]` or `<tool_call>...</tool_call>` tags

Parallel function calls are supported, and the parser can effectively separate text content from tool calls.

Supported models:

- Salesforce Llama-xLAM models: `Salesforce/Llama-xLAM-2-8B-fc-r`, `Salesforce/Llama-xLAM-2-70B-fc-r`
- Qwen-xLAM models: `Salesforce/xLAM-1B-fc-r`, `Salesforce/xLAM-3B-fc-r`, `Salesforce/Qwen-xLAM-32B-fc-r`

Flags:

- For Llama-based xLAM models: `--tool-call-parser xlam --chat-template examples/tool_chat_template_xlam_llama.jinja`
- For Qwen-based xLAM models: `--tool-call-parser xlam --chat-template examples/tool_chat_template_xlam_qwen.jinja`

### Qwen Models[¶](#qwen-models "Permanent link")

For Qwen2.5, the chat template in tokenizer\_config.json has already included support for the Hermes-style tool use. Therefore, you can use the `hermes` parser to enable tool calls for Qwen models. For more detailed information, please refer to the official [Qwen documentation](https://qwen.readthedocs.io/en/latest/framework/function_call.html#vllm)

- `Qwen/Qwen2.5-*`
- `Qwen/QwQ-32B`

Flags: `--tool-call-parser hermes`

### MiniMax Models (`minimax_m1`)[¶](#minimax-models-minimax_m1 "Permanent link")

Supported models:

- `MiniMaxAi/MiniMax-M1-40k` (use with [examples/tool\_chat\_template\_minimax\_m1.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_minimax_m1.jinja))
- `MiniMaxAi/MiniMax-M1-80k` (use with [examples/tool\_chat\_template\_minimax\_m1.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_minimax_m1.jinja))

Flags: `--tool-call-parser minimax --chat-template examples/tool_chat_template_minimax_m1.jinja`

### DeepSeek-V3 Models (`deepseek_v3`)[¶](#deepseek-v3-models-deepseek_v3 "Permanent link")

Supported models:

- `deepseek-ai/DeepSeek-V3-0324` (use with [examples/tool\_chat\_template\_deepseekv3.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_deepseekv3.jinja))
- `deepseek-ai/DeepSeek-R1-0528` (use with [examples/tool\_chat\_template\_deepseekr1.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_deepseekr1.jinja))

Flags: `--tool-call-parser deepseek_v3 --chat-template {see_above}`

### DeepSeek-V3.1 Models (`deepseek_v31`)[¶](#deepseek-v31-models-deepseek_v31 "Permanent link")

Supported models:

- `deepseek-ai/DeepSeek-V3.1` (use with [examples/tool\_chat\_template\_deepseekv31.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_deepseekv31.jinja))

Flags: `--tool-call-parser deepseek_v31 --chat-template {see_above}`

### OpenAI OSS Models ('openai\`)[¶](#openai-oss-models-openai "Permanent link")

Supported models:

- `openai/gpt-oss-20b`
- `openai/gpt-oss-120b`

Flags: `--tool-call-parser openai`

### Kimi-K2 Models (`kimi_k2`)[¶](#kimi-k2-models-kimi_k2 "Permanent link")

Supported models:

- `moonshotai/Kimi-K2-Instruct`

Flags: `--tool-call-parser kimi_k2`

### Hunyuan Models (`hunyuan_a13b`)[¶](#hunyuan-models-hunyuan_a13b "Permanent link")

Supported models:

- `tencent/Hunyuan-A13B-Instruct` (The chat template is already included in the Hugging Face model files.)

Flags:

- For non-reasoning: `--tool-call-parser hunyuan_a13b`
- For reasoning: `--tool-call-parser hunyuan_a13b --reasoning-parser hunyuan_a13b`

### Cohere Command A Reasoning (`cohere_command3`)[¶](#cohere-command-a-reasoning-cohere_command3 "Permanent link")

Supported models:

- [`CohereLabs/command-a-reasoning-08-2025`](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025)

Flags: `--tool-call-parser cohere_command3 --reasoning-parser cohere_command3`

Note: the Cohere tool parser requires the `cohere_melody` package, which is not installed by default. Before using this parser please install the [cohere\_melody](https://pypi.org/project/cohere-melody/) package.

### LongCat-Flash-Chat Models (`longcat`)[¶](#longcat-flash-chat-models-longcat "Permanent link")

Supported models:

- `meituan-longcat/LongCat-Flash-Chat`
- `meituan-longcat/LongCat-Flash-Chat-FP8`

Flags: `--tool-call-parser longcat`

### GLM-4.5 Models (`glm45`)[¶](#glm-45-models-glm45 "Permanent link")

Supported models:

- `zai-org/GLM-4.5`
- `zai-org/GLM-4.5-Air`
- `zai-org/GLM-4.6`

Flags: `--tool-call-parser glm45`

### GLM-4.7 Models (`glm47`)[¶](#glm-47-models-glm47 "Permanent link")

Supported models:

- `zai-org/GLM-4.7`
- `zai-org/GLM-4.7-Flash`

Flags: `--tool-call-parser glm47`

### FunctionGemma Models (`functiongemma`)[¶](#functiongemma-models-functiongemma "Permanent link")

Google's FunctionGemma is a lightweight (270M parameter) model specifically designed for function calling. It's built on Gemma 3 and optimized for edge deployment on devices like laptops and phones.

Supported models:

- `google/functiongemma-270m-it`

FunctionGemma uses a unique output format with `<start_function_call>` and `<end_function_call>` tags:

```
<start_function_call>call:get_weather{location:<escape>London<escape>}<end_function_call>
```

The model is designed to be fine-tuned for specific function-calling tasks for best results.

Flags: `--tool-call-parser functiongemma --chat-template examples/tool_chat_template_functiongemma.jinja`

Note

FunctionGemma is intended to be fine-tuned for your specific function-calling task. The base model provides general function calling capabilities, but best results are achieved with task-specific fine-tuning. See Google's [FunctionGemma documentation](https://ai.google.dev/gemma/docs/functiongemma) for fine-tuning guides.

### Qwen3-Coder Models (`qwen3_xml`)[¶](#qwen3-coder-models-qwen3_xml "Permanent link")

Supported models:

- `Qwen/Qwen3-Coder-480B-A35B-Instruct`
- `Qwen/Qwen3-Coder-30B-A3B-Instruct`

Flags: `--tool-call-parser qwen3_xml`

### Olmo 3 Models (`olmo3`)[¶](#olmo-3-models-olmo3 "Permanent link")

Olmo 3 models output tool calls in a format that is very similar to the one expected by the `pythonic` parser (see below), with a few differences. Each tool call is a pythonic string, but the parallel tool calls are newline-delimited, and the calls are wrapped within XML tags as `<function_calls>..</function_calls>`. In addition, the parser also allows JSON boolean and null literals (`true`, `false`, and `null`) in addition to the pythonic ones (`True`, `False`, and `None`).

Supported models:

- `allenai/Olmo-3-7B-Instruct`
- `allenai/Olmo-3-32B-Think`

Flags: `--tool-call-parser olmo3`

### Gigachat 3 Models (`gigachat3`)[¶](#gigachat-3-models-gigachat3 "Permanent link")

Use chat template from the Hugging Face model files.

Supported models:

- `ai-sage/GigaChat3-702B-A36B-preview`
- `ai-sage/GigaChat3-702B-A36B-preview-bf16`
- `ai-sage/GigaChat3-10B-A1.8B`
- `ai-sage/GigaChat3-10B-A1.8B-bf16`

Flags: `--tool-call-parser gigachat3`

### Models with Pythonic Tool Calls (`pythonic`)[¶](#models-with-pythonic-tool-calls-pythonic "Permanent link")

A growing number of models output a python list to represent tool calls instead of using JSON. This has the advantage of inherently supporting parallel tool calls and removing ambiguity around the JSON schema required for tool calls. The `pythonic` tool parser can support such models.

As a concrete example, these models may look up the weather in San Francisco and Seattle by generating:

```
[get_weather(city='San Francisco', metric='celsius'), get_weather(city='Seattle', metric='celsius')]
```

Limitations:

- The model must not generate both text and tool calls in the same generation. This may not be hard to change for a specific model, but the community currently lacks consensus on which tokens to emit when starting and ending tool calls. (In particular, the Llama 3.2 models emit no such tokens.)
- Llama's smaller models struggle to use tools effectively.

Example supported models:

- `meta-llama/Llama-3.2-1B-Instruct` ⚠️ (use with [examples/tool\_chat\_template\_llama3.2\_pythonic.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama3.2_pythonic.jinja))
- `meta-llama/Llama-3.2-3B-Instruct` ⚠️ (use with [examples/tool\_chat\_template\_llama3.2\_pythonic.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama3.2_pythonic.jinja))
- `Team-ACE/ToolACE-8B` (use with [examples/tool\_chat\_template\_toolace.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_toolace.jinja))
- `fixie-ai/ultravox-v0_4-ToolACE-8B` (use with [examples/tool\_chat\_template\_toolace.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_toolace.jinja))
- `meta-llama/Llama-4-Scout-17B-16E-Instruct` ⚠️ (use with [examples/tool\_chat\_template\_llama4\_pythonic.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama4_pythonic.jinja))
- `meta-llama/Llama-4-Maverick-17B-128E-Instruct` ⚠️ (use with [examples/tool\_chat\_template\_llama4\_pythonic.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama4_pythonic.jinja))

Flags: `--tool-call-parser pythonic --chat-template {see_above}`

Warning

Llama's smaller models frequently fail to emit tool calls in the correct format. Results may vary depending on the model.

A tool parser plugin is a Python file containing one or more ToolParser implementations. You can write a ToolParser similar to the `Hermes2ProToolParser` in [vllm/tool\_parsers/hermes\_tool\_parser.py](https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/hermes_tool_parser.py).

Here is a summary of a plugin file:

Code

```
# import the required packages

# define a tool parser and register it to vllm
# the name list in register_module can be used
# in --tool-call-parser. you can define as many
# tool parsers as you want here.
classExampleToolParser(ToolParser):
    def__init__(self, tokenizer: TokenizerLike):
        super().__init__(tokenizer)

    # adjust request. e.g.: set skip special tokens
    # to False for tool call output.
    defadjust_request(self, request: ChatCompletionRequest | ResponsesRequest) -> ChatCompletionRequest | ResponsesRequest:
        return request

    # implement the tool call parse for stream call
    defextract_tool_calls_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
        request: ChatCompletionRequest,
    ) -> DeltaMessage | None:
        return delta

    # implement the tool parse for non-stream call
    defextract_tool_calls(
        self,
        model_output: str,
        request: ChatCompletionRequest,
    ) -> ExtractedToolCallInformation:
        return ExtractedToolCallInformation(tools_called=False,
                                            tool_calls=[],
                                            content=text)
# register the tool parser to ToolParserManager
ToolParserManager.register_lazy_module(
    name="example",
    module_path="vllm.tool_parsers.example",
    class_name="ExampleToolParser",
)
```

Then you can use this plugin in the command line like this.

```
--enable-auto-tool-choice\
--tool-parser-plugin<absolutepathofthepluginfile>
--tool-call-parserexample\
--chat-template<yourchattemplate>\
```