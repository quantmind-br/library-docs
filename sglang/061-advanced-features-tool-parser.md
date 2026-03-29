---
title: Tool Parser — SGLang
url: https://docs.sglang.io/advanced_features/tool_parser.html
source: crawler
fetched_at: 2026-02-04T08:46:49.007610916-03:00
rendered_js: false
word_count: 2673
summary: This document explains how to implement and configure function calling in SGLang using various tool parsers and the OpenAI-compatible API. It covers launching the server with specific model parsers and defining tool schemas for model interaction.
tags:
    - sglang
    - function-calling
    - tool-parser
    - openai-api
    - llm-inference
    - server-configuration
category: guide
---

## Tool Parser[#](#Tool-Parser "Link to this heading")

This guide demonstrates how to use SGLang’s [Function calling](https://platform.openai.com/docs/guides/function-calling) functionality.

## Currently supported parsers:[#](#Currently-supported-parsers: "Link to this heading")

## OpenAI Compatible API[#](#OpenAI-Compatible-API "Link to this heading")

### Launching the Server[#](#Launching-the-Server "Link to this heading")

```
importjson
fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport wait_for_server, print_highlight, terminate_process
fromopenaiimport OpenAI

server_process, port = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path Qwen/Qwen2.5-7B-Instruct --tool-call-parser qwen25 --host 0.0.0.0 --log-level warning"  # qwen25
)
wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:24:12] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:24:12] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:24:12] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
[2026-02-04 11:24:17] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:24:17] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:24:17] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:24:18] WARNING server_args.py:825: The tool_call_parser 'qwen25' is deprecated. Please use 'qwen' instead.
[2026-02-04 11:24:20] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:24:20] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:24:26] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:24:26] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:24:26] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:24:26] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:24:26] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:24:26] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:24:32] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:24:32] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:24:32] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:24:32] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:02<00:07,  2.66s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:05<00:05,  2.58s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:07<00:02,  2.65s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:10<00:00,  2.54s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:10<00:00,  2.57s/it]

Capturing batches (bs=1 avail_mem=45.33 GB): 100%|██████████| 3/3 [00:00<00:00,  4.63it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

Note that `--tool-call-parser` defines the parser used to interpret responses.

### Define Tools for Function Call[#](#Define-Tools-for-Function-Call "Link to this heading")

Below is a Python snippet that shows how to define a tool as a dictionary. The dictionary includes a tool name, a description, and property defined Parameters.

```
# Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "the two-letter abbreviation for the state that the city is"
                        " in, e.g. 'CA' which would mean 'California'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "state", "unit"],
            },
        },
    }
]
```

### Define Messages[#](#Define-Messages "Link to this heading")

```
defget_messages():
    return [
        {
            "role": "user",
            "content": "What's the weather like in Boston today? Output a reasoning before act, then use the tools to help you.",
        }
    ]


messages = get_messages()
```

### Initialize the Client[#](#Initialize-the-Client "Link to this heading")

```
# Initialize OpenAI-like client
client = OpenAI(api_key="None", base_url=f"http://0.0.0.0:{port}/v1")
model_name = client.models.list().data[0].id
```

### Non-Streaming Request[#](#Non-Streaming-Request "Link to this heading")

```
# Non-streaming mode test
response_non_stream = client.chat.completions.create(
    model=model_name,
    messages=messages,
    temperature=0,
    top_p=0.95,
    max_tokens=1024,
    stream=False,  # Non-streaming
    tools=tools,
)
print_highlight("Non-stream response:")
print_highlight(response_non_stream)
print_highlight("==== content ====")
print_highlight(response_non_stream.choices[0].message.content)
print_highlight("==== tool_calls ====")
print_highlight(response_non_stream.choices[0].message.tool_calls)
```

**ChatCompletion(id='bfe2298aa50a47b397d476bc6d9314cf', choices=\[Choice(finish\_reason='tool\_calls', index=0, logprobs=None, message=ChatCompletionMessage(content="To determine the current weather in Boston, I will use the \`get\_current\_weather\` function by providing the city name, state, and unit for temperature. Boston is located in Massachusetts, so the state abbreviation is 'MA'. For the temperature unit, since it's not specified, I will provide both Celsius and Fahrenheit options to give you a comprehensive view.", refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=\[ChatCompletionMessageFunctionToolCall(id='call\_f7b870f5ad7b42f0ad44bd6d', function=Function(arguments='{"city": "Boston", "state": "MA", "unit": "celsius"}', name='get\_current\_weather'), type='function', index=0), ChatCompletionMessageFunctionToolCall(id='call\_2e368354e151428a8d8df62f', function=Function(arguments='{"city": "Boston", "state": "MA", "unit": "fahrenheit"}', name='get\_current\_weather'), type='function', index=0)], reasoning\_content=None), matched\_stop=None)], created=1770204293, model='Qwen/Qwen2.5-7B-Instruct', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=139, prompt\_tokens=281, total\_tokens=420, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

**To determine the current weather in Boston, I will use the \`get\_current\_weather\` function by providing the city name, state, and unit for temperature. Boston is located in Massachusetts, so the state abbreviation is 'MA'. For the temperature unit, since it's not specified, I will provide both Celsius and Fahrenheit options to give you a comprehensive view.**

**\[ChatCompletionMessageFunctionToolCall(id='call\_f7b870f5ad7b42f0ad44bd6d', function=Function(arguments='{"city": "Boston", "state": "MA", "unit": "celsius"}', name='get\_current\_weather'), type='function', index=0), ChatCompletionMessageFunctionToolCall(id='call\_2e368354e151428a8d8df62f', function=Function(arguments='{"city": "Boston", "state": "MA", "unit": "fahrenheit"}', name='get\_current\_weather'), type='function', index=0)]**

#### Handle Tools[#](#Handle-Tools "Link to this heading")

When the engine determines it should call a particular tool, it will return arguments or partial arguments through the response. You can parse these arguments and later invoke the tool accordingly.

```
name_non_stream = response_non_stream.choices[0].message.tool_calls[0].function.name
arguments_non_stream = (
    response_non_stream.choices[0].message.tool_calls[0].function.arguments
)

