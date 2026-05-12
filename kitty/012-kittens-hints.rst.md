---
title: Hints
title: Hints
word_count: 197
summary: This document explains how to use and customize the kitty terminal's 'hints' feature to select, process, and perform actions on visible text snippets like URLs, file paths, and custom patterns.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:08Z
---
# Hints

|kitty| has a *hints mode* to select and act on arbitrary text snippets visible on screen.

- `open_url` — choose any URL visible on screen and open in default browser.
- `insert_selected_path` — select a path/filename from terminal output and insert it into the command line (useful for `git` or `ls` output).
- `goto_file_line` — select a path:line pattern and open in your default editor at that line (requires editor support for `+linenum` syntax or a "known" editor).
- `open_selected_hyperlink` — open hyperlinks marked by the terminal program (e.g., `ls --hyperlink=auto`). If your `ls` does not support hyperlinks, install [GNU Coreutils](https://www.gnu.org/software/coreutils/).

Customize patterns and editor:

```
map ctrl+g kitten hints --type=linenum --linenum-action='tab nvim +{line} {path}'
```

> [!NOTE]
> If there are more hints than letters, hints use multiple letters. Press the first letter to filter; press the second to select, or Enter/Space for the empty hint.

Mouse users can click on matched text instead of typing hint characters.

## Custom matching and actions

Create `~/.config/kitty/custom-hints.py`:

```python
import re

def mark(text, args, Mark, extra_cli_args, *a):
    for idx, m in enumerate(re.finditer(r'\w+', text)):
        start, end = m.span()
        mark_text = text[start:end].replace('\n', '').replace('\0', '')
        yield Mark(idx, start, end, mark_text, {})

def handle_result(args, data, target_window_id, boss, extra_cli_args, *a):
    matches, groupdicts = [], []
    for m, g in zip(data['match'], data['groupdicts']):
        if m:
            matches.append(m), groupdicts.append(g)
    for word, match_data in zip(matches, groupdicts):
        boss.open_url(f'https://www.google.com/search?q=define:{word}')
```

Run:

```
kitty -o 'map f1 kitten hints --customize-processing custom-hints.py'
```

> [!NOTE]
> Use `action_alias` in [[037-conf|kitty.conf]] to avoid repeating options:
>
> ```conf
> action_alias myhints kitten hints --alphabet qfjdkslaureitywovmcxzpq1234567890
> map f1 myhints --customize-processing custom-hints.py
> ```

See [[040-open-actions|open_actions]] for customizing actions taken for different URL types.
