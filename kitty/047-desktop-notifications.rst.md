---
title: Desktop notifications
title: Desktop notifications
word_count: 843
summary: This document describes the OSC 99 escape sequence protocol used by the kitty terminal to display, manage, and interact with desktop notifications.
category: reference
optimized: true
optimized_at: 2026-05-04T20:46:47Z
---
# Desktop notifications

|kitty| implements OSC 99 escape sequence for desktop notifications with title/body, click actions, icons, buttons, and sounds.

## Protocol format

```
<OSC> 99 ; metadata ; payload <terminator>
```

- `<OSC>` = `<ESC>]`
- `<terminator>` = `<ESC>\`
- `metadata` = colon-separated `key=value` pairs
- Keys: single character `[a-zA-Z]`
- Values: `[a-zA-Z0-9-_/\+.,(){}[]*&^%$#@!~]`
- Payloads interpreted based on `p` key

## Quick examples

Simple notification:
```bash
printf '\x1b]99;;Hello world\x1b\\'
```

With title and body:
```bash
printf '\x1b]99;i=1:d=0;Hello world\x1b\\'
printf '\x1b]99;i=1:p=body;This is cool\x1b\\'
```

> [!tip]
> Use the built-in `kitten notify` command:
> ```bash
> kitten notify "Hello world" A good day to you
> ```

## Chunking

Different terminals have different escape code limits. Chunking uses:
- `i` — notification id (identifier)
- `d` — done flag (`0`=incomplete, `1`=complete)

Send title/body chunks with `d=0`, finalize with `d=1`. Concatenated text can be arbitrarily long (terminals may impose sensible limits). Payload max: 2048 bytes raw, 4096 base64-encoded.

## Filtering notifications

Applications identify themselves with:
- `f` — application name (base64 UTF-8, ideally `.desktop` filename or macOS bundle id)
- `t` — notification type (base64 UTF-8, can repeat for multiple types)

> [!NOTE]
> The `f` key allows the terminal to deduce an icon for the notification.

> [!tip]
> kitty provides sophisticated notification filtering via `filter_notification`.

## User activation responses

When user clicks the notification, `a` key controls actions:
- `focus` — focus the originating window (default)
- `report` — send escape code back to application

```
<OSC> 99 ; i=identifier ; <terminator>
```

Use `a=-focus` to disable all actions.

## Close notifications

Request close notification with `c=1`:

```
<OSC> 99 ; i=mynotification : c=1 ; hello world <terminator>
```

Terminal replies:
```
<OSC> 99 ; i=mynotification : p=close ; <terminator>
```

> [!NOTE]
> On macOS, the OS doesn't inform apps of closures. Terminal replies with `untracked`:
> ```
> <OSC> 99 ; i=mynotification : p=close ; untracked <terminator>
> ```

Poll for alive notifications:
```
<OSC> 99 ; i=myid : p=alive ; <terminator>
```
Reply:
```
<OSC> 99 ; i=myid : p=alive ; id1,id2,id3 <terminator>
```

## Updating notifications

Send new notification with same `i` key to update. On Linux, replacement is flicker-free; on macOS it is not.

## Auto-expiring

- `w=-1` (default) — use OS expiry policy
- `w=0` — never expire
- `w=N` — expire after N milliseconds (robust: terminal implements directly)

## Icons

### By name (`n` key)

Base64-encoded icon name. Resolved against system icons/applications. Supported names:

- Application identifiers (`.desktop` filename or bundle id)
- Symbol names

Multiple `n` keys allowed; terminal uses first available.

### By image data (`p=icon`)

- Formats: PNG, JPEG, GIF
- Recommended size: 256x256
- Must use `e=1` (base64 encoded)

### Icon caching (`g` key)

Cache icon data with a UUID-like identifier:
```
<OSC> 99 ; i=id : p=icon : e=1 : g=uuid ; <base64-data> <terminator>
```
Future notifications use just `g=uuid`. Cache persists for terminal session.

> [!NOTE]
> Terminals may impose max cache size and evict by LRU. Failure mode: icon not displayed.

## Buttons

Add buttons with `p=buttons`. UTF-8 text separated by U+2028 (LINE SEPARATOR). Safe UTF-8 or base64.

When clicked with `a=report`:
```
<OSC> 99 ; i=identifier ; button_number <terminator>
```
`button_number` = 1 for first button, 2 for second, etc.

> [!NOTE]
> On Linux, buttons appear individually. On macOS, they appear in a dropdown menu. Use 2-3 buttons maximum.

## Sounds

Use `s` key (base64 UTF-8 sound name):
- `silent` — no sound
- `system` — play platform default
- Other names — implementation dependent (Linux: standard sound names)

## Querying support

```
<OSC> 99 ; i=<id> : p=? ; <terminator>
```

Response:
```
<OSC> 99 ; i=<id> : p=? ; key=value : key=value <terminator>
```

| Key | Description |
|-----|-------------|
| `a` | Supported actions (comma-separated) |
| `c` | `c=1` if close events supported |
| `o` | Supported occasions: `always`, `unfocused`, `invisible` |
| `p` | Supported payload types (minimum: `title`) |
| `s` | Supported sound names |
| `u` | Supported urgency values (`0`, `1`, `2`) |
| `w` | `w=1` if auto-expiry supported |

## Key reference

| Key | Value | Default | Description |
|-----|-------|---------|-------------|
| `a` | `report`,`focus`,`-` prefix | `focus` | Actions on click |
| `c` | `0` or `1` | `0` | Send escape code on close |
| `d` | `0` or `1` | `1` | Notification complete |
| `e` | `0` or `1` | `0` | Payload is base64 encoded |
| `f` | base64 UTF-8 | unset | Application name for filtering |
| `g` | identifier | unset | Icon cache key (UUID-like) |
| `i` | identifier | unset | Notification ID (UUID-like, avoid `0`) |
| `n` | base64 UTF-8 | unset | Icon name (can repeat) |
| `o` | `always`,`unfocused`,`invisible` | `always` | When to honor request |
| `p` | `title`,`body`,`close`,`icon`,`?`,`alive`,`buttons` | `title` | Payload type |
| `s` | base64 sound name | `system` | Sound to play |
| `t` | base64 UTF-8 | unset | Notification type (can repeat) |
| `u` | `0`,`1`,`2` | unset | Urgency: low/normal/critical |
| `w` | `>=-1` | `-1` | Auto-close milliseconds |

## Base64 encoding

Per RFC 4648. Chunk before or after encoding:
- Before: max 2048 bytes raw per chunk, include padding
- After: max 4096 bytes encoded per chunk

## Safe UTF-8

Valid UTF-8 per RFC 3629. No C0/C1 control characters:
- U+0000–U+001F, U+007F, U+0080–U+009F forbidden

## Identifiers

Characters: `[a-zA-Z0-9_-+.]` (globally unique, UUID-like).

> [!IMPORTANT]
> Terminals must sanitize identifiers from clients to prevent injection attacks. Reject or strip invalid characters before echoing in responses.

## Legacy support

kitty supports iTerm2's OSC 9 protocol for backward compatibility.

#terminal-emulators #osc-99 #desktop-notifications #escape-codes
