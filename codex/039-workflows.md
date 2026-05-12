---
title: Workflows
url: https://developers.openai.com/codex/workflows.md
source: llms
fetched_at: 2026-04-30T10:16:12.771844792-03:00
rendered_js: false
word_count: 660
summary: This document provides practical, end-to-end workflow recipes for utilizing the Codex IDE extension, CLI, and cloud tools for common development tasks like code explanation, debugging, testing, and prototyping.
tags:
    - codex-ide
    - codex-cli
    - workflow-automation
    - code-refactoring
    - prompt-engineering
    - debugging-guide
    - ui-prototyping
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Workflows

Codex works best with explicit context and a clear definition of "done." Each workflow below includes: when to use it, which surface fits best (IDE, CLI, or cloud), steps with example prompts, context notes, and verification.

If new to Codex, read [[047-prompting|Prompting]] first.

> [!note]
> The IDE extension automatically includes open files as context. In the CLI, mention paths explicitly or attach files with `/mention` and `@` path autocomplete.

---

## Explain a codebase

Onboarding, inheriting a service, or reasoning about protocol/data model/request flow.

### IDE extension (fastest for local exploration)

1. Open the most relevant files.
2. Select code you care about (optional but recommended).
3. Prompt:
   ```text
   Explain how the request flows through the selected code.
   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this
   ```

Verification: ask for a diagram or checklist:
```text
Summarize the request flow as a numbered list of steps. Then list the files involved.
```

### CLI (transcript + shell commands)

1. Start interactive session: `codex`
2. Attach files and prompt:
   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.
   ```

---

## Fix a bug

Failing behavior you can reproduce locally.

### CLI (tight loop with reproduction and verification)

1. Start Codex at repo root: `codex`
2. Give reproduction recipe plus suspected file(s):
   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.
   ```

Verification: Codex should re-run repro steps after fix. If you have a standard check pipeline, ask it to run it:
```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.
```

### IDE extension

1. Open the file where you think the bug lives, plus its nearest caller.
2. Prompt:
   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.
   ```

---

## Write a test

Be explicit about scope.

### IDE extension (selection-based)

1. Open the file with the function.
2. Select the lines that define the function. Choose "Add to Codex Thread" from command palette.
3. Prompt:
   ```text
   Write a unit test for this function. Follow conventions used in other tests.
   ```

### CLI (path + line range)

1. Start Codex: `codex`
2. Prompt with function name:
   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.
   ```

---

## Prototype from a screenshot

Design mock, screenshot, or UI reference → working prototype quickly.

### CLI (image + prompt)

1. Save screenshot locally (e.g., `./specs/ui.png`).
2. Run Codex: `codex`
3. Drag image into terminal to attach.
4. Follow up with constraints:
   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Deliverables:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally
   ```

Verification:
```text
Start the dev server and tell me the local URL/route to view the prototype.
```

### IDE extension (image + existing files)

1. Attach image in Codex chat (drag-and-drop or paste).
2. Prompt:
   ```text
   Create a new settings page. Use the attached screenshot as the target UI. Follow design and visual patterns from other files in this project.
   ```

---

## Iterate on UI with live updates

Tight "design → tweak → refresh → tweak" loop.

### CLI (run Vite, iterate with small prompts)

1. Start Codex: `codex`
2. Start dev server in separate terminal: `npm run dev`
3. Prompt:
   ```text
   Propose 2-3 styling improvements for the landing page.
   ```
4. Pick a direction and iterate:
   ```text
   Go with option 2.
   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile
   ```
5. Repeat with focused requests:
   ```text
   Next iteration: reduce visual noise. Keep the layout, but simplify colors and remove any redundant borders.
   ```

Verification: review in browser "live" as code updates. Commit changes you like; revert those you don't. Tell Codex about reverts so it doesn't overwrite them on the next prompt.

---

## Delegate refactor to the cloud

Design carefully locally, then outsource long implementation to a cloud task that runs in parallel.

### Local planning (IDE)

1. Make sure current work is committed or stashed.
2. Ask Codex to produce a refactor plan. If `$plan` skill available, invoke explicitly:
   ```text
   $plan
   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan
   ```
3. Review and negotiate:
   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy
   ```

### Cloud delegation (IDE → Cloud)

1. Set up a [[052-cloud-environments|Codex cloud environment]] if you haven't.
2. Click cloud icon beneath prompt composer and select your environment.
3. Next prompt creates a cloud thread carrying over existing context:
   ```text
   Implement Milestone 1 from the plan.
   ```
4. Review cloud diff, iterate if needed.
5. Create PR from cloud or pull changes locally to test and finish.
6. Iterate on additional milestones.

---

## Do a local code review

Second set of eyes before committing or creating a PR.

### CLI (review working tree)

1. Start Codex: `codex`
2. Run: `/review`
3. Optional custom focus:
   ```text
   /review Focus on edge cases and security issues
   ```

Verification: apply fixes, then rerun `/review` to confirm issues are resolved.

---

## Review a GitHub pull request

Review feedback without pulling the branch locally.

Prerequisite: enable Codex **Code review** on your repository. See [[026-integrations-github|Use Codex in GitHub]].

### GitHub workflow (comment-driven)

1. Open the pull request on GitHub.
2. Leave a comment:
   ```text
   @codex review
   ```
3. Optional explicit focus:
   ```text
   @codex review for security vulnerabilities and security concerns
   ```

---

## Update documentation

Doc change that is accurate and clear.

### IDE or CLI (local edits + validation)

1. Identify doc file(s) and open them (IDE) or `@` mention them.
2. Prompt with scope and validation:
   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.
   ```
3. Review and iterate.

Verification: read the rendered page.

#workflows #recipes #ide #cli #cloud #codex