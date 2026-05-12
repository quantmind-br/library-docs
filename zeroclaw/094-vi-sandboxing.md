---
title: Sandboxing
authors:
  - ZeroClaw Team
tags:
  - sandboxing
  - zero-claw
  - system-security
  - linux-security
  - firejail
  - bubblewrap
  - landlock
  - containerization
  - process-isolation
category: concept
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 792
---
# Chiến lược sandboxing hệ thống

> ⚠️ **Status: Proposal / Roadmap**
>
> This document describes proposed approaches and may include placeholder commands or configurations.
> For current runtime behavior, see [[114-i18n-vi-config-reference|config-reference]], [[041-i18n-vi-operations-runbook|operations-runbook]], and [[143-vi-troubleshooting|troubleshooting]].

## Vấn đề bảo mật

ZeroClaw currently has **application-layer security** (allowlists, path blocking, command injection protection) but lacks **OS-level isolation**. If an attacker is within the allowlist, they can execute any allowed command with the privileges of the `zeroclaw` user.

> **Risk**: Privilege escalation, arbitrary code execution, system compromise.

## Giải pháp đề xuất

### Option 1: Firejail Integration (Recommended for Linux)

Firejail provides user-space sandboxing with minimal overhead and no root privileges required.

**Rust integration wrapper:**

```rust
// src/security/firejail.rs
use std::process::Command;

pub struct FirejailSandbox {
    enabled: bool,
}

impl FirejailSandbox {
    pub fn new() -> Self {
        let enabled = which::which("firejail").is_ok();
        Self { enabled }
    }

    pub fn wrap_command(&self, cmd: &mut Command) -> &mut Command {
        if !self.enabled {
            return cmd;
        }

        // Wrap any command with firejail sandboxing
        let mut jail = Command::new("firejail");
        jail.args([
            "--private=home",           // New home directory
            "--private-dev",            // Minimal /dev
            "--nosound",                // No audio
            "--no3d",                   // No 3D acceleration
            "--novideo",                // No video devices
            "--nowheel",                // No input devices
            "--notv",                   // No TV devices
            "--noprofile",              // Skip profile loading
            "--quiet",                  // Suppress warnings
            "--seccomp",                // Enable seccomp filtering
            "--caps.drop=all",          // Drop all capabilities
        ]);

        // Append original command
        if let Some(program) = cmd.get_program().to_str() {
            jail.arg(program);
        }
        for arg in cmd.get_args() {
            if let Some(s) = arg.to_str() {
                jail.arg(s);
            }
        }

        // Replace original command with firejail wrapper
        *cmd = jail;
        cmd
    }
}
```

**Configuration:**

```toml
[security]
enable_sandbox = true
sandbox_backend = "firejail"  # auto | firejail | bubblewrap | landlock | docker | none

[security.sandbox.firejail]
extra_args = ["--seccomp", "--caps.drop=all"]
```

**Firejail command examples:**

```bash
# Manual sandboxing
firejail --private --noprofile --seccomp --caps.drop=all zeroclaw agent

# With specific paths
firejail --private=/home/zeroclaw --read-only=/usr --net=none zeroclaw agent
```

> **Benefits**: 
> - No root required
> - Minimal performance overhead
> - Easy to deploy
> - Supports seccomp filtering
> - Drops Linux capabilities

### Option 2: Bubblewrap (Portable, No Root)

Bubblewrap uses Linux user namespaces to create lightweight containers. Ideal for systems without Firejail.

**Installation:**

```bash
sudo apt install bubblewrap
```

**Command wrapping:**

```bash
# Basic bubblewrap sandbox
bwrap --ro-bind /usr /usr \
      --dev /dev \
      --proc /proc \
      --bind /workspace /workspace \
      --unshare-all \
      --share-net \
      --die-with-parent \
      -- /bin/sh -c "command"
```

**Rust integration:**

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
    
    // Append original command
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

> **Benefits**:
> - No root privileges needed
> - Works on any Linux system
> - Lightweight
> - Supports user namespaces

### Option 3: Docker-in-Docker (Heavy but Complete Isolation)