print_highlight(f"Final streamed function call name: {name_non_stream}")
print_highlight(f"Final streamed function call arguments: {arguments_non_stream}")
```

**Final streamed function call name: get\_current\_weather**

**Final streamed function call arguments: {"city": "Boston", "state": "MA", "unit": "celsius"}**

### Streaming Request[#](#Streaming-Request "Link to this heading")

```
# Streaming mode test
print_highlight("Streaming response:")
response_stream = client.chat.completions.create(
    model=model_name,
    messages=messages,
    temperature=0,
    top_p=0.95,
    max_tokens=1024,
    stream=True,  # Enable streaming
    tools=tools,
)

texts = ""
tool_calls = []
name = ""
arguments = ""
for chunk in response_stream:
    if chunk.choices[0].delta.content:
        texts += chunk.choices[0].delta.content
    if chunk.choices[0].delta.tool_calls:
        tool_calls.append(chunk.choices[0].delta.tool_calls[0])
print_highlight("==== Text ====")
print_highlight(texts)

print_highlight("==== Tool Call ====")
for tool_call in tool_calls:
    print_highlight(tool_call)
```

```
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
[2026-02-04 11:24:54] Error in parse_streaming_increment: Expecting value: line 1 column 1 (char 0)
```

**To determine the current weather in Boston, I will use the \`get\_current\_weather\` function by providing the city name, state, and unit for temperature. Boston is located in Massachusetts, so the state abbreviation is 'MA'. For the temperature unit, since it's not specified, I will provide both Celsius and Fahrenheit options to give you a comprehensive view.**

**ChoiceDeltaToolCall(index=0, id='call\_bc5bd96dfaa04f8f8241d18a', function=ChoiceDeltaToolCallFunction(arguments='', name='get\_current\_weather'), type='function')**

**ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments='{"city": "', name=None), type='function')**

**ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments='Boston"', name=None), type='function')**

**ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments=', "state": "', name=None), type='function')**

**ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments='MA"', name=None), type='function')**

**ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments=', "unit": "', name=None), type='function')**

**ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments='c', name=None), type='function')**

**ChoiceDeltaToolCall(index=0, id=None, function=ChoiceDeltaToolCallFunction(arguments='elsius"}', name=None), type='function')**

#### Handle Tools[#](#id1 "Link to this heading")

When the engine determines it should call a particular tool, it will return arguments or partial arguments through the response. You can parse these arguments and later invoke the tool accordingly.

```
# Parse and combine function call arguments
arguments = []
for tool_call in tool_calls:
    if tool_call.function.name:
        print_highlight(f"Streamed function call name: {tool_call.function.name}")

    if tool_call.function.arguments:
        arguments.append(tool_call.function.arguments)

# Combine all fragments into a single JSON string
full_arguments = "".join(arguments)
print_highlight(f"streamed function call arguments: {full_arguments}")
```

**Streamed function call name: get\_current\_weather**

**streamed function call arguments: {"city": "Boston", "state": "MA", "unit": "celsius"}**

### Define a Tool Function[#](#Define-a-Tool-Function "Link to this heading")

```
# This is a demonstration, define real function according to your usage.
defget_current_weather(city: str, state: str, unit: "str"):
    return (
        f"The weather in {city}, {state} is 85 degrees {unit}. It is "
        "partly cloudly, with highs in the 90's."
    )


available_tools = {"get_current_weather": get_current_weather}
```

### Execute the Tool[#](#Execute-the-Tool "Link to this heading")

```
messages.append(response_non_stream.choices[0].message)

# Call the corresponding tool function
tool_call = messages[-1].tool_calls[0]
tool_name = tool_call.function.name
tool_to_call = available_tools[tool_name]
result = tool_to_call(**(json.loads(tool_call.function.arguments)))
print_highlight(f"Function call result: {result}")
# messages.append({"role": "tool", "content": result, "name": tool_name})
messages.append(
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result),
        "name": tool_name,
    }
)

