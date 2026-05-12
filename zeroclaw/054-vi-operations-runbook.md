---
title: Operations runbook
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/operations-runbook.md
source: git
fetched_at: 2026-05-02T14:52:46.516418976-03:00
rendered_js: false
word_count: 474
summary: Tài liệu này cung cấp hướng dẫn vận hành day-2 cho hệ thống ZeroClaw, bao gồm quy trình khởi động, giám sát sức khỏe, xử lý sự cố và quản lý thay đổi cấu hình.
tags:
    - zeroclaw
    - operations-guide
    - system-maintenance
    - troubleshooting
    - service-management
    - runtime-monitoring
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---

# Sổ tay Vận hành ZeroClaw

Tài liệu này dành cho các operator chịu trách nhiệm duy trì tính sẵn sàng, tình trạng bảo mật và xử lý sự cố.

Cập nhật lần cuối: **2026-02-18**.  
Dùng tài liệu này cho các tác vụ vận hành day-2: khởi động và giám sát runtime, kiểm tra sức khoẻ, triển khai an toàn, phân loại và khôi phục sau sự cố.

---

## Phạm vi

Nếu đây là lần cài đặt đầu tiên, hãy bắt đầu từ [[054-vi-operations-runbook|Sổ tay Vận hành]].

---

## Các chế độ Runtime

| Chế độ | Lệnh | Khi nào dùng |
|---|---|---|
| Foreground runtime | `zeroclaw daemon` | gỡ lỗi cục bộ, phiên ngắn |
| Foreground gateway only | `zeroclaw gateway` | kiểm thử webhook endpoint |
| User service | `zeroclaw service install && zeroclaw service start` | runtime được quản lý liên tục bởi operator |

---

## Checklist Cơ bản cho Operator

1. Xác thực cấu hình:

```bash
zeroclaw status
```

2. Kiểm tra chẩn đoán:

```bash
zeroclaw doctor
zeroclaw channel doctor
```

3. Khởi động runtime:

```bash
zeroclaw daemon
```

4. Để chạy như user session service liên tục:

```bash
zeroclaw service install
zeroclaw service start
zeroclaw service status
```

---

## Tín hiệu Sức khoẻ và Trạng thái

| Tín hiệu | Lệnh / File | Kỳ vọng |
|---|---|---|
| Tính hợp lệ của config | `zeroclaw doctor` | không có lỗi nghiêm trọng |
| Kết nối channel | `zeroclaw channel doctor` | các channel đã cấu hình đều khoẻ mạnh |
| Tóm tắt runtime | `zeroclaw status` | provider/model/channels như mong đợi |
| Heartbeat/trạng thái daemon | `~/.zeroclaw/daemon_state.json` | file được cập nhật định kỳ |

---

## Log và Chẩn đoán

### macOS / Windows (log của service wrapper)

- `~/.zeroclaw/logs/daemon.stdout.log`
- `~/.zeroclaw/logs/daemon.stderr.log`

### Linux (systemd user service)

```bash
journalctl --user -u zeroclaw.service -f
```

---

## Quy trình Phân loại Sự cố (Fast Path)

1. Chụp trạng thái hệ thống:

```bash
zeroclaw status
zeroclaw doctor
zeroclaw channel doctor
```

2. Kiểm tra trạng thái service:

```bash
zeroclaw service status
```

3. Nếu service không khoẻ, khởi động lại sạch:

```bash
zeroclaw service stop
zeroclaw service start
```

4. Nếu các channel vẫn thất bại, kiểm tra allowlist và thông tin xác thực trong `~/.zeroclaw/config.toml`.

5. Nếu liên quan đến gateway, kiểm tra cài đặt bind/auth (`[gateway]`) và khả năng tiếp cận cục bộ.

---

## Quy trình Thay đổi An toàn

Trước khi áp dụng thay đổi cấu hình:

1. sao lưu `~/.zeroclaw/config.toml`
2. chỉ áp dụng một thay đổi logic tại một thời điểm
3. chạy `zeroclaw doctor`
4. khởi động lại daemon/service
5. xác minh bằng `status` + `channel doctor`

---

## Quy trình Rollback

Nếu một lần triển khai gây ra suy giảm hành vi:

1. khôi phục `config.toml` trước đó
2. khởi động lại runtime (`daemon` hoặc `service`)
3. xác nhận khôi phục qua `doctor` và kiểm tra sức khoẻ channel
4. ghi lại nguyên nhân gốc rễ và biện pháp khắc phục sự cố

---

## Tài liệu Liên quan

- [[046-i18n-vi-security-roadmap|Lộ trình cải tiến bảo mật]] — Kế hoạch bảo mật
- [[049-vi-adding-boards-and-tools|Thêm Board và Tool]] — Cấu hình phần cứng
- [[054-vi-operations-runbook|Sổ tay Vận hành]] — Vận hành day-2
- [[055-vi-pr-workflow|Quy trình PR]] — Quản lý PR

#operations-guide #system-maintenance
