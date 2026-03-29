---
title: Perplexity with LangChain
url: https://docs.perplexity.ai/docs/getting-started/integrations/langchain.md
source: llms
fetched_at: 2026-02-04T07:22:57.741246906-03:00
rendered_js: false
word_count: 317
summary: This document provides instructions and code examples for integrating Perplexity's AI models and web search capabilities into LangChain applications using the langchain-perplexity package.
tags:
    - langchain
    - perplexity-api
    - python
    - retrieval-augmented-generation
    - ai-agents
    - chat-models
    - web-search
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Perplexity with LangChain

> Use Perplexity's chat models and search tool in your LangChain applications.

## Overview

The `langchain-perplexity` package provides LangChain integrations for Perplexity's API, enabling you to build LLM applications with real-time web search capabilities.

<Info>
  **LangChain** is a popular Python framework for building applications powered by large language models. It provides composable components for chains, agents, and retrieval-augmented generation (RAG). Learn more at [langchain.com](https://www.langchain.com).
</Info>

The integration includes:

* **ChatPerplexity** - Chat model with Pro Search, streaming, and search controls
* **PerplexitySearchRetriever** - Retriever for RAG applications
* **PerplexitySearchResults** - Tool for LangChain agents

## Installation

<Tabs>
  <Tab title="pip">
    ```bash  theme={null}
    pip install langchain-perplexity
    ```
  </Tab>

  <Tab title="uv">
    ```bash  theme={null}
    uv add langchain-perplexity
    ```
  </Tab>
</Tabs>

## API Key Setup

Set your Perplexity API key as an environment variable:

```python  theme={null}
import os

os.environ["PPLX_API_KEY"] = "your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/settings/api">
  Generate your API key from the Perplexity dashboard.
</Card>

## Quick Start: Chat Models

Use `ChatPerplexity` for conversational AI with web search:

```python  theme={null}
from langchain_perplexity import ChatPerplexity

chat = ChatPerplexity(model="sonar")

response = chat.invoke("What are the latest developments in AI?")
print(response.content)
```

### Pro Search

Enable multi-step reasoning with Pro Search:

```python  theme={null}
from langchain_perplexity import ChatPerplexity, WebSearchOptions

chat = ChatPerplexity(
    model="sonar-pro",
    web_search_options=WebSearchOptions(search_type="pro")
)

response = chat.invoke("How does the electoral college work?")

# Access reasoning steps
if reasoning := response.additional_kwargs.get("reasoning_steps"):
    for step in reasoning:
        print(f"Thought: {step['thought']}")
```

### Search Controls

Filter search results by domain, recency, or date:

```python  theme={null}
chat = ChatPerplexity(
    model="sonar",
    search_domain_filter=["wikipedia.org", "nature.com"],
    search_recency_filter="month",
    return_images=True
)

response = chat.invoke("Solar system planets")

# Access citations and images
print("Citations:", response.additional_kwargs.get("citations", []))
print("Images:", response.additional_kwargs.get("images", []))
```

### Streaming

```python  theme={null}
for chunk in chat.stream("Explain quantum computing"):
    print(chunk.content, end="", flush=True)
```

## Quick Start: Retriever

Use `PerplexitySearchRetriever` for RAG applications:

```python  theme={null}
from langchain_perplexity import PerplexitySearchRetriever

retriever = PerplexitySearchRetriever(k=5)

docs = retriever.invoke("What is nuclear fusion?")

for doc in docs:
    print(f"Title: {doc.metadata['title']}")
    print(f"URL: {doc.metadata['url']}")
    print(f"Content: {doc.page_content[:200]}...")
    print("---")
```

### RAG Chain Example

```python  theme={null}
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_perplexity import ChatPerplexity, PerplexitySearchRetriever

llm = ChatPerplexity(model="sonar")
retriever = PerplexitySearchRetriever(k=3)

template = """Answer based on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

answer = rag_chain.invoke("What is the current status of ITER?")
print(answer)
```

## Quick Start: Tool

Use `PerplexitySearchResults` with LangChain agents:

```python  theme={null}
from langchain_perplexity import PerplexitySearchResults

tool = PerplexitySearchResults()

results = tool.invoke("LangChain framework")

for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['snippet'][:100]}...")
    print("---")
```

### Agent Example

```python  theme={null}
from langchain.chat_models import init_chat_model
from langchain_perplexity import PerplexitySearchResults
from langgraph.prebuilt import create_react_agent

model = init_chat_model(model="gpt-4o", model_provider="openai")
search_tool = PerplexitySearchResults()

agent = create_react_agent(model, [search_tool])

for step in agent.stream(
    {"messages": [("user", "What are the latest LangChain releases?")]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
```

## Available Models

The integration supports all Perplexity models:

| Model                 | Description                               |
| --------------------- | ----------------------------------------- |
| `sonar`               | Fast, cost-effective search model         |
| `sonar-pro`           | Advanced model with Pro Search support    |
| `sonar-reasoning-pro` | Advanced reasoning capabilities           |
| `sonar-deep-research` | Deep research with comprehensive analysis |

See the full list of models on our [models page](/docs/getting-started/models).

## Links & Resources

<CardGroup cols={2}>
  <Card title="LangChain Docs" icon="book" href="https://docs.langchain.com/oss/python/integrations/providers/perplexity">
    Full LangChain integration documentation
  </Card>

  <Card title="ChatPerplexity" icon="message" href="https://docs.langchain.com/oss/python/integrations/chat/perplexity">
    Detailed chat model documentation
  </Card>

  <Card title="Retriever Docs" icon="magnifying-glass" href="https://docs.langchain.com/oss/python/integrations/retrievers/perplexity">
    PerplexitySearchRetriever documentation
  </Card>

  <Card title="Tool Docs" icon="wrench" href="https://docs.langchain.com/oss/python/integrations/tools/perplexity">
    PerplexitySearchResults documentation
  </Card>

  <Card title="PyPI Package" icon="python" href="https://pypi.org/project/langchain-perplexity/">
    View on PyPI
  </Card>

  <Card title="API Reference" icon="code" href="https://python.langchain.com/api_reference/perplexity/">
    LangChain API reference
  </Card>
</CardGroup>

## Support

Need help with the integration?

* Check the [LangChain documentation](https://docs.langchain.com)
* Review our [FAQ](/docs/resources/faq)