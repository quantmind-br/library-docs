---
title: Dependencies - Pydantic AI
url: https://ai.pydantic.dev/dependencies/
source: sitemap
fetched_at: 2026-01-22T22:23:21.208355336-03:00
rendered_js: false
word_count: 1017
summary: This document explains how to use Pydantic AI's dependency injection system to pass type-safe data and services to agents, tools, and prompts. It covers defining dependencies with dataclasses and accessing them through the RunContext object during execution.
tags:
    - dependency-injection
    - pydantic-ai
    - type-safety
    - run-context
    - python-agent
category: guide
---

Pydantic AI uses a dependency injection system to provide data and services to your agent's [system prompts](https://ai.pydantic.dev/agents/#system-prompts), [tools](https://ai.pydantic.dev/tools/) and [output validators](https://ai.pydantic.dev/output/#output-validator-functions).

Matching Pydantic AI's design philosophy, our dependency system tries to use existing best practice in Python development rather than inventing esoteric "magic", this should make dependencies type-safe, understandable, easier to test, and ultimately easier to deploy in production.

## Defining Dependencies

Dependencies can be any python type. While in simple cases you might be able to pass a single object as a dependency (e.g. an HTTP connection), [dataclasses](https://docs.python.org/3/library/dataclasses.html#module-dataclasses) are generally a convenient container when your dependencies included multiple objects.

Here's an example of defining an agent that requires dependencies.

(**Note:** dependencies aren't actually used in this example, see [Accessing Dependencies](#accessing-dependencies) below)

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) unused\_dependencies.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent


@dataclass
classMyDeps:  # (1)!
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'gateway/openai:gpt-5',
    deps_type=MyDeps,  # (2)!
)


async defmain():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run(
            'Tell me a joke.',
            deps=deps,  # (3)!
        )
        print(result.output)
        #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. Define a dataclass to hold dependencies.
2. Pass the dataclass type to the `deps_type` argument of the [`Agent` constructor](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__"). **Note**: we're passing the type here, NOT an instance, this parameter is not actually used at runtime, it's here so we can get full type checking of the agent.
3. When running the agent, pass an instance of the dataclass to the `deps` parameter.

unused\_dependencies.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent


@dataclass
classMyDeps:  # (1)!
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'openai:gpt-5',
    deps_type=MyDeps,  # (2)!
)


async defmain():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run(
            'Tell me a joke.',
            deps=deps,  # (3)!
        )
        print(result.output)
        #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. Define a dataclass to hold dependencies.
2. Pass the dataclass type to the `deps_type` argument of the [`Agent` constructor](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__"). **Note**: we're passing the type here, NOT an instance, this parameter is not actually used at runtime, it's here so we can get full type checking of the agent.
3. When running the agent, pass an instance of the dataclass to the `deps` parameter.

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Accessing Dependencies

Dependencies are accessed through the [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") type, this should be the first parameter of system prompt functions etc.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) system\_prompt\_dependencies.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'gateway/openai:gpt-5',
    deps_type=MyDeps,
)


@agent.system_prompt  # (1)!
async defget_system_prompt(ctx: RunContext[MyDeps]) -> str:  # (2)!
    response = await ctx.deps.http_client.get(  # (3)!
        'https://example.com',
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},  # (4)!
    )
    response.raise_for_status()
    return f'Prompt: {response.text}'


async defmain():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run('Tell me a joke.', deps=deps)
        print(result.output)
        #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") may optionally be passed to a [`system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt "system_prompt") function as the only argument.
2. [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") is parameterized with the type of the dependencies, if this type is incorrect, static type checkers will raise an error.
3. Access dependencies through the [`.deps`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.deps "deps            instance-attribute   ") attribute.
4. Access dependencies through the [`.deps`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.deps "deps            instance-attribute   ") attribute.

system\_prompt\_dependencies.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'openai:gpt-5',
    deps_type=MyDeps,
)


@agent.system_prompt  # (1)!
async defget_system_prompt(ctx: RunContext[MyDeps]) -> str:  # (2)!
    response = await ctx.deps.http_client.get(  # (3)!
        'https://example.com',
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},  # (4)!
    )
    response.raise_for_status()
    return f'Prompt: {response.text}'


async defmain():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run('Tell me a joke.', deps=deps)
        print(result.output)
        #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") may optionally be passed to a [`system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt "system_prompt") function as the only argument.