Run agent tools in temporary containers for complete isolation.

**Rust integration:**

```rust
use std::path::Path;
use std::process::Command;

pub struct DockerSandbox {
    image: String,
    memory_limit: String,
    cpu_limit: String,
}

impl DockerSandbox {
    pub fn new() -> Self {
        Self {
            image: "alpine:latest".to_string(),
            memory_limit: "512m".to_string(),
            cpu_limit: "1.0".to_string(),
        }
    }

    pub async fn execute(&self, command: &str, workspace: &Path) -> anyhow::Result<String> {
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

**Configuration:**

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

> **Benefits**:
> - Complete process and filesystem isolation
> - Resource limits (CPU, memory)
> - Network isolation
> - Easy to audit container images

> **Drawbacks**:
> - Requires Docker daemon
> - Higher overhead
> - Slower startup

### Option 4: Landlock (Linux Kernel LSM, Rust Native)

Landlock provides filesystem access control without containers. Native Rust implementation.

**Installation:**

```bash
# Requires Linux 5.13+ and Landlock enabled
# Check: grep LANDLOCK /boot/config-$(uname -r)
```

**Rust implementation:**

```rust
use landlock::{Ruleset, AccessFS};
use std::path::Path;

pub fn apply_landlock() -> anyhow::Result<()> {
    let ruleset = Ruleset::new()
        .set_access_fs(
            AccessFS::read_file
                | AccessFS::write_file
                | AccessFS::execute_file
                | AccessFS::remove_file
                | AccessFS::read_dir
                | AccessFS::remove_dir,
        )
        .add_path(
            Path::new("/workspace"),
            AccessFS::read_file | AccessFS::write_file | AccessFS::execute_file,
        )?
        .add_path(
            Path::new("/tmp"),
            AccessFS::read_file | AccessFS::write_file,
        )?
        .add_path(
            Path::new("/usr"),
            AccessFS::read_file | AccessFS::execute_file,
        )?
        .restrict_self()?;

    log::info!("Landlock sandbox applied successfully");
    Ok(())
}
```

**Configuration:**

```toml
[security.sandbox]
enabled = true
backend = "landlock"

[security.sandbox.landlock]
readonly_paths = ["/usr", "/bin", "/lib", "/etc"]
readwrite_paths = ["$HOME/workspace", "/tmp/zeroclaw"]
execute_paths = ["/usr/bin", "/bin", "$HOME/workspace"]
```

> **Benefits**:
> - Kernel-level enforcement
> - No external dependencies
> - Minimal overhead
> - Fine-grained filesystem access control

> **Limitations**:
> - Linux-only (requires 5.13+)
> - Filesystem-focused (no network isolation)

## Implementation Priority

| Phase | Solution | Effort | Security Enhancement |
|-------|----------|--------|----------------------|
| **P0** | Landlock (Linux only, native) | Low | High (filesystem) |
| **P1** | Firejail integration | Low | Very High |
| **P2** | Bubblewrap wrapper | Medium | Very High |
| **P3** | Docker sandbox mode | High | Complete isolation |

### Phase P0: Landlock Integration (Priority)

- [ ] Verify Linux kernel version (5.13+)
- [ ] Implement Landlock ruleset builder
- [ ] Add configuration schema
- [ ] Test filesystem access restrictions
- [ ] Unit tests for path traversal prevention

### Phase P1: Firejail Integration

- [ ] Add Firejail detection
- [ ] Implement command wrapping
- [ ] Add configuration options
- [ ] Test with various commands
- [ ] Performance benchmarking

### Phase P2: Bubblewrap Wrapper

- [ ] Implement bubblewrap command builder
- [ ] Add configuration schema
- [ ] Test on systems without Firejail
- [ ] Document deployment
- [ ] Fallback mechanism

### Phase P3: Docker Sandbox Mode

- [ ] Implement Docker execution wrapper
- [ ] Add resource limits configuration
- [ ] Test network isolation
- [ ] Security audit of container images
- [ ] Performance optimization

## Configuration Schema

```toml
[security]
enable_sandbox = true
sandbox_backend = "auto"  # auto | firejail | bubblewrap | landlock | docker | none

