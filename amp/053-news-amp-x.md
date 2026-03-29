---
title: amp dash x
url: https://ampcode.com/news/amp-x
source: crawler
fetched_at: 2026-02-06T02:08:42.255827433-03:00
rendered_js: false
word_count: 91
summary: This document introduces the Amp CLI's execute mode, explaining how to use the --execute flag for programmatic interactions and automation via the command line.
tags:
    - amp-cli
    - execute-mode
    - command-line
    - automation
    - shell-integration
category: reference
---

The [Amp CLI](https://ampcode.com/manual#getting-started-command-line-interface) has a new flag: `--execute`.

`-x` for short.

That flag turns on execute mode, which allows for programmatic use of the Amp CLI.

The CLI sends the given prompt to the agent and waits until the agent is done. Then it prints the agent's last message.

```
$ amp -x "Give me a list of targets in this Makefile. Only the names."
git
zsh
ghostty
atuin
jj
all
```

```
$ amp -x "Rename all .markdown files to .md then print the new names."
- readme.markdown → readme.md
- ghostty.markdown → ghostty.md
```

You can also pipe input to it:

```
$ echo "what package manager do we use here? reply only with name." | amp -x
pnpm
```

Execute mode is automatically turned on when you redirect stdout:

```
$ echo "list all markdown files in here" | amp > output.txt
$ cat output.txt
README.md
CONTRIBUTING.md
YOURE_ABSOLUTELY_RIGHT.md
```

You can also use execute mode with `threads continue`:

```
$ amp -x "what is 2+2?"
4

$ amp threads continue -x "add 5 to that"
9

$ amp threads continue -x "now minus 3"
6
```

*Note:* Execute mode consumes paid credits only, not [ad-supported free-tier](https://ampcode.com/free) credits, because it can't display ads.