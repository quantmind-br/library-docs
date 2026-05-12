# Decision Trees

Edge-case rulings for ambiguous situations. The scripts handle the deterministic cases; this document covers the calls you (the dispatcher) need to make.

## Phase 1 triage — keep vs delete

`triage.py` flags candidates. Spot-check the flagged list before applying — its heuristics are conservative but not infallible.

### Keep even if flagged

- **Has any code block, table, or `>` callout** → keep regardless of word count. Short-but-substantive is fine.
- **Reference card / cheat sheet** with terse content (e.g. a list of CLI flags with one-line descriptions) — `triage.py` may misread it as "pointer-only" if word count is low. Keep.
- **Index-named file (`README.md`, `overview.md`) that contains substantive prose** — overrides the filename heuristic. Read the body before trusting the flag.
- **Numbered file (`nnn-*.md`)** flagged as index-like — NEVER deleted by `triage.py` (numbered files are deliberate output of `organize-docs-skill`). If it does look like an index in body, the optimization pass compresses it instead.

### Delete even if not flagged

- **Two files with identical body** (different names, same content hash) — `triage.py` doesn't dedupe; rely on the upstream `organize-docs-skill` for duplicate detection. If a duplicate slipped through, delete manually before Phase 2.
- **File whose entire body is "Coming soon" / "TBD" / "WIP placeholder"** — too short to trip `triage.py`'s 30-word floor only if very brief. Delete manually.

## Phase 2 dispatch — batching judgment

`plan_batches.py` outputs size-bucketed batches. Override only when:

- A batch's combined size genuinely exceeds ~15k input tokens for the agent (rare; the heuristic is generous). Split.
- A batch contains files with extremely different formats (e.g., one is a 1k-line API reference, another is a 100-word changelog entry) — fine, keep batched. The agent prompt is per-file.
- You hit the 10-concurrent-agents-per-message cap — the script doesn't enforce this, the dispatcher does. Send in sequential waves of ≤10.

## Phase 2 — ambiguous DELETE decisions by agent

If an agent returns `DELETE:` for a file you suspect is substantive:

1. Read the file. If the agent was right (truly empty after stripping nav/footer) → let the deletion stand.
2. If the agent was wrong (has substance) → manually re-dispatch that file with an Agent call, prompting it explicitly to "rewrite, do not delete". Update the report.
3. If borderline → keep. The cost of one extra file is low; the cost of dropping unique content is high.

## Phase 4 — index regeneration nuance

`regenerate_index.py` flattens H4 sub-buckets into a single H3 table per category. You may want to re-add H4 grouping when:

- The category has ≥10 entries AND filename prefixes split cleanly into 2+ groups (e.g. `010-models-glm-*`, `019-models-qwen-*`, `023-models-deepseek-*`).
- The original `000-index.md` had H4 sub-headers that humans relied on for navigation.

When manually re-adding H4: read the entries' filenames, group by the most informative shared prefix, re-render the H4 + table for each group. Keep the H3 table as a "see below" pointer or remove it (your call — pick whichever the original used).

Skip this polish when:

- Category has <10 entries (one H3 table is fine).
- Filenames don't share a meaningful prefix.
- The folder is consumed only by agents (humans don't read this index).

## Phase 5 — verify failure routing

| Failure | Likely cause | Fix |
|---------|--------------|-----|
| `MISMATCH: counts differ` | Phase 2 deletion not synced into metadata | Re-run `sync_metadata.py`, then `verify.sh` |
| `MISSING: <file>` | metadata references a file the optimization pass deleted but didn't log | Remove the entry manually with `jq`, or re-run the full pipeline from Phase 1 |
| `ORPHAN: <file>` | File on disk not in metadata | Re-run `inventory.py --absorb-orphans`, then `sync_metadata.py` |
| `NOT-OPTIMIZED: <file>` | An agent batch failed silently for this file | Re-dispatch the file solo with Agent; re-run `verify.sh` |
| `BROKEN-WIKILINK: <file> -> <base>` | Agent wrote a wikilink to a file later deleted (race in dispatch order) | Open the file, revert the wikilink to its original `[text](url)` form, log as a known issue in run summary |

## When to abort the run

- `setup.sh` exits non-zero → tell the user the exact error and do NOT continue.
- `triage.py --apply` would delete >50% of the corpus → pause, show the deletion list to the user, ask for confirmation. Triage shouldn't be that aggressive on a healthy folder.
- Phase 2 returns DELETE for >25% of pending files → same pause; an over-aggressive agent (or a corpus full of nav stubs) needs a human glance before proceeding.
- `verify.sh` returns FAIL after one round of fix-ups → stop, report the failure list, do NOT loop. Loops mask root causes.
