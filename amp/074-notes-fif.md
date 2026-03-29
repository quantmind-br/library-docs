---
title: Frequently Ignored Feedback (FIF)
url: https://ampcode.com/notes/fif
source: crawler
fetched_at: 2026-02-06T02:08:57.023394618-03:00
rendered_js: false
word_count: 898
summary: This document outlines the product philosophy for the Amp coding assistant by explaining why specific feature requests are intentionally declined. It provides context on the developers' decisions regarding model selection, agent autonomy, and user interface design.
tags:
    - amp-assistant
    - product-philosophy
    - design-decisions
    - ai-coding
    - user-feedback
    - feature-requests
category: other
---

## Frequently Ignored Feedback[#](#frequently-ignored-feedback)[#](#frequently-ignored-feedback)

Our responses to some common feedback that we are intentionally not acting on. Note that we may change our minds here; this is just our current position.

## “Make it so the user can switch models.”[#](#model-selector)[#](#model-selector)

We believe that building deeply into the model’s capabilities yields the best product, vs. building for the lowest common denominator across many models. Amp has [agent modes](https://ampcode.com/manual#agent-modes) (such as `smart` and `rush`), which are a unique combination of multiple models, system prompts, and tools, instead of just a model switcher.

## “I don't want it to edit files directly.”[#](#directly-edit)[#](#directly-edit)

Requiring edit-by-edit approval traps you in a [local maximum](https://x.com/beyang/status/1924507302956302762) by impeding the agentic feedback loop. You’re not giving the agent a chance to iterate on its first draft through review, diagnostics, compiler output, and test execution. If you find that the agent rarely produces good enough code on its own, instead of trying to “micro-manage” it, we recommend writing [more detailed prompts](https://ampcode.com/how-i-use-amp) and improving your [`AGENTS.md` files](https://ampcode.com/manual#AGENTS.md).

## “Don't show all the noisy work the agent is doing, just hide it and show me the final result.”[#](#hide-details)[#](#hide-details)

We believe that hiding it all sets expectations too high about how well it works. We also get much better feedback from users when they see its work, and high-quality feedback is extremely valuable.

We believe that shared by default results in more threads being shared, which is an important benefit of the product. It reduces the expectation that your threads are “perfect” or “not dumb” if everyone knows the default is shared. It is akin to Google Docs “sharing” edit history by default, or GitHub “sharing” your Git branches by default.

(Note: Enterprise Premium workspaces have more configurable thread privacy options.)

## “Make it so threads are automatically compacted and I do not have to worry about the context window.”[#](#auto-compaction)[#](#auto-compaction)

We think this reduces quality and creates an inconsistent experience (devs wondering why the agent suddenly got dumber and not realizing it’s because they just hit an auto-compaction threshold). We would do this if we find a technique that provably doesn’t hurt quality. In the meantime, we offer a manual way to do it.

## “I want the agent to make Git commits.”[#](#git-commits)[#](#git-commits)

Our current thinking is that we want to give the agent as much freedom as possible. It should be able to run commands, edit files, and so on. But that means we want to always have the security of our VCS in the background. So for now, we don’t want the agent to touch the VCS on its own. You can tell it to make commits, sure, and tell it to open PRs, but we don’t want to mess with our staging/commits on its own.

## “Add more safety controls or configurability over shell commands that it runs.”[#](#shell-commands)[#](#shell-commands)

We are (currently) NOT trying to protect against a malicious actor prompt-injecting something that causes the `Bash` tool to execute malicious code.

## “Where is the .ampignore file?”[#](#ignore-files)[#](#ignore-files)

We think that an ignore file is actively harmful: hiding files from the model encourages it to find creative workarounds, for example by using the Bash tool, wasting tokens.

Such file restrictions can be trivially circumvented with the Bash tool, and thus give only a false sense of security.

Amp already redacts known secrets and provides an [extensive permissions system](https://ampcode.com/manual#permissions) if you need full control over its tool use.

## “Make it so Enter, not Cmd/Ctrl+Enter, submits the message.”[#](#cmd-enter)[#](#cmd-enter)

We think that Cmd/Ctrl+Enter as submit (in Amp’s editor extension) nudges people to write better, longer prompts. (In the Amp CLI, Enter submits the message because many terminals don’t allow us to detect Cmd/Ctrl+Enter keypresses correctly, but we’re working on a better solution.)

## “Make it so I can ask the model what model it is.”[#](#model-self-id)[#](#model-self-id)

Don’t waste your time asking an LLM what model it is. LLMs often self-report their model name incorrectly. We gently nudge Amp’s model to refer to the [Amp Owner’s Manual](https://ampcode.com/manual) when asked about this, but we don’t want to use more system prompt tokens to force it, because that would degrade the performance of Amp and waste tokens that you could otherwise use.

## “Add support for more editors.”[#](#more-editors)[#](#more-editors)

We don’t plan to create native extensions for editors other than VS Code (and forks thereof). Users of JetBrains and Neovim can use the Amp CLI with our [IDE integration](https://ampcode.com/manual#ide) to enhance Amp’s code awareness.

## “Let the agent run and manage background processes (such as dev servers).”[#](#background-processes)[#](#background-processes)

For now, we don’t want to add support for background processes to Amp. When Amp briefly supported background processes, it caused a lot of problems: running multiple Amp agents caused dev server port collisions, it was cumbersome to manually view the output, it was unclear if continuing an existing thread should restart the processes, and it interfered with spawning non-background processes (e.g., some test runners thought they should run in “watch” mode because of the different way we spawned processes that might be long-running). These problems accounted for about half of all user-reported issues.

Instead, you should run background processes yourself and tell Amp how to interact with them in the [AGENTS.md](https://ampcode.com/manual#AGENTS.md) file, such as by giving it the URL to your dev server or a log file it can `tail`.

## “Let me bring my own Anthropic API key or use Amazon Bedrock.”[#](#byok)[#](#byok)

We tried hard to make this work but decided to [remove BYOK](https://ampcode.com/news/no-more-byok) permanently because it hurts quality and focus.