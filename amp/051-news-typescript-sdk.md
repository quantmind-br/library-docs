---
title: Amp TypeScript SDK
url: https://ampcode.com/news/typescript-sdk
source: crawler
fetched_at: 2026-02-06T02:08:29.54089376-03:00
rendered_js: false
word_count: 208
summary: This document introduces the Amp TypeScript SDK, explaining how to programmatically integrate the Amp agent into TypeScript applications for automated tasks.
tags:
    - typescript-sdk
    - amp-agent
    - developer-tools
    - sourcegraph-amp
    - api-integration
category: guide
---

Today we've launched the Amp TypeScript SDK. It allows you to programmatically use the Amp agent in your TypeScript programs.

Here is a program, for example, that instructs the Amp agent to find and list specific files in a folder using a [custom toolbox tool](https://ampcode.com/news/toolboxes):

```
import { AmpOptions, execute } from '@sourcegraph/amp-sdk'
import path from 'path'

const prompt = `
	What files use authentication in this directory?
	Go through all the files and folders.
	Use the format_file_tree tool to format results.
	Only output the file tree.
`

const options: AmpOptions = {
	cwd: path.join(process.cwd(), 'src'), // Run in `./src` folder
	dangerouslyAllowAll: true, // Allow all tools, trust in Amp
	toolbox: path.join(process.cwd(), 'toolbox'), // Location of custom toolbox
}

// execute starts the agent and streams messages
const messages = execute({ prompt, options })

for await (const message of messages) {
	// A system message contains information about the current session
	if (message.type === 'system') {
		console.log(`Started thread: ${message.session_id}`)

		// For example, the custom tools that were found in the toolbox
		console.log(
			'Available tools in Toolbox: ',
			message.tools.filter((tool) => tool.startsWith('tb__')).join(', '),
		)
	} else if (message.type === 'assistant') {
		// An assistant message contains the assistants text replies
		// or tool uses
		console.log('Assistant:', message)
	} else if (message.type === 'result') {
		// A result message contains the last message of the assistant
		console.log('Files using authentication:', message.result)
	}
}
```

You only need to install one package to get started:

```
$ npm install @sourcegraph/amp-sdk
```

Since you can invoke Amp in any TypeScript program, there are very few limits to what you can build. Here are some ideas and examples of things we've built internally:

- **Code Review Agent**: Automated pull request analysis and feedback
- **Documentation Generator**: Create and maintain project documentation
- **Test Automation**: Generate and execute test suites
- **Migration Assistant**: Help upgrade codebases and refactor legacy code
- **CI/CD Integration**: Smart build and deployment pipelines
- **Issue Triage**: Automatically categorize and prioritize bug reports

To get more ideas and familiar with the SDK, take a look at the examples in the [manual](https://ampcode.com/manual/sdk#advanced-usage).

*Note:* The Amp SDK consumes paid credits only, not [ad-supported free-tier](https://ampcode.com/free) credits, because it can't display ads.