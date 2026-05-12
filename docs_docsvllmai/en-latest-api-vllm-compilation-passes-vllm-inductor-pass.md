---
title: vllm_inductor_pass - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/vllm_inductor_pass/
source: sitemap
fetched_at: 2026-05-07T21:16:48.19992838-03:00
rendered_js: false
word_count: 329
summary: This document defines the base classes VllmInductorPass, VllmPatternMatcherPass, and VllmFusionPatternMatcherPass, which provide infrastructure for pattern matching, logging, and debugging within the vLLM compilation framework.
tags:
    - vllm
    - compilation
    - pattern-matching
    - inductor
    - fx-graph
    - optimization
category: reference
---

## VllmFusionPatternMatcherPass [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass "Permanent link")

Bases: `VllmPatternMatcherPass`

A VllmPatternMatcherPass for passes that use VllmPatternReplacement objects. Subclasses register patterns via self.register() in their own **init**.

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
classVllmFusionPatternMatcherPass(VllmPatternMatcherPass):
"""
    A VllmPatternMatcherPass for passes that use VllmPatternReplacement objects.
    Subclasses register patterns via self.register() in their own __init__.
    """

    def__init__(self, config: VllmConfig, pass_name: str) -> None:
        super().__init__(config)
        self.pass_name = pass_name
        self.pm_pass = PatternMatcherPass(pass_name=pass_name)
        self._pattern_replacements: list[VllmPatternReplacement] = []

    @enable_fake_mode
    defregister(self, pr: VllmPatternReplacement) -> None:
        pm.register_replacement(
            pr.pattern,
            pr.replacement,
            pr.get_inputs(),
            self._trace_fn,
            self.pm_pass,
        )
        self._pattern_replacements.append(pr)

    defuuid(self) -> str:
        return VllmInductorPass.hash_source(
            type(self),
            *[type(pr) for pr in self._pattern_replacements],
        )

    @staticmethod
    def_trace_fn(*args: Any, **kwargs: Any) -> fx.GraphModule:
        gm = pm.fwd_only(*args, **kwargs)
        _fx_view_to_reshape(gm)
        _remove_noop_permutes(gm)
        return gm

    @VllmInductorPass.time_and_log
    def__call__(self, graph: torch.fx.Graph) -> None:
        self.matched_count = self.pm_pass.apply(graph)
        VllmPatternMatcherPass.match_table[self.pass_name] += self.matched_count
```

## VllmInductorPass [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass "Permanent link")

Bases: `InductorPass`

An inductor pass with access to vLLM PassConfig. It provides timing, logging, and dumping utilities.

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
classVllmInductorPass(InductorPass):
"""
    An inductor pass with access to vLLM PassConfig.
    It provides timing, logging, and dumping utilities.
    """

    dump_prefix: ClassVar[int | None] = None
"""Keep track of pass index for debug dump ordering."""

    def__init__(self, config: VllmConfig):
        # Get only the necessary CompilationConfig for the inductor pass, since
        # full `CompilationConfig` contains pointer to model which is unsafe.
        self.compilation_config = InductorCompilationConfig(
            splitting_ops=config.compilation_config.splitting_ops,
            use_inductor_graph_partition=config.compilation_config.use_inductor_graph_partition,
        )
        self.pass_config = config.compilation_config.pass_config
        self.model_dtype = config.model_config.dtype if config.model_config else None
        self.device: str | None = (
            config.device_config.device if config.device_config else None
        )
        self.pass_name = self.__class__.__name__

    @staticmethod
    deftime_and_log(
        call_fn: Callable[["VllmInductorPass", torch.fx.Graph], None],
    ) -> Callable[["VllmInductorPass", torch.fx.Graph], None]:
        @functools.wraps(call_fn)
        defwrapped(self: VllmInductorPass, graph: torch.fx.Graph) -> None:
            self.begin()
            self.dump_graph(graph, "before")
            call_fn(self, graph)
            self.dump_graph(graph, "after")
            self.end_and_log()

        return wrapped

    defdump_graph(self, graph: torch.fx.Graph, stage: str) -> None:
        i = VllmInductorPass.dump_prefix
        i_str = "" if i is None else f".{i}"
        lazy_format_graph_code(
            f"post_grad{i_str}.{self.pass_name}.{stage}", graph.owning_module
        )

    defbegin(self) -> None:
        self._start_time = time.perf_counter_ns()

    defend_and_log(self) -> None:
        self._end_time = time.perf_counter_ns()
        duration_ms = float(self._end_time - self._start_time) / 1.0e6
        logger.debug("%s completed in %.1f ms", self.pass_name, duration_ms)
```

