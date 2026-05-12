---
name: format-docs-pi-skill
description: Optimize markdown docs in a folder for AI agent consumption — Obsidian-flavored markdown, token-dense rewrite, parallel sub-agent dispatch via the pi-native `Agent` tool (tintinweb/pi-subagents extension), 100% content-integrity preserved. Use this skill whenever the user asks to format, optimize, compress, densify, AI-optimize, or rewrite a documentation folder previously produced by `repodocs-go` or the `organize-docs-skill` (folder containing `metadata.json` + numbered `nnn-*.md` files + `000-index.md`). Trigger on phrases like "format docs", "optimize docs for AI", "compress these docs", "obsidian format", "token dense", "format-docs", "ai-friendly docs", "library-docs format", "rewrite docs for agents", or any equivalent rewrite-for-density request. Runs AFTER `organize-docs-skill`. Requires the `pi-subagents` extension and the `format-docs-optimizer` + `format-docs-verifier` custom agents in `.pi/agents/`.
---

# Format Docs for AI Consumption

Rewrite every markdown file in the target folder for AI/LLM agent reading. Information density goes UP, token waste goes DOWN, **content integrity stays 100%** — no facts, code, parameters, examples, or edge cases may be removed. Output is Obsidian-flavored markdown.

## Hard rules (non-negotiable)

1. **Zero content loss.** Rewrite for density, never delete substance. Every fact, parameter, type, example, error code, version note, link, and code block must survive. If unsure → keep verbatim.
2. **Obsidian markdown only** for output (callouts, wikilinks, frontmatter). Rules in `references/agent_prompt.md`.
3. **Parallel sub-agents** for the optimization phase. Batch files, dispatch concurrently by emitting multiple `Agent` calls with `run_in_background: true` in the same turn (the `pi-subagents` runtime queues and joins them).
4. **Empty / unusable files** → delete + remove from `metadata.json` + remove from `000-index.md`. Never keep placeholders.
5. **Idempotent.** Re-running on an already-optimized folder must be a no-op (detect via `optimized: true` in frontmatter; `plan_batches.py` already filters those out).
6. **Never** touch `000-index.md` or `metadata.json` during the parallel rewrite phase. Update them sequentially in Phase 3 and Phase 4.

## Why a skill instead of inline reasoning

Triage, batching, metadata sync, index regeneration, and verification are deterministic and benefit from being scripted — scripts are faster, reproducible, and remove a class of arithmetic / typo errors. The semantic decisions (per-file rewriting, link resolution, ambiguous DELETE calls) live with the per-file Agent and with you. The split between "scripts do this, agents decide that" is what makes the workflow predictable.

## Bundled scripts

All scripts live next to this `SKILL.md` under `scripts/`. JSON-on-stdout for easy piping.

