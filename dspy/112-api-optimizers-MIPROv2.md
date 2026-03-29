---
title: MIPROv2 - DSPy
url: https://dspy.ai/api/optimizers/MIPROv2/
source: sitemap
fetched_at: 2026-01-23T08:02:21.635478323-03:00
rendered_js: false
word_count: 0
summary: This document defines the compile method for a prompt optimizer, detailing the process of bootstrapping few-shot examples and proposing instructions to optimize a student program.
tags:
    - dspy
    - prompt-optimization
    - mipro-optimizer
    - few-shot-learning
    - machine-learning-pipelines
    - hyperparameter-tuning
category: api
---

```
defcompile(
    self,
    student: Any,
    *,
    trainset: list,
    teacher: Any = None,
    valset: list | None = None,
    num_trials: int | None = None,
    max_bootstrapped_demos: int | None = None,
    max_labeled_demos: int | None = None,
    seed: int | None = None,
    minibatch: bool = True,
    minibatch_size: int = 35,
    minibatch_full_eval_steps: int = 5,
    program_aware_proposer: bool = True,
    data_aware_proposer: bool = True,
    view_data_batch_size: int = 10,
    tip_aware_proposer: bool = True,
    fewshot_aware_proposer: bool = True,
    requires_permission_to_run: bool | None = None, # deprecated
    provide_traceback: bool | None = None,
) -> Any:
    if requires_permission_to_run == False:
        logger.warning(
            "'requires_permission_to_run' is deprecated and will be removed in a future version."
        )
    elif requires_permission_to_run == True:
        raise ValueError("User confirmation is removed from MIPROv2. Please remove the 'requires_permission_to_run' argument.")

    effective_max_errors = (
        self.max_errors
        if self.max_errors is not None
        else dspy.settings.max_errors
    )

    effective_max_bootstrapped_demos = (
        max_bootstrapped_demos if max_bootstrapped_demos is not None else self.max_bootstrapped_demos
    )
    effective_max_labeled_demos = (
        max_labeled_demos if max_labeled_demos is not None else self.max_labeled_demos
    )

    zeroshot_opt = (effective_max_bootstrapped_demos == 0) and (effective_max_labeled_demos == 0)

    # If auto is None, and num_trials is not provided (but num_candidates is), raise an error that suggests a good num_trials value
    if self.auto is None and (self.num_candidates is not None and num_trials is None):
        raise ValueError(
            f"If auto is None, num_trials must also be provided. Given num_candidates={self.num_candidates}, we'd recommend setting num_trials to ~{self._set_num_trials_from_num_candidates(student,zeroshot_opt,self.num_candidates)}."
        )

    # If auto is None, and num_candidates or num_trials is None, raise an error
    if self.auto is None and (self.num_candidates is None or num_trials is None):
        raise ValueError("If auto is None, num_candidates must also be provided.")

    # If auto is provided, and either num_candidates or num_trials is not None, raise an error
    if self.auto is not None and (self.num_candidates is not None or num_trials is not None):
        raise ValueError(
            "If auto is not None, num_candidates and num_trials cannot be set, since they would be overridden by the auto settings. Please either set auto to None, or do not specify num_candidates and num_trials."
        )

    # Set random seeds
    seed = seed or self.seed
    self._set_random_seeds(seed)


    # Set training & validation sets
    trainset, valset = self._set_and_validate_datasets(trainset, valset)

    num_instruct_candidates = (
        self.num_instruct_candidates
        if self.num_instruct_candidates is not None
        else self.num_candidates
    )
    num_fewshot_candidates = (
        self.num_fewshot_candidates
        if self.num_fewshot_candidates is not None
        else self.num_candidates
    )

    # Set hyperparameters based on run mode (if set)
    (
        num_trials,
        valset,
        minibatch,
        num_instruct_candidates,
        num_fewshot_candidates,
    ) = self._set_hyperparams_from_run_mode(
        student,
        num_trials,
        minibatch,
        zeroshot_opt,
        valset,
        num_instruct_candidates,
        num_fewshot_candidates,
    )

    if self.auto:
        self._print_auto_run_settings(
            num_trials,
            minibatch,
            valset,
            num_fewshot_candidates,
            num_instruct_candidates,
        )

    if minibatch and minibatch_size > len(valset):
        raise ValueError(f"Minibatch size cannot exceed the size of the valset. Valset size: {len(valset)}.")

    # Initialize program and evaluator
    program = student.deepcopy()
    evaluate = Evaluate(
        devset=valset,
        metric=self.metric,
        num_threads=self.num_threads,
        max_errors=effective_max_errors,
        display_table=False,
        display_progress=True,
        provide_traceback=provide_traceback,
    )

    with dspy.context(lm=self.task_model):
        # Step 1: Bootstrap few-shot examples
        demo_candidates = self._bootstrap_fewshot_examples(
            program,
            trainset,
            seed,
            teacher,
            num_fewshot_candidates=num_fewshot_candidates,
            max_bootstrapped_demos=effective_max_bootstrapped_demos,
            max_labeled_demos=effective_max_labeled_demos,
            max_errors=effective_max_errors,
            metric_threshold=self.metric_threshold,
        )

    # Step 2: Propose instruction candidates
    instruction_candidates = self._propose_instructions(
        program,
        trainset,
        demo_candidates,
        view_data_batch_size,
        program_aware_proposer,
        data_aware_proposer,
        tip_aware_proposer,
        fewshot_aware_proposer,
        num_instruct_candidates=num_instruct_candidates,
    )

    # If zero-shot, discard demos
    if zeroshot_opt:
        demo_candidates = None

    with dspy.context(lm=self.task_model):
        # Step 3: Find optimal prompt parameters
        best_program = self._optimize_prompt_parameters(
            program,
            instruction_candidates,
            demo_candidates,
            evaluate,
            valset,
            num_trials,
            minibatch,
            minibatch_size,
            minibatch_full_eval_steps,
            seed,
        )

    return best_program
```