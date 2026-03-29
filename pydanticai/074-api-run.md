---
title: pydantic_ai.run - Pydantic AI
url: https://ai.pydantic.dev/api/run/
source: sitemap
fetched_at: 2026-01-22T22:24:16.054780092-03:00
rendered_js: false
word_count: 141
summary: The AgentRun class provides a stateful and async-iterable interface for managing and inspecting the execution of an AI agent, allowing users to iterate through graph nodes and access run results.
tags:
    - pydantic-ai
    - agent-run
    - async-iterator
    - state-management
    - message-history
    - graph-execution
category: api
---

```
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
 64
 65
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
 88
 89
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
113
114
115
116
117
118
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
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
```

````
@dataclasses.dataclass(repr=False)
classAgentRun(Generic[AgentDepsT, OutputDataT]):
"""A stateful, async-iterable run of an [`Agent`][pydantic_ai.agent.Agent].

    You generally obtain an `AgentRun` instance by calling `async with my_agent.iter(...) as agent_run:`.

    Once you have an instance, you can use it to iterate through the run's nodes as they execute. When an
    [`End`][pydantic_graph.nodes.End] is reached, the run finishes and [`result`][pydantic_ai.agent.AgentRun.result]
    becomes available.

    Example:
    ```python
    from pydantic_ai import Agent

    agent = Agent('openai:gpt-4o')

    async def main():
        nodes = []
        # Iterate through the run, recording each node along the way:
        async with agent.iter('What is the capital of France?') as agent_run:
            async for node in agent_run:
                nodes.append(node)
        print(nodes)
        '''
        [
            UserPromptNode(
                user_prompt='What is the capital of France?',
                instructions_functions=[],
                system_prompts=(),
                system_prompt_functions=[],
                system_prompt_dynamic_functions={},
            ),
            ModelRequestNode(
                request=ModelRequest(
                    parts=[
                        UserPromptPart(
                            content='What is the capital of France?',
                            timestamp=datetime.datetime(...),
                        )
                    ],
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            CallToolsNode(
                model_response=ModelResponse(
                    parts=[TextPart(content='The capital of France is Paris.')],
                    usage=RequestUsage(input_tokens=56, output_tokens=7),
                    model_name='gpt-4o',
                    timestamp=datetime.datetime(...),
                    run_id='...',
                )
            ),
            End(data=FinalResult(output='The capital of France is Paris.')),
        ]
        '''
        print(agent_run.result.output)
        #> The capital of France is Paris.
    ```

    You can also manually drive the iteration using the [`next`][pydantic_ai.agent.AgentRun.next] method for
    more granular control.
    """

    _graph_run: GraphRun[
        _agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any], FinalResult[OutputDataT]
    ]

    @overload
    def_traceparent(self, *, required: Literal[False]) -> str | None: ...
    @overload
    def_traceparent(self) -> str: ...
    def_traceparent(self, *, required: bool = True) -> str | None:
        traceparent = self._graph_run._traceparent(required=False)  # type: ignore[reportPrivateUsage]
        if traceparent is None and required:  # pragma: no cover
            raise AttributeError('No span was created for this agent run')
        return traceparent

    @property
    defctx(self) -> GraphRunContext[_agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any]]:
