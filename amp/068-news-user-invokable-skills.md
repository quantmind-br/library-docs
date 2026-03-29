---
title: User Invokable Skills
url: https://ampcode.com/news/user-invokable-skills
source: crawler
fetched_at: 2026-02-06T02:08:10.817823106-03:00
rendered_js: false
word_count: 98
summary: Explains the new user-invokable skill feature in Amp, allowing users to manually force an agent to use a specific skill via the command palette.
tags:
    - agent-skills
    - amp-editor
    - command-palette
    - user-invokable
    - automation
category: guide
---

Since we [added support for Agent Skills](https://ampcode.com/news/agent-skills), we became heavy users of them. There are now fifteen skills in the Amp repository.

But one frustration we had was that skills were only invoked when the agent deemed that necessary. Sometimes, though, *we* knew exactly which skill the agent should use.

So we made skills user-invokable: you, as the user, can now invoke a skill, which will force the agent to use it when you send your next message.

Open the command palette (`Cmd/Alt-Shift-A` in the Amp editor extensions or `Ctrl-O` in the Amp CLI) and run `skill: invoke`.