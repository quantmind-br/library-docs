---
title: pydantic_evals.evaluators - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_evals/evaluators/
source: sitemap
fetched_at: 2026-01-22T22:24:45.915299865-03:00
rendered_js: false
word_count: 83
summary: Defines the abstract base Evaluator class for implementing custom task performance assessments with support for both synchronous and asynchronous execution.
tags:
    - pydantic-evals
    - evaluator-base-class
    - asynchronous-execution
    - serialization
    - python-api
category: api
---

```
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
302
```

````
@dataclass(repr=False)
classEvaluator(Generic[InputsT, OutputT, MetadataT], metaclass=_StrictABCMeta):
"""Base class for all evaluators.

    Evaluators can assess the performance of a task in a variety of ways, as a function of the EvaluatorContext.

    Subclasses must implement the `evaluate` method. Note it can be defined with either `def` or `async def`.

    Example:
    ```python
    from dataclasses import dataclass

    from pydantic_evals.evaluators import Evaluator, EvaluatorContext


    @dataclass
    class ExactMatch(Evaluator):
        def evaluate(self, ctx: EvaluatorContext) -> bool:
            return ctx.output == ctx.expected_output
    ```
    """

    __pydantic_config__ = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    defget_serialization_name(cls) -> str:
"""Return the 'name' of this Evaluator to use during serialization.

        Returns:
            The name of the Evaluator, which is typically the class name.
        """
        return cls.__name__

    @classmethod
    @deprecated('`name` has been renamed, use `get_serialization_name` instead.')
    defname(cls) -> str:
"""`name` has been renamed, use `get_serialization_name` instead."""
        return cls.get_serialization_name()

    defget_default_evaluation_name(self) -> str:
"""Return the default name to use in reports for the output of this evaluator.

        By default, if the evaluator has an attribute called `evaluation_name` of type string, that will be used.
        Otherwise, the serialization name of the evaluator (which is usually the class name) will be used.

        This can be overridden to get a more descriptive name in evaluation reports, e.g. using instance information.

        Note that evaluators that return a mapping of results will always use the keys of that mapping as the names
        of the associated evaluation results.
        """
        evaluation_name = getattr(self, 'evaluation_name', None)
        if isinstance(evaluation_name, str):
            # If the evaluator has an attribute `name` of type string, use that
            return evaluation_name

        return self.get_serialization_name()

    @abstractmethod
    defevaluate(
        self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]
    ) -> EvaluatorOutput | Awaitable[EvaluatorOutput]:  # pragma: no cover
"""Evaluate the task output in the given context.

        This is the main evaluation method that subclasses must implement. It can be either synchronous
        or asynchronous, returning either an EvaluatorOutput directly or an Awaitable[EvaluatorOutput].

        Args:
            ctx: The context containing the inputs, outputs, and metadata for evaluation.

        Returns:
            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
            of evaluation names to either of those. Can be returned either synchronously or as an
            awaitable for asynchronous evaluation.
        """
        raise NotImplementedError('You must implement `evaluate`.')

    defevaluate_sync(self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]) -> EvaluatorOutput:
"""Run the evaluator synchronously, handling both sync and async implementations.

        This method ensures synchronous execution by running any async evaluate implementation
        to completion using run_until_complete.

        Args:
            ctx: The context containing the inputs, outputs, and metadata for evaluation.

        Returns:
            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
            of evaluation names to either of those.
        """
        output = self.evaluate(ctx)
        if inspect.iscoroutine(output):  # pragma: no cover
            return get_event_loop().run_until_complete(output)
        else:
            return cast(EvaluatorOutput, output)

    async defevaluate_async(self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]) -> EvaluatorOutput:
"""Run the evaluator asynchronously, handling both sync and async implementations.

        This method ensures asynchronous execution by properly awaiting any async evaluate
        implementation. For synchronous implementations, it returns the result directly.

        Args:
            ctx: The context containing the inputs, outputs, and metadata for evaluation.

        Returns:
            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
            of evaluation names to either of those.
        """
        # Note: If self.evaluate is synchronous, but you need to prevent this from blocking, override this method with:
        # return await anyio.to_thread.run_sync(self.evaluate, ctx)
        output = self.evaluate(ctx)
        if inspect.iscoroutine(output):
            return await output
        else:
            return cast(EvaluatorOutput, output)

    @model_serializer(mode='plain')
    defserialize(self, info: SerializationInfo) -> Any:
"""Serialize this Evaluator to a JSON-serializable form.

        Returns:
            A JSON-serializable representation of this evaluator as an EvaluatorSpec.
        """
        return to_jsonable_python(
            self.as_spec(),
            context=info.context,
            serialize_unknown=True,
        )

    defas_spec(self) -> EvaluatorSpec:
        raw_arguments = self.build_serialization_arguments()

        arguments: None | tuple[Any,] | dict[str, Any]
        if len(raw_arguments) == 0:
            arguments = None
        elif len(raw_arguments) == 1:
            arguments = (next(iter(raw_arguments.values())),)
        else:
            arguments = raw_arguments

        return EvaluatorSpec(name=self.get_serialization_name(), arguments=arguments)

    defbuild_serialization_arguments(self) -> dict[str, Any]:
"""Build the arguments for serialization.

        Evaluators are serialized for inclusion as the "source" in an `EvaluationResult`.
        If you want to modify how the evaluator is serialized for that or other purposes, you can override this method.

        Returns:
            A dictionary of arguments to be used during serialization.
        """
        raw_arguments: dict[str, Any] = {}
        for field in fields(self):
            value = getattr(self, field.name)
            # always exclude defaults:
            if field.default is not MISSING:
                if value == field.default:
                    continue
            if field.default_factory is not MISSING:
                if value == field.default_factory():  # pragma: no branch
                    continue
            raw_arguments[field.name] = value
        return raw_arguments

    __repr__ = _utils.dataclasses_no_defaults_repr
````