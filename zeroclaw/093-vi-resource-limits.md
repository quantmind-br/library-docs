---
title: Resource limits
authors:
  - ZeroClaw Team
tags:
  - resource-management
  - cgroups
  - rate-limiting
  - memory-monitoring
  - system-stability
  - process-control
  - performance-tuning
category: concept
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 560
---
# Giới hạn tài nguyên hệ thống

> ⚠️ **Status: Proposal / Roadmap**
>
> This document describes proposed approaches and may include placeholder commands or configurations.
> For current runtime behavior, see [[114-i18n-vi-config-reference|config-reference]], [[041-i18n-vi-operations-runbook|operations-runbook]], and [[143-vi-troubleshooting|troubleshooting]].

## Vấn đề cốt lõi

ZeroClaw has rate limiting (20 actions/hour) but lacks resource constraints. A faulty or malicious agent can:

- Exhaust available memory
- Spawn infinite CPU loops at 100% usage
- Fill disks with logs/output
- Create excessive subprocesses

> **Impact**: System instability, denial of service, data loss.

## Giải pháp đề xuất

### Option 1: cgroups v2 (Linux, recommended)

Automatically create a cgroup for ZeroClaw with hard limits.

**Systemd service configuration:**

```ini
[Service]
MemoryMax=512M
CPUQuota=50%
MemoryHigh=400M
MemoryLow=200M
TasksMax=100
Restart=on-failure
```

**CLI setup:**

```bash
# Create cgroup manually
sudo cgcreate -g memory,cpu:/zeroclaw

# Set limits
echo 536870912 > /sys/fs/cgroup/memory/zeroclaw/memory.max  # 512MB
echo 50000 > /sys/fs/cgroup/cpu/zeroclaw/cpu.cfs_quota_us    # 50% CPU
echo 100 > /sys/fs/cgroup/cpu/zeroclaw/cpu.cfs_period_us
```

> **Benefits**: OS-level isolation, automatic cleanup, works across all processes.

### Option 2: Deadlock detection with tokio::task

Prevent task starvation and infinite loops.

```rust
use tokio::time::{timeout, Duration};
use std::future::Future;

pub async fn execute_with_timeout<F, T>(
    fut: F,
    cpu_time_limit: Duration,
    memory_limit: usize,
) -> anyhow::Result<T>
where
    F: Future<Output = anyhow::Result<T>>,
{
    // CPU timeout
    match timeout(cpu_time_limit, fut).await {
        Ok(result) => result,
        Err(_) => {
            log::error!("Task exceeded CPU time limit: {:?}", cpu_time_limit);
            Err(anyhow::anyhow!("Task timeout exceeded"))
        }
    }
}
```

**Usage in agent loop:**

```rust
let result = execute_with_timeout(
    agent_loop(),
    Duration::from_secs(60),
    128 * 1024 * 1024, // 128MB
).await?;
```

### Option 3: Memory monitoring and enforcement

Track heap usage and terminate process if limit exceeded.

```rust
use std::alloc::{GlobalAlloc, Layout, System};
use std::sync::atomic::{AtomicUsize, Ordering};

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

// Usage
#[global_allocator]
static GLOBAL: LimitedAllocator<System> = LimitedAllocator {
    inner: System,
    max_bytes: 512 * 1024 * 1024, // 512MB
    used: AtomicUsize::new(0),
};
```

### Option 4: Process sandboxing with seccomp

Restrict system calls to prevent malicious actions.

```rust
use libseccomp::{ScmpFilterContext, ScmpSyscall};

fn create_seccomp_filter() -> anyhow::Result<ScmpFilterContext> {
    let mut filter = ScmpFilterContext::new_filter(libseccomp::ScmpAction::Allow)?;
    
    // Deny dangerous syscalls
    filter.add_rule(libseccomp::ScmpAction::Errno(libc::EPERM), 
                    ScmpSyscall::from_name("execve")?)?;
    filter.add_rule(libseccomp::ScmpAction::Errno(libc::EPERM), 
                    ScmpSyscall::from_name("execveat")?)?;
    
    Ok(filter)
}
```

## Cấu hình (config.toml)

```toml
[resources]
# Memory limits (in MB)
max_memory_mb = 512
max_memory_per_command_mb = 128

# CPU limits
max_cpu_percent = 50
max_cpu_time_seconds = 60

# Disk I/O limits
max_log_size_mb = 100
max_temp_storage_mb = 500

# Process limits
max_subprocesses = 10
max_open_files = 100
max_threads = 50

# Network limits
max_outgoing_connections = 20
max_incoming_connections = 10
```

## Implementation Roadmap

| Phase | Feature | Effort | Impact |
|-------|---------|--------|--------|
| **P0** | Memory monitoring + kill | Low | High |
| **P1** | CPU timeout per command | Low | High |
| **P2** | cgroups v2 integration (Linux) | Medium | Very High |
| **P3** | Disk I/O limits | Medium | Medium |
| **P4** | Process count limits | Low | High |
| **P5** | seccomp sandboxing | High | Very High |

### Phase P0: Memory Monitoring (Priority)

- [ ] Implement heap usage tracking
- [ ] Add memory limit enforcement
- [ ] Log warnings before killing
- [ ] Unit tests for memory allocation scenarios

### Phase P1: CPU Timeout

- [ ] Add tokio timeout wrapper for agent loop
- [ ] Implement per-command CPU limits
- [ ] Add metrics collection for CPU usage
- [ ] Graceful shutdown on timeout

### Phase P2: cgroups v2 Integration

- [ ] Detect cgroups v2 support
- [ ] Auto-create cgroup on startup
- [ ] Apply memory/CPU limits
- [ ] Cleanup on shutdown
- [ ] Fallback to manual cgroup setup

### Phase P3: Disk I/O Monitoring

- [ ] Track log file sizes
- [ ] Limit temporary storage growth
- [ ] Rotate logs when approaching limits
- [ ] Alert before reaching thresholds

### Phase P4: Process Limits

- [ ] Count running subprocesses
- [ ] Enforce max_subprocesses
- [ ] Limit open file descriptors
- [ ] Track thread count

### Phase P5: seccomp Sandboxing (Advanced)

- [ ] Define safe syscall whitelist
- [ ] Integrate with agent execution
- [ ] Test on multiple Linux distributions
- [ ] Document security guarantees

## Monitoring and Alerts

```toml
[observability.metrics]
resource_usage_enabled = true

[[observability.metrics.resources]]
name = "memory_usage_mb"
threshold_warning = 400
threshold_critical = 480

[[observability.metrics.resources]]
name = "cpu_usage_percent"
threshold_warning = 40
threshold_critical = 45
```

## Best Practices

- **Start conservative**: Use 512MB memory limit initially
- **Monitor first**: Enable metrics before applying strict limits
- **Test thoroughly**: Verify limits don't break legitimate workloads
- **Document**: Record actual usage patterns to tune limits
- **Fallback**: Always have graceful degradation paths

## Related Documents

- [[114-i18n-vi-config-reference|config-reference]] — Full configuration schema
- [[041-i18n-vi-operations-runbook|operations-runbook]] — Operational procedures
- [[143-vi-troubleshooting|troubleshooting]] — Troubleshooting guide
- [[092-vi-hardware-peripherals-design|hardware-peripherals-design]] — Hardware integration

## References

- [Linux cgroups v2 documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)
- [tokio timeout utilities](https://docs.rs/tokio/latest/tokio/time/fn.timeout.html)
- [seccomp documentation](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html)
- [Rust GlobalAlloc](https://doc.rust-lang.org/std/alloc/trait.GlobalAlloc.html)
