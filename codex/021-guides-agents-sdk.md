---
number: 21
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/guides/agents-sdk.md
word_count: 468
---
# Use Codex with the Agents SDK

> **BLUF:** Run Codex CLI as an MCP server and orchestrate multi-agent workflows with the OpenAI Agents SDK. Covers `codex mcp-server`, `codex`/`codex-reply` MCP tools, and complete single/multi-agent workflow examples.

## Running Codex as an MCP Server

Start Codex as MCP server for other MCP clients (e.g., [OpenAI Agents SDK MCP integration](https://developers.openai.com/api/docs/guides/agents/integrations-observability#mcp)).

```bash
codex mcp-server
```

Test with Model Context Protocol Inspector:
```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

### Exposed Tools

**`codex`** — Start a Codex session.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | ✅ | Initial user prompt |
| `approval-policy` | string | | `untrusted` \| `on-request` \| `never` |
| `base-instructions` | string | | Override default instructions |
| `config` | object | | `config.toml` overrides |
| `cwd` | string | | Working directory (relative = server cwd) |
| `include-plan-tool` | boolean | | Include plan tool |
| `model` | string | | Override model (e.g., `o3`, `o4-mini`) |
| `profile` | string | | Config profile from `config.toml` |
| `sandbox` | string | | `read-only` \| `workspace-write` \| `danger-full-access` |

**`codex-reply`** — Continue a session.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | ✅ | Next user prompt |
| `threadId` | string | ✅ | Thread ID from `structuredContent.threadId` |
| `conversationId` | string | | Deprecated alias for `threadId` |

> Approval prompts include `threadId` in `params` payload.

## Multi-Agent Workflow Setup

### Prerequisites

- Codex CLI installed (`npx codex` works)
- Python 3.10+ with `pip`
- Node.js 18+
- OpenAI API key in `.env`

```bash
mkdir codex-workflows && cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
pip install --upgrade openai openai-agents python-dotenv
```

### Initialize MCP Server

```python
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

async def main() -> None:
    async with MCPServerStdio(
        name="Codex CLI",
        params={"command": "npx", "args": ["-y", "codex", "mcp-server"]},
        client_session_timeout_seconds=360000,
    ) as codex_mcp_server:
        print("Codex MCP server started.")
```

## Single-Agent Example: Browser Game

Two agents: **Game Designer** (writes brief, hands off) → **Game Developer** (calls Codex MCP).

```python
developer_agent = Agent(
    name="Game Developer",
    instructions="Build simple browser games (html+css+js, ~50 lines). Save to index.html. Always call codex with approval-policy=never, sandbox=workspace-write.",
    mcp_servers=[codex_mcp_server],
)

designer_agent = Agent(
    name="Game Designer",
    instructions="Come up with a 3-sentence game design brief. Call Game Developer with your idea.",
    model="gpt-5",
    handoffs=[developer_agent],
)

await Runner.run(designer_agent, "Implement a fun new game!")
```

Codex creates `index.html` with full game. Each run produces unique design.

## Multi-Agent Example: Full Stack Workflow

**Agents:** Project Manager → Designer → Frontend Developer → Backend Developer → Tester → Project Manager

Project Manager coordinates hand-offs with file-based gates:

1. PM writes `REQUIREMENTS.md`, `TEST.md`, `AGENT_TASKS.md`
2. PM → Designer (provides requirements + tasks)
3. Designer writes `/design/design_spec.md`
4. PM gates: verify `design_spec.md` exists → parallel handoff to Frontend + Backend
5. Frontend writes `/frontend/index.html`; Backend writes `/backend/server.js`
6. PM gates: verify both files → PM → Tester
7. Tester writes `/tests/TEST_PLAN.md`

```python
project_manager_agent = Agent(
    name="Project Manager",
    instructions="""Create three files: REQUIREMENTS.md, TEST.md, AGENT_TASKS.md.
Gated handoffs: only advance when required files exist.
PM does NOT respond with status updates. Just hand off to next agent until complete.""",
    model="gpt-5",
    handoffs=[designer_agent, frontend_developer_agent, backend_developer_agent, tester_agent],
    mcp_servers=[codex_mcp_server],
)
```

### Example Task: Bug Busters Game

- **Designer**: UI/UX spec + wireframe → `/design/design_spec.md`
- **Frontend**: `index.html` + game logic → `/frontend/`
- **Backend**: `package.json` + API (GET /health, GET/POST /scores) → `/backend/`
- **Tester**: `TEST_PLAN.md` + `test.sh` → `/tests/`

```python
task_list = """
Goal: Build 'Bug Busters' browser game.

- Single-screen: player clicks moving bug to earn points
- Game ends after 20 seconds → final score
- Optional: submit score to backend, display top-10 leaderboard

No external database — memory storage is fine.
All outputs should be small files in clearly named folders.
"""

result = await Runner.run(project_manager_agent, task_list, max_turns=30)
```

## Tracing

Codex records traces (prompts, tool calls, hand-offs). Open [Traces dashboard](https://platform.openai.com/trace) to inspect execution timeline. Click into steps to see prompts, Codex MCP calls, files written, execution durations.

## Related

- [[070-models|Codex Models]]
- [[052-mcp|Model Context Protocol]]
- [[043-concepts-subagents|Subagents]]
- [[042-concepts-customization|Customization]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/guides/agents-sdk.md)*