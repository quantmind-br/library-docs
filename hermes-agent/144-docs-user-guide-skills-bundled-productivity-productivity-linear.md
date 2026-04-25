---
title: Linear — Manage Linear issues, projects, and teams via the GraphQL API | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-linear
source: crawler
fetched_at: 2026-04-24T17:05:33.983375263-03:00
rendered_js: false
word_count: 530
summary: This document serves as a reference guide detailing how to manage Linear issues, projects, and teams using its GraphQL API via command-line curl requests. It provides setup instructions, basic API patterns, workflow state definitions, and numerous examples for common queries and mutations.
tags:
    - linear
    - graphql
    - api-reference
    - issue-management
    - curl
    - productivity
category: reference
---

Manage Linear issues, projects, and teams via the GraphQL API. Create, update, search, and organize issues. Uses API key auth (no OAuth needed). All operations via curl — no dependencies.

SourceBundled (installed by default)Path`skills/productivity/linear`Version`1.0.0`AuthorHermes AgentLicenseMITTags`Linear`, `Project Management`, `Issues`, `GraphQL`, `API`, `Productivity`

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Linear — Issue & Project Management

Manage Linear issues, projects, and teams directly via the GraphQL API using `curl`. No MCP server, no OAuth flow, no extra dependencies.

## Setup[​](#setup "Direct link to Setup")

1. Get a personal API key from **Linear Settings &gt; API &gt; Personal API keys**
2. Set `LINEAR_API_KEY` in your environment (via `hermes setup` or your env config)

## API Basics[​](#api-basics "Direct link to API Basics")

- **Endpoint:** `https://api.linear.app/graphql` (POST)
- **Auth header:** `Authorization: $LINEAR_API_KEY` (no "Bearer" prefix for API keys)
- **All requests are POST** with `Content-Type: application/json`
- **Both UUIDs and short identifiers** (e.g., `ENG-123`) work for `issue(id:)`

Base curl pattern:

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ viewer { id name } }"}'| python3 -m json.tool
```

## Workflow States[​](#workflow-states "Direct link to Workflow States")

Linear uses `WorkflowState` objects with a `type` field. **6 state types:**

TypeDescription`triage`Incoming issues needing review`backlog`Acknowledged but not yet planned`unstarted`Planned/ready but not started`started`Actively being worked on`completed`Done`canceled`Won't do

Each team has its own named states (e.g., "In Progress" is type `started`). To change an issue's status, you need the `stateId` (UUID) of the target state — query workflow states first.

**Priority values:** 0 = None, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low

## Common Queries[​](#common-queries "Direct link to Common Queries")

### Get current user[​](#get-current-user "Direct link to Get current user")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ viewer { id name email } }"}'| python3 -m json.tool
```

### List teams[​](#list-teams "Direct link to List teams")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ teams { nodes { id name key } } }"}'| python3 -m json.tool
```

### List workflow states for a team[​](#list-workflow-states-for-a-team "Direct link to List workflow states for a team")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ workflowStates(filter: { team: { key: { eq: \"ENG\" } } }) { nodes { id name type } } }"}'| python3 -m json.tool
```

### List issues (first 20)[​](#list-issues-first-20 "Direct link to List issues (first 20)")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issues(first: 20) { nodes { identifier title priority state { name type } assignee { name } team { key } url } pageInfo { hasNextPage endCursor } } }"}'| python3 -m json.tool
```

### List my assigned issues[​](#list-my-assigned-issues "Direct link to List my assigned issues")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ viewer { assignedIssues(first: 25) { nodes { identifier title state { name type } priority url } } } }"}'| python3 -m json.tool
```

### Get a single issue (by identifier like ENG-123)[​](#get-a-single-issue-by-identifier-like-eng-123 "Direct link to Get a single issue (by identifier like ENG-123)")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issue(id: \"ENG-123\") { id identifier title description priority state { id name type } assignee { id name } team { key } project { name } labels { nodes { name } } comments { nodes { body user { name } createdAt } } url } }"}'| python3 -m json.tool
```

### Search issues by text[​](#search-issues-by-text "Direct link to Search issues by text")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issueSearch(query: \"bug login\", first: 10) { nodes { identifier title state { name } assignee { name } url } } }"}'| python3 -m json.tool
```

### Filter issues by state type[​](#filter-issues-by-state-type "Direct link to Filter issues by state type")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issues(filter: { state: { type: { in: [\"started\"] } } }, first: 20) { nodes { identifier title state { name } assignee { name } } } }"}'| python3 -m json.tool
```

### Filter by team and assignee[​](#filter-by-team-and-assignee "Direct link to Filter by team and assignee")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issues(filter: { team: { key: { eq: \"ENG\" } }, assignee: { email: { eq: \"user@example.com\" } } }, first: 20) { nodes { identifier title state { name } priority } } }"}'| python3 -m json.tool
```

