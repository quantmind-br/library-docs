---
title: Streaming - DSPy
url: https://dspy.ai/tutorials/streaming/
source: sitemap
fetched_at: 2026-01-23T08:04:26.01867059-03:00
rendered_js: false
word_count: 896
summary: This document explains how to implement real-time output token and intermediate status streaming in DSPy programs using the streamify wrapper and StreamListener objects.
tags:
    - dspy
    - streaming
    - async-io
    - token-generation
    - python-sdk
    - llm-optimization
category: guide
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/tutorials/streaming/index.md "Edit this page")

In this guide, we will walk you through how to enable streaming in your DSPy program. DSPy Streaming consists of two parts:

- **Output Token Streaming**: Stream individual tokens as they're generated, rather than waiting for the complete response.
- **Intermediate Status Streaming**: Provide real-time updates about the program's execution state (e.g., "Calling web search...", "Processing results...").

## Output Token Streaming[¶](#output-token-streaming "Permanent link")

DSPy's token streaming feature works with any module in your pipeline, not just the final output. The only requirement is that the streamed field must be of type `str`. To enable token streaming:

1. Wrap your program with `dspy.streamify`
2. Create one or more `dspy.streaming.StreamListener` objects to specify which fields to stream

Here's a basic example:

```
importos

importdspy

os.environ["OPENAI_API_KEY"] = "your_api_key"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

predict = dspy.Predict("question->answer")

# Enable streaming for the 'answer' field
stream_predict = dspy.streamify(
    predict,
    stream_listeners=[dspy.streaming.StreamListener(signature_field_name="answer")],
)
```

To consume the streamed output:

```
importasyncio

async defread_output_stream():
    output_stream = stream_predict(question="Why did a chicken cross the kitchen?")

    async for chunk in output_stream:
        print(chunk)

asyncio.run(read_output_stream())
```

This will produce output like:

```
StreamResponse(predict_name='self', signature_field_name='answer', chunk='To')
StreamResponse(predict_name='self', signature_field_name='answer', chunk=' get')
StreamResponse(predict_name='self', signature_field_name='answer', chunk=' to')
StreamResponse(predict_name='self', signature_field_name='answer', chunk=' the')
StreamResponse(predict_name='self', signature_field_name='answer', chunk=' other')
StreamResponse(predict_name='self', signature_field_name='answer', chunk=' side of the frying pan!')
Prediction(
    answer='To get to the other side of the frying pan!'
)
```

Note: Since `dspy.streamify` returns an async generator, you must use it within an async context. If you're using an environment like Jupyter or Google Colab that already has an event loop (async context), you can use the generator directly.

You may have noticed that the above streaming contains two different entities: `StreamResponse` and `Prediction.` `StreamResponse` is the wrapper over streaming tokens on the field being listened to, and in this example it is the `answer` field. `Prediction` is the program's final output. In DSPy, streaming is implemented in a sidecar fashion: we enable streaming on the LM so that LM outputs a stream of tokens. We send these tokens to a side channel, which is being continuously read by the user-defined listeners. Listeners keep interpreting the stream, and decides if the `signature_field_name` it is listening to has started to appear and has finalized. Once it decides that the field appears, the listener begins outputting tokens to the async generator users can read. Listeners' internal mechanism changes according to the adapter behind the scene, and because usually we cannot decide if a field has finalized until seeing the next field, the listener buffers the output tokens before sending to the final generator, which is why you will usually see the last chunk of type `StreamResponse` has more than one token. The program's output is also written to the stream, which is the chunk of `Prediction` as in the sample output above.

To handle these different types and implement custom logic:

```
importasyncio

async defread_output_stream():
  output_stream = stream_predict(question="Why did a chicken cross the kitchen?")

  async for chunk in output_stream:
    return_value = None
    if isinstance(chunk, dspy.streaming.StreamResponse):
      print(f"Output token of field {chunk.signature_field_name}: {chunk.chunk}")
    elif isinstance(chunk, dspy.Prediction):
      return_value = chunk


program_output = asyncio.run(read_output_stream())
print("Final output: ", program_output)
```

