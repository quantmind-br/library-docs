---
title: Building Custom Extensions | goose
url: https://block.github.io/goose/docs/tutorials/custom-extensions
source: github_pages
fetched_at: 2026-01-22T22:16:13.248177146-03:00
rendered_js: true
word_count: 903
summary: This guide provides step-by-step instructions for extending goose functionality by building custom MCP servers using the Python SDK.
tags:
    - goose
    - mcp
    - python-sdk
    - custom-extensions
    - mcp-server
    - model-context-protocol
category: tutorial
---

goose allows you to extend its functionality by creating your own custom extensions, which are built as MCP servers. These extensions are compatible with goose because it adheres to the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). MCP is an open protocol that standardizes how applications provide context to LLMs. It enables a consistent way to connect LLMs to various data sources and tools, making it ideal for extending functionality in a structured and interoperable way. 

In this guide, we build an MCP server using the [Python SDK for MCP](https://github.com/modelcontextprotocol/python-sdk). We’ll demonstrate how to create an MCP server that reads Wikipedia articles and converts them to Markdown, integrate it as an extension in goose. You can follow a similar process to develop your own custom extensions for goose.

You can check out other example servers in the [MCP servers repository](https://github.com/modelcontextprotocol/servers). MCP SDKs are also available for other common languages, such as [Typescript](https://github.com/modelcontextprotocol/typescript-sdk) and [Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk).

* * *

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you begin, ensure you have the following installed on your system:

- **Python 3.13 or higher** - Required for the MCP server
- [**uv**](https://docs.astral.sh/uv/) - Python package manager used in this tutorial
- **Node.js and npm** - Only required if you want to use the MCP Inspector development tool in [Step 4](#step-4-test-your-mcp-server).

* * *

## Step 1: Initialize Your Project[​](#step-1-initialize-your-project "Direct link to Step 1: Initialize Your Project")

The first step is to create a new project using [uv](https://docs.astral.sh/uv/getting-started/). We will name our project `mcp-wiki`.

Run the following commands in your terminal to set up a basic structure for your MCP server:

```
uv init --lib mcp-wiki
cd mcp-wiki

mkdir -p src/mcp_wiki
touch src/mcp_wiki/server.py
touch src/mcp_wiki/__main__.py
```

Your project directory structure should look like this:

```
.
├── README.md
├── pyproject.toml
└── src
    └── mcp_wiki
        ├── __init__.py   # Primary CLI entry point
        ├── __main__.py   # To enable running as a Python module
        ├── py.typed      # Indicates the package supports type hints
        └── server.py     # Your MCP server code (tool, resources, prompts)
```

* * *

## Step 2: Write Your MCP Server Code[​](#step-2-write-your-mcp-server-code "Direct link to Step 2: Write Your MCP Server Code")

In this step, we’ll implement the core functionality of the MCP server. Here is a breakdown of the key components:

1. **`server.py`** : This file holds the main MCP server code. In this example, we define a single tool to read Wikipedia articles. You can add your own custom tools, resources, and prompts here.
2. **`__init__.py`** : This is the primary CLI entry point for your MCP server.
3. **`__main__.py`** : This file allows your MCP server to be executed as a Python module.

Below is the example implementation for the Wikipedia MCP server:

### `server.py`[​](#serverpy "Direct link to serverpy")

```
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from html2text import html2text
from urllib.parse import urlparse

from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

mcp = FastMCP("wiki")

@mcp.tool()
defread_wikipedia_article(url:str)->str:
"""
    Fetch a Wikipedia article at the provided URL, parse its main content,
    convert it to Markdown, and return the resulting text.

    Usage:
        read_wikipedia_article("https://en.wikipedia.org/wiki/Python_(programming_language)")
    """
try:
# Validate input
ifnot url.startswith("http"):
raise ValueError("URL must start with http or https.")

# SSRF protection: only allow Wikipedia domains
        parsed = urlparse(url)
        hostname = parsed.netloc.lower()

# Allow wikipedia.org or *.wikipedia.org subdomains only
if hostname !='wikipedia.org'andnot hostname.endswith('.wikipedia.org'):
raise ValueError(f"Only Wikipedia URLs are allowed. Got: {parsed.netloc}")

# Add User-Agent header to avoid 403 from Wikipedia
        headers ={
'User-Agent':'MCP-Wiki/1.0 (Educational purposes; Python requests)'
}
        response = requests.get(url, headers=headers, timeout=10)
if response.status_code !=200:
raise McpError(
                ErrorData(
                    code=INTERNAL_ERROR,
                    message=f"Failed to retrieve the article. HTTP status code: {response.status_code}"
)
)

        soup = BeautifulSoup(response.text,"html.parser")
        content_div = soup.find("div",{"id":"mw-content-text"})
ifnot content_div:
raise McpError(
                ErrorData(
                    code=INVALID_PARAMS,
                    message="Could not find the main content on the provided Wikipedia URL."
)
)

# Convert to Markdown
        markdown_text = html2text(str(content_div))
return markdown_text

except ValueError as e:
raise McpError(ErrorData(code=INVALID_PARAMS, message=str(e)))from e
except RequestException as e:
raise McpError(ErrorData(code=INTERNAL_ERROR, message=f"Request error: {str(e)}"))from e
except Exception as e:
raise McpError(ErrorData(code=INTERNAL_ERROR, message=f"Unexpected error: {str(e)}"))from e
```

### `__init__.py`[​](#__init__py "Direct link to __init__py")

```
import argparse
from.server import mcp

defmain():
"""MCP Wiki: Read Wikipedia articles and convert them to Markdown."""
    parser = argparse.ArgumentParser(
        description="Gives you the ability to read Wikipedia articles and convert them to Markdown."
)
    parser.parse_args()
    mcp.run()

if __name__ =="__main__":
    main()
```

### `__main__.py`[​](#__main__py "Direct link to __main__py")

```
from mcp_wiki import main

main()
```

* * *

## Step 3: Define Project Configuration[​](#step-3-define-project-configuration "Direct link to Step 3: Define Project Configuration")

Configure your project using `pyproject.toml`. This configuration defines the CLI script so that the mcp-wiki command is available as a binary. Below is an example configuration:

```
[project]
name = "mcp-wiki"
version = "0.1.0"
description = "MCP Server for Wikipedia"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "beautifulsoup4>=4.14.0",
    "html2text>=2025.4.15",
    "mcp[cli]>=1.25.0",
    "requests>=2.32.3",
]

[project.scripts]
mcp-wiki = "mcp_wiki:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

* * *

## Step 4: Test Your MCP Server[​](#step-4-test-your-mcp-server "Direct link to Step 4: Test Your MCP Server")

Verify that your MCP server is running in the MCP Inspector (a browser-based development tool) or the server CLI.

- In MCP Inspector
- In the CLI

info

MCP Inspector requires Node.js and npm installed on your computer.

1. Setup the project environment:
2. Activate your virtual environment:
   
   ```
   source .venv/bin/activate
   ```
3. Run your server in development mode:
   
   ```
   mcp dev src/mcp_wiki/server.py
   ```
   
   MCP Inspector should open automatically in your browser. On first run, you'll be prompted to install `@modelcontextprotocol/inspector`.
4. Test the tool:
   
   1. Click `Connect` to initialize your MCP server
   2. On the `Tools` tab, click `List Tools` and click the `read_wikipedia_article` tool
   3. Enter `https://en.wikipedia.org/wiki/Bangladesh` for the URL and click `Run Tool`

[![MCP Inspector UI](https://block.github.io/goose/assets/images/custom-extension-mcp-inspector-db9f2e51b48d2529a9f90731c2a669db.png)](https://block.github.io/goose/assets/files/custom-extension-mcp-inspector-db9f2e51b48d2529a9f90731c2a669db.png)

* * *

## Step 5: Integrate with goose[​](#step-5-integrate-with-goose "Direct link to Step 5: Integrate with goose")

To add your MCP server as an extension in goose:

1. Build the extension binary:
2. Open goose Desktop and click the button in the top-left to open the sidebar
3. Click `Extensions` in the sidebar
4. Set the `Type` to `STDIO`
5. Provide a name and description for your extension
6. In the `Command` field, provide the absolute path to your executable:
   
   ```
   uv run /full/path/to/mcp-wiki/.venv/bin/mcp-wiki
   ```
   
   For example:
   
   ```
   uv run /Users/smohammed/Development/mcp/mcp-wiki/.venv/bin/mcp-wiki
   ```

Rebuild binary after changes

To see any changes you make to your MCP server code after integrating with goose, re-run `uv pip install .` and then restart goose Desktop.

For the purposes of this guide, we'll run the local version. Alternatively, you can publish your package to PyPI. Once published, the server can be run directly using `uvx`. For example:

* * *

## Step 6: Use Your Extension in goose[​](#step-6-use-your-extension-in-goose "Direct link to Step 6: Use Your Extension in goose")

Once integrated, you can start using your extension in goose. Open the goose chat interface and call your tool as needed.

You can verify that goose has picked up the tools from your custom extension by asking it "what tools do you have?"

![goose Chat - Ask about tools](https://block.github.io/goose/assets/images/custom-extension-tools-9d440447ae99b18ae92819e652148abe.png)

Then, you can try asking questions that require using the extension you added.

![goose Chat - Use custom extension](https://block.github.io/goose/assets/images/custom-extension-chat-dade20fed6d387174db32667977bdae1.png)

🎉 **Congratulations!** You’ve successfully built and integrated a custom MCP server with goose.

* * *

## Advanced Features for MCP Extensions[​](#advanced-features-for-mcp-extensions "Direct link to Advanced Features for MCP Extensions")

goose supports advanced MCP features that can enhance your extensions.

### MCP Sampling: AI-Powered Tools[​](#mcp-sampling-ai-powered-tools "Direct link to MCP Sampling: AI-Powered Tools")

[**MCP Sampling**](https://block.github.io/goose/docs/guides/mcp-sampling) allows your MCP servers to request AI completions from goose's LLM, transforming simple tools into intelligent agents.

**Key Benefits:**

- Your MCP server doesn't need its own OpenAI/Anthropic API key
- Tools can analyze data, provide explanations, and make intelligent decisions
- Enhanced user experience with smarter, more contextual responses
- Secure by design: requests are isolated and attributed automatically

**Getting Started:**

- Use the `sampling/createMessage` method in your MCP server to request AI assistance
- [goose's implementation](https://github.com/block/goose/blob/main/crates/goose/src/agents/mcp_client.rs) currently supports text and image content types
- goose automatically advertises sampling capability to all MCP servers

**Use Cases:** Document summarization, smart search filtering, code analysis, data insights

**Learn More:** See the [MCP Specification](https://modelcontextprotocol.io/specification/draft/client/sampling) for technical details.

### MCP Apps: Interactive Extensions[​](#mcp-apps-interactive-extensions "Direct link to MCP Apps: Interactive Extensions")

[**MCP Apps**](https://block.github.io/goose/docs/tutorials/building-mcp-apps) enable rich, interactive user interfaces instead of text-only responses.

**Key Benefits:**

- Return interactive UI components from your MCP server tools
- Components render securely in isolated sandboxes within goose Desktop
- Real-time user interactions trigger callbacks to your server

**Use Cases:** Interactive forms, data visualizations, booking interfaces, configuration wizards

**Learn More:** [Building MCP Apps Tutorial](https://block.github.io/goose/docs/tutorials/building-mcp-apps)

note

goose also supports [MCP-UI](https://block.github.io/goose/docs/guides/interactive-chat/mcp-ui), but MCP Apps is the recommended path for new extensions.