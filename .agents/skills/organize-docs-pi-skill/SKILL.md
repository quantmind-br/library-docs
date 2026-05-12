---
name: organize-docs-pi-skill
description: Organize a documentation folder produced by `repodocs-go` (or any crawler that emits `metadata.json` + `.md` files) into deterministic, lowercase, sequentially-numbered files plus a generated `000-index.md` optimized for AI agent consumption. Make sure to use this skill whenever the user asks to organize, normalize, renumber, sort, index, or clean up a documentation folder, or works with a folder containing `metadata.json` and bulk `.md` documents — even when phrased as "organize these docs", "sort the markdown files", "build me a docs index", "renumber this docs dump", "normalize the filenames", or any equivalent. Trigger on phrases like "library-docs", "metadata.json", "docs folder", "crawler output", "documentation index", "renumber files".
---

# Organize Documentation from Metadata

You are processing a folder produced by a documentation crawler. The folder contains:

- `metadata.json` with a top-level `documents[]` array. Each entry has at minimum: `file_path`, `title`, `summary`, `tags`, `category`, `url`, often `fetched_at`.
- The sibling `*.md` files referenced by `documents[].file_path`.

Goal: every doc ends up at `nnn-<lowercase-slug>.md` (zero-padded 3-digit prefix, ascending across categories). A generated `000-index.md` provides AI-agent navigation. `metadata.json` is mutated in place to track every rename plus a `dropped[]` audit trail.

## Why a skill instead of inline reasoning

The mechanics (lowercase, prefix detection, bucket assignment, atomic renames, JSON mutation, index rendering, verification) are deterministic and benefit from being scripted: scripts are faster, reproducible, and remove a class of arithmetic / typo errors. The semantic decisions (renaming an `index`-named file based on its content; resolving an ambiguous partial duplicate) require reading files and stay with you. The split between "the script does this, you decide that" is what makes the workflow predictable.

## Bundled scripts

All scripts live next to this `SKILL.md` under `scripts/`. They print JSON to stdout for easy piping/parsing.

| Script | Phase | Purpose |
|--------|-------|---------|
| `normalize.py <dir> [--apply]` | 1 | Lowercase + 100%-common-prefix strip; reports `index`-named files |
| `rename_one.py <dir> <old> <new>` | 1.3 / 2 | Single rename + metadata sync; refuses to leave `index` in source filenames |
| `find_dupes.py <dir> [--threshold N]` | 2 | SHA-256 + Jaccard scan over top-level `*.md` files; self-contained (Python stdlib only) |
| `classify_dupes.py <dupes.json>` | 2 | Splits raw dupe pairs into `identico` / `version_mirror` / `ambiguous` so the deterministic groups can be drained without reading any file |
| `apply_drop.py <dir> <dropped> --in-favor-of <kept>` | 2 | Delete file + remove from documents[] + log under organization.dropped[] |
| `categorize.py <metadata.json>` | 3 | Bucket assignment with override + overflow split; emits plan JSON |
| `number_and_rename.py <dir> --buckets <plan> --apply` | 4 + 5 | Sequential numbering + organization{} audit |
| `generate_index.py <dir> --buckets <plan>` | 6 | Renders `000-index.md` |
| `verify.sh <dir>` | 7 | Pass/fail check (count, gaps, missing, forbidden tokens) |

Most scripts default to dry-run; pass `--apply` (or run the bash variants directly) to mutate.

The `description` field in `metadata.json` is crawler boilerplate (e.g. `"> ## Documentation Index > Fetch..."`). Ignore it everywhere — `summary` and `tags` carry the real content.

## Workflow

### 0. Resolve the target directory

The skill argument (if any) is a path to `metadata.json` or its parent folder. `cd` into the parent. Verify `metadata.json` is present before continuing. Capture the absolute path in `$DIR` for downstream commands.

### 1. Normalize filenames

```bash
python3 "$SKILL_DIR/scripts/normalize.py" "$DIR" --apply
```

Read the JSON output. The interesting field is `index_files_pending`: every filename containing `index` that survived lowercase + prefix-strip. **For each entry**:

1. Read the file with the Read tool.
2. Derive a slug from H1 / `metadata.title` / `metadata.summary`. Slug **must not** contain the word `index` (rule enforced by `rename_one.py`). Examples and guidance live in `references/decision_trees.md` ("Index-rename slug derivation").
3. Apply:
   ```bash
   python3 "$SKILL_DIR/scripts/rename_one.py" "$DIR" "<old>" "<new>" --reason "phase 1.3 index rename"
   ```

If `index_files_pending` is empty, skip this step.

### 2. Detect and resolve duplicates

Run the dedupe scan and immediately split it into deterministic groups:

