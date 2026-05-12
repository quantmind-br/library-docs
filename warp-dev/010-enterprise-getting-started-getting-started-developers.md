---
title: Getting started for developers | Enterprise | Warp
url: https://docs.warp.dev/enterprise/getting-started/getting-started-developers
source: sitemap
fetched_at: 2026-04-29T15:06:00.045910787-03:00
rendered_js: false
word_count: 860
summary: This document provides a comprehensive guide for enterprise developers on installing, configuring, and leveraging Warp terminal features including Oz agents, codebase context, agent profiles, and collaboration tools.
tags:
    - warp-terminal
    - enterprise-setup
    - oz-agents
    - codebase-context
    - mcp-protocol
    - team-collaboration
    - terminal-productivity
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
This guide helps developers get up and running with their team in Warp. When you use agents in Warp, you're using **Oz agents**—Warp's programmable agent for running and coordinating agents at scale, locally or in the cloud.

> [!tip]
> New to Warp Enterprise? Try the [[012-enterprise-getting-started-quickstart|Enterprise quickstart]] for a 10-minute walkthrough.

## Step 1: Download and install Warp

Warp supports macOS, Linux, and Windows.

| Platform | Download | Requirements |
|---|---|---|
| macOS | `.dmg` installer | macOS 10.15 Catalina+ |
| Linux | `.deb`, `.rpm`, or install script | — |
| Windows | `.exe` installer | Windows 10+ |

**Install:**
- **macOS**: Open `.dmg`, drag Warp to Applications, launch from Applications or Spotlight.
- **Linux**: Run the installer or script.
- **Windows**: Run `.exe`, follow the wizard, launch from Start menu.

## Step 2: Log in to your team

### Logging in with SSO

1. Launch Warp, log in or create an account.
2. Click **Continue with SSO**.
3. Enter your work email or domain.
4. Complete authentication with your identity provider.

> [!warning]
> Do not launch Warp directly from your SSO provider's app portal (e.g., Okta dashboard)—this causes errors. Always log in through [app.warp.dev/login](https://app.warp.dev/login).

### Logging in with an invite link

1. Click the invite link in your email.
2. Log in via SSO if configured, otherwise use Google, GitHub, or email.
3. You're automatically added to your team.

### Linking an existing account to SSO

1. Log in with your original method (email, Google, or GitHub).
2. Follow prompts to link to SSO.
3. Use **Continue with SSO** going forward.

## Step 3: Set up key features

### Codebase Context

Codebase Context indexes Git repositories so agents understand your code and provide accurate, context-aware responses.

**Enable indexing:**
1. Go to **Settings** > **Code** > **Indexing and projects**.
2. Toggle **Enable Codebase Indexing** on.
3. Optionally enable **Index new folders by default**.

> [!warning]
> Codebase Context may be controlled by your team admin. Contact them if you don't see these settings.

**Index a repository:**
1. Navigate to a Git repo in your terminal.
2. Run `/init`.
3. Warp begins indexing. You'll be prompted to create an `AGENTS.md` file (optional but recommended).

**What gets indexed:**
- All Git-tracked files
- Up to 200,000 files per repository
- Files in `.gitignore` or `.warpindexingignore` are skipped

**Privacy:** Code is sent to Warp's servers for embedding creation. Only embeddings are stored—not the source code. For Oz cloud agents, code snippets may be stored as part of conversation records when agents create or modify files.

### Agent Profiles

Agent Profiles configure how Oz agents behave: model selection, autonomy, tools, and permissions.

**Create a profile:**
1. Go to **Settings** > **Agents** > **Profiles**.
2. Click **New Profile**.
3. Configure name, model, autonomy level, tools, and permissions.
4. Save.

**Use profiles by task:**
- **High autonomy** for routine tasks (writing tests, updating docs)
- **Low autonomy** for sensitive operations (infrastructure changes)
- **Specific models** for cost optimization or task requirements

### Warp Drive

Warp Drive is your workspace for sharing Workflows, Notebooks, Prompts, Rules, and Environment Variables.

**Access:** Click the tools panel icon in the top left, then the Warp Drive icon.

**Sections:**
- **Team** (top) — shared resources
- **Personal** (bottom) — your individual resources

**Resources:**
- **Workflows** — parameterized commands (deploy scripts, environment setup)
- **Notebooks** — interactive runbooks (markdown + executable code)
- **Prompts** — saved agent prompts ("review this PR", "write unit tests")
- **Plans** — agent-generated execution plans
- **Rules** — coding standards and conventions
- **Environment Variables** — configuration for terminal sessions

**Create a Workflow:**
1. From Warp Drive, click **+** in Personal or Team.
2. Select **Workflow**.
3. Enter name, description, command, and parameters.
4. Save.

Check the Team section for shared resources your admin created—onboarding notebooks, deployment workflows, coding standards rules.

### MCP (Model Context Protocol)

MCP connects agents to external tools and services for enhanced context.

**Configure MCP servers:**
1. Go to **Settings** > **Agents** > **MCP servers** or access via Warp Drive.
2. Browse available servers: Linear, Sentry, Figma, GitHub, and more.
3. Click **+** next to a server to add it.
4. Configure credentials and connection details.
5. Toggle on/off as needed.

Team-shared MCP configurations display a share icon—use them without manual setup.

## Step 4: Start using Warp

| Task | Example |
|---|---|
| **Environment setup** | "Set up Node 20, Python 3.12, and Docker Desktop" |
| **Understand codebases** | "How does authentication flow through this system?" |
| **Write code** | Use `/plan` for complex features, review diffs in real-time |
| **Debug** | Start a debugger, bring in an agent to operate it in natural language |
| **Version control** | "Stage these changes and write a detailed commit message" |
| **Testing** | "Write unit tests for this function following our patterns" |

Save frequently used command sequences as Workflows in Warp Drive.

## Troubleshooting

For login, SSO, and access issues, see the [[009-enterprise-getting-started-faq|Enterprise FAQ]].

## Support and feedback

- **Send feedback**: `Cmd+Shift+F` (macOS) or `Ctrl+Shift+F` (Linux/Windows), or **Help** > **Send Feedback**
- **Priority support**: Enterprise teams have access via dedicated Slack/Teams channels