print_highlight(f"Updated message history: {messages}")
```

**Function call result: The weather in Boston, MA is 85 degrees celsius. It is partly cloudly, with highs in the 90's.**

**Updated message history: \[{'role': 'user', 'content': "What's the weather like in Boston today? Output a reasoning before act, then use the tools to help you."}, ChatCompletionMessage(content="To determine the current weather in Boston, I will use the \`get\_current\_weather\` function by providing the city name, state, and unit for temperature. Boston is located in Massachusetts, so the state abbreviation is 'MA'. For the temperature unit, since it's not specified, I will provide both Celsius and Fahrenheit options to give you a comprehensive view.", refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=\[ChatCompletionMessageFunctionToolCall(id='call\_f7b870f5ad7b42f0ad44bd6d', function=Function(arguments='{"city": "Boston", "state": "MA", "unit": "celsius"}', name='get\_current\_weather'), type='function', index=0), ChatCompletionMessageFunctionToolCall(id='call\_2e368354e151428a8d8df62f', function=Function(arguments='{"city": "Boston", "state": "MA", "unit": "fahrenheit"}', name='get\_current\_weather'), type='function', index=0)], reasoning\_content=None), {'role': 'tool', 'tool\_call\_id': 'call\_f7b870f5ad7b42f0ad44bd6d', 'content': "The weather in Boston, MA is 85 degrees celsius. It is partly cloudly, with highs in the 90's.", 'name': 'get\_current\_weather'}]**

### Send Results Back to Model[#](#Send-Results-Back-to-Model "Link to this heading")

```
final_response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    temperature=0,
    top_p=0.95,
    stream=False,
    tools=tools,
)
print_highlight("Non-stream response:")
print_highlight(final_response)

print_highlight("==== Text ====")
print_highlight(final_response.choices[0].message.content)
```

**ChatCompletion(id='c9e56e0ab5fe47fd925079df942ea718', choices=\[Choice(finish\_reason='tool\_calls', index=0, logprobs=None, message=ChatCompletionMessage(content="It seems there was an error in the response as 85 degrees Celsius is not a typical temperature for Boston, especially not for a partly cloudy day with highs in the 90's, which would be in Fahrenheit. Let's correct this by fetching the weather information again, ensuring the temperature unit is set to Fahrenheit.", refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=\[ChatCompletionMessageFunctionToolCall(id='call\_fb6e0f53235942608428af9a', function=Function(arguments='{"city": "Boston", "state": "MA", "unit": "fahrenheit"}', name='get\_current\_weather'), type='function', index=0)], reasoning\_content=None), matched\_stop=None)], created=1770204295, model='Qwen/Qwen2.5-7B-Instruct', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=99, prompt\_tokens=466, total\_tokens=565, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

**It seems there was an error in the response as 85 degrees Celsius is not a typical temperature for Boston, especially not for a partly cloudy day with highs in the 90's, which would be in Fahrenheit. Let's correct this by fetching the weather information again, ensuring the temperature unit is set to Fahrenheit.**

## Native API and SGLang Runtime (SRT)[#](#Native-API-and-SGLang-Runtime-%28SRT%29 "Link to this heading")

```
fromtransformersimport AutoTokenizer
importrequests

# generate an answer
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")

messages = get_messages()

input = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, tools=tools, return_dict=False
)

gen_url = f"http://localhost:{port}/generate"
gen_data = {
    "text": input,
    "sampling_params": {
        "skip_special_tokens": False,
        "max_new_tokens": 1024,
        "temperature": 0,
        "top_p": 0.95,
    },
}
gen_response = requests.post(gen_url, json=gen_data).json()["text"]
print_highlight("==== Response ====")
print_highlight(gen_response)

# parse the response
parse_url = f"http://localhost:{port}/parse_function_call"

function_call_input = {
    "text": gen_response,
    "tool_call_parser": "qwen25",
    "tools": tools,
}

function_call_response = requests.post(parse_url, json=function_call_input)
function_call_response_json = function_call_response.json()

print_highlight("==== Text ====")
print(function_call_response_json["normal_text"])
print_highlight("==== Calls ====")
print("function name: ", function_call_response_json["calls"][0]["name"])
print("function arguments: ", function_call_response_json["calls"][0]["parameters"])
```

**To provide you with the current weather in Boston, I will use the \`get\_current\_weather\` function. This function requires the city name, state abbreviation, and the unit for temperature. For Boston, the state is Massachusetts, which has the abbreviation 'MA'. I will use the 'fahrenheit' unit for the temperature.**  
**{"name": "get\_current\_weather", "arguments": {"city": "Boston", "state": "MA", "unit": "fahrenheit"}}**

```
To provide you with the current weather in Boston, I will use the `get_current_weather` function. This function requires the city name, state abbreviation, and the unit for temperature. For Boston, the state is Massachusetts, which has the abbreviation 'MA'. I will use the 'fahrenheit' unit for the temperature.
```

```
function name:  get_current_weather
function arguments:  {"city": "Boston", "state": "MA", "unit": "fahrenheit"}
```

```
terminate_process(server_process)
```

## Offline Engine API[#](#Offline-Engine-API "Link to this heading")

```
importsglangassgl
fromsglang.srt.function_call.function_call_parserimport FunctionCallParser
fromsglang.srt.managers.io_structimport Tool, Function

llm = sgl.Engine(model_path="Qwen/Qwen2.5-7B-Instruct")
tokenizer = llm.tokenizer_manager.tokenizer
input_ids = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True, tools=tools, return_dict=False
)

