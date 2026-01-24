---
title: Steps - Pydantic AI
url: https://ai.pydantic.dev/graph/beta/steps/
source: sitemap
fetched_at: 2026-01-22T22:25:59.956160926-03:00
rendered_js: false
word_count: 495
summary: This document explains how to define and use steps as the fundamental units of work in a graph, covering step creation, state management, dependency injection, and customization.
tags:
    - pydantic-graph
    - python
    - asynchronous
    - state-management
    - dependency-injection
    - graph-builder
    - step-context
category: guide
---

Steps are the fundamental units of work in a graph. They're async functions that receive a [`StepContext`](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepContext "StepContext            dataclass   ") and return a value.

## Creating Steps

Steps are created using the [`@g.step`](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.step "step") decorator on the [`GraphBuilder`](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder "GraphBuilder            dataclass   "):

basic\_step.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classMyState:
    counter: int = 0

g = GraphBuilder(state_type=MyState, output_type=int)

@g.step
async defincrement(ctx: StepContext[MyState, None, None]) -> int:
    ctx.state.counter += 1
    return ctx.state.counter

g.add(
    g.edge_from(g.start_node).to(increment),
    g.edge_from(increment).to(g.end_node),
)

graph = g.build()

async defmain():
    state = MyState()
    result = await graph.run(state=state)
    print(result)
    #> 1
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Step Context

Every step function receives a [`StepContext`](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepContext "StepContext            dataclass   ") as its first parameter. The context provides access to:

- `ctx.state` - The mutable graph state (type: `StateT`)
- `ctx.deps` - Injected dependencies (type: `DepsT`)
- `ctx.inputs` - Input data for this step (type: `InputT`)

### Accessing State

State is shared across all steps in a graph and can be freely mutated:

state\_access.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classAppState:
    messages: list[str]


async defmain():
    g = GraphBuilder(state_type=AppState, output_type=list[str])

    @g.step
    async defadd_hello(ctx: StepContext[AppState, None, None]) -> None:
        ctx.state.messages.append('Hello')

    @g.step
    async defadd_world(ctx: StepContext[AppState, None, None]) -> None:
        ctx.state.messages.append('World')

    @g.step
    async defget_messages(ctx: StepContext[AppState, None, None]) -> list[str]:
        return ctx.state.messages

    g.add(
        g.edge_from(g.start_node).to(add_hello),
        g.edge_from(add_hello).to(add_world),
        g.edge_from(add_world).to(get_messages),
        g.edge_from(get_messages).to(g.end_node),
    )

    graph = g.build()
    state = AppState(messages=[])
    result = await graph.run(state=state)
    print(result)
    #> ['Hello', 'World']
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

### Working with Inputs

Steps can receive and transform input data:

step\_inputs.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(
        state_type=SimpleState,
        input_type=int,
        output_type=str,
    )

    @g.step
    async defdouble_it(ctx: StepContext[SimpleState, None, int]) -> int:
"""Double the input value."""
        return ctx.inputs * 2

    @g.step
    async defstringify(ctx: StepContext[SimpleState, None, int]) -> str:
"""Convert to a formatted string."""
        return f'Result: {ctx.inputs}'

    g.add(
        g.edge_from(g.start_node).to(double_it),
        g.edge_from(double_it).to(stringify),
        g.edge_from(stringify).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState(), inputs=21)
    print(result)
    #> Result: 42
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Dependency Injection

Steps can access injected dependencies through `ctx.deps`:

dependencies.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classAppState:
    pass


@dataclass
classAppDeps:
"""Dependencies injected into the graph."""

    multiplier: int


async defmain():
    g = GraphBuilder(
        state_type=AppState,
        deps_type=AppDeps,
        input_type=int,
        output_type=int,
    )

    @g.step
    async defmultiply(ctx: StepContext[AppState, AppDeps, int]) -> int:
"""Multiply input by the injected multiplier."""
        return ctx.inputs * ctx.deps.multiplier

    g.add(
        g.edge_from(g.start_node).to(multiply),
        g.edge_from(multiply).to(g.end_node),
    )

    graph = g.build()
    deps = AppDeps(multiplier=10)
    result = await graph.run(state=AppState(), deps=deps, inputs=5)
    print(result)
    #> 50
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Customizing Steps

### Custom Node IDs

By default, step node IDs are inferred from the function name. You can override this:

custom\_id.py

```
frompydantic_graph.betaimport StepContext

frombasic_stepimport MyState, g


@g.step(node_id='my_custom_id')
async defmy_step(ctx: StepContext[MyState, None, None]) -> int:
    return 42

# The node ID is now 'my_custom_id' instead of 'my_step'
```

### Human-Readable Labels

Labels provide documentation for diagram generation:

labels.py

```
frompydantic_graph.betaimport StepContext

frombasic_stepimport MyState, g


@g.step(label='Increment the counter')
async defincrement(ctx: StepContext[MyState, None, None]) -> int:
    ctx.state.counter += 1
    return ctx.state.counter

# Access the label programmatically
print(increment.label)
#> Increment the counter
```

