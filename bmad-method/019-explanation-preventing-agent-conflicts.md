---
title: Preventing Agent Conflicts
url: https://docs.bmad-method.org/explanation/preventing-agent-conflicts/
source: sitemap
fetched_at: 2026-04-08T11:30:01.12306296-03:00
rendered_js: false
word_count: 315
summary: This document explains how establishing formal architecture documentation prevents conflicts when multiple AI agents are implementing different parts of a system by setting shared standards for APIs, database design, and state management.
tags:
    - architecture
    - conflict-resolution
    - design-patterns
    - software-development
    - best-practices
    - adr
category: guide
---

When multiple AI agents implement different parts of a system, they can make conflicting technical decisions. Architecture documentation prevents this by establishing shared standards.

## Common Conflict Types

[Section titled “Common Conflict Types”](#common-conflict-types)

### API Style Conflicts

[Section titled “API Style Conflicts”](#api-style-conflicts)

Without architecture:

- Agent A uses REST with `/users/{id}`
- Agent B uses GraphQL mutations
- Result: Inconsistent API patterns, confused consumers

With architecture:

- ADR specifies: “Use GraphQL for all client-server communication”
- All agents follow the same pattern

### Database Design Conflicts

[Section titled “Database Design Conflicts”](#database-design-conflicts)

Without architecture:

- Agent A uses snake\_case column names
- Agent B uses camelCase column names
- Result: Inconsistent schema, confusing queries

With architecture:

- Standards document specifies naming conventions
- All agents follow the same patterns

### State Management Conflicts

[Section titled “State Management Conflicts”](#state-management-conflicts)

Without architecture:

- Agent A uses Redux for global state
- Agent B uses React Context
- Result: Multiple state management approaches, complexity

With architecture:

- ADR specifies state management approach
- All agents implement consistently

## How Architecture Prevents Conflicts

[Section titled “How Architecture Prevents Conflicts”](#how-architecture-prevents-conflicts)

### 1. Explicit Decisions via ADRs

[Section titled “1. Explicit Decisions via ADRs”](#1-explicit-decisions-via-adrs)

Every significant technology choice is documented with:

- Context (why this decision matters)
- Options considered (what alternatives exist)
- Decision (what we chose)
- Rationale (why we chose it)
- Consequences (trade-offs accepted)

### 2. FR/NFR-Specific Guidance

[Section titled “2. FR/NFR-Specific Guidance”](#2-frnfr-specific-guidance)

Architecture maps each functional requirement to technical approach:

- FR-001: User Management → GraphQL mutations
- FR-002: Mobile App → Optimized queries

### 3. Standards and Conventions

[Section titled “3. Standards and Conventions”](#3-standards-and-conventions)

Explicit documentation of:

- Directory structure
- Naming conventions
- Code organization
- Testing patterns

## Architecture as Shared Context

[Section titled “Architecture as Shared Context”](#architecture-as-shared-context)

Think of architecture as the shared context that all agents read before implementing:

```text

PRD: "What to build"
↓
Architecture: "How to build it"
↓
Agent A reads architecture → implements Epic 1
Agent B reads architecture → implements Epic 2
Agent C reads architecture → implements Epic 3
↓
Result: Consistent implementation
```

Common decisions that prevent conflicts:

TopicExample DecisionAPI StyleGraphQL vs REST vs gRPCDatabasePostgreSQL vs MongoDBAuthJWT vs SessionsState ManagementRedux vs Context vs ZustandStylingCSS Modules vs Tailwind vs Styled ComponentsTestingJest + Playwright vs Vitest + Cypress

## Anti-Patterns to Avoid

[Section titled “Anti-Patterns to Avoid”](#anti-patterns-to-avoid)