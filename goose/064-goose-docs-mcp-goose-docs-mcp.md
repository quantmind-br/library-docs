---
title: goose Docs Extension | goose
url: https://block.github.io/goose/docs/mcp/goose-docs-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:18.444934385-03:00
rendered_js: true
word_count: 402
summary: This tutorial explains how to install and configure the goose Docs MCP Server extension to enable goose to access and answer questions about its own documentation.
tags:
    - goose
    - mcp-server
    - extension-installation
    - documentation
    - git-mcp
category: tutorial
---

This tutorial covers how to add the [goose Docs MCP Server](https://github.com/idosal/git-mcp) as a goose extension to enable goose to answer questions about itself.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=mcp-remote&arg=https%3A%2F%2Fblock.gitmcp.io%2Fgoose%2F&id=goose-docs&name=goose%20Docs&description=GitMCP%20for%20goose%20documentation)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

GitMCP allows you to convert any Git repository into a goose extension. The goose Docs MCP Server is a great example of this, as it provides a way for goose to answer questions about itself.

Let's ask goose to create a recipe for us! It will use the goose Docs MCP Server to find the relevant information.

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
hey goose, I want to create a recipe for automated code review that my development team can use. Can you look at the goose documentation to understand the recipe format, then create a recipe that:


1. Reviews pull requests for:

- Code quality issues and best practices
- Security vulnerabilities
- Missing unit tests
- Performance concerns

2. Should be parameterized so teams can customize:

- Programming language (Python, JavaScript, etc.)
- Minimum test coverage threshold
- Specific coding standards to enforce

3. Should output structured results that can be parsed by CI/CD systems

Please research the recipe format first using the goose Docs extension, then create a complete recipe file with proper YAML structure, parameters, and any needed extensions. 
Make it something a development team could immediately use in their workflow.
```

### goose Output[​](#goose-output "Direct link to goose Output")

Desktop

Perfect! I've created a comprehensive automated code review recipe based on the goose documentation research. Here's what I've built for your development team:

#### 📋 Recipe Overview[​](#-recipe-overview "Direct link to 📋 Recipe Overview")

The **Automated Code Review** recipe (`automated-code-review.yaml`) provides:

#### ✅ **Core Review Areas**[​](#-core-review-areas "Direct link to -core-review-areas")

1. **Code Quality & Best Practices** - Architecture, naming, complexity, documentation
2. **Security Vulnerability Assessment** - OWASP Top 10, input validation, auth issues
3. **Test Coverage Analysis** - Missing tests, coverage thresholds, test quality
4. **Performance Concerns** - Bottlenecks, algorithm complexity, resource management
5. **Technical Debt Assessment** - Refactoring needs, maintainability issues

#### 🔧 **Parameterization Features**[​](#-parameterization-features "Direct link to -parameterization-features")

- **`programming_language`** - Python, JavaScript, Java, Go, Rust, TypeScript, etc.
- **`min_test_coverage`** - Customizable threshold (default: 80%)
- **`coding_standards`** - PEP8, ESLint, Google Style Guide, company-specific
- **`security_focus`** - Basic, standard, or comprehensive security analysis
- **`performance_analysis`** - Enable/disable performance review
- **`exclude_patterns`** - Skip certain files/directories

#### 📊 **Structured CI/CD Output**[​](#-structured-cicd-output "Direct link to -structured-cicd-output")

The recipe outputs a comprehensive JSON structure with:

- **Overall quality score** and recommendation (approve/request changes/reject)
- **Categorized issues** with severity levels and specific file locations
- **Security vulnerabilities** with CWE IDs and remediation steps
- **Test coverage metrics** and missing test recommendations
- **Performance concerns** with optimization suggestions
- **Technical debt assessment** with effort estimates
- **CI/CD metadata** for pipeline integration

#### 🚀 **Usage Examples**[​](#-usage-examples "Direct link to -usage-examples")

#### Basic Usage:[​](#basic-usage "Direct link to Basic Usage:")

```
goose run automated-code-review.yaml \
  --repository_path ./my-project \
  --programming_language Python
```

#### Advanced Usage:[​](#advanced-usage "Direct link to Advanced Usage:")

```
goose run automated-code-review.yaml \
  --repository_path ./my-project \
  --programming_language JavaScript \
  --min_test_coverage 85 \
  --coding_standards ESLint \
  --security_focus comprehensive \
  --exclude_patterns "*.test.js,dist/*,node_modules/*"
```

#### 🔧 **CI/CD Integration**[​](#-cicd-integration "Direct link to -cicd-integration")

The structured JSON output makes it perfect for CI/CD pipelines:

```
# Example GitHub Actions integration
-name: Run Code Review
run:|
    goose run automated-code-review.yaml \
      --repository_path . \
      --programming_language ${{ matrix.language }} \
      --output review-results.json

-name: Process Results
run:|
    # Parse JSON results for pipeline decisions
    RECOMMENDATION=$(jq -r '.review_summary.recommendation' review-results.json)
    if [ "$RECOMMENDATION" = "reject" ]; then
      exit 1
    fi
```

#### 📁 **File Structure**[​](#-file-structure "Direct link to -file-structure")

The recipe is saved as `automated-code-review.yaml` in your current directory and includes:

- Proper YAML structure following goose recipe format
- Comprehensive parameter definitions with defaults
- Built-in developer extension for file system access
- Detailed JSON schema for structured output
- Template syntax for parameter substitution

Your development team can immediately start using this recipe by placing it in their project repositories and customizing the parameters for their specific needs!

### Generated Recipe File[​](#generated-recipe-file "Direct link to Generated Recipe File")

automated-code-review.yaml