```bash
python3 "$SKILL_DIR/scripts/find_dupes.py" "$DIR" --threshold 85 > /tmp/dupes.json
python3 "$SKILL_DIR/scripts/classify_dupes.py" /tmp/dupes.json > /tmp/classified.json
jq '.summary' /tmp/classified.json
```

`classify_dupes.py` splits the raw pairs into three lists:

- **`identico`** (similarity 100): drop the loser deterministically.
- **`version_mirror`** (parcial pairs whose filenames differ only by a version segment like `1.5-` or `v2-`): keep the canonical / latest, drop the older. The classifier picks the version-less filename when one exists, otherwise the highest semantic version.
- **`ambiguous`**: read both files and apply the decision tree in `references/decision_trees.md`. **Default verdict is keep both.**

Drain the deterministic groups with a small loop — no file reads required:

```bash
jq -r '.identico[] | "\(.drop)|\(.keep)|identico"' /tmp/classified.json \
  > /tmp/auto_drops.tsv
jq -r '.version_mirror[] | "\(.drop)|\(.keep)|parcial-version-mirror"' /tmp/classified.json \
  >> /tmp/auto_drops.tsv

while IFS='|' read -r drop keep reason; do
  python3 "$SKILL_DIR/scripts/apply_drop.py" "$DIR" "$drop" \
    --in-favor-of "$keep" --reason "$reason"
done < /tmp/auto_drops.tsv
```

Only the **ambiguous** list needs your attention. If `ambiguous` is `0`, skip ahead to Phase 3. Otherwise inspect each pair via the Read tool and apply the decision tree. If `ambiguous ≥ 10`, parallelize via Agent tool batches per `references/decision_trees.md`.

If `find_dupes.py` returns `[]` (no duplicates), skip the entire phase.

### 3. Categorize

```bash
python3 "$SKILL_DIR/scripts/categorize.py" "$DIR/metadata.json" > /tmp/buckets.json
```

The script applies the canonical 3-step rule (override > primary > tertiary > fallback) and detects bucket overflow (>25% of total → split by filename prefix). You normally do **not** need to second-guess its output. Only intervene when:

