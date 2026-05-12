---
title: Security roadmap
authors:
  - ZeroClaw Team
tags:
  - security-roadmap
  - sandboxing
  - resource-limits
  - audit-logging
  - system-hardening
  - zeroclaw
  - security-hardening
  - production-grade
category: concept
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 1348
---
# Lộ trình cải tiến bảo mật ZeroClaw

> ⚠️ **Status: Proposal / Roadmap**
>
> This document describes proposed approaches and may include placeholder commands or configurations.
> For current runtime behavior, see [[114-i18n-vi-config-reference|config-reference]], [[041-i18n-vi-operations-runbook|operations-runbook]], and [[143-vi-troubleshooting|troubleshooting]].

## Tóm tắt nhanh

ZeroClaw has **excellent application-layer security** but lacks **OS-level isolation**. This roadmap transforms ZeroClaw from "safe for testing" to "production-grade secure" through sandboxing, resource limits, and tamper-evident audit logging.

## Current Security State: Strong Foundation

ZeroClaw already has **outstanding application-layer security**:

✅ **Command allowlist** (not blocklist) — only explicitly permitted commands can run
✅ **Path traversal protection** — blocks `../` and absolute paths
✅ **Command injection prevention** — blocks `$(...)`, backticks, `&&`, `>`, pipes
✅ **Secret isolation** — API keys never leaked to shell
✅ **Rate limiting** — 20 actions/hour per user
✅ **Channel authorization** — empty = deny all, `*` = allow all
✅ **Risk classification** — Low/Medium/High risk commands
✅ **Environment sanitization** — cleans PATH and other sensitive variables
✅ **Forbidden paths** — blocks access to `/etc`, `/root`, `~/.ssh`
✅ **Comprehensive test coverage** — 1,017 tests

## The Gap: OS-Level Isolation

🔴 **Missing**: OS-level sandboxing (chroot, containers, namespaces)
🔴 **Missing**: Resource limits (CPU, memory, disk I/O)
🔴 **Missing**: Tamper-evident audit logging
🔴 **Missing**: Syscall filtering (seccomp)

> **Risk**: If an attacker bypasses application-layer controls, they gain full system access.

## Security Comparison: ZeroClaw vs PicoClaw vs Production Grade

| Feature | PicoClaw | Current ZeroClaw | ZeroClaw + Roadmap | Production Target |
|---------|----------|------------------|---------------------|-------------------|
| **Binary size** | ~8MB | **3.4MB** ✅ | 3.5-4MB | < 5MB |
| **RAM usage** | < 10MB | **< 5MB** ✅ | < 10MB | < 20MB |
| **Startup time** | < 1s | **< 10ms** ✅ | < 50ms | < 100ms |
| **Command allowlist** | Unknown | ✅ Implemented | ✅ Implemented | ✅ Implemented |
| **Path blocking** | Unknown | ✅ Implemented | ✅ Implemented | ✅ Implemented |
| **Injection protection** | Unknown | ✅ Implemented | ✅ Implemented | ✅ Implemented |
| **OS sandbox** | ❌ No | ❌ No | ✅ Firejail/Landlock | ✅ Containers/namespaces |
| **Resource limits** | ❌ No | ❌ No | ✅ cgroups/Monitoring | ✅ Full cgroups |
| **Audit logging** | ❌ No | ❌ No | ✅ HMAC-signed | ✅ SIEM integration |
| **Security score** | C | **B+** | **A-** | **A+** |

## Implementation Roadmap

### Phase 1: Quick Wins (1-2 weeks)
**Goal**: Address critical gaps with minimal complexity

| Task | Implementation File | Effort | Impact |
|------|---------------------|--------|--------|
| Landlock filesystem sandbox | `src/security/landlock.rs` | 2 days | High |
| Memory monitoring + OOM kill | `src/resources/memory.rs` | 1 day | High |
| CPU timeout per command | `src/tools/shell.rs` | 1 day | High |
| Basic audit logging | `src/security/audit.rs` | 2 days | Medium |
| Update config schema | `src/config/schema.rs` | 1 day | - |

