---
title: Commands reference
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/commands-reference.md
source: git
fetched_at: 2026-05-02T14:51:06.74502369-03:00
rendered_js: false
word_count: 770
summary: Tài liệu này cung cấp bảng tham chiếu chi tiết cho các lệnh CLI của hệ thống ZeroClaw, bao gồm quản lý tác vụ, cấu hình phần cứng, tích hợp dịch vụ và vòng đời của các agent.
tags:
    - zeroclaw
    - cli-reference
    - command-line
    - system-administration
    - automation
    - configuration
category: reference
optimized: true
optimized_at: 2026-05-05T12:00:00Z
---

# Tham khảo lệnh ZeroClaw

Dựa trên CLI hiện tại (`zeroclaw --help`).

> [!info]
> Xác minh lần cuối: **2026-02-20**

---

## 1. Lệnh cấp cao nhất

| Lệnh | Mục đích |
|---|---|
| `onboard` | Khởi tạo workspace/config nhanh hoặc tương tác |
| `agent` | Chạy chat tương tác hoặc chế độ gửi tin nhắn đơn |
| `gateway` | Khởi động gateway webhook và HTTP WhatsApp |
| `daemon` | Khởi động runtime có giám sát (gateway + channels + heartbeat/scheduler tùy chọn) |
| `service` | Quản lý vòng đời dịch vụ cấp hệ điều hành |
| `doctor` | Chạy chẩn đoán và kiểm tra trạng thái |
| `status` | Hiển thị cấu hình và tóm tắt hệ thống |
| `cron` | Quản lý tác vụ định kỳ |
| `models` | Làm mới danh mục model của provider |
| `providers` | Liệt kê ID provider, bí danh và provider đang dùng |
| `channel` | Quản lý kênh và kiểm tra sức khỏe kênh |
| `integrations` | Kiểm tra chi tiết tích hợp |
| `skills` | Liệt kê/cài đặt/gỡ bỏ skills |
| `migrate` | Nhập dữ liệu từ runtime khác (hiện hỗ trợ OpenClaw) |
| `config` | Xuất schema cấu hình dạng máy đọc được |
| `completions` | Tạo script tự hoàn thành cho shell ra stdout |
| `hardware` | Phát hiện và kiểm tra phần cứng USB |
| `peripheral` | Cấu hình và nạp firmware thiết bị ngoại vi |

---

## 2. Nhóm lệnh chi tiết

### 2.1 `onboard`

```bash
zeroclaw onboard
zeroclaw onboard --interactive
zeroclaw onboard --channels-only
zeroclaw onboard --api-key <KEY> --provider <ID> --memory <sqlite|lucid|markdown|none>
zeroclaw onboard --api-key <KEY> --provider <ID> --model <MODEL_ID> --memory <sqlite|lucid|markdown|none>
```

### 2.2 `agent`

```bash
zeroclaw agent
zeroclaw agent -m "Hello"
zeroclaw agent --provider <ID> --model <MODEL> --temperature <0.0-2.0>
zeroclaw agent --peripheral <board:path>
```

### 2.3 `gateway` / `daemon`

```bash
zeroclaw gateway [--host <HOST>] [--port <PORT>]
zeroclaw daemon [--host <HOST>] [--port <PORT>]
```

### 2.4 `service`

```bash
zeroclaw service install
zeroclaw service start
zeroclaw service stop
zeroclaw service restart
zeroclaw service status
zeroclaw service uninstall
```

### 2.5 `cron`

```bash
zeroclaw cron list
zeroclaw cron add <expr> [--tz <IANA_TZ>] <command>
zeroclaw cron add-at <rfc3339_timestamp> <command>
zeroclaw cron add-every <every_ms> <command>
zeroclaw cron once <delay> <command>
zeroclaw cron remove <id>
zeroclaw cron pause <id>
zeroclaw cron resume <id>
```

### 2.6 `models`

```bash
zeroclaw models refresh
zeroclaw models refresh --provider <ID>
zeroclaw models refresh --force
```

**Provider hỗ trợ:**
`openrouter`, `openai`, `anthropic`, `groq`, `mistral`, `deepseek`, `xai`, `together-ai`, `gemini`, `ollama`, `astrai`, `venice`, `fireworks`, `cohere`, `moonshot`, `glm`, `zai`, `qwen`, `nvidia`

### 2.7 `channel`

```bash
zeroclaw channel list
zeroclaw channel start
zeroclaw channel doctor
zeroclaw channel bind-telegram <IDENTITY>
zeroclaw channel add <type> <json>
zeroclaw channel remove <name>
```

**Lệnh trong chat khi runtime đang chạy (Telegram/Discord):**
- `/models`
- `/models <provider>`
- `/model`
- `/model <model-id>`

**Lưu ý:**
Channel runtime theo dõi `config.toml` và tự động áp dụng thay đổi cho:
- `default_provider`
- `default_model`
- `default_temperature`
- `api_key` / `api_url` (cho provider mặc định)
- `reliability.*` cài đặt retry của provider

`add/remove` hiện chuyển hướng về thiết lập có hướng dẫn / cấu hình thủ công (chưa hỗ trợ đầy đủ mutator khai báo).

### 2.8 `integrations`

```bash
zeroclaw integrations info <name>
```

### 2.9 `skills`

```bash
zeroclaw skills list
zeroclaw skills install <source>
zeroclaw skills remove <name>
```

**`<source>`** chấp nhận:
- Git remote (`https://...`, `http://...`, `ssh://...` và `git@host:owner/repo.git`)
- Đường dẫn cục bộ

**Skill manifest (`SKILL.toml`):**
Hỗ trợ `prompts` và `[[tools]]`; cả hai được đưa vào system prompt của agent khi chạy, giúp model có thể tuân theo hướng dẫn skill mà không cần đọc thủ công.

### 2.10 `migrate`

```bash
zeroclaw migrate openclaw [--source <path>] [--dry-run]
```

### 2.11 `config`

```bash
zeroclaw config schema
```

**`config schema`** xuất JSON Schema (draft 2020-12) cho toàn bộ hợp đồng `config.toml` ra stdout.

### 2.12 `completions`

```bash
zeroclaw completions bash
zeroclaw completions fish
zeroclaw completions zsh
zeroclaw completions powershell
zeroclaw completions elvish
```

**Lưu ý:**
`completions` chỉ xuất ra stdout để script có thể được source trực tiếp mà không bị lẫn log/cảnh báo.

### 2.13 `hardware`

```bash
zeroclaw hardware discover
zeroclaw hardware introspect <path>
zeroclaw hardware info [--chip <chip_name>]
```

### 2.14 `peripheral`

```bash
zeroclaw peripheral list
zeroclaw peripheral add <board> <path>
zeroclaw peripheral flash [--port <serial_port>]
zeroclaw peripheral setup-uno-q [--host <ip_or_host>]
zeroclaw peripheral flash-nucleo
```

#zeroclaw #cli-reference #command-line #system-administration #automation #configuration #vietnamese-docs