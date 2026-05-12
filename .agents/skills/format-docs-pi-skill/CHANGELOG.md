# Changelog

All notable changes to format-docs-pi-skill. One line per change.

- 2026-05-02 — Initial pi-native skill. Targets the `tintinweb/pi-subagents` extension via the `Agent` tool (one agent per call, parallel by emitting multiple calls in the same turn with `run_in_background: true`). Custom agents in `.pi/agents/`: `format-docs-optimizer` (rewrite per file) and `format-docs-verifier` (Phase 5 fix). 10 scripts (setup, inventory, triage, siblings, plan_batches, apply_agent_results, sync_metadata, recalc_word_count, regenerate_index, verify), 2 references (`agent_prompt_pi.md` minimal per-batch prompt template; `agent_prompt.md` nested-agent fallback), 1 evals stub. Workflow: 6 phases (setup → triage → parallel optimize → metadata sync + word_count recalc → index regen → verify).