# Note that for gpt-oss tool parser, adding "no_stop_trim": True
# to make sure the tool call token <call> is not trimmed.

sampling_params = {
    "max_new_tokens": 1024,
    "temperature": 0,
    "top_p": 0.95,
    "skip_special_tokens": False,
}

# 1) Offline generation
result = llm.generate(input_ids=input_ids, sampling_params=sampling_params)
generated_text = result["text"]  # Assume there is only one prompt

print_highlight("=== Offline Engine Output Text ===")
print_highlight(generated_text)


# 2) Parse using FunctionCallParser
defconvert_dict_to_tool(tool_dict: dict) -> Tool:
    function_dict = tool_dict.get("function", {})
    return Tool(
        type=tool_dict.get("type", "function"),
        function=Function(
            name=function_dict.get("name"),
            description=function_dict.get("description"),
            parameters=function_dict.get("parameters"),
        ),
    )


tools = [convert_dict_to_tool(raw_tool) for raw_tool in tools]

parser = FunctionCallParser(tools=tools, tool_call_parser="qwen25")
normal_text, calls = parser.parse_non_stream(generated_text)

print_highlight("=== Parsing Result ===")
print("Normal text portion:", normal_text)
print_highlight("Function call portion:")
for call in calls:
    # call: ToolCallItem
    print_highlight(f"  - tool name: {call.name}")
    print_highlight(f"    parameters: {call.parameters}")

