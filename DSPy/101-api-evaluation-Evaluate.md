---
title: Evaluate - DSPy
url: https://dspy.ai/api/evaluation/Evaluate/
source: sitemap
fetched_at: 2026-01-23T08:01:32.358475425-03:00
rendered_js: false
word_count: 8
summary: This document defines the primary evaluation interface for DSPy programs, detailing parameters for metrics, datasets, and execution settings such as parallel threads and result visualization.
tags:
    - dspy
    - evaluation
    - python-api
    - metrics
    - parallel-execution
    - machine-learning
category: api
---

```
@with_callbacks
def__call__(
    self,
    program: "dspy.Module",
    metric: Callable | None = None,
    devset: list["dspy.Example"] | None = None,
    num_threads: int | None = None,
    display_progress: bool | None = None,
    display_table: bool | int | None = None,
    callback_metadata: dict[str, Any] | None = None,
    save_as_csv: str | None = None,
    save_as_json: str | None = None,
) -> EvaluationResult:
"""
    Args:
        program (dspy.Module): The DSPy program to evaluate.
        metric (Callable): The metric function to use for evaluation. if not provided, use `self.metric`.
        devset (list[dspy.Example]): the evaluation dataset. if not provided, use `self.devset`.
        num_threads (Optional[int]): The number of threads to use for parallel evaluation. if not provided, use
            `self.num_threads`.
        display_progress (bool): Whether to display progress during evaluation. if not provided, use
            `self.display_progress`.
        display_table (Union[bool, int]): Whether to display the evaluation results in a table. if not provided, use
            `self.display_table`. If a number is passed, the evaluation results will be truncated to that number before displayed.
        callback_metadata (dict): Metadata to be used for evaluate callback handlers.

    Returns:
        The evaluation results are returned as a dspy.EvaluationResult object containing the following attributes:

        - score: A float percentage score (e.g., 67.30) representing overall performance

        - results: a list of (example, prediction, score) tuples for each example in devset
    """
    metric = metric if metric is not None else self.metric
    devset = devset if devset is not None else self.devset
    num_threads = num_threads if num_threads is not None else self.num_threads
    display_progress = display_progress if display_progress is not None else self.display_progress
    display_table = display_table if display_table is not None else self.display_table
    save_as_csv = save_as_csv if save_as_csv is not None else self.save_as_csv
    save_as_json = save_as_json if save_as_json is not None else self.save_as_json

    if callback_metadata:
        logger.debug(f"Evaluate is called with callback metadata: {callback_metadata}")

    tqdm.tqdm._instances.clear()

    executor = ParallelExecutor(
        num_threads=num_threads,
        disable_progress_bar=not display_progress,
        max_errors=(self.max_errors if self.max_errors is not None else dspy.settings.max_errors),
        provide_traceback=self.provide_traceback,
        compare_results=True,
    )

    defprocess_item(example):
        prediction = program(**example.inputs())
        score = metric(example, prediction)
        return prediction, score

    results = executor.execute(process_item, devset)
    assert len(devset) == len(results)

    results = [((dspy.Prediction(), self.failure_score) if r is None else r) for r in results]
    results = [(example, prediction, score) for example, (prediction, score) in zip(devset, results, strict=False)]
    ncorrect, ntotal = sum(score for *_, score in results), len(devset)

    logger.info(f"Average Metric: {ncorrect} / {ntotal} ({round(100*ncorrect/ntotal,1)}%)")

    if display_table:
        if importlib.util.find_spec("pandas") is not None:
            # Rename the 'correct' column to the name of the metric object
            metric_name = metric.__name__ if isinstance(metric, types.FunctionType) else metric.__class__.__name__
            # Construct a pandas DataFrame from the results
            result_df = self._construct_result_table(results, metric_name)

            self._display_result_table(result_df, display_table, metric_name)
        else:
            logger.warning("Skipping table display since `pandas` is not installed.")

    if save_as_csv:
        metric_name = (
            metric.__name__
            if isinstance(metric, types.FunctionType)
            else metric.__class__.__name__
        )
        data = self._prepare_results_output(results, metric_name)

        with open(save_as_csv, "w", newline="") as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)
    if save_as_json:
        metric_name = (
            metric.__name__
            if isinstance(metric, types.FunctionType)
            else metric.__class__.__name__
        )
        data = self._prepare_results_output(results, metric_name)
        with open(
                save_as_json,
                "w",
        ) as f:
            json.dump(data, f)

    return EvaluationResult(
        score=round(100 * ncorrect / ntotal, 2),
        results=results,
    )
```