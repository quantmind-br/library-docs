---
title: Cognee Extension | goose
url: https://block.github.io/goose/docs/mcp/cognee-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:52.662418127-03:00
rendered_js: true
word_count: 359
summary: This tutorial provides instructions for integrating the Cognee MCP Server with the goose CLI to provide AI agents with knowledge graph memory capabilities.
tags:
    - goose-cli
    - cognee
    - mcp-server
    - knowledge-graph
    - ai-extensions
    - configuration
category: tutorial
---

This tutorial covers how to add the [Cognee MCP Server](https://github.com/topoteretes/cognee/tree/main/cognee-mcp) as a goose extension to enable knowledge graph memory capabilities, connecting to over 30 data sources for enhanced context and retrieval.

TLDR

**Command**

```
uv --directory /path/to/cognee-mcp run python src/server.py
```

**Environment Variables**

```
LLM_API_KEY: <YOUR_OPENAI_API_KEY>
```

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [uv](https://docs.astral.sh/uv/#installation) installed on your system to run this command, as it uses `uv`.

- goose CLI

**Install Cognee:**

```
# Clone and install Cognee
git clone https://github.com/topoteretes/cognee
cd cognee/cognee-mcp
uv sync --dev --all-extras --reinstall

# On Linux, install additional dependencies
sudo apt install -y libpq-dev python3-dev
```

**Configure the extension:**

1. Run the `configure` command:

<!--THE END-->

2. Choose to add a `Command-line Extension`.

```
┌   goose-configure
│
◇  What would you like to configure?
│  Add Extension
│
◆  What type of extension would you like to add?
│  ○ Built-in Extension
│  ● Command-line Extension (Run a local command or script)
│  ○ Remote Extension (Streamable HTTP)
└
```

3. Give your extension a name.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◆  What would you like to call this extension?
│  Cognee
└
```

4. Enter the command to run when this extension is used.

info

Replace `/path/to/cognee-mcp` with the actual path to your cloned cognee-mcp directory.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension 
│
◇  What would you like to call this extension?
│  Cognee
│
◆  What command should be run?
│  uv --directory /path/to/cognee-mcp run python src/server.py
└
```

5. Enter the number of seconds goose should wait for actions to complete before timing out. Default is `300` seconds.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◇  What would you like to call this extension?
│  Cognee
│
◇  What command should be run?
│  uv --directory /path/to/cognee-mcp run python src/server.py
│
◆  Please set the timeout for this tool (in secs):
│  300
└
```

6. Enter a description for this extension.

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◇  What would you like to call this extension?
│  Cognee
│
◇  What command should be run?
│  uv --directory /path/to/cognee-mcp run python src/server.py
│
◇  Please set the timeout for this tool (in secs):
│  300
│
◆  Enter a description for this extension:
│  Knowledge graph memory capabilities with 30+ data source connections
└
```

7. Add an environment variable for this extension.

info

Obtain an API key for your LLM provider and paste it in. By default, this is an [OpenAI API key](https://platform.openai.com/api-keys).

```
┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension
│
◇  What type of extension would you like to add?
│  Command-line Extension
│
◇  What would you like to call this extension?
│  Cognee
│
◇  What command should be run?
│  uv --directory /path/to/cognee-mcp run python src/server.py
│
◇  Please set the timeout for this tool (in secs):
│  300
│
◇  Enter a description for this extension:
│  Knowledge graph memory capabilities with 30+ data source connections
│
◆  Would you like to add environment variables?
│  Yes
│
◇  Environment variable name:
│  LLM_API_KEY
│
◇  Environment variable value:
│  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
│
◇  Add another environment variable?
│  No
│
└  Added Cognee extension
```

## Example Usage[​](#example-usage "Direct link to Example Usage")

Cognee provides knowledge graph memory capabilities for goose, allowing it to remember and connect information across conversations and documents.

LLM

OpenAI's GPT-4o was used for this task.

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> *goose, please cognify this information: "I prefer Python for data analysis and use pandas extensively. My current project involves analyzing customer behavior data." Then search for information about my programming preferences.*

### goose Output[​](#goose-output "Direct link to goose Output")

CLI

Tool Calls

I'll help you store that information in the knowledge graph and then search for your programming preferences.

First, let me cognify the information about your preferences:

**Cognify Status:** Background process launched due to MCP timeout limitations. The information about your Python and pandas preferences for data analysis has been added to the knowledge graph.

Now let me search for information about your programming preferences:

**Search Results:** Based on the knowledge graph, I found information about your programming preferences:

- **Language Preference**: You prefer Python for data analysis
- **Key Libraries**: You use pandas extensively for data manipulation
- **Current Focus**: Your current project involves analyzing customer behavior data
- **Domain**: Data science and analytics workflows
- **Technical Stack**: Python + pandas for data analysis tasks

The knowledge graph has successfully stored and can now retrieve your programming preferences and project context for future conversations.