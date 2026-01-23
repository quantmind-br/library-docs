---
title: Stream whales - Pydantic AI
url: https://ai.pydantic.dev/examples/stream-whales/
source: sitemap
fetched_at: 2026-01-22T22:25:51.202713702-03:00
rendered_js: false
word_count: 73
summary: This document demonstrates how to implement and validate streaming structured outputs from an LLM using Pydantic AI and Python's asynchronous capabilities.
tags:
    - pydantic-ai
    - streaming-output
    - structured-data
    - real-time-validation
    - python-asyncio
    - llm-agents
category: tutorial
---

Information about whales — an example of streamed structured response validation.

Demonstrates:

- [streaming structured output](https://ai.pydantic.dev/output/#streaming-structured-output)

This script streams structured responses from GPT-4 about whales, validates the data and displays it as a dynamic table using [`rich`](https://github.com/Textualize/rich) as the data is received.

## Running the Example

With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/setup/#usage), run:

pipuv

```
python-mpydantic_ai_examples.stream_whales
```

```
uvrun-mpydantic_ai_examples.stream_whales
```

Should give an output like this:

## Example Code

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) [stream\_whales.py](https://github.com/pydantic/pydantic-ai/blob/main/examples/pydantic_ai_examples/stream_whales.py)

```
"""Information about whales — an example of streamed structured response validation.

This script streams structured responses from GPT-4 about whales, validates the data
and displays it as a dynamic table using Rich as the data is received.

Run with:

    uv run -m pydantic_ai_examples.stream_whales
"""

fromtypingimport Annotated

importlogfire
frompydanticimport Field
fromrich.consoleimport Console
fromrich.liveimport Live
fromrich.tableimport Table
fromtyping_extensionsimport NotRequired, TypedDict

frompydantic_aiimport Agent

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()


classWhale(TypedDict):
    name: str
    length: Annotated[
        float, Field(description='Average length of an adult whale in meters.')
    ]
    weight: NotRequired[
        Annotated[
            float,
            Field(description='Average weight of an adult whale in kilograms.', ge=50),
        ]
    ]
    ocean: NotRequired[str]
    description: NotRequired[Annotated[str, Field(description='Short Description')]]


agent = Agent('gateway/openai:gpt-4', output_type=list[Whale])


async defmain():
    console = Console()
    with Live('\n' * 36, console=console) as live:
        console.print('Requesting data...', style='cyan')
        async with agent.run_stream(
            'Generate me details of 5 species of Whale.'
        ) as result:
            console.print('Response:', style='green')

            async for whales in result.stream_output(debounce_by=0.01):
                table = Table(
                    title='Species of Whale',
                    caption='Streaming Structured responses from GPT-4',
                    width=120,
                )
                table.add_column('ID', justify='right')
                table.add_column('Name')
                table.add_column('Avg. Length (m)', justify='right')
                table.add_column('Avg. Weight (kg)', justify='right')
                table.add_column('Ocean')
                table.add_column('Description', justify='right')

                for wid, whale in enumerate(whales, start=1):
                    table.add_row(
                        str(wid),
                        whale['name'],
                        f'{whale["length"]:0.0f}',
                        f'{w:0.0f}' if (w := whale.get('weight')) else '…',
                        whale.get('ocean') or '…',
                        whale.get('description') or '…',
                    )
                live.update(table)


if __name__ == '__main__':
    importasyncio

    asyncio.run(main())
```

[stream\_whales.py](https://github.com/pydantic/pydantic-ai/blob/main/examples/pydantic_ai_examples/stream_whales.py)

```
"""Information about whales — an example of streamed structured response validation.

This script streams structured responses from GPT-4 about whales, validates the data
and displays it as a dynamic table using Rich as the data is received.

Run with:

    uv run -m pydantic_ai_examples.stream_whales
"""

fromtypingimport Annotated

importlogfire
frompydanticimport Field
fromrich.consoleimport Console
fromrich.liveimport Live
fromrich.tableimport Table
fromtyping_extensionsimport NotRequired, TypedDict

frompydantic_aiimport Agent

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()


classWhale(TypedDict):
    name: str
    length: Annotated[
        float, Field(description='Average length of an adult whale in meters.')
    ]
    weight: NotRequired[
        Annotated[
            float,
            Field(description='Average weight of an adult whale in kilograms.', ge=50),
        ]
    ]
    ocean: NotRequired[str]
    description: NotRequired[Annotated[str, Field(description='Short Description')]]


agent = Agent('openai:gpt-4', output_type=list[Whale])


async defmain():
    console = Console()
    with Live('\n' * 36, console=console) as live:
        console.print('Requesting data...', style='cyan')
        async with agent.run_stream(
            'Generate me details of 5 species of Whale.'
        ) as result:
            console.print('Response:', style='green')

            async for whales in result.stream_output(debounce_by=0.01):
                table = Table(
                    title='Species of Whale',
                    caption='Streaming Structured responses from GPT-4',
                    width=120,
                )
                table.add_column('ID', justify='right')
                table.add_column('Name')
                table.add_column('Avg. Length (m)', justify='right')
                table.add_column('Avg. Weight (kg)', justify='right')
                table.add_column('Ocean')
                table.add_column('Description', justify='right')

                for wid, whale in enumerate(whales, start=1):
                    table.add_row(
                        str(wid),
                        whale['name'],
                        f'{whale["length"]:0.0f}',
                        f'{w:0.0f}' if (w := whale.get('weight')) else '…',
                        whale.get('ocean') or '…',
                        whale.get('description') or '…',
                    )
                live.update(table)


if __name__ == '__main__':
    importasyncio

    asyncio.run(main())
```