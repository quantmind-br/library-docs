---
title: Server - Pydantic AI
url: https://ai.pydantic.dev/mcp/server/
source: sitemap
fetched_at: 2026-01-22T22:26:02.974962192-03:00
rendered_js: false
word_count: 208
summary: This document explains how to integrate Pydantic AI agents into Model Context Protocol (MCP) servers and clients, including how to implement MCP sampling for delegating LLM calls back to the client.
tags:
    - pydantic-ai
    - mcp-server
    - mcp-client
    - mcp-sampling
    - python-sdk
    - llm-integration
    - model-context-protocol
category: tutorial
---

Pydantic AI models can also be used within MCP Servers.

## MCP Server

Here's a simple example of a [Python MCP server](https://github.com/modelcontextprotocol/python-sdk) using Pydantic AI within a tool call:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) mcp\_server.py

```
frommcp.server.fastmcpimport FastMCP

frompydantic_aiimport Agent

server = FastMCP('Pydantic AI Server')
server_agent = Agent(
    'gateway/anthropic:claude-haiku-4-5', system_prompt='always reply in rhyme'
)


@server.tool()
async defpoet(theme: str) -> str:
"""Poem generator"""
    r = await server_agent.run(f'write a poem about {theme}')
    return r.output


if __name__ == '__main__':
    server.run()
```

mcp\_server.py

```
frommcp.server.fastmcpimport FastMCP

frompydantic_aiimport Agent

server = FastMCP('Pydantic AI Server')
server_agent = Agent(
    'anthropic:claude-haiku-4-5', system_prompt='always reply in rhyme'
)


@server.tool()
async defpoet(theme: str) -> str:
"""Poem generator"""
    r = await server_agent.run(f'write a poem about {theme}')
    return r.output


if __name__ == '__main__':
    server.run()
```

## Simple client

This server can be queried with any MCP client. Here is an example using the Python SDK directly:

mcp\_client.py

```
importasyncio
importos

frommcpimport ClientSession, StdioServerParameters
frommcp.client.stdioimport stdio_client


async defclient():
    server_params = StdioServerParameters(
        command='python', args=['mcp_server.py'], env=os.environ
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool('poet', {'theme': 'socks'})
            print(result.content[0].text)
"""
            Oh, socks, those garments soft and sweet,
            That nestle softly 'round our feet,
            From cotton, wool, or blended thread,
            They keep our toes from feeling dread.
            """


if __name__ == '__main__':
    asyncio.run(client())
```

## MCP Sampling

What is MCP Sampling?

See the [MCP client docs](https://ai.pydantic.dev/mcp/client/#mcp-sampling) for details of what MCP sampling is, and how you can support it when using Pydantic AI as an MCP client.

When Pydantic AI agents are used within MCP servers, they can use sampling via [`MCPSamplingModel`](https://ai.pydantic.dev/api/models/mcp-sampling/#pydantic_ai.models.mcp_sampling.MCPSamplingModel "MCPSamplingModel            dataclass   ").

We can extend the above example to use sampling so instead of connecting directly to the LLM, the agent calls back through the MCP client to make LLM calls.

mcp\_server\_sampling.py

```
frommcp.server.fastmcpimport Context, FastMCP

frompydantic_aiimport Agent
frompydantic_ai.models.mcp_samplingimport MCPSamplingModel

server = FastMCP('Pydantic AI Server with sampling')
server_agent = Agent(system_prompt='always reply in rhyme')


@server.tool()
async defpoet(ctx: Context, theme: str) -> str:
"""Poem generator"""
    r = await server_agent.run(f'write a poem about {theme}', model=MCPSamplingModel(session=ctx.session))
    return r.output


if __name__ == '__main__':
    server.run()  # run the server over stdio
```

The [above](#simple-client) client does not support sampling, so if you tried to use it with this server you'd get an error.

The simplest way to support sampling in an MCP client is to [use](https://ai.pydantic.dev/mcp/client/#mcp-sampling) a Pydantic AI agent as the client, but if you wanted to support sampling with the vanilla MCP SDK, you could do so like this:

mcp\_client\_sampling.py

```
importasyncio
fromtypingimport Any

frommcpimport ClientSession, StdioServerParameters
frommcp.client.stdioimport stdio_client
frommcp.shared.contextimport RequestContext
frommcp.typesimport (
    CreateMessageRequestParams,
    CreateMessageResult,
    ErrorData,
    TextContent,
)


async defsampling_callback(
    context: RequestContext[ClientSession, Any], params: CreateMessageRequestParams
) -> CreateMessageResult | ErrorData:
    print('sampling system prompt:', params.systemPrompt)
    #> sampling system prompt: always reply in rhyme
    print('sampling messages:', params.messages)
"""
    sampling messages:
    [
        SamplingMessage(
            role='user',
            content=TextContent(
                type='text',
                text='write a poem about socks',
                annotations=None,
                meta=None,
            ),
            meta=None,
        )
    ]
    """

    # TODO get the response content by calling an LLM...
    response_content = 'Socks for a fox.'

    return CreateMessageResult(
        role='assistant',
        content=TextContent(type='text', text=response_content),
        model='fictional-llm',
    )


async defclient():
    server_params = StdioServerParameters(command='python', args=['mcp_server_sampling.py'])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=sampling_callback) as session:
            await session.initialize()
            result = await session.call_tool('poet', {'theme': 'socks'})
            print(result.content[0].text)
            #> Socks for a fox.


if __name__ == '__main__':
    asyncio.run(client())
```

*(This example is complete, it can be run "as is")*