---
description: Auto-generated documentation index for oh-my-pi
generated: 2026-03-10T09:30:00-03:00
source: https://github.com/can1357/oh-my-pi
total_docs: 49
categories: 10
---

# oh-my-pi Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://github.com/can1357/oh-my-pi |
| **Generated** | 2026-03-10T09:30:00-03:00 |
| **Total Documents** | 49 |
| **Categories** | Core Architecture, Configuration, Extensions & MCP, Tools & Execution, Session Management, Storage & Artifacts, Natives (Rust), UI & Skills, Integrations & Security, Advanced & Porting |

---

## Document Index

### 1. Core Architecture & Concepts (001-005)

*Foundational architecture and core concepts of the oh-my-pi coding agent.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-docs-natives-architecture.md` | Natives architecture | Three-layer architecture: TypeScript wrapper, runtime addon layer, Rust N-API | architecture, natives, n-api, rust |
| 002 | `002-docs-session.md` | Session | JSONL format, taxonomy, persistence, versioning for coding-agent sessions | session-storage, jsonl, migration |
| 003 | `003-docs-tui.md` | Tui | TUI contract for rendering engine and extensions | tui, component-contract, terminal |
| 004 | `004-docs-sdk.md` | Sdk | `@oh-my-pi/pi-coding-agent` SDK structure and usage | sdk, in-process, session-management |
| 005 | `005-docs-rpc.md` | Rpc | RPC protocol over JSONL on stdio | rpc, jsonl, stdio, command-schema |

### 2. Configuration & Setup (006-010)

*Configuration management, models, environment variables, and theme setup.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-docs-models.md` | Models | `models.yml` structure, provider config, authentication | models-yml, provider, model-resolution |
| 007 | `007-docs-config-usage.md` | Config usage | Configuration resolution, precedence, scanning order | configuration, resolution-flow, precedence |
| 008 | `008-docs-environment-variables.md` | Environment variables | Runtime env vars for providers and authentication | env-variables, runtime-config, api-auth |
| 009 | `009-docs-extension-loading.md` | Extension loading | Extension module discovery, resolution, import | extension-loading, module-resolution |
| 010 | `010-docs-theme.md` | Theme | Theming system, color tokens, JSON schema | theming, color-tokens, json-schema |

### 3. Extensions & MCP (011-016)

*Extensions, hooks, MCP protocol, and runtime lifecycle.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 011 | `011-docs-extensions.md` | Extensions | Authoring runtime extensions, lifecycle, API surfaces | extension-development, runtime-model |
| 012 | `012-docs-hooks.md` | Hooks | Hook subsystem implementation, event surfaces | hooks, extensibility, event-lifecycle |
| 013 | `013-docs-mcp-protocol-transports.md` | Mcp protocol transports | MCP JSON-RPC, transport layer (stdio, HTTP/SSE) | mcp-protocol, json-rpc, transport |
| 014 | `014-docs-mcp-runtime-lifecycle.md` | Mcp runtime lifecycle | MCP server lifecycle: discovery, connection, teardown | mcp, server-lifecycle, tool-discovery |
| 015 | `015-docs-mcp-server-tool-authoring.md` | Mcp server tool authoring | MCP server loading, validation, exposure as tools | mcp-server, tool-authoring |
| 016 | `016-docs-gemini-manifest-extensions.md` | Gemini manifest extensions | Gemini-style manifest discovery, capability items | gemini, manifest, extension-discovery |

### 4. Tools & Execution (017-022)

