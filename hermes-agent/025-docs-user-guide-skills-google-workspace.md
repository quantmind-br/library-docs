---
title: Google Workspace — Gmail, Calendar, Drive, Sheets & Docs | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/google-workspace
source: crawler
fetched_at: 2026-04-24T17:00:25.436768503-03:00
rendered_js: false
word_count: 455
summary: This document details how Hermes integrates with various Google Workspace applications (Gmail, Calendar, Drive, Sheets, Docs, Contacts) using OAuth2 authentication. It provides detailed instructions for setup and numerous command examples showing how to perform specific actions on each service.
tags:
    - google-workspace
    - gmail-api
    - calendar-management
    - sheets-integration
    - oauth2-auth
    - gws-cli
    - productivity-tools
category: reference
---

Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration for Hermes. Uses OAuth2 with automatic token refresh. Prefers the [Google Workspace CLI (`gws`)](https://github.com/nicholasgasior/gws) when available for broader coverage, and falls back to Google's Python client libraries otherwise.

**Skill path:** `skills/productivity/google-workspace/`

## Setup[​](#setup "Direct link to Setup")

The setup is fully agent-driven — ask Hermes to set up Google Workspace and it walks you through each step. The flow:

1. **Create a Google Cloud project** and enable the required APIs (Gmail, Calendar, Drive, Sheets, Docs, People)
2. **Create OAuth 2.0 credentials** (Desktop app type) and download the client secret JSON
3. **Authorize** — Hermes generates an auth URL, you approve in the browser, paste back the redirect URL
4. **Done** — token auto-refreshes from that point on

Email-only users

If you only need email (no Calendar/Drive/Sheets), use the **himalaya** skill instead — it works with a Gmail App Password and takes 2 minutes. No Google Cloud project needed.

## Gmail[​](#gmail "Direct link to Gmail")

### Searching[​](#searching "Direct link to Searching")

```bash
$GAPI gmail search "is:unread"--max10
$GAPI gmail search "from:boss@company.com newer_than:1d"
$GAPI gmail search "has:attachment filename:pdf newer_than:7d"
```

Returns JSON with `id`, `from`, `subject`, `date`, `snippet`, and `labels` for each message.

### Reading[​](#reading "Direct link to Reading")

```bash
$GAPI gmail get MESSAGE_ID
```

Returns the full message body as text (prefers plain text, falls back to HTML).

### Sending[​](#sending "Direct link to Sending")

```bash
# Basic send
$GAPI gmail send --to user@example.com --subject"Hello"--body"Message text"

# HTML email
$GAPI gmail send --to user@example.com --subject"Report"\
--body"<h1>Q4 Results</h1><p>Details here</p>"--html

# Custom From header (display name + email)
$GAPI gmail send --to user@example.com --subject"Hello"\
--from'"Research Agent" <user@example.com>'--body"Message text"

# With CC
$GAPI gmail send --to user@example.com --cc"team@example.com"\
--subject"Update"--body"FYI"
```

The `--from` flag lets you customize the sender display name on outgoing emails. This is useful when multiple agents share the same Gmail account but you want recipients to see different names:

```bash
# Agent 1
$GAPI gmail send --to client@co.com --subject"Research Summary"\
--from'"Research Agent" <shared@company.com>'--body"..."

# Agent 2  
$GAPI gmail send --to client@co.com --subject"Code Review"\
--from'"Code Assistant" <shared@company.com>'--body"..."
```

**How it works:** The `--from` value is set as the RFC 5322 `From` header on the MIME message. Gmail allows customizing the display name on your own authenticated email address without any additional configuration. Recipients see the custom display name (e.g. "Research Agent") while the email address stays the same.

**Important:** If you use a *different email address* in `--from` (not the authenticated account), Gmail requires that address to be configured as a [Send As alias](https://support.google.com/mail/answer/22370) in Gmail Settings → Accounts → Send mail as.

The `--from` flag works on both `send` and `reply`:

```bash
$GAPI gmail reply MESSAGE_ID \
--from'"Support Bot" <shared@company.com>'--body"We're on it"
```

### Replying[​](#replying "Direct link to Replying")

```bash
$GAPI gmail reply MESSAGE_ID --body"Thanks, that works for me."
```

Automatically threads the reply (sets `In-Reply-To` and `References` headers) and uses the original message's thread ID.

### Labels[​](#labels "Direct link to Labels")

```bash
# List all labels
$GAPI gmail labels

# Add/remove labels
$GAPI gmail modify MESSAGE_ID --add-labels LABEL_ID
$GAPI gmail modify MESSAGE_ID --remove-labels UNREAD
```

## Calendar[​](#calendar "Direct link to Calendar")

```bash
# List events (defaults to next 7 days)
$GAPI calendar list
$GAPI calendar list --start2026-03-01T00:00:00Z --end2026-03-07T23:59:59Z

# Create event (timezone required)
$GAPI calendar create --summary"Team Standup"\
--start2026-03-01T10:00:00-07:00 --end2026-03-01T10:30:00-07:00

# With location and attendees
$GAPI calendar create --summary"Lunch"\
--start2026-03-01T12:00:00Z --end2026-03-01T13:00:00Z \
--location"Cafe"--attendees"alice@co.com,bob@co.com"

# Delete event
$GAPI calendar delete EVENT_ID
```

warning

Calendar times **must** include a timezone offset (e.g. `-07:00`) or use UTC (`Z`). Bare datetimes like `2026-03-01T10:00:00` are ambiguous and will be treated as UTC.

## Drive[​](#drive "Direct link to Drive")

```bash
$GAPI drive search "quarterly report"--max10
$GAPI drive search "mimeType='application/pdf'" --raw-query --max5
```

## Sheets[​](#sheets "Direct link to Sheets")

```bash
# Read a range
$GAPI sheets get SHEET_ID "Sheet1!A1:D10"

# Write to a range
$GAPI sheets update SHEET_ID "Sheet1!A1:B2"--values'[["Name","Score"],["Alice","95"]]'

# Append rows
$GAPI sheets append SHEET_ID "Sheet1!A:C"--values'[["new","row","data"]]'
```

## Docs[​](#docs "Direct link to Docs")

Returns the document title and full text content.

```bash
$GAPI contacts list --max20
```

## Output Format[​](#output-format "Direct link to Output Format")

All commands return JSON. Key fields per service:

CommandFields`gmail search``id`, `threadId`, `from`, `to`, `subject`, `date`, `snippet`, `labels``gmail get``id`, `threadId`, `from`, `to`, `subject`, `date`, `labels`, `body``gmail send/reply``status`, `id`, `threadId``calendar list``id`, `summary`, `start`, `end`, `location`, `description`, `htmlLink``calendar create``status`, `id`, `summary`, `htmlLink``drive search``id`, `name`, `mimeType`, `modifiedTime`, `webViewLink``contacts list``name`, `emails`, `phones``sheets get`2D array of cell values

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

ProblemFix`NOT_AUTHENTICATED`Run setup (ask Hermes to set up Google Workspace)`REFRESH_FAILED`Token revoked — re-run authorization steps`HttpError 403: Insufficient Permission`Missing scope — revoke and re-authorize with the right services`HttpError 403: Access Not Configured`API not enabled in Google Cloud Console`ModuleNotFoundError`Run setup script with `--install-deps`