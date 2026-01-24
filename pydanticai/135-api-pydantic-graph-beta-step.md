---
title: pydantic_graph.beta.step - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_graph/beta_step/
source: sitemap
fetched_at: 2026-01-22T22:25:00.099190805-03:00
rendered_js: false
word_count: 939
summary: This document defines the core abstractions and protocols for step-based graph execution in pydantic-graph, including step contexts, function interfaces, and streaming components.
tags:
    - pydantic-graph
    - graph-execution
    - step-functions
    - python-api
    - async-programming
    - state-management
category: api
---

Step-based graph execution components.

This module provides the core abstractions for step-based graph execution, including step contexts, step functions, and step nodes that bridge between the v1 and v2 graph execution systems.

### StepContext `dataclass`

Bases: `Generic[StateT, DepsT, InputT]`

Context information passed to step functions during graph execution.

The step context provides access to the current graph state, dependencies, and input data for a step.

Class Type Parameters:

Name Bound or Constraints Description Default `StateT`

The type of the graph state

*required* `DepsT`

The type of the dependencies

*required* `InputT`

The type of the input data

*required*

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
```

```
@dataclass(init=False)
classStepContext(Generic[StateT, DepsT, InputT]):
"""Context information passed to step functions during graph execution.

    The step context provides access to the current graph state, dependencies, and input data for a step.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        InputT: The type of the input data
    """

    _state: StateT
"""The current graph state."""
    _deps: DepsT
"""The graph run dependencies."""
    _inputs: InputT
"""The input data for this step."""

    def__init__(self, *, state: StateT, deps: DepsT, inputs: InputT):
        self._state = state
        self._deps = deps
        self._inputs = inputs

    @property
    defstate(self) -> StateT:
        return self._state

    @property
    defdeps(self) -> DepsT:
        return self._deps

    @property
    definputs(self) -> InputT:
"""The input data for this step.

        This must be a property to ensure correct variance behavior
        """
        return self._inputs
```

#### inputs `property`

The input data for this step.

This must be a property to ensure correct variance behavior

### StepFunction

Bases: `Protocol[StateT, DepsT, InputT, OutputT]`

Protocol for step functions that can be executed in the graph.

Step functions are async callables that receive a step context and return a result.

Class Type Parameters:

Name Bound or Constraints Description Default `StateT`

The type of the graph state

*required* `DepsT`

The type of the dependencies

*required* `InputT`

The type of the input data

*required* `OutputT`

The type of the output data

*required*

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
```

```
classStepFunction(Protocol[StateT, DepsT, InputT, OutputT]):
"""Protocol for step functions that can be executed in the graph.

    Step functions are async callables that receive a step context and return a result.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        InputT: The type of the input data
        OutputT: The type of the output data
    """

    def__call__(self, ctx: StepContext[StateT, DepsT, InputT]) -> Awaitable[OutputT]:
"""Execute the step function with the given context.

        Args:
            ctx: The step context containing state, dependencies, and inputs

        Returns:
            An awaitable that resolves to the step's output
        """
        raise NotImplementedError
```

#### \_\_call\__

```
__call__(
    ctx: StepContext[StateT, DepsT, InputT],
) -> Awaitable[OutputT]
```

Execute the step function with the given context.

Parameters:

Name Type Description Default `ctx` `StepContext[StateT, DepsT, InputT]`

The step context containing state, dependencies, and inputs

*required*

Returns:

Type Description `Awaitable[OutputT]`

An awaitable that resolves to the step's output

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
78
79
80
81
82
83
84
85
86
87
```

```
def__call__(self, ctx: StepContext[StateT, DepsT, InputT]) -> Awaitable[OutputT]:
"""Execute the step function with the given context.

    Args:
        ctx: The step context containing state, dependencies, and inputs

    Returns:
        An awaitable that resolves to the step's output
    """
    raise NotImplementedError
```

### StreamFunction

Bases: `Protocol[StateT, DepsT, InputT, OutputT]`

Protocol for stream functions that can be executed in the graph.

Stream functions are async callables that receive a step context and return an async iterator.

Class Type Parameters:

Name Bound or Constraints Description Default `StateT`

The type of the graph state

*required* `DepsT`

The type of the dependencies

*required* `InputT`

The type of the input data

*required* `OutputT`

The type of the output data

*required*

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
```

```
classStreamFunction(Protocol[StateT, DepsT, InputT, OutputT]):
"""Protocol for stream functions that can be executed in the graph.

    Stream functions are async callables that receive a step context and return an async iterator.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        InputT: The type of the input data
        OutputT: The type of the output data
    """

    def__call__(self, ctx: StepContext[StateT, DepsT, InputT]) -> AsyncIterator[OutputT]:
"""Execute the stream function with the given context.

        Args:
            ctx: The step context containing state, dependencies, and inputs

        Returns:
            An async iterator yielding the streamed output
        """
        raise NotImplementedError
        yield
```

#### \_\_call\__

Execute the stream function with the given context.

Parameters:

