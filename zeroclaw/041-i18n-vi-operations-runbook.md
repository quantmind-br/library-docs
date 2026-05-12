---
optimized: true
optimized_at: 2026-05-05T00:00:00Z
title: Sổ tay Vận hành ZeroClaw
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/operations-runbook.md
source: git
fetched_at: 2026-05-02T14:51:24.657073041-03:00
rendered_js: false
word_count: 474
summary: Tài liệu này cung cấp hướng dẫn vận hành day-2, bao gồm quản lý runtime, giám sát sức khỏe hệ thống và các quy trình xử lý sự cố cho ZeroClaw.
tags:
    - operations
    - system-maintenance
    - troubleshooting
    - runtime-management
    - zeroclaw
    - deployment-safety
category: guide
---

# Sổ tay Vận hành ZeroClaw

Tài liệu này dành cho các operator chịu trách nhiệm duy trì tính sẵn sàng, tình trạng bảo mật và xử lý sự cố.

Cập nhật lần cuối: **2026-02-18**.

## Phạm vi

Dùng tài liệu này cho các tác vụ vận hành day-2:

- khởi động và giám sát runtime
- kiểm tra sức khoẻ và chẩn đoán hệ thống  
- triển khai an toàn và rollback
- phân loại và khôi phục sau sự cố

Nếu đây là lần cài đặt đầu tiên, hãy bắt đầu từ [[001-one-click-bootstrap|one-click-bootstrap]].

## Các chế độ Runtime

| Chế độ | Lệnh | Khi nào dùng |
|---|---|---|
| Foreground runtime | `zeroclaw daemon` | gỡ lỗi cục bộ, phiên ngắn |
| Foreground gateway only | `zeroclaw gateway` | kiểm thử webhook endpoint |
| User service | `zeroclaw service install && zeroclaw service start` | runtime được quản lý liên tục bởi operator |

## Checklist Cơ bản cho Operator

1. Xác thực cấu hình:

```bash
zeroclaw status
```

1. Kiểm tra chẩn đoán:

```bash
zeroclaw doctor
zeroclaw channel doctor
```

1. Khởi động runtime:

```bash
zeroclaw daemon
```

1. Để chạy như user session service liên tục:

```bash
zeroclaw service install
zeroclaw service start
zeroclaw service status
```

## Tín hiệu Sức khoẻ và Trạng thái

| Tín hiệu | Lệnh / File | Kỳ vọng |
|---|---|---|
| Tính hợp lệ của config | `zeroclaw doctor` | không có lỗi nghiêm trọng |
| Kết nối channel | `zeroclaw channel doctor` | các channel đã cấu hình đều khoẻ mạnh |
| Tóm tắt runtime | `zeroclaw status` | provider/model/channels như mong đợi |
| Heartbeat/trạng thái daemon | `~/.zeroclaw/daemon_state.json` | file được cập nhật định kỳ |

## Log và Chẩn đoán

### macOS / Windows (log của service wrapper)

- `~/.zeroclaw/logs/daemon.stdout.log`
- `~/.zeroclaw/logs/daemon.stderr.log`

### Linux (systemd user service)

```bash
journalctl --user -u zeroclaw.service -f
```

## Quy trình Phân loại Sự cố (Fast Path)

1. Chụp trạng thái hệ thống:

```bash
zeroclaw status
zeroclaw doctor
zeroclaw channel doctor
```

1. Kiểm tra trạng thái service:

```bash
zeroclaw service status
```

1. Nếu service không khoẻ, khởi động lại sạch:

```bash
zeroclaw service stop
zeroclaw service start
```

1. Nếu các channel vẫn thất bại, kiểm tra allowlist và thông tin xác thực trong `~/.zeroclaw/config.toml`.

2. Nếu liên quan đến gateway, kiểm tra cài đặt bind/auth (`[gateway]`) và khả năng tiếp cận cục bộ.

## Quy trình Thay đổi An toàn

Trước khi áp dụng thay đổi cấu hình:

1. sao lưu `~/.zeroclaw/config.toml`
2. chỉ áp dụng một thay đổi logic tại một thời điểm  
3. chạy `zeroclaw doctor`
4. khởi động lại daemon/service
5. xác minh bằng `status` + `channel doctor`

## Quy trình Rollback

Nếu một lần triển khai gây ra suy giảm hành vi:

1. khôi phục `config.toml` trước đó
2. khởi động lại runtime (`daemon` hoặc `service`)
3. xác nhận khôi phục qua `doctor` và kiểm tra sức khoẻ channel
4. ghi lại nguyên nhân gốc rễ và biện pháp khắc phục sự cố

## Tài liệu Liên quan

- [[001-one-click-bootstrap]]
- [[002-troubleshooting]]
- [[003-config-reference]]
- [[004-commands-reference]]
