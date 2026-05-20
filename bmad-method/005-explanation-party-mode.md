---
title: Party Mode
url: https://docs.bmad-method.org//explanation/party-mode/
source: llms
fetched_at: 2026-05-19T08:33:03.551712169-03:00
rendered_js: false
word_count: 296
summary: This document introduces Party Mode, a feature that allows users to collaborate with multiple AI agents simultaneously within a single conversation for brainstorming, decision-making, and project planning.
tags:
    - ai-collaboration
    - multi-agent-system
    - project-management
    - brainstorming
    - team-workflow
category: concept
optimized: true
optimized_at: 2026-05-19T11:33:03Z
---
Get all your AI agents in one conversation.

## What is Party Mode?

Run `bmad-party-mode` to bring your AI team into one room. BMad Master orchestrates, picking relevant agents per message. Agents respond in character, debate, and build on each other's ideas. Continue as long as needed — ask follow-ups, push back, redirect.

**Good for:**

- Big decisions with tradeoffs
- Brainstorming sessions
- Post-mortems
- Sprint retrospectives and planning

### Calling Out Bad Architecture

**You:** "Okay team, our last sprint was a disaster. The authentication service went down three times. Who screwed this up?"

**Architect:** "The design was sound - distributed authentication with proper fallbacks. If implementation deviated from the spec…"

**Dev:** "I followed the architecture doc exactly. The spec didn't account for concurrent session invalidation race conditions."

**PM:** "Both of you missed the bigger issue - we didn't validate session management requirements in the PRD. This is on me for not catching it."

**TEA:** "And I should've caught this in integration tests. The test scenarios didn't cover concurrent invalidation."

### Creative Brainstorming

**You:** "How do we make onboarding feel magical instead of boring?"

**UX Designer:** "Start with progressive disclosure - reveal features as users need them, not all at once in a tutorial."

**Storyteller:** "What if onboarding was a story? Each step reveals a character's journey - the user IS the hero."

**Game Designer:** "Building on that - what if the first 'quest' is actually solving a real user problem? They learn by doing something valuable."

### Technical Decision

**You:** "Monolith or microservices for MVP?"

**Architect:** "Start monolith. Microservices add complexity you don't need at 1000 users."

**PM:** "Agree. Time to market matters more than theoretical scalability."

**Dev:** "Monolith with clear module boundaries. We can extract services later if needed."

#ai-collaboration #multi-agent-system #brainstorming #project-management