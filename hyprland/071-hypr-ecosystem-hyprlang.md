---
title: hyprlang
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprlang/
source: sitemap
fetched_at: 2026-04-26T09:49:42.389578321-03:00
rendered_js: false
word_count: 612
summary: hyprlang configuration language syntax, structure, and features including variables, arithmetic operations, and conditional logic.
tags:
    - hyprlang
    - configuration-syntax
    - parsing-library
    - scripting-language
    - config-format
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

[hyprlang](https://github.com/hyprwm/hyprlang) parses the Hypr configuration language.

## Syntax[](#syntax)

### Line Style[](#line-style)

Every config line is a **command + value**. Commands are variables or special keywords (defined by the consuming app).

- **Variables** (options): can be specified only once; later definitions overwrite earlier.
- **Keywords** (commands): invoke behavior each time they are defined.

Trailing spaces are optional for legibility.

### Categories[](#categories)

Categories are regular or "special" (containing a key):

```ini
category {
    variable = value
}
```

Special categories define "groups" with a key:

```ini
special {
    key = A
    variable = value
}
special {
    key = B
    variable = value
}
```

Hyprland uses special categories for per-device configs.

### Defining variables[](#defining-variables)

```ini
$VARNAME = value
```

Variables expand inline:

```ini
$SUFFIX = -san
$NAME = Jeremy
greeting = Hello, $NAME$SUFFIX.
```

> [!note]
> Spaces around/separating values are not mandatory.

### Comments[](#comments)

`#` starts a comment. `##` produces a literal `#` in the line.

### Inline Options[](#inline-options)

Inline category syntax with `:` separator:

```ini
category:variable = value
```

For special categories with a key:

```ini
category[keyvalue]:variable = value
```

This syntax is used by `hyprctl keyword`.

## Error suppression[](#escaping-errors)

Ignore missing options/keywords from plugins to avoid error bars before load:

```ini
# hyprlang noerror true
bind = MOD, KEY, something, amogus
someoption = blah
# hyprlang noerror false
```

## Arithmetic Operations[](#arithmetic-operations)

Since 0.6.3, hyprlang supports basic arithmetic with `{{}}`:

| Operator | Supported |
|----------|-----------|
| `+` | yes |
| `-` | yes |
| `*` | yes |
| `/` | yes |

Rules:
- Only **two** operands (not `{{a + b + c}}`)
- Both sides must be numeric variables or constants
- Spaces **required** around operator (`{{a + b}}`, not `{{a+b}}`)

```ini
$VAR1 = 2
$VAR2 = {{VAR1 + 3}}
$VAR3 = {{VAR2 * 2}}
someVariable = {{VAR3 / 2}}
someVariable2 = VAR3
```

### Arithmetic Escaping[](#arithmetic-escaping)

Since 0.6.4, prefix `\` to escape expressions:

```ini
$VAR = \{{10 + 10}}
bind = MOD, KEY, exec, COMMAND "{\{10 + 10}}"
someVariable = \{\{10 + 10}}
```

Result: raw value verbatim, `\` removed. `\{{hello world}}` becomes `{{hello world}}`.

### Escaping Escapes[](#escaping-escapes)

Since 0.6.4, escape `\` that would otherwise escape:

```ini
someVariable = \\{{VAR1 + 10}}
someOtherVariable = \\{ hello \\}
```

## Conditionals[](#conditionals)

Since 0.6.4, use `# hyprlang if` directive for conditional blocks:

```ini
# hyprlang if MY_VAR
test = 24
# hyprlang endif
# hyprlang if !MY_VAR
test = 12
# hyprlang endif
```

> [!info]
> - A variable is `true` if it exists and is not an empty string.
> - Environment variables are supported.
> - `hyprctl keyword` changes **do not** re-trigger conditional blocks. Edit files directly (or relaunch/reload).

## Developer Documentation[](#developer-documentation)

See [standards.hyprland.org/hyprlang](https://standards.hyprland.org/hyprlang/).