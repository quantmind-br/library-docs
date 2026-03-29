---
title: Bring Your Own Tools
url: https://ampcode.com/news/toolboxes
source: crawler
fetched_at: 2026-02-06T02:08:31.830864183-03:00
rendered_js: false
word_count: 139
summary: This document explains how to integrate custom executable files as tools in Amp using environment variables and standard input/output protocols for discovery and execution.
tags:
    - amp-platform
    - external-tools
    - executable-integration
    - tool-discovery
    - environment-variables
category: guide
---

You can now provide tools to Amp in the form of executable files.

If the environment variable `AMP_TOOLBOX` is set and contains the path to a directory, Amp will look in that directory for executables to be used as tools.

On start, Amp will invoke each executable it found, with the environment variable `TOOLBOX_ACTION` set to `describe`. The tool is then expected to write its description (which is what will end up in the system prompt that's sent to the agent) to `stdout`.

Here is an example:

```
#!/usr/bin/env bun
import fs from 'node:fs'
const action = process.env.TOOLBOX_ACTION

if (action === 'describe') showDescription()
else if (action === 'execute') runTests()

function showDescription() {
	process.stdout.write(
		JSON.stringify({
			name: 'run-tests',
			description: 'use this tool instead of Bash to run tests in a workspace',
			args: { dir: ['string', 'the workspace directory'] },
		}),
	)
}
```

When the agent then decides to invoke your tool, Amp runs the executable again, this time setting `TOOLBOX_ACTION` to `execute`. Amp passes the tool call arguments on `stdin` and the executable can then execute the tool call:

```
function runTests() {
	let dir = JSON.parse(fs.readFileSync(0, 'utf-8'))['dir']
	dir = dir && dir.length > 0 ? dir : '.'
	Bun.spawn(['pnpm', '-C', dir, 'run', 'test', '--no-color', '--run'], {
		stdio: ['inherit', 'inherit', 'inherit'],
	})
}
```

You can read more about toolboxes and possible input and output formats [in the manual](https://ampcode.com/manual#toolboxes).