---
title: Troubleshoot
url: https://docs.docker.com/guides/github-sonarqube-sandbox/troubleshoot/
source: llms
fetched_at: 2026-01-24T14:10:10.312495884-03:00
rendered_js: false
word_count: 380
summary: This document provides troubleshooting solutions for common issues encountered when building code quality workflows using E2B sandboxes and MCP servers.
tags:
    - e2b-sandbox
    - mcp-server
    - troubleshooting
    - error-handling
    - github-api
    - sonarqube
    - claude-ai
category: guide
---

## Troubleshoot code quality workflows

Table of contents

* * *

This page covers common issues you might encounter when building code quality workflows with E2B sandboxes and MCP servers, along with their solutions.

If you're experiencing problems not covered here, check the [E2B documentation](https://e2b.dev/docs).

## [MCP tools not available](#mcp-tools-not-available)

Issue: Claude reports `I don't have any MCP tools available`.

Solution:

1. Verify you're using the authorization header:
   
   ```
   --header "Authorization: Bearer ${mcpToken}"
   ```
2. Check you're waiting for MCP initialization.
   
   ```
   // typescript
   await new Promise((resolve) => setTimeout(resolve, 1000));
   ```
   
   ```
   # python
   await asyncio.sleep(1)
   ```
3. Ensure credentials are in both `envs` and `mcp` configuration:
   
   ```
   // typescript
   const sbx = await Sandbox.betaCreate({
     envs: {
       ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY!,
       GITHUB_TOKEN: process.env.GITHUB_TOKEN!,
       SONARQUBE_TOKEN: process.env.SONARQUBE_TOKEN!,
     },
     mcp: {
       githubOfficial: {
         githubPersonalAccessToken: process.env.GITHUB_TOKEN!,
       },
       sonarqube: {
         org: process.env.SONARQUBE_ORG!,
         token: process.env.SONARQUBE_TOKEN!,
         url: "https://sonarcloud.io",
       },
     },
   });
   ```
   
   ```
   # python
   sbx = await AsyncSandbox.beta_create(
       envs={
           "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
           "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"),
           "SONARQUBE_TOKEN": os.getenv("SONARQUBE_TOKEN"),
       },
       mcp={
           "githubOfficial": {
               "githubPersonalAccessToken": os.getenv("GITHUB_TOKEN"),
           },
           "sonarqube": {
               "org": os.getenv("SONARQUBE_ORG"),
               "token": os.getenv("SONARQUBE_TOKEN"),
               "url": "https://sonarcloud.io",
           },
       },
   )
   ```
4. Verify your API tokens are valid and have proper scopes.

## [GitHub tools work but SonarQube doesn't](#github-tools-work-but-sonarqube-doesnt)

Issue: GitHub MCP tools load but SonarQube tools don't appear.

Solution: SonarQube MCP server requires GitHub to be configured simultaneously. Always include both servers in your sandbox configuration, even if you're only testing one.

```
// Include both servers even if only using one
const sbx = await Sandbox.betaCreate({
  envs: {
    ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY!,
    GITHUB_TOKEN: process.env.GITHUB_TOKEN!,
    SONARQUBE_TOKEN: process.env.SONARQUBE_TOKEN!,
  },
  mcp: {
    githubOfficial: {
      githubPersonalAccessToken: process.env.GITHUB_TOKEN!,
    },
    sonarqube: {
      org: process.env.SONARQUBE_ORG!,
      token: process.env.SONARQUBE_TOKEN!,
      url: "https://sonarcloud.io",
    },
  },
});
```

```
# Include both servers even if only using one
sbx = await AsyncSandbox.beta_create(
    envs={
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
        "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"),
        "SONARQUBE_TOKEN": os.getenv("SONARQUBE_TOKEN"),
    },
    mcp={
        "githubOfficial": {
            "githubPersonalAccessToken": os.getenv("GITHUB_TOKEN"),
        },
        "sonarqube": {
            "org": os.getenv("SONARQUBE_ORG"),
            "token": os.getenv("SONARQUBE_TOKEN"),
            "url": "https://sonarcloud.io",
        },
    },
)
```

