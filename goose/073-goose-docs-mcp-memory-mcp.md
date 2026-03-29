---
title: Memory Extension | goose
url: https://block.github.io/goose/docs/mcp/memory-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:26.175138873-03:00
rendered_js: true
word_count: 427
summary: This document explains how to enable and use the Memory extension in goose to store, retrieve, and manage persistent information such as project-specific standards and custom configurations.
tags:
    - goose-ai
    - memory-extension
    - mcp-server
    - knowledge-management
    - configuration-guide
    - persistent-storage
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

The Memory extension turns goose into a knowledgeable assistant by allowing you to teach it personalized key information (e.g. commands, code snippets, preferences and configurations) that it can recall and apply later. Whether it’s project-specific (local) or universal (global) knowledge, goose learns and remembers what matters most to you.

This tutorial covers enabling and using the Memory MCP Server, which is a built-in goose extension.

## Configuration[​](#configuration "Direct link to Configuration")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Extensions` in the sidebar
3. Toggle `Memory` on

## Why Use Memory?[​](#why-use-memory "Direct link to Why Use Memory?")

With the Memory extension, you’re not just storing static notes, you’re teaching goose how to assist you better. Imagine telling goose:

> *learn everything about MCP servers and save it to memory.*

Later, you can ask:

> *utilizing our MCP server knowledge help me build an MCP server.*

goose will recall everything you’ve saved as long as you instruct it to remember. This makes it easier to have consistent results when working with goose.

goose loads all saved memories at the start of a session and includes them in every prompt sent to the LLM. For large or detailed instructions, store them in files and instruct goose to reference those files:

> *Remember that if I ask for help writing JavaScript, I want you to refer to "/path/to/javascript\_notes.txt" and follow the instructions in that file.*

## Trigger Words and When to Use Them[​](#trigger-words-and-when-to-use-them "Direct link to Trigger Words and When to Use Them")

goose also recognizes certain trigger words that signal when to store, retrieve, or remove memory.

**Trigger Words****When to Use**rememberStore useful info for later useforgetRemove a stored memorymemoryGeneral memory-related actionssaveSave a command, config, or preferenceremove memoryDelete specific stored dataclear memoryWipe all stored memoriessearch memoryFind previously stored datafind memoryLocate specific saved information

## Example Usage[​](#example-usage "Direct link to Example Usage")

In this example, I’ll show you how to make goose a knowledgeable development assistant by teaching it about your project’s API standards. With the Memory extension, goose can store structured information and recall it when needed, helping you stay consistent in your work.

This means you no longer have to repeat yourself. goose will remember your project’s requirements and automatically apply them to new tasks.

tip

If you frequently work with API standards or other structured knowledge, goose may automatically suggest saving them to memory for you when it detects a pattern in your workflow.

- goose Desktop
- goose CLI

<!--THE END-->

1. Open a new session in goose Desktop

### Step 1: Teach goose Your API Standards[​](#step-1-teach-goose-your-api-standards "Direct link to Step 1: Teach goose Your API Standards")

#### goose Prompt #1[​](#goose-prompt-1 "Direct link to goose Prompt #1")

```
goose, learn our API development standards:

- All endpoints must use TypeScript interfaces
- Error responses follow RFC 7807 Problem Details spec
- Rate limiting headers are required
- Authentication uses JWT in Authorization header
- All endpoints need OpenAPI documentation

Remember this so you can help me follow these practices.
```

#### goose Output[​](#goose-output "Direct link to goose Output")

```
I've learned your API standards. I'll help enforce these requirements when working on API endpoints.

Storing in:
    - Category: development_standards
    - Tags: #api #typescript #security #documentation
    - Scope: global (these are general standards)

I can now help with:
    - API endpoint implementation
    - Error handling patterns
    - Authentication flows
    - Documentation requirements
```

### Step 2: Use Stored Knowledge to Create a New API Endpoint[​](#step-2-use-stored-knowledge-to-create-a-new-api-endpoint "Direct link to Step 2: Use Stored Knowledge to Create a New API Endpoint")

#### goose Prompt # 2[​](#goose-prompt--2 "Direct link to goose Prompt # 2")

```
Help me create a new endpoint for user preferences
```

#### goose Output[​](#goose-output-1 "Direct link to goose Output")

```
I see you need a new endpoint. Based on our API development standards that I have stored in memory, I'll ensure it meets all our requirements.

[.. Checking stored API standards ...]

I've included all our required elements:

✅ TypeScript interfaces
✅ RFC 7807 error response format
✅ Rate limiting
✅ JWT auth header
✅ OpenAPI documentation

Here's your compliant endpoint:

interface UserPreferences {
    userId: string;
    theme: 'light' | 'dark';
    notifications: boolean;
    timezone: string;
}

interface ErrorResponse { 
    type: string;
    title: string;
    status: number;
    detail: string;
    instance: string;
}

@Route('/api/users/:userId/preferences')
class UserPreferencesController {
    @Get()
    @RateLimit(100)  // Adding required rate limiting
    @OpenAPI({ ... }) // Including mandatory OpenAPI docs
    async getUserPreferences(
        @Header('Authorization') token: string,  // JWT auth as per our standard
        @Param('userId') userId: string
    ): Promise<UserPreferences | ErrorResponse> {
        // Implementation following our error handling pattern
    }
}

Would you like me to implement the full endpoint logic?
```