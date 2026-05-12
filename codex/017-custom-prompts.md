---
number: 17
category: guides
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://github.com/openai/codex/blob/main/CONFIGURATION.md
word_count: 271
---
# Custom Prompts & Instructions

> **BLUF:** Codex supports custom instructions at user, project, and repository levels. These files shape AI behavior for coding style, architecture, and workflow preferences. Supports Markdown, `RULES`, `AGENT`, and instruction files with explicit priority ordering.

## Instruction Types

| Type | Scope | File | Priority |
|------|-------|------|----------|
| User | Global | `~/.codex/instructions.md` | Lowest |
| Project | Local | `.codex/instructions.md` | Medium |
| Repository | Repo | `.codex/repo.md` | High |
| Inline | Prompt | `--instructions` flag | Highest |

Lower priority = overridden by higher. Same-priority files merge top-to-bottom.

## File Formats

### Markdown (`.md`)
Standard Markdown with natural language instructions. Most common.

### RULES (`.rules`)
Structured rule format for complex constraints:
```
RULE: always_use_typescript
  WHEN: generating_new_code
  THEN: use TypeScript with strict mode

RULE: no_console_in_prod
  WHEN: editing_production_files
  THEN: replace console.log with proper logger
```

### AGENT (`.agent`)
Define agent personas and capabilities:
```
AGENT: security_reviewer
  ROLE: Security-focused code reviewer
  CAPABILITIES: detect_sqli, detect_xss, check_auth
  RULES:
    - always_check_input_validation
    - flag_any_raw_queries
```

## Best Practices

| Practice | Rationale |
|----------|-----------|
| Keep under 200 lines | Long instructions dilute context window |
| Be specific, not vague | "Use TypeScript" vs "Prefer interfaces over types for object shapes" |
| Include examples | Show correct/incorrect patterns |
| Version in git | Track instruction evolution |
| Separate concerns | Use multiple focused files vs one monolith |

## Example: Full-Stack Project

`.codex/instructions.md`:
```markdown
# Project Instructions

## Stack
- Frontend: Next.js 14, React Server Components, Tailwind CSS
- Backend: tRPC with Zod validation
- Database: PostgreSQL via Prisma ORM
- Auth: NextAuth.js with GitHub provider

## Style
- Use TypeScript strict mode everywhere
- Prefer server components; mark client components with "use client"
- Use Zod for all API input validation
- Write tests with Vitest + React Testing Library

## Patterns
- Data fetching: Use tRPC queries in server components
- Forms: React Hook Form + Zod resolver
- Errors: Return `{ success: false, error: string }` from tRPC procedures
```

## Example: Repository-Level Rules

`.codex/repo.md`:
```markdown
# Repository Rules

## Code Quality
- All functions must have JSDoc comments
- No `any` types without explicit `@ts-expect-error` annotation
- 80% test coverage minimum for new code

## Security
- Never commit `.env` files
- Use `z.string().min(1)` over `z.string()` for non-empty strings
- Sanitize all user input with DOMPurify before DOM insertion

## Performance
- Use React.memo for components receiving objects/arrays
- Prefer `useSWR` over manual fetch with useEffect
```

## Dynamic Instructions

Load context based on file being edited:
```markdown
# Dynamic Instructions

IF file_path MATCHES "*.test.ts":
  - Use describe/it blocks
  - Mock external APIs with msw
  - Assert both success and error cases

IF file_path MATCHES "*/api/*":
  - Validate all inputs with Zod
  - Return consistent error shapes
  - Log errors with correlation IDs
```

## Debugging Instructions

When Codex ignores instructions:
1. Check file location (must be in `.codex/` directory)
2. Verify file extension (`.md`, `.rules`, `.agent`)
3. Simplify: remove half, test, repeat
4. Use explicit keywords: "ALWAYS", "NEVER", "MUST", "REQUIRED"
5. Check priority: inline > repo > project > user

## CLI Integration

```bash
# Use custom instructions for single command
codex --instructions ./docs/ai-style.md "refactor this component"

# Merge multiple instruction files
codex --instructions ./base.md --instructions ./frontend.md "create login page"
```

---

*Source: [openai/codex](https://github.com/openai/codex/blob/main/CONFIGURATION.md)*
