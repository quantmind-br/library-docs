---
title: Telegram | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram
source: crawler
fetched_at: 2026-04-24T17:00:12.436249601-03:00
rendered_js: false
word_count: 2961
summary: This document serves as a comprehensive guide detailing the integration of Hermes Agent with Telegram, covering steps from initial bot creation via BotFather to advanced configuration options like using webhooks and managing Docker file pathing.
tags:
    - telegram-integration
    - hermes-agent
    - botfather-setup
    - webhook-mode
    - docker-config
    - user-id-management
category: guide
---

Hermes Agent integrates with Telegram as a full-featured conversational bot. Once connected, you can chat with your agent from any device, send voice memos that get auto-transcribed, receive scheduled task results, and use the agent in group chats. The integration is built on [python-telegram-bot](https://python-telegram-bot.org/) and supports text, voice, images, and file attachments.

## Step 1: Create a Bot via BotFather[​](#step-1-create-a-bot-via-botfather "Direct link to Step 1: Create a Bot via BotFather")

Every Telegram bot requires an API token issued by [@BotFather](https://t.me/BotFather), Telegram's official bot management tool.

1. Open Telegram and search for **@BotFather**, or visit [t.me/BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose a **display name** (e.g., "Hermes Agent") — this can be anything
4. Choose a **username** — this must be unique and end in `bot` (e.g., `my_hermes_bot`)
5. BotFather replies with your **API token**. It looks like this:

```text
123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
```

warning

Keep your bot token secret. Anyone with this token can control your bot. If it leaks, revoke it immediately via `/revoke` in BotFather.

## Step 2: Customize Your Bot (Optional)[​](#step-2-customize-your-bot-optional "Direct link to Step 2: Customize Your Bot (Optional)")

These BotFather commands improve the user experience. Message @BotFather and use:

CommandPurpose`/setdescription`The "What can this bot do?" text shown before a user starts chatting`/setabouttext`Short text on the bot's profile page`/setuserpic`Upload an avatar for your bot`/setcommands`Define the command menu (the `/` button in chat)`/setprivacy`Control whether the bot sees all group messages (see Step 3)

tip

For `/setcommands`, a useful starting set:

```text
help - Show help information
new - Start a new conversation
sethome - Set this chat as the home channel
```

## Step 3: Privacy Mode (Critical for Groups)[​](#step-3-privacy-mode-critical-for-groups "Direct link to Step 3: Privacy Mode (Critical for Groups)")

Telegram bots have a **privacy mode** that is **enabled by default**. This is the single most common source of confusion when using bots in groups.

**With privacy mode ON**, your bot can only see:

- Messages that start with a `/` command
- Replies directly to the bot's own messages
- Service messages (member joins/leaves, pinned messages, etc.)
- Messages in channels where the bot is an admin

**With privacy mode OFF**, the bot receives every message in the group.

### How to disable privacy mode[​](#how-to-disable-privacy-mode "Direct link to How to disable privacy mode")

1. Message **@BotFather**
2. Send `/mybots`
3. Select your bot
4. Go to **Bot Settings → Group Privacy → Turn off**

warning

**You must remove and re-add the bot to any group** after changing the privacy setting. Telegram caches the privacy state when a bot joins a group, and it will not update until the bot is removed and re-added.

tip

An alternative to disabling privacy mode: promote the bot to **group admin**. Admin bots always receive all messages regardless of the privacy setting, and this avoids needing to toggle the global privacy mode.

## Step 4: Find Your User ID[​](#step-4-find-your-user-id "Direct link to Step 4: Find Your User ID")

Hermes Agent uses numeric Telegram user IDs to control access. Your user ID is **not** your username — it's a number like `123456789`.

**Method 1 (recommended):** Message [@userinfobot](https://t.me/userinfobot) — it instantly replies with your user ID.

**Method 2:** Message [@get\_id\_bot](https://t.me/get_id_bot) — another reliable option.

Save this number; you'll need it for the next step.

## Step 5: Configure Hermes[​](#step-5-configure-hermes "Direct link to Step 5: Configure Hermes")

### Option A: Interactive Setup (Recommended)[​](#option-a-interactive-setup-recommended "Direct link to Option A: Interactive Setup (Recommended)")

Select **Telegram** when prompted. The wizard asks for your bot token and allowed user IDs, then writes the configuration for you.

### Option B: Manual Configuration[​](#option-b-manual-configuration "Direct link to Option B: Manual Configuration")

Add the following to `~/.hermes/.env`:

```bash
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
TELEGRAM_ALLOWED_USERS=123456789# Comma-separated for multiple users
```

### Start the Gateway[​](#start-the-gateway "Direct link to Start the Gateway")

The bot should come online within seconds. Send it a message on Telegram to verify.

## Sending Generated Files from Docker-backed Terminals[​](#sending-generated-files-from-docker-backed-terminals "Direct link to Sending Generated Files from Docker-backed Terminals")

If your terminal backend is `docker`, keep in mind that Telegram attachments are sent by the **gateway process**, not from inside the container. That means the final `MEDIA:/...` path must be readable on the host where the gateway is running.

Common pitfall:

- the agent writes a file inside Docker to `/workspace/report.txt`
- the model emits `MEDIA:/workspace/report.txt`
- Telegram delivery fails because `/workspace/report.txt` only exists inside the container, not on the host

Recommended pattern:

```yaml
terminal:
backend: docker
docker_volumes:
-"/home/user/.hermes/cache/documents:/output"
```

Then:

- write files inside Docker to `/output/...`
- emit the **host-visible** path in `MEDIA:`, for example: `MEDIA:/home/user/.hermes/cache/documents/report.txt`

If you already have a `docker_volumes:` section, add the new mount to the same list. YAML duplicate keys silently override earlier ones.

## Webhook Mode[​](#webhook-mode "Direct link to Webhook Mode")

By default, Hermes connects to Telegram using **long polling** — the gateway makes outbound requests to Telegram's servers to fetch new updates. This works well for local and always-on deployments.

For **cloud deployments** (Fly.io, Railway, Render, etc.), **webhook mode** is more cost-effective. These platforms can auto-wake suspended machines on inbound HTTP traffic, but not on outbound connections. Since polling is outbound, a polling bot can never sleep. Webhook mode flips the direction — Telegram pushes updates to your bot's HTTPS URL, enabling sleep-when-idle deployments.

Polling (default)WebhookDirectionGateway → Telegram (outbound)Telegram → Gateway (inbound)Best forLocal, always-on serversCloud platforms with auto-wakeSetupNo extra configSet `TELEGRAM_WEBHOOK_URL`Idle costMachine must stay runningMachine can sleep between messages

### Configuration[​](#configuration "Direct link to Configuration")

Add the following to `~/.hermes/.env`:

```bash
TELEGRAM_WEBHOOK_URL=https://my-app.fly.dev/telegram
# TELEGRAM_WEBHOOK_PORT=8443        # optional, default 8443
# TELEGRAM_WEBHOOK_SECRET=mysecret  # optional, recommended
```

VariableRequiredDescription`TELEGRAM_WEBHOOK_URL`YesPublic HTTPS URL where Telegram will send updates. The URL path is auto-extracted (e.g., `/telegram` from the example above).`TELEGRAM_WEBHOOK_PORT`NoLocal port the webhook server listens on (default: `8443`).`TELEGRAM_WEBHOOK_SECRET`NoSecret token for verifying that updates actually come from Telegram. **Strongly recommended** for production deployments.

When `TELEGRAM_WEBHOOK_URL` is set, the gateway starts an HTTP webhook server instead of polling. When unset, polling mode is used — no behavior change from previous versions.

### Cloud deployment example (Fly.io)[​](#cloud-deployment-example-flyio "Direct link to Cloud deployment example (Fly.io)")

1. Add the env vars to your Fly.io app secrets:

```bash
fly secrets setTELEGRAM_WEBHOOK_URL=https://my-app.fly.dev/telegram
fly secrets setTELEGRAM_WEBHOOK_SECRET=$(openssl rand -hex32)
```

2. Expose the webhook port in your `fly.toml`:

```toml
[[services]]
internal_port=8443
protocol="tcp"

[[services.ports]]
handlers=["tls","http"]
port=443
```

3. Deploy:

The gateway log should show: `[telegram] Connected to Telegram (webhook mode)`.

## Proxy Support[​](#proxy-support "Direct link to Proxy Support")

If Telegram's API is blocked or you need to route traffic through a proxy, set a Telegram-specific proxy URL. This takes priority over the generic `HTTPS_PROXY` / `HTTP_PROXY` env vars.

**Option 1: config.yaml (recommended)**

```yaml
telegram:
proxy_url:"socks5://127.0.0.1:1080"
```

**Option 2: environment variable**

```bash
TELEGRAM_PROXY=socks5://127.0.0.1:1080
```

Supported schemes: `http://`, `https://`, `socks5://`.

The proxy applies to both the main Telegram connection and the fallback IP transport. If no Telegram-specific proxy is set, the gateway falls back to `HTTPS_PROXY` / `HTTP_PROXY` / `ALL_PROXY` (or macOS system proxy auto-detection).

## Home Channel[​](#home-channel "Direct link to Home Channel")

Use the `/sethome` command in any Telegram chat (DM or group) to designate it as the **home channel**. Scheduled tasks (cron jobs) deliver their results to this channel.

You can also set it manually in `~/.hermes/.env`:

```bash
TELEGRAM_HOME_CHANNEL=-1001234567890
TELEGRAM_HOME_CHANNEL_NAME="My Notes"
```

tip

Group chat IDs are negative numbers (e.g., `-1001234567890`). Your personal DM chat ID is the same as your user ID.

## Voice Messages[​](#voice-messages "Direct link to Voice Messages")

### Incoming Voice (Speech-to-Text)[​](#incoming-voice-speech-to-text "Direct link to Incoming Voice (Speech-to-Text)")

Voice messages you send on Telegram are automatically transcribed by Hermes's configured STT provider and injected as text into the conversation.

- `local` uses `faster-whisper` on the machine running Hermes — no API key required
- `groq` uses Groq Whisper and requires `GROQ_API_KEY`
- `openai` uses OpenAI Whisper and requires `VOICE_TOOLS_OPENAI_KEY`

### Outgoing Voice (Text-to-Speech)[​](#outgoing-voice-text-to-speech "Direct link to Outgoing Voice (Text-to-Speech)")

When the agent generates audio via TTS, it's delivered as native Telegram **voice bubbles** — the round, inline-playable kind.

- **OpenAI and ElevenLabs** produce Opus natively — no extra setup needed
- **Edge TTS** (the default free provider) outputs MP3 and requires **ffmpeg** to convert to Opus:

```bash
# Ubuntu/Debian
sudoaptinstall ffmpeg

# macOS
brew install ffmpeg
```

Without ffmpeg, Edge TTS audio is sent as a regular audio file (still playable, but uses the rectangular player instead of a voice bubble).

Configure the TTS provider in your `config.yaml` under the `tts.provider` key.

## Group Chat Usage[​](#group-chat-usage "Direct link to Group Chat Usage")

Hermes Agent works in Telegram group chats with a few considerations:

- **Privacy mode** determines what messages the bot can see (see [Step 3](#step-3-privacy-mode-critical-for-groups))
- `TELEGRAM_ALLOWED_USERS` still applies — only authorized users can trigger the bot, even in groups
- You can keep the bot from responding to ordinary group chatter with `telegram.require_mention: true`
- With `telegram.require_mention: true`, group messages are accepted when they are:
  
  - slash commands
  - replies to one of the bot's messages
  - `@botusername` mentions
  - matches for one of your configured regex wake words in `telegram.mention_patterns`
- Use `telegram.ignored_threads` to keep Hermes silent in specific Telegram forum topics, even when the group would otherwise allow free responses or mention-triggered replies
- If `telegram.require_mention` is left unset or false, Hermes keeps the previous open-group behavior and responds to normal group messages it can see

### Example group trigger configuration[​](#example-group-trigger-configuration "Direct link to Example group trigger configuration")

Add this to `~/.hermes/config.yaml`:

```yaml
telegram:
require_mention:true
mention_patterns:
-"^\\s*chompy\\b"
ignored_threads:
-31
-"42"
```

This example allows all the usual direct triggers plus messages that begin with `chompy`, even if they do not use an `@mention`. Messages in Telegram topics `31` and `42` are always ignored before the mention and free-response checks run.

### Notes on `mention_patterns`[​](#notes-on-mention_patterns "Direct link to notes-on-mention_patterns")

- Patterns use Python regular expressions
- Matching is case-insensitive
- Patterns are checked against both text messages and media captions
- Invalid regex patterns are ignored with a warning in the gateway logs rather than crashing the bot
- If you want a pattern to match only at the start of a message, anchor it with `^`

## Private Chat Topics (Bot API 9.4)[​](#private-chat-topics-bot-api-94 "Direct link to Private Chat Topics (Bot API 9.4)")

Telegram Bot API 9.4 (February 2026) introduced **Private Chat Topics** — bots can create forum-style topic threads directly in 1-on-1 DM chats, no supergroup needed. This lets you run multiple isolated workspaces within your existing DM with Hermes.

### Use case[​](#use-case "Direct link to Use case")

If you work on several long-running projects, topics keep their context separate:

- **Topic "Website"** — work on your production web service
- **Topic "Research"** — literature review and paper exploration
- **Topic "General"** — miscellaneous tasks and quick questions

Each topic gets its own conversation session, history, and context — completely isolated from the others.

### Configuration[​](#configuration-1 "Direct link to Configuration")

Prerequisites

Before adding topics to your config, the user must **enable Topics mode** in the DM chat with the bot:

1. Open your private chat with the Hermes bot in Telegram
2. Tap the bot's name at the top to open chat info
3. Enable **Topics** (the toggle to turn the chat into a forum)

Without this, Hermes will log `The chat is not a forum` on startup and skip topic creation. This is a Telegram client-side setting — the bot cannot enable it programmatically.

Add topics under `platforms.telegram.extra.dm_topics` in `~/.hermes/config.yaml`:

```yaml
platforms:
telegram:
extra:
dm_topics:
-chat_id:123456789# Your Telegram user ID
topics:
-name: General
icon_color:7322096
-name: Website
icon_color:9367192
-name: Research
icon_color:16766590
skill: arxiv              # Auto-load a skill in this topic
```

**Fields:**

FieldRequiredDescription`name`YesTopic display name`icon_color`NoTelegram icon color code (integer)`icon_custom_emoji_id`NoCustom emoji ID for the topic icon`skill`NoSkill to auto-load on new sessions in this topic`thread_id`NoAuto-populated after topic creation — don't set manually

### How it works[​](#how-it-works "Direct link to How it works")

1. On gateway startup, Hermes calls `createForumTopic` for each topic that doesn't have a `thread_id` yet
2. The `thread_id` is saved back to `config.yaml` automatically — subsequent restarts skip the API call
3. Each topic maps to an isolated session key: `agent:main:telegram:dm:{chat_id}:{thread_id}`
4. Messages in each topic have their own conversation history, memory flush, and context window

### Skill binding[​](#skill-binding "Direct link to Skill binding")

Topics with a `skill` field automatically load that skill when a new session starts in the topic. This works exactly like typing `/skill-name` at the start of a conversation — the skill content is injected into the first message, and subsequent messages see it in the conversation history.

For example, a topic with `skill: arxiv` will have the arxiv skill pre-loaded whenever its session resets (due to idle timeout, daily reset, or manual `/reset`).

tip

Topics created outside of the config (e.g., by manually calling the Telegram API) are discovered automatically when a `forum_topic_created` service message arrives. You can also add topics to the config while the gateway is running — they'll be picked up on the next cache miss.

## Group Forum Topic Skill Binding[​](#group-forum-topic-skill-binding "Direct link to Group Forum Topic Skill Binding")

Supergroups with **Topics mode** enabled (also called "forum topics") already get session isolation per topic — each `thread_id` maps to its own conversation. But you may want to **auto-load a skill** when messages arrive in a specific group topic, just like DM topic skill binding works.

### Use case[​](#use-case-1 "Direct link to Use case")

A team supergroup with forum topics for different workstreams:

- **Engineering** topic → auto-loads the `software-development` skill
- **Research** topic → auto-loads the `arxiv` skill
- **General** topic → no skill, general-purpose assistant

### Configuration[​](#configuration-2 "Direct link to Configuration")

Add topic bindings under `platforms.telegram.extra.group_topics` in `~/.hermes/config.yaml`:

```yaml
platforms:
telegram:
extra:
group_topics:
-chat_id:-1001234567890# Supergroup ID
topics:
-name: Engineering
thread_id:5
skill: software-development
-name: Research
thread_id:12
skill: arxiv
-name: General
thread_id:1
# No skill — general purpose
```

**Fields:**

FieldRequiredDescription`chat_id`YesThe supergroup's numeric ID (negative number starting with `-100`)`name`NoHuman-readable label for the topic (informational only)`thread_id`YesTelegram forum topic ID — visible in `t.me/c/<group_id>/<thread_id>` links`skill`NoSkill to auto-load on new sessions in this topic

### How it works[​](#how-it-works-1 "Direct link to How it works")

1. When a message arrives in a mapped group topic, Hermes looks up the `chat_id` and `thread_id` in `group_topics` config
2. If a matching entry has a `skill` field, that skill is auto-loaded for the session — identical to DM topic skill binding
3. Topics without a `skill` key get session isolation only (existing behavior, unchanged)
4. Unmapped `thread_id` values or `chat_id` values fall through silently — no error, no skill

### Differences from DM Topics[​](#differences-from-dm-topics "Direct link to Differences from DM Topics")

DM TopicsGroup TopicsConfig key`extra.dm_topics``extra.group_topics`Topic creationHermes creates topics via API if `thread_id` is missingAdmin creates topics in Telegram UI`thread_id`Auto-populated after creationMust be set manually`icon_color` / `icon_custom_emoji_id`SupportedNot applicable (admin controls appearance)Skill binding✓✓Session isolation✓✓ (already built-in for forum topics)

tip

To find a topic's `thread_id`, open the topic in Telegram Web or Desktop and look at the URL: `https://t.me/c/1234567890/5` — the last number (`5`) is the `thread_id`. The `chat_id` for supergroups is the group ID prefixed with `-100` (e.g., group `1234567890` becomes `-1001234567890`).

## Recent Bot API Features[​](#recent-bot-api-features "Direct link to Recent Bot API Features")

- **Bot API 9.4 (Feb 2026):** Private Chat Topics — bots can create forum topics in 1-on-1 DM chats via `createForumTopic`. See [Private Chat Topics](#private-chat-topics-bot-api-94) above.
- **Privacy policy:** Telegram now requires bots to have a privacy policy. Set one via BotFather with `/setprivacy_policy`, or Telegram may auto-generate a placeholder. This is particularly important if your bot is public-facing.
- **Message streaming:** Bot API 9.x added support for streaming long responses, which can improve perceived latency for lengthy agent replies.

## Interactive Model Picker[​](#interactive-model-picker "Direct link to Interactive Model Picker")

When you send `/model` with no arguments in a Telegram chat, Hermes shows an interactive inline keyboard for switching models:

1. **Provider selection** — buttons showing each available provider with model counts (e.g., "OpenAI (15)", "✓ Anthropic (12)" for the current provider).
2. **Model selection** — paginated model list with **Prev**/**Next** navigation, a **Back** button to return to providers, and **Cancel**.

The current model and provider are displayed at the top. All navigation happens by editing the same message in-place (no chat clutter).

tip

If you know the exact model name, type `/model <name>` directly to skip the picker. You can also type `/model <name> --global` to persist the change across sessions.

## DNS-over-HTTPS Fallback IPs[​](#dns-over-https-fallback-ips "Direct link to DNS-over-HTTPS Fallback IPs")

In some restricted networks, `api.telegram.org` may resolve to an IP that is unreachable. The Telegram adapter includes a **fallback IP** mechanism that transparently retries connections against alternative IPs while preserving the correct TLS hostname and SNI.

### How it works[​](#how-it-works-2 "Direct link to How it works")

1. If `TELEGRAM_FALLBACK_IPS` is set, those IPs are used directly.
2. Otherwise, the adapter automatically queries **Google DNS** and **Cloudflare DNS** via DNS-over-HTTPS (DoH) to discover alternative IPs for `api.telegram.org`.
3. IPs returned by DoH that differ from the system DNS result are used as fallbacks.
4. If DoH is also blocked, a hardcoded seed IP (`149.154.167.220`) is used as a last resort.
5. Once a fallback IP succeeds, it becomes "sticky" — subsequent requests use it directly without retrying the primary path first.

### Configuration[​](#configuration-3 "Direct link to Configuration")

```bash
# Explicit fallback IPs (comma-separated)
TELEGRAM_FALLBACK_IPS=149.154.167.220,149.154.167.221
```

Or in `~/.hermes/config.yaml`:

```yaml
platforms:
telegram:
extra:
fallback_ips:
-"149.154.167.220"
```

tip

You usually don't need to configure this manually. The auto-discovery via DoH handles most restricted-network scenarios. The `TELEGRAM_FALLBACK_IPS` env var is only needed if DoH is also blocked on your network.

## Proxy Support[​](#proxy-support-1 "Direct link to Proxy Support")

If your network requires an HTTP proxy to reach the internet (common in corporate environments), the Telegram adapter automatically reads standard proxy environment variables and routes all connections through the proxy.

### Supported variables[​](#supported-variables "Direct link to Supported variables")

The adapter checks these environment variables in order, using the first one that is set:

1. `HTTPS_PROXY`
2. `HTTP_PROXY`
3. `ALL_PROXY`
4. `https_proxy` / `http_proxy` / `all_proxy` (lowercase variants)

### Configuration[​](#configuration-4 "Direct link to Configuration")

Set the proxy in your environment before starting the gateway:

```bash
exportHTTPS_PROXY=http://proxy.example.com:8080
hermes gateway
```

Or add it to `~/.hermes/.env`:

```bash
HTTPS_PROXY=http://proxy.example.com:8080
```

The proxy applies to both the primary transport and all fallback IP transports. No additional Hermes configuration is needed — if the environment variable is set, it's used automatically.

note

This covers the custom fallback transport layer that Hermes uses for Telegram connections. The standard `httpx` client used elsewhere already respects proxy env vars natively.

## Message Reactions[​](#message-reactions "Direct link to Message Reactions")

The bot can add emoji reactions to messages as visual processing feedback:

- 👀 when the bot starts processing your message
- ✅ when the response is delivered successfully
- ❌ if an error occurs during processing

Reactions are **disabled by default**. Enable them in `config.yaml`:

```yaml
telegram:
reactions:true
```

Or via environment variable:

note

Unlike Discord (where reactions are additive), Telegram's Bot API replaces all bot reactions in a single call. The transition from 👀 to ✅/❌ happens atomically — you won't see both at once.

tip

If the bot doesn't have permission to add reactions in a group, the reaction calls fail silently and message processing continues normally.

## Per-Channel Prompts[​](#per-channel-prompts "Direct link to Per-Channel Prompts")

Assign ephemeral system prompts to specific Telegram groups or forum topics. The prompt is injected at runtime on every turn — never persisted to transcript history — so changes take effect immediately.

```yaml
telegram:
channel_prompts:
"-1001234567890":|
      You are a research assistant. Focus on academic sources,
      citations, and concise synthesis.
"42":|
      This topic is for creative writing feedback. Be warm and
      constructive.
```

Keys are chat IDs (groups/supergroups) or forum topic IDs. For forum groups, topic-level prompts override the group-level prompt:

- Message in topic `42` inside group `-1001234567890` → uses topic `42`'s prompt
- Message in topic `99` (no explicit entry) → falls back to group `-1001234567890`'s prompt
- Message in a group with no entry → no channel prompt applied

Numeric YAML keys are automatically normalized to strings.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

ProblemSolutionBot not responding at allVerify `TELEGRAM_BOT_TOKEN` is correct. Check `hermes gateway` logs for errors.Bot responds with "unauthorized"Your user ID is not in `TELEGRAM_ALLOWED_USERS`. Double-check with @userinfobot.Bot ignores group messagesPrivacy mode is likely on. Disable it (Step 3) or make the bot a group admin. **Remember to remove and re-add the bot after changing privacy.**Voice messages not transcribedVerify STT is available: install `faster-whisper` for local transcription, or set `GROQ_API_KEY` / `VOICE_TOOLS_OPENAI_KEY` in `~/.hermes/.env`.Voice replies are files, not bubblesInstall `ffmpeg` (needed for Edge TTS Opus conversion).Bot token revoked/invalidGenerate a new token via `/revoke` then `/newbot` or `/token` in BotFather. Update your `.env` file.Webhook not receiving updatesVerify `TELEGRAM_WEBHOOK_URL` is publicly reachable (test with `curl`). Ensure your platform/reverse proxy routes inbound HTTPS traffic from the URL's port to the local listen port configured by `TELEGRAM_WEBHOOK_PORT` (they do not need to be the same number). Ensure SSL/TLS is active — Telegram only sends to HTTPS URLs. Check firewall rules.

## Exec Approval[​](#exec-approval "Direct link to Exec Approval")

When the agent tries to run a potentially dangerous command, it asks you for approval in the chat:

> ⚠️ This command is potentially dangerous (recursive delete). Reply "yes" to approve.

Reply "yes"/"y" to approve or "no"/"n" to deny.

## Security[​](#security "Direct link to Security")

warning

Always set `TELEGRAM_ALLOWED_USERS` to restrict who can interact with your bot. Without it, the gateway denies all users by default as a safety measure.

Never share your bot token publicly. If compromised, revoke it immediately via BotFather's `/revoke` command.

For more details, see the [Security documentation](https://hermes-agent.nousresearch.com/docs/user-guide/security). You can also use [DM pairing](https://hermes-agent.nousresearch.com/docs/user-guide/messaging#dm-pairing-alternative-to-allowlists) for a more dynamic approach to user authorization.