---
title: Cargo slicer speedup
url: https://github.com/openagen/zeroclaw/blob/master/docs/contributing/cargo-slicer-speedup.md
source: git
fetched_at: 2026-05-02T14:50:33.759158287-03:00
rendered_js: false
word_count: 356
summary: This document explains how cargo-slicer accelerates Rust build times by identifying and stubbing unreachable code at the MIR level to reduce LLVM codegen overhead.
tags:
    - rust-language
    - build-optimization
    - cargo-slicer
    - compiler-performance
    - mir-analysis
    - compilation-tools
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Faster Builds with cargo-slicer

[cargo-slicer](https://github.com/nickel-org/cargo-slicer) is a `RUSTC_WRAPPER` that stubs unreachable library functions at the MIR level, skipping LLVM codegen for code the final binary never calls.

## Benchmark Results

| Environment | Mode | Baseline | With cargo-slicer | Wall-time savings |
|---|---|---|---|---|
| 48-core server | syn pre-analysis | 3m 52s | 3m 31s | **-9.1%** |
| 48-core server | MIR-precise | 3m 52s | 2m 49s | **-27.2%** |
| Raspberry Pi 4 | syn pre-analysis | 25m 03s | 17m 54s | **-28.6%** |

> All measurements are clean `cargo +nightly build --release`. MIR-precise mode reads actual compiler MIR to build a more accurate call graph, stubbing 1,060 mono items vs 799 with syn-based analysis.

## CI Integration

> **Purpose**: Accelerate release builds via cargo-slicer with fallback to standard build.

The workflow `.github/workflows/ci-build-fast.yml` (not yet implemented) runs an accelerated release build alongside the standard one.

- Triggers on Rust-code changes and workflow changes
- Does not gate merges
- Runs in parallel as a non-blocking check

**Strategy**:
- **Fast path**: Install `cargo-slicer` plus `rustc-driver` binaries and run MIR-precise sliced build
- **Fallback path**: If `rustc-driver` install fails (e.g., nightly `rustc` API drift), run plain `cargo +nightly build --release` instead of failing

> Keeps the check useful and green while preserving acceleration whenever toolchain is compatible.

## Local Usage

### One-time install

```bash
cargo install cargo-slicer
rustup component add rust-src rustc-dev llvm-tools-preview --toolchain nightly
cargo +nightly install cargo-slicer --profile release-rustc \
  --bin cargo-slicer-rustc --bin cargo_slicer_dispatch \
  --features rustc-driver
```

### Build with syn pre-analysis (from zeroclaw root)

```bash
cargo-slicer pre-analyze
CARGO_SLICER_VIRTUAL=1 CARGO_SLICER_CODEGEN_FILTER=1 \
  RUSTC_WRAPPER=$(which cargo_slicer_dispatch) \
  cargo +nightly build --release
```

### Build with MIR-precise analysis (more stubs, bigger savings)

> Step 1: generate .mir-cache (first build with MIR_PRECISE)

```bash
CARGO_SLICER_MIR_PRECISE=1 CARGO_SLICER_WORKSPACE_CRATES=zeroclaw,zeroclaw_robot_kit \
  CARGO_SLICER_VIRTUAL=1 CARGO_SLICER_CODEGEN_FILTER=1 \
  RUSTC_WRAPPER=$(which cargo_slicer_dispatch) \
  cargo +nightly build --release
```

> Step 2: subsequent builds automatically use .mir-cache

## How It Works

1. **Pre-analysis** scans workspace sources via `syn` to build a cross-crate call graph (~2 s)
2. **Cross-crate BFS** from `main()` identifies which public library functions are actually reachable
3. **MIR stubbing** replaces unreachable bodies with `Unreachable` terminators — the mono collector finds no callees and prunes entire codegen subtrees
4. **MIR-precise mode** (optional) reads actual compiler MIR from the binary crate's perspective, building a ground-truth call graph that identifies even more unreachable functions

> No source files are modified. The output binary is functionally identical.

#rust-language #build-optimization #cargo-slicer #compiler-performance #mir-analysis #compilation-tools
