---
title: Tham khảo lệnh ZeroClaw
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/commands-reference.md
source: git
fetched_at: 2026-05-02T14:52:28.724698247-03:00
rendered_js: false
word_count: 711
summary: Tài liệu cung cấp hướng dẫn tham khảo toàn diện về các lệnh CLI của ZeroClaw, bao gồm quản lý tác vụ, cấu hình hệ thống, tích hợp dịch vụ và điều khiển phần cứng.
tags:
    - zeroclaw
    - cli-reference
    - command-line
    - system-management
    - integration-tools
    - development-tools
    - vi-docs
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tham khảo lệnh ZeroClaw

Dựa trên CLI hiện tại (`zeroclaw --help`).

Xác minh lần cuối: **2026-02-20**

## Lệnh cấp cao nhất

| Lệnh | Mục đích |
|---|---|
| `onboard` | Khởi tạo workspace/config nhanh hoặc tương tác |
| `agent` | Chạy chat tương tác hoặc chế độ gửi tin nhắn đơn |
| `gateway` | Khởi động gateway webhook và HTTP WhatsApp |
| `daemon` | Khởi động runtime có giám sát (gateway + channels + heartbeat/scheduler) |
| `service` | Quản lý vòng đời dịch vụ cấp hệ điều hành |
| `doctor` | Chạy chẩn đoán và kiểm tra trạng thái |
| `status` | Hiển thị cấu hình và tóm tắt hệ thống |
| `cron` | Quản lý tác vụ định kỳ |
| `models` | Làm mới danh mục model của provider |
| `providers` | Liệt kê ID provider, bí danh và provider đang dùng |
| `channel` | Quản lý kênh và kiểm tra sức khỏe kênh |
| `integrations` | Kiểm tra chi tiết tích hợp |
| `skills` | Liệt kê/cài đặt/gỡ bỏ skills |
| `migrate` | Nhập dữ liệu từ runtime khác (hỗ trợ OpenClaw) |
| `config` | Xuất schema cấu hình dạng máy đọc được |
| `completions` | Tạo script tự hoàn thành cho shell ra stdout |
| `hardware` | Phát hiện và kiểm tra phần cứng USB |
| `peripheral` | Cấu hình và nạp firmware thiết bị ngoại vi |

---

## Nhóm lệnh

### `onboard`

- `zeroclaw onboard`
- `zeroclaw onboard --interactive`
- `zeroclaw onboard --channels-only`
- `zeroclaw onboard --api-key <KEY> --provider <ID> --memory <sqlite|lucid|markdown|none>`
- `zeroclaw onboard --api-key <KEY> --provider <ID> --model <MODEL_ID> --memory <sqlite|lucid|markdown|none>`

### `agent`

- `zeroclaw agent`
- `zeroclaw agent -m "Hello"`
- `zeroclaw agent --provider <ID> --model <MODEL> --temperature <0.0-2.0>`
- `zeroclaw agent --peripheral <board:path>`

### `gateway` / `daemon`

- `zeroclaw gateway [--host <HOST>] [--port <PORT>]`
- `zeroclaw daemon [--host <HOST>] [--port <PORT>]`

### `service`

- `zeroclaw service install`
- `zeroclaw service start`
- `zeroclaw service stop`
- `zeroclaw service restart`
- `zeroclaw service status`
- `zeroclaw service uninstall`

### `cron`

- `zeroclaw cron list`
- `zeroclaw cron add <expr> [--tz <IANA_TZ>] <command>`
- `zeroclaw cron add-at <rfc3339_timestamp> <command>`
- `zeroclaw cron add-every <every_ms> <command>`
- `zeroclaw cron once <delay> <command>`
- `zeroclaw cron remove <id>`
- `zeroclaw cron pause <id>`
- `zeroclaw cron resume <id>`

### `models`

- `zeroclaw models refresh`
- `zeroclaw models refresh --provider <ID>`
- `zeroclaw models refresh --force`

> [!note] Hỗ trợ providers
> `openrouter`, `openai`, `anthropic`, `groq`, `mistral`, `deepseek`, `xai`, `together-ai`, `gemini`, `ollama`, `astrai`, `venice`, `fireworks`, `cohere`, `moonshot`, `glm`, `zai`, `qwen`, `nvidia`

### `channel`

- `zeroclaw channel list`
- `zeroclaw channel start`
- `zeroclaw channel doctor`
- `zeroclaw channel bind-telegram <IDENTITY>`
- `zeroclaw channel add <type> <json>`
- `zeroclaw channel remove <name>`

> [!note] Lệnh chat runtime (Telegram/Discord)
> - `/models`
> - `/models <provider>`
> - `/model`
> - `/model <model-id>`

> [!tip] Cập nhật nóng
> Channel runtime theo dõi `config.toml` và áp dụng thay đổi cho:
> - `default_provider`, `default_model`, `default_temperature`
> - `api_key`, `api_url` (provider mặc định)
> - `reliability.*` cài đặt retry

### `integrations`

- `zeroclaw integrations info <name>`

### `skills`

- `zeroclaw skills list`
- `zeroclaw skills install <source>`
- `zeroclaw skills remove <name>`

> [!note] Nguồn
> Chấp nhận git remote (`https://...`, `http://...`, `ssh://...`, `git@host:owner/repo.git`) hoặc đường dẫn cục bộ.

> [!note] Skill manifest
> `SKILL.toml` hỗ trợ `prompts` và `[[tools]]`; cả hai được đưa vào system prompt của agent khi chạy.

### `migrate`

- `zeroclaw migrate openclaw [--source <path>] [--dry-run]`

### `config`

- `zeroclaw config schema`

> [!note] Xuất schema
> Xuất JSON Schema (draft 2020-12) cho toàn bộ hợp đồng `config.toml` ra stdout

### `completions`

- `zeroclaw completions bash`
- `zeroclaw completions fish`
- `zeroclaw completions zsh`
- `zeroclaw completions powershell`
- `zeroclaw completions elvish`

> [!note]
> Chỉ xuất ra stdout để script có thể được source trực tiếp

### `hardware`

- `zeroclaw hardware discover`
- `zeroclaw hardware introspect <path>`
- `zeroclaw hardware info [--chip <chip_name>]`

### `peripheral`

- `zeroclaw peripheral list`
- `zeroclaw peripheral add <board> <path>`
- `zeroclaw peripheral flash [--port <serial_port>]`
- `zeroclaw peripheral setup-uno-q [--host <ip_or_host>]`
- `zeroclaw peripheral flash-nucleo`

---

## Kiểm tra nhanh

```bash
zeroclaw --help
zeroclaw <command> --help
```