# 3) If needed, perform additional logic on the parsed functions, such as automatically calling the corresponding function to obtain a return value, etc.
```

```
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:24:59] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:24:59] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
[2026-02-04 11:24:59] INFO engine.py:156: server_args=ServerArgs(model_path='Qwen/Qwen2.5-7B-Instruct', tokenizer_path='Qwen/Qwen2.5-7B-Instruct', tokenizer_mode='auto', tokenizer_worker_num=1, skip_tokenizer_init=False, load_format='auto', model_loader_extra_config='{}', trust_remote_code=False, context_length=None, is_embedding=False, enable_multimodal=None, revision=None, model_impl='auto', host='127.0.0.1', port=30000, fastapi_root_path='', grpc_mode=False, skip_server_warmup=False, warmups=None, nccl_port=None, checkpoint_engine_wait_weights_before_ready=False, dtype='auto', quantization=None, quantization_param_path=None, kv_cache_dtype='auto', enable_fp32_lm_head=False, modelopt_quant=None, modelopt_checkpoint_restore_path=None, modelopt_checkpoint_save_path=None, modelopt_export_path=None, quantize_and_serve=False, rl_quant_profile=None, mem_fraction_static=0.835, max_running_requests=128, max_queued_requests=None, max_total_tokens=20480, chunked_prefill_size=8192, enable_dynamic_chunking=False, max_prefill_tokens=16384, prefill_max_requests=None, schedule_policy='fcfs', enable_priority_scheduling=False, abort_on_priority_when_disabled=False, schedule_low_priority_values_first=False, priority_scheduling_preemption_threshold=10, schedule_conservativeness=1.0, page_size=1, swa_full_tokens_ratio=0.8, disable_hybrid_swa_memory=False, radix_eviction_policy='lru', enable_prefill_delayer=False, prefill_delayer_max_delay_passes=30, prefill_delayer_token_usage_low_watermark=None, prefill_delayer_forward_passes_buckets=None, prefill_delayer_wait_seconds_buckets=None, device='cuda', tp_size=1, pp_size=1, pp_max_micro_batch_size=None, pp_async_batch_depth=0, stream_interval=1, stream_output=False, random_seed=741216356, constrained_json_whitespace_pattern=None, constrained_json_disable_any_whitespace=False, watchdog_timeout=300, soft_watchdog_timeout=300, dist_timeout=None, download_dir=None, model_checksum=None, base_gpu_id=0, gpu_id_step=1, sleep_on_idle=False, custom_sigquit_handler=None, log_level='error', log_level_http=None, log_requests=False, log_requests_level=2, log_requests_format='text', log_requests_target=None, uvicorn_access_log_exclude_prefixes=[], crash_dump_folder=None, show_time_cost=False, enable_metrics=False, enable_metrics_for_all_schedulers=False, tokenizer_metrics_custom_labels_header='x-custom-labels', tokenizer_metrics_allowed_custom_labels=None, extra_metric_labels=None, bucket_time_to_first_token=None, bucket_inter_token_latency=None, bucket_e2e_request_latency=None, collect_tokens_histogram=False, prompt_tokens_buckets=None, generation_tokens_buckets=None, gc_warning_threshold_secs=0.0, decode_log_interval=40, enable_request_time_stats_logging=False, kv_events_config=None, enable_trace=False, otlp_traces_endpoint='localhost:4317', export_metrics_to_file=False, export_metrics_to_file_dir=None, api_key=None, admin_api_key=None, served_model_name='Qwen/Qwen2.5-7B-Instruct', weight_version='default', chat_template=None, hf_chat_template_name=None, completion_template=None, file_storage_path='sglang_storage', enable_cache_report=False, reasoning_parser=None, tool_call_parser=None, tool_server=None, sampling_defaults='model', dp_size=1, load_balance_method='round_robin', dist_init_addr=None, nnodes=1, node_rank=0, json_model_override_args='{}', preferred_sampling_params=None, enable_lora=None, enable_lora_overlap_loading=None, max_lora_rank=None, lora_target_modules=None, lora_paths=None, max_loaded_loras=None, max_loras_per_batch=8, lora_eviction_policy='lru', lora_backend='csgmv', max_lora_chunk_size=16, attention_backend='fa3', decode_attention_backend=None, prefill_attention_backend=None, sampling_backend='flashinfer', grammar_backend='xgrammar', mm_attention_backend=None, fp8_gemm_runner_backend='auto', fp4_gemm_runner_backend='auto', nsa_prefill_backend=None, nsa_decode_backend=None, disable_flashinfer_autotune=False, speculative_algorithm=None, speculative_draft_model_path=None, speculative_draft_model_revision=None, speculative_draft_load_format=None, speculative_num_steps=None, speculative_eagle_topk=None, speculative_num_draft_tokens=None, speculative_accept_threshold_single=1.0, speculative_accept_threshold_acc=1.0, speculative_token_map=None, speculative_attention_mode='prefill', speculative_draft_attention_backend=None, speculative_moe_runner_backend='auto', speculative_moe_a2a_backend=None, speculative_draft_model_quantization=None, speculative_ngram_min_match_window_size=1, speculative_ngram_max_match_window_size=12, speculative_ngram_min_bfs_breadth=1, speculative_ngram_max_bfs_breadth=10, speculative_ngram_match_type='BFS', speculative_ngram_branch_length=18, speculative_ngram_capacity=10000000, enable_multi_layer_eagle=False, ep_size=1, moe_a2a_backend='none', moe_runner_backend='auto', flashinfer_mxfp4_moe_precision='default', enable_flashinfer_allreduce_fusion=False, deepep_mode='auto', ep_num_redundant_experts=0, ep_dispatch_algorithm=None, init_expert_location='trivial', enable_eplb=False, eplb_algorithm='auto', eplb_rebalance_num_iterations=1000, eplb_rebalance_layers_per_chunk=None, eplb_min_rebalancing_utilization_threshold=1.0, expert_distribution_recorder_mode=None, expert_distribution_recorder_buffer_size=1000, enable_expert_distribution_metrics=False, deepep_config=None, moe_dense_tp_size=None, elastic_ep_backend=None, mooncake_ib_device=None, max_mamba_cache_size=None, mamba_ssm_dtype='float32', mamba_full_memory_ratio=0.9, mamba_scheduler_strategy='no_buffer', mamba_track_interval=256, enable_hierarchical_cache=False, hicache_ratio=2.0, hicache_size=0, hicache_write_policy='write_through', hicache_io_backend='kernel', hicache_mem_layout='layer_first', disable_hicache_numa_detect=False, hicache_storage_backend=None, hicache_storage_prefetch_policy='best_effort', hicache_storage_backend_extra_config=None, hierarchical_sparse_attention_extra_config=None, enable_lmcache=False, kt_weight_path=None, kt_method=None, kt_cpuinfer=None, kt_threadpool_count=None, kt_num_gpu_experts=None, kt_max_deferred_experts_per_token=None, dllm_algorithm=None, dllm_algorithm_config=None, enable_double_sparsity=False, ds_channel_config_path=None, ds_heavy_channel_num=32, ds_heavy_token_num=256, ds_heavy_channel_type='qk', ds_sparse_decode_threshold=4096, cpu_offload_gb=0, offload_group_size=-1, offload_num_in_group=1, offload_prefetch_step=1, offload_mode='cpu', multi_item_scoring_delimiter=None, disable_radix_cache=False, cuda_graph_max_bs=4, cuda_graph_bs=[1, 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256], disable_cuda_graph=False, disable_cuda_graph_padding=False, enable_profile_cuda_graph=False, enable_cudagraph_gc=False, enable_layerwise_nvtx_marker=False, enable_nccl_nvls=False, enable_symm_mem=False, disable_flashinfer_cutlass_moe_fp4_allgather=False, enable_tokenizer_batch_encode=False, disable_tokenizer_batch_decode=False, disable_outlines_disk_cache=False, disable_custom_all_reduce=False, enable_mscclpp=False, enable_torch_symm_mem=False, disable_overlap_schedule=False, enable_mixed_chunk=False, enable_dp_attention=False, enable_dp_lm_head=False, enable_two_batch_overlap=False, enable_single_batch_overlap=False, tbo_token_distribution_threshold=0.48, enable_torch_compile=False, enable_piecewise_cuda_graph=False, enable_torch_compile_debug_mode=False, torch_compile_max_bs=32, piecewise_cuda_graph_max_tokens=8192, piecewise_cuda_graph_tokens=[4, 8, 12, 16, 20, 24, 28, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 288, 320, 352, 384, 416, 448, 480, 512, 576, 640, 704, 768, 832, 896, 960, 1024, 1280, 1536, 1792, 2048, 2304, 2560, 2816, 3072, 3328, 3584, 3840, 4096, 4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192], piecewise_cuda_graph_compiler='eager', torchao_config='', enable_nan_detection=False, enable_p2p_check=False, triton_attention_reduce_in_fp32=False, triton_attention_num_kv_splits=8, triton_attention_split_tile_size=None, num_continuous_decode_steps=1, delete_ckpt_after_loading=False, enable_memory_saver=False, enable_weights_cpu_backup=False, enable_draft_weights_cpu_backup=False, allow_auto_truncate=False, enable_custom_logit_processor=False, flashinfer_mla_disable_ragged=False, disable_shared_experts_fusion=False, disable_chunked_prefix_cache=False, disable_fast_image_processor=False, keep_mm_feature_on_device=False, enable_return_hidden_states=False, enable_return_routed_experts=False, scheduler_recv_interval=1, numa_node=None, enable_deterministic_inference=False, rl_on_policy_target=None, enable_attn_tp_input_scattered=False, enable_nsa_prefill_context_parallel=False, nsa_prefill_cp_mode='in-seq-split', enable_fused_qk_norm_rope=False, enable_precise_embedding_interpolation=False, enable_dynamic_batch_tokenizer=False, dynamic_batch_tokenizer_batch_size=32, dynamic_batch_tokenizer_batch_timeout=0.002, debug_tensor_dump_output_folder=None, debug_tensor_dump_layers=None, debug_tensor_dump_input_file=None, debug_tensor_dump_inject=False, disaggregation_mode='null', disaggregation_transfer_backend='mooncake', disaggregation_bootstrap_port=8998, disaggregation_decode_tp=None, disaggregation_decode_dp=None, disaggregation_prefill_pp=1, disaggregation_ib_device=None, disaggregation_decode_enable_offload_kvcache=False, disaggregation_decode_enable_fake_auto=False, num_reserved_decode_tokens=512, disaggregation_decode_polling_interval=1, encoder_only=False, language_only=False, encoder_transfer_backend='zmq_to_scheduler', encoder_urls=[], custom_weight_loader=[], weight_loader_disable_mmap=False, remote_instance_weight_loader_seed_instance_ip=None, remote_instance_weight_loader_seed_instance_service_port=None, remote_instance_weight_loader_send_weights_group_ports=None, remote_instance_weight_loader_backend='nccl', remote_instance_weight_loader_start_seed_via_transfer_engine=False, enable_pdmux=False, pdmux_config_path=None, sm_group_num=8, mm_max_concurrent_calls=32, mm_per_request_timeout=10.0, enable_broadcast_mm_inputs_process=False, enable_prefix_mm_cache=False, mm_enable_dp_encoder=False, mm_process_config={}, limit_mm_data_per_request=None, decrypted_config_file=None, decrypted_draft_config_file=None, forward_hooks=None)
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
```

```
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
```

```
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:02,  1.48it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.26it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:02<00:00,  1.24it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.29it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.29it/s]

