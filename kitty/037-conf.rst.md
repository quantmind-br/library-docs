---
title: kitty.conf
url: https://github.com/kovidgoyal/kitty/blob/master/docs/conf.rst
source: git
fetched_at: 2026-05-04T15:57:38.34481118-03:00
rendered_js: false
word_count: 193
summary: Structure, location, and syntax rules for the kitty terminal configuration file, including methods for reloading and modularizing settings.
tags:
    - kitty-terminal
    - configuration-file
    - system-customization
    - environment-variables
    - terminal-settings
category: configuration
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# kitty.conf

kitty is fully customizable: keyboard shortcuts, rendering, frames-per-second, and more. See the [[042-actions]] list for everything you can map.

## Config file location

kitty looks for `kitty.conf` in OS config directories (usually `~/.config/kitty/kitty.conf`). Override with:

- CLI flag: `kitty --config /path/to/custom.conf`
- Environment variable: `KITTY_CONFIG_DIRECTORY`

## Opening and reloading

| Action | macOS | Linux/BSD |
|--------|-------|-----------|
| Open config file | `⌘+,` | `edit_config_file` |
| Reload config file | `⌃+⌘+,` | `reload_config_file` |
| Display current config | `⌥+⌘+,` | `debug_config` |

Auto-reload on file change is controlled by `auto_reload_config`. Manual reload also works via `kill -SIGUSR1 $KITTY_PID`.

## Comments

Lines starting with `#` are comments. The `#` must be the first character.

## Line continuation

End a line with `\` to continue on the next line. Leading whitespace and the `\` are stripped.

## Include directives

Include other config files, globs, environment variables, or dynamically generated output:

```bash
# Include another file
include other.conf

# Include all *.conf in kitty.d subdirectories
globinclude kitty.d/**/*.conf

# Include contents of env vars starting with KITTY_CONF_
envinclude KITTY_CONF_*

# Run dynamic.py and include its STDOUT (Python is fastest; any executable works)
geninclude dynamic.py
```

Relative paths resolve from the current config file location. Environment variables expand: `${USER}.conf` becomes `name.conf` when `USER=name`. The special variable `KITTY_OS` is available: `linux`, `macos`, or `bsd`.

## Generate default config

```bash
kitty +runpy 'from kitty.config import *; print(commented_out_default_config())'
```

Prints the full default config with comments describing each option.
