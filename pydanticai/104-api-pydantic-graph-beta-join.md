---
title: pydantic_graph.beta.join - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_graph/beta_join/
source: sitemap
fetched_at: 2026-01-22T22:24:56.866974572-03:00
rendered_js: false
word_count: 24
summary: This document defines the Join class, which is used to synchronize and aggregate parallel execution paths within a graph using reducer functions.
tags:
    - pydantic-graph
    - parallel-execution
    - reducer-functions
    - data-aggregation
    - graph-nodes
category: api
---

```
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
166
167
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
199
200
201
202
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
```

```
@dataclass(init=False)
classJoin(Generic[StateT, DepsT, InputT, OutputT]):
"""A join operation that synchronizes and aggregates parallel execution paths.

    A join defines how to combine outputs from multiple parallel execution paths
    using a [`ReducerFunction`][pydantic_graph.beta.join.ReducerFunction]. It specifies which fork
    it joins (if any) and manages the initialization of reducers.

    Type Parameters:
        StateT: The type of the graph state
        DepsT: The type of the dependencies
        InputT: The type of input data to join
        OutputT: The type of the final joined output
    """

    id: JoinID
    _reducer: ReducerFunction[StateT, DepsT, InputT, OutputT]
    _initial_factory: Callable[[], OutputT]
    parent_fork_id: ForkID | None
    preferred_parent_fork: Literal['closest', 'farthest']

    def__init__(
        self,
        *,
        id: JoinID,
        reducer: ReducerFunction[StateT, DepsT, InputT, OutputT],
        initial_factory: Callable[[], OutputT],
        parent_fork_id: ForkID | None = None,
        preferred_parent_fork: Literal['farthest', 'closest'] = 'farthest',
    ):
        self.id = id
        self._reducer = reducer
        self._initial_factory = initial_factory
        self.parent_fork_id = parent_fork_id
        self.preferred_parent_fork = preferred_parent_fork

    @property
    defreducer(self):
        return self._reducer

    @property
    definitial_factory(self):
        return self._initial_factory

    defreduce(self, ctx: ReducerContext[StateT, DepsT], current: OutputT, inputs: InputT) -> OutputT:
        n_parameters = len(inspect.signature(self.reducer).parameters)
        if n_parameters == 2:
            return cast(PlainReducerFunction[InputT, OutputT], self.reducer)(current, inputs)
        else:
            return cast(ContextReducerFunction[StateT, DepsT, InputT, OutputT], self.reducer)(ctx, current, inputs)

    @overload
    defas_node(self, inputs: None = None) -> JoinNode[StateT, DepsT]: ...

    @overload
    defas_node(self, inputs: InputT) -> JoinNode[StateT, DepsT]: ...

    defas_node(self, inputs: InputT | None = None) -> JoinNode[StateT, DepsT]:
"""Create a step node with bound inputs.

        Args:
            inputs: The input data to bind to this step, or None

        Returns:
            A [`StepNode`][pydantic_graph.beta.step.StepNode] with this step and the bound inputs
        """
        return JoinNode(self, inputs)
```