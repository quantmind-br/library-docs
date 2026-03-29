---
title: Voicecall - OpenClaw
url: https://docs.openclaw.ai/cli/voicecall
source: sitemap
fetched_at: 2026-01-30T20:33:06.494152393-03:00
rendered_js: false
word_count: 45
summary: Provides documentation for the voicecall plugin commands including status, call, continue, end, and webhook exposure functionality.
tags:
    - voice-call
    - plugin
    - command-line
    - webhook
    - tailscale
    - telephony
category: reference
---

`voicecall` is a plugin-provided command. It only appears if the voice-call plugin is installed and enabled. Primary doc:

- Voice-call plugin: [Voice Call](https://docs.openclaw.ai/plugins/voice-call)

## Common commands

```
openclaw voicecall status --call-id <id>
openclaw voicecall call --to "+15555550123" --message "Hello" --mode notify
openclaw voicecall continue --call-id <id> --message "Any questions?"
openclaw voicecall end --call-id <id>
```

## Exposing webhooks (Tailscale)

```
openclaw voicecall expose --mode serve
openclaw voicecall expose --mode funnel
openclaw voicecall unexpose
```

Security note: only expose the webhook endpoint to networks you trust. Prefer Tailscale Serve over Funnel when possible.