- The `buckets_used` list contains a bucket you can verify is wrong by reading a few member docs.
- A sub-bucket prefix is meaningless (e.g., `prefix: "api"` when half the docs aren't actually API). In that case re-run with adjusted assumptions or hand-edit `/tmp/buckets.json` before Phase 4.

### 4 & 5. Sequential numbering + metadata sync

```bash
python3 "$SKILL_DIR/scripts/number_and_rename.py" "$DIR" --buckets /tmp/buckets.json --apply
```

Re-run safe: existing `nnn-` prefixes are stripped before re-numbering. Adds `organization{method, organized_at, total_files, categories, dropped[]}` to `metadata.json` and updates the top-level `total_documents`.

### 6. Generate `000-index.md`

```bash
python3 "$SKILL_DIR/scripts/generate_index.py" "$DIR" --buckets /tmp/buckets.json
```

Pass `--project-name "<name>"` if the inferred host name from `source_url` is unhelpful.

### 7. Verify

```bash
"$SKILL_DIR/scripts/verify.sh" "$DIR"
```

Exit 0 = PASS. Anything non-zero is a failure that must be investigated, not silenced.

### 8. Report

Summarize for the user, in this order:

- Number of files renamed.
- Buckets used (in canonical order).
- Anything skipped (prefix-strip didn't apply / no `index` files / no duplicates).
- Drops + renames decided during dedupe (with the reason from `organization.dropped[]`).
- Path to `000-index.md`.
- Verification verdict.

## Working directory and `$SKILL_DIR`

`$SKILL_DIR` is the directory containing this `SKILL.md`. Resolve it once at session start so subsequent commands stay readable — for example, derive it from the path of this file or set it from the location where the skill was loaded.

## Failure modes worth recognizing

- **`normalize.py` reports `prefix_stripped: null`** — fine, just means filenames don't share a 100% common leading substring (e.g., `core-*` mixed with `api-*`). Not an error.
- **`find_dupes.py` returns `[]`** — no duplicates above the threshold. Skip Phase 2 and proceed; not an error.
- **A bucket overflow split produces a single sub-bucket** — `categorize.py` already handles this (it returns `null` for `sub_buckets`). No action needed.
- **`verify.sh` reports a gap** — almost always indicates a previous run was interrupted between Phase 4 and Phase 6. Re-run from Phase 3 (categorize) onward; the scripts are idempotent.
- **`rename_one.py` refuses to apply a name containing `index`** — by design. Pick a slug that reflects the file's primary topic without using that token.

## Improving the skill from real-world use

Every run is a feedback signal. Real folders surface edge cases that the test cases miss, and the skill should evolve when they do — but only with explicit user approval. **Never edit `SKILL.md`, `scripts/`, or `references/` silently.**

The user can opt out with anything like "just organize, skip the review" — in that case run the workflow and report, no proposals.

### Where to look (review checkpoints)

These are not separate phases. They are moments where you already inspect output; pause and ask "does this look right?":

- **After Phase 1** — does `index_files_pending` cover every `index`-named file you see on disk? Did `prefix_stripped` skip a prefix that is obviously shared (e.g. several files share `crawl4ai-docs-` but the script returned `null`)?
- **After Phase 2** — for any `ambiguous` pair the decision tree resolved against your reading of the files, the tree (or `classify_dupes.py`) may need new logic. Same for `version_mirror` picks that landed on the older file.
- **After Phase 3** — read 1–2 docs from each bucket. Does anything sit in a clearly wrong bucket? (Marketing pages flagged `guide` is the classic example.)
- **After Phase 6** — open `000-index.md` and read it as a user would. Repeated values down the Title column? Broken acronyms (`Paas` instead of `PaaS`)? Sub-bucket headers that are just the project name? Section ranges off by one?
- **After Phase 7** — `verify.sh` PASS does not mean perfect; reread the run anyway.
- **Anywhere a script crashes or returns malformed output.**

### What is worth proposing

Propose a fix **only when all of these hold**:

1. The issue is **visible in concrete output** — you can quote the bad row, bucket, or filename. Not a hunch.
2. The **root cause sits in a script here**, not in upstream data quality (crawler labels, source `metadata.json`). When the crawler is wrong and the script can't reasonably tell, log it under "Open observations" in the run summary instead of patching around it.
3. The fix **generalizes** — the same change would help future folders too. Folder-specific quirks belong in the run summary, not in scripts.
4. The fix is **small and contained** (≤30 lines, ~1–2 functions, or a new entry in an existing list like `OVERRIDES`). Bigger refactors need a fresh conversation, not in-flight surgery.

If any of those fail, mention the observation under "Open observations" in the final report and move on. **Cap proposals at ~3 per run; rank by impact.** Suggestion fatigue is real — the bar must stay high or every run becomes a review meeting.

### Proposal format

Stop and ask **before editing anything**. Use this shape so the user can decide quickly:

```
**Proposed improvement [N/M]**
- Observed: <concrete evidence — quote the surprising output exactly>
- Cause: <script + function + the specific reason it produces this>
- Fix: <file path, before/after of the changed lines, or the new override / regex / branch>
- Generalizes because: <one sentence>
- Risk / regression check: <what could break; if you can name a previously-validated folder where this would still pass, say so>
- Apply?
```

Batch related proposals into one approval gate when natural ("three issues in the rendered index, all in `generate_index.py` — apply all?"). Each unrelated change still gets its own gate.

### Approval and aftermath

Wait for an explicit yes (`yes`, `apply`, `go`, `aprovar`) before touching any file under `$SKILL_DIR`. Ambiguous answers ("hmm", "maybe later") are noes. If the user redirects ("not that, do this instead"), follow the redirection — do not re-propose the original.

After applying:

1. Re-run only the affected phase forward — Phase 3 changed → re-run 3, 4, 5, 6, 7; Phase 6 changed → re-run 6, 7. The scripts are idempotent.
2. Confirm `verify.sh` still PASSes.
3. Confirm the targeted issue is gone in the new output. Quote the fixed row back to the user.
4. Append a one-line entry to `$SKILL_DIR/CHANGELOG.md`:
   ```
   - YYYY-MM-DD — <one-line summary>. Found via <folder name>.
   ```
   Keep it terse. The diff in the script is the detailed record; CHANGELOG.md is the index.

If the change regresses something (verify fails, a previously-good bucket breaks), revert the file with `git checkout` and tell the user. Do not patch the patch in the same turn.

### Things to avoid

- Editing a script without an explicit yes, even when the fix feels obvious.
- Vague proposals ("the workflow could be clearer") with no concrete output to point at.
- Bundling unrelated changes into one proposal — each gets its own gate.
- Cosmetic edits to `SKILL.md` or scripts mid-run. Save grooming for a dedicated session.
- Touching the skill in response to a single anecdotal failure on one folder. Wait for the second occurrence, or argue the generalization clearly.

## When the skill is the wrong tool

This skill expects a `metadata.json` with crawler-style entries. If the user has a flat folder of unrelated `.md` files without metadata, run `categorize.py` won't help — point them at a more general-purpose organize-by-content workflow instead, or generate a stub `metadata.json` first.
