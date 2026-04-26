---
title: Tree
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/tree.md
source: git
fetched_at: 2026-04-26T05:48:39.762689236-03:00
rendered_js: false
word_count: 1100
summary: This document explains the functionality of the tree-based session navigation system, including UI controls for branch traversal, branch summarization logic, and the technical implementation of session navigation hooks.
tags:
    - session-management
    - tree-navigation
    - branching
    - summarization
    - user-interface
    - hook-events
    - development-guide
category: guide
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Session Tree Navigation

The `/tree` command provides tree-based navigation of session history. Sessions are stored as trees where each entry has an `id` and `parentId`. A "leaf" pointer tracks current position. Navigate to any point and optionally summarize the branch you leave.

## Comparison with `/fork`

| Feature | `/fork` | `/tree` |
|---------|---------|---------|
| View | Flat list of user messages | Full tree structure |
| Action | Extracts path to **new session file** | Changes leaf in **same session** |
| Summary | Never | Optional (user prompted) |
| Events | `session_before_fork` / `session_start` (`reason: "fork"`) | `session_before_tree` / `session_tree` |

> [!tip] Use `/clone` when you want a new session file containing the full current active branch without rewinding to an earlier user message.

## Tree UI

```
├─ user: "Hello, can you help..."
│  └─ assistant: "Of course! I can..."
│     ├─ user: "Let's try approach A..."
│     │  └─ assistant: "For approach A..."
│     │     └─ [compaction: 12k tokens]
│     │        └─ user: "That worked..."  ← active
│     └─ user: "Actually, approach B..."
│        └─ assistant: "For approach B..."
```

### Controls

| Key | Action |
|-----|--------|
| Up/Down | Navigate (depth-first order) |
| Left/Right | Page up/down |
| Ctrl+Left/Ctrl+Right or Alt+Left/Alt+Right | Fold/unfold and jump between branch segments |
| Shift+L | Set or clear a label on the selected node |
| Shift+T | Toggle label timestamps |
| Enter | Select node |
| Escape/Ctrl+C | Cancel |
| Ctrl+U | Toggle: user messages only |
| Ctrl+O | Toggle: show all (including custom/label entries) |

**Fold/unfold behavior:**
- `Ctrl+Left` / `Alt+Left`: folds the current node if foldable (roots and branch segment starts with visible children). If not foldable or already folded, jumps up to the previous visible branch segment start.
- `Ctrl+Right` / `Alt+Right`: unfolds the current node if folded. Otherwise jumps down to the next visible branch segment start, or to the branch end if no further branch point.

### Display

- Height: half terminal height
- Current leaf: marked with `← active`
- Labels: shown inline as `[label-name]`; `Shift+T` shows latest label-change timestamp
- Foldable branch starts: `⊟` in connector; folded branches: `⊞`
- Active path marker `•` appears after fold indicator when applicable
- Search/filter changes reset all folds
- Default filter hides `label` and `custom` entries (shown in Ctrl+O mode)
- At each branch point: active subtree shown first; sibling branches sorted by timestamp (oldest first)

## Selection Behavior

### User Message or Custom Message

1. Leaf set to **parent** of selected node (or `null` if root)
2. Message text placed in **editor** for re-submission
3. User edits and submits, creating a new branch

### Non-User Message (assistant, compaction, etc.)

1. Leaf set to **selected node**
2. Editor stays empty
3. User continues from that point

### Selecting Root User Message

1. Leaf reset to `null` (empty conversation)
2. Message text placed in editor
3. User effectively restarts from scratch

## Branch Summarization

When switching branches, three options:

1. **No summary** — switch immediately
2. **Summarize** — generate summary using default prompt
3. **Summarize with custom prompt** — opens editor for additional focus instructions appended to default prompt

### What Gets Summarized

Path from old leaf back to common ancestor with target:

```
A → B → C → D → E → F  ← old leaf
        ↘ G → H        ← target
```

