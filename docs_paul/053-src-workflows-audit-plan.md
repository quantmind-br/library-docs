---
title: Audit plan
url: https://github.com/ChristopherKahler/paul/blob/main/src/workflows/audit-plan.md
source: git
fetched_at: 2026-04-30T00:53:08.935771376-03:00
rendered_js: false
word_count: 1338
summary: Process for performing enterprise-grade architectural audit on a technical plan. Includes risk assessment, compliance validation, and automated plan modification.
tags:
    - architectural-audit
    - compliance-review
    - risk-assessment
    - enterprise-software
    - quality-assurance
    - automated-governance
category: guide
optimized: true
optimized_at: 2026-05-04T21:20:00Z
---

# Audit plan

<purpose>
Perform an enterprise-grade architectural audit on an approved PLAN.md. Assume the role of a senior principal engineer + compliance reviewer. Identify gaps, classify findings by severity, auto-apply must-have and strongly-recommended fixes to the plan, and produce a persistent audit report.
</purpose>

---

## When to use

- After PLAN phase when `enterprise_plan_audit: enabled: true` in config.md
- When `/paul:audit` is explicitly invoked by the user
- Before APPLY phase to strengthen plan quality for commercial/enterprise software

---

## Loop context

| Aspect | Value |
|--------|-------|
| Expected phase | Between PLAN and APPLY (sub-step of PLAN) |
| Prior phase | PLAN (plan created, awaiting approval) |
| Next phase | APPLY (after audit and approval) |

---

## Required reading

- @.paul/STATE.md
- @.paul/config.md
- PLAN.md at path from STATE.md "Resume file" field

---

## Process

### Step 1: Validate preconditions

1. Read STATE.md to confirm:
   - Loop position shows PLAN complete (checkmark on PLAN)
   - A plan path exists (from $ARGUMENTS or infer from STATE.md "Resume file" field)
2. If no plan found:
   - Error: "No plan found to audit. Run /paul:plan first."
   - Exit workflow
3. If loop is not at PLAN complete:
   - Warn: "Loop not at PLAN stage. Current state: [state]"
   - Exit workflow
4. Read config.md and check for `enterprise_plan_audit: enabled: true`
   - If enabled: proceed normally
   - If not enabled or config missing: display warning but allow manual invocation
   - Proceed regardless (manual invocation is always allowed)

### Step 2: Load plan

1. Read the PLAN.md file at the resolved path
2. Derive paths:
   - Phase directory: parent directory of PLAN.md
   - Audit report path: replace `-PLAN.md` with `-AUDIT.md` in filename
3. Parse plan structure:
   - Extract objective, acceptance criteria, tasks, boundaries, verification
   - Note task count, checkpoint types, files modified
   - Identify the plan's scope and architectural decisions
4. Store full plan content for audit analysis

### Step 3: Execute audit

> [!warning]
> **Role:** Senior principal engineer + compliance reviewer. Perform a **hard, honest audit**. Do **not** validate or encourage. Assume system used in regulated environment, reviewed by auditors, operated by humans who make mistakes, maintained for multiple years.

**Tone requirements:**
- Direct, critical, and specific
- No praise unless it directly supports a risk decision
- Call out missing controls, underspecified behavior, and latent risk
- Do NOT optimize for politeness

Produce structured output:

#### 1. Executive Verdict
- Is this plan **enterprise-ready**, **conditionally acceptable**, or **not acceptable**?
- Would you approve this plan for production if accountable?

#### 2. What Is Solid
- Identify elements that are correctly layered, appropriately constrained, aligned with enterprise expectations
- Be specific about **why** they are solid

#### 3. Enterprise Gaps / Latent Risks
Identify **non-obvious risks**, including:
- Missing authorization boundaries
- State ambiguity or invalid transitions
- Audit trail weaknesses
- Idempotency gaps
- Error handling omissions
- Side-effect risks (email, payments, AI calls, external APIs)
- Long-term maintenance hazards
- Treat anything underspecified as a risk

#### 4. Concrete Upgrades Required
For each major gap:
- Explain **why it matters**
- Specify **what must be added or changed**
- Classify as:
  - **Must-have** (release-blocking)
  - **Strongly recommended**
  - **Can safely defer**
- Avoid abstract advice — give implementation-level guidance

#### 5. Audit & Compliance Readiness
Evaluate whether the plan:
- Produces defensible audit evidence
- Prevents silent failures
- Supports post-incident reconstruction
- Has clear ownership and accountability
- Call out any area that would fail a real audit

#### 6. Final Release Bar
- What must be true before this plan ships
- What risks remain if shipped as-is
- Whether you would sign your name to this system

**Constraints:**
- Do NOT invent requirements not implied by the plan
- Do NOT assume "future phases" will fix gaps
- Do NOT say "this is fine for v1" unless justified
- Treat this as the *last review before production*

### Step 4: Classify findings

From audit output, categorize all findings:

**Must-Have (Release-Blocking):**
- Each finding with: description, affected plan section, required change
- These WILL be applied to the plan automatically

**Strongly Recommended:**
- Each finding with: description, affected plan section, required change
- These WILL be applied to the plan automatically

**Can Safely Defer:**
- Each finding with: description, rationale for deferral
- These will NOT be applied but noted in audit report

Count totals: N must-have, M strongly-recommended, P can-safely-defer

### Step 5: Apply findings to plan

> [!critical]
> **Automatically apply must-have and strongly-recommended findings to the PLAN.md.**

For each finding requiring modification:

