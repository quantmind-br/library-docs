---
title: pydantic_evals.dataset - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_evals/dataset/
source: sitemap
fetched_at: 2026-01-22T22:24:43.731334517-03:00
rendered_js: false
word_count: 163
summary: This document defines the Dataset class, which facilitates organizing collections of test cases and evaluating them against task functions using custom evaluators. It includes methods for concurrent execution, retry management, and generating detailed evaluation reports.
tags:
    - pydantic-evals
    - test-automation
    - dataset-management
    - concurrency-control
    - python-api
    - evaluation-metrics
category: api
---

```
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
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
```

````
classDataset(BaseModel, Generic[InputsT, OutputT, MetadataT], extra='forbid', arbitrary_types_allowed=True):
"""A dataset of test [cases][pydantic_evals.Case].

    Datasets allow you to organize a collection of test cases and evaluate them against a task function.
    They can be loaded from and saved to YAML or JSON files, and can have dataset-level evaluators that
    apply to all cases.

    Example:
    ```python
    # Create a dataset with two test cases
    from dataclasses import dataclass

    from pydantic_evals import Case, Dataset
    from pydantic_evals.evaluators import Evaluator, EvaluatorContext


    @dataclass
    class ExactMatch(Evaluator):
        def evaluate(self, ctx: EvaluatorContext) -> bool:
            return ctx.output == ctx.expected_output

    dataset = Dataset(
        cases=[
            Case(name='test1', inputs={'text': 'Hello'}, expected_output='HELLO'),
            Case(name='test2', inputs={'text': 'World'}, expected_output='WORLD'),
        ],
        evaluators=[ExactMatch()],
    )

    # Evaluate the dataset against a task function
    async def uppercase(inputs: dict) -> str:
        return inputs['text'].upper()

    async def main():
        report = await dataset.evaluate(uppercase)
        report.print()
    '''
       Evaluation Summary: uppercase
    ┏━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
    ┃ Case ID  ┃ Assertions ┃ Duration ┃
    ┡━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
    │ test1    │ ✔          │     10ms │
    ├──────────┼────────────┼──────────┤
    │ test2    │ ✔          │     10ms │
    ├──────────┼────────────┼──────────┤
    │ Averages │ 100.0% ✔   │     10ms │
    └──────────┴────────────┴──────────┘
    '''
    ```
    """

    name: str | None = None
"""Optional name of the dataset."""
    cases: list[Case[InputsT, OutputT, MetadataT]]
"""List of test cases in the dataset."""
    evaluators: list[Evaluator[InputsT, OutputT, MetadataT]] = []
"""List of evaluators to be used on all cases in the dataset."""

    def__init__(
        self,
        *,
        name: str | None = None,
        cases: Sequence[Case[InputsT, OutputT, MetadataT]],
        evaluators: Sequence[Evaluator[InputsT, OutputT, MetadataT]] = (),
    ):
