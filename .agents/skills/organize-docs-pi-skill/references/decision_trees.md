# Reference: Decision Trees

Reference material for ambiguous calls during organize-docs-skill. SKILL.md points here when needed; do not load this file by default.

## Partial-duplicate decision tree (Phase 2)

This tree is applied **only** to pairs that `classify_dupes.py` could not auto-resolve — i.e. pairs in the `ambiguous` list. The classifier already handles two large deterministic cases without your help:

- **`identico` (similarity 100)** → drop the loser, keep the larger filename.
- **`version_mirror`** → filenames differ only by a version segment (`-1.5-`, `v2-`, etc.); keep the version-less / highest-semver filename, drop the rest.

For everything that lands in `ambiguous`, read both files **and** their `metadata.json` entries first, then walk the rules in order. **Stop at the first match.**

| # | Test | Action |
|---|------|--------|
| 1 | `metadata.url` (after stripping trailing `/`) is **equal** between the two | Same canonical source. Skip to rule 4. |
| 2 | H1 (first heading) differs **and** `metadata.title` differs | Different docs sharing boilerplate. **Keep both untouched.** |
| 3 | First non-empty paragraph differs in topic (different subject nouns) | **Keep both untouched.** |
| 4 | Same source confirmed; `metadata.fetched_at` available on both | Newer → `-current`, older → `-legacy`. Apply via `rename_one.py`. |
| 5 | Same source, no timestamps available | Larger file → `-current`, smaller → `-legacy`. |
| 6 | Same source, sizes within 10%, no timestamp delta | **Keep both untouched.** |
| 7 | Names already unique and rules 1–6 did not fire | **Keep both untouched.** |
| 8 | Filename collision after Phase 1 forces a choice | Derive suffix from each file's distinct H1 (`-<slug>` per side). Never `-copy`, `-2`. |

**Hard rule:** any uncertainty, conflicting signals, or rule mismatch → keep both. Bias toward preservation. Log the pair plus reason in the run summary.

## Parallelization heuristic for Phase 2

`parcial` pairs typically number 0–5. Inspect sequentially with the Read tool — subagent overhead exceeds the savings.

If `parcial` pairs ≥ 10, dispatch them via the Agent tool in a single message with multiple parallel calls, batched ≤ 5 pairs per subagent (`subagent_type: general-purpose`). Each subagent receives:

- The file paths
- The relevant `metadata.json` entries (extract via `jq`)
- This decision tree

And must return one JSON line per pair:

```json
{"pair": ["a.md", "b.md"], "verdict": "keep_both|drop_a|drop_b|rename", "rename": {"a": "...", "b": "..."}, "reason": "..."}
```

Apply the verdicts via `rename_one.py` / `apply_drop.py`.

## Index-rename slug derivation (Phase 1.3)

When `normalize.py` returns a non-empty `index_files_pending`, you must read each file and derive a slug.

**Required:** the new name must not contain `index` in any form (`index`, `Index`, `indexes`, `indexing`, …). Only the generated `000-index.md` is allowed to use that token.

**Derivation order:**

1. H1 of the file → kebab-case it (e.g., "Welcome to Crawl4AI" → `welcome-overview`).
2. If H1 absent or generic ("Documentation"), use `metadata.title` for the doc.
3. If still ambiguous, use the dominant noun phrase from `metadata.summary`.

**Common transformations:**

| Original | Likely new name |
|----------|------------------|
| `index.md` | `welcome-overview.md` |
| `api-index.md` | `api-reference-overview.md` |
| `whats-new-index.md` | `release-notes-overview.md` |
| `getting-started-index.md` | `getting-started-overview.md` |

**Conflicts:** if the derived name collides with an existing file, append a content-derived disambiguator (`-summary`, `-overview`). Never `-2`, `-copy`.

Apply via `rename_one.py "$DIR" old_name new_name --reason "phase 1.3 index rename"`.
