---
title: Execute Browser Code - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/browser-execute
source: sitemap
fetched_at: 2026-03-23T07:26:16.684229-03:00
rendered_js: false
word_count: 204
summary: This document defines the API endpoint for executing arbitrary code within a sandboxed browser environment, detailing request parameters and response structures.
tags:
    - api-reference
    - code-execution
    - browser-automation
    - firecrawl-api
    - web-scraping
category: api
---

Execute code in a browser session

HeaderValue`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Request Body

ParameterTypeRequiredDefaultDescription`code`stringYes-Code to execute (1-100,000 characters)`language`stringNo`"node"`Language of the code: `"python"`, `"node"`, or `"bash"` (for agent-browser CLI commands)`timeout`numberNo-Execution timeout in seconds (1-300)

## Response

FieldTypeDescription`success`booleanWhether the code executed successfully`stdout`stringStandard output from the code execution`result`stringStandard output from the code execution`stderr`stringStandard error output from the code execution`exitCode`numberExit code of the executed process`killed`booleanWhether the process was killed due to timeout`error`stringError message if execution failed (only present on failure)

### Example Request

```
curl -X POST "https://api.firecrawl.dev/v2/browser/550e8400-e29b-41d4-a716-446655440000/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\")\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }'
```

### Example Response (Success)

```
{
  "success": true,
  "result": "Example Domain"
}
```

### Example Response (Error)

```
{
  "success": true,
  "error": "TimeoutError: page.goto: Timeout 30000ms exceeded."
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Body

Code to execute in the browser sandbox

Required string length: `1 - 100000`

Language of the code to execute. Use `node` for JavaScript or `bash` for agent-browser CLI commands.

Available options:

`python`,

`node`,

`bash`

Execution timeout in seconds

Required range: `1 <= x <= 300`

#### Response

Code executed successfully

Standard output from the code execution

Standard output (alias for stdout)

Standard error output from the code execution

Exit code of the executed process

Whether the process was killed due to timeout

Error message if the code raised an exception