### dump\_prefix `class-attribute` [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass.dump_prefix "Permanent link")

```
dump_prefix: int | None = None
```

Keep track of pass index for debug dump ordering.

## VllmPatternMatcherPass [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass "Permanent link")

Bases: `VllmInductorPass`

A VllmInductorPass that uses the Inductor pattern matcher. Provides pattern registration with match counting, debug dumping, and logging.

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
classVllmPatternMatcherPass(VllmInductorPass):
"""
    A VllmInductorPass that uses the Inductor pattern matcher.
    Provides pattern registration with match counting, debug dumping, and logging.
    """

    matched_count: int = 0
"""The number of matched patterns in the pass."""

    match_table: ClassVar[defaultdict[str, int]] = defaultdict(int)
"""Global table mapping pass name to its total match count."""

    _OP_OVERLOAD_PATTERN: ClassVar[re.Pattern] = re.compile(
        r"<OpOverload\(op='([^']*)', overload='([^']*)'\)>"
    )

    def_replace_op_overloads(self, string: str) -> str:
"""Replace <OpOverload(..., ...)> with nicer formulations"""
        return str(
            self._OP_OVERLOAD_PATTERN.sub(
                lambda m: f"torch.ops.{m.group(1)}.{m.group(2)}",
                string,
            )
        )

    @classmethod
    deflog_match_summary(cls) -> None:
        if cls.match_table:
            logger.debug("fusion pass matches: %s", dict(cls.match_table))

    defdump_patterns(self, config: VllmConfig, pm_pass: PatternMatcherPass) -> None:
"""
        If debug dumping is enabled, dump the Inductor pattern-matcher patterns
        into the debug_dump_path folder next to the dumped fx graphs.

        This method does its best to print something that looks like Python code
        for easier debugging and potentially navigation. If any errors appear in
        the output, please add to this method.

        TODO(luka): use pattern object to manually produce pattern graph
        """
        debug_dump_path = config.compile_debug_dump_path()
        if not debug_dump_path:
            return

        debug_dump_path.mkdir(parents=True, exist_ok=True)

        fromvllm.utils.system_utilsimport unique_filepath

        file_path = unique_filepath(
            lambda i: debug_dump_path / f"patterns.{self.pass_name}.{i}.py"
        )

        with file_path.open("w") as f:
            print(
                f"# This file was produced by VllmPatternMatcherPass."
                f"dump_patterns for {self.pass_name}.\n"
                f"# It does its best to produce valid-Python-looking code but"
                f" please add to dump_patterns if there are any errors.\n\n"
                f"from torch._higher_order_ops.auto_functionalize import "
                f"auto_functionalized as auto_functionalized\n"
                f"from torch._inductor.pattern_matcher import *\n"
                f"vllm = torch.ops.vllm",
                "vllm_ir = torch.ops.vllm_ir",
                file=f,
            )

            for node, patterns in pm_pass.patterns.items():
                # fix the operator.getitem repr
                if node[1] == operator.getitem:
                    node_repr = f"({repr(node[0])}, operator.getitem)"
                else:
                    node_repr = repr(node)

                node_repr = self._replace_op_overloads(node_repr)

                print(f"\n\n# Patterns for op: {node_repr}", file=f)
                for i, pattern in enumerate(patterns):
                    # reserve auto_functionalized ahead of time
                    pp = PatternPrettyPrinter()
                    pp.namespace.create_name("auto_functionalized", None)

                    # Assemble pattern
                    out_node = pp.pretty_print(pattern.pattern)
                    pattern_repr = "\n".join(
                        [f"def pattern_{i}():"]
                        + [
                            f"{pp.memoized_objs_names[key]} = "
                            f"{pp.memoized_objs_pp[key]}"
                            for key in pp.memoized_objs_names
                        ]
                        + [f"return {out_node}"]
                    ).replace("\n", "\n    ")

                    pattern_repr = self._replace_op_overloads(pattern_repr)
                    print(f"{pattern_repr}\n", file=f)