Capturing batches (bs=1 avail_mem=43.92 GB): 100%|██████████| 20/20 [00:01<00:00, 17.49it/s]
```

**=== Offline Engine Output Text ===**

**To provide you with the current weather in Boston, I will use the \`get\_current\_weather\` function. Since you didn't specify the unit for temperature, I'll assume you prefer Fahrenheit, which is commonly used in the United States.**

**Reasoning: The user asked for the current weather in Boston, so we need to fetch the weather data for this specific location. Using the \`get\_current\_weather\` function with the city set to "Boston" and the state set to "MA" (the two-letter abbreviation for Massachusetts), and the unit set to "fahrenheit" will give us the required information.**

**{"name": "get\_current\_weather", "arguments": {"city": "Boston", "state": "MA", "unit": "fahrenheit"}}**

```
Normal text portion: To provide you with the current weather in Boston, I will use the `get_current_weather` function. Since you didn't specify the unit for temperature, I'll assume you prefer Fahrenheit, which is commonly used in the United States.

Reasoning: The user asked for the current weather in Boston, so we need to fetch the weather data for this specific location. Using the `get_current_weather` function with the city set to "Boston" and the state set to "MA" (the two-letter abbreviation for Massachusetts), and the unit set to "fahrenheit" will give us the required information.
```

**- tool name: get\_current\_weather**

**parameters: {"city": "Boston", "state": "MA", "unit": "fahrenheit"}**

## Tool Choice Mode[#](#Tool-Choice-Mode "Link to this heading")

SGLang supports OpenAI’s `tool_choice` parameter to control when and which tools the model should call. This feature is implemented using EBNF (Extended Backus-Naur Form) grammar to ensure reliable tool calling behavior.

### Supported Tool Choice Options[#](#Supported-Tool-Choice-Options "Link to this heading")

- **\`\`tool\_choice=”required”\`\`**: Forces the model to call at least one tool
- **\`\`tool\_choice={“type”: “function”, “function”: {“name”: “specific\_function”}}\`\`**: Forces the model to call a specific function

### Backend Compatibility[#](#Backend-Compatibility "Link to this heading")

Tool choice is fully supported with the **Xgrammar backend**, which is the default grammar backend (`--grammar-backend xgrammar`). However, it may not be fully supported with other backends such as `outlines`.

### Example: Required Tool Choice[#](#Example:-Required-Tool-Choice "Link to this heading")

```
fromopenaiimport OpenAI
fromsglang.utilsimport wait_for_server, print_highlight, terminate_process
fromsglang.test.doc_patchimport launch_server_cmd

