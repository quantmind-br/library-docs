---
title: One click bootstrap
date: 2026-05-05T00:00:00Z
optimized: true
tags:
  - installation-guide
  - zeroclaw
  - bootstrap
  - deployment
  - cli-setup
  - docker-containers
---

# One-Click Bootstrap

Định nghĩa đường dẫn cài đặt và khởi tạo ZeroClaw nhanh nhất được hỗ trợ.

Đã xác minh lần cuối: **20 tháng 2, 2026**.

---

## Tùy chọn 0: Homebrew (macOS/Linuxbrew)

```bash
brew install zeroclaw
```

---

## Tùy chọn A (Khuyến nghị): Clone + script local

```bash
git clone https://github.com/zeroclaw-labs/zeroclaw.git
cd zeroclaw
./install.sh
```

Mặc định thực hiện:

1. `cargo build --release --locked`
2. `cargo install --path . --force --locked`

### Flow resource preflight và pre-built

Build từ source thường yêu cầu:

- **RAM + swap tối thiểu 2 GB**
- **Ổ đĩa trống 6 GB**

Khi tài nguyên hạn chế, bootstrap cố gắng tải binary pre-built trước.

```bash
./install.sh --prefer-prebuilt
```

Yêu cầu cài đặt binary-only và thất bại nếu không có asset release tương thích:

```bash
./install.sh --prebuilt-only
```

Bỏ qua flow pre-built và buộc build từ source:

```bash
./install.sh --force-source-build
```

---

## Dual-mode bootstrap

Hành vi mặc định là **app-only** (build/install ZeroClaw) và yêu cầu toolchain Rust đã có sẵn.

Cho máy mới, kích hoạt bootstrap môi trường tường minh:

```bash
./install.sh --install-system-deps --install-rust
```

Ghi chú:

- `--install-system-deps` cài dependencies build hệ thống (có thể yêu cầu `sudo`).
- `--install-rust` cài Rust qua `rustup` khi thiếu.
- `--prefer-prebuilt` thử download binary release trước, sau đó fallback sang build từ source.
- `--prebuilt-only` vô hiệu hóa fallback từ source.
- `--force-source-build` vô hiệu hóa flow pre-built hoàn toàn.

---

## Tùy chọn B: One-liner remote

```bash
curl -fsSL https://raw.githubusercontent.com/zeroclaw-labs/zeroclaw/master/install.sh | bash
```

Cho môi trường bảo mật cao, dùng Tùy chọn A để bạn có thể xem script trước khi thực thi.

Nếu chạy Tùy chọn B ngoài checkout repo, script install tự động clone workspace tạm thời, build, cài đặt, sau đó dọn dẹp.

---

## Các mode onboarding tùy chọn

### Onboarding container hóa (Docker)

```bash
./install.sh --docker
```

Build image ZeroClaw local và khởi động onboarding bên trong container trong khi persist config/workspace vào `./.zeroclaw-docker`.

CLI container mặc định là `docker`. Nếu Docker CLI không có sẵn và `podman` tồn tại, installer tự động fallback sang `podman`. Bạn cũng có thể set `ZEROCLAW_CONTAINER_CLI` tường minh (ví dụ: `ZEROCLAW_CONTAINER_CLI=podman ./install.sh --docker`).

Cho Podman, installer chạy với `--userns keep-id` và gắn nhãn volume `:Z` để mounts config/workspace vẫn writable bên trong container.

Nếu thêm `--skip-build`, installer bỏ qua build image local. Nó thử tag Docker local trước (`ZEROCLAW_DOCKER_IMAGE`, mặc định: `zeroclaw-bootstrap:local`); nếu thiếu, pull `ghcr.io/zeroclaw-labs/zeroclaw:latest` và tag local trước khi chạy.

### Onboarding nhanh (non-interactive)

```bash
./install.sh --onboard --api-key "sk-..." --provider openrouter
```

Hoặc với environment variables:

```bash
ZEROCLAW_API_KEY="sk-..." ZEROCLAW_PROVIDER="openrouter" ./install.sh --onboard
```

### Onboarding tương tác

```bash
./install.sh --interactive-onboard
```

---

## Flags hữu ích

- `--install-system-deps`
- `--install-rust`
- `--skip-build` (trong mode `--docker`: dùng image local nếu có, nếu không pull `ghcr.io/zeroclaw-labs/zeroclaw:latest`)
- `--skip-install`
- `--provider <id>`

Xem tất cả options:

```bash
./install.sh --help
```

---

## Tài liệu liên quan

- [[002-setup-guides-readme|README]] — Chỉ mục tài liệu.
- [[126-reference-cli-commands-reference|commands-reference]] — Tham khảo CLI.
- [[125-reference-api-providers-reference|providers-reference]] — Tham khảo providers.
- [[133-vi-channels-reference|channels-reference]] — Tham khảo channels.
