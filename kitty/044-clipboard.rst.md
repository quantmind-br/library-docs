---
title: Copying all data types to the clipboard
title: Copying all data types to the clipboard
word_count: 519
summary: OSC 5522 clipboard protocol for terminal emulators supporting arbitrary data types, MIME type handling, permission management, and multiplexed clipboard access.
optimized: true
optimized_at: 2026-05-04T20:45:41Z
---
# Copying all data types to the clipboard

kitty implements **OSC 5522**, an extension of OSC 52 that supports:
- Copying arbitrary data (images, rich text, etc.)
- User permission prompts for clipboard access

**Format:** `<OSC>5522;metadata;payload<ST>`

Where `metadata` is colon-separated key-value pairs and `payload` is base64-encoded data. OSC is `<ESC>[`, ST is `<ESC>\`.

## Reading from clipboard

**Request:**
```
<OSC>5522;type=read;<base64 MIME types><ST>
```

Payload is a space-separated list of MIME types to read (e.g., `text/plain image/png`).

Add `loc=primary` to metadata to read from the primary selection instead of the clipboard.

To list available MIME types, use `.` (period) as the payload.

**Terminal response sequence:**
```
<OSC>5522;type=read:status=OK<ST>
<OSC>5522;type=read:status=DATA:mime=<base64 MIME>;<base64 data><ST>
...
<OSC>5522;type=read:status=DONE<ST>
```

> [!important]
> Chunk data into packets of **4096 bytes maximum** (pre-base64). Transmit all chunks for one MIME type sequentially before moving to the next type.

**Read error codes:**
| Code | Meaning |
|------|---------|
| `ENOSYS` | Requested clipboard type unavailable (e.g., primary selection not supported) |
| `EPERM` | Permission denied |
| `EBUSY` | Temporary problem (e.g., multiplexer conflict) |

> [!note]
> Terminals should prompt for permission before read requests. Requests listing only available MIME types (`payload=.") should be allowed without prompting to avoid double prompts.

## Writing to clipboard

**Sequence:**
```
<OSC>5522;type=write<ST>
<OSC>5522;type=wdata:mime=<base64 MIME>;<base64 chunk><ST>
...
<OSC>5522;type=wdata<ST>
```

Final packet with no mime/data indicates end of transmission.

**Terminal response:**
```
<OSC>5522;type=write:status=DONE<ST>
```

**Write error codes:**
| Code | Meaning |
|------|---------|
| `EIO` | I/O error during processing |
| `EINVAL` | Invalid base64 encoding |
| `ENOSYS` | Primary selection (`loc=primary`) unavailable |
| `EPERM` | Permission denied |
| `EBUSY` | Temporary problem (e.g., multiplexer conflict) |

> [!warning]
> After an error occurs, ignore all further OSC 5522 write packets until a new `type=write` packet.

Use `loc=primary` in the initial `type=write` packet to write to the primary selection.

### MIME type aliases

```
<OSC>5522;type=walias;mime=<base64 target MIME>;<base64 aliases><ST>
```

System clipboard makes all aliased MIME types available with the same data. Alias packets can be sent after the initial write packet and before the end-of-data packet.

## Avoiding repeated permission prompts

Send a password and human-friendly name with requests:

```conf
<OSC>5522;type=read;pw=<base64 UUID4>;name=<base64 name><ST>
<OSC>5522;type=write;pw=<base64 UUID4>;name=<base64 name><ST>
```

The terminal prompts once to allow all future requests with that password on the same TTY.

> [!tip]
> Programs should generate a random UUID4 password at startup. Terminals may implement permanent stored passwords.

## Paste events

Applications can handle paste events (bracketed paste MIME listing) by enabling private mode 5522:

- `CSI ? 5522 h` to enable
- `CSI ? 5522 l` to disable

When enabled, the terminal sends clipboard MIME types on paste and includes a one-time password (`pw` key, base64) allowing the application to request data without further prompts.

## Detecting protocol support

Query with DECRQM:
```
CSI ? 5522 $ p
```

Response: `CSI ? 5522 ; Ps $ y`

A Ps value of 0 or 4 means unsupported.

## Terminal multiplexer support

Include an optional `id` field in metadata; the terminal echoes it unchanged in every response. Valid characters: `[a-zA-Z0-9-_+.]`.

> [!warning]
> Multiple programs can overwrite each other's clipboard requests. Responses may be lost with simultaneous write requests. Ensure only one request is in flight at a time; abort with `EBUSY` if conflicts occur.

For unsolicited paste events (no associated id), multiplexers must forward to the currently active window.

#osc-5522 #clipboard #terminal-protocol