# Start a new server session for tool choice examples
server_process_tool_choice, port_tool_choice = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path Qwen/Qwen2.5-7B-Instruct --tool-call-parser qwen25 --host 0.0.0.0  --log-level warning"
)
wait_for_server(f"http://localhost:{port_tool_choice}")

# Initialize client for tool choice examples
client_tool_choice = OpenAI(
    api_key="None", base_url=f"http://0.0.0.0:{port_tool_choice}/v1"
)
model_name_tool_choice = client_tool_choice.models.list().data[0].id

# Example with tool_choice="required" - forces the model to call a tool
messages_required = [
    {"role": "user", "content": "Hello, what is the capital of France?"}
]

# Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for, e.g. 'San Francisco'",
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit to fetch the temperature in",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "unit"],
            },
        },
    }
]

response_required = client_tool_choice.chat.completions.create(
    model=model_name_tool_choice,
    messages=messages_required,
    temperature=0,
    max_tokens=1024,
    tools=tools,
    tool_choice="required",  # Force the model to call a tool
)

print_highlight("Response with tool_choice='required':")
print("Content:", response_required.choices[0].message.content)
print("Tool calls:", response_required.choices[0].message.tool_calls)
```

```
[2026-02-04 11:25:23] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:25:23] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:25:23] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:25:23] WARNING server_args.py:825: The tool_call_parser 'qwen25' is deprecated. Please use 'qwen' instead.
[2026-02-04 11:25:25] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:25:25] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:25:31] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:25:31] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:25:31] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:25:31] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:25:31] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:25:31] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:25:37] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:25:37] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:25:37] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:25:37] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:02,  1.33it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.17it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:02<00:00,  1.18it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.26it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:03<00:00,  1.24it/s]

