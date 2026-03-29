---
title: SDK
url: https://ampcode.com/manual/sdk
source: crawler
fetched_at: 2026-02-06T02:07:51.813391579-03:00
rendered_js: false
word_count: 673
summary: This document provides an overview of the Amp SDK for TypeScript, explaining how to programmatically interact with the Amp agent through message streaming, thread management, and configuration settings.
tags:
    - amp-sdk
    - typescript-sdk
    - message-streaming
    - thread-continuity
    - mcp-integration
    - api-integration
    - automation
category: api
---

## Overview[#](#overview)[#](#overview)

The Amp SDK allows you to programmatically use the Amp agent in your TypeScript programs.

### Why use the Amp SDK?[#](#why-use-the-amp-sdk)[#](#why-use-the-amp-sdk)

The Amp SDK offers the following functionality:

- **Stream Inputs**: Send messages one-by-one to the Amp agent
- **Stream Outputs**: Receive structured JSON responses (system, assistant, result) while the agent runs
- **Multi-turn Conversations**: Maintain back-and-forth interactions across multiple inference calls
- **Thread Continuity**: Continue an existing thread (latest or by ID) to build stateful agent workflows
- **Programmatic Settings**: Configure working directories, settings, and tools without user prompts — ideal for automation
- **MCP Integration**: specify which MCP servers are available for a given session
- **Custom Skills**: Define and use custom agent skills to extend Amp’s functionality

### What can you build?[#](#what-can-you-build)[#](#what-can-you-build)

Here are some examples of what you can build with the Amp SDK:

#### Development Tools[#](#development-tools)[#](#development-tools)

- **Code Review Agent**: Automated pull request analysis and feedback
- **Documentation Generator**: Create and maintain project documentation
- **Test Automation**: Generate and execute test suites
- **Migration Assistant**: Help upgrade codebases and refactor legacy code

#### Workflow Automation[#](#workflow-automation)[#](#workflow-automation)

- **CI/CD Integration**: Smart build and deployment pipelines
- **Issue Triage**: Automatically categorize and prioritize bug reports
- **Code Quality Monitoring**: Continuous analysis of code health metrics
- **Release Management**: Automated changelog generation and version bumping

### Limitations[#](#limitations)[#](#limitations)