### Understand `StreamResponse`[¶](#understand-streamresponse "Permanent link")

`StreamResponse` (`dspy.streaming.StreamResponse`) is the wrapper class of streaming tokens. It comes with 3 fields:

- `predict_name`: the name of the predict that holds the `signature_field_name`. The name is the same name of keys as you run `your_program.named_predictors()`. In the code above because `answer` is from the `predict` itself, so the `predict_name` shows up as `self`, which is the only key as your run `predict.named_predictors()`.
- `signature_field_name`: the output field that these tokens map to. `predict_name` and `signature_field_name` together form the unique identifier of the field. We will demonstrate how to handle multiple fields streaming and duplicated field name later in this guide.
- `chunk`: the value of the stream chunk.

### Streaming with Cache[¶](#streaming-with-cache "Permanent link")

When a cached result is found, the stream will skip individual tokens and only yield the final `Prediction`. For example:

```
Prediction(
    answer='To get to the other side of the dinner plate!'
)
```

### Streaming Multiple Fields[¶](#streaming-multiple-fields "Permanent link")

You can monitor multiple fields by creating a `StreamListener` for each one. Here's an example with a multi-module program:

```
importasyncio

importdspy

lm = dspy.LM("openai/gpt-4o-mini", cache=False)
dspy.configure(lm=lm)


classMyModule(dspy.Module):
    def__init__(self):
        super().__init__()

        self.predict1 = dspy.Predict("question->answer")
        self.predict2 = dspy.Predict("answer->simplified_answer")

    defforward(self, question: str, **kwargs):
        answer = self.predict1(question=question)
        simplified_answer = self.predict2(answer=answer)
        return simplified_answer


predict = MyModule()
stream_listeners = [
    dspy.streaming.StreamListener(signature_field_name="answer"),
    dspy.streaming.StreamListener(signature_field_name="simplified_answer"),
]
stream_predict = dspy.streamify(
    predict,
    stream_listeners=stream_listeners,
)

async defread_output_stream():
    output = stream_predict(question="why did a chicken cross the kitchen?")

    return_value = None
    async for chunk in output:
        if isinstance(chunk, dspy.streaming.StreamResponse):
            print(chunk)
        elif isinstance(chunk, dspy.Prediction):
            return_value = chunk
    return return_value

program_output = asyncio.run(read_output_stream())
print("Final output: ", program_output)
```

The output will look like:

```
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk='To')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' get')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' to')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' the')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' other side of the recipe!')
StreamResponse(predict_name='predict2', signature_field_name='simplified_answer', chunk='To')
StreamResponse(predict_name='predict2', signature_field_name='simplified_answer', chunk=' reach')
StreamResponse(predict_name='predict2', signature_field_name='simplified_answer', chunk=' the')
StreamResponse(predict_name='predict2', signature_field_name='simplified_answer', chunk=' other side of the recipe!')
Final output:  Prediction(
    simplified_answer='To reach the other side of the recipe!'
)
```

### Streaming the Same Field Multiple Times (as in dspy.ReAct)[¶](#streaming-the-same-field-multiple-times-as-in-dspyreact "Permanent link")

By default, a `StreamListener` automatically closes itself after completing a single streaming session. This design helps prevent performance issues, since every token is broadcast to all configured stream listeners, and having too many active listeners can introduce significant overhead.

However, in scenarios where a DSPy module is used repeatedly in a loop—such as with `dspy.ReAct` — you may want to stream the same field from each prediction, every time it is used. To enable this behavior, set allow\_reuse=True when creating your `StreamListener`. See the example below:

```
importasyncio

importdspy

lm = dspy.LM("openai/gpt-4o-mini", cache=False)
dspy.configure(lm=lm)


deffetch_user_info(user_name: str):
"""Get user information like name, birthday, etc."""
    return {
        "name": user_name,
        "birthday": "2009-05-16",
    }


defget_sports_news(year: int):
"""Get sports news for a given year."""
    if year == 2009:
        return "Usane Bolt broke the world record in the 100m race."
    return None


react = dspy.ReAct("question->answer", tools=[fetch_user_info, get_sports_news])

stream_listeners = [
    # dspy.ReAct has a built-in output field called "next_thought".
    dspy.streaming.StreamListener(signature_field_name="next_thought", allow_reuse=True),
]
stream_react = dspy.streamify(react, stream_listeners=stream_listeners)


async defread_output_stream():
    output = stream_react(question="What sports news happened in the year Adam was born?")
    return_value = None
    async for chunk in output:
        if isinstance(chunk, dspy.streaming.StreamResponse):
            print(chunk)
        elif isinstance(chunk, dspy.Prediction):
            return_value = chunk
    return return_value


print(asyncio.run(read_output_stream()))
```

In this example, by setting `allow_reuse=True` in the StreamListener, you ensure that streaming for "next\_thought" is available for every iteration, not just the first. When you run this code, you will see the streaming tokens for `next_thought` output each time the field is produced.

#### Handling Duplicate Field Names[¶](#handling-duplicate-field-names "Permanent link")

When streaming fields with the same name from different modules, specify both the `predict` and `predict_name` in the `StreamListener`:

```
importasyncio

importdspy

lm = dspy.LM("openai/gpt-4o-mini", cache=False)
dspy.configure(lm=lm)


classMyModule(dspy.Module):
    def__init__(self):
        super().__init__()

        self.predict1 = dspy.Predict("question->answer")
        self.predict2 = dspy.Predict("question, answer->answer, score")

    defforward(self, question: str, **kwargs):
        answer = self.predict1(question=question)
        simplified_answer = self.predict2(answer=answer)
        return simplified_answer


predict = MyModule()
stream_listeners = [
    dspy.streaming.StreamListener(
        signature_field_name="answer",
        predict=predict.predict1,
        predict_name="predict1"
    ),
    dspy.streaming.StreamListener(
        signature_field_name="answer",
        predict=predict.predict2,
        predict_name="predict2"
    ),
]
stream_predict = dspy.streamify(
    predict,
    stream_listeners=stream_listeners,
)


async defread_output_stream():
    output = stream_predict(question="why did a chicken cross the kitchen?")

    return_value = None
    async for chunk in output:
        if isinstance(chunk, dspy.streaming.StreamResponse):
            print(chunk)
        elif isinstance(chunk, dspy.Prediction):
            return_value = chunk
    return return_value


program_output = asyncio.run(read_output_stream())
print("Final output: ", program_output)
```

The output will be like:

```
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk='To')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' get')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' to')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' the')
StreamResponse(predict_name='predict1', signature_field_name='answer', chunk=' other side of the recipe!')
StreamResponse(predict_name='predict2', signature_field_name='answer', chunk="I'm")
StreamResponse(predict_name='predict2', signature_field_name='answer', chunk=' ready')
StreamResponse(predict_name='predict2', signature_field_name='answer', chunk=' to')
StreamResponse(predict_name='predict2', signature_field_name='answer', chunk=' assist')
StreamResponse(predict_name='predict2', signature_field_name='answer', chunk=' you')
StreamResponse(predict_name='predict2', signature_field_name='answer', chunk='! Please provide a question.')
Final output:  Prediction(
    answer="I'm ready to assist you! Please provide a question.",
    score='N/A'
)
```

Status streaming keeps users informed about the program's progress, especially useful for long-running operations like tool calls or complex AI pipelines. To implement status streaming:

1. Create a custom status message provider by subclassing `dspy.streaming.StatusMessageProvider`
2. Override the desired hook methods to provide custom status messages
3. Pass your provider to `dspy.streamify`

Example:

```
classMyStatusMessageProvider(dspy.streaming.StatusMessageProvider):
    deflm_start_status_message(self, instance, inputs):
        return f"Calling LM with inputs {inputs}..."

    deflm_end_status_message(self, outputs):
        return f"Tool finished with output: {outputs}!"
```

