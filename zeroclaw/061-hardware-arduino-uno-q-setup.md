---
title: Arduino uno q setup
date: 2026-05-05T00:00:00Z
optimized: true
tags:
  - arduino-uno-q
  - zeroclaw
  - linux-deployment
  - gpio-control
  - telegram-bot
  - rust-installation
  - cross-compilation
---

# ZeroClaw on Arduino Uno Q — Hướng dẫn từng bước

Chạy ZeroClaw trên Linux side của Arduino Uno Q. Telegram hoạt động qua WiFi; điều khiển GPIO sử dụng Bridge (yêu cầu app App Lab tối thiểu).

---

## Những gì đã bao gồm (không cần thay đổi code)

ZeroClaw bao gồm mọi thứ cần thiết cho Arduino Uno Q. **Clone repo và làm theo hướng dẫn này — không cần patch hoặc code tùy chỉnh.**

| Thành phần | Vị trí | Mục đích |
|---|---|---|
| App Bridge | `firmware/uno-q-bridge/` | Sketch MCU + Python socket server (port 9999) cho GPIO |
| Công cụ Bridge | `src/peripherals/uno_q_bridge.rs` | Công cụ `gpio_read` / `gpio_write` giao tiếp với Bridge qua TCP |
| Lệnh setup | `src/peripherals/uno_q_setup.rs` | `zeroclaw peripheral setup-uno-q` triển khai Bridge qua scp + arduino-app-cli |
| Schema config | `board = "arduino-uno-q"`, `transport = "bridge"` | Hỗ trợ trong `config.toml` |

Build với `--features hardware` để bao gồm hỗ trợ Uno Q.

---

## Điều kiện tiên quyết

- Arduino Uno Q đã cấu hình WiFi
- Arduino App Lab cài trên Mac (cho setup ban đầu và triển khai)
- API key cho LLM (OpenRouter, v.v.)

---

## Phase 1: Setup Uno Q ban đầu (một lần)

### 1.1 Cấu hình Uno Q qua App Lab

