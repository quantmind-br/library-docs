---
title: Nucleo setup
date: 2026-05-05T00:00:00Z
optimized: true
tags:
  - nucleo-f401re
  - zeroclaw
  - embedded-systems
  - gpio-control
  - firmware-flashing
  - rust-embedded
---

# ZeroClaw on Nucleo-F401RE — Hướng dẫn từng bước

Chạy ZeroClaw trên Mac hoặc Linux host. Kết nối Nucleo-F401RE qua USB. Điều khiển GPIO (LED, pins) qua Telegram hoặc CLI.

---

## Lấy thông tin board qua Telegram (không cần flash firmware)

ZeroClaw có thể đọc thông tin chip từ Nucleo qua USB **mà không cần flash bất kỳ firmware nào**. Nhắn bot Telegram:

- *"What board info do I have?"*
- *"Board info"*
- *"What hardware is connected?"*
- *"Chip info"*

Agent dùng tool `hardware_board_info` để trả về tên chip, kiến trúc, và memory map. Với feature `probe`, nó đọc dữ liệu live qua USB/SWD; nếu không, trả về thông tin datasheet tĩnh.

**Config:** Thêm Nucleo vào `config.toml` trước (để agent biết board nào để query):

```toml
[[peripherals.boards]]
board = "nucleo-f401re"
transport = "serial"
path = "/dev/ttyACM0"
baud = 115200
```

**Thay thế CLI:**

```bash
cargo build --features hardware,probe
zeroclaw hardware info
zeroclaw hardware discover
```

---

## Những gì đã bao gồm (không cần thay đổi code)

ZeroClaw bao gồm mọi thứ cho Nucleo-F401RE:

| Thành phần | Vị trí | Mục đích |
|---|---|---|
| Firmware | `firmware/nucleo/` | Embassy Rust — USART2 (115200), gpio_read, gpio_write |
| Peripheral serial | `src/peripherals/serial.rs` | Giao thức JSON-over-serial (giống Arduino/ESP32) |
| Lệnh flash | `zeroclaw peripheral flash-nucleo` | Build firmware, flash qua probe-rs |

Giao thức: newline-delimited JSON. Request: `{"id":"1","cmd":"gpio_write","args":{"pin":13,"value":1}}`. Response: `{"id":"1","ok":true,"result":"done"}`.

---

## Điều kiện tiên quyết

- Board Nucleo-F401RE
- Cáp USB (USB-A to Mini-USB; Nucleo có ST-Link tích hợp)
- Để flash: `cargo install probe-rs-tools --locked` (hoặc dùng [install script](https://probe.rs/docs/getting-started/installation/))

---

## Phase 1: Flash Firmware

### 1.1 Kết nối Nucleo

1. Kết nối Nucleo với Mac/Linux qua USB.
2. Board xuất hiện như device USB (ST-Link). Không cần driver riêng trên hệ thống hiện đại.

### 1.2 Flash qua ZeroClaw

Từ root repo zeroclaw:

```bash
zeroclaw peripheral flash-nucleo
```

Lệnh này build `firmware/nucleo` và chạy `probe-rs run --chip STM32F401RETx`. Firmware chạy ngay sau khi flash.

### 1.3 Flash thủ công (thay thế)

```bash
cd firmware/nucleo
cargo build --release --target thumbv7em-none-eabihf
probe-rs run --chip STM32F401RETx target/thumbv7em-none-eabihf/release/nucleo
```

---

## Phase 2: Tìm port serial

- **macOS:** `/dev/cu.usbmodem*` hoặc `/dev/tty.usbmodem*` (ví dụ `/dev/cu.usbmodem101`)
- **Linux:** `/dev/ttyACM0` (hoặc kiểm tra `dmesg` sau khi cắm vào)

USART2 (PA2/PA3) được bridge tới port COM ảo của ST-Link, nên host thấy một device serial.

---

## Phase 3: Cấu hình ZeroClaw

Thêm vào `~/.zeroclaw/config.toml`:

```toml
[peripherals]
enabled = true

[[peripherals.boards]]
board = "nucleo-f401re"
transport = "serial"
path = "/dev/cu.usbmodem101"   # điều chỉnh theo port của bạn
baud = 115200
```

---

## Phase 4: Chạy và test

```bash
zeroclaw daemon --host 127.0.0.1 --port 42617
```

Hoặc dùng agent trực tiếp:

```bash
zeroclaw agent --message "Turn on the LED on pin 13"
```

Pin 13 = PA5 = User LED (LD2) trên Nucleo-F401RE.

---

## Tóm tắt: Lệnh

| Bước | Lệnh |
|------|------|
| 1 | Kết nối Nucleo qua USB |
| 2 | `cargo install probe-rs-tools --locked` |
| 3 | `zeroclaw peripheral flash-nucleo` |
| 4 | Thêm Nucleo vào config.toml (path = port serial của bạn) |
| 5 | `zeroclaw daemon` hoặc `zeroclaw agent -m "Turn on LED"` |

---

## Troubleshooting

- **flash-nucleo unrecognized** — Build từ repo: `cargo run --features hardware -- peripheral flash-nucleo`. Subcommand chỉ có trong build repo, không trong cài đặt crates.io.
- **probe-rs not found** — `cargo install probe-rs-tools --locked` (crate `probe-rs` là thư viện; CLI trong `probe-rs-tools`)
- **No probe detected** — Đảm bảo Nucleo kết nối. Thử cable/port khác.
- **Serial port not found** — Trên Linux, add user vào `dialout`: `sudo usermod -a -G dialout $USER`, sau đó logout/login.
- **Lệnh GPIO bị bỏ qua** — Kiểm tra `path` trong config khớp port serial của bạn. Chạy `zeroclaw peripheral list` để xác minh. Kiểm tra `zeroclaw peripheral list` để xác minh.

---

## Tài liệu liên quan

- [[001-i18n-vi-getting-started-readme|README]] — Chỉ mục tài liệu.
- [[061-hardware-arduino-uno-q-setup|Arduino Uno Q setup]] — Hướng dẫn setup Arduino Uno Q.
- [[110-hardware-datasheets-nucleo-f401re|Nucleo F401RE datasheet]] — Tham khảo datasheet.
