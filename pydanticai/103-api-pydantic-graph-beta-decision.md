---
title: pydantic_graph.beta.decision - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_graph/beta_decision/
source: sitemap
fetched_at: 2026-01-22T22:24:52.365909909-03:00
rendered_js: false
word_count: 74
summary: The DecisionBranchBuilder class provides a fluent API for defining decision branches in a graph, allowing for type-safe routing, data transformation, and parallel execution path configuration.
tags:
    - pydantic-graph
    - graph-builder
    - fluent-api
    - python-api
    - decision-logic
    - type-safety
category: api
---

```
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
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
```

```
@dataclass(init=False)
classDecisionBranchBuilder(Generic[StateT, DepsT, OutputT, SourceT, HandledT]):
"""Builder for constructing decision branches with fluent API.

    This builder provides methods to configure branches with destinations,
    forks, and transformations in a type-safe manner.

    Instances of this class should be created using [`GraphBuilder.match`][pydantic_graph.beta.graph_builder.GraphBuilder],
    not created directly.
    """

    _decision: Decision[StateT, DepsT, HandledT]
"""The parent decision node."""
    _source: TypeOrTypeExpression[SourceT]
"""The expected source type for this branch."""
    _matches: Callable[[Any], bool] | None
"""Optional matching predicate."""

    _path_builder: PathBuilder[StateT, DepsT, OutputT]
"""Builder for the execution path."""

    def__init__(
        self,
        *,
        decision: Decision[StateT, DepsT, HandledT],
        source: TypeOrTypeExpression[SourceT],
        matches: Callable[[Any], bool] | None,
        path_builder: PathBuilder[StateT, DepsT, OutputT],
    ):
        # This manually-defined initializer is necessary due to https://github.com/python/mypy/issues/17623.
        self._decision = decision
        self._source = source
        self._matches = matches
        self._path_builder = path_builder

    defto(
        self,
        destination: DestinationNode[StateT, DepsT, OutputT] | type[BaseNode[StateT, DepsT, Any]],
        /,
        *extra_destinations: DestinationNode[StateT, DepsT, OutputT] | type[BaseNode[StateT, DepsT, Any]],
        fork_id: str | None = None,
    ) -> DecisionBranch[SourceT]:
"""Set the destination(s) for this branch.

        Args:
            destination: The primary destination node.
            *extra_destinations: Additional destination nodes.
            fork_id: Optional node ID to use for the resulting broadcast fork if multiple destinations are provided.

        Returns:
            A completed DecisionBranch with the specified destinations.
        """
        destination = get_origin(destination) or destination
        extra_destinations = tuple(get_origin(d) or d for d in extra_destinations)
        destinations = [(NodeStep(d) if inspect.isclass(d) else d) for d in (destination, *extra_destinations)]
        return DecisionBranch(
            source=self._source,
            matches=self._matches,
            path=self._path_builder.to(*destinations, fork_id=fork_id),
            destinations=destinations,
        )

    defbroadcast(
        self, get_forks: Callable[[Self], Sequence[DecisionBranch[SourceT]]], /, *, fork_id: str | None = None
    ) -> DecisionBranch[SourceT]:
"""Broadcast this decision branch into multiple destinations.

        Args:
            get_forks: The callback that will return a sequence of decision branches to broadcast to.
            fork_id: Optional node ID to use for the resulting broadcast fork.

        Returns:
            A completed DecisionBranch with the specified destinations.
        """
        fork_decision_branches = get_forks(self)
        new_paths = [b.path for b in fork_decision_branches]
        if not new_paths:
            raise GraphBuildingError(f'The call to {get_forks} returned no branches, but must return at least one.')
        path = self._path_builder.broadcast(new_paths, fork_id=fork_id)
        destinations = [d for fdp in fork_decision_branches for d in fdp.destinations]
        return DecisionBranch(source=self._source, matches=self._matches, path=path, destinations=destinations)

    deftransform(
        self, func: TransformFunction[StateT, DepsT, OutputT, NewOutputT], /
    ) -> DecisionBranchBuilder[StateT, DepsT, NewOutputT, SourceT, HandledT]:
"""Apply a transformation to the branch's output.

        Args:
            func: Transformation function to apply.

        Returns:
            A new DecisionBranchBuilder where the provided transform is applied prior to generating the final output.
        """
        return DecisionBranchBuilder(
            decision=self._decision,
            source=self._source,
            matches=self._matches,
            path_builder=self._path_builder.transform(func),
        )

    defmap(
        self: DecisionBranchBuilder[StateT, DepsT, Iterable[T], SourceT, HandledT]
        | DecisionBranchBuilder[StateT, DepsT, AsyncIterable[T], SourceT, HandledT],
        *,
        fork_id: str | None = None,
        downstream_join_id: str | None = None,
    ) -> DecisionBranchBuilder[StateT, DepsT, T, SourceT, HandledT]:
"""Spread the branch's output.

        To do this, the current output must be iterable, and any subsequent steps in the path being built for this
        branch will be applied to each item of the current output in parallel.

        Args:
            fork_id: Optional ID for the fork, defaults to a generated value
            downstream_join_id: Optional ID of a downstream join node which is involved when mapping empty iterables

        Returns:
            A new DecisionBranchBuilder where mapping is performed prior to generating the final output.
        """
        return DecisionBranchBuilder(
            decision=self._decision,
            source=self._source,
            matches=self._matches,
            path_builder=self._path_builder.map(fork_id=fork_id, downstream_join_id=downstream_join_id),
        )

    deflabel(self, label: str) -> DecisionBranchBuilder[StateT, DepsT, OutputT, SourceT, HandledT]:
"""Apply a label to the branch at the current point in the path being built.

        These labels are only used in generated mermaid diagrams.

        Args:
            label: The label to apply.

        Returns:
            A new DecisionBranchBuilder where the label has been applied at the end of the current path being built.
        """
        return DecisionBranchBuilder(
            decision=self._decision,
            source=self._source,
            matches=self._matches,
            path_builder=self._path_builder.label(label),
        )
```