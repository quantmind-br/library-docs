---
title: Keybindings
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/keybindings.md
source: git
fetched_at: 2026-05-03T09:31:12.590045432-03:00
rendered_js: false
word_count: 973
summary: This document provides a comprehensive reference for configuring and utilizing keyboard shortcuts within the pi agent terminal interface.
tags:
    - keybindings
    - configuration
    - tui
    - shortcuts
    - editor-settings
    - productivity
category: reference
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Keybindings

Customize via `~/.pi/agent/keybindings.json`. Run `/reload` to apply without restarting.

## Key Format

`modifier+key` where modifiers are `ctrl`, `shift`, `alt` (combinable):

- **Letters:** `a-z`
- **Digits:** `0-9`
- **Special:** `escape`, `esc`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, `insert`, `clear`, `home`, `end`, `pageUp`, `pageDown`, `up`, `down`, `left`, `right`
- **Function:** `f1`-`f12`
- **Symbols:** `` ` ``, `-`, `=`, `[`, `]`, `\`, `;`, `'`, `,`, `.`, `/`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `_`, `+`, `|`, `~`, `{`, `}`, `:`, `<`, `>`, `?`

Examples: `ctrl+shift+x`, `alt+ctrl+x`, `ctrl+1`

> [!note]
> Older configs with pre-namespaced ids (`cursorUp`, `expandTools`) migrate automatically to namespaced ids on startup.

## All Actions

### Cursor Movement

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `tui.editor.cursorUp` | `up` | Move up |
| `tui.editor.cursorDown` | `down` | Move down |
| `tui.editor.cursorLeft` | `left`, `ctrl+b` | Move left |
| `tui.editor.cursorRight` | `right`, `ctrl+f` | Move right |
| `tui.editor.cursorWordLeft` | `alt+left`, `ctrl+left`, `alt+b` | Move word left |
| `tui.editor.cursorWordRight` | `alt+right`, `ctrl+right`, `alt+f` | Move word right |
| `tui.editor.cursorLineStart` | `home`, `ctrl+a` | Line start |
| `tui.editor.cursorLineEnd` | `end`, `ctrl+e` | Line end |
| `tui.editor.jumpForward` | `ctrl+]` | Jump to character |
| `tui.editor.jumpBackward` | `ctrl+alt+]` | Jump backward to character |
| `tui.editor.pageUp` | `pageUp` | Page up |
| `tui.editor.pageDown` | `pageDown` | Page down |

### Deletion

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `tui.editor.deleteCharBackward` | `backspace` | Delete char backward |
| `tui.editor.deleteCharForward` | `delete`, `ctrl+d` | Delete char forward |
| `tui.editor.deleteWordBackward` | `ctrl+w`, `alt+backspace` | Delete word backward |
| `tui.editor.deleteWordForward` | `alt+d`, `alt+delete` | Delete word forward |
| `tui.editor.deleteToLineStart` | `ctrl+u` | Delete to line start |
| `tui.editor.deleteToLineEnd` | `ctrl+k` | Delete to line end |

### Input

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `tui.input.newLine` | `shift+enter` | Insert newline |
| `tui.input.submit` | `enter` | Submit input |
| `tui.input.tab` | `tab` | Tab / autocomplete |

### Kill Ring & Undo

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `tui.editor.yank` | `ctrl+y` | Paste deleted text |
| `tui.editor.yankPop` | `alt+y` | Cycle through deleted text |
| `tui.editor.undo` | `ctrl+-` | Undo last edit |

### Selection & Clipboard

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `tui.input.copy` | `ctrl+c` | Copy selection |
| `tui.select.up` | `up` | Move selection up |
| `tui.select.down` | `down` | Move selection down |
| `tui.select.pageUp` | `pageUp` | Page up in list |
| `tui.select.pageDown` | `pageDown` | Page down in list |
| `tui.select.confirm` | `enter` | Confirm selection |
| `tui.select.cancel` | `escape`, `ctrl+c` | Cancel selection |

### Application

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `app.interrupt` | `escape` | Cancel / abort |
| `app.clear` | `ctrl+c` | Clear editor |
| `app.exit` | `ctrl+d` | Exit (when editor empty) |
| `app.suspend` | `ctrl+z` (not on Windows) | Suspend to background |
| `app.editor.external` | `ctrl+g` | Open in `$VISUAL` or `$EDITOR` |
| `app.clipboard.pasteImage` | `ctrl+v` (`alt+v` on Windows) | Paste image from clipboard |

> [!warning]
> On Windows, `app.suspend` has no default binding. In WSL, `ctrl+z`/`fg` works normally.

