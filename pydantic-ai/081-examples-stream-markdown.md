---
title: Stream markdown - Pydantic AI
url: https://ai.pydantic.dev/examples/stream-markdown/
source: sitemap
fetched_at: 2026-01-22T22:25:49.715095433-03:00
rendered_js: false
word_count: 256
summary: This document demonstrates how to stream markdown text responses from a Pydantic AI agent and render them in real-time within a terminal using the rich library.
tags:
    - pydantic-ai
    - streaming
    - markdown
    - rich-library
    - asynchronous-programming
    - terminal-ui
category: tutorial
---

This example shows how to stream markdown from an agent, using the [`rich`](https://github.com/Textualize/rich) library to highlight the output in the terminal.

It'll run the example with both OpenAI and Google Gemini models if the required environment variables are set.

Demonstrates:

- [streaming text responses](https://ai.pydantic.dev/output/#streaming-text)

## Running the Example

With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/setup/#usage), run:

pipuv

```
python-mpydantic_ai_examples.stream_markdown
```

```
uvrun-mpydantic_ai_examples.stream_markdown
```

## Example Code

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) [stream\_markdown.py](https://github.com/pydantic/pydantic-ai/blob/main/examples/pydantic_ai_examples/stream_markdown.py)

```
"""This example shows how to stream markdown from an agent, using the `rich` library to display the markdown.

Run with:

    uv run -m pydantic_ai_examples.stream_markdown
"""

importasyncio
importos

importlogfire
fromrich.consoleimport Console, ConsoleOptions, RenderResult
fromrich.liveimport Live
fromrich.markdownimport CodeBlock, Markdown
fromrich.syntaximport Syntax
fromrich.textimport Text

frompydantic_aiimport Agent
frompydantic_ai.modelsimport KnownModelName

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()

agent = Agent()

# models to try, and the appropriate env var
models: list[tuple[KnownModelName, str]] = [
    ('gateway/gemini:gemini-2.5-flash', 'GEMINI_API_KEY'),
    ('openai:gpt-5-mini', 'OPENAI_API_KEY'),
    ('groq:llama-3.3-70b-versatile', 'GROQ_API_KEY'),
]


async defmain():
    prettier_code_blocks()
    console = Console()
    prompt = 'Show me a short example of using Pydantic.'
    console.log(f'Asking: {prompt}...', style='cyan')
    for model, env_var in models:
        if env_var in os.environ:
            console.log(f'Using model: {model}')
            with Live('', console=console, vertical_overflow='visible') as live:
                async with agent.run_stream(prompt, model=model) as result:
                    async for message in result.stream_output():
                        live.update(Markdown(message))
            console.log(result.usage())
        else:
            console.log(f'{model} requires {env_var} to be set.')


defprettier_code_blocks():
"""Make rich code blocks prettier and easier to copy.

    From https://github.com/samuelcolvin/aicli/blob/v0.8.0/samuelcolvin_aicli.py#L22
    """

    classSimpleCodeBlock(CodeBlock):
        def__rich_console__(
            self, console: Console, options: ConsoleOptions
        ) -> RenderResult:
            code = str(self.text).rstrip()
            yield Text(self.lexer_name, style='dim')
            yield Syntax(
                code,
                self.lexer_name,
                theme=self.theme,
                background_color='default',
                word_wrap=True,
            )
            yield Text(f'/{self.lexer_name}', style='dim')

    Markdown.elements['fence'] = SimpleCodeBlock


if __name__ == '__main__':
    asyncio.run(main())
```

[stream\_markdown.py](https://github.com/pydantic/pydantic-ai/blob/main/examples/pydantic_ai_examples/stream_markdown.py)

```
"""This example shows how to stream markdown from an agent, using the `rich` library to display the markdown.

Run with:

    uv run -m pydantic_ai_examples.stream_markdown
"""

importasyncio
importos

importlogfire
fromrich.consoleimport Console, ConsoleOptions, RenderResult
fromrich.liveimport Live
fromrich.markdownimport CodeBlock, Markdown
fromrich.syntaximport Syntax
fromrich.textimport Text

frompydantic_aiimport Agent
frompydantic_ai.modelsimport KnownModelName

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()

agent = Agent()

# models to try, and the appropriate env var
models: list[tuple[KnownModelName, str]] = [
    ('google-gla:gemini-2.5-flash', 'GEMINI_API_KEY'),
    ('openai:gpt-5-mini', 'OPENAI_API_KEY'),
    ('groq:llama-3.3-70b-versatile', 'GROQ_API_KEY'),
]


async defmain():
    prettier_code_blocks()
    console = Console()
    prompt = 'Show me a short example of using Pydantic.'
    console.log(f'Asking: {prompt}...', style='cyan')
    for model, env_var in models:
        if env_var in os.environ:
            console.log(f'Using model: {model}')
            with Live('', console=console, vertical_overflow='visible') as live:
                async with agent.run_stream(prompt, model=model) as result:
                    async for message in result.stream_output():
                        live.update(Markdown(message))
            console.log(result.usage())
        else:
            console.log(f'{model} requires {env_var} to be set.')


defprettier_code_blocks():
"""Make rich code blocks prettier and easier to copy.

    From https://github.com/samuelcolvin/aicli/blob/v0.8.0/samuelcolvin_aicli.py#L22
    """

    classSimpleCodeBlock(CodeBlock):
        def__rich_console__(
            self, console: Console, options: ConsoleOptions
        ) -> RenderResult:
            code = str(self.text).rstrip()
            yield Text(self.lexer_name, style='dim')
            yield Syntax(
                code,
                self.lexer_name,
                theme=self.theme,
                background_color='default',
                word_wrap=True,
            )
            yield Text(f'/{self.lexer_name}', style='dim')

    Markdown.elements['fence'] = SimpleCodeBlock


if __name__ == '__main__':
    asyncio.run(main())
```