"""The current context of the agent run."""
        return GraphRunContext[_agent_graph.GraphAgentState, _agent_graph.GraphAgentDeps[AgentDepsT, Any]](
            state=self._graph_run.state, deps=self._graph_run.deps
        )

    @property
    defnext_node(
        self,
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
"""The next node that will be run in the agent graph.

        This is the next node that will be used during async iteration, or if a node is not passed to `self.next(...)`.
        """
        task = self._graph_run.next_task
        return self._task_to_node(task)

    @property
    defresult(self) -> AgentRunResult[OutputDataT] | None:
"""The final result of the run if it has ended, otherwise `None`.

        Once the run returns an [`End`][pydantic_graph.nodes.End] node, `result` is populated
        with an [`AgentRunResult`][pydantic_ai.agent.AgentRunResult].
        """
        graph_run_output = self._graph_run.output
        if graph_run_output is None:
            return None
        return AgentRunResult(
            graph_run_output.output,
            graph_run_output.tool_name,
            self._graph_run.state,
            self._graph_run.deps.new_message_index,
            self._traceparent(required=False),
        )

    defall_messages(self) -> list[_messages.ModelMessage]:
"""Return all messages for the run so far.

        Messages from older runs are included.
        """
        return self.ctx.state.message_history

    defall_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:
"""Return all messages from [`all_messages`][pydantic_ai.agent.AgentRun.all_messages] as JSON bytes.

        Returns:
            JSON bytes representing the messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(self.all_messages())

    defnew_messages(self) -> list[_messages.ModelMessage]:
"""Return new messages for the run so far.

        Messages from older runs are excluded.
        """
        return self.all_messages()[self.ctx.deps.new_message_index :]

    defnew_messages_json(self) -> bytes:
"""Return new messages from [`new_messages`][pydantic_ai.agent.AgentRun.new_messages] as JSON bytes.

        Returns:
            JSON bytes representing the new messages.
        """
        return _messages.ModelMessagesTypeAdapter.dump_json(self.new_messages())

    def__aiter__(
        self,
    ) -> AsyncIterator[_agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]]:
"""Provide async-iteration over the nodes in the agent run."""
        return self

    async def__anext__(
        self,
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
"""Advance to the next node automatically based on the last returned node."""
        task = await anext(self._graph_run)
        return self._task_to_node(task)

    def_task_to_node(
        self, task: EndMarker[FinalResult[OutputDataT]] | JoinItem | Sequence[GraphTaskRequest]
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
        if isinstance(task, Sequence) and len(task) == 1:
            first_task = task[0]
            if isinstance(first_task.inputs, BaseNode):  # pragma: no branch
                base_node: BaseNode[
                    _agent_graph.GraphAgentState,
                    _agent_graph.GraphAgentDeps[AgentDepsT, OutputDataT],
                    FinalResult[OutputDataT],
                ] = first_task.inputs  # type: ignore[reportUnknownMemberType]
                if _agent_graph.is_agent_node(node=base_node):  # pragma: no branch
                    return base_node
        if isinstance(task, EndMarker):
            return End(task.value)
        raise exceptions.AgentRunError(f'Unexpected node: {task}')  # pragma: no cover

    def_node_to_task(self, node: _agent_graph.AgentNode[AgentDepsT, OutputDataT]) -> GraphTaskRequest:
        return GraphTaskRequest(NodeStep(type(node)).id, inputs=node, fork_stack=())

    async defnext(
        self,
        node: _agent_graph.AgentNode[AgentDepsT, OutputDataT],
    ) -> _agent_graph.AgentNode[AgentDepsT, OutputDataT] | End[FinalResult[OutputDataT]]:
"""Manually drive the agent run by passing in the node you want to run next.

        This lets you inspect or mutate the node before continuing execution, or skip certain nodes
        under dynamic conditions. The agent run should be stopped when you return an [`End`][pydantic_graph.nodes.End]
        node.

        Example:
        ```python
        from pydantic_ai import Agent
        from pydantic_graph import End

        agent = Agent('openai:gpt-4o')

        async def main():
            async with agent.iter('What is the capital of France?') as agent_run:
                next_node = agent_run.next_node  # start with the first node
                nodes = [next_node]
                while not isinstance(next_node, End):
                    next_node = await agent_run.next(next_node)
                    nodes.append(next_node)
                # Once `next_node` is an End, we've finished:
                print(nodes)
                '''
                [
                    UserPromptNode(
                        user_prompt='What is the capital of France?',
                        instructions_functions=[],
                        system_prompts=(),
                        system_prompt_functions=[],
                        system_prompt_dynamic_functions={},
                    ),
                    ModelRequestNode(
                        request=ModelRequest(
                            parts=[
                                UserPromptPart(
                                    content='What is the capital of France?',
                                    timestamp=datetime.datetime(...),
                                )
                            ],
                            timestamp=datetime.datetime(...),
                            run_id='...',
                        )
                    ),
                    CallToolsNode(
                        model_response=ModelResponse(
                            parts=[TextPart(content='The capital of France is Paris.')],
                            usage=RequestUsage(input_tokens=56, output_tokens=7),
                            model_name='gpt-4o',
                            timestamp=datetime.datetime(...),
                            run_id='...',
                        )
                    ),
                    End(data=FinalResult(output='The capital of France is Paris.')),
                ]
                '''
                print('Final result:', agent_run.result.output)
                #> Final result: The capital of France is Paris.
        ```

        Args:
            node: The node to run next in the graph.

        Returns:
            The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if
            the run has completed.
        """
        # Note: It might be nice to expose a synchronous interface for iteration, but we shouldn't do it
        # on this class, or else IDEs won't warn you if you accidentally use `for` instead of `async for` to iterate.
        task = [self._node_to_task(node)]
        try:
            task = await self._graph_run.next(task)
        except StopAsyncIteration:
            pass
        return self._task_to_node(task)

    # TODO (v2): Make this a property
    defusage(self) -> _usage.RunUsage:
"""Get usage statistics for the run so far, including token usage, model requests, and so on."""
        return self._graph_run.state.usage

    @property
    defmetadata(self) -> dict[str, Any] | None:
"""Metadata associated with this agent run, if configured."""
        return self._graph_run.state.metadata

    @property
    defrun_id(self) -> str:
"""The unique identifier for the agent run."""
        return self._graph_run.state.run_id

    def__repr__(self) -> str:  # pragma: no cover
        result = self._graph_run.output
        result_repr = '<run not finished>' if result is None else repr(result.output)
        return f'<{type(self).__name__} result={result_repr} usage={self.usage()}>'
````