2. [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   ") is parameterized with the type of the dependencies, if this type is incorrect, static type checkers will raise an error.
3. Access dependencies through the [`.deps`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.deps "deps            instance-attribute   ") attribute.
4. Access dependencies through the [`.deps`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.deps "deps            instance-attribute   ") attribute.

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

### Asynchronous vs. Synchronous dependencies

[System prompt functions](https://ai.pydantic.dev/agents/#system-prompts), [function tools](https://ai.pydantic.dev/tools/) and [output validators](https://ai.pydantic.dev/output/#output-validator-functions) are all run in the async context of an agent run.

If these functions are not coroutines (e.g. `async def`) they are called with [`run_in_executor`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor) in a thread pool. It's therefore marginally preferable to use `async` methods where dependencies perform IO, although synchronous dependencies should work fine too.

`run` vs. `run_sync` and Asynchronous vs. Synchronous dependencies

Whether you use synchronous or asynchronous dependencies is completely independent of whether you use `run` or `run_sync` — `run_sync` is just a wrapper around `run` and agents are always run in an async context.

Here's the same example as above, but with a synchronous dependency:

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) sync\_dependencies.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.Client  # (1)!


agent = Agent(
    'gateway/openai:gpt-5',
    deps_type=MyDeps,
)


@agent.system_prompt
defget_system_prompt(ctx: RunContext[MyDeps]) -> str:  # (2)!
    response = ctx.deps.http_client.get(
        'https://example.com', headers={'Authorization': f'Bearer {ctx.deps.api_key}'}
    )
    response.raise_for_status()
    return f'Prompt: {response.text}'


async defmain():
    deps = MyDeps('foobar', httpx.Client())
    result = await agent.run(
        'Tell me a joke.',
        deps=deps,
    )
    print(result.output)
    #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. Here we use a synchronous `httpx.Client` instead of an asynchronous `httpx.AsyncClient`.
2. To match the synchronous dependency, the system prompt function is now a plain function, not a coroutine.

sync\_dependencies.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.Client  # (1)!


agent = Agent(
    'openai:gpt-5',
    deps_type=MyDeps,
)


@agent.system_prompt
defget_system_prompt(ctx: RunContext[MyDeps]) -> str:  # (2)!
    response = ctx.deps.http_client.get(
        'https://example.com', headers={'Authorization': f'Bearer {ctx.deps.api_key}'}
    )
    response.raise_for_status()
    return f'Prompt: {response.text}'


async defmain():
    deps = MyDeps('foobar', httpx.Client())
    result = await agent.run(
        'Tell me a joke.',
        deps=deps,
    )
    print(result.output)
    #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. Here we use a synchronous `httpx.Client` instead of an asynchronous `httpx.AsyncClient`.
2. To match the synchronous dependency, the system prompt function is now a plain function, not a coroutine.

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Full Example

As well as system prompts, dependencies can be used in [tools](https://ai.pydantic.dev/tools/) and [output validators](https://ai.pydantic.dev/output/#output-validator-functions).

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) full\_example.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, ModelRetry, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'gateway/openai:gpt-5',
    deps_type=MyDeps,
)


@agent.system_prompt
async defget_system_prompt(ctx: RunContext[MyDeps]) -> str:
    response = await ctx.deps.http_client.get('https://example.com')
    response.raise_for_status()
    return f'Prompt: {response.text}'


@agent.tool  # (1)!
async defget_joke_material(ctx: RunContext[MyDeps], subject: str) -> str:
    response = await ctx.deps.http_client.get(
        'https://example.com#jokes',
        params={'subject': subject},
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},
    )
    response.raise_for_status()
    return response.text


@agent.output_validator  # (2)!
async defvalidate_output(ctx: RunContext[MyDeps], output: str) -> str:
    response = await ctx.deps.http_client.post(
        'https://example.com#validate',
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},
        params={'query': output},
    )
    if response.status_code == 400:
        raise ModelRetry(f'invalid response: {response.text}')
    response.raise_for_status()
    return output


async defmain():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run('Tell me a joke.', deps=deps)
        print(result.output)
        #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. To pass `RunContext` to a tool, use the [`tool`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool "tool") decorator.
2. `RunContext` may optionally be passed to a [`output_validator`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.output_validator "output_validator") function as the first argument.

full\_example.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, ModelRetry, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'openai:gpt-5',
    deps_type=MyDeps,
)


@agent.system_prompt
async defget_system_prompt(ctx: RunContext[MyDeps]) -> str:
    response = await ctx.deps.http_client.get('https://example.com')
    response.raise_for_status()
    return f'Prompt: {response.text}'


@agent.tool  # (1)!
async defget_joke_material(ctx: RunContext[MyDeps], subject: str) -> str:
    response = await ctx.deps.http_client.get(
        'https://example.com#jokes',
        params={'subject': subject},
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},
    )
    response.raise_for_status()
    return response.text