Abandoned path: D → E → F (summarized). Summarization stops at:
1. Common ancestor (always)
2. Compaction node (if encountered first)

### Summary Storage

Stored as `BranchSummaryEntry`:

```typescript
interface BranchSummaryEntry {
  type: "branch_summary";
  id: string;
  parentId: string;      // New leaf position
  timestamp: string;
  fromId: string;        // Old leaf we abandoned
  summary: string;       // LLM-generated summary
  details?: unknown;     // Optional hook data
}
```

## Implementation

### AgentSession.navigateTree()

```typescript
async navigateTree(
  targetId: string,
  options?: {
    summarize?: boolean;
    customInstructions?: string;
    replaceInstructions?: boolean;
    label?: string;
  }
): Promise<{ editorText?: string; cancelled: boolean }>
```

| Option | Description |
|--------|-------------|
| `summarize` | Whether to generate a summary of the abandoned branch |
| `customInstructions` | Custom instructions for the summarizer |
| `replaceInstructions` | If true, `customInstructions` replaces the default prompt instead of being appended |
| `label` | Label to attach to the branch summary entry (or target entry if not summarizing) |

**Flow:**
1. Validate target; check no-op (target === current leaf)
2. Find common ancestor between old leaf and target
3. Collect entries to summarize (if requested)
4. Fire `session_before_tree` event (hook can cancel or provide summary)
5. Run default summarizer if needed
6. Switch leaf via `branch()` or `branchWithSummary()`
7. Update agent: `agent.state.messages = sessionManager.buildSessionContext().messages`
8. Fire `session_tree` event
9. Notify custom tools via session event
10. Return result with `editorText` if user message was selected

### SessionManager

- **`getLeafUuid(): string | null`** — current leaf (null if empty)
- **`resetLeaf(): void`** — set leaf to null (for root user message navigation)
- **`getTree(): SessionTreeNode[]`** — full tree with children sorted by timestamp
- **`branch(id)`** — change leaf pointer
- **`branchWithSummary(id, summary)`** — change leaf and create summary entry

### InteractiveMode

`/tree` command shows `TreeSelectorComponent`, then: prompt for summarization, call `session.navigateTree()`, clear and re-render chat, set editor text if applicable.

## Hook Events

### `session_before_tree`

```typescript
interface TreePreparation {
  targetId: string;
  oldLeafId: string | null;
  commonAncestorId: string | null;
  entriesToSummarize: SessionEntry[];
  userWantsSummary: boolean;
  customInstructions?: string;
  replaceInstructions?: boolean;
  label?: string;
}

interface SessionBeforeTreeEvent {
  type: "session_before_tree";
  preparation: TreePreparation;
  signal: AbortSignal;
}

interface SessionBeforeTreeResult {
  cancel?: boolean;
  summary?: { summary: string; details?: unknown };
  customInstructions?: string;    // Override custom instructions
  replaceInstructions?: boolean;  // Override replace mode
  label?: string;                 // Override label
}
```

Extensions can override `customInstructions`, `replaceInstructions`, and `label` by returning them from the handler.

### `session_tree`

```typescript
interface SessionTreeEvent {
  type: "session_tree";
  newLeafId: string | null;
  oldLeafId: string | null;
  summaryEntry?: BranchSummaryEntry;
  fromHook?: boolean;
}
```

### Example: Custom Summarizer

```typescript
export default function(pi: HookAPI) {
  pi.on("session_before_tree", async (event, ctx) => {
    if (!event.preparation.userWantsSummary) return;
    if (event.preparation.entriesToSummarize.length === 0) return;
    
    const summary = await myCustomSummarizer(event.preparation.entriesToSummarize);
    return { summary: { summary, details: { custom: true } } };
  });
}
```

## Error Handling

| Scenario | Result |
|----------|--------|
| Summarization failure | Cancels navigation, shows error |
| User abort (Escape) | Cancels navigation |
| Hook returns `cancel: true` | Cancels navigation silently |

#session-management #tree-navigation #branching #summarization #hook-events #user-interface
