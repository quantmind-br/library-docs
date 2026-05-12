---
optimized: true
optimized_at: 2026-05-05T00:00:00Z
title: Troubleshooting
url: https://github.com/openagen/zeroclaw/blob/master/docs/ops/troubleshooting.md
source: git
fetched_at: 2026-05-02T14:51:51.634974408-03:00
rendered_js: false
word_count: 372
summary: This document provides troubleshooting steps for common installation, build, and runtime issues encountered when deploying the ZeroClaw software.
tags:
    - troubleshooting
    - installation
    - build-errors
    - zeroclaw
    - runtime-issues
    - rust-cargo
category: guide
---
# ZeroClaw Troubleshooting

Guide to common setup/runtime failures and fast resolution paths.

Last verified: **February 20, 2026**.

## Installation / Bootstrap

### `cargo` not found

Symptom: bootstrap exits with `cargo is not installed`

Fix:

```bash
./install.sh --install-rust
```

Or install from <https://rustup.rs/>.

### Missing system build dependencies

Symptom: build fails due to compiler or `pkg-config` issues

Fix:

```bash
./install.sh --install-system-deps
```

### Build fails on low-RAM / low-disk hosts

Symptoms: `cargo build --release` is killed (`signal: 9`, OOM killer, or `cannot allocate memory`)

Why: Runtime memory (<5MB) ≠ compile-time memory. Full source build needs **2 GB RAM + swap** and **6+ GB free disk**.

Preferred path for constrained machines:

```bash
./install.sh --prefer-prebuilt
```

Binary-only mode:

```bash
./install.sh --prebuilt-only
```

If compiling from source on constrained hosts:

1. Add swap only if enough free disk for swap + build output
2. Limit cargo parallelism:

```bash
CARGO_BUILD_JOBS=1 cargo build --release --locked
```

3. Reduce heavy features when Matrix not required:

```bash
cargo build --release --locked --features hardware
```

4. Cross-compile on stronger machine and copy binary

### Build is very slow or appears stuck

Symptoms: `cargo check` / `cargo build` appears stuck at `Checking zeroclaw`

Why: Matrix E2EE stack (`matrix-sdk`, `ruma`, `vodozemac`) is large and expensive to type-check. TLS + crypto native build scripts (`aws-lc-sys`, `ring`) add compile time.

Fast checks:

```bash
cargo check --timings
cargo tree -d
```

Timing report: `target/cargo-timings/cargo-timing.html`

Faster local iteration (Matrix not needed):

```bash
cargo check
```

Build with Matrix support:

```bash
cargo check --features channel-matrix
```

Lock-contention mitigation:

```bash
pgrep -af "cargo (check|build|test)|cargo check|cargo build|cargo test"
```

Stop unrelated cargo jobs before running build.

### `zeroclaw` command not found after install

Symptom: install succeeds but shell cannot find `zeroclaw`

Fix:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
which zeroclaw
```

Persist in shell profile if needed.

## Runtime / Gateway

### Gateway unreachable

Checks:

```bash
zeroclaw status
zeroclaw doctor
```

Verify `~/.zeroclaw/config.toml`:
- `[gateway].host` (default `127.0.0.1`)
- `[gateway].port` (default `42617`)
- `allow_public_bind` only when exposing LAN/public interfaces

### Pairing / auth failures on webhook

Checks:

1. Ensure pairing completed (`/pair` flow)
2. Ensure bearer token is current
3. Re-run diagnostics:

```bash
zeroclaw doctor
```

## Channel Issues

### Telegram conflict: `terminated by other getUpdates request`

Cause: multiple pollers using same bot token

Fix:
- Keep only one active runtime for that token
- Stop extra `zeroclaw daemon` / `zeroclaw channel start` processes

### Channel unhealthy in `channel doctor`

Checks:

```bash
zeroclaw channel doctor
```

Then verify channel-specific credentials + allowlist in config.

## Service Mode

### Service installed but not running

Checks:

```bash
zeroclaw service status
```

Recovery:

```bash
zeroclaw service stop
zeroclaw service start
```

Linux logs:

```bash
journalctl --user -u zeroclaw.service -f
```

## Installer URL

```bash
curl -fsSL https://raw.githubusercontent.com/zeroclaw-labs/zeroclaw/master/install.sh | bash
```

## Still Stuck?

Collect and include these outputs when filing an issue:

```bash
zeroclaw --version
zeroclaw status
zeroclaw doctor
zeroclaw channel doctor
```

Also include OS, install method, and sanitized config snippets (no secrets).
