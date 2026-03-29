---
title: pydantic_graph.nodes - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_graph/nodes/
source: sitemap
fetched_at: 2026-01-22T22:25:04.972585218-03:00
rendered_js: false
word_count: 478
summary: This document defines the core API components for pydantic-graph, specifically the BaseNode abstract class and the GraphRunContext used to manage state and dependencies during graph execution.
tags:
    - pydantic-graph
    - python
    - graph-execution
    - api-reference
    - state-management
    - async-programming
category: api
---

### StateT `module-attribute`

```
StateT = TypeVar('StateT', default=None)
```

Type variable for the state in a graph.

### GraphRunContext `dataclass`

Bases: `Generic[StateT, DepsT]`

Context for a graph.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
@dataclass(kw_only=True)
classGraphRunContext(Generic[StateT, DepsT]):
"""Context for a graph."""

    state: StateT
"""The state of the graph."""
    deps: DepsT
"""Dependencies for the graph."""
```

#### state `instance-attribute`

The state of the graph.

#### deps `instance-attribute`

Dependencies for the graph.

### BaseNode

Bases: `ABC`, `Generic[StateT, DepsT, NodeRunEndT]`

Base class for a node.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
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
```

```
classBaseNode(ABC, Generic[StateT, DepsT, NodeRunEndT]):
"""Base class for a node."""

    docstring_notes: ClassVar[bool] = False
"""Set to `True` to generate mermaid diagram notes from the class's docstring.

    While this can add valuable information to the diagram, it can make diagrams harder to view, hence
    it is disabled by default. You can also customise notes overriding the
    [`get_note`][pydantic_graph.nodes.BaseNode.get_note] method.
    """

    @abstractmethod
    async defrun(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]:
"""Run the node.

        This is an abstract method that must be implemented by subclasses.

        !!! note "Return types used at runtime"
            The return type of this method are read by `pydantic_graph` at runtime and used to define which
            nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
            and enforced when running the graph.

        Args:
            ctx: The graph context.

        Returns:
            The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.
        """
        ...

    defget_snapshot_id(self) -> str:
        if snapshot_id := getattr(self, '__snapshot_id', None):
            return snapshot_id
        else:
            self.__dict__['__snapshot_id'] = snapshot_id = generate_snapshot_id(self.get_node_id())
            return snapshot_id

    defset_snapshot_id(self, snapshot_id: str) -> None:
        self.__dict__['__snapshot_id'] = snapshot_id

    @classmethod
    @cache
    defget_node_id(cls) -> str:
"""Get the ID of the node."""
        return cls.__name__

    @classmethod
    defget_note(cls) -> str | None:
"""Get a note about the node to render on mermaid charts.

        By default, this returns a note only if [`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]
        is `True`. You can override this method to customise the node notes.
        """
        if not cls.docstring_notes:
            return None
        docstring = cls.__doc__
        # dataclasses get an automatic docstring which is just their signature, we don't want that
        if docstring and is_dataclass(cls) and docstring.startswith(f'{cls.__name__}('):
            docstring = None  # pragma: no cover
        if docstring:  # pragma: no branch
            # remove indentation from docstring
            importinspect

            docstring = inspect.cleandoc(docstring)
        return docstring

    @classmethod
    defget_node_def(cls, local_ns: dict[str, Any] | None) -> NodeDef[StateT, DepsT, NodeRunEndT]:
"""Get the node definition."""
        type_hints = get_type_hints(cls.run, localns=local_ns, include_extras=True)
        try:
            return_hint = type_hints['return']
        except KeyError as e:
            raise exceptions.GraphSetupError(f'Node {cls} is missing a return type hint on its `run` method') frome

        next_node_edges: dict[str, Edge] = {}
        end_edge: Edge | None = None
        returns_base_node: bool = False
        for return_type in _utils.get_union_args(return_hint):
            return_type, annotations = _utils.unpack_annotated(return_type)
            edge = next((a for a in annotations if isinstance(a, Edge)), Edge(None))
            return_type_origin = get_origin(return_type) or return_type
            if return_type_origin is End:
                end_edge = edge
            elif return_type_origin is BaseNode:
                returns_base_node = True
            elif issubclass(return_type_origin, BaseNode):
                next_node_edges[return_type.get_node_id()] = edge
            else:
                raise exceptions.GraphSetupError(f'Invalid return type: {return_type}')

        return NodeDef(
            node=cls,
            node_id=cls.get_node_id(),
            note=cls.get_note(),
            next_node_edges=next_node_edges,
            end_edge=end_edge,
            returns_base_node=returns_base_node,
        )

    defdeep_copy(self) -> Self:
"""Returns a deep copy of the node."""
        return copy.deepcopy(self)
```

#### docstring\_notes `class-attribute`

```
docstring_notes: bool = False
```

Set to `True` to generate mermaid diagram notes from the class's docstring.

While this can add valuable information to the diagram, it can make diagrams harder to view, hence it is disabled by default. You can also customise notes overriding the [`get_note`](#pydantic_graph.nodes.BaseNode.get_note "get_note            classmethod   ") method.

#### run `abstractmethod` `async`

Run the node.

This is an abstract method that must be implemented by subclasses.

Return types used at runtime

The return type of this method are read by `pydantic_graph` at runtime and used to define which nodes can be called next in the graph. This is displayed in [mermaid diagrams](https://ai.pydantic.dev/api/pydantic_graph/mermaid/) and enforced when running the graph.

Parameters:

Name Type Description Default `ctx` `GraphRunContext[StateT, DepsT]`

The graph context.

*required*

Returns:

Type Description `BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]`

The next node to run or [`End`](#pydantic_graph.nodes.End "End            dataclass   ") to signal the end of the graph.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
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
```

```
@abstractmethod
async defrun(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]:
"""Run the node.

    This is an abstract method that must be implemented by subclasses.

    !!! note "Return types used at runtime"
        The return type of this method are read by `pydantic_graph` at runtime and used to define which
        nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
        and enforced when running the graph.

    Args:
        ctx: The graph context.

    Returns:
        The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.
    """
    ...
```

#### get\_node\_id `cached` `classmethod`

Get the ID of the node.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
@classmethod
@cache
defget_node_id(cls) -> str:
"""Get the ID of the node."""
    return cls.__name__
```

#### get\_note `classmethod`

Get a note about the node to render on mermaid charts.

By default, this returns a note only if [`docstring_notes`](#pydantic_graph.nodes.BaseNode.docstring_notes "docstring_notes            class-attribute   ") is `True`. You can override this method to customise the node notes.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
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
```

```
@classmethod
defget_note(cls) -> str | None:
"""Get a note about the node to render on mermaid charts.

    By default, this returns a note only if [`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]
    is `True`. You can override this method to customise the node notes.
    """
    if not cls.docstring_notes:
        return None
    docstring = cls.__doc__
    # dataclasses get an automatic docstring which is just their signature, we don't want that
    if docstring and is_dataclass(cls) and docstring.startswith(f'{cls.__name__}('):
        docstring = None  # pragma: no cover
    if docstring:  # pragma: no branch
        # remove indentation from docstring
        importinspect

        docstring = inspect.cleandoc(docstring)
    return docstring
```

#### get\_node\_def `classmethod`

```
get_node_def(
    local_ns: dict[str, Any] | None,
) -> NodeDef[StateT, DepsT, NodeRunEndT]
```

Get the node definition.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
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
```

```
@classmethod
defget_node_def(cls, local_ns: dict[str, Any] | None) -> NodeDef[StateT, DepsT, NodeRunEndT]:
"""Get the node definition."""
    type_hints = get_type_hints(cls.run, localns=local_ns, include_extras=True)
    try:
        return_hint = type_hints['return']
    except KeyError as e:
        raise exceptions.GraphSetupError(f'Node {cls} is missing a return type hint on its `run` method') frome

    next_node_edges: dict[str, Edge] = {}
    end_edge: Edge | None = None
    returns_base_node: bool = False
    for return_type in _utils.get_union_args(return_hint):
        return_type, annotations = _utils.unpack_annotated(return_type)
        edge = next((a for a in annotations if isinstance(a, Edge)), Edge(None))
        return_type_origin = get_origin(return_type) or return_type
        if return_type_origin is End:
            end_edge = edge
        elif return_type_origin is BaseNode:
            returns_base_node = True
        elif issubclass(return_type_origin, BaseNode):
            next_node_edges[return_type.get_node_id()] = edge
        else:
            raise exceptions.GraphSetupError(f'Invalid return type: {return_type}')

    return NodeDef(
        node=cls,
        node_id=cls.get_node_id(),
        note=cls.get_note(),
        next_node_edges=next_node_edges,
        end_edge=end_edge,
        returns_base_node=returns_base_node,
    )
```

#### deep\_copy

Returns a deep copy of the node.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
defdeep_copy(self) -> Self:
"""Returns a deep copy of the node."""
    return copy.deepcopy(self)
```

### End `dataclass`

Bases: `Generic[RunEndT]`

Type to return from a node to signal the end of the graph.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
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
```

```
@dataclass
classEnd(Generic[RunEndT]):
"""Type to return from a node to signal the end of the graph."""

    data: RunEndT
"""Data to return from the graph."""

    defdeep_copy_data(self) -> End[RunEndT]:
"""Returns a deep copy of the end of the run."""
        if self.data is None:
            return self
        else:
            end = End(copy.deepcopy(self.data))
            end.set_snapshot_id(self.get_snapshot_id())
            return end

    defget_snapshot_id(self) -> str:
        if snapshot_id := getattr(self, '__snapshot_id', None):
            return snapshot_id
        else:
            self.__dict__['__snapshot_id'] = snapshot_id = generate_snapshot_id('end')
            return snapshot_id

    defset_snapshot_id(self, set_id: str) -> None:
        self.__dict__['__snapshot_id'] = set_id
```

#### data `instance-attribute`

Data to return from the graph.

#### deep\_copy\_data

```
deep_copy_data() -> End[RunEndT]
```

Returns a deep copy of the end of the run.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
149
150
151
152
153
154
155
156
```

```
defdeep_copy_data(self) -> End[RunEndT]:
"""Returns a deep copy of the end of the run."""
    if self.data is None:
        return self
    else:
        end = End(copy.deepcopy(self.data))
        end.set_snapshot_id(self.get_snapshot_id())
        return end
```

### Edge `dataclass`

Annotation to apply a label to an edge in a graph.

Source code in `pydantic_graph/pydantic_graph/nodes.py`

```
@dataclass(frozen=True)
classEdge:
"""Annotation to apply a label to an edge in a graph."""

    label: str | None
"""Label for the edge."""
```

#### label `instance-attribute`

Label for the edge.

### DepsT `module-attribute`

```
DepsT = TypeVar('DepsT', default=None, contravariant=True)
```

Type variable for the dependencies of a graph and node.

### RunEndT `module-attribute`

```
RunEndT = TypeVar('RunEndT', covariant=True, default=None)
```

Covariant type variable for the return type of a graph [`run`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.run "run            async   ").

### NodeRunEndT `module-attribute`

```
NodeRunEndT = TypeVar(
    "NodeRunEndT", covariant=True, default=Never
)
```

Covariant type variable for the return type of a node [`run`](#pydantic_graph.nodes.BaseNode.run "run            abstractmethod       async   ").