---
title: Security roadmap
url: https://github.com/openagen/zeroclaw/blob/master/docs/security/security-roadmap.md
source: git
fetched_at: 2026-05-02T14:52:11.785764876-03:00
rendered_js: false
word_count: 762
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - security-roadmap
  - os-sandboxing
  - system-hardening
  - resource-limits
  - audit-logging
  - containerization
category: concept
---
# ZeroClaw Security Improvement Roadmap

> [!warning] Status
> Proposal / Roadmap — implementation details may differ from current runtime behavior. For current behavior, see [[099-config-reference|config-reference]], [[098-operations-runbook|operations-runbook]], and [[097-troubleshooting|troubleshooting]].

## Bottom Line Up Front
ZeroClaw already has excellent application-layer security. This roadmap adds OS-level sandboxing, resource limits, and tamper-evident audit logging to reach production-grade security in 4-7 weeks of development time.

## Current State: Strong Foundation

ZeroClaw already has **excellent application-layer security**:

✅ Command allowlist (not blocklist)  
✅ Path traversal protection  
✅ Command injection blocking (`$(...)`, backticks, `&&`, `>`)  
✅ Secret isolation (API keys not leaked to shell)  
✅ Rate limiting (20 actions/hour)  
✅ Channel authorization (empty = deny all, `*` = allow all)  
✅ Risk classification (Low/Medium/High)  
✅ Environment variable sanitization  
✅ Forbidden paths blocking  
✅ Comprehensive test coverage (1,017 tests)

## What's Missing: OS-Level Containment

🔴 No OS-level sandboxing (chroot, containers, namespaces)  
🔴 No resource limits (CPU, memory, disk I/O caps)  
🔴 No tamper-evident audit logging  
🔴 No syscall filtering (seccomp)

## Comparison: ZeroClaw vs PicoClaw vs Production Grade

| Feature | PicoClaw | ZeroClaw Now | ZeroClaw + Roadmap | Production Target |
|---------|----------|--------------|-------------------|-------------------|
| **Binary Size** | ~8MB | **3.4MB** ✅ | 3.5-4MB | < 5MB |
| **RAM Usage** | < 10MB | **< 5MB** ✅ | < 10MB | < 20MB |
| **Startup Time** | < 1s | **< 10ms** ✅ | < 50ms | < 100ms |
| **Command Allowlist** | Unknown | ✅ Yes | ✅ Yes | ✅ Yes |
| **Path Blocking** | Unknown | ✅ Yes | ✅ Yes | ✅ Yes |
| **Injection Protection** | Unknown | ✅ Yes | ✅ Yes | ✅ Yes |
| **OS Sandbox** | No | ❌ No | ✅ Firejail/Landlock | ✅ Container/namespaces |
| **Resource Limits** | No | ❌ No | ✅ cgroups/Monitor | ✅ Full cgroups |
| **Audit Logging** | No | ❌ No | ✅ HMAC-signed | ✅ SIEM integration |
| **Security Score** | C | **B+** | **A-** | **A+** |

## Implementation Roadmap

### Phase 1: Quick Wins (1-2 weeks)
**Goal**: Address critical gaps with minimal complexity

| Task | File | Effort | Impact |
|------|------|--------|-------|
| Landlock filesystem sandbox | `src/security/landlock.rs` | 2 days | High |
| Memory monitoring + OOM kill | `src/resources/memory.rs` | 1 day | High |
| CPU timeout per command | `src/tools/shell.rs` | 1 day | High |
| Basic audit logging | `src/security/audit.rs` | 2 days | Medium |
| Config schema updates | `src/config/schema.rs` | 1 day | - |

**Deliverables**:
- Linux: Filesystem access restricted to workspace
- All platforms: Memory/CPU guards against runaway commands
- All platforms: Tamper-evident audit trail

---

### Phase 2: Platform Integration (2-3 weeks)
**Goal**: Deep OS integration for production-grade isolation

| Task | Effort | Impact |
|------|--------|-------|
| Firejail auto-detection + wrapping | 3 days | Very High |
| Bubblewrap wrapper for macOS/*nix | 4 days | Very High |
| cgroups v2 systemd integration | 3 days | High |
| seccomp syscall filtering | 5 days | High |
| Audit log query CLI | 2 days | Medium |

**Deliverables**:
- Linux: Full container-like isolation via Firejail
- macOS: Bubblewrap filesystem isolation
- Linux: cgroups resource enforcement
- Linux: Syscall allowlisting

---

### Phase 3: Production Hardening (1-2 weeks)
**Goal**: Enterprise security features

| Task | Effort | Impact |
|------|--------|-------|
| Docker sandbox mode option | 3 days | High |
| Certificate pinning for channels | 2 days | Medium |
| Signed config verification | 2 days | Medium |
| SIEM-compatible audit export | 2 days | Medium |
| Security self-test (`zeroclaw audit --check`) | 1 day | Low |

**Deliverables**:
- Optional Docker-based execution isolation
- HTTPS certificate pinning for channel webhooks
- Config file signature verification
- JSON/CSV audit export for external analysis

## New Config Schema Preview

```toml
[security]
level = "strict"  # relaxed | default | strict | paranoid

# Sandbox configuration
[security.sandbox]
enabled = true
backend = "auto"  # auto | firejail | bubblewrap | landlock | docker | none

# Resource limits
[resources]
max_memory_mb = 512
max_memory_per_command_mb = 128
max_cpu_percent = 50
max_cpu_time_seconds = 60
max_subprocesses = 10

# Audit logging
[security.audit]
enabled = true
log_path = "~/.config/zeroclaw/audit.log"
sign_events = true
max_size_mb = 100

# Autonomy (existing, enhanced)
[autonomy]
level = "supervised"  # readonly | supervised | full
allowed_commands = ["git", "ls", "cat", "grep", "find"]
forbidden_paths = ["/etc", "/root", "~/.ssh"]
require_approval_for_medium_risk = true
block_high_risk_commands = true
max_actions_per_hour = 20
```

## CLI Commands Preview

```bash
# Security status check
zeroclaw security --check
# → ✓ Sandbox: Firejail active
# → ✓ Audit logging enabled (42 events today)
# → → Resource limits: 512MB mem, 50% CPU

# Audit log queries
zeroclaw audit --user @alice --since 24h
zeroclaw audit --risk high --violations-only
zeroclaw audit --verify-signatures

# Sandbox test
zeroclaw sandbox --test
# → Testing isolation...
#   ✓ Cannot read /etc/passwd
#   ✓ Cannot access ~/.ssh
#   ✓ Can read /workspace
```

## Summary

**ZeroClaw is already more secure than PicoClaw** with:
- 50% smaller binary (3.4MB vs 8MB)
- 50% less RAM (< 5MB vs < 10MB)
- 100x faster startup (< 10ms vs < 1s)
- Comprehensive security policy engine
- Extensive test coverage

**By implementing this roadmap**, ZeroClaw becomes:
- Production-grade with OS-level sandboxing
- Resource-aware with memory/CPU guards
- Audit-ready with tamper-evident logging
- Enterprise-ready with configurable security levels

**Estimated effort**: 4-7 weeks for full implementation  
**Value**: Transforms ZeroClaw from "safe for testing" to "safe for production"

tags:
- security-roadmap
- os-sandboxing
- system-hardening
- resource-limits
- audit-logging
- containerization