1. **Acceptance Criteria gaps:** Add new Given/When/Then criteria or strengthen existing ones
2. **Task gaps:** Add new tasks, verification steps, or strengthen action descriptions
3. **Boundary gaps:** Add new boundary constraints to `<boundaries>` section
4. **Verification gaps:** Add new checks to `<verification>` section
5. **Authorization/security gaps:** Add constraints, validation steps, or audit trail requirements
6. **Error handling gaps:** Add error scenarios to acceptance criteria and recovery steps to tasks

**Rules for applying findings:**
- Preserve existing plan structure and formatting
- Add new content clearly (do not silently rewrite)
- Mark audit-added content with `<!-- audit-added -->` comment where practical
- If finding requires new task, add it in appropriate sequence position
- If finding strengthens existing task, append to its `<action>` or `<verify>` section
- Update `files_modified` in frontmatter if new files introduced
- Update `autonomous` flag if new checkpoints required

Track all changes:
- Section modified
- What was added/changed
- Which finding it addresses

### Step 6: Create audit report

Write audit report to `{NN}-{PP}-AUDIT.md` in same phase directory as PLAN.

**Report structure:**

```markdown
# Enterprise Plan Audit Report

**Plan:** [plan-path]
**Audited:** [timestamp]
**Verdict:** [enterprise-ready / conditionally acceptable / not acceptable]

---

## 1. Executive Verdict

[From audit step - clear yes/no/conditional with reasoning]

## 2. What Is Solid

[From audit step - elements that should not change and why]

## 3. Enterprise Gaps Identified

[From audit step - full list of non-obvious risks found]

## 4. Upgrades Applied to Plan

### Must-Have (Release-Blocking)

| # | Finding | Plan Section Modified | Change Applied |
|---|---------|----------------------|----------------|
| 1 | [description] | [section] | [what was changed] |

### Strongly Recommended

| # | Finding | Plan Section Modified | Change Applied |
|---|---------|----------------------|----------------|
| 1 | [description] | [section] | [what was changed] |

### Deferred (Can Safely Defer)

| # | Finding | Rationale for Deferral |
|---|---------|----------------------|
| 1 | [description] | [why safe to defer] |

## 5. Audit & Compliance Readiness

[From audit step - evidence, failure prevention, reconstruction, ownership]

## 6. Final Release Bar

[From audit step - what must be true, remaining risks, sign-off statement]

---

**Summary:** Applied [X] must-have + [Y] strongly-recommended upgrades. Deferred [Z] items.
**Plan status:** [Updated and ready for APPLY / Requires manual review before APPLY]

---
*Audit performed by PAUL Enterprise Audit Workflow*
*Audit template version: 1.0*
```

### Step 7: Update state

> [!required]
> **This step is REQUIRED. Do not skip.**

1. **Update STATE.md:**
   - Change plan status from "created, awaiting approval" to "created + audited, awaiting approval"
   - Update Last activity with audit timestamp
   - Add to `### Decisions` section:
     `| [timestamp]: Enterprise audit performed on [plan-path]. Applied [X] must-have, [Y] strongly-recommended upgrades. Deferred [Z]. Verdict: [verdict] | Phase [N] | Plan strengthened for enterprise standards |`

2. **Do NOT change loop position** — PLAN still checked, APPLY still unchecked. Audit is a sub-step of PLAN.

### Step 8: Report and route

Display audit summary with routing:

```
════════════════════════════════════════
AUDIT COMPLETE
════════════════════════════════════════

Verdict: [enterprise-ready / conditionally acceptable / not acceptable]

Applied to plan:
  [X] must-have (release-blocking) upgrades
  [Y] strongly-recommended upgrades
Deferred:
  [Z] can-safely-defer items

Report: [audit-report-path]

---
Continue to APPLY?

[1] Approved, run APPLY | [2] Review audit report | [3] Questions | [4] Pause
```

**Accept quick inputs:**
- "1", "approved", "yes", "go" → run `/paul:apply [plan-path]`
- "2", "review" → Read and display AUDIT.md report contents

**If verdict is "not acceptable":**
```
⚠️  Plan did NOT pass enterprise audit.

The plan requires significant revision before execution.
Review the audit report and address critical findings.

[1] Review audit report | [2] Re-plan this phase | [3] Questions
```

---

## Output

- Updated PLAN.md with must-have and strongly-recommended fixes applied
- AUDIT.md report at `{phase-dir}/{NN}-{PP}-AUDIT.md`
- STATE.md updated with audit status

---

## Error handling

| Error | Action |
|-------|--------|
| **Plan not found** | Check STATE.md for correct path. Ask user to confirm plan location or run /paul:plan first |
| **Config missing enterprise_plan_audit** | Warn but proceed (manual invocation valid). Suggest adding config for automatic suggestion flow |
| **Plan too vague to audit meaningfully** | Note in audit report. Classify as "not acceptable" with concrete requirements for what must be specified. Do NOT fabricate an audit |
| **Audit produces no findings** | Valid (plan may already be enterprise-grade). Report "enterprise-ready" verdict with reasoning. Proceed to APPLY routing normally |

---

## Anti-patterns

| Anti-pattern | Description |
|--------------|-------------|
| **Rubber-stamping** | Do NOT produce positive audit without substantive analysis. Every plan has areas that can be strengthened |
| **Scope creep in fixes** | Applied fixes should address specific gap, not redesign the plan. Stay within existing architecture |
| **Inventing phantom requirements** | Only audit against what plan implies. Do not introduce requirements from outside project scope |
| **Skipping auto-apply** | The entire value of this workflow is automated remediation. If findings identified, they MUST be applied (except can-safely-defer) |

---

#architectural-audit #compliance-review #risk-assessment #enterprise-software #quality-assurance