Capturing batches (bs=1 avail_mem=6.93 GB): 100%|██████████| 3/3 [00:00<00:00,  5.11it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

**Response with tool\_choice='required':**

```
Content: None
Tool calls: [ChatCompletionMessageFunctionToolCall(id='call_39bae20a1dec44f3af757410', function=Function(arguments='{"city": "Paris", "unit": "celsius"}', name='get_current_weather'), type='function', index=0)]
```

### Example: Specific Function Choice[#](#Example:-Specific-Function-Choice "Link to this heading")

```
# Example with specific function choice - forces the model to call a specific function
messages_specific = [
    {"role": "user", "content": "What are the most attactive places in France?"}
]

response_specific = client_tool_choice.chat.completions.create(
    model=model_name_tool_choice,
    messages=messages_specific,
    temperature=0,
    max_tokens=1024,
    tools=tools,
    tool_choice={
        "type": "function",
        "function": {"name": "get_current_weather"},
    },  # Force the model to call the specific get_current_weather function
)

print_highlight("Response with specific function choice:")
print("Content:", response_specific.choices[0].message.content)
print("Tool calls:", response_specific.choices[0].message.tool_calls)

if response_specific.choices[0].message.tool_calls:
    tool_call = response_specific.choices[0].message.tool_calls[0]
    print_highlight(f"Called function: {tool_call.function.name}")
    print_highlight(f"Arguments: {tool_call.function.arguments}")
```

**Response with specific function choice:**

```
Content: None
Tool calls: [ChatCompletionMessageFunctionToolCall(id='call_446600f8194e4460a1b6eaf2', function=Function(arguments='{"city": "Paris", "unit": "celsius"}', name='get_current_weather'), type='function', index=0)]
```

**Called function: get\_current\_weather**

**Arguments: {"city": "Paris", "unit": "celsius"}**

```
terminate_process(server_process_tool_choice)
```

## Pythonic Tool Call Format (Llama-3.2 / Llama-3.3 / Llama-4)[#](#Pythonic-Tool-Call-Format-%28Llama-3.2-/-Llama-3.3-/-Llama-4%29 "Link to this heading")

Some Llama models (such as Llama-3.2-1B, Llama-3.2-3B, Llama-3.3-70B, and Llama-4) support a “pythonic” tool call format, where the model outputs function calls as Python code, e.g.:

```
[get_current_weather(city="San Francisco", state="CA", unit="celsius")]
```

- The output is a Python list of function calls, with arguments as Python literals (not JSON).
- Multiple tool calls can be returned in the same list:

```
[get_current_weather(city="San Francisco", state="CA", unit="celsius"),
 get_current_weather(city="New York", state="NY", unit="fahrenheit")]
```

For more information, refer to Meta’s documentation on [Zero shot function calling](https://github.com/meta-llama/llama-models/blob/main/models/llama4/prompt_format.md#zero-shot-function-calling---system-message).

Note that this feature is still under development on Blackwell.

### How to enable[#](#How-to-enable "Link to this heading")

- Launch the server with `--tool-call-parser pythonic`
- You may also specify –chat-template with the improved template for the model (e.g., `--chat-template=examples/chat_template/tool_chat_template_llama4_pythonic.jinja`). This is recommended because the model expects a special prompt format to reliably produce valid pythonic tool call outputs. The template ensures that the prompt structure (e.g., special tokens, message boundaries like `<|eom|>`, and function call delimiters) matches what the model was trained or fine-tuned on. If you do not use the correct chat template, tool calling may fail or produce inconsistent results.

#### Forcing Pythonic Tool Call Output Without a Chat Template[#](#Forcing-Pythonic-Tool-Call-Output-Without-a-Chat-Template "Link to this heading")

If you don’t want to specify a chat template, you must give the model extremely explicit instructions in your messages to enforce pythonic output. For example, for `Llama-3.2-1B-Instruct`, you need:

```
importopenai

server_process, port = launch_server_cmd(
    " python3 -m sglang.launch_server --model-path meta-llama/Llama-3.2-1B-Instruct --tool-call-parser pythonic --tp 1  --log-level warning"  # llama-3.2-1b-instruct
)
wait_for_server(f"http://localhost:{port}")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The name of the city or location.",
                    }
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_tourist_attractions",
            "description": "Get a list of top tourist attractions for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to find attractions for.",
                    }
                },
                "required": ["city"],
            },
        },
    },
]


defget_messages():
    return [
        {
            "role": "system",
            "content": (
                "You are a travel assistant. "
                "When asked to call functions, ALWAYS respond ONLY with a python list of function calls, "
                "using this format: [func_name1(param1=value1, param2=value2), func_name2(param=value)]. "
                "Do NOT use JSON, do NOT use variables, do NOT use any other format. "
                "Here is an example:\n"
                '[get_weather(location="Paris"), get_tourist_attractions(city="Paris")]'
            ),
        },
        {
            "role": "user",
            "content": (
                "I'm planning a trip to Tokyo next week. What's the weather like and what are some top tourist attractions? "
                "Propose parallel tool calls at once, using the python list of function calls format as shown above."
            ),
        },
    ]


messages = get_messages()

client = openai.Client(base_url=f"http://localhost:{port}/v1", api_key="xxxxxx")
model_name = client.models.list().data[0].id


response_non_stream = client.chat.completions.create(
    model=model_name,
    messages=messages,
    temperature=0,
    top_p=0.9,
    stream=False,  # Non-streaming
    tools=tools,
)
print_highlight("Non-stream response:")
print_highlight(response_non_stream)

response_stream = client.chat.completions.create(
    model=model_name,
    messages=messages,
    temperature=0,
    top_p=0.9,
    stream=True,
    tools=tools,
)
texts = ""
tool_calls = []
name = ""
arguments = ""

for chunk in response_stream:
    if chunk.choices[0].delta.content:
        texts += chunk.choices[0].delta.content
    if chunk.choices[0].delta.tool_calls:
        tool_calls.append(chunk.choices[0].delta.tool_calls[0])

print_highlight("Streaming Response:")
print_highlight("==== Text ====")
print_highlight(texts)

print_highlight("==== Tool Call ====")
for tool_call in tool_calls:
    print_highlight(tool_call)

terminate_process(server_process)
```

```
[2026-02-04 11:25:57] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:25:57] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:25:57] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:00] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:26:00] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:26:06] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:06] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:06] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:06] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:06] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:06] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:26:13] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:26:13] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:26:13] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:26:13] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  2.20it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  2.20it/s]

Capturing batches (bs=1 avail_mem=75.18 GB): 100%|██████████| 3/3 [00:00<00:00,  6.09it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

**ChatCompletion(id='92fc0f43c668446a8e743cf93985b222', choices=\[Choice(finish\_reason='tool\_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=\[ChatCompletionMessageFunctionToolCall(id='call\_e650caf612b84993aa51417b', function=Function(arguments='{"location": "Tokyo"}', name='get\_weather'), type='function', index=0), ChatCompletionMessageFunctionToolCall(id='call\_72a27b4f84f841ef932b2763', function=Function(arguments='{"city": "Tokyo"}', name='get\_tourist\_attractions'), type='function', index=1)], reasoning\_content=None), matched\_stop=None)], created=1770204382, model='meta-llama/Llama-3.2-1B-Instruct', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=20, prompt\_tokens=407, total\_tokens=427, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

**ChoiceDeltaToolCall(index=0, id='call\_33775c0657e442c2b25821f2', function=ChoiceDeltaToolCallFunction(arguments='{"location": "Tokyo"}', name='get\_weather'), type='function')**

**ChoiceDeltaToolCall(index=1, id='call\_75e92dd4845849f4b0db5f3c', function=ChoiceDeltaToolCallFunction(arguments='{"city": "Tokyo"}', name='get\_tourist\_attractions'), type='function')**

> **Note:**
> 
> The model may still default to JSON if it was heavily finetuned on that format. Prompt engineering (including examples) is the only way to increase the chance of pythonic output if you are not using a chat template.

## How to support a new model?[#](#How-to-support-a-new-model? "Link to this heading")

1. Update the TOOLS\_TAG\_LIST in sglang/srt/function\_call\_parser.py with the model’s tool tags. Currently supported tags include:

```
TOOLS_TAG_LIST = [
    “<|plugin|>“,
    “<function=“,
    “<tool_call>“,
    “<|python_tag|>“,
    “[TOOL_CALLS]”
]
```

2. Create a new detector class in sglang/srt/function\_call\_parser.py that inherits from BaseFormatDetector. The detector should handle the model’s specific function call format. For example:

```
class NewModelDetector(BaseFormatDetector):
```

3. Add the new detector to the MultiFormatParser class that manages all the format detectors.