*Custom tools, task agents, bash, notebook, Python REPL, and resolve tools.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 017 | `017-docs-custom-tools.md` | Custom tools | Define and integrate custom tools with factory pattern | custom-tools, factory-pattern, tool-execution |
| 018 | `018-docs-task-agent-discovery.md` | Task agent discovery | Task subsystem: agent discovery, merging, availability | agent-discovery, task-subsystem |
| 019 | `019-docs-bash-tool-runtime.md` | Bash tool runtime | Bash tool execution flow, PTY, input normalization | bash-tool, pty-execution, runtime-path |
| 020 | `020-docs-notebook-tool-runtime.md` | Notebook tool runtime | Notebook tool as JSON editor for .ipynb files | notebook-tool, json-editing, ipython |
| 021 | `021-docs-python-repl.md` | Python repl | Python execution via Jupyter Kernel Gateway | python-tool, kernel-gateway, session-persistence |
| 022 | `022-docs-resolve-tool-runtime.md` | Resolve tool runtime | Preview/apply workflows, pending actions | resolve-tool, preview-apply, pending-actions |

### 5. Session Management (023-028)

*Session tree, switching, operations, compaction, retry policy, and memory.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 023 | `023-docs-session-tree-plan.md` | Session tree plan | In-memory session tree, append-only log, leaf movement | session-tree, tree-structure, branching |
| 024 | `024-docs-session-switching-and-recent-listing.md` | Session switching and recent listing | Session discovery, listing, selection, resume | session-management, runtime-switching |
| 025 | `025-docs-session-operations-export-share-fork-resume.md` | Session operations | Export, dump, share, fork, resume sessions | session-management, export, fork, resume |
| 026 | `026-docs-compaction.md` | Compaction | Branch summary, history rewriting, context maintenance | compaction, branch-summary, pruning |
| 027 | `027-docs-non-compaction-retry-policy.md` | Non compaction retry policy | Auto-retry for API errors, backoff, lifecycle | auto-retry, api-error-handling, backoff |
| 028 | `028-docs-memory.md` | Memory | Autonomous Memory: knowledge extraction, consolidation | autonomous-memory, knowledge-retention |

### 6. Storage & Artifacts (029-030)

*Blob storage, artifacts, and filesystem caching.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 029 | `029-docs-blob-artifact-architecture.md` | Blob artifact architecture | Dual storage: blobs for binary, artifacts for session outputs | blob-storage, artifact-storage, url-resolution |
| 030 | `030-docs-fs-scan-cache-architecture.md` | Fs scan cache architecture | Rust filesystem scan cache, invalidation, freshness | filesystem-cache, rust, api-contract |

### 7. Natives (Rust) (031-037)

*Native Rust modules, addons, bindings, and system utilities.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 031 | `031-docs-natives-addon-loader-runtime.md` | Natives addon loader runtime | Loading, validating, platform detection for native addons | addon-loading, native-bindings |
| 032 | `032-docs-natives-binding-contract.md` | Natives binding contract | TypeScript contract, N-API wrapper, public exports | native-bindings, typescript-contract, n-api |
| 033 | `033-docs-natives-build-release-debugging.md` | Natives build release debugging | Build, release, debug native Node.js addons | native-addons, build-pipeline, cargo, rust |
| 034 | `034-docs-natives-media-system-utils.md` | Natives media system utils | Image processing, HTML conversion, clipboard, work profiling | system-utilities, image-conversion, clipboard |
| 035 | `035-docs-natives-rust-task-cancellation.md` | Natives rust task cancellation | Rust task scheduling, CancelToken, signal propagation | rust, napi, task-scheduling, cancellation |
| 036 | `036-docs-natives-shell-pty-process.md` | Natives shell pty process | Shell, PTY, process tree, key parsing primitives | shell, pty, process-management |
| 037 | `037-docs-natives-text-search-pipeline.md` | Natives text search pipeline | TypeScript/Rust bindings for grep, glob, text search | natives, grep, glob, fs-cache |

### 8. UI & Skills (038-041)

*TUI internals, skills system, slash commands, and handoff.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 038 | `038-docs-tui-runtime-internals.md` | Tui runtime internals | TUI internal architecture, input handling, render loop | tui, runtime, input-handling |
| 039 | `039-docs-skills.md` | Skills | Skills: file-backed capability packs, discovery pipeline | skills, capability-packs, skill-protocol |
| 040 | `040-docs-slash-command-internals.md` | Slash command internals | Slash command discovery, deduplication, precedence | slash-commands, command-discovery |
| 041 | `041-docs-handoff-generation-pipeline.md` | Handoff generation pipeline | `/handoff` command: trigger, context, session switch | handoff-pipeline, context-injection |

