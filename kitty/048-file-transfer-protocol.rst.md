---
title: File transfer over the TTY
title: File transfer protocol
word_count: 548
summary: This document outlines a protocol for transferring files, directories, and links over a TTY interface, including security requirements for session authorization and bidirectional data flow handling.
category: reference
optimized: true
optimized_at: 2026-05-04T20:46:47Z
---
# File transfer over the TTY

Transfer files, directories, and links over a TTY using OSC 5113 escape codes. Supports compression, rsync-style binary deltas, and user authorization.

## Protocol design

- Transfer "sessions" with bidirectional commands
- Session must be user-approved unless pre-shared password provided
- Session id: random unique identifier (avoid conflicts)
- Commands: `action`, `id`, action-specific fields
- Data chunks: max 4096 bytes

## Escape code format

```
<OSC> 5113 ; key=value ; key=value ... <ST>
```

- `OSC` = `0x1b 0x5d`
- `ST` = `0x1b 0x5c`
- `5113` = numeralization of "file"
- Key names serialized short (e.g., `permissions` → `prm`)

### Value types

| Type | Format |
|------|--------|
| enum | From permitted set |
| safe_string | `[0-9a-zA-Z_:./@-]` |
| integer | Base-10, optional leading `-` |
| base64_string | Standard base64 UTF-8 |
| base64_bytes | Standard base64 binary |

## Sending files to terminal

### 1. Start session
```
→ action=send id=someid
```

Wait for status before sending more commands.

Response:
```
← action=status id=someid status=OK
← action=status id=someid status=EPERM:User refused the transfer
```

### 2. Send file metadata
```
→ action=file id=someid file_id=f1 name=/path/to/destination
→ action=file id=someid file_id=f2 name=/path/to/destination2 ftype=directory
```

Response:
```
← action=status id=someid file_id=f1 status=STARTED
← action=status id=someid file_id=f2 status=OK
```

### 3. Send file data
```
→ action=data id=someid file_id=f1 data=chunk
→ action=end_data id=someid file_id=f1 data=last_chunk
```

Terminal acknowledges:
```
← action=status id=someid file_id=f1 status=PROGRESS size=bytes
← action=status id=someid file_id=f1 status=OK size=bytes
```

### 4. Finish session
```
→ action=finish id=someid
```

## Receiving files from terminal

### 1. Start session
```
→ action=receive id=someid size=num_of_paths
→ action=file id=someid file_id=f1 name=/some/path
```

Wait for `OK` response.

### 2. Receive file listing

Terminal sends metadata for all files recursively (symlinks not followed):
```
← action=file id=someid file_id=f1 mtime=XXX permissions=XXX name=/path status=file_id1 size=N ftype=type parent=parent_id
```

Ends with home directory path:
```
← action=status id=someid status=OK name=/path/to/home
```

### 3. Request file data
```
→ action=file id=someid file_id=f1 name=/some/path
```

Terminal sends data:
```
← action=data id=someid file_id=f1 data=chunk
← action=end_data id=someid file_id=f1 data=last_chunk
```

### 4. Finish session
```
→ action=finished id=someid
```

## Canceling sessions

```
→ action=cancel id=someid
← action=status id=someid status=CANCELED
```

Client must wait for cancel response, discarding other responses.

## Quiet mode

Add `quiet` to start command:
- `quiet=1` — suppress acknowledgements
- `quiet=2` — suppress all responses except data

Useful for shell scripts with `bypass_auth`.

## File metadata

### Paths
- UTF-8 encoded POSIX paths (forward slash `/`)
- `~/` = relative to HOME
- Absolute or HOME-relative only
- Max component: 255 bytes
- Max total: 4096 bytes
- Windows: `/C:/path/to/file`
- Omit from paths: `\ * : < > ? | /`

### Modification times
- Nanoseconds since UNIX epoch
- Use closest approximation if filesystem less precise

### Permissions
- UNIX read/write/execute bits + sticky/setgid/setuid
- Windows: read-only bit only
  - Write: set read-only if user write bit clear
  - Read: always set all READ bits; set EXECUTE if Windows-executable

## Symbolic and hard links

### Sending links

```
→ action=file id=someid file_id=f1 name=/path/to/link ftype=link
→ action=file id=someid file_id=f2 name=/path/to/symlink ftype=symlink
```

Hardlink data: target file_id as UTF-8:
```
→ action=end_data id=someid file_id=f1 data=target_file_id
```

Symlink data:
- Transmitted file: `fid:target_file_id` or `fid_abs:target_file_id`
- External file: `path:actual_path`

### Receiving links

First listing sets `file_type` and `data` to target file_id:
```
← action=file id=someid file_id=f1 status=file_id1 ...
← action=file id=someid file_id=f2 status=file_id1 ftype=symlink data=file_id1 ...
```

Client creates hardlinks directly. Terminal sends symlink target path for client to resolve.

## Binary deltas (rsync algorithm)

Use `transmission_type=rsync` for changed-file transfers.

### Signature format (12 byte header)

```
uint16 version      (must be 0)
uint16 checksum_type (0 = XXH3-128)
uint16 strong_hash_type (0 = XXH3-64)
uint16 weak_hash_type (0 = rsync rolling checksum)
uint32 block_size   (usually sqrt of file size)
```

### Block signature (16 bytes each)

```
uint64 index        (zero-based block number)
uint32 weak_hash
uint64 strong_hash
```

Block position: `index * block_size`

### Delta operations

| Type | Value | Data |
|------|-------|------|
| Block | `0` | `uint64` block index |
| Data | `1` | `uint32` size + payload |
| Hash | `2` | `uint16` checksum size + checksum |
| BlockRange | `3` | `uint64` start + `uint32` count |

## Compression

Add `compression=zlib` to file metadata:
```
→ action=file id=someid file_id=f1 name=/path compression=zlib
```

Only DEFLATE (RFC 1950) supported.

## Bypass authorization

Use pre-shared secret (password) to skip interactive auth:
```
→ action=send id=someid bypass=sha256:hash_value
```

Hash value: `sha256("session_id" + ";" + "password")`

> [!WARNING]
> Hashing doesn't hide the password effectively. Use only in trusted contexts. kitty uses public key encryption via `KITTY_PUBLIC_KEY` (see `check_bypass()` in source).

## Example serialization

Input:
```
action=send id=test name=somefile size=3 data=01 02 03
```

Output:
```
<OSC> 5113 ; ac=send ; id=test ; n=c29tZWZpbGU= ; sz=3 ; d=AQID <ST>
```

#tty #file-transfer #protocol-design #terminal-emulator #data-transmission