Name Type Description Default `ctx` `StepContext[StateT, DepsT, InputT]`

The step context containing state, dependencies, and inputs

*required*

Returns:

Type Description `AsyncIterator[OutputT]`

An async iterator yielding the streamed output

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
102
103
104
105
106
107
108
109
110
111
112
```

```
def__call__(self, ctx: StepContext[StateT, DepsT, InputT]) -> AsyncIterator[OutputT]:
"""Execute the stream function with the given context.

    Args:
        ctx: The step context containing state, dependencies, and inputs

    Returns:
        An async iterator yielding the streamed output
    """
    raise NotImplementedError
    yield
```

### AnyStepFunction `module-attribute`

Type alias for a step function with any type parameters.

### Step `dataclass`

Bases: `Generic[StateT, DepsT, InputT, OutputT]`

A step in the graph execution that wraps a step function.

Steps represent individual units of execution in the graph, encapsulating a step function along with metadata like ID and label.

Class Type Parameters:

Name Bound or Constraints Description Default `StateT`

The type of the graph state

*required* `DepsT`

The type of the dependencies

*required* `InputT`

The type of the input data

*required* `OutputT`

The type of the output data

*required*

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
```

```
@dataclass(init=False)
classStep(Generic[StateT, DepsT, InputT, OutputT]):
"""A step in the graph execution that wraps a step function.

    Steps represent individual units of execution in the graph, encapsulating
    a step function along with metadata like ID and label.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        InputT: The type of the input data
        OutputT: The type of the output data
    """

    id: NodeID
"""Unique identifier for this step."""
    _call: StepFunction[StateT, DepsT, InputT, OutputT]
"""The step function to execute."""
    label: str | None
"""Optional human-readable label for this step."""

    def__init__(self, *, id: NodeID, call: StepFunction[StateT, DepsT, InputT, OutputT], label: str | None = None):
        self.id = id
        self._call = call
        self.label = label

    @property
    defcall(self) -> StepFunction[StateT, DepsT, InputT, OutputT]:
"""The step function to execute. This needs to be a property for proper variance inference."""
        return self._call

    @overload
    defas_node(self, inputs: None = None) -> StepNode[StateT, DepsT]: ...

    @overload
    defas_node(self, inputs: InputT) -> StepNode[StateT, DepsT]: ...

    defas_node(self, inputs: InputT | None = None) -> StepNode[StateT, DepsT]:
"""Create a step node with bound inputs.

        Args:
            inputs: The input data to bind to this step, or None

        Returns:
            A [`StepNode`][pydantic_graph.beta.step.StepNode] with this step and the bound inputs
        """
        return StepNode(self, inputs)
```

#### id `instance-attribute`

Unique identifier for this step.

#### label `instance-attribute`

```
label: str | None = label
```

Optional human-readable label for this step.

#### call `property`

```
call: StepFunction[StateT, DepsT, InputT, OutputT]
```

The step function to execute. This needs to be a property for proper variance inference.

#### as\_node

```
as_node(inputs: None = None) -> StepNode[StateT, DepsT]
```

```
as_node(inputs: InputT) -> StepNode[StateT, DepsT]
```

```
as_node(
    inputs: InputT | None = None,
) -> StepNode[StateT, DepsT]
```

Create a step node with bound inputs.

Parameters:

Name Type Description Default `inputs` `InputT | None`

The input data to bind to this step, or None

`None`

Returns:

Type Description `StepNode[StateT, DepsT]`

