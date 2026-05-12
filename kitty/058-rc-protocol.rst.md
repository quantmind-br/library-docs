---
title: The kitty remote control protocol
title: The kitty remote control protocol
word_count: 272
summary: JSON-based remote control protocol for kitty with encrypted communication and async/streaming request support.
category: reference
optimized: true
optimized_at: 2026-05-04T20:46:03Z
---
# The kitty remote control protocol

Simple JSON-based protocol for sending commands to kitty.

## Message format

```
<ESC>P@kitty-cmd<JSON object><ESC>\
```

`ESC` = byte `0x1b`.

### JSON structure

```json
{
    "cmd": "command name",
    "version": "<kitty version>",
    "no_response": "<Optional Boolean>",
    "kitty_window_id": "<Optional value of KITTY_WINDOW_ID env var>",
    "payload": "<Optional JSON object>"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `cmd` | string | Command name |
| `version` | array | `[0, 14, 2]` format — use version you're developing against |
| `no_response` | boolean | Set `true` to skip response |
| `kitty_window_id` | string | Match specific window |
| `payload` | object | Command-specific fields |

> [!warning]
> Version must not exceed kitty instance version — causes failure.

## Quick example

Run kitty:
```bash
kitty -o allow_remote_control=socket-only --listen-on unix:/tmp/test
```

Send command:
```bash
echo -en '\eP@kitty-cmd{"cmd":"ls","version":[0,14,2]}\e\\' | socat - unix:/tmp/test | awk '{ print substr($0, 13, length($0) - 14) }' | jq -c '.data | fromjson' | jq .
```

Or use `kitten` (from [[023-binary|releases]]):
```bash
kitten @ --help
```

## Encrypted communication

When using `remote_control_password`, communication is encrypted.

### Protocol

- Key from `KITTY_PUBLIC_KEY` env var (protocol `1`, Base-85 encoded)
- Algorithm: ECDH X25519 + AES-256-GCM
- Time-based nonce (nanoseconds since epoch)
- Commands with timestamp >5 minutes from now rejected

### Encryption process

1. Original JSON gets `password` and `timestamp` fields added
2. Encrypted with AES-256-GCM (authenticated encryption)
3. Symmetric key derived: ECDH shared secret → SHA-256 hash
4. IV: 96+ bits CSPRNG
5. Auth tag: 128+ bits

### Encrypted command format

```json
{
    "version": "<kitty version>",
    "iv": "base85 encoded IV",
    "tag": "base85 encoded AEAD tag",
    "pubkey": "base85 encoded ECDH public key of sender",
    "encrypted": "Original command encrypted and base85 encoded"
}
```

## Async and streaming requests

### Async requests

Commands like `select-window` wait for user action. Set `async` to random string ID:

```json
{
    "cmd": "select-window",
    "async": "<unique-id>"
}
```

Cancel with `cancel_async` field. Cancellation doesn't need encryption (no user prompts).

### Streaming requests

For large data, split into chunks:

| Field | Description |
|-------|-------------|
| `stream` | `true` for streaming chunks |
| `stream_id` | Same random string for all chunks |
| Final chunk | Empty data to end stream |

#kitty-terminal #remote-control #json-api #encryption