- The Amp SDK consumes paid credits only, not [ad-supported free-tier](https://ampcode.com/free) credits, because it can’t display ads.

### Quick Start[#](#quick-start)[#](#quick-start)

#### Installation[#](#installation)[#](#installation)

```
# Install the Amp SDK using npm
npm install @sourcegraph/amp-sdk

# or yarn
yarn add @sourcegraph/amp-sdk
```

Once installed, add your access token to the environment. You can access your access token at [ampcode.com/settings](https://ampcode.com/settings).

```
export AMP_API_KEY=sgamp_your_access_token_here
```

If you already have the Amp CLI installed locally, you can log in using the following command `amp login`.

#### Run Your First Amp Command[#](#run-your-first-amp-command)[#](#run-your-first-amp-command)

Now that you have the SDK installed and your access token set up, you can start using Amp with the `execute()` function:

```
import { execute } from '@sourcegraph/amp-sdk'

// Simple execution - get the final result
for await (const message of execute({ prompt: 'What files are in this directory?' })) {
	if (message.type === 'result' && !message.is_error) {
		console.log('Result:', message.result)
		break
	}
}
```

The `execute()` function only requires that you provide a `prompt` to get started. The SDK streams messages as the agent works, letting you handle responses and integrate them directly into your application.

### Core Concepts[#](#core-concepts)[#](#core-concepts)

#### Message Streaming[#](#message-streaming)[#](#message-streaming)

The SDK streams different types of messages as your agent executes:

```
for await (const message of execute({ prompt: 'Run tests' })) {
	if (message.type === 'system') {
		// Session info, available tools, MCP servers
		console.log('Available tools:', message.tools)
	} else if (message.type === 'assistant') {
		// AI responses and tool usage
		console.log('Assistant is working...')
	} else if (message.type === 'result') {
		// Final result (success or error)
		console.log('Done:', message.result)
	}
}
```

When you just need the final result without handling streaming:

```
async function getResult(prompt: string): Promise<string> {
	for await (const message of execute({ prompt, options: { dangerouslyAllowAll: true } })) {
		if (message.type === 'result') {
			if (message.is_error) {
				throw new Error(message.error)
			}
			return message.result
		}
	}
	throw new Error('No result received')
}

// Usage
try {
	const result = await getResult('List all TypeScript files in this project')
	console.log('Found files:', result)
} catch (error) {
	console.error('Failed:', error.message)
}
```

#### Thread Continuity[#](#thread-continuity)[#](#thread-continuity)

Continue conversations across multiple interactions:

```
// Continue the most recent conversation
for await (const message of execute({
	prompt: 'What was the last error you found?',
	options: { continue: true },
})) {
	if (message.type === 'result') {
		console.log(message.result)
	}
}

// Continue a specific thread by ID
for await (const message of execute({
	prompt: 'Can you update that code we discussed?',
	options: { continue: 'T-abc123-def456' },
})) {
	if (message.type === 'result') {
		console.log(message.result)
	}
}
```

### Common Configuration[#](#common-configuration)[#](#common-configuration)

#### Skip Permission Prompts[#](#skip-permission-prompts)[#](#skip-permission-prompts)

For automation scenarios, bypass permission prompts:

```
const options = {
	dangerouslyAllowAll: true, // Skip permission prompts
}

for await (const message of execute({
	prompt: 'Make changes without asking for permission',
	options,
})) {
	// Handle messages...
}
```

#### Working Directory[#](#working-directory)[#](#working-directory)

Specify where Amp should run:

```
for await (const message of execute({
	prompt: 'Refactor the auth module',
	options: { cwd: './my-project' },
})) {
	// Process messages...
}
```

#### Enable Debug Logging[#](#enable-debug-logging)[#](#enable-debug-logging)

See what’s happening under the hood:

```
for await (const message of execute({
	prompt: 'Analyze this project',
	options: {
		logLevel: 'debug', // Shows CLI command in console
		logFile: './amp-debug.log', // Optional: write logs to file
	},
})) {
	// Process messages
}
```

#### Agent Mode[#](#agent-mode)[#](#agent-mode)

Select which agent mode to use. The mode controls the model, system prompt, and tool selection:

```
for await (const message of execute({
	prompt: 'Quickly fix this typo',
	options: {
		mode: 'rush', // Use rush mode for faster responses
	},
})) {
	// Process messages
}
```

Available modes:

- `smart` (default): Balanced mode with full capabilities
- `rush`: Faster responses with streamlined tool usage
- `deep`: Extended reasoning for complex tasks

#### Thread Labels[#](#thread-labels)[#](#thread-labels)

Add labels to threads created by `execute()`:

```
for await (const message of execute({
	prompt: 'Summarize this repo',
	options: {
		labels: ['sdk', 'summary'],
	},
})) {
	if (message.type === 'result') {
		console.log(message.result)
		break
	}
}
```

#### Thread Visibility[#](#thread-visibility)[#](#thread-visibility)

Control who can see threads created by `execute()`:

```
for await (const message of execute({
	prompt: 'Analyze this private codebase',
	options: {
		visibility: 'private', // Only you can see this thread
	},
})) {
	if (message.type === 'result') {
		console.log(message.result)
		break
	}
}
```

Available visibility levels:

- `workspace` (default): Visible to all workspace members
- `private`: Only visible to you
- `public`: Visible to anyone with the link
- `group`: Visible to members of your user group (Enterprise)

#### Tool Permissions[#](#tool-permissions)[#](#tool-permissions)

Control which tools Amp can use with fine-grained permissions:

```
import { execute, createPermission } from '@sourcegraph/amp-sdk'

for await (const message of execute({
	prompt: 'List files and run tests',
	options: {
		permissions: [
			// Allow listing files
			createPermission('Bash', 'allow', { matches: { cmd: 'ls *' } }),
			// Allow running tests
			createPermission('Bash', 'allow', { matches: { cmd: 'npm test' } }),
			// Ask before reading sensitive files
			createPermission('Read', 'ask', { matches: { path: '/etc/*' } }),
		],
	},
})) {
	// Process messages
}
```

Permission rules support:

- **Pattern matching**: Use `*` wildcards and regex patterns
- **Context control**: Restrict rules to main thread or sub-agents
- **Delegation**: Delegate permission decisions to external programs

Learn more about permissions in the [manual](#permissions) and the [appendix](https://ampcode.com/manual/appendix#permissions-reference).

### Advanced Usage[#](#advanced-usage)[#](#advanced-usage)

#### Interactive Progress Tracking[#](#interactive-progress-tracking)[#](#interactive-progress-tracking)

For building user interfaces that show real-time progress:

```
async function executeWithProgress(prompt: string) {
	console.log('Starting task...')

	for await (const message of execute({ prompt })) {
		if (message.type === 'system' && message.subtype === 'init') {
			console.log('Tools available:', message.tools.join(', '))
		} else if (message.type === 'assistant') {
			// Show tool usage or assistant responses
			const content = message.message.content[0]
			if (content.type === 'tool_use') {
				console.log(`Using ${content.name}...`)
			} else if (content.type === 'text') {
				console.log('Assistant:', content.text.slice(0, 100) + '...')
			}
		} else if (message.type === 'result') {
			if (message.is_error) {
				console.log('Failed:', message.error)
			} else {
				console.log('Completed successfully!')
				console.log(message.result)
			}
		}
	}
}
```

#### Cancellation and Timeouts[#](#cancellation-and-timeouts)[#](#cancellation-and-timeouts)

Handle long-running operations gracefully:

```
async function executeWithTimeout(prompt: string, timeoutMs = 30000) {
	const signal = AbortSignal.timeout(timeoutMs)

	try {
		for await (const message of execute({
			prompt,
			signal,
			options: { dangerouslyAllowAll: true },
		})) {
			if (message.type === 'result') {
				return message.result
			}
		}
	} catch (error) {
		if (error.message.includes('aborted')) {
			throw new Error(`Operation timed out after ${timeoutMs}ms`)
		}
		throw error
	}
}
```

#### MCP Integration[#](#mcp-integration)[#](#mcp-integration)

Extend Amp’s capabilities with custom tools and data sources:

```
import { execute, type MCPConfig } from '@sourcegraph/amp-sdk'

const mcpConfig: MCPConfig = {
	playwright: {
		command: 'npx',
		args: ['-y', '@playwright/mcp@latest', '--headless'],
		env: { NODE_ENV: 'production' },
	},
	database: {
		command: 'node',
		args: ['./custom-mcp-server.js'],
		env: { DB_CONNECTION_STRING: process.env.DATABASE_URL },
	},
}

for await (const message of execute({
	prompt: 'Test the login flow on staging environment',
	options: { mcpConfig, dangerouslyAllowAll: true },
})) {
	if (message.type === 'system') {
		console.log(
			'MCP Servers:',
			message.mcp_servers.map((s) => `${s.name}: ${s.status}`),
		)
	}
	// Handle other messages...
}
```

To find out more about extending Amp with MCP servers, visit the [MCP Configuration](https://ampcode.com/manual#mcp) section of the manual.

#### Multi-turn Conversations[#](#multi-turn-conversations)[#](#multi-turn-conversations)

Build streaming conversations using async generators:

```
import { execute, createUserMessage } from '@sourcegraph/amp-sdk'

async function* generateMessages() {
	yield createUserMessage('Start analyzing the codebase')

	// Wait for some condition or user input
	await new Promise((resolve) => setTimeout(resolve, 1000))

	yield createUserMessage('Now focus on the authentication module')
}

for await (const message of execute({
	prompt: generateMessages(),
})) {
	if (message.type === 'result') {
		console.log(message.result)
	}
}
```

#### Settings File Configuration[#](#settings-file-configuration)[#](#settings-file-configuration)

Configure Amp’s behavior with a settings file, like the `settings.json`. You can provide Amp with a custom settings file you have saved in your project:

```
import { execute } from '@sourcegraph/amp-sdk'

// Use a custom settings file
for await (const message of execute({
	prompt: 'Deploy the application',
	options: {
		settingsFile: './settings.json',
		logLevel: 'debug',
	},
})) {
	// Handle messages...
}
```

Example `settings.json`:

```
{
	"amp.mcpServers": {
		"playwright": {
			"command": "npx",
			"args": ["-y", "@playwright/mcp@latest", "--headless", "--isolated"]
		}
	},
	"amp.commands.allowlist": ["npx", "node", "npm"],
	"amp.tools.disable": ["mermaid", "mcp__playwright__browser_resize"]
}
```

To find all available settings, see the [Configuration Settings](https://ampcode.com/manual#configuration).

#### Custom Tools[#](#custom-tools)[#](#custom-tools)

Extend Amp’s capabilities with custom toolbox scripts:

```
for await (const message of execute({
	prompt: 'Use my custom deployment scripts',
	options: {
		toolbox: '/usr/repository-path/toolbox', // Path to toolbox scripts
	},
})) {
	// Handle messages...
}
```

To find out more about Amp Toolboxes, see the [Toolboxes](https://ampcode.com/manual#toolboxes) section of the Amp Owner’s Manual.

### Custom Skills[#](#custom-skills)[#](#custom-skills)

Load custom skills from a specified directory:

```
for await (const message of execute({
	prompt: 'Use my custom deployment skill',
	options: {
		skills: './my-skills', // Path to custom skills directory
	},
})) {
	// Process messages
}
```

To learn more about creating custom skills, see the [Agent Skills](https://ampcode.com/manual#agent-skills) section of the Amp documentation.