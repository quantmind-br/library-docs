---
title: Parallel Execution - Pydantic AI
url: https://ai.pydantic.dev/graph/beta/parallel/
source: sitemap
fetched_at: 2026-01-22T22:25:57.740262395-03:00
rendered_js: false
word_count: 579
summary: This document explains how to implement parallel execution in the Pydantic Graph beta API using broadcasting and mapping techniques. It details how to fan out data to multiple steps or iterate over collections for concurrent processing.
tags:
    - pydantic-graph
    - parallel-execution
    - broadcasting
    - mapping
    - async-iterables
    - graph-orchestration
category: guide
---

The beta graph API provides two powerful mechanisms for parallel execution: **broadcasting** and **mapping**.

## Overview

- **Broadcasting** - Send the same data to multiple parallel paths
- **Spreading** - Fan out items from an iterable to parallel paths

Both create "forks" in the execution graph that can later be synchronized with [join nodes](https://ai.pydantic.dev/graph/beta/joins/).

## Broadcasting

Broadcasting sends identical data to multiple destinations simultaneously:

basic\_broadcast.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[int])

    @g.step
    async defsource(ctx: StepContext[SimpleState, None, None]) -> int:
        return 10

    @g.step
    async defadd_one(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs + 1

    @g.step
    async defadd_two(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs + 2

    @g.step
    async defadd_three(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs + 3

    collect = g.join(reduce_list_append, initial_factory=list[int])

    # Broadcasting: send the value from source to all three steps
    g.add(
        g.edge_from(g.start_node).to(source),
        g.edge_from(source).to(add_one, add_two, add_three),
        g.edge_from(add_one, add_two, add_three).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> [11, 12, 13]
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

All three steps receive the same input value (`10`) and execute in parallel.

## Spreading

Spreading fans out elements from an iterable, processing each element in parallel:

basic\_map.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[int])

    @g.step
    async defgenerate_list(ctx: StepContext[SimpleState, None, None]) -> list[int]:
        return [1, 2, 3, 4, 5]

    @g.step
    async defsquare(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs * ctx.inputs

    collect = g.join(reduce_list_append, initial_factory=list[int])

    # Spreading: each item in the list gets its own parallel execution
    g.add(
        g.edge_from(g.start_node).to(generate_list),
        g.edge_from(generate_list).map().to(square),
        g.edge_from(square).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> [1, 4, 9, 16, 25]
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

### Spreading AsyncIterables

The `.map()` operation also works with `AsyncIterable` values. When mapping over an async iterable, the graph creates parallel tasks dynamically as values are yielded. This is particularly useful for streaming data or processing data that's being generated on-the-fly:

async\_iterable\_map.py

```
importasyncio
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[int])

    @g.stream
    async defstream_numbers(ctx: StepContext[SimpleState, None, None]):
"""Stream numbers with delays to simulate real-time data."""
        for i in range(1, 4):
            await asyncio.sleep(0.05)  # Simulate delay
            yield i

    @g.step
    async deftriple(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs * 3

    collect = g.join(reduce_list_append, initial_factory=list[int])

    g.add(
        g.edge_from(g.start_node).to(stream_numbers),
        # Map over the async iterable - tasks created as items are yielded
        g.edge_from(stream_numbers).map().to(triple),
        g.edge_from(triple).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> [3, 6, 9]
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

This allows for progressive processing where downstream steps can start working on early results while later results are still being generated.

### Using `add_mapping_edge()`

The convenience method [`add_mapping_edge()`](https://ai.pydantic.dev/api/pydantic_graph/beta_graph_builder/#pydantic_graph.beta.graph_builder.GraphBuilder.add_mapping_edge "add_mapping_edge") provides a simpler syntax:

mapping\_convenience.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[str])

    @g.step
    async defgenerate_numbers(ctx: StepContext[SimpleState, None, None]) -> list[int]:
        return [10, 20, 30]

    @g.step
    async defstringify(ctx: StepContext[SimpleState, None, int]) -> str:
        return f'Value: {ctx.inputs}'

    collect = g.join(reduce_list_append, initial_factory=list[str])

    g.add(g.edge_from(g.start_node).to(generate_numbers))
    g.add_mapping_edge(generate_numbers, stringify)
    g.add(
        g.edge_from(stringify).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> ['Value: 10', 'Value: 20', 'Value: 30']
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Empty Iterables

When mapping an empty iterable, you can specify a `downstream_join_id` to ensure the join still executes:

empty\_map.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[int])

    @g.step
    async defgenerate_empty(ctx: StepContext[SimpleState, None, None]) -> list[int]:
        return []

    @g.step
    async defdouble(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs * 2

    collect = g.join(reduce_list_append, initial_factory=list[int])

    g.add(g.edge_from(g.start_node).to(generate_empty))
    g.add_mapping_edge(generate_empty, double, downstream_join_id=collect.id)
    g.add(
        g.edge_from(double).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(result)
    #> []
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Nested Parallel Operations

You can nest broadcasts and maps for complex parallel patterns:

### Spread then Broadcast

map\_then\_broadcast.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[int])

    @g.step
    async defgenerate_list(ctx: StepContext[SimpleState, None, None]) -> list[int]:
        return [10, 20]

    @g.step
    async defadd_one(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs + 1

    @g.step
    async defadd_two(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs + 2

    collect = g.join(reduce_list_append, initial_factory=list[int])

    g.add(
        g.edge_from(g.start_node).to(generate_list),
        # Spread the list, then broadcast each item to both steps
        g.edge_from(generate_list).map().to(add_one, add_two),
        g.edge_from(add_one, add_two).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> [11, 12, 21, 22]
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

The result contains: - From 10: `10+1=11` and `10+2=12` - From 20: `20+1=21` and `20+2=22`

### Multiple Sequential Spreads

sequential\_maps.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[str])

    @g.step
    async defgenerate_pairs(ctx: StepContext[SimpleState, None, None]) -> list[tuple[int, int]]:
        return [(1, 2), (3, 4)]

    @g.step
    async defunpack_pair(ctx: StepContext[SimpleState, None, tuple[int, int]]) -> list[int]:
        return [ctx.inputs[0], ctx.inputs[1]]

    @g.step
    async defstringify(ctx: StepContext[SimpleState, None, int]) -> str:
        return f'num:{ctx.inputs}'

    collect = g.join(reduce_list_append, initial_factory=list[str])

    g.add(
        g.edge_from(g.start_node).to(generate_pairs),
        # First map: one task per tuple
        g.edge_from(generate_pairs).map().to(unpack_pair),
        # Second map: one task per number in each tuple
        g.edge_from(unpack_pair).map().to(stringify),
        g.edge_from(stringify).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> ['num:1', 'num:2', 'num:3', 'num:4']
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Edge Labels

Add labels to parallel edges for better documentation:

labeled\_parallel.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[str])

    @g.step
    async defgenerate(ctx: StepContext[SimpleState, None, None]) -> list[int]:
        return [1, 2, 3]

    @g.step
    async defprocess(ctx: StepContext[SimpleState, None, int]) -> str:
        return f'item-{ctx.inputs}'

    collect = g.join(reduce_list_append, initial_factory=list[str])

    g.add(g.edge_from(g.start_node).to(generate))
    g.add_mapping_edge(
        generate,
        process,
        pre_map_label='before map',
        post_map_label='after map',
    )
    g.add(
        g.edge_from(process).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> ['item-1', 'item-2', 'item-3']
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## State Sharing in Parallel Execution

All parallel tasks share the same graph state. Be careful with mutations:

parallel\_state.py

```
fromdataclassesimport dataclass, field

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classCounterState:
    values: list[int] = field(default_factory=list)


async defmain():
    g = GraphBuilder(state_type=CounterState, output_type=list[int])

    @g.step
    async defgenerate(ctx: StepContext[CounterState, None, None]) -> list[int]:
        return [1, 2, 3]

    @g.step
    async deftrack_and_square(ctx: StepContext[CounterState, None, int]) -> int:
        # All parallel tasks mutate the same state
        ctx.state.values.append(ctx.inputs)
        return ctx.inputs * ctx.inputs

    collect = g.join(reduce_list_append, initial_factory=list[int])

    g.add(
        g.edge_from(g.start_node).to(generate),
        g.edge_from(generate).map().to(track_and_square),
        g.edge_from(track_and_square).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    state = CounterState()
    result = await graph.run(state=state)

    print(f'Squared: {sorted(result)}')
    #> Squared: [1, 4, 9]
    print(f'Tracked: {sorted(state.values)}')
    #> Tracked: [1, 2, 3]
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Edge Transformations

You can transform data inline as it flows along edges using the `.transform()` method:

edge\_transform.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=str)

    @g.step
    async defgenerate_number(ctx: StepContext[SimpleState, None, None]) -> int:
        return 42

    @g.step
    async defformat_output(ctx: StepContext[SimpleState, None, str]) -> str:
        return f'The answer is: {ctx.inputs}'

    # Transform the number to a string inline
    g.add(
        g.edge_from(g.start_node).to(generate_number),
        g.edge_from(generate_number).transform(lambda ctx: str(ctx.inputs * 2)).to(format_output),
        g.edge_from(format_output).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(result)
    #> The answer is: 84
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

The transform function receives a [`StepContext`](https://ai.pydantic.dev/api/pydantic_graph/beta_step/#pydantic_graph.beta.step.StepContext "StepContext            dataclass   ") with the current inputs and has access to state and dependencies. This is useful for:

- Converting data types between incompatible steps
- Extracting specific fields from complex objects
- Applying simple computations without creating a full step
- Adapting data formats during routing

Transforms can be chained and combined with other edge operations like `.map()` and `.label()`:

chained\_transforms.py

```
fromdataclassesimport dataclass

frompydantic_graph.betaimport GraphBuilder, StepContext
frompydantic_graph.beta.joinimport reduce_list_append


@dataclass
classSimpleState:
    pass


async defmain():
    g = GraphBuilder(state_type=SimpleState, output_type=list[str])

    @g.step
    async defgenerate_data(ctx: StepContext[SimpleState, None, None]) -> list[dict[str, int]]:
        return [{'value': 10}, {'value': 20}, {'value': 30}]

    @g.step
    async defprocess_number(ctx: StepContext[SimpleState, None, int]) -> str:
        return f'Processed: {ctx.inputs}'

    collect = g.join(reduce_list_append, initial_factory=list[str])

    g.add(
        g.edge_from(g.start_node).to(generate_data),
        # Transform to extract values, then map over them
        g.edge_from(generate_data)
        .transform(lambda ctx: [item['value'] for item in ctx.inputs])
        .label('Extract values')
        .map()
        .to(process_number),
        g.edge_from(process_number).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result = await graph.run(state=SimpleState())
    print(sorted(result))
    #> ['Processed: 10', 'Processed: 20', 'Processed: 30']
```

*(This example is complete, it can be run "as is" — you'll need to add `import asyncio; asyncio.run(main())` to run `main`)*

## Next Steps

- Learn about [join nodes](https://ai.pydantic.dev/graph/beta/joins/) for aggregating parallel results
- Explore [conditional branching](https://ai.pydantic.dev/graph/beta/decisions/) with decision nodes
- See the [steps documentation](https://ai.pydantic.dev/graph/beta/steps/) for more on step execution