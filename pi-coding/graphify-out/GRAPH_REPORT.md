# Graph Report - /home/diogo/dev/library-docs/pi-coding  (2026-05-03)

## Corpus Check
- Corpus is ~33,901 words - fits in a single context window. You may not need a graph.

## Summary
- 254 nodes · 226 edges · 33 communities detected
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_RPC Commands|RPC Commands]]
- [[_COMMUNITY_Keybindings & Configuration|Keybindings & Configuration]]
- [[_COMMUNITY_Extensions API|Extensions API]]
- [[_COMMUNITY_Agent Runtime SDK|Agent Runtime SDK]]
- [[_COMMUNITY_Message & Session Types|Message & Session Types]]
- [[_COMMUNITY_TUI Components|TUI Components]]
- [[_COMMUNITY_Custom Providers|Custom Providers]]
- [[_COMMUNITY_Termux Android Setup|Termux Android Setup]]
- [[_COMMUNITY_Pi Packages|Pi Packages]]
- [[_COMMUNITY_Session Management|Session Management]]
- [[_COMMUNITY_Themes System|Themes System]]
- [[_COMMUNITY_CLI Usage|CLI Usage]]
- [[_COMMUNITY_Documentation Index|Documentation Index]]
- [[_COMMUNITY_Development Setup|Development Setup]]
- [[_COMMUNITY_Prompt Templates|Prompt Templates]]
- [[_COMMUNITY_Quickstart|Quickstart]]
- [[_COMMUNITY_Quickstart Next Steps|Quickstart Next Steps]]
- [[_COMMUNITY_Termux Prerequisites|Termux Prerequisites]]
- [[_COMMUNITY_Termux Agent Setup|Termux Agent Setup]]
- [[_COMMUNITY_Extension UI Protocol|Extension UI Protocol]]
- [[_COMMUNITY_Read-only Mode|Read-only Mode]]
- [[_COMMUNITY_Termux Update|Termux Update]]
- [[_COMMUNITY_Termux Install Deps|Termux Install Deps]]
- [[_COMMUNITY_Termux Install Pi|Termux Install Pi]]
- [[_COMMUNITY_Termux Config Dir|Termux Config Dir]]
- [[_COMMUNITY_Interactive Initial Prompt|Interactive Initial Prompt]]
- [[_COMMUNITY_Non-interactive Usage|Non-interactive Usage]]
- [[_COMMUNITY_Piped Stdin|Piped Stdin]]
- [[_COMMUNITY_Different Model|Different Model]]
- [[_COMMUNITY_Provider Prefix|Provider Prefix]]
- [[_COMMUNITY_Thinking Shorthand|Thinking Shorthand]]
- [[_COMMUNITY_Model Cycling|Model Cycling]]
- [[_COMMUNITY_Display Queue|Display Queue]]

## God Nodes (most connected - your core abstractions)
1. `RPC Mode` - 54 edges
2. `SDK` - 18 edges
3. `Session File Format` - 18 edges
4. `004-extensions_Extensions` - 17 edges
5. `Keybindings` - 16 edges
6. `002-custom-provider_Custom Providers` - 11 edges
7. `008-termux_Agent Environment: Termux on Android` - 11 edges
8. `TUI Components` - 9 edges
9. `005-packages_Pi Packages` - 8 edges
10. `007-sessions_Sessions` - 8 edges

## Surprising Connections (you probably didn't know these)
- `TUI Components` --conceptually_related_to--> `Keybindings`  [INFERRED]
  026-tui.md → 021-keybindings.md
- `SDK` --conceptually_related_to--> `RPC Mode`  [INFERRED]
  024-sdk.md → 023-rpc.md
- `Session File Format` --conceptually_related_to--> `SDK`  [INFERRED]
  025-session-format.md → 024-sdk.md
- `Session File Format` --references--> `SessionManager`  [EXTRACTED]
  025-session-format.md → 024-sdk.md
- `Keybindings` --references--> `Pi Documentation`  [INFERRED]
  021-keybindings.md → 022-pi-documentation.md

## Communities

### Community 0 - "RPC Commands"
Cohesion: 0.04
Nodes (53): RPC Mode, abort command, abort_bash command, abort_retry command, bash command, clone command, compact command, cycle_model command (+45 more)

### Community 1 - "Keybindings & Configuration"
Cohesion: 0.09
Nodes (23): Keybindings, Pi Documentation, Application, Emacs Configuration Example, keybindings.json, Models and Thinking, Compaction, Development (+15 more)

