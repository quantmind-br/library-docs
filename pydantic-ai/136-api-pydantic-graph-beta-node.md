---
title: pydantic_graph.beta.node - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_graph/beta_node/
source: sitemap
fetched_at: 2026-01-22T22:24:58.866871231-03:00
rendered_js: false
word_count: 236
summary: This document defines the fundamental node types for constructing and executing graphs, including entry points, terminal nodes, and fork nodes for parallel execution.
tags:
    - pydantic-graph
    - node-types
    - graph-execution
    - parallel-execution
    - data-flow
    - python-typing
category: api
---

Core node types for graph construction and execution.

This module defines the fundamental node types used to build execution graphs, including start/end nodes and fork nodes for parallel execution.

### StateT `module-attribute`

```
StateT = TypeVar('StateT', infer_variance=True)
```

Type variable for graph state.

### OutputT `module-attribute`

```
OutputT = TypeVar('OutputT', infer_variance=True)
```

Type variable for node output data.

### InputT `module-attribute`

```
InputT = TypeVar('InputT', infer_variance=True)
```

Type variable for node input data.

### StartNode

Bases: `Generic[OutputT]`

Entry point node for graph execution.

The StartNode represents the beginning of a graph execution flow.

Source code in `pydantic_graph/pydantic_graph/beta/node.py`

```
classStartNode(Generic[OutputT]):
"""Entry point node for graph execution.

    The StartNode represents the beginning of a graph execution flow.
    """

    id = NodeID('__start__')
"""Fixed identifier for the start node."""
```

#### id `class-attribute` `instance-attribute`

Fixed identifier for the start node.

### EndNode

Bases: `Generic[InputT]`

Terminal node representing the completion of graph execution.

The EndNode marks the successful completion of a graph execution flow and can collect the final output data.

Source code in `pydantic_graph/pydantic_graph/beta/node.py`

```
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
```

```
classEndNode(Generic[InputT]):
"""Terminal node representing the completion of graph execution.

    The EndNode marks the successful completion of a graph execution flow
    and can collect the final output data.
    """

    id = NodeID('__end__')
"""Fixed identifier for the end node."""

    def_force_variance(self, inputs: InputT) -> None:  # pragma: no cover
"""Force type variance for proper generic typing.

        This method exists solely for type checking purposes and should never be called.

        Args:
            inputs: Input data of type InputT.

        Raises:
            RuntimeError: Always, as this method should never be executed.
        """
        raise RuntimeError('This method should never be called, it is just defined for typing purposes.')
```

#### id `class-attribute` `instance-attribute`

Fixed identifier for the end node.

### Fork `dataclass`

Bases: `Generic[InputT, OutputT]`

Fork node that creates parallel execution branches.

A Fork node splits the execution flow into multiple parallel branches, enabling concurrent execution of downstream nodes. It can either map a sequence across multiple branches or duplicate data to each branch.

Source code in `pydantic_graph/pydantic_graph/beta/node.py`

```
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
```

```
@dataclass
classFork(Generic[InputT, OutputT]):
"""Fork node that creates parallel execution branches.

    A Fork node splits the execution flow into multiple parallel branches,
    enabling concurrent execution of downstream nodes. It can either map
    a sequence across multiple branches or duplicate data to each branch.
    """

    id: ForkID
"""Unique identifier for this fork node."""

    is_map: bool
"""Determines fork behavior.

    If True, InputT must be Sequence[OutputT] and each element is sent to a separate branch.
    If False, InputT must be OutputT and the same data is sent to all branches.
    """
    downstream_join_id: JoinID | None
"""Optional identifier of a downstream join node that should be jumped to if mapping an empty iterable."""

    def_force_variance(self, inputs: InputT) -> OutputT:  # pragma: no cover
"""Force type variance for proper generic typing.

        This method exists solely for type checking purposes and should never be called.

        Args:
            inputs: Input data to be forked.

        Returns:
            Output data type (never actually returned).

        Raises:
            RuntimeError: Always, as this method should never be executed.
        """
        raise RuntimeError('This method should never be called, it is just defined for typing purposes.')
```

#### id `instance-attribute`

Unique identifier for this fork node.

#### is\_map `instance-attribute`

Determines fork behavior.

If True, InputT must be Sequence\[OutputT] and each element is sent to a separate branch. If False, InputT must be OutputT and the same data is sent to all branches.

#### downstream\_join\_id `instance-attribute`

```
downstream_join_id: JoinID | None
```

Optional identifier of a downstream join node that should be jumped to if mapping an empty iterable.