A [`StepNode`](#pydantic_graph.beta.step.StepNode "StepNode            dataclass   ") with this step and the bound inputs

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
156
157
158
159
160
161
162
163
164
165
```

```
defas_node(self, inputs: InputT | None = None) -> StepNode[StateT, DepsT]:
"""Create a step node with bound inputs.

    Args:
        inputs: The input data to bind to this step, or None

    Returns:
        A [`StepNode`][pydantic_graph.beta.step.StepNode] with this step and the bound inputs
    """
    return StepNode(self, inputs)
```

### StepNode `dataclass`

Bases: `BaseNode[StateT, DepsT, Any]`

A base node that represents a step with bound inputs.

StepNode bridges between the v1 and v2 graph execution systems by wrapping a [`Step`](#pydantic_graph.beta.step.Step "Step            dataclass   ") with bound inputs in a BaseNode interface. It is not meant to be run directly but rather used to indicate transitions to v2-style steps.

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
```

```
@dataclass
classStepNode(BaseNode[StateT, DepsT, Any]):
"""A base node that represents a step with bound inputs.

    StepNode bridges between the v1 and v2 graph execution systems by wrapping
    a [`Step`][pydantic_graph.beta.step.Step] with bound inputs in a BaseNode interface.
    It is not meant to be run directly but rather used to indicate transitions
    to v2-style steps.
    """

    step: Step[StateT, DepsT, Any, Any]
"""The step to execute."""

    inputs: Any
"""The inputs bound to this step."""

    async defrun(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[Any]:
"""Attempt to run the step node.

        Args:
            ctx: The graph execution context

        Returns:
            The result of step execution

        Raises:
            NotImplementedError: Always raised as StepNode is not meant to be run directly
        """
        raise NotImplementedError(
            '`StepNode` is not meant to be run directly, it is meant to be used in `BaseNode` subclasses to indicate a transition to v2-style steps.'
        )
```

#### step `instance-attribute`

The step to execute.

#### inputs `instance-attribute`

The inputs bound to this step.

#### run `async`

Attempt to run the step node.

Parameters:

Name Type Description Default `ctx` `GraphRunContext[StateT, DepsT]`

The graph execution context

*required*

Returns:

Type Description `BaseNode[StateT, DepsT, Any] | End[Any]`

The result of step execution

Raises:

Type Description `NotImplementedError`

Always raised as StepNode is not meant to be run directly

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
```

```
async defrun(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[Any]:
"""Attempt to run the step node.

    Args:
        ctx: The graph execution context

    Returns:
        The result of step execution

    Raises:
        NotImplementedError: Always raised as StepNode is not meant to be run directly
    """
    raise NotImplementedError(
        '`StepNode` is not meant to be run directly, it is meant to be used in `BaseNode` subclasses to indicate a transition to v2-style steps.'
    )
```

### NodeStep

Bases: `Step[StateT, DepsT, Any, BaseNode[StateT, DepsT, Any] | End[Any]]`

A step that wraps a BaseNode type for execution.

NodeStep allows v1-style BaseNode classes to be used as steps in the v2 graph execution system. It validates that the input is of the expected node type and runs it with the appropriate graph context.

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
```

```
classNodeStep(Step[StateT, DepsT, Any, BaseNode[StateT, DepsT, Any] | End[Any]]):
"""A step that wraps a BaseNode type for execution.

    NodeStep allows v1-style BaseNode classes to be used as steps in the
    v2 graph execution system. It validates that the input is of the expected
    node type and runs it with the appropriate graph context.
    """

    node_type: type[BaseNode[StateT, DepsT, Any]]
"""The BaseNode type this step executes."""

    def__init__(
        self,
        node_type: type[BaseNode[StateT, DepsT, Any]],
        *,
        id: NodeID | None = None,
        label: str | None = None,
    ):
"""Initialize a node step.

        Args:
            node_type: The BaseNode class this step will execute
            id: Optional unique identifier, defaults to the node's get_node_id()
            label: Optional human-readable label for this step
        """
        super().__init__(
            id=id or NodeID(node_type.get_node_id()),
            call=self._call_node,
            label=label,
        )
        # `type[BaseNode[StateT, DepsT, Any]]` could actually be a `typing._GenericAlias` like `pydantic_ai._agent_graph.UserPromptNode[~DepsT, ~OutputT]`,
        # so we get the origin to get to the actual class
        self.node_type = get_origin(node_type) or node_type

    async def_call_node(self, ctx: StepContext[StateT, DepsT, Any]) -> BaseNode[StateT, DepsT, Any] | End[Any]:
"""Execute the wrapped node with the step context.

        Args:
            ctx: The step context containing the node instance to run

        Returns:
            The result of running the node, either another BaseNode or End

        Raises:
            ValueError: If the input node is not of the expected type
        """
        node = ctx.inputs
        if not isinstance(node, self.node_type):
            raise ValueError(f'Node {node} is not of type {self.node_type}')  # pragma: no cover
        node = cast(BaseNode[StateT, DepsT, Any], node)
        return await node.run(GraphRunContext(state=ctx.state, deps=ctx.deps))
```

#### \_\_init\__

```
__init__(
    node_type: type[BaseNode[StateT, DepsT, Any]],
    *,
    id: NodeID | None = None,
    label: str | None = None
)
```

Initialize a node step.

Parameters:

Name Type Description Default `node_type` `type[BaseNode[StateT, DepsT, Any]]`

The BaseNode class this step will execute

*required* `id` `NodeID | None`

Optional unique identifier, defaults to the node's get\_node\_id()

`None` `label` `str | None`

Optional human-readable label for this step

`None`

Source code in `pydantic_graph/pydantic_graph/beta/step.py`

```
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
```

```
def__init__(
    self,
    node_type: type[BaseNode[StateT, DepsT, Any]],
    *,
    id: NodeID | None = None,
    label: str | None = None,
):
"""Initialize a node step.

    Args:
        node_type: The BaseNode class this step will execute
        id: Optional unique identifier, defaults to the node's get_node_id()
        label: Optional human-readable label for this step
    """
    super().__init__(
        id=id or NodeID(node_type.get_node_id()),
        call=self._call_node,
        label=label,
    )
    # `type[BaseNode[StateT, DepsT, Any]]` could actually be a `typing._GenericAlias` like `pydantic_ai._agent_graph.UserPromptNode[~DepsT, ~OutputT]`,
    # so we get the origin to get to the actual class
    self.node_type = get_origin(node_type) or node_type
```

#### node\_type `instance-attribute`

The BaseNode type this step executes.