---
title: Code Interpreter | Mistral Docs
url: https://docs.mistral.ai/agents/tools/built-in/code_interpreter
source: crawler
fetched_at: 2026-01-29T07:34:17.673106712-03:00
rendered_js: false
word_count: 329
---

Code Interpreter adds the capability to safely execute code in an isolated container, this built-in [tool](https://docs.mistral.ai/agents/tools/built-in) tool allows Agents to run code at any point on demand, practical to draw graphs, data analysis, mathematical operations, code validation, and much more.

![code_interpreter_graph](https://docs.mistral.ai/img/code_interpreter_connector.png)![code_interpreter_graph](https://docs.mistral.ai/img/code_interpreter_connector_dark.png)

To use the code interpreter, you can create an agent with the code interpreter tool, once done you can start a conversation with the agent and it will run code on demand, leveraging the outputs to answer your questions.

You can create an agent with access to our code interpreter by providing it as one of the tools.  
Note that you can still add more tools to the agent, the model is free to run code or not on demand.

As for other agents, when creating one you will receive an agent id corresponding to the created agent that you can use to start a conversation.

Now that we have our coding agent ready, we can at any point make use of it to run code.

To start a conversation with our code interpreter agent, we can use the following code:

Below we will explain the different outputs of the response of the previous snippet example:

- **`message.output`** : This entry corresponds to the initial response from the assistant, indicating that it can help generate the first 20 Fibonacci numbers.
- **`tool.execution`** : This entry corresponds to the execution of the code interpreter tool. It includes metadata about the execution, such as:
  
  - `name`: The name of the tool, which in this case is `code_interpreter`.
  - `object`: The type of object, which is `entry`.
  - `type`: The type of entry, which is `tool.execution`.
  - `created_at` and `completed_at`: Timestamps indicating when the tool execution started and finished.
  - `id`: A unique identifier for the tool execution.
  - `info`: This section contains additional information specific to the tool execution. For the `code_interpreter` tool, the `info` section includes:
    
    - `code`: The actual code that was executed. In this example, it contains a Python function `fibonacci(n)` that generates the first `n` numbers in the Fibonacci sequence and a call to this function to get the first 20 Fibonacci numbers.
    - `code_output`: The output of the executed code, which is the list of the first 20 Fibonacci numbers.
- **`message.output`** : This entry corresponds to the final response from the assistant, providing the first 20 values of the Fibonacci sequence.