### List projects[​](#list-projects "Direct link to List projects")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ projects(first: 20) { nodes { id name description progress lead { name } teams { nodes { key } } url } } }"}'| python3 -m json.tool
```

### List team members[​](#list-team-members "Direct link to List team members")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ users { nodes { id name email active } } }"}'| python3 -m json.tool
```

### List labels[​](#list-labels "Direct link to List labels")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issueLabels { nodes { id name color } } }"}'| python3 -m json.tool
```

## Common Mutations[​](#common-mutations "Direct link to Common Mutations")

### Create an issue[​](#create-an-issue "Direct link to Create an issue")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{
    "query": "mutation($input: IssueCreateInput!) { issueCreate(input: $input) { success issue { id identifier title url } } }",
    "variables": {
      "input": {
        "teamId": "TEAM_UUID",
        "title": "Fix login bug",
        "description": "Users cannot login with SSO",
        "priority": 2
      }
    }
  }'| python3 -m json.tool
```

### Update issue status[​](#update-issue-status "Direct link to Update issue status")

First get the target state UUID from the workflow states query above, then:

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { stateId: \"STATE_UUID\" }) { success issue { identifier state { name type } } } }"}'| python3 -m json.tool
```

### Assign an issue[​](#assign-an-issue "Direct link to Assign an issue")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { assigneeId: \"USER_UUID\" }) { success issue { identifier assignee { name } } } }"}'| python3 -m json.tool
```

### Set priority[​](#set-priority "Direct link to Set priority")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { priority: 1 }) { success issue { identifier priority } } }"}'| python3 -m json.tool
```

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "mutation { commentCreate(input: { issueId: \"ISSUE_UUID\", body: \"Investigated. Root cause is X.\" }) { success comment { id body } } }"}'| python3 -m json.tool
```

### Set due date[​](#set-due-date "Direct link to Set due date")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { dueDate: \"2026-04-01\" }) { success issue { identifier dueDate } } }"}'| python3 -m json.tool
```

### Add labels to an issue[​](#add-labels-to-an-issue "Direct link to Add labels to an issue")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { labelIds: [\"LABEL_UUID_1\", \"LABEL_UUID_2\"] }) { success issue { identifier labels { nodes { name } } } } }"}'| python3 -m json.tool
```

### Add issue to a project[​](#add-issue-to-a-project "Direct link to Add issue to a project")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { projectId: \"PROJECT_UUID\" }) { success issue { identifier project { name } } } }"}'| python3 -m json.tool
```

### Create a project[​](#create-a-project "Direct link to Create a project")

```bash
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{
    "query": "mutation($input: ProjectCreateInput!) { projectCreate(input: $input) { success project { id name url } } }",
    "variables": {
      "input": {
        "name": "Q2 Auth Overhaul",
        "description": "Replace legacy auth with OAuth2 and PKCE",
        "teamIds": ["TEAM_UUID"]
      }
    }
  }'| python3 -m json.tool
```

Linear uses Relay-style cursor pagination:

```bash
# First page
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issues(first: 20) { nodes { identifier title } pageInfo { hasNextPage endCursor } } }"}'| python3 -m json.tool

# Next page — use endCursor from previous response
curl-s-X POST https://api.linear.app/graphql \
-H"Authorization: $LINEAR_API_KEY"\
-H"Content-Type: application/json"\
-d'{"query": "{ issues(first: 20, after: \"CURSOR_FROM_PREVIOUS\") { nodes { identifier title } pageInfo { hasNextPage endCursor } } }"}'| python3 -m json.tool
```

Default page size: 50. Max: 250. Always use `first: N` to limit results.

## Filtering Reference[​](#filtering-reference "Direct link to Filtering Reference")

Comparators: `eq`, `neq`, `in`, `nin`, `lt`, `lte`, `gt`, `gte`, `contains`, `startsWith`, `containsIgnoreCase`

Combine filters with `or: [...]` for OR logic (default is AND within a filter object).

## Typical Workflow[​](#typical-workflow "Direct link to Typical Workflow")

1. **Query teams** to get team IDs and keys
2. **Query workflow states** for target team to get state UUIDs
3. **List or search issues** to find what needs work
4. **Create issues** with team ID, title, description, priority
5. **Update status** by setting `stateId` to the target workflow state
6. **Add comments** to track progress
7. **Mark complete** by setting `stateId` to the team's "completed" type state

## Rate Limits[​](#rate-limits "Direct link to Rate Limits")

- 5,000 requests/hour per API key
- 3,000,000 complexity points/hour
- Use `first: N` to limit results and reduce complexity cost
- Monitor `X-RateLimit-Requests-Remaining` response header

## Important Notes[​](#important-notes "Direct link to Important Notes")

- Always use `terminal` tool with `curl` for API calls — do NOT use `web_extract` or `browser`
- Always check the `errors` array in GraphQL responses — HTTP 200 can still contain errors
- If `stateId` is omitted when creating issues, Linear defaults to the first backlog state
- The `description` field supports Markdown
- Use `python3 -m json.tool` or `jq` to format JSON responses for readability