---
title: How We Think about Permissions
url: https://ampcode.com/notes/permissions
source: crawler
fetched_at: 2026-02-06T02:08:55.105117141-03:00
rendered_js: false
word_count: 1054
summary: This document explains the Amp permission system and how to configure rules that control an AI agent's access to tools, files, and commands. It covers various scenarios ranging from full automation to granular restrictions for sensitive operations like database management and git commits.
tags:
    - ai-agents
    - permissions-management
    - amp-agent
    - security-policies
    - access-control
    - developer-tools
category: guide
---

In our experience, agents work best when they can get feedback about the changes they are making. For example, when they’re able to run tests and see the results of the test run.

Taking tools away, like preventing the agent from reading certain files, makes the agent look for an alternative, like running a Bash command instead to access file contents.

Most people do not worry about file edits anymore, because Git makes the cost of a wrong edit negligible. Restrictions aren’t necessary for tools like this with an easy undo action.

Alternatively, you can set up rules for what the agent is allowed to do with and without asking you. This means Amp will interrupt you more frequently, but in exchange you can examine what Amp is about to do before it triggers a deploy, or accesses the production database.

Amp’s [Permission System](https://ampcode.com/manual#permissions) allows for both modes of operation.

## “I don't want the agent to run npm exec.”[#](#feedback-loops)[#](#feedback-loops)

You already rely on many sources of feedback, some of them very subtle, to develop software successfully.

It’s the little red squiggles under a typo, the errors produced by the compiler, the failures you get when running your test suite.

While state-of-the-art models are better than most humans at generating working code in one try without feedback, they still need feedback just like you to work effectively in real-world projects.

This feedback allows them to iterate, finally converging on a solution that meets all the constraints imposed by the project, and your task at hand.

Only through running external tools like the type checker and your test suite can the model learn about any mistakes it has made.

With precise instructions like “Use `npm test` to run the test suite”, you’ll find the model doing just that when it’s time to run the tests.

## “AI just dropped my production database!”[#](#error-friendly-environment)[#](#error-friendly-environment)

While this is a popular story on X, it is usually one told by people new to software development.

You, of course, know that database backups are critical because they reduce the potential damage of database-related accidents to near zero.

Similarly, version control eliminates any damage from undesired file edits.

The same goes for letting the model commit to git: the cost of doing it is low, because commits can be dropped and amended easily.

Errors occur both for models and humans, and building an environment acknowledging this produces better outcomes than trying to prevent all errors in the first place.

## “Allow All feels scary and is not granular enough!”[#](#allow-all)[#](#allow-all)

This is true! And so is the opposite: “I’m tired of approving so many tool calls for a simple task!”

We have observed there being two kinds of operators:

- risk-tolerant ones using frontier coding agents all day, often running multiple instances at the same time;
- and cautious users who like to stay in control, carefully reviewing every step the agent takes.

Both groups’ needs are valid, and Amp’s [Permissions system](https://ampcode.com/manual#permissions) supports that.

Before performing *any* tool call, Amp checks all permission rules in sequence until it finds a matching rule.

The matching rule tells Amp what action to take.

These rules are stored in your settings under the `amp.permissions` key and can be edited in a more convenient text format.

The examples below use the CLI, and the same functionality is available in VS Code through the “Amp: Edit User Permissions” command.

## “I want the agent to take the wheel, running in full-auto mode.”[#](#full-auto)[#](#full-auto)

This sets your permissions to just two rules, asking you when Amp wants to run commands which look like they are mass-deleting files.

```
amp permissions edit <<'END'
ask Bash --cmd '*rm*rf*' --cmd '*find*exec*' --cmd '*find*delete*'
allow '*'
END
```

## “I do not want Amp to read any of my dotfiles.”[#](#restricting-reads)[#](#restricting-reads)

The following adds a rule to the beginning of your rules list, which makes Amp ask every time it tries to read a file whose name starts with `.` in your home directory.

```
amp permissions add ask Read --path "$HOME/.*"
```

You can verify this behavior with the `test` command:

```
amp permissions test Read --path "$HOME/.bashrc"
```

```
tool: Read
arguments: {"path":"/Users/dhamidi/.bashrc"}
action: ask
matched-rule: 0
source: user
```

## “I want Amp to create Jira issues, but only in a specific project.”[#](#jira)[#](#jira)

Using [Atlassian’s MCP server](https://support.atlassian.com/rovo/docs/getting-started-with-the-atlassian-remote-mcp-server/) for accessing Jira, you can tell Amp to modify issues in the `EXPERIMENT` project without asking, while asking you for the same operations in any other project.

Using `amp tools list` we can see Jira-related tools exposed by the server:

```
amp tools list | awk '$1 ~ /[iI]ssue/ { print $1 }'
```

```
mcp__atlassian__addCommentToJiraIssue
mcp__atlassian__createJiraIssue
mcp__atlassian__editJiraIssue
# ... rest omitted ...
```

Running `amp tools show mcp__atlassian__createJiraIssue`, we can see that the tool expects a `projectKey` parameter.

With this information in hand, we can create two rules, the first for making Amp ask before creating issues:

```
amp permissions add ask mcp__atlassian__createJiraIssue
```

And a more specific one, allowing Amp to create issues when the project key is `EXPERIMENT`:

```
amp permissions add allow mcp__atlassian__createJiraIssue --projectKey "EXPERIMENT"
```

## “I don't want Amp to accidentally push to GitHub.”[#](#bash-git)[#](#bash-git)

The `Bash` tool accepts the entire shell command pipeline to run in the `cmd` parameter.

This is a string containing source code, so we need match any command line that *looks* like a git push command:

```
amp permissions add ask Bash --cmd '*git*push*'
```

The `*` is a wildcard, so this rule will match all of these command lines:

```
cd ../other-repo && git push
git commit -m 'WIP' && git push
git --work-tree=. push origin
```

## “Amp must not modify my infrastructure.”[#](#bash-infra)[#](#bash-infra)

In a similar vein, you might want to restrict Amp from modifying infrastructure through `terraform` or `kubectl`, while still allowing Amp to inspect the current state of deployed infrastructure.

This rule allows all terraform commands:

```
amp permissions add allow Bash --cmd "*terraform*"
```

Then we add a more specific rule rejecting destructive terraform commands:

```
amp permissions add reject Bash --cmd "*terraform*apply*" --cmd "*terraform*destroy*" --cmd "*terraform*force-unlock*"
```

## “I need even more control.”[#](#helper-steering)[#](#helper-steering)

Amp allows you to provide a helper program which is responsible for making the decision about each tool call.

Here’s how you tell Amp about the helper, let’s call it `amp-permissions-helper`:

```
amp permissions add delegate --to amp-permissions-helper '*'
```

And then you’ll write a tiny program called `amp-permissions-helper` and put it on your `$PATH`.

The program receives the tool parameters on stdin as JSON, and makes a decision with its exit code: `0` allows the tool call, `1` makes Amp ask, and `2` rejects the tool call, forwarding stderr to the model.

This little helper program will reject `git push` when there are unstaged changes, and allow every other command.

```
#!/usr/bin/env bash
attempted_command=$(jq -r .cmd)
if ! [[ $attempted_command =~ git.*push ]]; then
  # allow, we only care about git push
  exit 0
fi

if ! git diff --quiet; then
  printf "Ask the user how to proceed, there are unstaged changes." >&2
  exit 2
fi
```

## “How can I centrally manage permissions?”[#](#helper-opa)[#](#helper-opa)

[Open Policy Agent](https://www.openpolicyagent.org/) is a popular piece of software for centrally managing access control rules.

You’d define your policies in one location and make them accessible using the OPA server.

Using a permission helper, you can forward tool arguments to the OPA server and let it make the decision according to a central ruleset:

Let’s say we have this policy running on the server:

```
package amp

# Default result
default action := "ask"

# Reject git push commands in Bash
action := "reject" if {
    input.toolName == "Bash"
    regex.match(".*git.*push.*", input.args.cmd)
}

# Allow other Bash commands
action := "allow" if {
    input.toolName == "Bash"
    not regex.match(".*git.*push.*", input.args.cmd)
}
```

Then we can query the OPA server like this:

```
#!/usr/bin/env bash
tool_input=$(jq -r .)
tool_name="$AGENT_TOOL_NAME"
policy_input=$(jq --arg name "$tool_name" --argjson args "$tool_input" -n '{input:{toolName: $name, args: $args}}')

# {"result": $value }
response=$(
  curl -s -XPOST --data-binary "$policy_input" \
    -H "Content-Type: application/json" \
    $OPA_SERVER/data/amp/action
)

case $(jq -r .result <<<"$response") in
  allow) exit 0;;
  ask) exit 1;;
  reject) exit 2;;
  *) exit 1;;
esac
```