---
title: Structured Outputs - vLLM
url: https://docs.vllm.ai/en/latest/features/structured_outputs/
source: sitemap
fetched_at: 2026-05-07T21:14:18.452142851-03:00
rendered_js: false
word_count: 780
summary: This document explains how to configure and use structured outputs in vLLM, including support for JSON schema, regex, choices, and grammars via the OpenAI-compatible API.
tags:
    - vllm
    - structured-outputs
    - openai-api
    - json-schema
    - regex-generation
    - grammar-constrained-decoding
    - pydantic
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/structured_outputs.md "Edit this page")

vLLM supports the generation of structured outputs using [xgrammar](https://github.com/mlc-ai/xgrammar) or [guidance](https://github.com/guidance-ai/llguidance) as backends. This document shows you some examples of the different options that are available to generate structured outputs.

Warning

If you are still using the following deprecated API fields which were removed in v0.12.0, please update your code to use `structured_outputs` as demonstrated in the rest of this document:

- `guided_json` -&gt; `{"structured_outputs": {"json": ...}}` or `StructuredOutputsParams(json=...)`
- `guided_regex` -&gt; `{"structured_outputs": {"regex": ...}}` or `StructuredOutputsParams(regex=...)`
- `guided_choice` -&gt; `{"structured_outputs": {"choice": ...}}` or `StructuredOutputsParams(choice=...)`
- `guided_grammar` -&gt; `{"structured_outputs": {"grammar": ...}}` or `StructuredOutputsParams(grammar=...)`
- `guided_whitespace_pattern` -&gt; `{"structured_outputs": {"whitespace_pattern": ...}}` or `StructuredOutputsParams(whitespace_pattern=...)`
- `structural_tag` -&gt; `{"structured_outputs": {"structural_tag": ...}}` or `StructuredOutputsParams(structural_tag=...)`
- `guided_decoding_backend` -&gt; Remove this field from your request

## Online Serving (OpenAI API)[¶](#online-serving-openai-api "Permanent link")

You can generate structured outputs using the OpenAI's [Completions](https://platform.openai.com/docs/api-reference/completions) and [Chat](https://platform.openai.com/docs/api-reference/chat) API.

The following parameters are supported, which must be added as extra parameters:

- `choice`: the output will be exactly one of the choices.
- `regex`: the output will follow the regex pattern.
- `json`: the output will follow the JSON schema.
- `grammar`: the output will follow the context free grammar.
- `structural_tag`: Follow a JSON schema within a set of specified tags within the generated text.

You can see the complete list of supported parameters on the [OpenAI-Compatible Server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/) page.

Structured outputs are supported by default in the OpenAI-Compatible Server. You may choose to specify the backend to use by setting the `--structured-outputs-config.backend` flag to `vllm serve`. The default backend is `auto`, which will try to choose an appropriate backend based on the details of the request. You may also choose a specific backend, along with some options. A full set of options is available in the `vllm serve --help` text.

Now let's see an example for each of the cases, starting with the `choice`, as it's the easiest one:

Code

```
fromopenaiimport OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="-",
)
model = client.models.list().data[0].id

completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"}
    ],
    extra_body={"structured_outputs": {"choice": ["positive", "negative"]}},
)
print(completion.choices[0].message.content)
```

The next example shows how to use the `regex`. The supported regex syntax depends on the structured output backend. For example, `xgrammar`, `guidance`, and `outlines` use Rust-style regex, while `lm-format-enforcer` uses Python's `re` module. The idea is to generate an email address, given a simple regex template:

Code

```
completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Generate an example email address for Alan Turing, who works in Enigma. End in .com and new line. Example result: [email protected]\n",
        }
    ],
    extra_body={"structured_outputs": {"regex": r"\w+@\w+\.com\n"}, "stop": ["\n"]},
)
print(completion.choices[0].message.content)
```

One of the most relevant features in structured text generation is the option to generate a valid JSON with pre-defined fields and formats. For this we can use the `json` parameter in two different ways:

- Using directly a [JSON Schema](https://json-schema.org/)
- Defining a [Pydantic model](https://docs.pydantic.dev/latest/) and then extracting the JSON Schema from it (which is normally an easier option).

The next example shows how to use the `response_format` parameter with a Pydantic model:

Code

```
frompydanticimport BaseModel
fromenumimport Enum

classCarType(str, Enum):
    sedan = "sedan"
    suv = "SUV"
    truck = "Truck"
    coupe = "Coupe"

classCarDescription(BaseModel):
    brand: str
    model: str
    car_type: CarType

json_schema = CarDescription.model_json_schema()

completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's",
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "car-description",
            "schema": CarDescription.model_json_schema()
        },
    },
)
print(completion.choices[0].message.content)
```

Tip

While not strictly necessary, normally it's better to indicate in the prompt the JSON schema and how the fields should be populated. This can improve the results notably in most cases.

Finally we have the `grammar` option, which is probably the most difficult to use, but it's really powerful. It allows us to define complete languages like SQL queries. It works by using a context free EBNF grammar. As an example, we can use to define a specific format of simplified SQL queries:

Code

```
simplified_sql_grammar = """
    root ::= select_statement

    select_statement ::= "SELECT " column " from " table " where " condition

    column ::= "col_1 " | "col_2 "

    table ::= "table_1 " | "table_2 "

    condition ::= column "= " number

    number ::= "1 " | "2 "
"""

completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Generate an SQL query to show the 'username' and 'email' from the 'users' table.",
        }
    ],
    extra_body={"structured_outputs": {"grammar": simplified_sql_grammar}},
)
print(completion.choices[0].message.content)
```

See also: [full example](https://github.com/vllm-project/vllm/blob/main/examples/features/structured_outputs/README.md)

## Reasoning Outputs[¶](#reasoning-outputs "Permanent link")

You can also use structured outputs with for reasoning models.

```
vllmservedeepseek-ai/DeepSeek-R1-Distill-Qwen-7B--reasoning-parserdeepseek_r1
```

Note that you can use reasoning with any provided structured outputs feature. The following uses one with JSON schema:

Code

```
frompydanticimport BaseModel


classPeople(BaseModel):
    name: str
    age: int


completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Generate a JSON with the name and age of one random person.",
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "people",
            "schema": People.model_json_schema()
        }
    },
)
print("reasoning: ", completion.choices[0].message.reasoning)
print("content: ", completion.choices[0].message.content)
```

See also: [full example](https://github.com/vllm-project/vllm/blob/main/examples/features/structured_outputs/README.md)

Note

When using Qwen3 Coder models with reasoning enabled, structured outputs might become disabled if the reasoning content does not get parsed into the `reasoning` field separately (v0.11.2+). To use both features together, you must explicitly enable structured outputs in reasoning mode. To do so, add the following flag when starting the vLLM server: `--structured-outputs-config.enable_in_reasoning=True`. See also: [Reasoning Outputs](https://docs.vllm.ai/en/latest/features/reasoning_outputs/) documentation.

## Experimental Automatic Parsing (OpenAI API)[¶](#experimental-automatic-parsing-openai-api "Permanent link")

This section covers the OpenAI beta wrapper over the `client.chat.completions.create()` method that provides richer integrations with Python specific types.

At the time of writing (`openai==1.54.4`), this is a "beta" feature in the OpenAI client library. Code reference can be found [here](https://github.com/openai/openai-python/blob/52357cff50bee57ef442e94d78a0de38b4173fc2/src/openai/resources/beta/chat/completions.py#L100-L104).

For the following examples, vLLM was set up using `vllm serve meta-llama/Llama-3.1-8B-Instruct`

Here is a simple example demonstrating how to get structured output using Pydantic models:

Code

```
frompydanticimport BaseModel
fromopenaiimport OpenAI

classInfo(BaseModel):
    name: str
    age: int

client = OpenAI(base_url="http://0.0.0.0:8000/v1", api_key="dummy")
model = client.models.list().data[0].id
completion = client.beta.chat.completions.parse(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "My name is Cameron, I'm 28. What's my name and age?"},
    ],
    response_format=Info,
)

message = completion.choices[0].message
print(message)
assert message.parsed
print("Name:", message.parsed.name)
print("Age:", message.parsed.age)

ParsedChatCompletionMessage[Testing](content='{"name": "Cameron", "age": 28}', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[], parsed=Testing(name='Cameron', age=28))
Name: Cameron
Age: 28
```

Here is a more complex example using nested Pydantic models to handle a step-by-step math solution:

Code

```
fromtypingimport List
frompydanticimport BaseModel
fromopenaiimport OpenAI

classStep(BaseModel):
    explanation: str
    output: str

classMathResponse(BaseModel):
    steps: list[Step]
    final_answer: str

completion = client.beta.chat.completions.parse(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful expert math tutor."},
        {"role": "user", "content": "Solve 8x + 31 = 2."},
    ],
    response_format=MathResponse,
)

message = completion.choices[0].message
print(message)
assert message.parsed
for i, step in enumerate(message.parsed.steps):
    print(f"Step #{i}:", step)
print("Answer:", message.parsed.final_answer)
```

Output:

```
ParsedChatCompletionMessage[MathResponse](content='{ "steps": [{ "explanation": "First, let\'s isolate the term with the variable \'x\'. To do this, we\'ll subtract 31 from both sides of the equation.", "output": "8x + 31 - 31 = 2 - 31"}, { "explanation": "By subtracting 31 from both sides, we simplify the equation to 8x = -29.", "output": "8x = -29"}, { "explanation": "Next, let\'s isolate \'x\' by dividing both sides of the equation by 8.", "output": "8x / 8 = -29 / 8"}], "final_answer": "x = -29/8" }', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[], parsed=MathResponse(steps=[Step(explanation="First, let's isolate the term with the variable 'x'. To do this, we'll subtract 31 from both sides of the equation.", output='8x + 31 - 31 = 2 - 31'), Step(explanation='By subtracting 31 from both sides, we simplify the equation to 8x = -29.', output='8x = -29'), Step(explanation="Next, let's isolate 'x' by dividing both sides of the equation by 8.", output='8x / 8 = -29 / 8')], final_answer='x = -29/8'))
Step #0: explanation="First, let's isolate the term with the variable 'x'. To do this, we'll subtract 31 from both sides of the equation." output='8x + 31 - 31 = 2 - 31'
Step #1: explanation='By subtracting 31 from both sides, we simplify the equation to 8x = -29.' output='8x = -29'
Step #2: explanation="Next, let's isolate 'x' by dividing both sides of the equation by 8." output='8x / 8 = -29 / 8'
Answer: x = -29/8
```

An example of using `structural_tag` can be found here: [examples/features/structured\_outputs](https://github.com/vllm-project/vllm/blob/main/examples/features/structured_outputs/README.md)

## Offline Inference[¶](#offline-inference "Permanent link")

Offline inference allows for the same types of structured outputs. To use it, we'll need to configure the structured outputs using the class `StructuredOutputsParams` inside [`SamplingParams`](https://docs.vllm.ai/en/latest/api/vllm/sampling_params/#vllm.sampling_params.SamplingParams "            SamplingParams"). The main available options inside `StructuredOutputsParams` are:

- `json`
- `regex`
- `choice`
- `grammar`
- `structural_tag`

These parameters can be used in the same way as the parameters from the Online Serving examples above. One example for the usage of the `choice` parameter is shown below:

Code

```
fromvllmimport LLM, SamplingParams
fromvllm.sampling_paramsimport StructuredOutputsParams

llm = LLM(model="HuggingFaceTB/SmolLM2-1.7B-Instruct")

structured_outputs_params = StructuredOutputsParams(choice=["Positive", "Negative"])
sampling_params = SamplingParams(structured_outputs=structured_outputs_params)
outputs = llm.generate(
    prompts="Classify this sentiment: vLLM is wonderful!",
    sampling_params=sampling_params,
)
print(outputs[0].outputs[0].text)
```

See also: [full example](https://github.com/vllm-project/vllm/blob/main/examples/features/structured_outputs/structured_outputs_offline.py)