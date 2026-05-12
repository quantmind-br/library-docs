---
title: Audit logging
url: https://github.com/openagen/zeroclaw/blob/master/docs/security/audit-logging.md
source: git
fetched_at: 2026-05-02T14:52:07.762162189-03:00
rendered_js: false
word_count: 312
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - audit-logging
  - security-compliance
  - tamper-evidence
  - log-rotation
  - system-administration
  - hmac-signing
category: concept
---
# Audit Logging for ZeroClaw

> [!warning] Status
> Proposal / Roadmap — implementation details may differ from current runtime behavior. For current behavior, see [[099-config-reference|config-reference]], [[098-operations-runbook|operations-runbook]], and [[097-troubleshooting|troubleshooting]].

## Bottom Line Up Front
ZeroClaw currently logs actions but lacks tamper-evident audit trails. Proposed solution: structured JSON events with HMAC signatures, log rotation, and CLI query capabilities for compliance and forensics.

## Problem
ZeroClaw logs actions but lacks tamper-evident audit trails for:
- Who executed what command
- When and from which channel
- What resources were accessed
- Whether security policies were triggered

## Proposed Audit Log Format

```json
{
  "timestamp": "2026-02-16T12:34:56Z",
  "event_id": "evt_1a2b3c4d",
  "event_type": "command_execution",
  "actor": {
    "channel": "telegram",
    "user_id": "123456789",
    "username": "@alice"
  },
  "action": {
    "command": "ls -la",
    "risk_level": "low",
    "approved": false,
    "allowed": true
  },
  "result": {
    "success": true,
    "exit_code": 0,
    "duration_ms": 15
  },
  "security": {
    "policy_violation": false,
    "rate_limit_remaining": 19
  },
  "signature": "SHA256:abc123..."  // HMAC for tamper evidence
}
```

## Implementation

```rust
// src/security/audit.rs
use serde::{Deserialize, Serialize};
use std::io::Write;
use std::path::PathBuf;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AuditEvent {
    pub timestamp: String,
    pub event_id: String,
    pub event_type: AuditEventType,
    pub actor: Actor,
    pub action: Action,
    pub result: ExecutionResult,
    pub security: SecurityContext,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum AuditEventType {
    CommandExecution,
    FileAccess,
    ConfigurationChange,
    AuthSuccess,
    AuthFailure,
    PolicyViolation,
}

pub struct AuditLogger {
    log_path: PathBuf,
    signing_key: Option<hmac::Hmac<sha2::Sha256>>,
}

impl AuditLogger {
    pub fn log(&self, event: &AuditEvent) -> anyhow::Result<()> {
        let mut line = serde_json::to_string(event)?;

        // Add HMAC signature if key configured
        if let Some(ref key) = self.signing_key {
            let signature = compute_hmac(key, line.as_bytes());
            line.push_str(&format!("\n\"signature\": \"{}\"", signature));
        }

        let mut file = std::fs::OpenOptions::new()
            .create(true)
            .append(true)
            .open(&self.log_path)?;

        writeln!(file, "{}", line)?;
        file.sync_all()?;  // Force flush for durability
        Ok(())
    }

    pub fn search(&self, filter: AuditFilter) -> Vec<AuditEvent> {
        // Search log file by filter criteria
        todo!()
    }
}
```

## Config Schema

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `enabled` | boolean | `true` | Enable audit logging |
| `log_path` | string | `~/.config/zeroclaw/audit.log` | Log file path |
| `max_size_mb` | integer | `100` | Maximum log size before rotation |
| `rotate` | string | `daily` | Rotation schedule: `daily`, `weekly`, or `size` |
| `sign_events` | boolean | `true` | Enable HMAC signing for tamper evidence |
| `signing_key_path` | string | `~/.config/zeroclaw/audit.key` | Path to HMAC signing key |
| `log_commands` | boolean | `true` | Log command executions |
| `log_file_access` | boolean | `true` | Log file access events |
| `log_auth_events` | boolean | `true` | Log authentication events |
| `log_policy_violations` | boolean | `true` | Log policy violations |

```toml
[security.audit]
enabled = true
log_path = "~/.config/zeroclaw/audit.log"
max_size_mb = 100
rotate = "daily"  # daily | weekly | size

# Tamper evidence
sign_events = true
signing_key_path = "~/.config/zeroclaw/audit.key"

# What to log
log_commands = true
log_file_access = true
log_auth_events = true
log_policy_violations = true
```

## Audit Query CLI

```bash
# Show all commands executed by @alice
zeroclaw audit --user @alice

# Show all high-risk commands
zeroclaw audit --risk high

# Show violations from last 24 hours
zeroclaw audit --since 24h --violations-only

# Export to JSON for analysis
zeroclaw audit --format json --output audit.json

# Verify log integrity
zeroclaw audit --verify-signatures
```

## Log Rotation

```rust
pub fn rotate_audit_log(log_path: &PathBuf, max_size: u64) -> anyhow::Result<()> {
    let metadata = std::fs::metadata(log_path)?;
    if metadata.len() < max_size {
        return Ok(());
    }

    // Rotate: audit.log -> audit.log.1 -> audit.log.2 -> ...
    let stem = log_path.file_stem().unwrap_or_default();
    let extension = log_path.extension().and_then(|s| s.to_str()).unwrap_or("log");

    for i in (1..10).rev() {
        let old_name = format!("{}.{}.{}", stem, i, extension);
        let new_name = format!("{}.{}.{}", stem, i + 1, extension);
        let _ = std::fs::rename(old_name, new_name);
    }

    let rotated = format!("{}.1.{}", stem, extension);
    std::fs::rename(log_path, &rotated)?;

    Ok(())
}
```

## Implementation Priority

| Phase | Feature | Effort | Security Value |
|-------|---------|--------|----------------|
| **P0** | Basic event logging | Low | Medium |
| **P1** | Query CLI | Medium | Medium |
| **P2** | HMAC signing | Medium | High |
| **P3** | Log rotation + archival | Low | Medium |

tags:
- audit-logging
- security-compliance
- tamper-evidence
- log-rotation
- system-administration
- hmac-signing
