---
title: Developing builtin kittens
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/developing-builtin-kittens.rst
source: git
fetched_at: 2026-05-04T15:57:56.717404322-03:00
rendered_js: false
word_count: 67
summary: Guide to creating builtin kittens for kitty: Go main logic + Python CLI wrappers, with file templates and integration steps.
tags:
    - kitty-terminal
    - go-development
    - cli-tools
    - plugin-development
    - python-integration
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# Developing builtin kittens

Builtin kittens are written in Go (core logic) with Python wrappers (CLI options + UI).

## File Structure

Create `kittens/my_kitten/__init__.py`, `__main__.py`, and `main.go`.

## Python Wrapper (`__main__.py`)

Defines CLI options and help text.

```python
#!/usr/bin/env python
# License: GPL v3 Copyright: 2018, Kovid Goyal <kovid at kovidgoyal.net>

import sys

# Syntax reference: kitty/tools/cli.py in the kitty source
OPTIONS = r'''
--some-string-option -s
default=my_default_value
Help text for a simple option taking a string value.

--some-boolean-option -b
type=bool-set
Help text for a boolean option defaulting to false.

--some-inverted-boolean-option
type=bool-unset
Help text for a boolean option defaulting to true.

--an-integer-option
type=int
default=13

--an-enum-option
choices=a,b,c,d
default=a
This option can only take the values a, b, c, or d
'''.format

help_text = '''\
Introductory help text for your kitten.
Multiple paragraphs with :bold:`bold` :green:`colored`
:code:`code` :link:`links <http://url>` formatting.
'''

usage = 'TITLE [BODY ...]'
short_description = 'short description shown in kitten --help'

if __name__ == '__main__':
    raise SystemExit('This should be run as kitten my-kitten')
elif __name__ == '__doc__':
    cd = sys.cli_docs  # type: ignore
    cd['usage'] = usage
    cd['options'] = OPTIONS
    cd['help_text'] = help_text
    cd['short_desc'] = short_description
```

## Go Implementation (`main.go`)

```go
package my_kitten

import (
    "fmt"
    "kitty/tools/cli"
)

var _ = fmt.Print

func main(_ *cli.Command, opts *Options, args []string) (rc int, err error) {
    // rc: exit code (1+ if err != nil)
    fmt.Println("Hello world!")
    fmt.Println(args)
    fmt.Println(fmt.Sprintf("%#v", opts))
    return
}

func EntryPoint(parent *cli.Command) {
    create_cmd(parent, main)
}
```

## Integrate into kitty

Edit `tools/cmd/tool/main.go`:

1. Add import: `"kitty/kittens/my_kitten"`
2. Add to `func KittyToolEntryPoints(root *cli.Command)`: `my_kitten.EntryPoint(root)`

Build with `make`, then test:

```
kitten my-kitten
```

#kitty-terminal #go-development #cli-tools #plugin-development
