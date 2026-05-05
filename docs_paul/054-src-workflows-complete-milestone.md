---
title: Complete milestone
url: https://github.com/ChristopherKahler/paul/blob/main/src/workflows/complete-milestone.md
source: git
fetched_at: 2026-04-30T00:53:10.026728623-03:00
rendered_js: false
word_count: 912
summary: Workflow for finalizing a project milestone. Gathers performance statistics, updates project documentation, archives milestone states, and resets development environment.
tags:
    - milestone-completion
    - project-management
    - workflow-automation
    - documentation-maintenance
    - version-control
    - process-standardization
category: guide
optimized: true
optimized_at: 2026-05-04T21:20:00Z
---

# Complete milestone

<purpose>
Mark a milestone complete after all phases are done. Creates permanent milestone entry in MILESTONES.md, archives the milestone state, evolves PROJECT.md requirements, updates ROADMAP.md, and prepares for the next milestone.

**Completion ritual:** This is a moment to reflect on what was accomplished before moving forward.
</purpose>

---

## When to use

- All phases in current milestone have status "Complete"
- User explicitly triggers milestone completion
- Triggered by transition-phase when last phase completes

---

## Loop context

| Aspect | Value |
|--------|-------|
| Context | Milestone transition workflow, not a loop phase |
| After completion | Project ready for /paul:discuss-milestone or /paul:milestone |

---

## Required reading

- @.paul/STATE.md
- @.paul/PROJECT.md
- @.paul/ROADMAP.md
- SUMMARY.md files from all milestone phases

---

## References

- [[047-src-templates-milestones.md|MILESTONES.md]] (entry format)
- [[082-src-templates-milestone-archive.md|milestone-archive.md]] (archive format)

---

## Process

### Step 1: Verify readiness

1. Read ROADMAP.md to identify current milestone phases
2. For each phase in milestone:
   - Check if Status = "Complete" or "✅ Complete"
   - Count completed vs total

3. **If all phases complete:**
   - Display: "All {N} phases complete. Ready to finalize milestone."
   - Proceed to next step

4. **If incomplete phases exist:**
   ```
   ════════════════════════════════════════
   MILESTONE INCOMPLETE
   ════════════════════════════════════════

   {milestone_name} has incomplete phases:

   | Phase | Name | Status |
   |-------|------|--------|
   | {N} | {name} | ✓ Complete |
   | {N+1} | {name} | ✗ In Progress |

   Options:
   [1] Complete remaining phases first
   [2] Mark complete anyway (skip remaining)
   ════════════════════════════════════════
   ```
   Wait for decision. If "1" → exit workflow. If "2" → proceed.

### Step 2: Gather stats

Calculate milestone statistics:

| Metric | Source | Calculation |
|--------|--------|-------------|
| **Duration** | First and last SUMMARY.md timestamps | Elapsed time between `started:` and `completed:` |
| **Files** | All SUMMARY.md `key-files.created` + `key-files.modified` | Count unique files |
| **Plans** | SUMMARY.md files | Count across all phases |
| **Phases** | Phase directories | Count in milestone |

Store as:
```yaml
duration: "X days" or "X hours"
files_changed: N
plans_completed: N
phases: N
```

### Step 3: Extract accomplishments

Read all SUMMARY.md files from milestone phases:

1. Collect all "Accomplishments" sections
2. Deduplicate similar items
3. Group by theme/feature
4. Create 5-10 bullet summary

Store as `accomplishments` list.

### Step 4: Create milestone entry

Create or update `.paul/MILESTONES.md`:

**If file doesn't exist, create with header:**
```markdown
# Milestones

Completed milestone log for this project.

| Milestone | Completed | Duration | Stats |
|-----------|-----------|----------|-------|

---
```

**Add entry:**
```markdown
## ✅ {milestone_name}

**Completed:** {date}
**Duration:** {duration}

### Stats

| Metric | Value |
|--------|-------|
| Phases | {phases} |
| Plans | {plans_completed} |
| Files changed | {files_changed} |

### Key Accomplishments

{accomplishments as bullets}

### Key Decisions

{decisions from SUMMARY.md files}

---
```

**Update table at top:**
```markdown
| {milestone_name} | {date} | {duration} | {phases} phases, {plans} plans |
```

### Step 5: Evolve project

> [!note]
> **Full PROJECT.md review** — milestone boundary is the right time to evolve requirements.

Read PROJECT.md and assess each section:

1. **Requirements - Validated:**
   - What requirements shipped in this milestone?
   - Move from "Active" to "Validated": `- [x] {requirement} — {milestone_name}`

2. **Requirements - Invalidated:**
   - What requirements were discovered unnecessary?
   - Move to "Out of Scope": `- {requirement} — Discovered during {milestone_name}`

3. **Requirements - Emerged:**
   - What new requirements emerged during building?
   - Add to "Active": `- [ ] {new requirement}`

4. **Key Decisions:**
   - Extract significant decisions from milestone SUMMARYs
   - Add to Key Decisions table with date and rationale

5. **Success Metrics:**
   - Update "Current" column with actual values

6. **Version:**
   - Update version number to milestone version

Update footer: `*Last updated: {date} after {milestone_name}*`

### Step 6: Archive milestone

Create milestone archive:

1. Create directory: `mkdir -p .paul/milestones`

2. Create archive file `.paul/milestones/{version}-ROADMAP.md`:
   - Copy current ROADMAP.md content
   - Add archive header with completion date

3. Archive structure:
   ```markdown
   # {milestone_name} - Archive

   **Archived:** {date}
   **Status:** Complete

   ---

   {ROADMAP.md content at time of completion}
   ```