Available hooks:

- lm\_start\_status\_message: status message at the start of calling dspy.LM.
- lm\_end\_status\_message: status message at the end of calling dspy.LM.
- module\_start\_status\_message: status message at the start of calling a dspy.Module.
- module\_end\_status\_message: status message at the start of calling a dspy.Module.
- tool\_start\_status\_message: status message at the start of calling dspy.Tool.
- tool\_end\_status\_message: status message at the end of calling dspy.Tool.

Each hook should return a string containing the status message.

After creating the message provider, just pass it to `dspy.streamify`, and you can enable both status message streaming and output token streaming. Please see the example below. The intermediate status message is represented in the class `dspy.streaming.StatusMessage`, so we need to have another condition check to capture it.

```
importasyncio

importdspy

lm = dspy.LM("openai/gpt-4o-mini", cache=False)
dspy.configure(lm=lm)


classMyModule(dspy.Module):
    def__init__(self):
        super().__init__()

        self.tool = dspy.Tool(lambda x: 2 * x, name="double_the_number")
        self.predict = dspy.ChainOfThought("num1, num2->sum")

    defforward(self, num, **kwargs):
        num2 = self.tool(x=num)
        return self.predict(num1=num, num2=num2)


classMyStatusMessageProvider(dspy.streaming.StatusMessageProvider):
    deftool_start_status_message(self, instance, inputs):
        return f"Calling Tool {instance.name} with inputs {inputs}..."

    deftool_end_status_message(self, outputs):
        return f"Tool finished with output: {outputs}!"


predict = MyModule()
stream_listeners = [
    # dspy.ChainOfThought has a built-in output field called "reasoning".
    dspy.streaming.StreamListener(signature_field_name="reasoning"),
]
stream_predict = dspy.streamify(
    predict,
    stream_listeners=stream_listeners,
    status_message_provider=MyStatusMessageProvider(),
)


async defread_output_stream():
    output = stream_predict(num=3)

    return_value = None
    async for chunk in output:
        if isinstance(chunk, dspy.streaming.StreamResponse):
            print(chunk)
        elif isinstance(chunk, dspy.Prediction):
            return_value = chunk
        elif isinstance(chunk, dspy.streaming.StatusMessage):
            print(chunk)
    return return_value


program_output = asyncio.run(read_output_stream())
print("Final output: ", program_output)
```

Sample output:

```
StatusMessage(message='Calling tool double_the_number...')
StatusMessage(message='Tool calling finished! Querying the LLM with tool calling results...')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk='To')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' find')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' the')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' sum')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' of')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' the')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' two')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' numbers')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=',')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' we')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' simply')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' add')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' them')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' together')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk='.')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' Here')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=',')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' ')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk='3')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' plus')
StreamResponse(predict_name='predict.predict', signature_field_name='reasoning', chunk=' 6 equals 9.')
Final output:  Prediction(
    reasoning='To find the sum of the two numbers, we simply add them together. Here, 3 plus 6 equals 9.',
    sum='9'
)
```

## Synchronous Streaming[¶](#synchronous-streaming "Permanent link")

By default calling a streamified DSPy program produces an async generator. In order to get back a sync generator, you can set the flag `async_streaming=False`:

```
importos

importdspy

os.environ["OPENAI_API_KEY"] = "your_api_key"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

predict = dspy.Predict("question->answer")

# Enable streaming for the 'answer' field
stream_predict = dspy.streamify(
    predict,
    stream_listeners=[dspy.streaming.StreamListener(signature_field_name="answer")],
    async_streaming=False,
)

output = stream_predict(question="why did a chicken cross the kitchen?")

program_output = None
for chunk in output:
    if isinstance(chunk, dspy.streaming.StreamResponse):
        print(chunk)
    elif isinstance(chunk, dspy.Prediction):
        program_output = chunk
print(f"Program output: {program_output}")
```