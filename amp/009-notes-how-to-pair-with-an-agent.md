---
title: How to Pair With an Agent
url: https://ampcode.com/notes/how-to-pair-with-an-agent
source: crawler
fetched_at: 2026-02-06T02:08:53.141008625-03:00
rendered_js: false
word_count: 576
summary: This document provides strategies for effectively using AI coding agents by emphasizing the importance of detailed specification and the integration of feedback loops into prompts.
tags:
    - ai-agents
    - prompt-engineering
    - software-development
    - coding-assistants
    - developer-productivity
    - workflow-optimization
category: guide
---

The gap between folks who use agents effectively and those who don’t is widening. Most people start their journey like a drunken sailor, reacting to whatever the machine spits out next, staggering through prompts without a clear destination. They end up effectively in the same place they started.

The difference between those who go far and those who don’t is vision. Without it, you are simply reacting to events as they happen.

If you’re an AI-maxi and are running Amp in 10 parallel tmux sessions, this might just confirm what you already know.

But if you’re just getting started with coding agents, or if you’ve tried them and bounced off, this one is for you.

We are reaching a point where agents can solve nearly anything you can specify. Consequently, the primary failure mode is under-specification. When you give an agent an unrestricted prompt, you get unrestricted results, which are almost never what you want. The more you can specify, the better. We spend a lot of time taking customers on this journey, and we want to distill it into a path to get you to that “oh shit” moment a little faster.

We’re going to work through real examples together. By the end, you’ll have a mental model that actually works.

## The “Sitting Next to Me” Test

You’ve been handed a bug. The back button isn’t working on the settings page. Your first instinct might be to treat your agent like a glorified search bar.

Try this instead: imagine a capable peer sitting next to you. They’ve never seen your codebase, but they move at more than 10x your speed. Their only limiting factors are the tools they can access, the feedback loops they can see, and your ability to lead them.

**Vague prompt:**

```
Why isn't the back button working?
```

Give them direction, not a question.

**Specified prompt:**

```
The back button on the settings page doesn't navigate.
Reproduce it locally, find the bug, fix it, check your own work.
```

It works. The agent fixed the bug in minutes. Feeling confident, you hand it something bigger. A feature that would normally take you an afternoon.

This is where you fall into the trap.

The Speed Trap happens the moment the agent moves faster than your ability to verify its output. The agent produces 500 lines of code across six files in a few seconds, but it broke the auth flow. Damn.

This isn’t a “hallucination.” The agent reasoned correctly from everything you gave it. You just need to guide it that one bit further, like you would with the capable peer sitting next to you.

**Vague prompt:**

```
Add dark mode to the settings page
```

Know about a trap they might fall into? Mention it.

**Specified prompt:**

```
Add dark mode to the settings page.
We store user preferences in localStorage under `user-prefs`.
Match the toggle style we use in the notifications panel.
Use Chrome devtools to check dark mode is implemented correctly,
toggle it back to light mode and check that it works correctly too.
Run the e2e tests when you're done.
```

Same task. Different outcome. The difference is context.

When you’re stuck in the Speed Trap, you spend more time debugging the agent’s “solutions” than you would have spent writing the code yourself.

Don’t just ask for the feature. Give it a definition of done, then engineer feedback loops into the prompt itself.

**Vague prompt:**

```
Build a new API endpoint for user notifications
```

How do they know they did the right thing? Specify it, give them a feedback loop.

**Specified prompt:**

```
Build a new API endpoint for user notifications.
Follow the pattern in `src/api/messages.ts` as your reference.
Run the API tests after each step. Don't move on until they pass.
```

You gave it a reference to follow and a way to check its own work. Now you can step away. Let the agent iterate until the tests pass.

You check back. It worked.

Not because the AI got “smarter” overnight, but because you built a better environment for it to succeed.

Trust isn’t a feeling, it’s a passing test suite.