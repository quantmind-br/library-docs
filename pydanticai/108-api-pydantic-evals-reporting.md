---
title: pydantic_evals.reporting - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_evals/reporting/
source: sitemap
fetched_at: 2026-01-22T22:24:51.316506557-03:00
rendered_js: false
word_count: 129
summary: Defines the EvaluationReport class for aggregating, summarizing, and rendering results from model evaluation experiments, including support for performance metrics and console output.
tags:
    - python
    - model-evaluation
    - reporting
    - rich-console
    - experiment-tracking
    - dataclass
category: api
---

```
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
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
```

```
@dataclass(kw_only=True)
classEvaluationReport(Generic[InputsT, OutputT, MetadataT]):
"""A report of the results of evaluating a model on a set of cases."""

    name: str
"""The name of the report."""

    cases: list[ReportCase[InputsT, OutputT, MetadataT]]
"""The cases in the report."""
    failures: list[ReportCaseFailure[InputsT, OutputT, MetadataT]] = field(default_factory=list)
"""The failures in the report. These are cases where task execution raised an exception."""

    experiment_metadata: dict[str, Any] | None = None
"""Metadata associated with the specific experiment represented by this report."""
    trace_id: str | None = None
"""The trace ID of the evaluation."""
    span_id: str | None = None
"""The span ID of the evaluation."""

    defaverages(self) -> ReportCaseAggregate | None:
        if self.cases:
            return ReportCaseAggregate.average(self.cases)
        return None

    defrender(
        self,
        width: int | None = None,
        baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None,
        *,
        include_input: bool = False,
        include_metadata: bool = False,
        include_expected_output: bool = False,
        include_output: bool = False,
        include_durations: bool = True,
        include_total_duration: bool = False,
        include_removed_cases: bool = False,
        include_averages: bool = True,
        include_errors: bool = True,
        include_error_stacktrace: bool = False,
        include_evaluator_failures: bool = True,
        input_config: RenderValueConfig | None = None,
        metadata_config: RenderValueConfig | None = None,
        output_config: RenderValueConfig | None = None,
        score_configs: dict[str, RenderNumberConfig] | None = None,
        label_configs: dict[str, RenderValueConfig] | None = None,
        metric_configs: dict[str, RenderNumberConfig] | None = None,
        duration_config: RenderNumberConfig | None = None,
        include_reasons: bool = False,
    ) -> str:
"""Render this report to a nicely-formatted string, optionally comparing it to a baseline report.

        If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.
        """
        io_file = StringIO()
        console = Console(width=width, file=io_file)
        self.print(
            width=width,
            baseline=baseline,
            console=console,
            include_input=include_input,
            include_metadata=include_metadata,
            include_expected_output=include_expected_output,
            include_output=include_output,
            include_durations=include_durations,
            include_total_duration=include_total_duration,
            include_removed_cases=include_removed_cases,
            include_averages=include_averages,
            include_errors=include_errors,
            include_error_stacktrace=include_error_stacktrace,
            include_evaluator_failures=include_evaluator_failures,
            input_config=input_config,
            metadata_config=metadata_config,
            output_config=output_config,
            score_configs=score_configs,
            label_configs=label_configs,
            metric_configs=metric_configs,
            duration_config=duration_config,
            include_reasons=include_reasons,
        )
        return io_file.getvalue()

    defprint(
        self,
        width: int | None = None,
        baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None,
        *,
        console: Console | None = None,
        include_input: bool = False,
        include_metadata: bool = False,
        include_expected_output: bool = False,
        include_output: bool = False,
        include_durations: bool = True,
        include_total_duration: bool = False,
        include_removed_cases: bool = False,
        include_averages: bool = True,
        include_errors: bool = True,
        include_error_stacktrace: bool = False,
        include_evaluator_failures: bool = True,
        input_config: RenderValueConfig | None = None,
        metadata_config: RenderValueConfig | None = None,
        output_config: RenderValueConfig | None = None,
        score_configs: dict[str, RenderNumberConfig] | None = None,
        label_configs: dict[str, RenderValueConfig] | None = None,
        metric_configs: dict[str, RenderNumberConfig] | None = None,
        duration_config: RenderNumberConfig | None = None,
        include_reasons: bool = False,
    ) -> None:
"""Print this report to the console, optionally comparing it to a baseline report.

        If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.
        """
        if console is None:  # pragma: no branch
            console = Console(width=width)

        metadata_panel = self._metadata_panel(baseline=baseline)
        renderable: RenderableType = self.console_table(
            baseline=baseline,
            include_input=include_input,
            include_metadata=include_metadata,
            include_expected_output=include_expected_output,
            include_output=include_output,
            include_durations=include_durations,
            include_total_duration=include_total_duration,
            include_removed_cases=include_removed_cases,
            include_averages=include_averages,
            include_evaluator_failures=include_evaluator_failures,
            input_config=input_config,
            metadata_config=metadata_config,
            output_config=output_config,
            score_configs=score_configs,
            label_configs=label_configs,
            metric_configs=metric_configs,
            duration_config=duration_config,
            include_reasons=include_reasons,
            with_title=not metadata_panel,
        )
        # Wrap table with experiment metadata panel if present
        if metadata_panel:
            renderable = Group(metadata_panel, renderable)
        console.print(renderable)
        if include_errors and self.failures:  # pragma: no cover
            failures_table = self.failures_table(
                include_input=include_input,
                include_metadata=include_metadata,
                include_expected_output=include_expected_output,
                include_error_message=True,
                include_error_stacktrace=include_error_stacktrace,
                input_config=input_config,
                metadata_config=metadata_config,
            )
            console.print(failures_table, style='red')

    # TODO(DavidM): in v2, change the return type here to RenderableType
    defconsole_table(
        self,
        baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None,
        *,
        include_input: bool = False,
        include_metadata: bool = False,
        include_expected_output: bool = False,
        include_output: bool = False,
        include_durations: bool = True,
        include_total_duration: bool = False,
        include_removed_cases: bool = False,
        include_averages: bool = True,
        include_evaluator_failures: bool = True,
        input_config: RenderValueConfig | None = None,
        metadata_config: RenderValueConfig | None = None,
        output_config: RenderValueConfig | None = None,
        score_configs: dict[str, RenderNumberConfig] | None = None,
        label_configs: dict[str, RenderValueConfig] | None = None,
        metric_configs: dict[str, RenderNumberConfig] | None = None,
        duration_config: RenderNumberConfig | None = None,
        include_reasons: bool = False,
        with_title: bool = True,
    ) -> Table:
"""Return a table containing the data from this report.

        If a baseline is provided, returns a diff between this report and the baseline report.
        Optionally include input and output details.
        """
        renderer = EvaluationRenderer(
            include_input=include_input,
            include_metadata=include_metadata,
            include_expected_output=include_expected_output,
            include_output=include_output,
            include_durations=include_durations,
            include_total_duration=include_total_duration,
            include_removed_cases=include_removed_cases,
            include_averages=include_averages,
            include_error_message=False,
            include_error_stacktrace=False,
            include_evaluator_failures=include_evaluator_failures,
            input_config={**_DEFAULT_VALUE_CONFIG, **(input_config or {})},
            metadata_config={**_DEFAULT_VALUE_CONFIG, **(metadata_config or {})},
            output_config=output_config or _DEFAULT_VALUE_CONFIG,
            score_configs=score_configs or {},
            label_configs=label_configs or {},
            metric_configs=metric_configs or {},
            duration_config=duration_config or _DEFAULT_DURATION_CONFIG,
            include_reasons=include_reasons,
        )
        if baseline is None:
            return renderer.build_table(self, with_title=with_title)
        else:
            return renderer.build_diff_table(self, baseline, with_title=with_title)

    def_metadata_panel(
        self, baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None
    ) -> RenderableType | None:
"""Wrap a table with an experiment metadata panel if metadata exists.

        Args:
            table: The table to wrap
            baseline: Optional baseline report for diff metadata

        Returns:
            Either the table unchanged or a Group with Panel and Table
        """
        if baseline is None:
            # Single report - show metadata if present
            if self.experiment_metadata:
                metadata_text = Text()
                items = list(self.experiment_metadata.items())
                for i, (key, value) in enumerate(items):
                    metadata_text.append(f'{key}: {value}', style='dim')
                    if i < len(items) - 1:
                        metadata_text.append('\n')
                return Panel(
                    metadata_text,
                    title=f'Evaluation Summary: {self.name}',
                    title_align='left',
                    border_style='dim',
                    padding=(0, 1),
                    expand=False,
                )
        else:
            # Diff report - show metadata diff if either has metadata
            if self.experiment_metadata or baseline.experiment_metadata:
                diff_name = baseline.name if baseline.name == self.name else f'{baseline.name} → {self.name}'
                metadata_text = Text()
                lines_styles: list[tuple[str, str]] = []
                if baseline.experiment_metadata and self.experiment_metadata:
                    # Collect all keys from both
                    all_keys = sorted(set(baseline.experiment_metadata.keys()) | set(self.experiment_metadata.keys()))
                    for key in all_keys:
                        baseline_val = baseline.experiment_metadata.get(key)
                        report_val = self.experiment_metadata.get(key)
                        if baseline_val == report_val:
                            lines_styles.append((f'{key}: {report_val}', 'dim'))
                        elif baseline_val is None:
                            lines_styles.append((f'+ {key}: {report_val}', 'green'))
                        elif report_val is None:
                            lines_styles.append((f'- {key}: {baseline_val}', 'red'))
                        else:
                            lines_styles.append((f'{key}: {baseline_val} → {report_val}', 'yellow'))
                elif self.experiment_metadata:
                    lines_styles = [(f'+ {k}: {v}', 'green') for k, v in self.experiment_metadata.items()]
                else:  # baseline.experiment_metadata only
                    assert baseline.experiment_metadata is not None
                    lines_styles = [(f'- {k}: {v}', 'red') for k, v in baseline.experiment_metadata.items()]

                for i, (line, style) in enumerate(lines_styles):
                    metadata_text.append(line, style=style)
                    if i < len(lines_styles) - 1:
                        metadata_text.append('\n')

                return Panel(
                    metadata_text,
                    title=f'Evaluation Diff: {diff_name}',
                    title_align='left',
                    border_style='dim',
                    padding=(0, 1),
                    expand=False,
                )

        return None

    # TODO(DavidM): in v2, change the return type here to RenderableType
    deffailures_table(
        self,
        *,
        include_input: bool = False,
        include_metadata: bool = False,
        include_expected_output: bool = False,
        include_error_message: bool = True,
        include_error_stacktrace: bool = True,
        input_config: RenderValueConfig | None = None,
        metadata_config: RenderValueConfig | None = None,
    ) -> Table:
"""Return a table containing the failures in this report."""
        renderer = EvaluationRenderer(
            include_input=include_input,
            include_metadata=include_metadata,
            include_expected_output=include_expected_output,
            include_output=False,
            include_durations=False,
            include_total_duration=False,
            include_removed_cases=False,
            include_averages=False,
            input_config={**_DEFAULT_VALUE_CONFIG, **(input_config or {})},
            metadata_config={**_DEFAULT_VALUE_CONFIG, **(metadata_config or {})},
            output_config=_DEFAULT_VALUE_CONFIG,
            score_configs={},
            label_configs={},
            metric_configs={},
            duration_config=_DEFAULT_DURATION_CONFIG,
            include_reasons=False,
            include_error_message=include_error_message,
            include_error_stacktrace=include_error_stacktrace,
            include_evaluator_failures=False,  # Not applicable for failures table
        )
        return renderer.build_failures_table(self)

    def__str__(self) -> str:  # pragma: lax no cover
"""Return a string representation of the report."""
        return self.render()
```