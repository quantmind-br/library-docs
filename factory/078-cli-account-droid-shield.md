---
title: Droid Shield - Factory Documentation
url: https://docs.factory.ai/cli/account/droid-shield
source: sitemap
fetched_at: 2026-01-13T19:03:43.60417466-03:00
rendered_js: false
word_count: 327
summary: Explains the Droid Shield security feature that automatically scans git changes for potential secrets and credentials before commits or pushes to prevent accidental exposure.
tags:
    - security
    - git-integration
    - secret-scanning
    - credentials
    - droid-shield
    - automation
category: guide
---

## What is Droid Shield?

Droid Shield is a built-in security feature that automatically scans un-committed changes for potential secrets before committing and pushing them to remote. It acts as a safety net to prevent accidental exposure of sensitive credentials like API keys, tokens, and passwords in your version control history.

* * *

## How Droid Shield Works

When you use Droid to perform `git commit` or `git push` operations, Droid Shield automatically:

1. **Scans the diff** - Analyzes only the lines being added (not removed or unchanged)
2. **Detects secrets** - Uses pattern matching to identify potential credentials
3. **Blocks execution** - Stops the git operation if secrets are detected
4. **Reports findings** - Shows exactly where potential secrets were found

* * *

## What Droid Shield Detects

Droid Shield scans for a wide range of credential patterns, including:

### Detection Algorithm

Droid Shield uses smart pattern matching with randomness validation:

- **Pattern matching** - Identifies credentials by format
- **Randomness check** - Validates that captured values look like actual secrets
- **Context awareness** - Considers variable names and assignment patterns to reduce false positives

* * *

## When Droid Shield Activates

Droid Shield automatically activates during these git operations:

- **`git commit`** - Scans staged changes before creating the commit
- **`git push`** - Scans commits that would be pushed to the remote

* * *

## Managing Droid Shield Settings

### In the CLI

You can toggle Droid Shield on or off through the settings menu:

1. Run `droid`
2. Enter `/settings`
3. Toggle **“Droid Shield”** setting
4. Changes take effect immediately

* * *

## What to Do if Secrets are Detected

When Droid Shield detects potential secrets, you’ll see an error message like:

```
Droid-Shield has detected potential secrets in 2 location(s) across files:
src/config.ts, .env.example

If you would like to override, you can either:
1. Perform the commit/push yourself manually
2. Disable Droid Shield by running /settings and toggling the "Droid Shield" option
```

### Recommended Actions

### If You Get a False Positive

Droid Shield uses conservative patterns to err on the side of caution. If you believe a detection is a false positive:

1. **Verify it’s not a real secret** - Double-check that the value isn’t sensitive
2. **Use a manual commit** - Perform the git operation yourself outside of Droid
3. **Report the pattern** - Contact [support@factory.ai](mailto:support@factory.ai) if you encounter recurring false positives

* * *

## Best Practices

* * *

## Limitations

* * *

* * *

## Need Help?