**Deliverables**:
- Linux: Filesystem access restricted to workspace
- All platforms: Memory/CPU protection against infinite loops
- All platforms: Tamper-evident audit trail

### Phase 2: Platform Integration (2-3 weeks)
**Goal**: Deep OS integration for production-grade isolation

| Task | Effort | Impact |
|------|--------|--------|
| Auto-detect Firejail + command wrapping | 3 days | Very High |
| Bubblewrap wrapper for macOS/*nix | 4 days | Very High |
| Systemd cgroups v2 integration | 3 days | High |
| Syscall filtering with seccomp | 5 days | High |
| Audit log query CLI | 2 days | Medium |

**Deliverables**:
- Linux: Full container-like isolation via Firejail
- macOS: Filesystem isolation via Bubblewrap
- Linux: Resource limits via cgroups
- Linux: Syscall allowlisting

### Phase 3: Production Hardening (1-2 weeks)
**Goal**: Enterprise-grade security features

| Task | Effort | Impact |
|------|--------|--------|
| Docker sandbox mode | 3 days | High |
| Certificate pinning for channels | 2 days | Medium |
| Signed config verification | 2 days | Medium |
| SIEM-compatible audit export | 2 days | Medium |
| `zeroclaw audit --check` self-audit | 1 day | Low |

**Deliverables**:
- Optional Docker-based execution isolation
- HTTPS certificate pinning for webhook channels
- Signed configuration file verification
- JSON/CSV audit export for external analysis

## New Configuration Schema Preview

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

# Existing autonomy settings (enhanced)
[autonomy]
level = "supervised"  # readonly | supervised | full
allowed_commands = ["git", "ls", "cat", "grep", "find", "curl", "wget"]
forbidden_paths = ["/etc", "/root", "~/.ssh", "/proc", "/sys"]
require_approval_for_medium_risk = true
block_high_risk_commands = true
max_actions_per_hour = 20
```

## New CLI Commands Preview

```bash
# Security status check
zeroclaw security --check
# → ✓ Sandbox: Firejail active (Linux)
# → ✓ Audit logging enabled (42 events today)
# → ✓ Resource limits: 512MB memory, 50% CPU
# → ✓ Syscall filtering: seccomp active
# → → Configuration level: strict

# Query audit log
zeroclaw audit --user @alice --since 24h
zeroclaw audit --risk high --violations-only
zeroclaw audit --verify-signatures
zeroclaw audit --export json > audit-2024-05-05.json

# Sandbox testing
zeroclaw sandbox --test
# → Testing isolation...
#   ✓ Cannot read /etc/passwd
#   ✓ Cannot access ~/.ssh
#   ✓ Can read /workspace
#   ✓ Can execute allowed commands
#   ✓ Network access blocked in strict mode

# Security self-audit
zeroclaw audit --check
# → Checking security configuration...
#   ✓ Firejail installed and configured
#   ✓ Landlock rules applied
#   ✓ Memory limits configured
#   ✓ CPU timeout active
#   ✓ All security checks passed
```

## Detailed Phase Breakdown

### Phase 1: Quick Wins — Security Essentials

#### 1.1 Landlock Filesystem Sandbox (Linux 5.13+)

**Implementation**: `src/security/landlock.rs`

```rust
use landlock::{Ruleset, AccessFS};
use std::path::Path;

pub fn apply_landlock_sandbox() -> anyhow::Result<()> {
    let ruleset = Ruleset::new()
        .set_access_fs(
            AccessFS::read_file
                | AccessFS::write_file
                | AccessFS::execute_file
                | AccessFS::read_dir
                | AccessFS::remove_file,
        )
        .add_path(Path::new("/workspace"), 
                 AccessFS::all())
        .add_path(Path::new("/tmp"), 
                 AccessFS::read_file | AccessFS::write_file)
        .add_path(Path::new("/usr"), 
                 AccessFS::read_file | AccessFS::execute_file)
        .restrict_self()?;

    Ok(())
}
```

**Configuration**:

```toml
[security.sandbox]
enabled = true
backend = "landlock"

[security.sandbox.landlock]
readonly_paths = ["/usr", "/bin", "/lib", "/etc"]
readwrite_paths = ["/workspace", "/tmp/zeroclaw"]
execute_paths = ["/usr/bin", "/bin", "/workspace"]
```

**Benefits**:
- Kernel-level enforcement
- No external dependencies
- Minimal overhead (~1ms)
- Fine-grained filesystem control

#### 1.2 Memory Monitoring and OOM Kill

**Implementation**: `src/resources/memory.rs`

```rust
use std::sync::atomic::{AtomicUsize, Ordering};
use std::alloc::{GlobalAlloc, Layout, System};

struct LimitedAllocator<A> {
    inner: A,
    max_bytes: usize,
    used: AtomicUsize,
}

unsafe impl<A: GlobalAlloc> GlobalAlloc for LimitedAllocator<A> {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        let current = self.used.fetch_add(layout.size(), Ordering::Relaxed);
        if current + layout.size() > self.max_bytes {
            log::error!(
                "Memory limit exceeded: {} > {} bytes",
                current + layout.size(),
                self.max_bytes
            );
            std::process::abort();
        }
        self.inner.alloc(layout)
    }

    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        self.used.fetch_sub(layout.size(), Ordering::Relaxed);
        self.inner.dealloc(ptr, layout);
    }
}

#[global_allocator]
static GLOBAL: LimitedAllocator<System> = LimitedAllocator {
    inner: System,
    max_bytes: 512 * 1024 * 1024, // 512MB
    used: AtomicUsize::new(0),
};
```

**Configuration**:

```toml
[resources]
max_memory_mb = 512
max_memory_per_command_mb = 128
```

#### 1.3 CPU Timeout per Command

**Implementation**: `src/tools/shell.rs`

```rust
use tokio::time::{timeout, Duration};

pub async fn execute_with_timeout<F, T>(
    fut: F,
    timeout_duration: Duration,
) -> anyhow::Result<T>
where
    F: Future<Output = anyhow::Result<T>>,
{
    match timeout(timeout_duration, fut).await {
        Ok(result) => result,
        Err(_) => {
            log::error!(
                "Command exceeded CPU time limit: {:?}",
                timeout_duration
            );
            Err(anyhow::anyhow!("Command timeout exceeded"))
        }
    }
}
```

**Usage**:

```rust
let result = execute_with_timeout(
    run_agent_command(),
    Duration::from_secs(60),
).await?;
```

#### 1.4 Basic Audit Logging

**Implementation**: `src/security/audit.rs`

```rust
use chrono::Utc;
use hmac::{Hmac, Mac};
use sha2::Sha256;

pub struct AuditLogger {
    log_path: PathBuf,
    secret: String,
}

impl AuditLogger {
    pub fn log_event(&self, event: AuditEvent) -> anyhow::Result<()> {
        let serialized = serde_json::to_string(&event)?;
        let signature = self.generate_signature(&serialized);
        let log_entry = format!("{}|{}\n", serialized, signature);
        
        std::fs::create_dir_all(self.log_path.parent().unwrap())?;
        std::fs::write(&self.log_path, log_entry, OpenOptions::append(true))?;
        
        Ok(())
    }

    fn generate_signature(&self, data: &str) -> String {
        let mut hmac = Hmac::<Sha256>::new_from_slice(self.secret.as_bytes())
            .expect("HMAC can take key of any size");
        hmac.update(data.as_bytes());
        hex::encode(hmac.finalize().into_bytes())
    }
}

#[derive(serde::Serialize)]
struct AuditEvent {
    timestamp: i64,
    user: String,
    action: String,
    risk_level: String,
    command: String,
    success: bool,
    metadata: serde_json::Value,
}
```

**Configuration**:

```toml
[security.audit]
enabled = true
log_path = "~/.config/zeroclaw/audit.log"
sign_events = true
max_size_mb = 100
```

### Phase 2: Platform Integration — Production Hardening

#### 2.1 Auto-detect Firejail + Command Wrapping

**Implementation**: `src/security/firejail.rs`

```rust
use std::process::Command;

pub struct FirejailSandbox {
    enabled: bool,
}

impl FirejailSandbox {
    pub fn new() -> Self {
        Self {
            enabled: which::which("firejail").is_ok(),
        }
    }

    pub fn wrap_command(&self, cmd: &mut Command) -> &mut Command {
        if !self.enabled {
            return cmd;
        }

        let mut jail = Command::new("firejail");
        jail.args([
            "--private=home",
            "--private-dev",
            "--nosound",
            "--no3d",
            "--novideo",
            "--nowheel",
            "--notv",
            "--noprofile",
            "--quiet",
            "--seccomp",
            "--caps.drop=all",
        ]);

        if let Some(program) = cmd.get_program().to_str() {
            jail.arg(program);
        }
        for arg in cmd.get_args() {
            if let Some(s) = arg.to_str() {
                jail.arg(s);
            }
        }

        *cmd = jail;
        cmd
    }
}
```

#### 2.2 Bubblewrap Wrapper for macOS/*nix

**Implementation**: `src/security/bubblewrap.rs`

```rust
use std::process::Command;

pub fn wrap_with_bubblewrap(cmd: &mut Command) -> &mut Command {
    let mut bwrap = Command::new("bwrap");
    
    bwrap.args([
        "--ro-bind", "/usr", "/usr",
        "--dev", "/dev",
        "--proc", "/proc",
        "--bind", "/workspace", "/workspace",
        "--unshare-all",
        "--share-net",
        "--die-with-parent",
    ]);
    
    if let Some(program) = cmd.get_program().to_str() {
        bwrap.arg(program);
    }
    for arg in cmd.get_args() {
        if let Some(s) = arg.to_str() {
            bwrap.arg(s);
        }
    }
    
    *cmd = bwrap;
    cmd
}
```

#### 2.3 Systemd cgroups v2 Integration

**Systemd service configuration**:

```ini
[Service]
MemoryMax=512M
MemoryHigh=400M
CPUQuota=50%
TasksMax=100
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6
NoNewPrivileges=true
PrivateTmp=true
PrivateDevices=true
ProtectSystem=strict
ProtectHome=read-only
```

**Implementation**: `src/resources/cgroups.rs`

```rust
use std::path::PathBuf;

pub struct CgroupManager {
    cgroup_path: PathBuf,
}

impl CgroupManager {
    pub fn new() -> Self {
        let path = PathBuf::from("/sys/fs/cgroup/zeroclaw");
        std::fs::create_dir_all(&path).ok();
        Self { cgroup_path: path }
    }

    pub fn apply_limits(&self) -> anyhow::Result<()> {
        // Memory limits
        std::fs::write(
            self.cgroup_path.join("memory.max"),
            "536870912" // 512MB
        )?;
        
        // CPU limits
        std::fs::write(
            self.cgroup_path.join("cpu.max"),
            "50000 100000" // 50% CPU
        )?;
        
        Ok(())
    }
}
```

#### 2.4 Syscall Filtering with seccomp

**Implementation**: `src/security/seccomp.rs`

```rust
use libseccomp::{ScmpFilterContext, ScmpSyscall};

pub fn create_seccomp_filter() -> anyhow::Result<ScmpFilterContext> {
    let mut filter = ScmpFilterContext::new_filter(libseccomp::ScmpAction::Allow)?;
    
    // Deny dangerous syscalls
    filter.add_rule(
        libseccomp::ScmpAction::Errno(libc::EPERM),
        ScmpSyscall::from_name("execve")?
    )?;
    filter.add_rule(
        libseccomp::ScmpAction::Errno(libc::EPERM),
        ScmpSyscall::from_name("execveat")?
    )?;
    filter.add_rule(
        libseccomp::ScmpAction::Errno(libc::EPERM),
        ScmpSyscall::from_name("mount")?
    )?;
    filter.add_rule(
        libseccomp::ScmpAction::Errno(libc::EPERM),
        ScmpSyscall::from_name("umount")?
    )?;
    
    Ok(filter)
}
```

### Phase 3: Production Hardening — Enterprise Features

#### 3.1 Docker Sandbox Mode

**Implementation**: `src/security/docker.rs`

```rust
use std::path::Path;
use std::process::Command;

pub struct DockerSandbox {
    image: String,
    memory_limit: String,
    cpu_limit: String,
}

impl DockerSandbox {
    pub async fn execute(
        &self,
        command: &str,
        workspace: &Path,
    ) -> anyhow::Result<String> {
        let output = Command::new("docker")
            .args([
                "run", "--rm",
                "--memory", &self.memory_limit,
                "--cpus", &self.cpu_limit,
                "--network", "none",
                "--volume", &format!("{}:/workspace", workspace.display()),
                &self.image,
                "sh", "-c", command,
            ])
            .output()
            .await?;

        if !output.status.success() {
            let stderr = String::from_utf8_lossy(&output.stderr);
            return Err(anyhow::anyhow!("Docker execution failed: {}", stderr));
        }

        Ok(String::from_utf8_lossy(&output.stdout).to_string())
    }
}
```

**Configuration**:

```toml
[security.sandbox]
enabled = true
backend = "docker"

[security.sandbox.docker]
image = "alpine:latest"
memory_limit = "512m"
cpu_limit = "1.0"
network_mode = "none"
```

#### 3.2 Certificate Pinning for Channels

**Implementation**: `src/channels/webhook.rs`

```rust
use reqwest::Certificate;
use std::collections::HashMap;

pub struct CertificatePinning {
    pinned_certs: HashMap<String, Vec<u8>>,
}

impl CertificatePinning {
    pub async fn verify_channel(
        &self,
        url: &str,
    ) -> anyhow::Result<()> {
        let certs = self.fetch_certificates(url).await?;
        
        for (domain, cert_der) in &self.pinned_certs {
            if url.contains(domain) {
                if !certs.contains(cert_der) {
                    return Err(anyhow::anyhow!(
                        "Certificate pinning failed for {}",
                        domain
                    ));
                }
            }
        }
        
        Ok(())
    }

    async fn fetch_certificates(&self, url: &str) -> anyhow::Result<Vec<Vec<u8>>> {
        // Implementation to fetch and parse certificates
        Ok(vec![])
    }
}
```

## Security Self-Check CLI

```bash
$ zeroclaw security --check

✓ Application-layer security: PASSED
  - Command allowlist: 42/42 rules active
  - Path blocking: All forbidden paths blocked
  - Injection protection: Regex patterns active
  - Secret isolation: Environment sanitized

✓ OS-level isolation: PASSED (Linux)
  - Firejail: Installed and active
  - Landlock: Rules applied
  - cgroups: Memory/CPU limits active
  - seccomp: Syscall filtering active

✓ Resource limits: PASSED
  - Memory: 512MB limit active
  - CPU: 50% quota active
  - Disk: 100MB log limit active

✓ Audit logging: PASSED
  - HMAC signing: Active
  - Log rotation: Configured
  - Query interface: Available

✓ Configuration integrity: PASSED
  - Config file: Valid and signed
  - Secrets: Encrypted at rest
  - Policy: Low/Medium/High risk classification active

Security score: A- (92/100)
Next recommended action: Enable certificate pinning for production channels
```

## Effort Estimation and Timeline

| Phase | Duration | Effort (person-days) | Team Size | Total Calendar Weeks |
|-------|----------|---------------------|-----------|---------------------|
| Phase 1: Quick Wins | 2 weeks | 10 days | 1-2 | 2 |
| Phase 2: Platform Integration | 3 weeks | 20 days | 2 | 3 |
| Phase 3: Production Hardening | 2 weeks | 10 days | 1-2 | 2 |
| **Total** | **7 weeks** | **40 days** | **1-2** | **7** |

**Team composition**:
- 1 Security Engineer (50%)
- 1 Rust Engineer (50%)
- 1 DevOps Engineer (25%)

## Success Metrics

### Security Metrics
- **Sandbox coverage**: 100% of command execution paths
- **Resource limit violations**: < 0.1% of commands
- **Audit log completeness**: 100% of security events logged
- **Tamper detection**: 100% of logs verifiable

### Performance Metrics
- **Startup overhead**: < 50ms added
- **Memory overhead**: < 10MB per sandbox
- **CPU overhead**: < 5% in normal operation
- **Compatibility**: 99% of existing workflows unaffected

### Compliance Metrics
- **SIEM integration**: JSON export compatible with Splunk, ELK, Datadog
- **Audit trail**: Tamper-evident with HMAC signatures
- **Configuration verification**: SHA-256 hashes for config files

## Risk Mitigation

### Technical Risks
| Risk | Mitigation | Contingency |
|------|------------|-------------|
| Firejail not available | Fallback to Bubblewrap/Landlock | Use auto-detection |
| cgroups v2 not available | Use cgroups v1 or manual limits | Graceful degradation |
| Landlock not available | Use Firejail/Bubblewrap | Platform-specific fallback |
| Performance degradation | Benchmark and optimize | Disable non-critical features |

### Operational Risks
| Risk | Mitigation | Contingency |
|------|------------|-------------|
| False positives in sandboxing | Gradual rollout with monitoring | Disable sandbox temporarily |
| Resource limits too restrictive | Configurable thresholds | Increase limits via config |
| Audit log performance impact | Log rotation and compression | Disable signing if needed |
| Configuration complexity | Sensible defaults | Provide migration tools |

## Related Documents

- [[092-vi-hardware-peripherals-design|hardware-peripherals-design]] — Hardware integration and security
- [[093-vi-resource-limits|resource-limits]] — Resource management and limits
- [[094-vi-sandboxing|sandboxing]] — Sandboxing strategies and implementation
- [[105-vi-actions-source-policy|actions-source-policy]] — GitHub Actions security
- [[085-security-audit-logging|audit-logging]] — Audit logging design
- [[084-security-agnostic-security|agnostic-security]] — Platform-agnostic security

## References

- [Landlock Linux Security Module](https://landlock.io/)
- [Firejail documentation](https://firejail.wordpress.com/)
- [Bubblewrap documentation](https://github.com/containers/bubblewrap)
- [systemd cgroups v2](https://www.freedesktop.org/software/systemd/man/systemd.resource-control.html)
- [seccomp documentation](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html)
- [Docker security](https://docs.docker.com/engine/security/)
- [HMAC specification](https://datatracker.ietf.org/doc/html/rfc2104)

## Summary

**ZeroClaw is already more secure than PicoClaw** with:
- **50% smaller binary** (3.4MB vs 8MB)
- **50% less RAM usage** (< 5MB vs < 10MB)
- **100x faster startup** (< 10ms vs < 1s)
- **Comprehensive policy engine**
- **Extensive test coverage** (1,017 tests)

**With this roadmap**, ZeroClaw becomes:
- **Production-grade** with OS-level sandboxing
- **Resource-aware** with memory/CPU protection
- **Audit-ready** with tamper-evident logging
- **Enterprise-ready** with configurable security levels

**Estimated effort**: 40 person-days (7 calendar weeks)
**Value delivered**: Transform ZeroClaw from "safe for testing" to "safe for production"
