---
title: Network deployment
date: 2026-05-05T00:00:00Z
optimized: true
tags:
  - zeroclaw
  - raspberry-pi
  - deployment
  - webhooks
  - network-configuration
  - openrc
  - daemon-service
---

# Network Deployment — ZeroClaw trên Raspberry Pi và mạng local

Hướng dẫn triển khai ZeroClaw trên Raspberry Pi hoặc host khác trong mạng local, với kênh Telegram và webhook tùy chọn.

---

## Tổng quan

| Mode | Port inbound cần? | Use case |
|------|-------------------|----------|
| **Telegram polling** | Không | ZeroClaw poll API Telegram; hoạt động từ bất kỳ đâu |
| **Matrix sync (bao gồm E2EE)** | Không | ZeroClaw sync qua Matrix client API; không cần webhook inbound |
| **Discord/Slack** | Không | Tương tự — chỉ outbound |
| **Nostr** | Không | Kết nối tới relays qua WebSocket; chỉ outbound |
| **Gateway webhook** | Có | POST /webhook, /whatsapp, /linq, /nextcloud-talk cần URL public |
| **Gateway pairing** | Có | Nếu bạn pair clients qua gateway |
| **Alpine/OpenRC service** | Không | Service background system-wide trên Alpine Linux |

**Trọng điểm:** Telegram, Discord, Slack, và Nostr dùng **kết nối outbound** — ZeroClaw kết nối tới servers/relays bên ngoài. Không cần port forwarding hoặc public IP.

---

## ZeroClaw trên Raspberry Pi

### Điều kiện tiên quyết

- Raspberry Pi (3/4/5) với Raspberry Pi OS
- Peripherals USB (Arduino, Nucleo) nếu dùng transport serial
- Tùy chọn: `rppal` cho GPIO native (`peripheral-rpi` feature)

### Cài đặt

```bash
# Build cho RPi (hoặc cross-compile từ host)
cargo build --release --features hardware

# Hoặc cài đặt theo phương pháp ưa thích của bạn
```

### Config

Chỉnh sửa `~/.zeroclaw/config.toml`:

```toml
[peripherals]
enabled = true

[[peripherals.boards]]
board = "rpi-gpio"
transport = "native"

# Hoặc Arduino qua USB
[[peripherals.boards]]
board = "arduino-uno"
transport = "serial"
path = "/dev/ttyACM0"
baud = 115200

[channels_config.telegram]
bot_token = "YOUR_BOT_TOKEN"
allowed_users = []

[gateway]
host = "127.0.0.1"
port = 42617
allow_public_bind = false
```

### Chạy daemon (chỉ local)

```bash
zeroclaw daemon --host 127.0.0.1 --port 42617
```

- Gateway bind tới `127.0.0.1` — không thể truy cập từ máy khác
- Kênh Telegram hoạt động: ZeroClaw poll API Telegram (outbound)
- Không cần firewall hoặc port forwarding

---

## Binding tới 0.0.0.0 (mạng local)

Để cho phép devices khác trong LAN của bạn truy cập gateway (ví dụ cho pairing hoặc webhooks):

### Tùy chọn A: Opt-in tường minh

```toml
[gateway]
host = "0.0.0.0"
port = 42617
allow_public_bind = true
```

```bash
zeroclaw daemon --host 0.0.0.0 --port 42617
```

**Bảo mật:** `allow_public_bind = true` exposes gateway tới mạng local của bạn. Chỉ dùng trên LAN tin cậy.

### Tùy chọn B: Tunnel (khuyến nghị cho webhooks)

Nếu bạn cần **URL public** (ví dụ WhatsApp webhook, clients external):

1. Chạy gateway trên localhost:
   ```bash
   zeroclaw daemon --host 127.0.0.1 --port 42617
   ```

2. Bắt đầu tunnel:
   ```toml
   [tunnel]
   provider = "tailscale"   # hoặc "ngrok", "cloudflare"
   ```
   Hoặc dùng `zeroclaw tunnel` (xem docs tunnel).

3. ZeroClaw sẽ từ chối `0.0.0.0` trừ khi `allow_public_bind = true` hoặc tunnel active.

---

## Telegram Polling (không port inbound)

Telegram dùng **long-polling** mặc định:

- ZeroClaw gọi `https://api.telegram.org/bot{token}/getUpdates`
- Không cần port inbound hoặc public IP
- Hoạt động sau NAT, trên RPi, trong phòng lab home

**Config:**

```toml
[channels_config.telegram]
bot_token = "YOUR_BOT_TOKEN"
allowed_users = []            # deny-by-default, bind identities tường minh
```

Chạy `zeroclaw daemon` — kênh Telegram khởi động tự động.

Để approve một tài khoản Telegram tại runtime:

```bash
zeroclaw channel bind-telegram <IDENTITY>
```

`<IDENTITY>` có thể là Telegram user ID numeric hoặc username (không có `@`).

### Quy tắc single poller (quan trọng)

Telegram Bot API `getUpdates` chỉ hỗ trợ một poller active per bot token.

- Giữ một instance runtime cho cùng token (khuyến nghị: service `zeroclaw daemon`).
- Không chạy `cargo run -- channel start` hoặc process bot khác cùng lúc.