## [Claude can't access private repositories](#claude-cant-access-private-repositories)

Issue: "I don't have access to that repository".

Solution:

1. Verify your GitHub token has `repo` scope (not just `public_repo`).
2. Test with a public repository first.
3. Ensure the repository owner and name are correct in your `.env`:
   
   ```
   GITHUB_OWNER=your_github_username
   GITHUB_REPO=your_repository_name
   ```
   
   ```
   GITHUB_OWNER=your_github_username
   GITHUB_REPO=your_repository_name
   ```

## [Workflow times out or runs too long](#workflow-times-out-or-runs-too-long)

Issue: Workflow doesn't complete or Claude credits run out.

Solutions:

1. Use `timeoutMs: 0` (TypeScript) or `timeout_ms=0` (Python) for complex workflows to allow unlimited time:
   
   ```
   await sbx.commands.run(
     `echo '${prompt}' | claude -p --dangerously-skip-permissions`,
     {
       timeoutMs: 0, // No timeout
       onStdout: console.log,
       onStderr: console.log,
     },
   );
   ```
   
   ```
   await sbx.commands.run(
       f"echo '{prompt}' | claude -p --dangerously-skip-permissions",
       timeout_ms=0,  # No timeout
       on_stdout=print,
       on_stderr=print,
   )
   ```
2. Break complex workflows into smaller, focused tasks.
3. Monitor your Anthropic API credit usage.
4. Add checkpoints in prompts: "After each step, show progress before continuing".

## [Sandbox cleanup errors](#sandbox-cleanup-errors)

Issue: Sandboxes aren't being cleaned up properly, leading to resource exhaustion.

Solution: Always use proper error handling with cleanup in the `finally` block:

```
async function robustWorkflow() {
  let sbx: Sandbox | undefined;
  try {
    sbx = await Sandbox.betaCreate({
      // ... configuration
    });
    // ... workflow logic
  } catch (error) {
    console.error("Workflow failed:", error);
    process.exit(1);
  } finally {
    if (sbx) {
      console.log("Cleaning up sandbox...");
      await sbx.kill();
    }
  }
}
```

```
async def robust_workflow():
    sbx = None
    try:
        sbx = await AsyncSandbox.beta_create(
            # ... configuration
        )
        # ... workflow logic
    except Exception as error:
        print(f"Workflow failed: {error}")
        sys.exit(1)
    finally:
        if sbx:
            print("Cleaning up sandbox...")
            await sbx.kill()
```

## [Environment variable not loading](#environment-variable-not-loading)

Issue: Script fails with "undefined" or "None" for environment variables.

Solution:

1. Ensure `dotenv` is loaded at the top of your file:
2. Verify the `.env` file is in the same directory as your script.
3. Check variable names match exactly (case-sensitive):
   
   ```
   // .env file
   GITHUB_TOKEN = ghp_xxxxx;
   // In code
   process.env.GITHUB_TOKEN; // Correct
   process.env.github_token; // Wrong - case doesn't match
   ```

<!--THE END-->

1. Ensure `dotenv` is loaded at the top of your file:
   
   ```
   from dotenv import load_dotenv
   load_dotenv()
   ```
2. Verify the `.env` file is in the same directory as your script.
3. Check variable names match exactly (case-sensitive):
   
   ```
   # .env file
   GITHUB_TOKEN=ghp_xxxxx
   # In code
   os.getenv("GITHUB_TOKEN")  # Correct
   os.getenv("github_token")  # Wrong - case doesn't match
   ```

## [SonarQube returns empty results](#sonarqube-returns-empty-results)

Issue: SonarQube analysis returns no projects or issues.

Solution:

1. Verify your SonarCloud organization key is correct.
2. Ensure you have at least one project configured in SonarCloud.
3. Check that your SonarQube token has the necessary permissions.
4. Confirm your project has been analyzed at least once in SonarCloud.