## Sequential Steps

Multiple steps can be chained sequentially:

sequential.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classMathState:
    operations: list[str]


async defmain():
    g = GraphBuilder(
        state_type=MathState,
        input_type=int,
        output_type=int,
    )

    @g.step
    async defadd_five(ctx: StepContext[MathState, None, int]) -> int:
        ctx.state.operations.append('add 5')
        return ctx.inputs + 5

    @g.step
    async defmultiply_by_two(ctx: StepContext[MathState, None, int]) -> int:
        ctx.state.operations.append('multiply by 2')
        return ctx.inputs * 2

    @g.step
    async defsubtract_three(ctx: StepContext[MathState, None, int]) -> int:
        ctx.state.operations.append('subtract 3')
        return ctx.inputs - 3

    # Connect steps sequentially
    g.add(
        g.edge_from(g.start_node).to(add_five),
        g.edge_from(add_five).to(multiply_by_two),
        g.edge_from(multiply_by_two).to(subtract_three),
        g.edge_from(subtract_three).to(g.end_node),
    )

    graph = g.build()
    state = MathState(operations=[])
    result = await graph.run(state=state, inputs=10)

    print(f'Result: {result}')
    #> Result: 27
    print(f'Operations: {state.operations}')
    #> Operations: ['add 5', 'multiply by 2', 'subtract 3']
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

The computation is: `(10 + 5) * 2 - 3 = 27`

## Streaming Steps

In addition to regular steps that return a single value, you can create streaming steps that yield multiple values over time using the [`@g.stream`](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.stream "stream") decorator:

streaming\_step.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


g = GraphBuilder(state_type=SimpleState, output_type=list[int])

@g.stream
async defgenerate_stream(ctx: StepContext[SimpleState, None, None]):
"""Stream numbers from 1 to 5."""
    for i in range(1, 6):
        yield i

@g.step
async defsquare(ctx: StepContext[SimpleState, None, int]) -> int:
    return ctx.inputs * ctx.inputs

collect = g.join(reduce_list_append, initial_factory=list[int])

g.add(
    g.edge_from(g.start_node).to(generate_stream),
    # The stream output is an AsyncIterable, so we can map over it
    g.edge_from(generate_stream).map().to(square),
    g.edge_from(square).to(collect),
    g.edge_from(collect).to(g.end_node),
)

graph = g.build()

async defmain():
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> [1, 4, 9, 16, 25]
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

### How Streaming Steps Work

Streaming steps return an `AsyncIterable` that yields values over time. When you use `.map()` on a streaming step's output, the graph processes each yielded value as it becomes available, creating parallel tasks dynamically. This is particularly useful for:

- Processing data from APIs that stream responses
- Handling real-time data feeds
- Progressive processing of large datasets
- Any scenario where you want to start processing results before all data is available

Like regular steps, streaming steps can also have custom node IDs and labels:

labeled\_stream.py

```
frompydantic_graph.betaimport StepContext

fromstreaming_stepimport SimpleState, g


@g.stream(node_id='my_stream', label='Generate numbers progressively')
async deflabeled_stream(ctx: StepContext[SimpleState, None, None]):
    for i in range(10):
        yield i
```

## Edge Building Convenience Methods

The builder provides helper methods for common edge patterns:

### Simple Edges with `add_edge()`

add\_edge\_example.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=int)

    @g.step
    async defstep_a(ctx: StepContext[SimpleState, None, None]) -> int:
        return 10

    @g.step
    async defstep_b(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs + 5

    # Using add_edge() for simple connections
    g.add_edge(g.start_node, step_a)
    g.add_edge(step_a, step_b, label='from a to b')
    g.add_edge(step_b, g.end_node)

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(result)
    #> 15
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Type Safety

The beta graph API provides strong type checking through generics. Type parameters on [`StepContext`](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepContext "StepContext            dataclass   ") ensure:

- State access is properly typed
- Dependencies are correctly typed
- Input/output types match across edges

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classMyState:
    pass

g = GraphBuilder(state_type=MyState, output_type=str)

# Type checker will catch mismatches
@g.step
async defexpects_int(ctx: StepContext[MyState, None, int]) -> str:
    return str(ctx.inputs)

@g.step
async defreturns_str(ctx: StepContext[MyState, None, None]) -> str:
    return 'hello'

# This would be a type error - expects_int needs int input, but returns_str outputs str
# g.add(g.edge_from(returns_str).to(expects_int))  # Type error!
```

## Next Steps

- Learn about [parallel execution](https://ai.pydantic.dev/graph/beta/parallel/) with broadcasting and mapping
- Understand [join nodes](https://ai.pydantic.dev/graph/beta/joins/) for aggregating parallel results
- Explore [conditional branching](https://ai.pydantic.dev/graph/beta/decisions/) with decision nodes