# Firejail-specific
[security.sandbox.firejail]
extra_args = ["--seccomp", "--caps.drop=all"]
private_home = true
private_dev = true

# Landlock-specific
[security.sandbox.landlock]
readonly_paths = ["/usr", "/bin", "/lib", "/etc", "/usr/local"]
readwrite_paths = ["$HOME/workspace", "/tmp/zeroclaw", "/var/cache/zeroclaw"]
execute_paths = ["/usr/bin", "/bin", "$HOME/workspace"]

# Docker-specific
[security.sandbox.docker]
image = "alpine:latest"
memory_limit = "512m"
cpu_limit = "1.0"
cpu_quota = 50000
network_mode = "none"
volumes = ["/tmp:/tmp"]
```

## Security Guarantees

### Filesystem Isolation

| Backend | Read-only Paths | Write Paths | Execute Control |
|---------|----------------|-------------|-----------------|
| Firejail | Configurable | Configurable | Yes |
| Bubblewrap | Configurable | Configurable | Yes |
| Landlock | Configurable | Configurable | Configurable |
| Docker | Configurable | Configurable | Configurable |

### Process Isolation

| Backend | Capabilities | Seccomp | User Namespace | Network |
|---------|--------------|---------|----------------|---------|
| Firejail | Dropped | Yes | Yes | Configurable |
| Bubblewrap | Dropped | Optional | Yes | Configurable |
| Landlock | N/A | N/A | N/A | N/A |
| Docker | Configurable | Yes | Yes | Isolated |

### Attack Surface Reduction

- **Command injection**: Prevented by seccomp and capability dropping
- **Path traversal**: Blocked by filesystem restrictions
- **Privilege escalation**: Mitigated by dropped capabilities
- **Resource exhaustion**: Limited by cgroups (separate configuration)

## Testing Strategy

```rust
#[cfg(test)]
mod sandbox_tests {
    use super::*;

    #[test]
    fn test_firejail_wrapping() {
        let mut cmd = Command::new("ls");
        let sandbox = FirejailSandbox::new();
        let wrapped = sandbox.wrap_command(&mut cmd);
        
        let args: Vec<_> = wrapped.get_args().collect();
        assert!(args.iter().any(|a| a.to_string_lossy().contains("firejail")));
        assert!(args.iter().any(|a| a.to_string_lossy().contains("--private")));
    }

    #[test]
    fn test_landlock_restrictions() {
        let ruleset = build_landlock_ruleset().unwrap();
        
        // Verify critical paths are restricted
        assert!(ruleset.is_path_restricted("/etc/passwd"));
        assert!(!ruleset.is_path_restricted("/workspace"));
    }

    #[test]
    fn test_docker_network_isolation() {
        let config = DockerConfig {
            network_mode: "none".to_string(),
            ..Default::default()
        };
        
        assert_eq!(config.network_mode, "none");
    }
}
```

## Best Practices

- **Start with Landlock**: Lowest overhead, good filesystem protection
- **Deploy Firejail**: Best balance of security and compatibility
- **Use Docker for untrusted code**: Complete isolation for external tools
- **Monitor sandbox violations**: Log attempts to access restricted paths
- **Test thoroughly**: Verify sandbox doesn't break legitimate operations
- **Document exceptions**: Clearly document any allowed paths/exceptions

## Related Documents

- [[114-i18n-vi-config-reference|config-reference]] — Full configuration schema
- [[041-i18n-vi-operations-runbook|operations-runbook]] — Operational procedures
- [[143-vi-troubleshooting|troubleshooting]] — Troubleshooting guide
- [[093-vi-resource-limits|resource-limits]] — Resource management
- [[095-vi-security-roadmap|security-roadmap]] — Security roadmap

## References

- [Firejail documentation](https://firejail.wordpress.com/)
- [Bubblewrap documentation](https://github.com/containers/bubblewrap)
- [Landlock Linux Security Module](https://landlock.io/)
- [Docker security documentation](https://docs.docker.com/engine/security/)
- [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)
- [seccomp documentation](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html)
