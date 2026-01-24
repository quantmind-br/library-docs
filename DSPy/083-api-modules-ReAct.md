---
title: ReAct - DSPy
url: https://dspy.ai/api/modules/ReAct/
source: sitemap
fetched_at: 2026-01-23T08:02:01.350902531-03:00
rendered_js: false
word_count: 12
summary: This document defines the implementation and initialization of the ReAct module in DSPy, a paradigm for building tool-using agents that interleave reasoning with action.
tags:
    - dspy
    - react-agent
    - tool-use
    - signature-polymorphism
    - agentic-workflows
    - llm-reasoning
category: api
---

````
def__init__(self, signature: type["Signature"], tools: list[Callable], max_iters: int = 20):
"""
    ReAct stands for "Reasoning and Acting," a popular paradigm for building tool-using agents.
    In this approach, the language model is iteratively provided with a list of tools and has
    to reason about the current situation. The model decides whether to call a tool to gather more
    information or to finish the task based on its reasoning process. The DSPy version of ReAct is
    generalized to work over any signature, thanks to signature polymorphism.

    Args:
        signature: The signature of the module, which defines the input and output of the react module.
        tools (list[Callable]): A list of functions, callable objects, or `dspy.Tool` instances.
        max_iters (Optional[int]): The maximum number of iterations to run. Defaults to 10.

    Example:

    ```python
    def get_weather(city: str) -> str:
        return f"The weather in {city} is sunny."

    react = dspy.ReAct(signature="question->answer", tools=[get_weather])
    pred = react(question="What is the weather in Tokyo?")
    ```
    """
    super().__init__()
    self.signature = signature = ensure_signature(signature)
    self.max_iters = max_iters

    tools = [t if isinstance(t, Tool) else Tool(t) for t in tools]
    tools = {tool.name: tool for tool in tools}

    inputs = ", ".join([f"`{k}`" for k in signature.input_fields.keys()])
    outputs = ", ".join([f"`{k}`" for k in signature.output_fields.keys()])
    instr = [f"{signature.instructions}\n"] if signature.instructions else []

    instr.extend(
        [
            f"You are an Agent. In each episode, you will be given the fields {inputs} as input. And you can see your past trajectory so far.",
            f"Your goal is to use one or more of the supplied tools to collect any necessary information for producing {outputs}.\n",
            "To do this, you will interleave next_thought, next_tool_name, and next_tool_args in each turn, and also when finishing the task.",
            "After each tool call, you receive a resulting observation, which gets appended to your trajectory.\n",
            "When writing next_thought, you may reason about the current situation and plan for future steps.",
            "When selecting the next_tool_name and its next_tool_args, the tool must be one of:\n",
        ]
    )

    tools["finish"] = Tool(
        func=lambda: "Completed.",
        name="finish",
        desc=f"Marks the task as complete. That is, signals that all information for producing the outputs, i.e. {outputs}, are now available to be extracted.",
        args={},
    )

    for idx, tool in enumerate(tools.values()):
        instr.append(f"({idx+1}) {tool}")
    instr.append("When providing `next_tool_args`, the value inside the field must be in JSON format")

    react_signature = (
        dspy.Signature({**signature.input_fields}, "\n".join(instr))
        .append("trajectory", dspy.InputField(), type_=str)
        .append("next_thought", dspy.OutputField(), type_=str)
        .append("next_tool_name", dspy.OutputField(), type_=Literal[tuple(tools.keys())])
        .append("next_tool_args", dspy.OutputField(), type_=dict[str, Any])
    )

    fallback_signature = dspy.Signature(
        {**signature.input_fields, **signature.output_fields},
        signature.instructions,
    ).append("trajectory", dspy.InputField(), type_=str)

    self.tools = tools
    self.react = dspy.Predict(react_signature)
    self.extract = dspy.ChainOfThought(fallback_signature)
````