### Community 2 - "Extensions API"
Cohesion: 0.11
Nodes (18): 004-extensions_Available Imports, 004-extensions_Custom Tools, 004-extensions_Custom UI, 004-extensions_Error Handling, 004-extensions_Events, 004-extensions_Example Use Cases, 004-extensions_Examples Reference, 004-extensions_Extension Locations (+10 more)

### Community 3 - "Agent Runtime SDK"
Cohesion: 0.12
Nodes (15): SDK, AgentSession, AgentSessionRuntime, AgentState, AuthStorage, followUp() method, InteractiveMode, ModelRegistry (+7 more)

### Community 4 - "Message & Session Types"
Cohesion: 0.12
Nodes (17): Session File Format, AgentMessage Union, Base Message Types, BranchSummaryEntry, CompactionEntry, Content Blocks, CustomEntry, CustomMessageEntry (+9 more)

### Community 5 - "TUI Components"
Cohesion: 0.13
Nodes (15): TUI Components, Background Colors, Built-in Components, Component Interface, CURSOR_MARKER, Editor Component, Foreground Colors, Focusable Interface (+7 more)

### Community 6 - "Custom Providers"
Cohesion: 0.17
Nodes (12): 002-custom-provider_API Types, 002-custom-provider_Config Reference, 002-custom-provider_Custom Providers, 002-custom-provider_Custom Streaming API, 002-custom-provider_Example Extensions, 002-custom-provider_Model Definition Reference, 002-custom-provider_OAuth Support, 002-custom-provider_Override Existing Provider (+4 more)

### Community 7 - "Termux Android Setup"
Cohesion: 0.17
Nodes (12): 008-termux_Agent Environment: Termux on Android, 008-termux_Clipboard, 008-termux_Device Info, 008-termux_Limitations, 008-termux_Location, 008-termux_Notes, 008-termux_Notifications, 008-termux_Opening Files (+4 more)

### Community 8 - "Pi Packages"
Cohesion: 0.22
Nodes (9): 005-packages_Creating a Pi Package, 005-packages_Dependencies, 005-packages_Enable and Disable Resources, 005-packages_Install and Manage, 005-packages_Package Filtering, 005-packages_Package Sources, 005-packages_Package Structure, 005-packages_Pi Packages (+1 more)

### Community 9 - "Session Management"
Cohesion: 0.22
Nodes (9): 007-sessions_Branch Summaries, 007-sessions_Branching with `/tree`, 007-sessions_Naming Sessions, 007-sessions_Resuming and Deleting Sessions, 007-sessions_Session Commands, 007-sessions_Session Format, 007-sessions_Session Storage, 007-sessions_Sessions (+1 more)

### Community 10 - "Themes System"
Cohesion: 0.22
Nodes (9): 009-themes_Color Tokens, 009-themes_Color Values, 009-themes_Creating a Custom Theme, 009-themes_Examples, 009-themes_Selecting a Theme, 009-themes_Theme Format, 009-themes_Theme Locations, 009-themes_Themes (+1 more)

### Community 11 - "CLI Usage"
Cohesion: 0.25
Nodes (8): 010-usage_CLI Reference, 010-usage_Context Files, 010-usage_Exporting and Sharing Sessions, 010-usage_Interactive Mode, 010-usage_Message Queue, 010-usage_Sessions, 010-usage_Slash Commands, 010-usage_Using Pi

### Community 12 - "Documentation Index"
Cohesion: 0.25
Nodes (8): pi-coding-agent Documentation Index, API, Concept, Configuration, Guide, Reference, Tutorial, Document Index

### Community 13 - "Development Setup"
Cohesion: 0.29
Nodes (7): 003-development_Debug Command, 003-development_Development, 003-development_Forking / Rebranding, 003-development_Path Resolution, 003-development_Project Structure, 003-development_Setup, 003-development_Testing

### Community 14 - "Prompt Templates"
Cohesion: 0.33
Nodes (6): 006-prompt-templates_Argument Hints, 006-prompt-templates_Arguments, 006-prompt-templates_Format, 006-prompt-templates_Locations, 006-prompt-templates_Prompt Templates, 006-prompt-templates_Usage

### Community 15 - "Quickstart"
Cohesion: 0.4
Nodes (5): 001-quickstart_Authenticate, 001-quickstart_First session, 001-quickstart_Give pi project instructions, 001-quickstart_Install, 001-quickstart_Quickstart

