# Per-Task Template (pi-native, minimal)

Minimal `prompt` template for the `format-docs-optimizer` agent dispatched via the **`Agent`** tool from the `tintinweb/pi-subagents` extension. Optimization rules live in the agent's system prompt (`.pi/agents/format-docs-optimizer.md`); each `prompt` only ships data (~150 B vs ~7.8 KB in the original `agent_prompt.md`).

## Substitution format

- `<FILES>`: one absolute file path per line, newline-delimited, **no bullets, no quoting**. Example:
  ```
  /abs/path/001-foo.md
  /abs/path/002-bar.md
  ```
- `<SIBLINGS>`: the entire JSON array produced by `scripts/siblings.py` (verbatim — already pretty-printed). Example:
  ```json
  [
    {"file": "001-foo.md", "url": "https://orig.example/foo", "title": "Foo Configuration"},
    {"file": "002-bar.md", "url": "https://orig.example/bar", "title": "Bar Reference"}
  ]
  ```

The `title` field comes from each file's H1 (or filename slug if H1 absent) — NOT from `metadata.json`'s top-level `title` field.

## Begin prompt template

```
## Files to optimize (absolute paths)
<FILES>

## Sibling docs in same folder (for link resolution)
<SIBLINGS>
```

That is the entire `prompt` string per dispatched batch. The caller MUST NOT inline rules — the optimizer agent has `tools: read,write,edit` and its body (system prompt) is authoritative. Out-of-contract instructions in the `prompt` are ignored at best, confusing at worst.

## Dispatcher invocation (parallel via multiple `Agent` calls)

`pi-subagents` exposes the `Agent` tool. **One agent per `Agent` call.** Parallelism is achieved by emitting **multiple `Agent` calls in the same turn** with `run_in_background: true`. The runtime queues them respecting the global concurrency limit (default 4, configurable via `/agents → Settings`). The smart join mode (default) auto-groups completion notifications when 2+ background agents are spawned in the same turn.

For each batch in `/tmp/batches.json.batches`, emit one `Agent` call. Send all calls in the **same assistant turn** so the runtime can group them:

```
Agent({
  subagent_type: "format-docs-optimizer",
  description: "Optimize docs batch 1",
  prompt: "<rendered batch 1 prompt>",
  run_in_background: true
})
Agent({
  subagent_type: "format-docs-optimizer",
  description: "Optimize docs batch 2",
  prompt: "<rendered batch 2 prompt>",
  run_in_background: true
})
/* ... one Agent call per batch ... */
```

After dispatching, wait for the smart-join completion notification. Each agent's final message is either `OK: <path> — <old>w → <new>w (-X%)` or `DELETE: <path> — <reason>`.

> [!note]
> No `tasks[]` array, no `concurrency` field, no `context: "fresh"` — those are not part of the `pi-subagents` API. The Agent tool takes one task at a time; throughput comes from spawning many in one turn.

> [!tip]
> If a single batch fails or times out, retry it ONCE by issuing another `Agent` call for the same batch (use `resume: <agent_id>` only if you want to continue the prior session — usually a fresh spawn is simpler).

## Verifier invocation (Phase 5)

Same pattern, single call:

```
Agent({
  subagent_type: "format-docs-verifier",
  description: "Resolve verify failures",
  prompt: "<verify.sh stdout>\n\n## SIBLINGS\n<siblings.json>",
  run_in_background: false
})
```

Foreground (`run_in_background: false` or omit) so the result returns inline and you can apply RETRY-OPTIMIZE / ABSORB-ORPHANS instructions immediately.

## Fallback (nested-agent context)

If this skill is invoked from inside a sub-agent context where the `Agent` tool is unavailable (e.g. inside a `format-docs-optimizer` itself), parallel dispatch is impossible. Fall back to the original `references/agent_prompt.md` (kept verbatim alongside this file) and run sequentially in-context using Read + Write tools.