"""Initialize a new dataset with test cases and optional evaluators.

        Args:
            name: Optional name for the dataset.
            cases: Sequence of test cases to include in the dataset.
            evaluators: Optional sequence of evaluators to apply to all cases in the dataset.
        """
        case_names = set[str]()
        for case in cases:
            if case.name is None:
                continue
            if case.name in case_names:
                raise ValueError(f'Duplicate case name: {case.name!r}')
            case_names.add(case.name)

        super().__init__(
            name=name,
            cases=cases,
            evaluators=list(evaluators),
        )

    # TODO in v2: Make everything not required keyword-only
    async defevaluate(
        self,
        task: Callable[[InputsT], Awaitable[OutputT]] | Callable[[InputsT], OutputT],
        name: str | None = None,
        max_concurrency: int | None = None,
        progress: bool = True,
        retry_task: RetryConfig | None = None,
        retry_evaluators: RetryConfig | None = None,
        *,
        task_name: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> EvaluationReport[InputsT, OutputT, MetadataT]:
"""Evaluates the test cases in the dataset using the given task.

        This method runs the task on each case in the dataset, applies evaluators,
        and collects results into a report. Cases are run concurrently, limited by `max_concurrency` if specified.

        Args:
            task: The task to evaluate. This should be a callable that takes the inputs of the case
                and returns the output.
            name: The name of the experiment being run, this is used to identify the experiment in the report.
                If omitted, the task_name will be used; if that is not specified, the name of the task function is used.
            max_concurrency: The maximum number of concurrent evaluations of the task to allow.
                If None, all cases will be evaluated concurrently.
            progress: Whether to show a progress bar for the evaluation. Defaults to `True`.
            retry_task: Optional retry configuration for the task execution.
            retry_evaluators: Optional retry configuration for evaluator execution.
            task_name: Optional override to the name of the task being executed, otherwise the name of the task
                function will be used.
            metadata: Optional dict of experiment metadata.

        Returns:
            A report containing the results of the evaluation.
        """
        task_name = task_name or get_unwrapped_function_name(task)
        name = name or task_name
        total_cases = len(self.cases)
        progress_bar = Progress() if progress else None

        limiter = anyio.Semaphore(max_concurrency) if max_concurrency is not None else AsyncExitStack()

        extra_attributes: dict[str, Any] = {'gen_ai.operation.name': 'experiment'}
        if metadata is not None:
            extra_attributes['metadata'] = metadata
        with (
            logfire_span(
                'evaluate {name}',
                name=name,
                task_name=task_name,
                dataset_name=self.name,
                n_cases=len(self.cases),
                **extra_attributes,
            ) as eval_span,
            progress_bar or nullcontext(),
        ):
            task_id = progress_bar.add_task(f'Evaluating {task_name}', total=total_cases) if progress_bar else None

            async def_handle_case(case: Case[InputsT, OutputT, MetadataT], report_case_name: str):
                async with limiter:
                    result = await _run_task_and_evaluators(
                        task, case, report_case_name, self.evaluators, retry_task, retry_evaluators
                    )
                    if progress_bar and task_id is not None:  # pragma: no branch
                        progress_bar.update(task_id, advance=1)
                    return result

            if (context := eval_span.context) is None:  # pragma: no cover
                trace_id = None
                span_id = None
            else:
                trace_id = f'{context.trace_id:032x}'
                span_id = f'{context.span_id:016x}'
            cases_and_failures = await task_group_gather(
                [
                    lambda case=case, i=i: _handle_case(case, case.name or f'Case {i}')
                    for i, case in enumerate(self.cases, 1)
                ]
            )
            cases: list[ReportCase] = []
            failures: list[ReportCaseFailure] = []
            for item in cases_and_failures:
                if isinstance(item, ReportCase):
                    cases.append(item)
                else:
                    failures.append(item)
            report = EvaluationReport(
                name=name,
                cases=cases,
                failures=failures,
                experiment_metadata=metadata,
                span_id=span_id,
                trace_id=trace_id,
            )
            full_experiment_metadata: dict[str, Any] = {'n_cases': len(self.cases)}
            if metadata is not None:
                full_experiment_metadata['metadata'] = metadata
            if (averages := report.averages()) is not None:
                full_experiment_metadata['averages'] = averages
                if averages.assertions is not None:
                    eval_span.set_attribute('assertion_pass_rate', averages.assertions)
            eval_span.set_attribute('logfire.experiment.metadata', full_experiment_metadata)
        return report

    defevaluate_sync(
        self,
        task: Callable[[InputsT], Awaitable[OutputT]] | Callable[[InputsT], OutputT],
        name: str | None = None,
        max_concurrency: int | None = None,
        progress: bool = True,
        retry_task: RetryConfig | None = None,
        retry_evaluators: RetryConfig | None = None,
        *,
        task_name: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> EvaluationReport[InputsT, OutputT, MetadataT]:
"""Evaluates the test cases in the dataset using the given task.

        This is a synchronous wrapper around [`evaluate`][pydantic_evals.dataset.Dataset.evaluate] provided for convenience.

        Args:
            task: The task to evaluate. This should be a callable that takes the inputs of the case
                and returns the output.
            name: The name of the experiment being run, this is used to identify the experiment in the report.
                If omitted, the task_name will be used; if that is not specified, the name of the task function is used.
            max_concurrency: The maximum number of concurrent evaluations of the task to allow.
                If None, all cases will be evaluated concurrently.
            progress: Whether to show a progress bar for the evaluation. Defaults to `True`.
            retry_task: Optional retry configuration for the task execution.
            retry_evaluators: Optional retry configuration for evaluator execution.
            task_name: Optional override to the name of the task being executed, otherwise the name of the task
                function will be used.
            metadata: Optional dict of experiment metadata.

        Returns:
            A report containing the results of the evaluation.
        """
        return get_event_loop().run_until_complete(
            self.evaluate(
                task,
                name=name,
                max_concurrency=max_concurrency,
                progress=progress,
                retry_task=retry_task,
                retry_evaluators=retry_evaluators,
                task_name=task_name,
                metadata=metadata,
            )
        )

    defadd_case(
        self,
        *,
        name: str | None = None,
        inputs: InputsT,
        metadata: MetadataT | None = None,
        expected_output: OutputT | None = None,
        evaluators: tuple[Evaluator[InputsT, OutputT, MetadataT], ...] = (),
    ) -> None:
"""Adds a case to the dataset.

        This is a convenience method for creating a [`Case`][pydantic_evals.Case] and adding it to the dataset.

        Args:
            name: Optional name for the case. If not provided, a generic name will be assigned.
            inputs: The inputs to the task being evaluated.
            metadata: Optional metadata for the case, which can be used by evaluators.
            expected_output: The expected output of the task, used for comparison in evaluators.
            evaluators: Tuple of evaluators specific to this case, in addition to dataset-level evaluators.
        """
        if name in {case.name for case in self.cases}:
            raise ValueError(f'Duplicate case name: {name!r}')

        case = Case[InputsT, OutputT, MetadataT](
            name=name,
            inputs=inputs,
            metadata=metadata,
            expected_output=expected_output,
            evaluators=evaluators,
        )
        self.cases.append(case)

    defadd_evaluator(
        self,
        evaluator: Evaluator[InputsT, OutputT, MetadataT],
        specific_case: str | None = None,
    ) -> None:
"""Adds an evaluator to the dataset or a specific case.

        Args:
            evaluator: The evaluator to add.
            specific_case: If provided, the evaluator will only be added to the case with this name.
                If None, the evaluator will be added to all cases in the dataset.

        Raises:
            ValueError: If `specific_case` is provided but no case with that name exists in the dataset.
        """
        if specific_case is None:
            self.evaluators.append(evaluator)
        else:
            # If this is too slow, we could try to add a case lookup dict.
            # Note that if we do that, we'd need to make the cases list private to prevent modification.
            added = False
            for case in self.cases:
                if case.name == specific_case:
                    case.evaluators.append(evaluator)
                    added = True
            if not added:
                raise ValueError(f'Case {specific_case!r} not found in the dataset')

    @classmethod
    @functools.cache
    def_params(cls) -> tuple[type[InputsT], type[OutputT], type[MetadataT]]:
"""Get the type parameters for the Dataset class.

        Returns:
            A tuple of (InputsT, OutputT, MetadataT) types.
        """
        for c in cls.__mro__:
            metadata = getattr(c, '__pydantic_generic_metadata__', {})
            if len(args := (metadata.get('args', ()) or getattr(c, '__args__', ()))) == 3:  # pragma: no branch
                return args
        else:  # pragma: no cover
            warnings.warn(
                f'Could not determine the generic parameters for {cls}; using `Any` for each.'
                f' You should explicitly set the generic parameters via `Dataset[MyInputs, MyOutput, MyMetadata]`'
                f' when serializing or deserializing.',
                UserWarning,
            )
            return Any, Any, Any  # type: ignore

    @classmethod
    deffrom_file(
        cls,
        path: Path | str,
        fmt: Literal['yaml', 'json'] | None = None,
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    ) -> Self:
"""Load a dataset from a file.

        Args:
            path: Path to the file to load.
            fmt: Format of the file. If None, the format will be inferred from the file extension.
                Must be either 'yaml' or 'json'.
            custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.
                These are additional evaluators beyond the default ones.

        Returns:
            A new Dataset instance loaded from the file.

        Raises:
            ValidationError: If the file cannot be parsed as a valid dataset.
            ValueError: If the format cannot be inferred from the file extension.
        """
        path = Path(path)
        fmt = cls._infer_fmt(path, fmt)

        raw = Path(path).read_text(encoding='utf-8')
        try:
            return cls.from_text(raw, fmt=fmt, custom_evaluator_types=custom_evaluator_types, default_name=path.stem)
        except ValidationError as e:  # pragma: no cover
            raise ValueError(f'{path} contains data that does not match the schema for {cls.__name__}:\n{e}.') frome

    @classmethod
    deffrom_text(
        cls,
        contents: str,
        fmt: Literal['yaml', 'json'] = 'yaml',
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
        *,
        default_name: str | None = None,
    ) -> Self:
"""Load a dataset from a string.

        Args:
            contents: The string content to parse.
            fmt: Format of the content. Must be either 'yaml' or 'json'.
            custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.
                These are additional evaluators beyond the default ones.
            default_name: Default name of the dataset, to be used if not specified in the serialized contents.

        Returns:
            A new Dataset instance parsed from the string.

        Raises:
            ValidationError: If the content cannot be parsed as a valid dataset.
        """
        if fmt == 'yaml':
            loaded = yaml.safe_load(contents)
            return cls.from_dict(loaded, custom_evaluator_types, default_name=default_name)
        else:
            dataset_model_type = cls._serialization_type()
            dataset_model = dataset_model_type.model_validate_json(contents)
            return cls._from_dataset_model(dataset_model, custom_evaluator_types, default_name)

    @classmethod
    deffrom_dict(
        cls,
        data: dict[str, Any],
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
        *,
        default_name: str | None = None,
    ) -> Self:
"""Load a dataset from a dictionary.

        Args:
            data: Dictionary representation of the dataset.
            custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.
                These are additional evaluators beyond the default ones.
            default_name: Default name of the dataset, to be used if not specified in the data.

        Returns:
            A new Dataset instance created from the dictionary.

        Raises:
            ValidationError: If the dictionary cannot be converted to a valid dataset.
        """
        dataset_model_type = cls._serialization_type()
        dataset_model = dataset_model_type.model_validate(data)
        return cls._from_dataset_model(dataset_model, custom_evaluator_types, default_name)

    @classmethod
    def_from_dataset_model(
        cls,
        dataset_model: _DatasetModel[InputsT, OutputT, MetadataT],
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
        default_name: str | None = None,
    ) -> Self:
"""Create a Dataset from a _DatasetModel.

        Args:
            dataset_model: The _DatasetModel to convert.
            custom_evaluator_types: Custom evaluator classes to register for deserialization.
            default_name: Default name of the dataset, to be used if the value is `None` in the provided model.

        Returns:
            A new Dataset instance created from the _DatasetModel.
        """
        registry = _get_registry(custom_evaluator_types)

        cases: list[Case[InputsT, OutputT, MetadataT]] = []
        errors: list[ValueError] = []
        dataset_evaluators: list[Evaluator] = []
        for spec in dataset_model.evaluators:
            try:
                dataset_evaluator = _load_evaluator_from_registry(registry, None, spec)
            except ValueError as e:
                errors.append(e)
                continue
            dataset_evaluators.append(dataset_evaluator)

        for row in dataset_model.cases:
            evaluators: list[Evaluator] = []
            for spec in row.evaluators:
                try:
                    evaluator = _load_evaluator_from_registry(registry, row.name, spec)
                except ValueError as e:
                    errors.append(e)
                    continue
                evaluators.append(evaluator)
            row = Case[InputsT, OutputT, MetadataT](
                name=row.name,
                inputs=row.inputs,
                metadata=row.metadata,
                expected_output=row.expected_output,
            )
            row.evaluators = evaluators
            cases.append(row)
        if errors:
            raise ExceptionGroup(f'{len(errors)} error(s) loading evaluators from registry', errors[:3])
        result = cls(name=dataset_model.name, cases=cases)
        if result.name is None:
            result.name = default_name
        result.evaluators = dataset_evaluators
        return result

    defto_file(
        self,
        path: Path | str,
        fmt: Literal['yaml', 'json'] | None = None,
        schema_path: Path | str | None = DEFAULT_SCHEMA_PATH_TEMPLATE,
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    ):
"""Save the dataset to a file.

        Args:
            path: Path to save the dataset to.
            fmt: Format to use. If None, the format will be inferred from the file extension.
                Must be either 'yaml' or 'json'.
            schema_path: Path to save the JSON schema to. If None, no schema will be saved.
                Can be a string template with {stem} which will be replaced with the dataset filename stem.
            custom_evaluator_types: Custom evaluator classes to include in the schema.
        """
        path = Path(path)
        fmt = self._infer_fmt(path, fmt)

        schema_ref: str | None = None
        if schema_path is not None:  # pragma: no branch
            if isinstance(schema_path, str):  # pragma: no branch
                schema_path = Path(schema_path.format(stem=path.stem))

            if not schema_path.is_absolute():
                schema_ref = str(schema_path)
                schema_path = path.parent / schema_path
            elif schema_path.is_relative_to(path):  # pragma: no cover
                schema_ref = str(_get_relative_path_reference(schema_path, path))
            else:  # pragma: no cover
                schema_ref = str(schema_path)
            self._save_schema(schema_path, custom_evaluator_types)

        context: dict[str, Any] = {'use_short_form': True}
        if fmt == 'yaml':
            dumped_data = self.model_dump(mode='json', by_alias=True, context=context)
            content = yaml.dump(dumped_data, sort_keys=False)
            if schema_ref:  # pragma: no branch
                yaml_language_server_line = f'{_YAML_SCHEMA_LINE_PREFIX}{schema_ref}'
                content = f'{yaml_language_server_line}\n{content}'
            path.write_text(content, encoding='utf-8')
        else:
            context['$schema'] = schema_ref
            json_data = self.model_dump_json(indent=2, by_alias=True, context=context)
            path.write_text(json_data + '\n', encoding='utf-8')

    @classmethod
    defmodel_json_schema_with_evaluators(
        cls,
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    ) -> dict[str, Any]:
"""Generate a JSON schema for this dataset type, including evaluator details.

        This is useful for generating a schema that can be used to validate YAML-format dataset files.

        Args:
            custom_evaluator_types: Custom evaluator classes to include in the schema.

        Returns:
            A dictionary representing the JSON schema.
        """
        # Note: this function could maybe be simplified now that Evaluators are always dataclasses
        registry = _get_registry(custom_evaluator_types)

        evaluator_schema_types: list[Any] = []
        for name, evaluator_class in registry.items():
            type_hints = _typing_extra.get_function_type_hints(evaluator_class)
            type_hints.pop('return', None)
            required_type_hints: dict[str, Any] = {}

            for p in inspect.signature(evaluator_class).parameters.values():
                type_hints.setdefault(p.name, Any)
                if p.default is not p.empty:
                    type_hints[p.name] = NotRequired[type_hints[p.name]]
                else:
                    required_type_hints[p.name] = type_hints[p.name]

            def_make_typed_dict(cls_name_prefix: str, fields: dict[str, Any]) -> Any:
                td = TypedDict(f'{cls_name_prefix}_{name}', fields)  # pyright: ignore[reportArgumentType]
                config = ConfigDict(extra='forbid', arbitrary_types_allowed=True)
                # TODO: Replace with pydantic.with_config once pydantic 2.11 is the min supported version
                td.__pydantic_config__ = config  # pyright: ignore[reportAttributeAccessIssue]
                return td

            # Shortest form: just the call name
            if len(type_hints) == 0 or not required_type_hints:
                evaluator_schema_types.append(Literal[name])

            # Short form: can be called with only one parameter
            if len(type_hints) == 1:
                [type_hint_type] = type_hints.values()
                evaluator_schema_types.append(_make_typed_dict('short_evaluator', {name: type_hint_type}))
            elif len(required_type_hints) == 1:  # pragma: no branch
                [type_hint_type] = required_type_hints.values()
                evaluator_schema_types.append(_make_typed_dict('short_evaluator', {name: type_hint_type}))

            # Long form: multiple parameters, possibly required
            if len(type_hints) > 1:
                params_td = _make_typed_dict('evaluator_params', type_hints)
                evaluator_schema_types.append(_make_typed_dict('evaluator', {name: params_td}))

        in_type, out_type, meta_type = cls._params()

        # Note: we shadow the `Case` and `Dataset` class names here to generate a clean JSON schema
        classCase(BaseModel, extra='forbid'):  # pyright: ignore[reportUnusedClass]  # this _is_ used below, but pyright doesn't seem to notice..
            name: str | None = None
            inputs: in_type  # pyright: ignore[reportInvalidTypeForm]
            metadata: meta_type | None = None  # pyright: ignore[reportInvalidTypeForm,reportUnknownVariableType]
            expected_output: out_type | None = None  # pyright: ignore[reportInvalidTypeForm,reportUnknownVariableType]
            if evaluator_schema_types:  # pragma: no branch
                evaluators: list[Union[tuple(evaluator_schema_types)]] = []  # pyright: ignore  # noqa: UP007

        classDataset(BaseModel, extra='forbid'):
            name: str | None = None
            cases: list[Case]
            if evaluator_schema_types:  # pragma: no branch
                evaluators: list[Union[tuple(evaluator_schema_types)]] = []  # pyright: ignore  # noqa: UP007

        json_schema = Dataset.model_json_schema()
        # See `_add_json_schema` below, since `$schema` is added to the JSON, it has to be supported in the JSON
        json_schema['properties']['$schema'] = {'type': 'string'}
        return json_schema

    @classmethod
    def_save_schema(
        cls, path: Path | str, custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = ()
    ):
"""Save the JSON schema for this dataset type to a file.

        Args:
            path: Path to save the schema to.
            custom_evaluator_types: Custom evaluator classes to include in the schema.
        """
        path = Path(path)
        json_schema = cls.model_json_schema_with_evaluators(custom_evaluator_types)
        schema_content = to_json(json_schema, indent=2).decode() + '\n'
        if not path.exists() or path.read_text(encoding='utf-8') != schema_content:  # pragma: no branch
            path.write_text(schema_content, encoding='utf-8')

    @classmethod
    @functools.cache
    def_serialization_type(cls) -> type[_DatasetModel[InputsT, OutputT, MetadataT]]:
"""Get the serialization type for this dataset class.

        Returns:
            A _DatasetModel type with the same generic parameters as this Dataset class.
        """
        input_type, output_type, metadata_type = cls._params()
        return _DatasetModel[input_type, output_type, metadata_type]

    @classmethod
    def_infer_fmt(cls, path: Path, fmt: Literal['yaml', 'json'] | None) -> Literal['yaml', 'json']:
"""Infer the format to use for a file based on its extension.

        Args:
            path: The path to infer the format for.
            fmt: The explicitly provided format, if any.

        Returns:
            The inferred format ('yaml' or 'json').

        Raises:
            ValueError: If the format cannot be inferred from the file extension.
        """
        if fmt is not None:
            return fmt
        suffix = path.suffix.lower()
        if suffix in {'.yaml', '.yml'}:
            return 'yaml'
        elif suffix == '.json':
            return 'json'
        raise ValueError(
            f'Could not infer format for filename {path.name!r}. Use the `fmt` argument to specify the format.'
        )

    @model_serializer(mode='wrap')
    def_add_json_schema(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo) -> dict[str, Any]:
"""Add the JSON schema path to the serialized output.

        See <https://github.com/json-schema-org/json-schema-spec/issues/828> for context, that seems to be the nearest
        there is to a spec for this.
        """
        context = cast(dict[str, Any] | None, info.context)
        if isinstance(context, dict) and (schema := context.get('$schema')):
            return {'$schema': schema} | nxt(self)
        else:
            return nxt(self)
````