@agent.output_validator  # (2)!
async defvalidate_output(ctx: RunContext[MyDeps], output: str) -> str:
    response = await ctx.deps.http_client.post(
        'https://example.com#validate',
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},
        params={'query': output},
    )
    if response.status_code == 400:
        raise ModelRetry(f'invalid response: {response.text}')
    response.raise_for_status()
    return output


async defmain():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run('Tell me a joke.', deps=deps)
        print(result.output)
        #> Did you hear about the toothpaste scandal? They called it Colgate.
```

1. To pass `RunContext` to a tool, use the [`tool`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool "tool") decorator.
2. `RunContext` may optionally be passed to a [`output_validator`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.output_validator "output_validator") function as the first argument.

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Overriding Dependencies

When testing agents, it's useful to be able to customise dependencies.

While this can sometimes be done by calling the agent directly within unit tests, we can also override dependencies while calling application code which in turn calls the agent.

This is done via the [`override`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.override "override") method on the agent.

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) joke\_app.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.AsyncClient

    async defsystem_prompt_factory(self) -> str:  # (1)!
        response = await self.http_client.get('https://example.com')
        response.raise_for_status()
        return f'Prompt: {response.text}'


joke_agent = Agent('gateway/openai:gpt-5', deps_type=MyDeps)


@joke_agent.system_prompt
async defget_system_prompt(ctx: RunContext[MyDeps]) -> str:
    return await ctx.deps.system_prompt_factory()  # (2)!


async defapplication_code(prompt: str) -> str:  # (3)!
    ...
    ...
    # now deep within application code we call our agent
    async with httpx.AsyncClient() as client:
        app_deps = MyDeps('foobar', client)
        result = await joke_agent.run(prompt, deps=app_deps)  # (4)!
    return result.output
```

1. Define a method on the dependency to make the system prompt easier to customise.
2. Call the system prompt factory from within the system prompt function.
3. Application code that calls the agent, in a real application this might be an API endpoint.
4. Call the agent from within the application code, in a real application this call might be deep within a call stack. Note `app_deps` here will NOT be used when deps are overridden.

joke\_app.py

```
fromdataclassesimport dataclass

importhttpx

frompydantic_aiimport Agent, RunContext


@dataclass
classMyDeps:
    api_key: str
    http_client: httpx.AsyncClient

    async defsystem_prompt_factory(self) -> str:  # (1)!
        response = await self.http_client.get('https://example.com')
        response.raise_for_status()
        return f'Prompt: {response.text}'


joke_agent = Agent('openai:gpt-5', deps_type=MyDeps)


@joke_agent.system_prompt
async defget_system_prompt(ctx: RunContext[MyDeps]) -> str:
    return await ctx.deps.system_prompt_factory()  # (2)!


async defapplication_code(prompt: str) -> str:  # (3)!
    ...
    ...
    # now deep within application code we call our agent
    async with httpx.AsyncClient() as client:
        app_deps = MyDeps('foobar', client)
        result = await joke_agent.run(prompt, deps=app_deps)  # (4)!
    return result.output
```

1. Define a method on the dependency to make the system prompt easier to customise.
2. Call the system prompt factory from within the system prompt function.
3. Application code that calls the agent, in a real application this might be an API endpoint.
4. Call the agent from within the application code, in a real application this call might be deep within a call stack. Note `app_deps` here will NOT be used when deps are overridden.

*(This example is complete, it can be run "as is")*

test\_joke\_app.py

```
fromjoke_appimport MyDeps, application_code, joke_agent


classTestMyDeps(MyDeps):  # (1)!
    async defsystem_prompt_factory(self) -> str:
        return 'test prompt'


async deftest_application_code():
    test_deps = TestMyDeps('test_key', None)  # (2)!
    with joke_agent.override(deps=test_deps):  # (3)!
        joke = await application_code('Tell me a joke.')  # (4)!
    assert joke.startswith('Did you hear about the toothpaste scandal?')
```

1. Define a subclass of `MyDeps` in tests to customise the system prompt factory.
2. Create an instance of the test dependency, we don't need to pass an `http_client` here as it's not used.
3. Override the dependencies of the agent for the duration of the `with` block, `test_deps` will be used when the agent is run.
4. Now we can safely call our application code, the agent will use the overridden dependencies.

## Examples

The following examples demonstrate how to use dependencies in Pydantic AI:

- [Weather Agent](https://ai.pydantic.dev/examples/weather-agent/)
- [SQL Generation](https://ai.pydantic.dev/examples/sql-gen/)
- [RAG](https://ai.pydantic.dev/examples/rag/)