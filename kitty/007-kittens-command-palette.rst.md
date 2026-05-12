---
title: Command palette
title: Command palette
word_count: 296
summary: This document explains how to use the kitty command palette to search, filter, and trigger both mapped and unmapped keyboard actions.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:08Z
---
# Command palette

The command palette lets you browse, search, and trigger all keyboard shortcuts and actions in kitty from a single searchable overlay. Press `command_palette` to open it (default: Ctrl+Shift+F3).

![A screenshot of the command palette kitten](../screenshots/command-palette.webp)

All mapped and unmapped actions are listed, organized by category. Mouse bindings appear in a separate section. Type to filter results in real time; press Enter to run the selected action.

## Searching

Matching is case-insensitive and works across three columns simultaneously: **key** (shortcut), **action** name, and **category**. Matched characters are highlighted.

**Multiple words** — separate terms with spaces. Items matching more terms rank higher. Each word in the query is matched against every word in the three columns:

- *Exact word* — highest score.
- *Prefix* — e.g. `scr` matches `scroll`.
- *Typo tolerance* — for words of 4+ characters: one typo produces a match; two typos give a lower score.

**Compound names** — delimiters (`_`, `+`, `/`, `-`) are kept intact. Search for `mouse_selection` as a unit, or it splits into `mouse` and `selection` if no exact match.

**Ranking** — items are sorted by:
1. Number of query words matched (more is better).
2. Action column score (action matches outrank key/category matches).
3. Key column score.
4. Category column score.
5. Shorter action name as tiebreaker.

## Keyboard controls

Available keys while the palette is open:

## Unmapped actions

Unmapped actions appear with an `(unmapped)` label. Press F12 to toggle their visibility. This preference is remembered across sessions. Useful for discovering unconfigured functionality; note the action name and add a mapping in [[037-conf|kitty.conf]].

## Custom keyboard modes

Custom keyboard modes defined in [[037-conf|kitty.conf]] appear under separate mode headers. `push_keyboard_mode` bindings are grouped with the target mode they activate.

## Configuration

Default mapping:

```conf
map kitty_mod+f3 command_palette
```

Change it in [[037-conf|kitty.conf]]:

```conf
map ctrl+p command_palette
```
