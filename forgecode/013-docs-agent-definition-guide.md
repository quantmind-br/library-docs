---
title: ForgeCode
url: https://forgecode.dev/docs/agent-definition-guide/
source: sitemap
fetched_at: 2026-03-29T16:30:30.781671-03:00
rendered_js: false
word_count: 1503
summary: This document explains how to create and configure custom AI agents within the ForgeCode environment using markdown definition files and YAML configuration.
tags:
    - ai-agents
    - forgecode
    - yaml-configuration
    - agent-development
    - mcp-tools
    - custom-prompts
category: guide
---

Need an agent that specializes in React development? Or one focused on security auditing? You can create custom agents tailored to your specific needs using simple markdown files.

Think of agents like different specialists for your development team:

- **Agent**: A specialized AI assistant with specific expertise, tools, and behavior patterns - like having expert consultants for different development tasks
- **Agent Definition File**: A markdown file containing YAML configuration and system instructions that define the agent's capabilities and behavior
- **System Prompt**: The markdown content that defines the agent's personality, expertise, and specific instructions
- **Tools**: Specific capabilities an agent can use, such as reading files, running commands, or searching code

<!--THE END-->

- ForgeCode installed and running
- Access to create directories in your home folder
- Basic familiarity with YAML syntax

Follow these steps to create and use a custom agent in under 5 minutes:

### Step 1: Choose Your Agent Storage Location[​](#step-1-choose-your-agent-storage-location "Direct link to Step 1: Choose Your Agent Storage Location")

You have two options for storing custom agents:

**Global Agents** (Recommended for most cases)