### Step 7: Reorganize roadmap

Update ROADMAP.md to collapse completed milestone:

1. **Update Current Milestone section:**
   ```markdown
   ## Current Milestone
   **{milestone_name}** ({version})
   Status: ✅ Complete
   Completed: {date}
   ```

2. **Add Next Milestone placeholder:**
   ```markdown
   ## Next Milestone
   Run /paul:discuss-milestone or /paul:milestone to define.
   ```

3. **Move completed phases to Completed section:**
   ```markdown
   ## Completed Milestones

   <details>
   <summary>{milestone_name} - {date} ({phases} phases)</summary>

   | Phase | Name | Plans | Completed |
   |-------|------|-------|-----------|
   | {N} | {name} | {X/X} | {date} |

   </details>
   ```

4. **Update footer timestamp**

### Step 8: Update state

Update STATE.md for post-milestone state:

1. **Current Position:**
   ```markdown
   ## Current Position

   Milestone: Awaiting next milestone
   Phase: None active
   Plan: None
   Status: Milestone {milestone_name} complete — ready for next
   Last activity: {timestamp} — Milestone completed
   ```

2. **Progress:**
   ```markdown
   Progress:
   - {milestone_name}: [██████████] 100% ✓
   ```

3. **Loop Position:**
   ```markdown
   ## Loop Position

   Current loop state:
   ```
   PLAN ──▶ APPLY ──▶ UNIFY
     ○        ○        ○     [Milestone complete - ready for next]
   ```
   ```

4. **Session Continuity:**
   ```markdown
   ## Session Continuity

   Last session: {timestamp}
   Stopped at: Milestone {milestone_name} complete
   Next action: /paul:discuss-milestone or /paul:milestone
   Resume file: .paul/MILESTONES.md
   ```

### Step 9: Verify version alignment

> [!critical]
> **Verify version consistency across all locations before tagging.**

**Version locations to check:**

| Location | Field | Example |
|----------|-------|---------|
| `.paul/PROJECT.md` | Current State table → Version | `0.3.0` |
| `.paul/ROADMAP.md` | Version Overview table | `v0.3` |
| `.paul/STATE.md` | Version field | `v0.3.0` |
| `.paul/config.md` | version field (if exists) | `0.3.0` |
| `package.json` | "version" field (if exists) | `"0.3.0"` |

**Process:**

1. Read current version from each location
2. Compare versions:
   - **If all aligned:** Proceed to git_tag
   - **If misaligned:** Display table of mismatches, ask user which is correct, then update all locations
3. After updating, commit version alignment
4. Confirm: "Version alignment: ✓ All locations now show: {version}"

### Step 10: Git tag

Create annotated git tag:

```bash
git tag -a "{version}" -m "{milestone_name} complete - {accomplishment_summary}"
```

Display:
```
Git tag created: {version}
(Push with: git push origin {version})
```

**Note:** Do not push automatically — user controls when to push.

### Step 11: Sync paul.json

**Sync satellite manifest (paul.json):**

1. Check if `.paul/paul.json` exists
2. If found: update:
   - `milestone.status` → "complete"
   - `timestamps.updated_at` → current ISO timestamp
3. Write updated paul.json back

### Step 12: Offer next

Display completion with celebration:

```
════════════════════════════════════════
🎉 MILESTONE COMPLETE
════════════════════════════════════════

{milestone_name}

Stats:
| Metric | Value |
|--------|-------|
| Duration | {duration} |
| Phases | {phases} |
| Plans | {plans_completed} |
| Files | {files_changed} |

Key Accomplishments:
{top 3 accomplishments}

Created:
  .paul/MILESTONES.md entry    ✓
  .paul/milestones/{version}-ROADMAP.md    ✓
  git tag: {version}    ✓

Updated:
  PROJECT.md (evolved)    ✓
  ROADMAP.md (reorganized)    ✓
  STATE.md (cleared)    ✓

────────────────────────────────────────
▶ NEXT: /paul:discuss-milestone
  Define the scope for the next milestone
────────────────────────────────────────

Or /paul:milestone to create milestone directly.
```

---

## Output

| Output | Description |
|--------|-------------|
| MILESTONES.md entry created | Permanent record of milestone |
| .paul/milestones/{version}-ROADMAP.md archive created | Preserves state at completion |
| PROJECT.md evolved | Requirements validated/invalidated |
| ROADMAP.md reorganized | Milestone collapsed |
| STATE.md cleared | Ready for next milestone |
| Git tag created | Version marker |

---

## Success criteria

- [ ] All phases verified complete (or user chose to skip)
- [ ] Statistics gathered from SUMMARYs
- [ ] MILESTONES.md entry created with accomplishments
- [ ] Archive file created in .paul/milestones/
- [ ] PROJECT.md evolved (requirements audited)
- [ ] ROADMAP.md reorganized (milestone collapsed)
- [ ] STATE.md updated for post-milestone state
- [ ] Version alignment verified across 5 locations
- [ ] Git tag created
- [ ] Clear next action offered

---

## Error handling

| Error | Action |
|-------|--------|
| **MILESTONES.md doesn't exist** | Create with header template, proceed with entry creation |
| **No SUMMARY.md files found** | Warn, offer to proceed anyway or investigate |
| **Git tag already exists** | Warn, offer to increment patch version or skip tag |
| **PROJECT.md evolution unclear** | Ask user which requirements to validate/invalidate, don't make assumptions |

---

#milestone-completion #project-management #workflow-automation #documentation-maintenance #version-control