```

### match\_table `class-attribute` [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.match_table "Permanent link")

Global table mapping pass name to its total match count.

### matched\_count `class-attribute` `instance-attribute` [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.matched_count "Permanent link")

The number of matched patterns in the pass.

### \_replace\_op\_overloads [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass._replace_op_overloads "Permanent link")

```
_replace_op_overloads(string: str) -> str
```

Replace with nicer formulations

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
def_replace_op_overloads(self, string: str) -> str:
"""Replace <OpOverload(..., ...)> with nicer formulations"""
    return str(
        self._OP_OVERLOAD_PATTERN.sub(
            lambda m: f"torch.ops.{m.group(1)}.{m.group(2)}",
            string,
        )
    )
```

### dump\_patterns [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.dump_patterns "Permanent link")

```
dump_patterns(
    config: VllmConfig, pm_pass: PatternMatcherPass
) -> None
```

If debug dumping is enabled, dump the Inductor pattern-matcher patterns into the debug\_dump\_path folder next to the dumped fx graphs.

This method does its best to print something that looks like Python code for easier debugging and potentially navigation. If any errors appear in the output, please add to this method.

TODO(luka): use pattern object to manually produce pattern graph

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
defdump_patterns(self, config: VllmConfig, pm_pass: PatternMatcherPass) -> None:
"""
    If debug dumping is enabled, dump the Inductor pattern-matcher patterns
    into the debug_dump_path folder next to the dumped fx graphs.

    This method does its best to print something that looks like Python code
    for easier debugging and potentially navigation. If any errors appear in
    the output, please add to this method.

    TODO(luka): use pattern object to manually produce pattern graph
    """
    debug_dump_path = config.compile_debug_dump_path()
    if not debug_dump_path:
        return

    debug_dump_path.mkdir(parents=True, exist_ok=True)

    fromvllm.utils.system_utilsimport unique_filepath

    file_path = unique_filepath(
        lambda i: debug_dump_path / f"patterns.{self.pass_name}.{i}.py"
    )

    with file_path.open("w") as f:
        print(
            f"# This file was produced by VllmPatternMatcherPass."
            f"dump_patterns for {self.pass_name}.\n"
            f"# It does its best to produce valid-Python-looking code but"
            f" please add to dump_patterns if there are any errors.\n\n"
            f"from torch._higher_order_ops.auto_functionalize import "
            f"auto_functionalized as auto_functionalized\n"
            f"from torch._inductor.pattern_matcher import *\n"
            f"vllm = torch.ops.vllm",
            "vllm_ir = torch.ops.vllm_ir",
            file=f,
        )

        for node, patterns in pm_pass.patterns.items():
            # fix the operator.getitem repr
            if node[1] == operator.getitem:
                node_repr = f"({repr(node[0])}, operator.getitem)"
            else:
                node_repr = repr(node)

            node_repr = self._replace_op_overloads(node_repr)

            print(f"\n\n# Patterns for op: {node_repr}", file=f)
            for i, pattern in enumerate(patterns):
                # reserve auto_functionalized ahead of time
                pp = PatternPrettyPrinter()
                pp.namespace.create_name("auto_functionalized", None)

                # Assemble pattern
                out_node = pp.pretty_print(pattern.pattern)
                pattern_repr = "\n".join(
                    [f"def pattern_{i}():"]
                    + [
                        f"{pp.memoized_objs_names[key]} = "
                        f"{pp.memoized_objs_pp[key]}"
                        for key in pp.memoized_objs_names
                    ]
                    + [f"return {out_node}"]
                ).replace("\n", "\n    ")

                pattern_repr = self._replace_op_overloads(pattern_repr)
                print(f"{pattern_repr}\n", file=f)