- Location: `~/forge/agents/` (Unix/macOS) or `%USERPROFILE%\forge\agents\` (Windows)
- Available across all projects and ForgeCode sessions
- Use for general-purpose agents you'll reuse

**Project-Specific Agents**

- Location: `.forge/agents/` (in your project root - note the dot prefix)
- Override global agents with the same ID
- Use for project-specific customizations

### Step 2: Create the Agent Directory[​](#step-2-create-the-agent-directory "Direct link to Step 2: Create the Agent Directory")

**For Global Agents:**

**For Project-Specific Agents:** **macOS/Linux:**

**Windows Command Prompt:**

**Windows PowerShell:**

### Step 3: Create Your Agent Definition File[​](#step-3-create-your-agent-definition-file "Direct link to Step 3: Create Your Agent Definition File")

Create `frontend-expert.md` in your chosen directory:

**Important**: The filename can be anything ending in `.md`, but the `id` field in the YAML must be unique across all your agents.

### Step 4: Load Your Agent[​](#step-4-load-your-agent "Direct link to Step 4: Load Your Agent")

1. Restart ForgeCode to discover new agents
2. Use the `/agent` command to view available agents
3. Select "FRONTEND\_EXPERT" from the list
4. Your custom agent is now active

Every agent definition file follows this structure:

ForgeCode validates all agent definitions during startup. Understanding these rules prevents common errors:

### Validation Rules[​](#validation-rules "Direct link to Validation Rules")

- **Unique IDs**: Each `id` must be unique across all agent definition files
- **Valid YAML**: Frontmatter must use proper YAML syntax (spaces, not tabs)
- **Recognized Tools**: Only supported tools allowed in the `tools` array
- **Parameter Ranges**: All numeric values must be within valid ranges (see table below)

### Parameter Constraints[​](#parameter-constraints "Direct link to Parameter Constraints")

ParameterValid RangeDefaultPurpose`id`Required-Must be unique across all agents`max_turns`0+100Maximum conversation turns`max_walker_depth`0+1File tree traversal depth`max_tool_failure_per_turn`0+3Max tool failures before completion`max_requests_per_turn`0+100Max requests in single turn`temperature`0.0 - 2.0ProviderResponse creativity (0=precise, 2=creative)`top_p`0.0 - 1.00.8Nucleus sampling threshold`top_k`1 - 100030Top-k sampling limit`max_tokens`1 - 100,00020480Maximum response length

### Required Configuration[​](#required-configuration "Direct link to Required Configuration")

Only one field is mandatory:

### Model and Provider Selection[​](#model-and-provider-selection "Direct link to Model and Provider Selection")

You can customize which model and provider your agent uses:

**Provider naming rules:**

- Provider names must be in **snake\_case** format
- Examples of valid provider names:
  
  - `provider: openai`
  - `provider: open_router`
  - `provider: requesty`
  - `provider: anthropic`

**When to specify a provider:**

- If you want to use a specific provider instead of the default
- When using models available on multiple providers
- For testing different provider implementations
- Leave unspecified to use the default provider configured in ForgeCode

### Recommended Minimum Configuration[​](#recommended-minimum-configuration "Direct link to Recommended Minimum Configuration")

For agents that can be used as tools by other agents:

**Note**: Agents without a `description` field cannot be used as tools by other agents.

### Complete Configuration Reference[​](#complete-configuration-reference "Direct link to Complete Configuration Reference")

You can customize which tools each agent has access to using exact names or glob patterns for flexible configuration.

### Tool Configuration with Glob Patterns[​](#tool-configuration-with-glob-patterns "Direct link to Tool Configuration with Glob Patterns")

Instead of listing every tool individually, use glob patterns to grant access to tool families:

Check the list of [built-in tools](https://forgecode.dev/docs/tools-reference/).

### Glob Pattern Syntax[​](#glob-pattern-syntax "Direct link to Glob Pattern Syntax")

PatternDescriptionExample`*`Match any characters`mcp_*` matches all MCP tools`?`Match single character`read?` matches `read1`, `read2``[...]`Match character class`tool[123]` matches `tool1`, `tool2`, `tool3`

### Built-in Tools[​](#built-in-tools "Direct link to Built-in Tools")

- **`read`** - Read files and directories
  
  - *Use for*: Code analysis, documentation review, configuration inspection
- **`write`** - Create and modify files
  
  - *Use for*: Generating new code, creating documentation, updating configurations
- **`patch`** - Apply targeted changes to files
  
  - *Use for*: Bug fixes, small modifications, refactoring
- **`remove`** - Delete files
  
  - *Use for*: Cleanup tasks, removing deprecated code
- **`shell`** - Execute shell commands
  
  - *Use for*: Running tests, building projects, system operations
- **`fetch`** - Retrieve external resources
  
  - *Use for*: API calls, downloading dependencies, checking external services
- **`search`** - Search within files
  
  - *Use for*: Finding code patterns, locating specific functions, analyzing codebases
- **`undo`** - Reverse previous changes
  
  - *Use for*: Error recovery, experimentation
- **`plan`** - Create implementation plans
  
  - *Use for*: Breaking down complex tasks, project planning
- **`followup`** - Ask clarifying questions
  
  - *Use for*: Gathering requirements, clarifying ambiguous requests

### MCP Tools (External Integrations)[​](#mcp-tools-external-integrations "Direct link to MCP Tools (External Integrations)")

MCP (Model Context Protocol) tools connect your agents to external services. Once configured, can be accessed using glob patterns.

**Popular integrations:**

- Weather data for real-time information
- Database connections (PostgreSQL, MySQL)
- Email services for notifications
- Browser automation for testing

**Example**: Grant access to all MCP tools automatically:

**Benefits of using glob patterns for MCP tools:**

- **Automatic Access**: New MCP servers you add are automatically available to the agent
- **No Configuration Updates**: Don't need to modify agent definitions when adding MCP tools
- **Flexible Control**: Can still restrict specific MCP tools if needed

Use `/tools` in ForgeCode to see all available tools (MCP tools are listed separately).

Learn more: [MCP Integration Guide](https://forgecode.dev/docs/mcp-integration/)

### Frontend Development Specialist[​](#frontend-development-specialist "Direct link to Frontend Development Specialist")

### Backend API Specialist[​](#backend-api-specialist "Direct link to Backend API Specialist")

### Security Code Auditor[​](#security-code-auditor "Direct link to Security Code Auditor")

Instead of creating agents from scratch, you can customize ForgeCode's built-in agents (ForgeCode, Muse, Sage, Parker, Prime) to match your project needs.

### How Customization Works[​](#how-customization-works "Direct link to How Customization Works")

ForgeCode loads agents in this priority order:

1. **Project-specific** (`.forge/agents/` - highest priority)
2. **Global** (`~/forge/agents/`)
3. **Built-in** (embedded in ForgeCode - lowest priority)

The filename doesn't matter - only the `id` field in the YAML frontmatter must match the built-in agent you want to override.

### Setting Up Agent Customization[​](#setting-up-agent-customization "Direct link to Setting Up Agent Customization")

Create a markdown file in your agents directory with the appropriate `id`:

- `id: "forge"` - customize the ForgeCode agent
- `id: "muse"` - customize the Muse agent
- `id: "sage"` - customize the Sage agent
- `id: "parker"` - customize the Parker agent
- `id: "prime"` - customize the Prime agent

### Customization Example[​](#customization-example "Direct link to Customization Example")

Here's how to customize the ForgeCode agent for frontend development. Create `my-custom-forge.md` in `.forge/agents/`:

### Common Issues and Solutions[​](#common-issues-and-solutions "Direct link to Common Issues and Solutions")

**Agent not appearing in selection list**

1. Verify file location:
   
   - Global: `~/forge/agents/` or `%USERPROFILE%\forge\agents\`
   - Project: `.forge/agents/` (note the dot prefix)
2. Ensure `.md` file extension
3. Check YAML frontmatter is valid
4. Confirm `id` field exists and is unique
5. Restart ForgeCode to reload agents

**"Invalid YAML" errors**

1. Use an online YAML validator to check syntax
2. Use spaces for indentation, not tabs
3. Quote strings containing special characters
4. Use `|` for multiline strings with preserved line breaks
5. Use `>` for multiline strings with folded line breaks

**Agent validation warnings**

1. Check parameter values are within valid ranges (see constraints table)
2. Verify all tools in `tools` array are recognized
3. Ensure `reasoning.max_tokens` &gt; 1024 and &lt; `max_tokens`
4. Add `description` field if agent will be used as a tool

**Agent not behaving as expected**

1. Review system prompt for clarity and specificity
2. Adjust `temperature` (lower = more consistent responses)
3. Make `custom_rules` more specific and actionable
4. Verify appropriate tools are included
5. Check model supports requested features

### Error Message Reference[​](#error-message-reference "Direct link to Error Message Reference")

- `"Agent with id 'example' already exists"` → Duplicate agent ID found
- `"Invalid temperature value: 3.0"` → Temperature outside 0.0-2.0 range
- `"Unknown tool: invalid_tool"` → Tool name not recognized
- `"reasoning.max_tokens must be greater than 1024"` → Reasoning tokens too low

### Writing Effective System Prompts[​](#writing-effective-system-prompts "Direct link to Writing Effective System Prompts")

1. **Be Specific**: Define clear responsibilities and focus areas
2. **Include Examples**: Show the type of output you expect
3. **Set Boundaries**: Specify what the agent should and shouldn't do
4. **Use Structure**: Organize instructions with headers and lists
5. **Test Iteratively**: Refine prompts based on agent behavior

### Configuration Tips[​](#configuration-tips "Direct link to Configuration Tips")

1. **Start Conservative**: Use lower temperature values for consistent behavior
2. **Limit Tools**: Only include tools the agent actually needs
3. **Set Appropriate Limits**: Configure `max_turns` based on expected conversation length
4. **Use Custom Rules**: Add specific guidelines for your project or team
5. **Enable Reasoning**: Use reasoning mode for complex problem-solving agents

### Team Collaboration[​](#team-collaboration "Direct link to Team Collaboration")

1. **Consistent Naming**: Use descriptive, consistent agent IDs and titles
2. **Document Purpose**: Write clear descriptions explaining each agent's role
3. **Share Configurations**: Version control agent definition files with your project
4. **Establish Conventions**: Create team standards for agent organization
5. **Regular Review**: Update agents as project requirements evolve

### Dynamic Prompt Templates[​](#dynamic-prompt-templates "Direct link to Dynamic Prompt Templates")

Agent prompts support Handlebars template variables for context-aware behavior:

**System Prompt Variables:**

- `{{current_time}}` - Current timestamp
- `{{env.cwd}}` - Current working directory path
- `{{env.os}}` - Operating system (macOS, Linux, Windows)
- `{{env.shell}}` - Shell type (bash, zsh, PowerShell)

**User Prompt Variables:**

- `{{current_time}}` - Current timestamp
- `{{event.name}}` - Event identifier (e.g., "agent-id/user\_task\_init")
- `{{event.value}}` - Event payload (user's message, feedback, or task data)

### Environment-Specific Agents[​](#environment-specific-agents "Direct link to Environment-Specific Agents")

Create specialized agents for different deployment contexts:

### Model-Specific Optimization[​](#model-specific-optimization "Direct link to Model-Specific Optimization")

Different models work better with different configurations:

### Provider-Specific Configuration[​](#provider-specific-configuration "Direct link to Provider-Specific Configuration")

You can specify different providers for different use cases:

- OpenAI:

<!--THE END-->

- Requesty

**Important**: Provider names must always be in snake\_case format (lowercase with underscores separating words).

If you encounter issues not covered in this guide:

1. Check ForgeCode startup logs for specific error messages and warnings
2. Test with a minimal agent configuration first to isolate issues
3. Verify your agent definition against the working examples provided
4. Check the ForgeCode documentation for updated tool lists and configuration options
5. Consult the ForgeCode community or support channels for additional assistance

Remember: Custom agents are powerful tools for streamlining your development workflow. Start with simple configurations and gradually add complexity as you become familiar with the options.