### Community 16 - "Quickstart Next Steps"
Cohesion: 0.67
Nodes (3): 001-quickstart_Common things to try, 001-quickstart_Next steps, 001-quickstart_Project Instructions

### Community 17 - "Termux Prerequisites"
Cohesion: 0.67
Nodes (3): 008-termux_Installation, 008-termux_Prerequisites, 008-termux_Termux (Android) Setup

### Community 18 - "Termux Agent Setup"
Cohesion: 0.67
Nodes (3): 008-termux_Clipboard Support, 008-termux_Example AGENTS.md, 008-termux_Run pi

### Community 19 - "Extension UI Protocol"
Cohesion: 0.67
Nodes (3): Extension UI Protocol, Extension UI Request, Extension UI Response

### Community 20 - "Read-only Mode"
Cohesion: 1.0
Nodes (2): 010-usage_Design Principles, 010-usage_Read-only mode

### Community 21 - "Termux Update"
Cohesion: 1.0
Nodes (1): 008-termux_Update packages

### Community 22 - "Termux Install Deps"
Cohesion: 1.0
Nodes (1): 008-termux_Install dependencies

### Community 23 - "Termux Install Pi"
Cohesion: 1.0
Nodes (1): 008-termux_Install pi

### Community 24 - "Termux Config Dir"
Cohesion: 1.0
Nodes (1): 008-termux_Create config directory

### Community 25 - "Interactive Initial Prompt"
Cohesion: 1.0
Nodes (1): 010-usage_Interactive with initial prompt

### Community 26 - "Non-interactive Usage"
Cohesion: 1.0
Nodes (1): 010-usage_Non-interactive

### Community 27 - "Piped Stdin"
Cohesion: 1.0
Nodes (1): 010-usage_Non-interactive with piped stdin

### Community 28 - "Different Model"
Cohesion: 1.0
Nodes (1): 010-usage_Different model

### Community 29 - "Provider Prefix"
Cohesion: 1.0
Nodes (1): 010-usage_Model with provider prefix

### Community 30 - "Thinking Shorthand"
Cohesion: 1.0
Nodes (1): 010-usage_Model with thinking level shorthand

### Community 31 - "Model Cycling"
Cohesion: 1.0
Nodes (1): 010-usage_Limit model cycling

### Community 32 - "Display Queue"
Cohesion: 1.0
Nodes (1): Display and Message Queue

## Knowledge Gaps
- **228 isolated node(s):** `001-quickstart_Install`, `001-quickstart_Authenticate`, `001-quickstart_First session`, `001-quickstart_Give pi project instructions`, `001-quickstart_Common things to try` (+223 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Read-only Mode`** (2 nodes): `010-usage_Design Principles`, `010-usage_Read-only mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Termux Update`** (1 nodes): `008-termux_Update packages`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Termux Install Deps`** (1 nodes): `008-termux_Install dependencies`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Termux Install Pi`** (1 nodes): `008-termux_Install pi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Termux Config Dir`** (1 nodes): `008-termux_Create config directory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Interactive Initial Prompt`** (1 nodes): `010-usage_Interactive with initial prompt`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Non-interactive Usage`** (1 nodes): `010-usage_Non-interactive`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Piped Stdin`** (1 nodes): `010-usage_Non-interactive with piped stdin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Different Model`** (1 nodes): `010-usage_Different model`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Provider Prefix`** (1 nodes): `010-usage_Model with provider prefix`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Thinking Shorthand`** (1 nodes): `010-usage_Model with thinking level shorthand`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Model Cycling`** (1 nodes): `010-usage_Limit model cycling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Display Queue`** (1 nodes): `Display and Message Queue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `RPC Mode` connect `RPC Commands` to `Agent Runtime SDK`, `Extension UI Protocol`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `SDK` connect `Agent Runtime SDK` to `RPC Commands`, `Message & Session Types`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Why does `Session File Format` connect `Message & Session Types` to `Agent Runtime SDK`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `SDK` (e.g. with `RPC Mode` and `Session File Format`) actually correct?**
  _`SDK` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Keybindings` (e.g. with `Pi Documentation` and `TUI Components`) actually correct?**
  _`Keybindings` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `001-quickstart_Install`, `001-quickstart_Authenticate`, `001-quickstart_First session` to the rest of the system?**
  _228 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `RPC Commands` be split into smaller, more focused modules?**
  _Cohesion score 0.04 - nodes in this community are weakly interconnected._