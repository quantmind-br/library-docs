---
title: Overview - Pydantic AI
url: https://ai.pydantic.dev/graph/
source: sitemap
fetched_at: 2026-01-22T22:23:28.774628238-03:00
rendered_js: false
word_count: 3116
summary: This document introduces pydantic-graph, a type-safe library for building asynchronous graphs and finite state machines to model and control complex workflows in Python.
tags:
    - pydantic-graph
    - state-machine
    - python
    - type-hints
    - asynchronous-programming
    - workflow-automation
category: concept
---

## Graphs

Don't use a nail gun unless you need a nail gun

If Pydantic AI [agents](https://ai.pydantic.dev/agents/) are a hammer, and [multi-agent workflows](https://ai.pydantic.dev/multi-agent-applications/) are a sledgehammer, then graphs are a nail gun:

- sure, nail guns look cooler than hammers
- but nail guns take a lot more setup than hammers
- and nail guns don't make you a better builder, they make you a builder with a nail gun
- Lastly, (and at the risk of torturing this metaphor), if you're a fan of medieval tools like mallets and untyped Python, you probably won't like nail guns or our approach to graphs. (But then again, if you're not a fan of type hints in Python, you've probably already bounced off Pydantic AI to use one of the toy agent frameworks — good luck, and feel free to borrow my sledgehammer when you realize you need it)

In short, graphs are a powerful tool, but they're not the right tool for every job. Please consider other [multi-agent approaches](https://ai.pydantic.dev/multi-agent-applications/) before proceeding.

If you're not confident a graph-based approach is a good idea, it might be unnecessary.

Graphs and finite state machines (FSMs) are a powerful abstraction to model, execute, control and visualize complex workflows.

Alongside Pydantic AI, we've developed `pydantic-graph` — an async graph and state machine library for Python where nodes and edges are defined using type hints.

While this library is developed as part of Pydantic AI; it has no dependency on `pydantic-ai` and can be considered as a pure graph-based state machine library. You may find it useful whether or not you're using Pydantic AI or even building with GenAI.

`pydantic-graph` is designed for advanced users and makes heavy use of Python generics and type hints. It is not designed to be as beginner-friendly as Pydantic AI.

## Installation

`pydantic-graph` is a required dependency of `pydantic-ai`, and an optional dependency of `pydantic-ai-slim`, see [installation instructions](https://ai.pydantic.dev/install/#slim-install) for more information. You can also install it directly:

pipuv

```
pipinstallpydantic-graph
```

## Graph Types

`pydantic-graph` is made up of a few key components:

### GraphRunContext

[`GraphRunContext`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.GraphRunContext "GraphRunContext            dataclass   ") — The context for the graph run, similar to Pydantic AI's [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext            dataclass   "). This holds the state of the graph and dependencies and is passed to nodes when they're run.

`GraphRunContext` is generic in the state type of the graph it's used in, [`StateT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT            module-attribute   ").

### End

[`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End            dataclass   ") — return value to indicate the graph run should end.

`End` is generic in the graph return type of the graph it's used in, [`RunEndT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT            module-attribute   ").

### Nodes

Subclasses of [`BaseNode`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode") define nodes for execution in the graph.

Nodes, which are generally [`dataclass`es](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass), generally consist of:

- fields containing any parameters required/optional when calling the node
- the business logic to execute the node, in the [`run`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode.run "run            abstractmethod       async   ") method
- return annotations of the [`run`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode.run "run            abstractmethod       async   ") method, which are read by `pydantic-graph` to determine the outgoing edges of the node

Nodes are generic in:

- **state**, which must have the same type as the state of graphs they're included in, [`StateT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT            module-attribute   ") has a default of `None`, so if you're not using state you can omit this generic parameter, see [stateful graphs](#stateful-graphs) for more information
- **deps**, which must have the same type as the deps of the graph they're included in, [`DepsT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT            module-attribute   ") has a default of `None`, so if you're not using deps you can omit this generic parameter, see [dependency injection](#dependency-injection) for more information
- **graph return type** — this only applies if the node returns [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End            dataclass   "). [`RunEndT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT            module-attribute   ") has a default of [Never](https://docs.python.org/3/library/typing.html#typing.Never) so this generic parameter can be omitted if the node doesn't return `End`, but must be included if it does.

Here's an example of a start or intermediate node in a graph — it can't end the run as it doesn't return [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End            dataclass   "):

intermediate\_node.py

```
fromdataclassesimport dataclass

frompydantic_graphimport BaseNode, GraphRunContext


@dataclass
classMyNode(BaseNode[MyState]):  # (1)!
    foo: int  # (2)!

    async defrun(
        self,
        ctx: GraphRunContext[MyState],  # (3)!
    ) -> AnotherNode:  # (4)!
        ...
        return AnotherNode()
```

1. State in this example is `MyState` (not shown), hence `BaseNode` is parameterized with `MyState`. This node can't end the run, so the `RunEndT` generic parameter is omitted and defaults to `Never`.
2. `MyNode` is a dataclass and has a single field `foo`, an `int`.
3. The `run` method takes a `GraphRunContext` parameter, again parameterized with state `MyState`.
4. The return type of the `run` method is `AnotherNode` (not shown), this is used to determine the outgoing edges of the node.

We could extend `MyNode` to optionally end the run if `foo` is divisible by 5:

intermediate\_or\_end\_node.py

```
fromdataclassesimport dataclass

frompydantic_graphimport BaseNode, End, GraphRunContext


@dataclass
classMyNode(BaseNode[MyState, None, int]):  # (1)!
    foo: int

    async defrun(
        self,
        ctx: GraphRunContext[MyState],
    ) -> AnotherNode | End[int]:  # (2)!
        if self.foo % 5 == 0:
            return End(self.foo)
        else:
            return AnotherNode()
```

1. We parameterize the node with the return type (`int` in this case) as well as state. Because generic parameters are positional-only, we have to include `None` as the second parameter representing deps.
2. The return type of the `run` method is now a union of `AnotherNode` and `End[int]`, this allows the node to end the run if `foo` is divisible by 5.

### Graph

[`Graph`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "Graph            dataclass   ") — this is the execution graph itself, made up of a set of [node classes](#nodes) (i.e., `BaseNode` subclasses).

`Graph` is generic in:

- **state** the state type of the graph, [`StateT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.StateT "StateT            module-attribute   ")
- **deps** the deps type of the graph, [`DepsT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.DepsT "DepsT            module-attribute   ")
- **graph return type** the return type of the graph run, [`RunEndT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT            module-attribute   ")

Here's an example of a simple graph:

graph\_example.py

```
from__future__import annotations

fromdataclassesimport dataclass

frompydantic_graphimport BaseNode, End, Graph, GraphRunContext


@dataclass
classDivisibleBy5(BaseNode[None, None, int]):  # (1)!
    foo: int

    async defrun(
        self,
        ctx: GraphRunContext,
    ) -> Increment | End[int]:
        if self.foo % 5 == 0:
            return End(self.foo)
        else:
            return Increment(self.foo)


@dataclass
classIncrement(BaseNode):  # (2)!
    foo: int

    async defrun(self, ctx: GraphRunContext) -> DivisibleBy5:
        return DivisibleBy5(self.foo + 1)


fives_graph = Graph(nodes=[DivisibleBy5, Increment])  # (3)!
result = fives_graph.run_sync(DivisibleBy5(4))  # (4)!
print(result.output)
#> 5
```

1. The `DivisibleBy5` node is parameterized with `None` for the state param and `None` for the deps param as this graph doesn't use state or deps, and `int` as it can end the run.
2. The `Increment` node doesn't return `End`, so the `RunEndT` generic parameter is omitted, state can also be omitted as the graph doesn't use state.
3. The graph is created with a sequence of nodes.
4. The graph is run synchronously with [`run_sync`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.run_sync "run_sync"). The initial node is `DivisibleBy5(4)`. Because the graph doesn't use external state or deps, we don't pass `state` or `deps`.

*(This example is complete, it can be run "as is")*

A [mermaid diagram](#mermaid-diagrams) for this graph can be generated with the following code:

graph\_example\_diagram.py

```
fromgraph_exampleimport DivisibleBy5, fives_graph

fives_graph.mermaid_code(start_node=DivisibleBy5)
```

```
---
title: fives_graph
---
stateDiagram-v2
  [*] --> DivisibleBy5
  DivisibleBy5 --> Increment
  DivisibleBy5 --> [*]
  Increment --> DivisibleBy5
```

In order to visualize a graph within a `jupyter-notebook`, `IPython.display` needs to be used:

jupyter\_display\_mermaid.py

```
fromgraph_exampleimport DivisibleBy5, fives_graph
fromIPython.displayimport Image, display

display(Image(fives_graph.mermaid_image(start_node=DivisibleBy5)))
```

## Stateful Graphs

The "state" concept in `pydantic-graph` provides an optional way to access and mutate an object (often a `dataclass` or Pydantic model) as nodes run in a graph. If you think of Graphs as a production line, then your state is the engine being passed along the line and built up by each node as the graph is run.

`pydantic-graph` provides state persistence, with the state recorded after each node is run. (See [State Persistence](#state-persistence).)

Here's an example of a graph which represents a vending machine where the user may insert coins and select a product to purchase.

vending\_machine.py

```
from__future__import annotations

fromdataclassesimport dataclass

fromrich.promptimport Prompt

frompydantic_graphimport BaseNode, End, Graph, GraphRunContext


@dataclass
classMachineState:  # (1)!
    user_balance: float = 0.0
    product: str | None = None


@dataclass
classInsertCoin(BaseNode[MachineState]):  # (3)!
    async defrun(self, ctx: GraphRunContext[MachineState]) -> CoinsInserted:  # (16)!
        return CoinsInserted(float(Prompt.ask('Insert coins')))  # (4)!


@dataclass
classCoinsInserted(BaseNode[MachineState]):
    amount: float  # (5)!

    async defrun(
        self, ctx: GraphRunContext[MachineState]
    ) -> SelectProduct | Purchase:  # (17)!
        ctx.state.user_balance += self.amount  # (6)!
        if ctx.state.product is not None:  # (7)!
            return Purchase(ctx.state.product)
        else:
            return SelectProduct()


@dataclass
classSelectProduct(BaseNode[MachineState]):
    async defrun(self, ctx: GraphRunContext[MachineState]) -> Purchase:
        return Purchase(Prompt.ask('Select product'))


PRODUCT_PRICES = {  # (2)!
    'water': 1.25,
    'soda': 1.50,
    'crisps': 1.75,
    'chocolate': 2.00,
}


@dataclass
classPurchase(BaseNode[MachineState, None, None]):  # (18)!
    product: str

    async defrun(
        self, ctx: GraphRunContext[MachineState]
    ) -> End | InsertCoin | SelectProduct:
        if price := PRODUCT_PRICES.get(self.product):  # (8)!
            ctx.state.product = self.product  # (9)!
            if ctx.state.user_balance >= price:  # (10)!
                ctx.state.user_balance -= price
                return End(None)
            else:
                diff = price - ctx.state.user_balance
                print(f'Not enough money for {self.product}, need {diff:0.2f} more')
                #> Not enough money for crisps, need 0.75 more
                return InsertCoin()  # (11)!
        else:
            print(f'No such product: {self.product}, try again')
            return SelectProduct()  # (12)!


vending_machine_graph = Graph(  # (13)!
    nodes=[InsertCoin, CoinsInserted, SelectProduct, Purchase]
)


async defmain():
    state = MachineState()  # (14)!
    await vending_machine_graph.run(InsertCoin(), state=state)  # (15)!
    print(f'purchase successful item={state.product} change={state.user_balance:0.2f}')
    #> purchase successful item=crisps change=0.25
```

01. The state of the vending machine is defined as a dataclass with the user's balance and the product they've selected, if any.
02. A dictionary of products mapped to prices.
03. The `InsertCoin` node, [`BaseNode`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode") is parameterized with `MachineState` as that's the state used in this graph.
04. The `InsertCoin` node prompts the user to insert coins. We keep things simple by just entering a monetary amount as a float. Before you start thinking this is a toy too since it's using [rich's `Prompt.ask`](https://rich.readthedocs.io/en/stable/reference/prompt.html#rich.prompt.PromptBase.ask) within nodes, see [below](#example-human-in-the-loop) for how control flow can be managed when nodes require external input.
05. The `CoinsInserted` node; again this is a [`dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass) with one field `amount`.
06. Update the user's balance with the amount inserted.
07. If the user has already selected a product, go to `Purchase`, otherwise go to `SelectProduct`.
08. In the `Purchase` node, look up the price of the product if the user entered a valid product.
09. If the user did enter a valid product, set the product in the state so we don't revisit `SelectProduct`.
10. If the balance is enough to purchase the product, adjust the balance to reflect the purchase and return [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End            dataclass   ") to end the graph. We're not using the run return type, so we call `End` with `None`.
11. If the balance is insufficient, go to `InsertCoin` to prompt the user to insert more coins.
12. If the product is invalid, go to `SelectProduct` to prompt the user to select a product again.
13. The graph is created by passing a list of nodes to [`Graph`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "Graph            dataclass   "). Order of nodes is not important, but it can affect how [diagrams](#mermaid-diagrams) are displayed.
14. Initialize the state. This will be passed to the graph run and mutated as the graph runs.
15. Run the graph with the initial state. Since the graph can be run from any node, we must pass the start node — in this case, `InsertCoin`. [`Graph.run`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.run "run            async   ") returns a [`GraphRunResult`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRunResult "GraphRunResult            dataclass   ") that provides the final data and a history of the run.
16. The return type of the node's [`run`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode.run "run            abstractmethod       async   ") method is important as it is used to determine the outgoing edges of the node. This information in turn is used to render [mermaid diagrams](#mermaid-diagrams) and is enforced at runtime to detect misbehavior as soon as possible.
17. The return type of `CoinsInserted`'s [`run`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode.run "run            abstractmethod       async   ") method is a union, meaning multiple outgoing edges are possible.
18. Unlike other nodes, `Purchase` can end the run, so the [`RunEndT`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "RunEndT            module-attribute   ") generic parameter must be set. In this case it's `None` since the graph run return type is `None`.

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

A [mermaid diagram](#mermaid-diagrams) for this graph can be generated with the following code:

vending\_machine\_diagram.py

```
fromvending_machineimport InsertCoin, vending_machine_graph

vending_machine_graph.mermaid_code(start_node=InsertCoin)
```

The diagram generated by the above code is:

```
---
title: vending_machine_graph
---
stateDiagram-v2
  [*] --> InsertCoin
  InsertCoin --> CoinsInserted
  CoinsInserted --> SelectProduct
  CoinsInserted --> Purchase
  SelectProduct --> Purchase
  Purchase --> InsertCoin
  Purchase --> SelectProduct
  Purchase --> [*]
```

See [below](#mermaid-diagrams) for more information on generating diagrams.

## GenAI Example

So far we haven't shown an example of a Graph that actually uses Pydantic AI or GenAI at all.

In this example, one agent generates a welcome email to a user and the other agent provides feedback on the email.

This graph has a very simple structure:

```
---
title: feedback_graph
---
stateDiagram-v2
  [*] --> WriteEmail
  WriteEmail --> Feedback
  Feedback --> WriteEmail
  Feedback --> [*]
```

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) genai\_email\_feedback.py

```
from__future__import annotations as _annotations

fromdataclassesimport dataclass, field

frompydanticimport BaseModel, EmailStr

frompydantic_aiimport Agent, ModelMessage, format_as_xml
frompydantic_graphimport BaseNode, End, Graph, GraphRunContext


@dataclass
classUser:
    name: str
    email: EmailStr
    interests: list[str]


@dataclass
classEmail:
    subject: str
    body: str


@dataclass
classState:
    user: User
    write_agent_messages: list[ModelMessage] = field(default_factory=list)


email_writer_agent = Agent(
    'gateway/gemini:gemini-2.5-pro',
    output_type=Email,
    system_prompt='Write a welcome email to our tech blog.',
)


@dataclass
classWriteEmail(BaseNode[State]):
    email_feedback: str | None = None

    async defrun(self, ctx: GraphRunContext[State]) -> Feedback:
        if self.email_feedback:
            prompt = (
                f'Rewrite the email for the user:\n'
                f'{format_as_xml(ctx.state.user)}\n'
                f'Feedback: {self.email_feedback}'
            )
        else:
            prompt = (
                f'Write a welcome email for the user:\n'
                f'{format_as_xml(ctx.state.user)}'
            )

        result = await email_writer_agent.run(
            prompt,
            message_history=ctx.state.write_agent_messages,
        )
        ctx.state.write_agent_messages += result.new_messages()
        return Feedback(result.output)


classEmailRequiresWrite(BaseModel):
    feedback: str


classEmailOk(BaseModel):
    pass


feedback_agent = Agent[None, EmailRequiresWrite | EmailOk](
    'openai:gpt-5',
    output_type=EmailRequiresWrite | EmailOk,  # type: ignore
    system_prompt=(
        'Review the email and provide feedback, email must reference the users specific interests.'
    ),
)


@dataclass
classFeedback(BaseNode[State, None, Email]):
    email: Email

    async defrun(
        self,
        ctx: GraphRunContext[State],
    ) -> WriteEmail | End[Email]:
        prompt = format_as_xml({'user': ctx.state.user, 'email': self.email})
        result = await feedback_agent.run(prompt)
        if isinstance(result.output, EmailRequiresWrite):
            return WriteEmail(email_feedback=result.output.feedback)
        else:
            return End(self.email)


async defmain():
    user = User(
        name='John Doe',
        email='john.joe@example.com',
        interests=['Haskel', 'Lisp', 'Fortran'],
    )
    state = State(user)
    feedback_graph = Graph(nodes=(WriteEmail, Feedback))
    result = await feedback_graph.run(WriteEmail(), state=state)
    print(result.output)
"""
    Email(
        subject='Welcome to our tech blog!',
        body='Hello John, Welcome to our tech blog! ...',
    )
    """
```

genai\_email\_feedback.py

```
from__future__import annotations as _annotations

fromdataclassesimport dataclass, field

frompydanticimport BaseModel, EmailStr

frompydantic_aiimport Agent, ModelMessage, format_as_xml
frompydantic_graphimport BaseNode, End, Graph, GraphRunContext


@dataclass
classUser:
    name: str
    email: EmailStr
    interests: list[str]


@dataclass
classEmail:
    subject: str
    body: str


@dataclass
classState:
    user: User
    write_agent_messages: list[ModelMessage] = field(default_factory=list)


email_writer_agent = Agent(
    'google-gla:gemini-2.5-pro',
    output_type=Email,
    system_prompt='Write a welcome email to our tech blog.',
)


@dataclass
classWriteEmail(BaseNode[State]):
    email_feedback: str | None = None

    async defrun(self, ctx: GraphRunContext[State]) -> Feedback:
        if self.email_feedback:
            prompt = (
                f'Rewrite the email for the user:\n'
                f'{format_as_xml(ctx.state.user)}\n'
                f'Feedback: {self.email_feedback}'
            )
        else:
            prompt = (
                f'Write a welcome email for the user:\n'
                f'{format_as_xml(ctx.state.user)}'
            )

        result = await email_writer_agent.run(
            prompt,
            message_history=ctx.state.write_agent_messages,
        )
        ctx.state.write_agent_messages += result.new_messages()
        return Feedback(result.output)


classEmailRequiresWrite(BaseModel):
    feedback: str


classEmailOk(BaseModel):
    pass


feedback_agent = Agent[None, EmailRequiresWrite | EmailOk](
    'openai:gpt-5',
    output_type=EmailRequiresWrite | EmailOk,  # type: ignore
    system_prompt=(
        'Review the email and provide feedback, email must reference the users specific interests.'
    ),
)


@dataclass
classFeedback(BaseNode[State, None, Email]):
    email: Email

    async defrun(
        self,
        ctx: GraphRunContext[State],
    ) -> WriteEmail | End[Email]:
        prompt = format_as_xml({'user': ctx.state.user, 'email': self.email})
        result = await feedback_agent.run(prompt)
        if isinstance(result.output, EmailRequiresWrite):
            return WriteEmail(email_feedback=result.output.feedback)
        else:
            return End(self.email)


async defmain():
    user = User(
        name='John Doe',
        email='john.joe@example.com',
        interests=['Haskel', 'Lisp', 'Fortran'],
    )
    state = State(user)
    feedback_graph = Graph(nodes=(WriteEmail, Feedback))
    result = await feedback_graph.run(WriteEmail(), state=state)
    print(result.output)
"""
    Email(
        subject='Welcome to our tech blog!',
        body='Hello John, Welcome to our tech blog! ...',
    )
    """
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Iterating Over a Graph

### Using `Graph.iter` for `async for` iteration

Sometimes you want direct control or insight into each node as the graph executes. The easiest way to do that is with the [`Graph.iter`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.iter "iter            async   ") method, which returns a **context manager** that yields a [`GraphRun`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun "GraphRun") object. The `GraphRun` is an async-iterable over the nodes of your graph, allowing you to record or modify them as they execute.

Here's an example:

count\_down.py

```
from__future__import annotations as _annotations

fromdataclassesimport dataclass
frompydantic_graphimport Graph, BaseNode, End, GraphRunContext


@dataclass
classCountDownState:
    counter: int


@dataclass
classCountDown(BaseNode[CountDownState, None, int]):
    async defrun(self, ctx: GraphRunContext[CountDownState]) -> CountDown | End[int]:
        if ctx.state.counter <= 0:
            return End(ctx.state.counter)
        ctx.state.counter -= 1
        return CountDown()


count_down_graph = Graph(nodes=[CountDown])


async defmain():
    state = CountDownState(counter=3)
    async with count_down_graph.iter(CountDown(), state=state) as run:  # (1)!
        async for node in run:  # (2)!
            print('Node:', node)
            #> Node: CountDown()
            #> Node: CountDown()
            #> Node: CountDown()
            #> Node: CountDown()
            #> Node: End(data=0)
    print('Final output:', run.result.output)  # (3)!
    #> Final output: 0
```

1. `Graph.iter(...)` returns a [`GraphRun`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun "GraphRun").
2. Here, we step through each node as it is executed.
3. Once the graph returns an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End            dataclass   "), the loop ends, and `run.result` becomes a [`GraphRunResult`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRunResult "GraphRunResult            dataclass   ") containing the final outcome (`0` here).

### Using `GraphRun.next(node)` manually

Alternatively, you can drive iteration manually with the [`GraphRun.next`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun.next "next            async   ") method, which allows you to pass in whichever node you want to run next. You can modify or selectively skip nodes this way.

Below is a contrived example that stops whenever the counter is at 2, ignoring any node runs beyond that:

count\_down\_next.py

```
frompydantic_graphimport End, FullStatePersistence
fromcount_downimport CountDown, CountDownState, count_down_graph


async defmain():
    state = CountDownState(counter=5)
    persistence = FullStatePersistence()  # (7)!
    async with count_down_graph.iter(
        CountDown(), state=state, persistence=persistence
    ) as run:
        node = run.next_node  # (1)!
        while not isinstance(node, End):  # (2)!
            print('Node:', node)
            #> Node: CountDown()
            #> Node: CountDown()
            #> Node: CountDown()
            #> Node: CountDown()
            if state.counter == 2:
                break  # (3)!
            node = await run.next(node)  # (4)!

        print(run.result)  # (5)!
        #> None

        for step in persistence.history:  # (6)!
            print('History Step:', step.state, step.state)
            #> History Step: CountDownState(counter=5) CountDownState(counter=5)
            #> History Step: CountDownState(counter=4) CountDownState(counter=4)
            #> History Step: CountDownState(counter=3) CountDownState(counter=3)
            #> History Step: CountDownState(counter=2) CountDownState(counter=2)
```

1. We start by grabbing the first node that will be run in the agent's graph.
2. The agent run is finished once an `End` node has been produced; instances of `End` cannot be passed to `next`.
3. If the user decides to stop early, we break out of the loop. The graph run won't have a real final result in that case (`run.result` remains `None`).
4. At each step, we call `await run.next(node)` to run it and get the next node (or an `End`).
5. Because we did not continue the run until it finished, the `result` is not set.
6. The run's history is still populated with the steps we executed so far.
7. Use [`FullStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence "FullStatePersistence            dataclass   ") so we can show the history of the run, see [State Persistence](#state-persistence) below for more information.

## State Persistence

One of the biggest benefits of finite state machine (FSM) graphs is how they simplify the handling of interrupted execution. This might happen for a variety of reasons:

- the state machine logic might fundamentally need to be paused — e.g. the returns workflow for an e-commerce order needs to wait for the item to be posted to the returns center or because execution of the next node needs input from a user so needs to wait for a new http request,
- the execution takes so long that the entire graph can't reliably be executed in a single continuous run — e.g. a deep research agent that might take hours to run,
- you want to run multiple graph nodes in parallel in different processes / hardware instances (note: parallel node execution is not yet supported in `pydantic-graph`, see [#704](https://github.com/pydantic/pydantic-ai/issues/704)).

Trying to make a conventional control flow (i.e., boolean logic and nested function calls) implementation compatible with these usage scenarios generally results in brittle and over-complicated spaghetti code, with the logic required to interrupt and resume execution dominating the implementation.

To allow graph runs to be interrupted and resumed, `pydantic-graph` provides state persistence — a system for snapshotting the state of a graph run before and after each node is run, allowing a graph run to be resumed from any point in the graph.

`pydantic-graph` includes three state persistence implementations:

- [`SimpleStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence "SimpleStatePersistence            dataclass   ") — Simple in memory state persistence that just hold the latest snapshot. If no state persistence implementation is provided when running a graph, this is used by default.
- [`FullStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence "FullStatePersistence            dataclass   ") — In memory state persistence that hold a list of snapshots.
- [`FileStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence "FileStatePersistence            dataclass   ") — File-based state persistence that saves snapshots to a JSON file.

In production applications, developers should implement their own state persistence by subclassing [`BaseStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence") abstract base class, which might persist runs in a relational database like PostgresQL.

At a high level the role of `StatePersistence` implementations is to store and retrieve [`NodeSnapshot`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot "NodeSnapshot            dataclass   ") and [`EndSnapshot`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot "EndSnapshot            dataclass   ") objects.

[`graph.iter_from_persistence()`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.iter_from_persistence "iter_from_persistence            async   ") may be used to run the graph based on the state stored in persistence.

We can run the `count_down_graph` from [above](#iterating-over-a-graph), using [`graph.iter_from_persistence()`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.iter_from_persistence "iter_from_persistence            async   ") and [`FileStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence "FileStatePersistence            dataclass   ").

As you can see in this code, `run_node` requires no external application state (apart from state persistence) to be run, meaning graphs can easily be executed by distributed execution and queueing systems.

count\_down\_from\_persistence.py

```
frompathlibimport Path

frompydantic_graphimport End
frompydantic_graph.persistence.fileimport FileStatePersistence

fromcount_downimport CountDown, CountDownState, count_down_graph


async defmain():
    run_id = 'run_abc123'
    persistence = FileStatePersistence(Path(f'count_down_{run_id}.json'))  # (1)!
    state = CountDownState(counter=5)
    await count_down_graph.initialize(  # (2)!
        CountDown(), state=state, persistence=persistence
    )

    done = False
    while not done:
        done = await run_node(run_id)


async defrun_node(run_id: str) -> bool:  # (3)!
    persistence = FileStatePersistence(Path(f'count_down_{run_id}.json'))
    async with count_down_graph.iter_from_persistence(persistence) as run:  # (4)!
        node_or_end = await run.next()  # (5)!

    print('Node:', node_or_end)
    #> Node: CountDown()
    #> Node: CountDown()
    #> Node: CountDown()
    #> Node: CountDown()
    #> Node: CountDown()
    #> Node: End(data=0)
    return isinstance(node_or_end, End)  # (6)!
```

1. Create a [`FileStatePersistence`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence "FileStatePersistence            dataclass   ") to use to start the graph.
2. Call [`graph.initialize()`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.initialize "initialize            async   ") to set the initial graph state in the persistence object.
3. `run_node` is a pure function that doesn't need access to any other process state to run the next node of the graph, except the ID of the run.
4. Call [`graph.iter_from_persistence()`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.iter_from_persistence "iter_from_persistence            async   ") create a [`GraphRun`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun "GraphRun") object that will run the next node of the graph from the state stored in persistence. This will return either a node or an `End` object.
5. [`graph.run()`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.run "run            async   ") will return either a [node](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode") or an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End            dataclass   ") object.
6. Check if the node is an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "End            dataclass   ") object, if it is, the graph run is complete.

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

### Example: Human in the loop.

As noted above, state persistence allows graphs to be interrupted and resumed. One use case of this is to allow user input to continue.

In this example, an AI asks the user a question, the user provides an answer, the AI evaluates the answer and ends if the user got it right or asks another question if they got it wrong.

Instead of running the entire graph in a single process invocation, we run the graph by running the process repeatedly, optionally providing an answer to the question as a command line argument.

`ai_q_and_a_graph.py` — `question_graph` definition

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) ai\_q\_and\_a\_graph.py

```
from__future__import annotations as _annotations

fromtypingimport Annotated
frompydantic_graphimport Edge
fromdataclassesimport dataclass, field
frompydanticimport BaseModel
frompydantic_graphimport (
    BaseNode,
    End,
    Graph,
    GraphRunContext,
)
frompydantic_aiimport Agent, format_as_xml
frompydantic_aiimport ModelMessage

ask_agent = Agent('gateway/openai:gpt-5', output_type=str, instrument=True)


@dataclass
classQuestionState:
    question: str | None = None
    ask_agent_messages: list[ModelMessage] = field(default_factory=list)
    evaluate_agent_messages: list[ModelMessage] = field(default_factory=list)


@dataclass
classAsk(BaseNode[QuestionState]):
"""Generate question using GPT-5."""
    docstring_notes = True
    async defrun(
        self, ctx: GraphRunContext[QuestionState]
    ) -> Annotated[Answer, Edge(label='Ask the question')]:
        result = await ask_agent.run(
            'Ask a simple question with a single correct answer.',
            message_history=ctx.state.ask_agent_messages,
        )
        ctx.state.ask_agent_messages += result.new_messages()
        ctx.state.question = result.output
        return Answer(result.output)


@dataclass
classAnswer(BaseNode[QuestionState]):
    question: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Evaluate:
        answer = input(f'{self.question}: ')
        return Evaluate(answer)


classEvaluationResult(BaseModel, use_attribute_docstrings=True):
    correct: bool
"""Whether the answer is correct."""
    comment: str
"""Comment on the answer, reprimand the user if the answer is wrong."""


evaluate_agent = Agent(
    'gateway/openai:gpt-5',
    output_type=EvaluationResult,
    system_prompt='Given a question and answer, evaluate if the answer is correct.',
)


@dataclass
classEvaluate(BaseNode[QuestionState, None, str]):
    answer: str

    async defrun(
        self,
        ctx: GraphRunContext[QuestionState],
    ) -> Annotated[End[str], Edge(label='success')] | Reprimand:
        assert ctx.state.question is not None
        result = await evaluate_agent.run(
            format_as_xml({'question': ctx.state.question, 'answer': self.answer}),
            message_history=ctx.state.evaluate_agent_messages,
        )
        ctx.state.evaluate_agent_messages += result.new_messages()
        if result.output.correct:
            return End(result.output.comment)
        else:
            return Reprimand(result.output.comment)


@dataclass
classReprimand(BaseNode[QuestionState]):
    comment: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Ask:
        print(f'Comment: {self.comment}')
        ctx.state.question = None
        return Ask()


question_graph = Graph(
    nodes=(Ask, Answer, Evaluate, Reprimand), state_type=QuestionState
)
```

ai\_q\_and\_a\_graph.py

```
from__future__import annotations as _annotations

fromtypingimport Annotated
frompydantic_graphimport Edge
fromdataclassesimport dataclass, field
frompydanticimport BaseModel
frompydantic_graphimport (
    BaseNode,
    End,
    Graph,
    GraphRunContext,
)
frompydantic_aiimport Agent, format_as_xml
frompydantic_aiimport ModelMessage

ask_agent = Agent('openai:gpt-5', output_type=str, instrument=True)


@dataclass
classQuestionState:
    question: str | None = None
    ask_agent_messages: list[ModelMessage] = field(default_factory=list)
    evaluate_agent_messages: list[ModelMessage] = field(default_factory=list)


@dataclass
classAsk(BaseNode[QuestionState]):
"""Generate question using GPT-5."""
    docstring_notes = True
    async defrun(
        self, ctx: GraphRunContext[QuestionState]
    ) -> Annotated[Answer, Edge(label='Ask the question')]:
        result = await ask_agent.run(
            'Ask a simple question with a single correct answer.',
            message_history=ctx.state.ask_agent_messages,
        )
        ctx.state.ask_agent_messages += result.new_messages()
        ctx.state.question = result.output
        return Answer(result.output)


@dataclass
classAnswer(BaseNode[QuestionState]):
    question: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Evaluate:
        answer = input(f'{self.question}: ')
        return Evaluate(answer)


classEvaluationResult(BaseModel, use_attribute_docstrings=True):
    correct: bool
"""Whether the answer is correct."""
    comment: str
"""Comment on the answer, reprimand the user if the answer is wrong."""


evaluate_agent = Agent(
    'openai:gpt-5',
    output_type=EvaluationResult,
    system_prompt='Given a question and answer, evaluate if the answer is correct.',
)


@dataclass
classEvaluate(BaseNode[QuestionState, None, str]):
    answer: str

    async defrun(
        self,
        ctx: GraphRunContext[QuestionState],
    ) -> Annotated[End[str], Edge(label='success')] | Reprimand:
        assert ctx.state.question is not None
        result = await evaluate_agent.run(
            format_as_xml({'question': ctx.state.question, 'answer': self.answer}),
            message_history=ctx.state.evaluate_agent_messages,
        )
        ctx.state.evaluate_agent_messages += result.new_messages()
        if result.output.correct:
            return End(result.output.comment)
        else:
            return Reprimand(result.output.comment)


@dataclass
classReprimand(BaseNode[QuestionState]):
    comment: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Ask:
        print(f'Comment: {self.comment}')
        ctx.state.question = None
        return Ask()


question_graph = Graph(
    nodes=(Ask, Answer, Evaluate, Reprimand), state_type=QuestionState
)
```

*(This example is complete, it can be run "as is")*

ai\_q\_and\_a\_run.py

```
importsys
frompathlibimport Path

frompydantic_graphimport End
frompydantic_graph.persistence.fileimport FileStatePersistence
frompydantic_aiimport ModelMessage  # noqa: F401

fromai_q_and_a_graphimport Ask, question_graph, Evaluate, QuestionState, Answer


async defmain():
    answer: str | None = sys.argv[1] if len(sys.argv) > 1 else None  # (1)!
    persistence = FileStatePersistence(Path('question_graph.json'))  # (2)!
    persistence.set_graph_types(question_graph)  # (3)!

    if snapshot := await persistence.load_next():  # (4)!
        state = snapshot.state
        assert answer is not None
        node = Evaluate(answer)
    else:
        state = QuestionState()
        node = Ask()  # (5)!

    async with question_graph.iter(node, state=state, persistence=persistence) as run:
        while True:
            node = await run.next()  # (6)!
            if isinstance(node, End):  # (7)!
                print('END:', node.data)
                history = await persistence.load_all()  # (8)!
                print([e.node for e in history])
                break
            elif isinstance(node, Answer):  # (9)!
                print(node.question)
                #> What is the capital of France?
                break
            # otherwise just continue
```

1. Get the user's answer from the command line, if provided. See [question graph example](https://ai.pydantic.dev/examples/question-graph/) for a complete example.
2. Create a state persistence instance the `'question_graph.json'` file may or may not already exist.
3. Since we're using the [persistence interface](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "BaseStatePersistence") outside a graph, we need to call [`set_graph_types`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.set_graph_types "set_graph_types") to set the graph generic types `StateT` and `RunEndT` for the persistence instance. This is necessary to allow the persistence instance to know how to serialize and deserialize graph nodes.
4. If we're run the graph before, [`load_next`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.load_next "load_next            abstractmethod       async   ") will return a snapshot of the next node to run, here we use `state` from that snapshot, and create a new `Evaluate` node with the answer provided on the command line.
5. If the graph hasn't been run before, we create a new `QuestionState` and start with the `Ask` node.
6. Call [`GraphRun.next()`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.GraphRun.next "next            async   ") to run the node. This will return either a node or an `End` object.
7. If the node is an `End` object, the graph run is complete. The `data` field of the `End` object contains the comment returned by the `evaluate_agent` about the correct answer.
8. To demonstrate the state persistence, we call [`load_all`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.load_all "load_all            abstractmethod       async   ") to get all the snapshots from the persistence instance. This will return a list of [`Snapshot`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot "Snapshot            module-attribute   ") objects.
9. If the node is an `Answer` object, we print the question and break out of the loop to end the process and wait for user input.

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

For a complete example of this graph, see the [question graph example](https://ai.pydantic.dev/examples/question-graph/).

## Dependency Injection

As with Pydantic AI, `pydantic-graph` supports dependency injection via a generic parameter on [`Graph`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "Graph            dataclass   ") and [`BaseNode`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "BaseNode"), and the [`GraphRunContext.deps`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.GraphRunContext.deps "deps            instance-attribute   ") field.

As an example of dependency injection, let's modify the `DivisibleBy5` example [above](#graph) to use a [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) to run the compute load in a separate process (this is a contrived example, `ProcessPoolExecutor` wouldn't actually improve performance in this example):

deps\_example.py

```
from__future__import annotations

importasyncio
fromconcurrent.futuresimport ProcessPoolExecutor
fromdataclassesimport dataclass

frompydantic_graphimport BaseNode, End, FullStatePersistence, Graph, GraphRunContext


@dataclass
classGraphDeps:
    executor: ProcessPoolExecutor


@dataclass
classDivisibleBy5(BaseNode[None, GraphDeps, int]):
    foo: int

    async defrun(
        self,
        ctx: GraphRunContext[None, GraphDeps],
    ) -> Increment | End[int]:
        if self.foo % 5 == 0:
            return End(self.foo)
        else:
            return Increment(self.foo)


@dataclass
classIncrement(BaseNode[None, GraphDeps]):
    foo: int

    async defrun(self, ctx: GraphRunContext[None, GraphDeps]) -> DivisibleBy5:
        loop = asyncio.get_running_loop()
        compute_result = await loop.run_in_executor(
            ctx.deps.executor,
            self.compute,
        )
        return DivisibleBy5(compute_result)

    defcompute(self) -> int:
        return self.foo + 1


fives_graph = Graph(nodes=[DivisibleBy5, Increment])


async defmain():
    with ProcessPoolExecutor() as executor:
        deps = GraphDeps(executor)
        result = await fives_graph.run(DivisibleBy5(3), deps=deps, persistence=FullStatePersistence())
    print(result.output)
    #> 5
    # the full history is quite verbose (see below), so we'll just print the summary
    print([item.node for item in result.persistence.history])
"""
    [
        DivisibleBy5(foo=3),
        Increment(foo=3),
        DivisibleBy5(foo=4),
        Increment(foo=4),
        DivisibleBy5(foo=5),
        End(data=5),
    ]
    """
```

*(This example is complete, it can be run "as is" — you'll need to add `asyncio.run(main())` to run `main`)*

## Mermaid Diagrams

Pydantic Graph can generate [mermaid](https://mermaid.js.org/) [`stateDiagram-v2`](https://mermaid.js.org/syntax/stateDiagram.html) diagrams for graphs, as shown above.

These diagrams can be generated with:

- [`Graph.mermaid_code`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.mermaid_code "mermaid_code") to generate the mermaid code for a graph
- [`Graph.mermaid_image`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.mermaid_image "mermaid_image") to generate an image of the graph using [mermaid.ink](https://mermaid.ink/)
- [`Graph.mermaid_save`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.mermaid_save "mermaid_save") to generate an image of the graph using [mermaid.ink](https://mermaid.ink/) and save it to a file

Beyond the diagrams shown above, you can also customize mermaid diagrams with the following options:

- [`Edge`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.Edge "Edge            dataclass   ") allows you to apply a label to an edge
- [`BaseNode.docstring_notes`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode.docstring_notes "docstring_notes            class-attribute   ") and [`BaseNode.get_note`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode.get_note "get_note            classmethod   ") allows you to add notes to nodes
- The [`highlighted_nodes`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.mermaid_code "mermaid_code") parameter allows you to highlight specific node(s) in the diagram

Putting that together, we can edit the last [`ai_q_and_a_graph.py`](#example-human-in-the-loop) example to:

- add labels to some edges
- add a note to the `Ask` node
- highlight the `Answer` node
- save the diagram as a `PNG` image to file

With Pydantic AI GatewayDirectly to Provider API

[Learn about Gateway](https://ai.pydantic.dev/gateway) ai\_q\_and\_a\_graph\_extra.py

```
fromtypingimport Annotated
frompydantic_graphimport BaseNode, End, Graph, GraphRunContext, Edge
ask_agent = Agent('gateway/openai:gpt-5', output_type=str, instrument=True)


@dataclass
classQuestionState:
    question: str | None = None
    ask_agent_messages: list[ModelMessage] = field(default_factory=list)
    evaluate_agent_messages: list[ModelMessage] = field(default_factory=list)

@dataclass
classAsk(BaseNode[QuestionState]):
"""Generate question using GPT-5."""
    docstring_notes = True
    async defrun(
        self, ctx: GraphRunContext[QuestionState]
    ) -> Annotated[Answer, Edge(label='Ask the question')]:
        result = await ask_agent.run(
            'Ask a simple question with a single correct answer.',
            message_history=ctx.state.ask_agent_messages,
        )
        ctx.state.ask_agent_messages += result.new_messages()
        ctx.state.question = result.output
        return Answer(result.output)


@dataclass
classAnswer(BaseNode[QuestionState]):
    question: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Evaluate:
        answer = input(f'{self.question}: ')
        return Evaluate(answer)


classEvaluationResult(BaseModel, use_attribute_docstrings=True):
    correct: bool
"""Whether the answer is correct."""
    comment: str
"""Comment on the answer, reprimand the user if the answer is wrong."""


evaluate_agent = Agent(
    'gateway/openai:gpt-5',
    output_type=EvaluationResult,
    system_prompt='Given a question and answer, evaluate if the answer is correct.',
)


@dataclass
classEvaluate(BaseNode[QuestionState, None, str]):
    answer: str

    async defrun(
        self,
        ctx: GraphRunContext[QuestionState],
    ) -> Annotated[End[str], Edge(label='success')] | Reprimand:
        assert ctx.state.question is not None
        result = await evaluate_agent.run(
            format_as_xml({'question': ctx.state.question, 'answer': self.answer}),
            message_history=ctx.state.evaluate_agent_messages,
        )
        ctx.state.evaluate_agent_messages += result.new_messages()
        if result.output.correct:
            return End(result.output.comment)
        else:
            return Reprimand(result.output.comment)


@dataclass
classReprimand(BaseNode[QuestionState]):
    comment: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Ask:
        print(f'Comment: {self.comment}')
        ctx.state.question = None
        return Ask()


question_graph = Graph(
    nodes=(Ask, Answer, Evaluate, Reprimand), state_type=QuestionState
)
```

ai\_q\_and\_a\_graph\_extra.py

```
fromtypingimport Annotated
frompydantic_graphimport BaseNode, End, Graph, GraphRunContext, Edge
ask_agent = Agent('openai:gpt-5', output_type=str, instrument=True)


@dataclass
classQuestionState:
    question: str | None = None
    ask_agent_messages: list[ModelMessage] = field(default_factory=list)
    evaluate_agent_messages: list[ModelMessage] = field(default_factory=list)

@dataclass
classAsk(BaseNode[QuestionState]):
"""Generate question using GPT-5."""
    docstring_notes = True
    async defrun(
        self, ctx: GraphRunContext[QuestionState]
    ) -> Annotated[Answer, Edge(label='Ask the question')]:
        result = await ask_agent.run(
            'Ask a simple question with a single correct answer.',
            message_history=ctx.state.ask_agent_messages,
        )
        ctx.state.ask_agent_messages += result.new_messages()
        ctx.state.question = result.output
        return Answer(result.output)


@dataclass
classAnswer(BaseNode[QuestionState]):
    question: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Evaluate:
        answer = input(f'{self.question}: ')
        return Evaluate(answer)


classEvaluationResult(BaseModel, use_attribute_docstrings=True):
    correct: bool
"""Whether the answer is correct."""
    comment: str
"""Comment on the answer, reprimand the user if the answer is wrong."""


evaluate_agent = Agent(
    'openai:gpt-5',
    output_type=EvaluationResult,
    system_prompt='Given a question and answer, evaluate if the answer is correct.',
)


@dataclass
classEvaluate(BaseNode[QuestionState, None, str]):
    answer: str

    async defrun(
        self,
        ctx: GraphRunContext[QuestionState],
    ) -> Annotated[End[str], Edge(label='success')] | Reprimand:
        assert ctx.state.question is not None
        result = await evaluate_agent.run(
            format_as_xml({'question': ctx.state.question, 'answer': self.answer}),
            message_history=ctx.state.evaluate_agent_messages,
        )
        ctx.state.evaluate_agent_messages += result.new_messages()
        if result.output.correct:
            return End(result.output.comment)
        else:
            return Reprimand(result.output.comment)


@dataclass
classReprimand(BaseNode[QuestionState]):
    comment: str

    async defrun(self, ctx: GraphRunContext[QuestionState]) -> Ask:
        print(f'Comment: {self.comment}')
        ctx.state.question = None
        return Ask()


question_graph = Graph(
    nodes=(Ask, Answer, Evaluate, Reprimand), state_type=QuestionState
)
```

*(This example is not complete and cannot be run directly)*

This would generate an image that looks like this:

```
---
title: question_graph
---
stateDiagram-v2
  Ask --> Answer: Ask the question
  note right of Ask
    Judge the answer.
    Decide on next step.
  end note
  Answer --> Evaluate
  Evaluate --> Reprimand
  Evaluate --> [*]: success
  Reprimand --> Ask

classDef highlighted fill:#fdff32
class Answer highlighted
```

### Setting Direction of the State Diagram

You can specify the direction of the state diagram using one of the following values:

- `'TB'`: Top to bottom, the diagram flows vertically from top to bottom.
- `'LR'`: Left to right, the diagram flows horizontally from left to right.
- `'RL'`: Right to left, the diagram flows horizontally from right to left.
- `'BT'`: Bottom to top, the diagram flows vertically from bottom to top.

Here is an example of how to do this using 'Left to Right' (LR) instead of the default 'Top to Bottom' (TB):

vending\_machine\_diagram.py

```
fromvending_machineimport InsertCoin, vending_machine_graph

vending_machine_graph.mermaid_code(start_node=InsertCoin, direction='LR')
```

```
---
title: vending_machine_graph
---
stateDiagram-v2
  direction LR
  [*] --> InsertCoin
  InsertCoin --> CoinsInserted
  CoinsInserted --> SelectProduct
  CoinsInserted --> Purchase
  SelectProduct --> Purchase
  Purchase --> InsertCoin
  Purchase --> SelectProduct
  Purchase --> [*]
```