1. Tải [Arduino App Lab](https://docs.arduino.cc/software/app-lab/) (AppImage trên Linux).
2. Kết nối Uno Q qua USB, bật nguồn.
3. Mở App Lab, kết nối với board.
4. Làm theo wizard setup:
   - Đặt username và password (cho SSH)
   - Cấu hình WiFi (SSID, password)
   - Áp dụng bất kỳ cập nhật firmware nào
5. Ghi chú địa chỉ IP hiển thị (ví dụ `arduino@192.168.1.42`) hoặc tìm sau qua `ip addr show` trong terminal App Lab.

### 1.2 Xác minh truy cập SSH

```bash
ssh arduino@<UNO_Q_IP>
# Nhập password bạn đã đặt
```

---

## Phase 2: Cài ZeroClaw trên Uno Q

### Tùy chọn A: Build trên thiết bị (đơn giản hơn, ~20–40 phút)

```bash
# SSH vào Uno Q
ssh arduino@<UNO_Q_IP>

# Cài Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source ~/.cargo/env

# Cài dependencies build (Debian)
sudo apt-get update
sudo apt-get install -y pkg-config libssl-dev

# Clone zeroclaw (hoặc scp project của bạn)
git clone https://github.com/zeroclaw-labs/zeroclaw.git
cd zeroclaw

# Build (mất ~15–30 phút trên Uno Q)
cargo build --release --features hardware

# Cài đặt
sudo cp target/release/zeroclaw /usr/local/bin/
```

### Tùy chọn B: Cross-compile trên Mac (nhanh hơn)

```bash
# Trên Mac — add target aarch64
hrustup target add aarch64-unknown-linux-gnu

# Cài cross-compiler (macOS; required cho linking)
brew tap messense/macos-cross-toolchains
brew install aarch64-unknown-linux-gnu

# Build
CC_aarch64_unknown_linux_gnu=aarch64-unknown-linux-gnu-gcc cargo build --release --target aarch64-unknown-linux-gnu --features hardware

# Copy sang Uno Q
scp target/aarch64-unknown-linux-gnu/release/zeroclaw arduino@<UNO_Q_IP>:~/
ssh arduino@<UNO_Q_IP> "sudo mv ~/zeroclaw /usr/local/bin/"
```

Nếu cross-compile thất bại, dùng Tùy chọn A và build trên thiết bị.

---

## Phase 3: Cấu hình ZeroClaw

### 3.1 Chạy onboard (hoặc tạo config thủ công)

```bash
ssh arduino@<UNO_Q_IP>

# Cấu hình nhanh
zeroclaw onboard --api-key YOUR_OPENROUTER_KEY --provider openrouter

# Hoặc tạo config thủ công
mkdir -p ~/.zeroclaw/workspace
nano ~/.zeroclaw/config.toml
```

### 3.2 config.toml tối thiểu

```toml
api_key = "YOUR_OPENROUTER_API_KEY"
default_provider = "openrouter"
default_model = "anthropic/claude-sonnet-4-6"

[peripherals]
enabled = false
# GPIO qua Bridge yêu cầu Phase 4

[channels_config.telegram]
bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
allowed_users = ["*"]

[gateway]
host = "127.0.0.1"
port = 42617
allow_public_bind = false

[agent]
compact_context = true
```

---

## Phase 4: Chạy ZeroClaw Daemon

```bash
ssh arduino@<UNO_Q_IP>

# Chạy daemon (Telegram polling hoạt động qua WiFi)
zeroclaw daemon --host 127.0.0.1 --port 42617
```

**Lúc này:** Telegram chat hoạt động. Gửi tin nhắn đến bot — ZeroClaw phản hồi. Chưa có GPIO.

---

## Phase 5: GPIO qua Bridge (ZeroClaw xử lý)

ZeroClaw bao gồm app Bridge và lệnh setup.

### 5.1 Triển khai app Bridge

**Từ Mac của bạn** (với repo zeroclaw):
```bash
zeroclaw peripheral setup-uno-q --host 192.168.0.48
```

**Từ Uno Q** (đã SSH vào):
```bash
zeroclaw peripheral setup-uno-q
```

Lệnh này copy app Bridge đến `~/ArduinoApps/uno-q-bridge` và khởi động nó.

### 5.2 Thêm vào config.toml

```toml
[peripherals]
enabled = true

[[peripherals.boards]]
board = "arduino-uno-q"
transport = "bridge"
```

### 5.3 Chạy ZeroClaw

```bash
zeroclaw daemon --host 127.0.0.1 --port 42617
```

Giờ khi bạn nhắn bot Telegram *"Bật đèn LED"* hoặc *"Set pin 13 high"*, ZeroClaw sử dụng `gpio_write` qua Bridge.

---

## Tóm tắt: Lệnh từ đầu đến cuối

| Bước | Lệnh |
|------|------|
| 1 | Cấu hình Uno Q trong App Lab (WiFi, SSH) |
| 2 | `ssh arduino@<IP>` |
| 3 | `curl -sSf https://sh.rustup.rs | sh -s -- -y && source ~/.cargo/env` |
| 4 | `sudo apt-get install -y pkg-config libssl-dev` |
| 5 | `git clone https://github.com/zeroclaw-labs/zeroclaw.git && cd zeroclaw` |
| 6 | `cargo build --release --features hardware` |
| 7 | `zeroclaw onboard --api-key KEY --provider openrouter` |
| 8 | Chỉnh sửa `~/.zeroclaw/config.toml` (thêm bot_token Telegram) |
| 9 | `zeroclaw daemon --host 127.0.0.1 --port 42617` |
| 10 | Nhắn bot Telegram — nó phản hồi |

---

## Troubleshooting

- **"command not found: zeroclaw"** — Dùng path đầy đủ: `/usr/local/bin/zeroclaw` hoặc đảm bảo `~/.cargo/bin` trong PATH.
- **Telegram không phản hồi** — Kiểm tra bot_token, allowed_users, và Uno Q có internet (WiFi).
- **Out of memory** — Giữ features tối thiểu (`--features hardware` cho Uno Q); cân nhắc `compact_context = true`.
- **Lệnh GPIO bị bỏ qua** — Đảm bảo app Bridge đang chạy (`zeroclaw peripheral setup-uno-q` triển khai và khởi động nó). Config phải có `board = "arduino-uno-q"` và `transport = "bridge"`.
- **Provider LLM (GLM/Zhipu)** — Dùng `default_provider = "glm"` hoặc `"zhipu"` với `GLM_API_KEY` trong env hoặc config. ZeroClaw dùng endpoint v4 chính xác.

---

## Tài liệu liên quan

- [[001-i18n-vi-getting-started-readme|README]] — Chỉ mục tài liệu.
- [[063-setup-guides-mattermost-setup|Mattermost setup]] — Hướng dẫn setup Mattermost.
- [[136-vi-datasheets-arduino-uno|Arduino Uno datasheet]] — Tham khảo datasheet.