### 9. Integrations & Security (042-044)

*Provider streaming, plugin management, and secrets.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 042 | `042-docs-provider-streaming-internals.md` | Provider streaming internals | Token/tool streaming from Anthropic, OpenAI, Google | streaming, provider-normalization |
| 043 | `043-docs-plugin-manager-installer-plumbing.md` | Plugin manager installer plumbing | Plugin management, disk state, runtime loading | plugin-management, pluginmanager |
| 044 | `044-docs-secrets.md` | Secrets | Secret obfuscation, API key protection | secrets-management, obfuscation |

### 10. Advanced & Porting (045-049)

*Porting guides, rulebook, TTSR, and tree navigation.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 045 | `045-docs-porting-from-pi-mono.md` | Porting from pi mono | Porting from pi-mono, Bun migration, API replacement | porting, merge-guide, bun-migration |
| 046 | `046-docs-porting-to-natives.md` | Porting to natives | Porting JS to Rust N-API, performance, benchmarking | n-api, rust, porting, native-bindings |
| 047 | `047-docs-rulebook-matching-pipeline.md` | Rulebook matching pipeline | Rule discovery, normalization, TTSR sets | rule-discovery, configuration-normalization |
| 048 | `048-docs-ttsr-injection-lifecycle.md` | Ttsr injection lifecycle | TTSR lifecycle: discovery, monitoring, injection | ttsr, stream-rules, rule-injection |
| 049 | `049-docs-tree.md` | Tree | `/tree` command: Session Tree navigator | session-tree, navigation, branching |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Natives/Rust** | 001, 031-037 |
| **Session Management** | 002, 023-028 |
| **MCP** | 013-016 |
| **Extensions** | 011-012, 016 |
| **Tools** | 017-022 |
| **TUI** | 003, 038 |
| **Configuration** | 006-010 |
| **Skills** | 039-041 |
| **Storage** | 029-030 |
| **Security** | 042-044 |
| **Porting** | 045-046 |

### By Category Type

| Category | Files |
|----------|-------|
| **Reference** | 001-005, 008, 010, 012-016, 019-021, 023-026, 029-032, 034-037, 039-040, 042-043, 047, 049 |
| **Guide/How-To** | 003, 007, 009, 011, 017-018, 022, 027-028, 033, 038, 041, 044-046, 048 |
| **Configuration** | 006-010 |
| **Concept** | 001 |

---

## Learning Path

### Level 1: Foundation (001-010)
- Read **001** for natives architecture overview
- Understand **002** session storage format
- Learn **003** TUI contract basics
- Explore **004** SDK structure
- Study **005** RPC protocol
- Configure with **006-010**: models, config, env vars, extensions, theme

### Level 2: Core Understanding (011-022)
- Master extensions **011-016**: extensions, hooks, MCP protocol/lifecycle/tool authoring, Gemini manifests
- Learn tools **017-022**: custom tools, task agents, bash, notebook, Python REPL, resolve

### Level 3: Practical Application (023-037)
- Session management **023-028**: tree, switching, operations, compaction, retry, memory
- Storage **029-030**: blob artifacts, filesystem cache
- Native modules **031-037**: addon loader, binding contract, build/debug, media utils, task cancellation, shell/PTY, text search

### Level 4: Advanced Usage (038-044)
- UI internals **038**: TUI runtime
- Skills system **039-041**: skills, slash commands, handoff
- Integrations **042-044**: provider streaming, plugins, secrets

### Level 5: Expert Topics (045-049)
- Porting **045-046**: from pi-mono, to natives
- Advanced rules **047-048**: rulebook matching, TTSR
- Navigation **049**: tree command

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the documentation structure.*