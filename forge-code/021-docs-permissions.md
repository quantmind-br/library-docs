---
title: "Permissions in ForgeCode"
url: https://forgecode.dev/docs/permissions/
source: sitemap
fetched_at: 2026-04-30T14:09:14.607232927-03:00
rendered_js: false
word_count: 270
summary: "Configure `permissions.yaml` to restrict built-in tool operations in ForgeCode's restricted mode."
tags:
  - security-policy
  - access-control
  - restricted-mode
  - forgecode-configuration
  - tool-permissions
category: configuration
optimized: true
---
# Permissions in ForgeCode

> **TL;DR**
> Use `permissions.yaml` to control tool access when `restricted = true` in `.forge.toml`.

## Basics

- **File**: `~/.forge/permissions.yaml` (or `$FORGE_CONFIG/permissions.yaml`).
- **Default**: Allow-all if file doesn’t exist.
- **Fallback**: `confirm` for unmatched operations.

## Enabling Restricted Mode
```toml
# ~/.forge/.forge.toml
restricted = true
```

## Policy Structure

### Top-Level Key
```yaml
policy:
  - permission: allow|deny|confirm
    rule: { ... }
```

### Permission Values
| Value | Behavior |
|-------|----------|
| `allow` | Run immediately |
| `deny` | Reject immediately |
| `confirm` | Ask before proceeding |

### Rule Types
| Key | Matches | Example |
|-----|---------|---------|
| `read` | File reads/searches | `"docs/**/*"` |
| `write` | Writes/patches/deletes | `"src/**/*"` |
| `command` | Shell commands | `"git *"` |
| `url` | Network fetches | `"https://api.github.com/*"` |
| `dir` | Working directory | `"/projects/foo"` |

## Examples

### Allow Reads, Confirm Writes
```yaml
policy:
  - permission: allow
    rule: { read: "*" }
  - permission: confirm
    rule: { write: "*" }
```

### Block `rm`
```yaml
policy:
  - permission: deny
    rule: { command: "rm *" }
```

### Allow Writes Only for `.md` Files
```yaml
policy:
  - permission: allow
    rule: { write: "*.md" }
  - permission: deny
    rule: { write: "*" }
```

### Allow One API, Deny Others
```yaml
policy:
  - permission: allow
    rule: { url: "https://api.example.com/*" }
  - permission: deny
    rule: { url: "*" }
```

### Allow Writes Only in `/projects/foo`
```yaml
policy:
  - permission: allow
    rule:
      write: "*"
      dir: "/projects/foo"
  - permission: deny
    rule: { write: "*" }
```

## Confirmation Prompt
- **Accept**: Allow once.
- **Reject**: Deny once.
- **Accept and Remember**: Allow and add rule to `permissions.yaml`.

## Tool Mapping
| Tool Family | Operation Type |
|--------------|----------------|
| Read, FsSearch | `read` |
| Write, Patch, Remove | `write` |
| Shell | `command` |
| Fetch | `url` |

> **Note**: MCP tools and `SemSearch`, `Undo`, `Plan`, `Task` bypass this system.

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Restricted mode doesn’t restrict | Check `permissions.yaml` rules |
| Fallback surprises | Remember: no match → `confirm` |
| MCP tools unaffected | Use MCP’s own permission system |

## Next Steps
- [`.forge.toml` Reference](https://forgecode.dev/docs/forgecode-config/)