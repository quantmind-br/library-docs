---
title: MultipleInstructionsDisallowed
url: https://docs.docker.com/reference/build-checks/multiple-instructions-disallowed/
source: llms
fetched_at: 2026-01-24T14:32:23.445207416-03:00
rendered_js: false
word_count: 68
summary: This document explains that Dockerfiles should only contain a single instance of CMD, HEALTHCHECK, or ENTRYPOINT instructions per stage, as only the final occurrence is executed.
tags:
    - docker
    - dockerfile
    - best-practices
    - entrypoint
    - cmd
    - healthcheck
category: reference
---

Table of contents

* * *

## [Output](#output)

```
Multiple CMD instructions should not be used in the same stage because only the last one will be used
```

## [Description](#description)

If you have multiple `CMD`, `HEALTHCHECK`, or `ENTRYPOINT` instructions in your Dockerfile, only the last occurrence is used. An image can only ever have one `CMD`, `HEALTHCHECK`, and `ENTRYPOINT`.

## [Examples](#examples)

❌ Bad: Duplicate instructions.

```
FROMalpineENTRYPOINT ["echo", "Hello, Norway!"]ENTRYPOINT ["echo", "Hello, Sweden!"]# Only "Hello, Sweden!" will be printed
```

✅ Good: only one `ENTRYPOINT` instruction.

```
FROMalpineENTRYPOINT ["echo", "Hello, Norway!\nHello, Sweden!"]
```

You can have both a regular, top-level `CMD` and a separate `CMD` for a `HEALTHCHECK` instruction.

✅ Good: only one top-level `CMD` instruction.

```
FROMpython:alpineRUN apk add curlHEALTHCHECK --interval=1s --timeout=3s \
  CMD ["curl", "-f", "http://localhost:8080"]CMD ["python", "-m", "http.server", "8080"]
```