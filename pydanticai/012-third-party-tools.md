---
title: Third-Party Tools - Pydantic AI
url: https://ai.pydantic.dev/third-party-tools/
source: sitemap
fetched_at: 2026-01-22T22:23:42.097219429-03:00
rendered_js: false
word_count: 459
summary: This document explains how to integrate third-party tool ecosystems like LangChain and ACI.dev into Pydantic AI agents using dedicated adapters and toolsets.
tags:
    - pydantic-ai
    - langchain-integration
    - aci-dev
    - toolsets
    - mcp-client
    - external-tools
category: guide
---

Pydantic AI supports integration with various third-party tool libraries, allowing you to leverage existing tool ecosystems in your agents.

See the [MCP Client](https://ai.pydantic.dev/mcp/client/) documentation for how to use MCP servers with Pydantic AI as [toolsets](https://ai.pydantic.dev/toolsets/).

If you'd like to use a tool from LangChain's [community tool library](https://python.langchain.com/docs/integrations/tools/) with Pydantic AI, you can use the [`tool_from_langchain`](https://ai.pydantic.dev/api/ext/#pydantic_ai.ext.langchain.tool_from_langchain "tool_from_langchain") convenience method. Note that Pydantic AI will not validate the arguments in this case -- it's up to the model to provide arguments matching the schema specified by the LangChain tool, and up to the LangChain tool to raise an error if the arguments are invalid.

You will need to install the `langchain-community` package and any others required by the tool in question.

Here is how you can use the LangChain `DuckDuckGoSearchRun` tool, which requires the `ddgs` package:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
fromlangchain_community.toolsimport DuckDuckGoSearchRun

frompydantic_aiimport Agent
frompydantic_ai.ext.langchainimport tool_from_langchain

search = DuckDuckGoSearchRun()
search_tool = tool_from_langchain(search)

agent = Agent(
    'gateway/gemini:gemini-2.5-flash',
    tools=[search_tool],
)

result = agent.run_sync('What is the release date of Elden Ring Nightreign?')  # (1)!
print(result.output)
#> Elden Ring Nightreign is planned to be released on May 30, 2025.
```

1. The release date of this game is the 30th of May 2025, which is after the knowledge cutoff for Gemini 2.0 (August 2024).

```
fromlangchain_community.toolsimport DuckDuckGoSearchRun

frompydantic_aiimport Agent
frompydantic_ai.ext.langchainimport tool_from_langchain

search = DuckDuckGoSearchRun()
search_tool = tool_from_langchain(search)

agent = Agent(
    'google-gla:gemini-2.5-flash',
    tools=[search_tool],
)

result = agent.run_sync('What is the release date of Elden Ring Nightreign?')  # (1)!
print(result.output)
#> Elden Ring Nightreign is planned to be released on May 30, 2025.
```

1. The release date of this game is the 30th of May 2025, which is after the knowledge cutoff for Gemini 2.0 (August 2024).

If you'd like to use multiple LangChain tools or a LangChain [toolkit](https://python.langchain.com/docs/concepts/tools/#toolkits), you can use the [`LangChainToolset`](https://ai.pydantic.dev/api/ext/#pydantic_ai.ext.langchain.LangChainToolset "LangChainToolset") [toolset](https://ai.pydantic.dev/toolsets/) which takes a list of LangChain tools:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
fromlangchain_community.agent_toolkitsimport SlackToolkit

frompydantic_aiimport Agent
frompydantic_ai.ext.langchainimport LangChainToolset

toolkit = SlackToolkit()
toolset = LangChainToolset(toolkit.get_tools())

agent = Agent('gateway/openai:gpt-5', toolsets=[toolset])
# ...
```

```
fromlangchain_community.agent_toolkitsimport SlackToolkit

frompydantic_aiimport Agent
frompydantic_ai.ext.langchainimport LangChainToolset

toolkit = SlackToolkit()
toolset = LangChainToolset(toolkit.get_tools())

agent = Agent('openai:gpt-5', toolsets=[toolset])
# ...
```

If you'd like to use a tool from the [ACI.dev tool library](https://www.aci.dev/tools) with Pydantic AI, you can use the [`tool_from_aci`](https://ai.pydantic.dev/api/ext/#pydantic_ai.ext.aci.tool_from_aci "tool_from_aci") convenience method. Note that Pydantic AI will not validate the arguments in this case -- it's up to the model to provide arguments matching the schema specified by the ACI tool, and up to the ACI tool to raise an error if the arguments are invalid.

You will need to install the `aci-sdk` package, set your ACI API key in the `ACI_API_KEY` environment variable, and pass your ACI "linked account owner ID" to the function.

Here is how you can use the ACI.dev `TAVILY__SEARCH` tool:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
importos

frompydantic_aiimport Agent
frompydantic_ai.ext.aciimport tool_from_aci

tavily_search = tool_from_aci(
    'TAVILY__SEARCH',
    linked_account_owner_id=os.getenv('LINKED_ACCOUNT_OWNER_ID'),
)

agent = Agent(
    'gateway/gemini:gemini-2.5-flash',
    tools=[tavily_search],
)

result = agent.run_sync('What is the release date of Elden Ring Nightreign?')  # (1)!
print(result.output)
#> Elden Ring Nightreign is planned to be released on May 30, 2025.
```

1. The release date of this game is the 30th of May 2025, which is after the knowledge cutoff for Gemini 2.0 (August 2024).

```
importos

frompydantic_aiimport Agent
frompydantic_ai.ext.aciimport tool_from_aci

tavily_search = tool_from_aci(
    'TAVILY__SEARCH',
    linked_account_owner_id=os.getenv('LINKED_ACCOUNT_OWNER_ID'),
)

agent = Agent(
    'google-gla:gemini-2.5-flash',
    tools=[tavily_search],
)

result = agent.run_sync('What is the release date of Elden Ring Nightreign?')  # (1)!
print(result.output)
#> Elden Ring Nightreign is planned to be released on May 30, 2025.
```

1. The release date of this game is the 30th of May 2025, which is after the knowledge cutoff for Gemini 2.0 (August 2024).

If you'd like to use multiple ACI.dev tools, you can use the [`ACIToolset`](https://ai.pydantic.dev/api/ext/#pydantic_ai.ext.aci.ACIToolset "ACIToolset") [toolset](https://ai.pydantic.dev/toolsets/) which takes a list of ACI tool names as well as the `linked_account_owner_id`:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway)

```
importos

frompydantic_aiimport Agent
frompydantic_ai.ext.aciimport ACIToolset

toolset = ACIToolset(
    [
        'OPEN_WEATHER_MAP__CURRENT_WEATHER',
        'OPEN_WEATHER_MAP__FORECAST',
    ],
    linked_account_owner_id=os.getenv('LINKED_ACCOUNT_OWNER_ID'),
)

agent = Agent('gateway/openai:gpt-5', toolsets=[toolset])
```

```
importos

frompydantic_aiimport Agent
frompydantic_ai.ext.aciimport ACIToolset

toolset = ACIToolset(
    [
        'OPEN_WEATHER_MAP__CURRENT_WEATHER',
        'OPEN_WEATHER_MAP__FORECAST',
    ],
    linked_account_owner_id=os.getenv('LINKED_ACCOUNT_OWNER_ID'),
)

agent = Agent('openai:gpt-5', toolsets=[toolset])
```

## See Also

- [Function Tools](https://ai.pydantic.dev/tools/) - Basic tool concepts and registration
- [Toolsets](https://ai.pydantic.dev/toolsets/) - Managing collections of tools
- [MCP Client](https://ai.pydantic.dev/mcp/client/) - Using MCP servers with Pydantic AI
- [LangChain Toolsets](https://ai.pydantic.dev/toolsets/#langchain-tools) - Using LangChain toolsets
- [ACI.dev Toolsets](https://ai.pydantic.dev/toolsets/#aci-tools) - Using ACI.dev toolsets