```

## VllmPatternReplacement [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement "Permanent link")

Bases: `ABC`, `Generic[P, R]`

A pattern/replacement pair for FX graph fusion.

Implement the three abstract members below, then pass instances to VllmFusionPatternMatcherPass.register(). The pass will find every occurrence of `pattern` in the graph and substitute it with `replacement`.

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
classVllmPatternReplacement(ABC, Generic[P, R]):
"""
    A pattern/replacement pair for FX graph fusion.

    Implement the three abstract members below, then pass
    instances to VllmFusionPatternMatcherPass.register(). The pass will
    find every occurrence of `pattern` in the graph and substitute it
    with `replacement`.
    """

    # TODO(Badr): bound methods work for pattern registration since
    # PyTorch 2.10. Once vLLM requires torch>=2.11, replace these properties
    # with plain methods and drop the closure indirection.
    @property
    @abstractmethod
    defpattern(self) -> Callable[P, R]:
"""Returns a closure defining the FX subgraph to search for."""
        ...

    @property
    @abstractmethod
    defreplacement(self) -> Callable[P, R]:
"""
        Returns a closure defining the FX subgraph to
        substitute in place of each match.
        """
        ...

    @abstractmethod
    defget_inputs(self) -> list[torch.Tensor]:
"""Example tensors used to trace pattern and replacement."""
        ...

    # Helpers for get_inputs: uninitialized tensors of common dtypes.
    @staticmethod
    defempty(*args, **kwargs) -> torch.Tensor:
        return torch.empty(*args, device="cuda", **kwargs)

    @staticmethod
    defempty_bf16(*args, **kwargs) -> torch.Tensor:
        return torch.empty(*args, dtype=torch.bfloat16, device="cuda", **kwargs)

    @staticmethod
    defempty_fp16(*args, **kwargs) -> torch.Tensor:
        return torch.empty(*args, dtype=torch.float16, device="cuda", **kwargs)

    @staticmethod
    defempty_fp32(*args, **kwargs) -> torch.Tensor:
        return torch.empty(*args, dtype=torch.float32, device="cuda", **kwargs)

    @staticmethod
    defempty_i32(*args, **kwargs) -> torch.Tensor:
        return torch.empty(*args, dtype=torch.int32, device="cuda", **kwargs)
```

### pattern `abstractmethod` `property` [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement.pattern "Permanent link")

Returns a closure defining the FX subgraph to search for.

### replacement `abstractmethod` `property` [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement.replacement "Permanent link")

Returns a closure defining the FX subgraph to substitute in place of each match.

### get\_inputs `abstractmethod` [¶](#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement.get_inputs "Permanent link")

Example tensors used to trace pattern and replacement.

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
@abstractmethod
defget_inputs(self) -> list[torch.Tensor]:
"""Example tensors used to trace pattern and replacement."""
    ...
```

## get\_match\_table [¶](#vllm.compilation.passes.vllm_inductor_pass.get_match_table "Permanent link")

Return a snapshot of the match table.

Source code in `vllm/compilation/passes/vllm_inductor_pass.py`

```
defget_match_table() -> dict[str, int]:
"""Return a snapshot of the match table."""
    return dict(VllmPatternMatcherPass.match_table)
```