Nếu gặp lỗi:

`Conflict: terminated by other getUpdates request`

bạn có conflict poller. Dừng instances extra và restart chỉ một daemon.

---

## Kênh webhook (WhatsApp, Nextcloud Talk, Custom)

Kênh dựa webhook cần **URL public** để Meta (WhatsApp) hoặc client của bạn có thể POST events.

### Tailscale Funnel

```toml
[tunnel]
provider = "tailscale"
```

Tailscale Funnel exposes gateway qua URL `*.ts.net`. Không cần port forwarding.

### ngrok

```toml
[tunnel]
provider = "ngrok"
```

Hoặc chạy ngrok thủ công:
```bash
ngrok http 42617
# Dùng URL HTTPS cho webhook của bạn
```

### Cloudflare Tunnel

Cấu hình Cloudflare Tunnel forward tới `127.0.0.1:42617`, sau đó set URL webhook của bạn tới hostname public của tunnel.

---

## Checklist: Triển khai RPi

- [ ] Build với `--features hardware` (và `peripheral-rpi` nếu dùng GPIO native)
- [ ] Cấu hình `[peripherals]` và `[channels_config.telegram]`
- [ ] Chạy `zeroclaw daemon --host 127.0.0.1 --port 42617` (Telegram hoạt động không cần 0.0.0.0)
- [ ] Cho truy cập LAN: `--host 0.0.0.0` + `allow_public_bind = true` trong config
- [ ] Cho webhooks: dùng Tailscale, ngrok, hoặc Cloudflare tunnel

---

## OpenRC (service Alpine Linux)

ZeroClaw hỗ trợ OpenRC cho Alpine Linux và distros khác dùng hệ thống init OpenRC. Services OpenRC chạy **system-wide** và yêu cầu root/sudo.

### Điều kiện tiên quyết

- Alpine Linux (hoặc distro OpenRC-based khác)
- Root hoặc sudo
- Một user system `zeroclaw` chuyên dụng (tạo trong install)

### Cài service

```bash
# Cài service (OpenRC auto-detect trên Alpine)
sudo zeroclaw service install
```

Tạo:
- Script init: `/etc/init.d/zeroclaw`
- Config directory: `/etc/zeroclaw/`
- Log directory: `/var/log/zeroclaw/`

### Cấu hình

Copy config thủ công thường không cần.

`sudo zeroclaw service install` tự động chuẩn bị `/etc/zeroclaw`, migrate trạng thái runtime hiện có từ setup user khi có sẵn, và set ownership/permissions cho user service `zeroclaw`.

Nếu không có trạng thái runtime trước để migrate, tạo `/etc/zeroclaw/config.toml` trước khi start service.

### Enable và start

```bash
# Thêm vào runlevel mặc định
sudo rc-update add zeroclaw default

# Start service
sudo rc-service zeroclaw start

# Check status
sudo rc-service zeroclaw status
```

### Quản lý service

| Command | Mô tả |
|---------|-------|
| `sudo rc-service zeroclaw start` | Start daemon |
| `sudo rc-service zeroclaw stop` | Stop daemon |
| `sudo rc-service zeroclaw status` | Check trạng thái service |
| `sudo rc-service zeroclaw restart` | Restart daemon |
| `sudo zeroclaw service status` | Wrapper status ZeroClaw (dùng config `/etc/zeroclaw`) |

### Logs

OpenRC routes logs tới:

| Log | Path |
|-----|------|
| Access/stdout | `/var/log/zeroclaw/access.log` |
| Errors/stderr | `/var/log/zeroclaw/error.log` |

Xem logs:

```bash
sudo tail -f /var/log/zeroclaw/error.log
```

### Uninstall

```bash
# Stop và remove khỏi runlevel
sudo rc-service zeroclaw stop
sudo rc-update del zeroclaw default

# Remove script init
sudo zeroclaw service uninstall
```

### Ghi chú

- OpenRC **chỉ system-wide** (không service user-level)
- Yêu cầu `sudo` hoặc root cho tất cả operations service
- Service chạy dưới user `zeroclaw:zeroclaw` (least privilege)
- Config phải tại `/etc/zeroclaw/config.toml` (path tường minh trong script init)
- Nếu user `zeroclaw` không tồn tại, install sẽ fail với instructions tạo nó

### Checklist: Triển khai Alpine/OpenRC

- [ ] Cài: `sudo zeroclaw service install`
- [ ] Enable: `sudo rc-update add zeroclaw default`
- [ ] Start: `sudo rc-service zeroclaw start`
- [ ] Verify: `sudo rc-service zeroclaw status`
- [ ] Check logs: `/var/log/zeroclaw/error.log`

---

## Tài liệu liên quan

- [[133-vi-channels-reference|channels-reference]] — Tổng quan cấu hình channel.
- [[073-security-matrix-e2ee-guide|matrix-e2ee-guide]] — Setup Matrix và troubleshooting encrypted-room.
- [[076-hardware-hardware-peripherals-design|hardware-peripherals-design]] — Thiết kế peripherals.
- [[146-contributing-adding-boards-and-tools|adding-boards-and-tools]] — Setup hardware và thêm boards.
