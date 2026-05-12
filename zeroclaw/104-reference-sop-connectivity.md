---
title: Connectivity
title_vi: Kết nối & Fan-In Sự kiện SOP
url: https://github.com/openagen/zeroclaw/blob/master/docs/reference/sop/connectivity.md
source: git
fetched_at: 2026-05-02T14:52:01.707591898-03:00
rendered_js: false
word_count: 551
summary: This document details the configuration and operational integration of external event sources, including MQTT, webhooks, and cron jobs, into the ZeroClaw SOP dispatcher.
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - event-driven-architecture
  - mqtt-integration
  - webhook-config
  - cron-scheduler
  - system-integration
  - security-defaults
  - idempotency
category: configuration
---
# SOP Connectivity & Event Fan-In

> [!info] Tóm tắt
> Tài liệu mô tả cách các sự kiện bên ngoài (MQTT, webhook, cron) kích hoạt chạy SOP trong ZeroClaw.

## Tổng quan

ZeroClaw định tuyến sự kiện MQTT/webhook/cron/peripheral qua dispatcher SOP thống nhất (`dispatch_sop_event`).

**Hành vi chính:**
- **Matching trigger nhất quán:** một đường dẫn matcher cho tất cả nguồn sự kiện
- **Audit khởi chạy SOP:** các lần chạy khởi động được lưu trữ qua `SopAuditLogger`
- **An toàn headless:** trong ngữ cảnh non-agent-loop, actions `ExecuteStep` được log là pending (không thực thi im lặng)

## Cấu hình MQTT

### Cấu hình Broker

```toml
[channels_config.mqtt]
broker_url = "mqtts://broker.example.com:8883"  # dùng mqtt:// cho plaintext
client_id = "zeroclaw-agent-1"
topics = ["sensors/alert", "ops/deploy/#"]
qos = 1
username = "mqtt-user"      # tùy chọn
password = "mqtt-password"  # tùy chọn
use_tls = true              # phải match scheme (mqtts:// => true)
```

### Định nghĩa Trigger MQTT

Trong `SOP.toml`:

```toml
[[triggers]]
type = "mqtt"
topic = "sensors/alert"
condition = "$.severity >= 2"
```

Payload MQTT được forward vào payload sự kiện SOP (`event.payload`), sau đó hiển thị trong context step.

## Tích hợp Webhook

### Endpoints

- **`POST /sop/{*rest}`**: endpoint SOP-exclusive. Trả về `404` nếu không match SOP nào. Không fallback LLM
- **`POST /webhook`**: endpoint chat. Thử dispatch SOP đầu tiên; nếu không match, fallback về flow LLM bình thường

Matching path là exact so với đường dẫn trigger webhook đã cấu hình.

**Ví dụ:**
- Trigger path trong SOP: `path = "/sop/deploy"`
- Request match: `POST /sop/deploy`

### Authorization

Khi pairing enabled (mặc định), cung cấp:

1. `Authorization: Bearer <token>` (từ `POST /pair`)
2. Lớp thứ hai tùy chọn: `X-Webhook-Secret: <secret>` khi secret webhook được cấu hình

### Idempotency

Sử dụng:

`X-Idempotency-Key: <unique-key>`

**Mặc định:**
- TTL: 300s
- Phản hồi trùng lặp: `200 OK` với `"status": "duplicate"`

Idempotency keys được namespaced theo endpoint (`/webhook` vs `/sop/*`).

### Request mẫu

```bash
curl -X POST http://127.0.0.1:3000/sop/deploy \
  -H "Authorization: Bearer <token>" \
  -H "X-Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"message":"deploy-service-a"}'
```

**Phản hồi điển hình:**
```json
{
  "status": "accepted",
  "matched_sops": ["deploy-pipeline"],
  "source": "sop_webhook",
  "path": "/sop/deploy"
}
```

## Tích hợp Cron

Bộ lập lịch đánh giá triggers cron đã cache sử dụng window-based check.

- **Window-based:** các sự kiện trong `(last_check, now]` không bị bỏ lỡ
- **At-most-once per expression per tick:** nếu nhiều điểm fire trong một cửa sổ poll, dispatch xảy ra một lần

**Ví dụ trigger:**
```toml
[[triggers]]
type = "cron"
expression = "0 0 8 * * *"
```

Biểu thức cron hỗ trợ 5, 6, hoặc 7 fields.

## Mặc định bảo mật

| Tính năng | Cơ chế |
|-----------|--------|
| **Transport MQTT** | `mqtts://` + `use_tls = true` cho transport TLS |
| **Auth webhook** | Bearer token pairing (mặc định required), secret header tùy chọn |
| **Rate limiting** | Giới hạn mỗi client trên routes webhook (`webhook_rate_limit_per_minute`, mặc định `60`) |
| **Idempotency** | Deduplication dựa header (`X-Idempotency-Key`, TTL mặc định `300s`) |
| **Validation cron** | Biểu thức cron không hợp lệ fail closed trong quá trình parsing/cache build |

## Troubleshooting

| Triệu chứng | Nguyên nhân có khả năng | Fix |
|-------------|------------------------|-----|
| **Lỗi kết nối MQTT** | broker URL/TLS mismatch | Verify scheme + TLS flag pairing (`mqtt://`/`false`, `mqtts://`/`true`) |
| **Webhook `401 Unauthorized`** | thiếu bearer hoặc secret không hợp lệ | Re-pair token (`POST /pair`) và verify `X-Webhook-Secret` nếu cấu hình |
| **`/sop/*` trả về 404** | trigger path mismatch | Đảm bảo `SOP.toml` dùng exact path (ví dụ `/sop/deploy`) |
| **SOP khởi động nhưng step không thực thi** | trigger headless không có agent loop active | Chạy agent loop cho `ExecuteStep`, hoặc thiết kế run để pause trên approvals |
| **Cron không fire** | daemon không chạy hoặc expression không hợp lệ | Chạy `zeroclaw daemon`; check logs cho warnings parse cron |

#zeroclaw #sop #event-driven