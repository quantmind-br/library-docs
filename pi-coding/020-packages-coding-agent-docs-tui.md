---
title: Tui
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/tui.md
source: git
fetched_at: 2026-04-26T05:48:41.637820934-03:00
rendered_js: false
word_count: 3338
optimized: true
optimized_at: 2026-04-26T09:00:00Z
summary: This document describes the component system for building interactive text user interfaces (TUI), covering component interfaces, IME support, overlay management, and available built-in UI elements.
tags:
    - tui
    - cli-framework
    - terminal-ui
    - typescript
    - ime-support
    - component-based-architecture
category: guide
---

# TUI Components

Extensions and custom tools render custom TUI components for interactive user interfaces.

**Source:** [`@mariozechner/pi-tui`](https://github.com/badlogic/pi-mono/tree/main/packages/tui)

## Component Interface

All components implement:

```typescript
interface Component {
  render(width: number): string[];
  handleInput?(data: string): void;
  wantsKeyRelease?: boolean;
  invalidate(): void;
}
```

| Method | Description |
|--------|-------------|
| `render(width)` | Return array of strings (one per line). Each line **must not exceed `width`**. |
| `handleInput?(data)` | Receive keyboard input when component has focus. |
| `wantsKeyRelease?` | If true, component receives key release events (Kitty protocol). Default: false. |
| `invalidate()` | Clear cached render state. Called on theme changes. |

> [!warning] Line styles reset between lines. The TUI appends a full SGR reset and OSC 8 reset at the end of each rendered line. Reapply styles per line or use `wrapTextWithAnsi()`.

## Focusable Interface (IME Support)

Components displaying a text cursor that need IME support should implement `Focusable`:

```typescript
import { CURSOR_MARKER, type Component, type Focusable } from "@mariozechner/pi-tui";

class MyInput implements Component, Focusable {
  focused: boolean = false;  // Set by TUI when focus changes
  
  render(width: number): string[] {
    const marker = this.focused ? CURSOR_MARKER : "";
    return [`> ${beforeCursor}${marker}\x1b[7m${atCursor}\x1b[27m${afterCursor}`];
  }
}
```

When a `Focusable` component has focus, TUI:

1. Sets `focused = true` on the component
2. Scans rendered output for `CURSOR_MARKER` (zero-width APC escape sequence)
3. Positions the hardware terminal cursor at that location
4. Shows the hardware cursor

> [!tip] `Editor` and `Input` built-in components already implement `Focusable`.

### Container Components with Embedded Inputs

Containers holding an `Input` or `Editor` child must implement `Focusable` and propagate focus state to the child for correct IME cursor positioning.

```typescript
import { Container, type Focusable, Input } from "@mariozechner/pi-tui";

class SearchDialog extends Container implements Focusable {
  private searchInput: Input;

  private _focused = false;
  get focused(): boolean { return this._focused; }
  set focused(value: boolean) {
    this._focused = value;
    this.searchInput.focused = value;
  }

  constructor() {
    super();
    this.searchInput = new Input();
    this.addChild(this.searchInput);
  }
}
```

> [!warning] Without focus propagation, IME candidate windows (CJK input) appear in the wrong position.

## Using Components

**In extensions** via `ctx.ui.custom()`:

```typescript
pi.on("session_start", async (_event, ctx) => {
  const handle = ctx.ui.custom(myComponent);
  // handle.requestRender() - trigger re-render
  // handle.close() - restore normal UI
});
```

**In custom tools** via `pi.ui.custom()`:

```typescript
async execute(toolCallId, params, onUpdate, ctx, signal) {
  const handle = pi.ui.custom(myComponent);
  // ...
  handle.close();
}
```

## Overlays

Overlays render on top of existing content without clearing the screen. Pass `{ overlay: true }` to `ctx.ui.custom()`:

```typescript
const result = await ctx.ui.custom<string | null>(
  (tui, theme, keybindings, done) => new MyDialog({ onClose: done }),
  { overlay: true }
);
```

For positioning and sizing, use `overlayOptions`:

```typescript
const result = await ctx.ui.custom<string | null>(
  (tui, theme, keybindings, done) => new SidePanel({ onClose: done }),
  {
    overlay: true,
    overlayOptions: {
      // Size: number or percentage string
      width: "50%",          // 50% of terminal width
      minWidth: 40,          // minimum 40 columns
      maxHeight: "80%",      // max 80% of terminal height

      // Position: anchor-based (default: "center")
      anchor: "right-center", // 9 positions: center, top-left, top-center, etc.
      offsetX: -2,
      offsetY: 0,

      // Or percentage/absolute positioning
      row: "25%",            // 25% from top
      col: 10,               // column 10

      // Margins
      margin: 2,             // all sides, or { top, right, bottom, left }

      // Responsive: hide on narrow terminals
      visible: (termWidth, termHeight) => termWidth >= 80,
    },
    onHandle: (handle) => {
      // handle.setHidden(true/false) - toggle visibility
      // handle.hide() - permanently remove
    },
  }
);
```

### Overlay Lifecycle

> [!warning] Overlay components are disposed when closed. Don't reuse references — create fresh instances.

```typescript
// Wrong - stale reference
let menu: MenuComponent;
await ctx.ui.custom((_, __, ___, done) => {
  menu = new MenuComponent(done);
  return menu;
}, { overlay: true });
setActiveComponent(menu);  // Disposed

// Correct - re-call to re-show
const showMenu = () => ctx.ui.custom((_, __, ___, done) => 
  new MenuComponent(done), { overlay: true });

await showMenu();  // First show
await showMenu();  // "Back" = just call again
```

See [overlay-qa-tests.ts](../examples/extensions/overlay-qa-tests.ts) for comprehensive examples.

## Built-in Components

Import from `@mariozechner/pi-tui`:

```typescript
import { Text, Box, Container, Spacer, Markdown } from "@mariozechner/pi-tui";
```

### Text

Multi-line text with word wrapping.

```typescript
const text = new Text(
  "Hello World",    // content
  1,                // paddingX (default: 1)
  1,                // paddingY (default: 1)
  (s) => bgGray(s)  // optional background function
);
text.setText("Updated");
```

### Box

Container with padding and background color.

```typescript
const box = new Box(
  1,                // paddingX
  1,                // paddingY
  (s) => bgGray(s)  // background function
);
box.addChild(new Text("Content", 0, 0));
box.setBgFn((s) => bgBlue(s));
```

### Container

Groups child components vertically.

```typescript
const container = new Container();
container.addChild(component1);
container.addChild(component2);
container.removeChild(component1);
```

### Spacer

```typescript
const spacer = new Spacer(2);  // 2 empty lines
```

### Markdown

Renders markdown with syntax highlighting.

```typescript
const md = new Markdown(
  "# Title\n\nSome **bold** text",
  1,        // paddingX
  1,        // paddingY
  theme     // MarkdownTheme (see below)
);
md.setText("Updated markdown");
```

### Image

Renders images in supported terminals (Kitty, iTerm2, Ghostty, WezTerm).

```typescript
const image = new Image(
  base64Data,   // base64-encoded image
  "image/png",  // MIME type
  theme,        // ImageTheme
  { maxWidthCells: 80, maxHeightCells: 24 }
);
```

## Keyboard Input

Use `matchesKey()` for key detection:

```typescript
import { matchesKey, Key } from "@mariozechner/pi-tui";

handleInput(data: string) {
  if (matchesKey(data, Key.up)) {
    this.selectedIndex--;
  } else if (matchesKey(data, Key.enter)) {
    this.onSelect?.(this.selectedIndex);
  } else if (matchesKey(data, Key.escape)) {
    this.onCancel?.();
  } else if (matchesKey(data, Key.ctrl("c"))) {
    // Ctrl+C
  }
}
```

**Key identifiers** (use `Key.*` for autocomplete, or string literals):

- Basic: `Key.enter`, `Key.escape`, `Key.tab`, `Key.space`, `Key.backspace`, `Key.delete`, `Key.home`, `Key.end`
- Arrow: `Key.up`, `Key.down`, `Key.left`, `Key.right`
- With modifiers: `Key.ctrl("c")`, `Key.shift("tab")`, `Key.alt("left")`, `Key.ctrlShift("p")`
- String format: `"enter"`, `"ctrl+c"`, `"shift+tab"`, `"ctrl+shift+p"`

## Line Width

> [!danger] Each line from `render()` must not exceed the `width` parameter.

```typescript
import { visibleWidth, truncateToWidth } from "@mariozechner/pi-tui";

render(width: number): string[] {
  return [truncateToWidth(this.text, width)];
}
```

| Utility | Description |
|---------|-------------|
| `visibleWidth(str)` | Display width (ignores ANSI codes) |
| `truncateToWidth(str, width, ellipsis?)` | Truncate with optional ellipsis |
| `wrapTextWithAnsi(str, width)` | Word wrap preserving ANSI codes |

## Creating Custom Components

Example: Interactive selector

```typescript
import {
  matchesKey, Key,
  truncateToWidth, visibleWidth
} from "@mariozechner/pi-tui";

class MySelector {
  private items: string[];
  private selected = 0;
  private cachedWidth?: number;
  private cachedLines?: string[];
  
  public onSelect?: (item: string) => void;
  public onCancel?: () => void;

  constructor(items: string[]) {
    this.items = items;
  }

  handleInput(data: string): void {
    if (matchesKey(data, Key.up) && this.selected > 0) {
      this.selected--;
      this.invalidate();
    } else if (matchesKey(data, Key.down) && this.selected < this.items.length - 1) {
      this.selected++;
      this.invalidate();
    } else if (matchesKey(data, Key.enter)) {
      this.onSelect?.(this.items[this.selected]);
    } else if (matchesKey(data, Key.escape)) {
      this.onCancel?.();
    }
  }

  render(width: number): string[] {
    if (this.cachedLines && this.cachedWidth === width) {
      return this.cachedLines;
    }

    this.cachedLines = this.items.map((item, i) => {
      const prefix = i === this.selected ? "> " : "  ";
      return truncateToWidth(prefix + item, width);
    });
    this.cachedWidth = width;
    return this.cachedLines;
  }

  invalidate(): void {
    this.cachedWidth = undefined;
    this.cachedLines = undefined;
  }
}
```

Usage in an extension:

```typescript
pi.registerCommand("pick", {
  description: "Pick an item",
  handler: async (args, ctx) => {
    const items = ["Option A", "Option B", "Option C"];
    const selector = new MySelector(items);
    
    let handle: { close: () => void; requestRender: () => void };
    
    await new Promise<void>((resolve) => {
      selector.onSelect = (item) => {
        ctx.ui.notify(`Selected: ${item}`, "info");
        handle.close();
        resolve();
      };
      selector.onCancel = () => {
        handle.close();
        resolve();
      };
      handle = ctx.ui.custom(selector);
    });
  }
});
```

## Theming

### Using Theme in renderCall/renderResult

```typescript
renderResult(result, options, theme, context) {
  return new Text(theme.fg("success", "Done!"), 0, 0);
  // Background: theme.bg("toolPendingBg", theme.fg("accent", "text"))
}
```

### Foreground Colors (`theme.fg(color, text)`)

| Category | Colors |
|----------|--------|
| General | `text`, `accent`, `muted`, `dim` |
| Status | `success`, `error`, `warning` |
| Borders | `border`, `borderAccent`, `borderMuted` |
| Messages | `userMessageText`, `customMessageText`, `customMessageLabel` |
| Tools | `toolTitle`, `toolOutput` |
| Diffs | `toolDiffAdded`, `toolDiffRemoved`, `toolDiffContext` |
| Markdown | `mdHeading`, `mdLink`, `mdLinkUrl`, `mdCode`, `mdCodeBlock`, `mdCodeBlockBorder`, `mdQuote`, `mdQuoteBorder`, `mdHr`, `mdListBullet` |
| Syntax | `syntaxComment`, `syntaxKeyword`, `syntaxFunction`, `syntaxVariable`, `syntaxString`, `syntaxNumber`, `syntaxType`, `syntaxOperator`, `syntaxPunctuation` |
| Thinking | `thinkingOff`, `thinkingMinimal`, `thinkingLow`, `thinkingMedium`, `thinkingHigh`, `thinkingXhigh` |
| Modes | `bashMode` |

### Background Colors (`theme.bg(color, text)`)

`selectedBg`, `userMessageBg`, `customMessageBg`, `toolPendingBg`, `toolSuccessBg`, `toolErrorBg`

### Markdown Theme

```typescript
import { getMarkdownTheme } from "@mariozechner/pi-coding-agent";
import { Markdown } from "@mariozechner/pi-tui";

renderResult(result, options, theme, context) {
  const mdTheme = getMarkdownTheme();
  return new Markdown(result.details.markdown, 0, 0, mdTheme);
}
```

### Custom Theme Interface

```typescript
interface MyTheme {
  selected: (s: string) => string;
  normal: (s: string) => string;
}
```

## Debug Logging

Set `PI_TUI_WRITE_LOG` to capture raw ANSI stream written to stdout:

```bash
PI_TUI_WRITE_LOG=/tmp/tui-ansi.log npx tsx packages/tui/test/chat-simple.ts
```

## Performance

Cache rendered output and call `invalidate()` on state changes, then `handle.requestRender()` to trigger re-render.

```typescript
class CachedComponent {
  private cachedWidth?: number;
  private cachedLines?: string[];

  render(width: number): string[] {
    if (this.cachedLines && this.cachedWidth === width) {
      return this.cachedLines;
    }
    // ... compute lines ...
    this.cachedWidth = width;
    this.cachedLines = lines;
    return lines;
  }

  invalidate(): void {
    this.cachedWidth = undefined;
    this.cachedLines = undefined;
  }
}
```

## Invalidation and Theme Changes

The TUI calls `invalidate()` on all components when the theme changes. Components that pre-bake theme colors into cached strings must rebuild content when invalidated.

### Anti-pattern (theme colors won't update)

```typescript
class BadComponent extends Container {
  private content: Text;

  constructor(message: string, theme: Theme) {
    super();
    // Pre-baked theme colors stored in Text component
    this.content = new Text(theme.fg("accent", message), 1, 0);
    this.addChild(this.content);
  }
  // No invalidate override - parent's invalidate only clears
  // child render caches, not the pre-baked content
}
```

### Correct pattern: rebuild on invalidate

```typescript
class GoodComponent extends Container {
  private message: string;
  private content: Text;

  constructor(message: string) {
    super();
    this.message = message;
    this.content = new Text("", 1, 0);
    this.addChild(this.content);
    this.updateDisplay();
  }

  private updateDisplay(): void {
    this.content.setText(theme.fg("accent", this.message));
  }

  override invalidate(): void {
    super.invalidate();
    this.updateDisplay();
  }
}
```

### Complex component pattern

```typescript
class ComplexComponent extends Container {
  private data: SomeData;

  constructor(data: SomeData) {
    super();
    this.data = data;
    this.rebuild();
  }

  private rebuild(): void {
    this.clear();  // Remove all children
    this.addChild(new Text(theme.fg("accent", theme.bold("Title")), 1, 0));
    this.addChild(new Spacer(1));
    for (const item of this.data.items) {
      const color = item.active ? "success" : "muted";
      this.addChild(new Text(theme.fg(color, item.label), 1, 0));
    }
  }

  override invalidate(): void {
    super.invalidate();
    this.rebuild();
  }
}
```

### When rebuild-on-invalidate is needed

- **Pre-baking theme colors** — using `theme.fg()`/`theme.bg()` to create styled strings stored in child components
- **Syntax highlighting** — using `highlightCode()` which applies theme-based syntax colors
- **Complex layouts** — building child component trees that embed theme colors

> [!tip] NOT needed when: using theme callbacks passed as functions, simple containers without themed content, or stateless `render()` that computes fresh every call.

## Common Patterns

> [!tip] Copy these patterns instead of building from scratch. `SelectList`, `SettingsList`, `BorderedLoader` cover 90% of cases.

### Pattern 1: Selection Dialog (SelectList)

Let users pick from a list. Use `SelectList` from `@mariozechner/pi-tui` with `DynamicBorder` for framing.

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { DynamicBorder } from "@mariozechner/pi-coding-agent";
import { Container, type SelectItem, SelectList, Text } from "@mariozechner/pi-tui";

pi.registerCommand("pick", {
  handler: async (_args, ctx) => {
    const items: SelectItem[] = [
      { value: "opt1", label: "Option 1", description: "First option" },
      { value: "opt2", label: "Option 2", description: "Second option" },
      { value: "opt3", label: "Option 3" },  // description is optional
    ];

    const result = await ctx.ui.custom<string | null>((tui, theme, _kb, done) => {
      const container = new Container();

      // Top border
      container.addChild(new DynamicBorder((s: string) => theme.fg("accent", s)));

      // Title
      container.addChild(new Text(theme.fg("accent", theme.bold("Pick an Option")), 1, 0));

      // SelectList with theme
      const selectList = new SelectList(items, Math.min(items.length, 10), {
        selectedPrefix: (t) => theme.fg("accent", t),
        selectedText: (t) => theme.fg("accent", t),
        description: (t) => theme.fg("muted", t),
        scrollInfo: (t) => theme.fg("dim", t),
        noMatch: (t) => theme.fg("warning", t),
      });
      selectList.onSelect = (item) => done(item.value);
      selectList.onCancel = () => done(null);
      container.addChild(selectList);

      // Help text
      container.addChild(new Text(theme.fg("dim", "↑↓ navigate • enter select • esc cancel"), 1, 0));

      // Bottom border
      container.addChild(new DynamicBorder((s: string) => theme.fg("accent", s)));

      return {
        render: (w) => container.render(w),
        invalidate: () => container.invalidate(),
        handleInput: (data) => { selectList.handleInput(data); tui.requestRender(); },
      };
    });

    if (result) {
      ctx.ui.notify(`Selected: ${result}`, "info");
    }
  },
});
```

**Examples:** [preset.ts](../examples/extensions/preset.ts), [tools.ts](../examples/extensions/tools.ts)

### Pattern 2: Async Operation with Cancel (BorderedLoader)

Cancellable operations with spinner. `BorderedLoader` handles escape to cancel.

```typescript
import { BorderedLoader } from "@mariozechner/pi-coding-agent";

pi.registerCommand("fetch", {
  handler: async (_args, ctx) => {
    const result = await ctx.ui.custom<string | null>((tui, theme, _kb, done) => {
      const loader = new BorderedLoader(tui, theme, "Fetching data...");
      loader.onAbort = () => done(null);

      fetchData(loader.signal)
        .then((data) => done(data))
        .catch(() => done(null));

      return loader;
    });

    if (result === null) {
      ctx.ui.notify("Cancelled", "info");
    } else {
      ctx.ui.setEditorText(result);
    }
  },
});
```

**Examples:** [qna.ts](../examples/extensions/qna.ts), [handoff.ts](../examples/extensions/handoff.ts)

### Pattern 3: Settings/Toggles (SettingsList)

Toggle multiple settings. Use `SettingsList` from `@mariozechner/pi-tui` with `getSettingsListTheme()`.

```typescript
import { getSettingsListTheme } from "@mariozechner/pi-coding-agent";
import { Container, type SettingItem, SettingsList, Text } from "@mariozechner/pi-tui";

pi.registerCommand("settings", {
  handler: async (_args, ctx) => {
    const items: SettingItem[] = [
      { id: "verbose", label: "Verbose mode", currentValue: "off", values: ["on", "off"] },
      { id: "color", label: "Color output", currentValue: "on", values: ["on", "off"] },
    ];

    await ctx.ui.custom((_tui, theme, _kb, done) => {
      const container = new Container();
      container.addChild(new Text(theme.fg("accent", theme.bold("Settings")), 1, 1));

      const settingsList = new SettingsList(
        items,
        Math.min(items.length + 2, 15),
        getSettingsListTheme(),
        (id, newValue) => {
          ctx.ui.notify(`${id} = ${newValue}`, "info");
        },
        () => done(undefined),
        { enableSearch: true }, // Optional: enable fuzzy search by label
      );
      container.addChild(settingsList);

      return {
        render: (w) => container.render(w),
        invalidate: () => container.invalidate(),
        handleInput: (data) => settingsList.handleInput?.(data),
      };
    });
  },
});
```

**Examples:** [tools.ts](../examples/extensions/tools.ts)

### Pattern 4: Persistent Status Indicator

Show status in the footer that persists across renders.

```typescript
// Set status (shown in footer)
ctx.ui.setStatus("my-ext", ctx.ui.theme.fg("accent", "● active"));

// Clear status
ctx.ui.setStatus("my-ext", undefined);
```

**Examples:** [status-line.ts](../examples/extensions/status-line.ts), [plan-mode.ts](../examples/extensions/plan-mode.ts), [preset.ts](../examples/extensions/preset.ts)

### Pattern 4b: Working Indicator Customization

Customize the inline working indicator shown while pi is streaming a response.

```typescript
// Static indicator
ctx.ui.setWorkingIndicator({ frames: [ctx.ui.theme.fg("accent", "●")] });

// Custom animated indicator
ctx.ui.setWorkingIndicator({
  frames: [
    ctx.ui.theme.fg("dim", "·"),
    ctx.ui.theme.fg("muted", "•"),
    ctx.ui.theme.fg("accent", "●"),
    ctx.ui.theme.fg("muted", "•"),
  ],
  intervalMs: 120,
});

// Hide the indicator entirely
ctx.ui.setWorkingIndicator({ frames: [] });

// Restore pi's default spinner
ctx.ui.setWorkingIndicator();
```

> [!note] This only affects the normal streaming working indicator. Compaction and retry loaders keep their built-in styling. Custom frames render verbatim — extensions must add their own colors.

**Examples:** [working-indicator.ts](../examples/extensions/working-indicator.ts)

### Pattern 5: Widgets Above/Below Editor

Show persistent content above or below the input editor.

```typescript
// Simple string array (above editor by default)
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"]);

// Render below the editor
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"], { placement: "belowEditor" });

// Or with theme
ctx.ui.setWidget("my-widget", (_tui, theme) => {
  const lines = items.map((item, i) =>
    item.done
      ? theme.fg("success", "✓ ") + theme.fg("muted", item.text)
      : theme.fg("dim", "○ ") + item.text
  );
  return {
    render: () => lines,
    invalidate: () => {},
  };
});

// Clear
ctx.ui.setWidget("my-widget", undefined);
```

**Examples:** [plan-mode.ts](../examples/extensions/plan-mode.ts)

### Pattern 6: Custom Footer

Replace the footer. `footerData` exposes data not otherwise accessible to extensions.

```typescript
ctx.ui.setFooter((tui, theme, footerData) => ({
  invalidate() {},
  render(width: number): string[] {
    // footerData.getGitBranch(): string | null
    // footerData.getExtensionStatuses(): ReadonlyMap<string, string>
    return [`${ctx.model?.id} (${footerData.getGitBranch() || "no git"})`];
  },
  dispose: footerData.onBranchChange(() => tui.requestRender()), // reactive
}));

ctx.ui.setFooter(undefined); // restore default
```

Token stats available via `ctx.sessionManager.getBranch()` and `ctx.model`.

**Examples:** [custom-footer.ts](../examples/extensions/custom-footer.ts)

### Pattern 7: Custom Editor (vim mode, etc.)

Replace the main input editor for modal editing (vim), different keybindings (emacs), or specialized input handling.

```typescript
import { CustomEditor, type ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { matchesKey, truncateToWidth } from "@mariozechner/pi-tui";

type Mode = "normal" | "insert";

class VimEditor extends CustomEditor {
  private mode: Mode = "insert";

  handleInput(data: string): void {
    // Escape: switch to normal mode, or pass through for app handling
    if (matchesKey(data, "escape")) {
      if (this.mode === "insert") {
        this.mode = "normal";
        return;
      }
      // In normal mode, escape aborts agent (handled by CustomEditor)
      super.handleInput(data);
      return;
    }

    // Insert mode: pass everything to CustomEditor
    if (this.mode === "insert") {
      super.handleInput(data);
      return;
    }

    // Normal mode: vim-style navigation
    switch (data) {
      case "i": this.mode = "insert"; return;
      case "h": super.handleInput("\x1b[D"); return; // Left
      case "j": super.handleInput("\x1b[B"); return; // Down
      case "k": super.handleInput("\x1b[A"); return; // Up
      case "l": super.handleInput("\x1b[C"); return; // Right
    }
    // Pass unhandled keys to super (ctrl+c, etc.), but filter printable chars
    if (data.length === 1 && data.charCodeAt(0) >= 32) return;
    super.handleInput(data);
  }

  render(width: number): string[] {
    const lines = super.render(width);
    // Add mode indicator to bottom border (use truncateToWidth for ANSI-safe truncation)
    if (lines.length > 0) {
      const label = this.mode === "normal" ? " NORMAL " : " INSERT ";
      const lastLine = lines[lines.length - 1]!;
      // Pass "" as ellipsis to avoid adding "..." when truncating
      lines[lines.length - 1] = truncateToWidth(lastLine, width - label.length, "") + label;
    }
    return lines;
  }
}

export default function (pi: ExtensionAPI) {
  pi.on("session_start", (_event, ctx) => {
    // Factory receives theme and keybindings from the app
    ctx.ui.setEditorComponent((tui, theme, keybindings) =>
      new VimEditor(theme, keybindings)
    );
  });
}
```

Key points:

- **Extend `CustomEditor`** (not base `Editor`) to get app keybindings (escape to abort, ctrl+d to exit, model switching, etc.)
- **Call `super.handleInput(data)`** for keys you don't handle
- **Factory pattern**: `setEditorComponent` receives a factory function that gets `tui`, `theme`, and `keybindings`
- **Pass `undefined`** to restore the default editor: `ctx.ui.setEditorComponent(undefined)`

**Examples:** [modal-editor.ts](../examples/extensions/modal-editor.ts)

## Key Rules

1. **Always use theme from callback** — use `theme` from `ctx.ui.custom((tui, theme, keybindings, done) => ...)`, don't import directly.
2. **Always type DynamicBorder color param** — write `(s: string) => theme.fg("accent", s)`, not `(s) => theme.fg("accent", s)`.
3. **Call `tui.requestRender()` after state changes** — in `handleInput`, call after updating state.
4. **Return the three-method object** — custom components need `{ render, invalidate, handleInput }`.
5. **Use existing components** — `SelectList`, `SettingsList`, `BorderedLoader` cover 90% of cases.

## Examples

- **Selection UI**: [examples/extensions/preset.ts](../examples/extensions/preset.ts) - SelectList with DynamicBorder framing
- **Async with cancel**: [examples/extensions/qna.ts](../examples/extensions/qna.ts) - BorderedLoader for LLM calls
- **Settings toggles**: [examples/extensions/tools.ts](../examples/extensions/tools.ts) - SettingsList for tool enable/disable
- **Status indicators**: [examples/extensions/plan-mode.ts](../examples/extensions/plan-mode.ts) - setStatus and setWidget
- **Working indicator**: [examples/extensions/working-indicator.ts](../examples/extensions/working-indicator.ts) - setWorkingIndicator
- **Custom footer**: [examples/extensions/custom-footer.ts](../examples/extensions/custom-footer.ts) - setFooter with stats
- **Custom editor**: [examples/extensions/modal-editor.ts](../examples/extensions/modal-editor.ts) - Vim-like modal editing
- **Snake game**: [examples/extensions/snake.ts](../examples/extensions/snake.ts) - Full game with keyboard input, game loop
- **Custom tool rendering**: [examples/extensions/todo.ts](../examples/extensions/todo.ts) - renderCall and renderResult

#tui #component-based-architecture #ime-support #terminal-ui #typescript