| Script | Phase | Purpose |
|--------|-------|---------|
| `setup.sh <dir>` | 0 | Validate folder + `metadata.json`. Print absolute path. |
| `inventory.py <dir> [--absorb-orphans]` | 0 | List `*.md` (root only), find orphans, detect already-optimized. |
| `triage.py <dir> [--apply]` | 1 | Duplicate-index + empty/unusable detection. Default dry-run. |
| `siblings.py <dir>` | 2 prep | Emit `<SIBLINGS>` JSON for agent prompt injection (title from H1). |
| `plan_batches.py <dir>` | 2 prep | Build size-bucketed batches (≤4 KB → 9, 4-15 KB → 5, 15-50 KB → 2, >50 KB → solo). |
| `apply_agent_results.py <dir>` | 2 post | Parse agent reports from stdin, apply `DELETE:` lines. |
| `sync_metadata.py <dir>` | 3 | Re-read frontmatter, sync `documents[]`, write `optimization{}` block. |
| `recalc_word_count.py <dir>` | 3a | Recompute body word count for each `nnn-*.md`, rewrite `word_count:` in frontmatter, sync `metadata.json[*].word_count`. Idempotent. |
| `regenerate_index.py <dir>` | 4 | Rebuild compact `000-index.md` (3-column table: # \| File \| Title). Strips site-name suffix from titles. |
| `verify.sh <dir>` | 5 | 5-check audit: counts, missing, orphans, optimized flag, broken wikilinks. |

`$SKILL_DIR` is the directory containing this `SKILL.md`. Resolve once at session start so subsequent commands stay readable.

## Workflow

### Phase 0 — Setup & Inventory

```bash
TARGET="$("$SKILL_DIR/scripts/setup.sh" "$1")"
"$SKILL_DIR/scripts/inventory.py" "$TARGET" --absorb-orphans > /tmp/inv.json
jq '{orphans: .orphans, absorbed: .absorbed_orphans, already: (.already_optimized|length), pending: (.pending|length)}' /tmp/inv.json
```

`setup.sh` aborts the whole run if `metadata.json` is missing (tell the user to run `organize-docs-skill` first), invalid JSON, or the folder doesn't exist. `inventory.py --absorb-orphans` adds stub `documents[]` entries for `.md` files on disk that weren't in metadata, so they join the normal flow downstream.

If `pending == 0` and `orphans == 0`: report "already optimized, nothing to do" and exit. Idempotency win.

### Phase 1 — Triage empty / unusable / duplicate-index

```bash
"$SKILL_DIR/scripts/triage.py" "$TARGET" --apply > /tmp/triage.json
jq '.' /tmp/triage.json
```

The script handles both:

- **1a — duplicate-index**: any non-numbered file whose role duplicates `000-index.md` (filename like `index.md` / `README.md` / `TOC.md` / `contents.md` / `catalog.md` / `summary.md` / `overview.md`, or body dominated by links to numbered siblings). Numbered `nnn-*.md` files are NEVER triaged here — they're deliberate output of `organize-docs-skill`; if a numbered file looks index-like, the optimization pass compresses it instead.
- **1b — empty/unusable**: <30 words with no code/tables/links, pointer-only stubs, error/404 pages.

Deletions are recorded in `metadata.optimization.deleted_files[]` (accumulator that survives across re-runs).

### Phase 2 — Parallel optimization (subagents)

This is where the bulk of the work happens. Sequence:

```bash
"$SKILL_DIR/scripts/siblings.py" "$TARGET" > /tmp/siblings.json
"$SKILL_DIR/scripts/plan_batches.py" "$TARGET" > /tmp/batches.json
jq '{total_pending, batch_count}' /tmp/batches.json
```

Then:

1. Read `references/agent_prompt_pi.md`. That is the **minimal per-task template** with `<FILES>` and `<SIBLINGS>` placeholders. Optimization rules already live in the `format-docs-optimizer` agent's system prompt (`.pi/agents/format-docs-optimizer.md`); each prompt only ships data (~150 B vs ~7.8 KB before).
2. For each batch in `/tmp/batches.json.batches`, build the per-batch prompt string:
   - `<FILES>` = newline-delimited absolute paths from the batch (no bullets, no quoting).
   - `<SIBLINGS>` = the entire `/tmp/siblings.json` body (a JSON array — inject verbatim).
3. **Dispatch via parallel `Agent` calls** — `pi-subagents` exposes the `Agent` tool with **one agent per call**. Throughput comes from emitting **multiple `Agent` calls in the same assistant turn** with `run_in_background: true`; the runtime queues them respecting the global concurrency limit (default 4, configurable via `/agents → Settings`) and the default smart-join groups completion notifications:
   ```
   Agent({
     subagent_type: "format-docs-optimizer",
     description: "Optimize docs batch 1",
     prompt: "<batch 1 rendered prompt>",
     run_in_background: true
   })
   Agent({
     subagent_type: "format-docs-optimizer",
     description: "Optimize docs batch 2",
     prompt: "<batch 2 rendered prompt>",
     run_in_background: true
   })
   /* ... one Agent call per batch, all in the same turn ... */
   ```
   No `tasks[]` array, no `concurrency` parameter, no per-call cap — the runtime owns queueing. For very large batch counts, splitting across 2–3 turns is fine, but a single turn is preferred so smart-join consolidates the completion notifications.
4. Collect every agent result via the smart-join notification (or `get_subagent_result(agent_id)` if you need a specific one). Each agent's final message is either `OK: <path> — <old>w → <new>w (-X%)` or `DELETE: <path> — <reason>`. Concatenate all results into `/tmp/agent_reports.txt`.
5. Apply DELETEs:
   ```bash
   cat /tmp/agent_reports.txt | "$SKILL_DIR/scripts/apply_agent_results.py" "$TARGET"
   ```

> [!warning]
> **Nested-agent fallback**: if this skill is invoked from inside a sub-agent context where the `Agent` tool is unavailable (e.g. inside a `format-docs-optimizer` itself), parallel dispatch is impossible. Fall back to sequential per-file optimization in this same context — apply the per-agent prompt rules (see `references/agent_prompt.md`, kept verbatim for this fallback) one file at a time using the Read + Write tools yourself. All other phases run identically.

### Phase 3 — Sync metadata.json

```bash
"$SKILL_DIR/scripts/sync_metadata.py" "$TARGET"
```

Re-reads each surviving file's YAML frontmatter (agents may have updated `summary`, `tags`, added `optimized: true`), syncs into `documents[]`, and writes the top-level `optimization{}` block (preserving the `deleted_files[]` accumulator). Atomic write.

### Phase 3a — Recalculate `word_count`

```bash
"$SKILL_DIR/scripts/recalc_word_count.py" "$TARGET"
```

Optimizer rewrites prose into tables/code/structured Obsidian markdown. The original `word_count` field (set by upstream crawler from raw HTML extraction) becomes stale. This script re-counts each file's body words (excluding frontmatter and code fence interiors), updates `word_count:` in frontmatter in-place, and syncs `metadata.json[*].word_count`. Idempotent — safe to re-run.

### Phase 4 — Regenerate `000-index.md`

```bash
"$SKILL_DIR/scripts/regenerate_index.py" "$TARGET"
```

Produces a compact 3-column table (`# | File | Title`) per category. Strips trailing site-name suffix from titles (e.g. " - Fireworks AI Docs"). Honors the original index's category order + frontmatter `categories` field type (int vs YAML list). Drops empty categories. Recomputes per-category file ranges from current numbering — gaps from deletions stay (a feature, signaling what was removed without breaking external references). Per-doc `summary` and `tags` deliberately omitted: index is for navigation, not full metadata; consult each file's frontmatter for those.

> [!note]
> The script flattens H4 sub-buckets into a single H3 table per category. If the original `000-index.md` used H4 sub-grouping (e.g. by filename prefix) and that nuance matters to the reader, manually polish the regenerated index after the script. Read `references/decision_trees.md` for when this is worth the bother.

### Phase 5 — Verify

```bash
"$SKILL_DIR/scripts/verify.sh" "$TARGET"
```

Five checks: file count vs metadata, every metadata entry exists, every disk file is in metadata, every numbered file has `optimized: true`, no wikilinks point to deleted files. Exit 0 = PASS. Anything non-zero must be investigated, not silenced.

If `verify.sh` exits non-zero, dispatch a single foreground `Agent` call with `subagent_type: "format-docs-verifier"`. Pass the raw `verify.sh` stdout (the failure list) plus the contents of `/tmp/siblings.json` (under a `## SIBLINGS` heading) as the `prompt`:

```
Agent({
  subagent_type: "format-docs-verifier",
  description: "Resolve verify failures",
  prompt: "<verify.sh stdout>\n\n## SIBLINGS\n<siblings.json>",
  run_in_background: false
})
```

The verifier returns one line per failure:

- `FIXED: <file> — <summary>` → already applied in place; no caller action needed.
- `RETRY-OPTIMIZE: <path>` → re-dispatch that single file via `format-docs-optimizer` (a one-file batch — single `Agent` call). Then re-run `sync_metadata.py`.
- `ABSORB-ORPHANS: <path>` or `ABSORB-ORPHANS: <ALL>` → re-run `inventory.py --absorb-orphans` then `sync_metadata.py`.
- `UNFIXABLE: <file> — <reason>` → escalate to user with the reason; do NOT loop.

After applying any retries/absorbs, re-run `verify.sh` ONCE. Two consecutive FAIL → stop and report to user. Do not loop.

### Phase 6 — Final report

Single concise message to user (caveman style if active):

```
Done. <N_kept> files optimized, <N_deleted> deleted, <N_added> orphans absorbed.
Avg density: -X% tokens (median of OK lines from agents).
Folder: <path>.
Deleted: <list> (or "none").
Added (orphans): <list> (or "none").
Index regenerated: 000-index.md.
Verify: PASS / FAIL (with details).
```

## Failure modes worth recognizing

- **Folder has no `metadata.json`** → `setup.sh` aborts with exit 2. Tell the user to run `organize-docs-skill` first.
- **All files already have `optimized: true`** → `plan_batches.py` returns `total_pending: 0`. Skip Phase 2, still run Phase 3 + 4 (in case orphan absorption changed `documents[]`) and verify.
- **Sub-agent fails / times out** → retry that batch ONCE by issuing a fresh `Agent` call for the same batch. If second failure → report which files were skipped, do NOT block the rest of the run.
- **Binary or non-markdown file dragged in** (e.g. a `.json` mixed into the folder) → skip optimization, leave as-is, keep in metadata.
- **Frontmatter parse error** in a file → report the path, skip optimization for that file, keep it in metadata as-is.
- **Verify fails on `NOT-OPTIMIZED`** → that file's batch failed silently. Re-dispatch the file solo, then re-run verify.
- **Verify fails on `MISMATCH` / `ORPHAN`** → run `inventory.py --absorb-orphans` again, then `sync_metadata.py`, then re-run verify.

## Edge cases

- **Numbered files NEVER renumbered.** Sequential numbering from `organize-docs-skill` is preserved as-is. Gaps from deletions stay (002, 003, 005, 006...) — they signal what was removed without breaking external references.
- **Sub-bucket recovery** — when `regenerate_index.py` flattens H4 groupings, you may manually re-add H4 sections by reading the categorized entries' filename prefixes. Only worth it for indexes that humans will read; agents don't care.
- **Custom frontmatter fields** — `sync_metadata.py` only syncs `summary`, `tags`, `title`, `optimized`. If a domain has custom fields that need syncing, extend the script and gate the change behind a user approval.

## Working directory and `$SKILL_DIR`

`$SKILL_DIR` is the directory containing this `SKILL.md`. Resolve it from the path of this file at session start. With this pi-native install, `$SKILL_DIR` resolves to `/home/diogo/dev/library-docs/.pi/skills/format-docs-pi-skill/`.

## Improving the skill from real-world use

Every run is a feedback signal. Real folders surface edge cases the test cases miss. **Never edit `SKILL.md`, `scripts/`, or `references/` silently.**

The user can opt out with anything like "just format, skip the review" — in that case run the workflow and report, no proposals.

### Where to look (review checkpoints)

These are not separate phases. They are moments where you already inspect output; pause and ask "does this look right?":

- **After Phase 0** — does `orphans` cover every `.md` file you see on disk that's not in metadata? Did `--absorb-orphans` create stubs that look reasonable (title derived from H1, not gibberish)?
- **After Phase 1** — read 2-3 files that triage marked for deletion. Are any of them actually substantive? (False positives belong in `triage.py`'s heuristics, not in a one-off undo.)
- **After Phase 2** — spot-check one OK and one DELETE result. Does the OK file still have all original code blocks / parameter tables? Does the DELETE file actually deserve removal?
- **After Phase 4** — open `000-index.md` and read it as a user would. Repeated values down the Title column? Broken acronyms? Sub-bucket headers that should have been H4 but flattened to H3?
- **After Phase 5** — `verify.sh` PASS does not mean perfect; reread the run anyway.
- **Anywhere a script crashes or returns malformed output.**

### What is worth proposing

Propose a fix **only when all of these hold**:

1. Issue is **visible in concrete output** — quote the bad row, file, or report line. Not a hunch.
2. Root cause sits in a script here, not in upstream data quality (crawler labels, source `metadata.json`).
3. Fix **generalizes** — same change would help future folders too. Folder-specific quirks belong in the run summary, not in scripts.
4. Fix is **small and contained** (≤30 lines, ~1-2 functions). Bigger refactors need a fresh conversation.

Cap proposals at ~3 per run; rank by impact.

### Proposal format

Stop and ask **before editing anything**:

```
**Proposed improvement [N/M]**
- Observed: <concrete evidence — quote the surprising output exactly>
- Cause: <script + function + the specific reason it produces this>
- Fix: <file path, before/after of the changed lines>
- Generalizes because: <one sentence>
- Risk / regression check: <what could break>
- Apply?
```

### Approval and aftermath

Wait for an explicit yes (`yes`, `apply`, `go`, `aprovar`) before touching any file under `$SKILL_DIR`. Ambiguous answers ("hmm", "maybe later") are noes.

After applying:

1. Re-run only the affected phase forward. Phase 1 changed → re-run 1, 2, 3, 4, 5. Phase 4 changed → re-run 4, 5. Scripts are idempotent.
2. Confirm `verify.sh` still PASSes.
3. Confirm the targeted issue is gone in new output. Quote the fixed row back.
4. Append a one-line entry to `$SKILL_DIR/CHANGELOG.md`:
   ```
   - YYYY-MM-DD — <one-line summary>. Found via <folder name>.
   ```

## When the skill is the wrong tool

This skill expects a `metadata.json` produced by `organize-docs-skill` (or `repodocs-go`) plus numbered `nnn-*.md` files. If the folder has unrelated `.md` files without metadata, run `organize-docs-skill` first. If the user wants to optimize a single isolated `.md` file (no folder context), do the rewrite inline using the rules from `references/agent_prompt.md` — no batching, no metadata, no index needed.
