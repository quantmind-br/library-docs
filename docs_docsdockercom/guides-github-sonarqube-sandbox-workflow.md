---
title: Build workflow
url: https://docs.docker.com/guides/github-sonarqube-sandbox/workflow/
source: llms
fetched_at: 2026-01-24T14:04:56.456175595-03:00
rendered_js: false
word_count: 806
---

## Build a code quality check workflow

In this section, you'll build a complete code quality automation workflow step-by-step. You'll start by creating an E2B sandbox with GitHub and SonarQube MCP servers, then progressively add functionality until you have a production-ready workflow that analyzes code quality and creates pull requests.

By working through each step sequentially, you'll learn how MCP servers work, how to interact with them through Claude, and how to chain operations together to build powerful automation workflows.

Before you begin, make sure you have:

- E2B account with [API access](https://e2b.dev/docs/api-key)
- [Anthropic API key](https://docs.claude.com/en/api/admin-api/apikeys/get-api-key)
  
  > This example uses Claude CLI which comes pre-installed in E2B sandboxes, but you can adapt the example to work with other AI assistants of your choice. See [E2B's MCP documentation](https://e2b.dev/docs/mcp/quickstart) for alternative connection methods.
- GitHub account with:
  
  - A repository containing code to analyze
  - [Personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with `repo` scope
- SonarCloud account with:
  
  - [Organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/resources-structure/organization) created
  - [Project configured](https://docs.sonarsource.com/sonarqube-community-build/project-administration/creating-and-importing-projects) for your repository
  - [User token](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/administering-tokens) generated
- Language runtime installed:
  
  - TypeScript: [Node.js 18+](https://nodejs.org/en/download)
  - Python: [Python 3.8+](https://www.python.org/downloads/)

> This guide uses Claude's `--dangerously-skip-permissions` flag to enable automated command execution in E2B sandboxes. This flag bypasses permission prompts, which is appropriate for isolated container environments like E2B where sandboxes are disposable and separate from your local machine.
> 
> However, be aware that Claude can execute any commands within the sandbox, including accessing files and credentials available in that environment. Only use this approach with trusted code and workflows. For more information, see [Anthropic's guidance on container security](https://docs.anthropic.com/en/docs/claude-code/devcontainer).

1. Create a new directory for your workflow and initialize Node.js:
2. Open `package.json` and configure it for ES modules:
3. Install required dependencies:
4. Create a `.env` file in your project root:
5. Add your API keys and configuration, replacing the placeholders with your actual credentials:
6. Protect your credentials by adding `.env` to `.gitignore`:

<!--THE END-->

1. Create a new directory for your workflow:
2. Create a virtual environment and activate it:
3. Install required dependencies:
4. Create a `.env` file in your project root:
5. Add your API keys and configuration, replacing the placeholders with your actual credentials:
6. Protect your credentials by adding `.env` to `.gitignore`:

Let's start by creating a sandbox and verifying the MCP servers are configured correctly.

Create a file named `01-test-connection.ts` in your project root:

Run this script to verify your setup:

Create a file named `01_test_connection.py` in your project root:

Run this script to verify your setup:

Your output should look similar to the following example:

You've just learned how to create an E2B sandbox with multiple MCP servers configured. The `betaCreate` method initializes a cloud environment with Claude CLI and your specified MCP servers.

MCP servers expose tools that Claude can call. The GitHub MCP server provides repository management tools, while SonarQube provides code analysis tools. By listing their tools, you know what operations are possible.

To try listing MCP tools:

Create `02-list-tools.ts`:

Run the script:

Create `02_list_tools.py`:

Run the script:

In the console, you should see a list of MCP tools:

Let's try testing GitHub using MCP tools. Start simple by listing repository issues.

Create `03-test-github.ts`:

Run the script:

Create `03_test_github.py`:

Run the script:

You should see Claude use the GitHub MCP tools to list your repository's issues:

You can now send prompts to Claude and interact with GitHub through natural language. Claude decides what tool to call based on your prompt.

Let's analyze code quality using SonarQube MCP tools.

Create `04-test-sonarqube.ts`:

Run the script:

Create `04_test_sonarqube.py`:

Run the script:

> This script may take a few minutes to run.

You should see Claude output SonarQube analysis results:

You can now use SonarQube MCP tools to analyze code quality through natural language. You can retrieve quality metrics, identify issues, and understand what code needs fixing.

Now, let's teach Claude to fix code based on quality issues discovered by SonarQube.

Create `05-fix-code-issue.ts`:

Run the script:

Create `05_fix_code_issue.py`:

Run the script:

> This script may take a few minutes to run.

Claude will analyze your repository and fix a code quality issue:

You can now use GitHub and SonarQube MCP tools in the same workflow to read files, make code changes, and commit them.

Finally, let's build the complete workflow: analyze quality, fix issues, and create a PR only if improvements are made.

Create `06-quality-gated-pr.ts`:

Run the script:

Create `06_quality_gated_pr.py`:

Run the script:

> This script may take a few minutes to run.

Claude will run the entire workflow, creating a quality improvement and opening a PR in GitHub:

You've now built a complete, multi-step workflow with conditional logic. Claude analyzes quality with SonarQube, makes fixes using GitHub tools, verifies improvements, and only creates a PR if quality actually improves.

Production workflows need error handling. Let's make the workflow more robust.

Create `07-robust-workflow.ts`:

Run the script:

Create `07_robust_workflow.py`:

Run the script:

Claude will run the entire workflow, and if it encounters an error, respond with robust error messaging.

In the next section, you'll customize your workflow for your needs.