### Sessions

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `app.session.new` | *(none)* | Start new session (`/new`) |
| `app.session.tree` | *(none)* | Open session tree (`/tree`) |
| `app.session.fork` | *(none)* | Fork current session (`/fork`) |
| `app.session.resume` | *(none)* | Open session picker (`/resume`) |
| `app.session.togglePath` | `ctrl+p` | Toggle path display |
| `app.session.toggleSort` | `ctrl+s` | Toggle sort mode |
| `app.session.toggleNamedFilter` | `ctrl+n` | Toggle named-only filter |
| `app.session.rename` | `ctrl+r` | Rename session |
| `app.session.delete` | `ctrl+d` | Delete session |
| `app.session.deleteNoninvasive` | `ctrl+backspace` | Delete when query empty |

### Models & Thinking

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `app.model.select` | `ctrl+l` | Open model selector |
| `app.model.cycleForward` | `ctrl+p` | Cycle to next model |
| `app.model.cycleBackward` | `shift+ctrl+p` | Cycle to previous model |
| `app.thinking.cycle` | `shift+tab` | Cycle thinking level |
| `app.thinking.toggle` | `ctrl+t` | Collapse/expand thinking blocks |

### Display & Messages

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `app.tools.expand` | `ctrl+o` | Collapse/expand tool output |
| `app.message.followUp` | `alt+enter` | Queue follow-up message |
| `app.message.dequeue` | `alt+up` | Restore queued messages |

### Tree Navigation

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `app.tree.foldOrUp` | `ctrl+left`, `alt+left` | Fold branch or jump to previous segment |
| `app.tree.unfoldOrDown` | `ctrl+right`, `alt+right` | Unfold branch or jump to next segment |
| `app.tree.editLabel` | `shift+l` | Edit tree node label |
| `app.tree.toggleLabelTimestamp` | `shift+t` | Toggle label timestamps |
| `app.tree.filter.default` | `ctrl+d` | Set default filter |
| `app.tree.filter.noTools` | `ctrl+t` | Hide tool results |
| `app.tree.filter.userOnly` | `ctrl+u` | Show user messages only |
| `app.tree.filter.labeledOnly` | `ctrl+l` | Show labeled entries only |
| `app.tree.filter.all` | `ctrl+a` | Show all entries |
| `app.tree.filter.cycleForward` | `ctrl+o` | Cycle filter forward |
| `app.tree.filter.cycleBackward` | `shift+ctrl+o` | Cycle filter backward |

### Scoped Models Selector (`/scoped-models`)

| Keybinding id | Default | Description |
|--------------|---------|-------------|
| `app.models.save` | `ctrl+s` | Save model selection |
| `app.models.enableAll` | `ctrl+a` | Enable all (or matching search) |
| `app.models.clearAll` | `ctrl+x` | Clear all (or matching search) |
| `app.models.toggleProvider` | `ctrl+p` | Toggle all models for provider |
| `app.models.reorderUp` | `alt+up` | Move selected model up |
| `app.models.reorderDown` | `alt+down` | Move selected model down |

## Custom Configuration

Create `~/.pi/agent/keybindings.json`:

```json
{
  "tui.editor.cursorUp": ["up", "ctrl+p"],
  "tui.editor.cursorDown": ["down", "ctrl+n"],
  "tui.editor.deleteWordBackward": ["ctrl+w", "alt+backspace"]
}
```

Single key or array. User config overrides defaults.

### Emacs Example

```json
{
  "tui.editor.cursorUp": ["up", "ctrl+p"],
  "tui.editor.cursorDown": ["down", "ctrl+n"],
  "tui.editor.cursorLeft": ["left", "ctrl+b"],
  "tui.editor.cursorRight": ["right", "ctrl+f"],
  "tui.editor.cursorWordLeft": ["alt+left", "alt+b"],
  "tui.editor.cursorWordRight": ["alt+right", "alt+f"],
  "tui.editor.deleteCharForward": ["delete", "ctrl+d"],
  "tui.editor.deleteCharBackward": ["backspace", "ctrl+h"],
  "tui.input.newLine": ["shift+enter", "ctrl+j"]
}
```

### Vim Example

```json
{
  "tui.editor.cursorUp": ["up", "alt+k"],
  "tui.editor.cursorDown": ["down", "alt+j"],
  "tui.editor.cursorLeft": ["left", "alt+h"],
  "tui.editor.cursorRight": ["right", "alt+l"],
  "tui.editor.cursorWordLeft": ["alt+left", "alt+b"],
  "tui.editor.cursorWordRight": ["alt+right", "alt+w"]
}
```

#keybindings #configuration #tui #shortcuts #editor-settings #productivity