---
title: Building a coding agent
url: https://docs.docker.com/ai/cagent/tutorial/
source: llms
fetched_at: 2026-01-24T14:13:49.149710646-03:00
rendered_js: false
word_count: 807
summary: This tutorial explains how to build, configure, and refine AI coding agents using cagent, covering tool integration, structured instructions, and multi-agent workflows.
tags:
    - cagent
    - coding-agents
    - ai-development
    - agent-configuration
    - multi-agent-systems
    - yaml-config
category: tutorial
---

This tutorial teaches you how to build a coding agent that can help with software development tasks. You'll start with a basic agent and progressively add capabilities until you have a production-ready assistant that can read code, make changes, run tests, and even look up documentation.

By the end, you'll understand how to structure agent instructions, configure tools, and compose multiple agents for complex workflows.

A coding agent that can:

- Read and modify files in your project
- Run commands like tests and linters
- Follow a structured development workflow
- Look up documentation when needed
- Track progress through multi-step tasks

<!--THE END-->

- How to configure cagent agents in YAML
- How to give agents access to tools (filesystem, shell, etc.)
- How to write effective agent instructions
- How to compose multiple agents for specialized tasks
- How to adapt agents for your own projects

Before starting, you need:

- **cagent installed** - See the [installation guide](https://docs.docker.com/ai/cagent/#installation)
- **API key configured** - Set `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` in your environment. Get keys from [Anthropic](https://console.anthropic.com/) or [OpenAI](https://platform.openai.com/api-keys)
- **A project to work with** - Any codebase where you want agent assistance

A cagent agent is defined in a YAML configuration file. The minimal agent needs just a model and instructions that define its purpose.

Create a file named `agents.yml`:

Run your agent:

Try asking it: "How do I read a file in Python?"

The agent can answer coding questions, but it can't see your files or run commands yet. To make it useful for real development work, it needs access to tools.

A coding agent needs to interact with your project files and run commands. You enable these capabilities by adding toolsets.

Update `agents.yml` to add filesystem and shell access:

Run the updated agent and try: "Read the README.md file and summarize it."

Your agent can now:

- Read and write files in the current directory
- Execute shell commands
- Explore your project structure

> directory. The agent will request permission if it needs to access other directories.

The agent can now interact with your code, but its behavior is still generic. Next, you'll teach it how to work effectively.

Generic instructions produce generic results. For production use, you want your agent to follow a specific workflow and understand your project's conventions.

Update your agent with structured instructions. This example shows a Go development agent, but you can adapt the pattern for any language:

Try asking: "Add error handling to the `parseConfig` function in main.go"

The structured instructions give your agent:

- A clear workflow to follow (analyze, examine, modify, validate)
- Project-specific commands to run
- Constraints that prevent common mistakes
- Context about the environment (`add_date` and `add_environment_info`)

The `todo` toolset helps the agent track progress through multi-step tasks. When you ask for complex changes, the agent will break down the work and update its progress as it goes.

Complex tasks often benefit from specialized agents. You can add sub-agents that handle specific responsibilities, like researching documentation while your main agent stays focused on coding.

Add a librarian agent that can search for documentation:

Try asking: "How do I use `context.Context` in Go? Then add it to my server code."

Your main agent will delegate the research to the librarian, then use that information to modify your code. This keeps the main agent's context focused on the coding task while still having access to up-to-date documentation.

Using a smaller, faster model (Haiku) for the librarian saves costs since documentation lookup doesn't need the same reasoning depth as code changes.

Now that you understand the core concepts, adapt the agent for your specific project:

### [Update the development commands](#update-the-development-commands)

Replace the Go commands with your project's workflow:

### [Add project-specific constraints](#add-project-specific-constraints)

If your agent keeps making the same mistakes, add explicit constraints:

### [Choose the right models](#choose-the-right-models)

For coding tasks, use reasoning-focused models:

- `anthropic/claude-sonnet-4-5` - Strong reasoning, good for complex code
- `openai/gpt-5` - Fast, good general coding ability

For auxiliary tasks like documentation lookup, smaller models work well:

- `anthropic/claude-haiku-4-5` - Fast and cost-effective
- `openai/gpt-5-mini` - Good for simple tasks

### [Iterate based on usage](#iterate-based-on-usage)

The best way to improve your agent is to use it. When you notice issues:

1. Add specific instructions to prevent the problem
2. Update constraints to guide behavior
3. Add relevant commands to the development workflow
4. Consider adding specialized sub-agents for complex areas

You now know how to:

- Create a basic cagent configuration
- Add tools to enable agent capabilities
- Write structured instructions for consistent behavior
- Compose multiple agents for specialized tasks
- Adapt agents for different programming languages and workflows

<!--THE END-->

- Learn [best practices](https://docs.docker.com/ai/cagent/best-practices/) for handling large outputs, structuring agent teams, and optimizing performance
- Integrate cagent with your [editor](https://docs.docker.com/ai/cagent/integrations/acp/) or use agents as [tools in MCP clients](https://docs.docker.com/ai/cagent/integrations/mcp/)
- Review the [Configuration reference](https://docs.docker.com/ai/cagent/reference/config/) for all available options
- Explore the [Tools reference](https://docs.docker.com/ai/cagent/reference/toolsets/) to see what capabilities you can enable
- Check out [example configurations](https://github.com/docker/cagent/tree/main/examples) for different use cases
- See the full [golang\_developer.yaml](https://github.com/docker/cagent/blob/main/golang_developer.yaml) that the Docker team uses to develop cagent