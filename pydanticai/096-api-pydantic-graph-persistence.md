---
title: pydantic_graph.persistence - Pydantic AI
url: https://ai.pydantic.dev/api/pydantic_graph/persistence/
source: sitemap
fetched_at: 2026-01-22T22:25:04.800305915-03:00
rendered_js: false
word_count: 45
summary: This document defines the FileStatePersistence class for storing and managing graph run states and node snapshots in JSON files. It provides mechanisms for state serialization, execution recording, and file-based locking to ensure data integrity during concurrent access.
tags:
    - pydantic-graph
    - state-persistence
    - file-storage
    - json-serialization
    - snapshot-management
    - concurrency-control
category: reference
---

```
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
```

````
@dataclass
classFileStatePersistence(BaseStatePersistence[StateT, RunEndT]):
"""File based state persistence that hold graph run state in a JSON file."""

    json_file: Path
"""Path to the JSON file where the snapshots are stored.

    You should use a different file for each graph run, but a single file should be reused for multiple
    steps of the same run.

    For example if you have a run ID of the form `run_123abc`, you might create a `FileStatePersistence` thus:

    ```py
    from pathlib import Path

    from pydantic_graph import FullStatePersistence

    run_id = 'run_123abc'
    persistence = FullStatePersistence(Path('runs') / f'{run_id}.json')
    ```
    """
    _snapshots_type_adapter: pydantic.TypeAdapter[list[Snapshot[StateT, RunEndT]]] | None = field(
        default=None, init=False, repr=False
    )

    async defsnapshot_node(self, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]) -> None:
        await self._append_save(NodeSnapshot(state=state, node=next_node))

    async defsnapshot_node_if_new(
        self, snapshot_id: str, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]
    ) -> None:
        async with self._lock():
            snapshots = await self.load_all()
            if not any(s.id == snapshot_id for s in snapshots):  # pragma: no branch
                await self._append_save(NodeSnapshot(state=state, node=next_node), lock=False)

    async defsnapshot_end(self, state: StateT, end: End[RunEndT]) -> None:
        await self._append_save(EndSnapshot(state=state, result=end))

    @asynccontextmanager
    async defrecord_run(self, snapshot_id: str) -> AsyncIterator[None]:
        async with self._lock():
            snapshots = await self.load_all()
            try:
                snapshot = next(s for s in snapshots if s.id == snapshot_id)
            except StopIteration as e:
                raise LookupError(f'No snapshot found with id={snapshot_id!r}') frome

            assert isinstance(snapshot, NodeSnapshot), 'Only NodeSnapshot can be recorded'
            exceptions.GraphNodeStatusError.check(snapshot.status)
            snapshot.status = 'running'
            snapshot.start_ts = _utils.now_utc()
            await self._save(snapshots)

        start = perf_counter()
        try:
            yield
        except Exception:
            duration = perf_counter() - start
            async with self._lock():
                await _graph_utils.run_in_executor(self._after_run_sync, snapshot_id, duration, 'error')
            raise
        else:
            snapshot.duration = perf_counter() - start
            async with self._lock():
                await _graph_utils.run_in_executor(self._after_run_sync, snapshot_id, snapshot.duration, 'success')

    async defload_next(self) -> NodeSnapshot[StateT, RunEndT] | None:
        async with self._lock():
            snapshots = await self.load_all()
            if snapshot := next((s for s in snapshots if isinstance(s, NodeSnapshot) and s.status == 'created'), None):
                snapshot.status = 'pending'
                await self._save(snapshots)
                return snapshot

    defshould_set_types(self) -> bool:
"""Whether types need to be set."""
        return self._snapshots_type_adapter is None

    defset_types(self, state_type: type[StateT], run_end_type: type[RunEndT]) -> None:
        self._snapshots_type_adapter = build_snapshot_list_type_adapter(state_type, run_end_type)

    async defload_all(self) -> list[Snapshot[StateT, RunEndT]]:
        return await _graph_utils.run_in_executor(self._load_sync)

    def_load_sync(self) -> list[Snapshot[StateT, RunEndT]]:
        assert self._snapshots_type_adapter is not None, 'snapshots type adapter must be set'
        try:
            content = self.json_file.read_bytes()
        except FileNotFoundError:
            return []
        else:
            return self._snapshots_type_adapter.validate_json(content)

    def_after_run_sync(self, snapshot_id: str, duration: float, status: SnapshotStatus) -> None:
        snapshots = self._load_sync()
        snapshot = next(s for s in snapshots if s.id == snapshot_id)
        assert isinstance(snapshot, NodeSnapshot), 'Only NodeSnapshot can be recorded'
        snapshot.duration = duration
        snapshot.status = status
        self._save_sync(snapshots)

    async def_save(self, snapshots: list[Snapshot[StateT, RunEndT]]) -> None:
        await _graph_utils.run_in_executor(self._save_sync, snapshots)

    def_save_sync(self, snapshots: list[Snapshot[StateT, RunEndT]]) -> None:
        assert self._snapshots_type_adapter is not None, 'snapshots type adapter must be set'
        self.json_file.write_bytes(self._snapshots_type_adapter.dump_json(snapshots, indent=2))

    async def_append_save(self, snapshot: Snapshot[StateT, RunEndT], *, lock: bool = True) -> None:
        assert self._snapshots_type_adapter is not None, 'snapshots type adapter must be set'
        async with AsyncExitStack() as stack:
            if lock:
                await stack.enter_async_context(self._lock())
            snapshots = await self.load_all()
            snapshots.append(snapshot)
            await self._save(snapshots)

    @asynccontextmanager
    async def_lock(self, *, timeout: float = 1.0) -> AsyncIterator[None]:
"""Lock a file by checking and writing a `.pydantic-graph-persistence-lock` to it.

        Args:
            timeout: how long to wait for the lock

        Returns: an async context manager that holds the lock
        """
        lock_file = self.json_file.parent / f'{self.json_file.name}.pydantic-graph-persistence-lock'
        lock_id = secrets.token_urlsafe().encode()

        with anyio.fail_after(timeout):
            while not await _file_append_check(lock_file, lock_id):
                await anyio.sleep(0.01)

        try:
            yield
        finally:
            await _graph_utils.run_in_executor(lock_file.unlink, missing_ok=True)
````