---
title: Proxy agent playbook
date: 2026-05-05T00:00:00Z
optimized: true
tags:
  - proxy-management
  - zeroclaw
  - network-configuration
  - agent-operations
  - tool-calls
  - troubleshooting
---

# Proxy Agent Playbook

Sổ tay vận hành cung cấp tool call copy-paste để cấu hình hành vi proxy qua `proxy_config`.

Dùng khi bạn muốn agent chuyển đổi phạm vi proxy nhanh chóng và an toàn.

---

## Tóm tắt

- **Mục đích:** cung cấp tool call sẵn sàng sử dụng để quản lý phạm vi proxy và rollback.
- **Đối tượng:** operators và maintainers vận hành ZeroClaw trong mạng có proxy.
- **Phạm vi:** hành động `proxy_config`, lựa chọn mode, quy trình xác minh và xử lý sự cố.
- **Ngoài phạm vi:** gỡ lỗi mạng chung không liên quan đến hành vi runtime của ZeroClaw.

---

## Đường dẫn nhanh theo mục đích

### Chỉ proxy traffic nội bộ ZeroClaw

1. Dùng scope `zeroclaw`.
2. Đặt `http_proxy`/`https_proxy` hoặc `all_proxy`.
3. Xác minh bằng `{"action":"get"}`.

Xem: [[070-ops-proxy-agent-playbook#mode-a-chỉ-proxy-cho-nội-bộ-zeroclaw|Mode A]]

### Chỉ proxy các dịch vụ được chọn

1. Dùng scope `services`.
2. Đặt các key cụ thể hoặc wildcard selector trong `services`.
3. Xác minh phủ sóng bằng `{"action":"list_services"}`.

Xem: [[070-ops-proxy-agent-playbook#mode-b-chỉ-proxy-cho-các-dịch-vụ-cụ-thể|Mode B]]

### Xuất biến môi trường proxy cho toàn bộ process

1. Dùng scope `environment`.
2. Áp dụng bằng `{"action":"apply_env"}`.
3. Xác minh snapshot env qua `{"action":"get"}`.

Xem: [[070-ops-proxy-agent-playbook#mode-c-proxy-cho-toàn-bộ-môi-trường-process|Mode C]]

### Rollback khẩn cấp

1. Tắt proxy.
2. Nếu cần, xóa các biến env đã xuất.
3. Kiểm tra lại snapshot runtime và môi trường.

Xem: [[070-ops-proxy-agent-playbook#rollback|Rollback]]

---

## Ma trận quyết định phạm vi

| Phạm vi | Ảnh hưởng | Xuất biến env | Trường hợp dùng điển hình |
|---|---|---|---|
| `zeroclaw` | Các HTTP client nội bộ ZeroClaw | Không | Proxying runtime thông thường không có tác dụng phụ cấp process |
| `services` | Chỉ các service key/selector được chọn | Không | Định tuyến chi tiết cho provider/tool/channel cụ thể |
| `environment` | Runtime + biến môi trường proxy của process | Có | Các tích hợp yêu cầu `HTTP_PROXY`/`HTTPS_PROXY`/`ALL_PROXY` |

---

## Quy trình an toàn chuẩn

Trình tự cho mọi thay đổi proxy:

1. Kiểm tra trạng thái hiện tại.
2. Khám phá các service key/selector hợp lệ.
3. Áp dụng cấu hình phạm vi mục tiêu.
4. Xác minh snapshot runtime và môi trường.
5. Rollback nếu hành vi không như kỳ vọng.

Tool call:

```json
{"action":"get"}
{"action":"list_services"}
```

---

## Mode A — Chỉ Proxy Cho Nội Bộ ZeroClaw

Dùng khi traffic HTTP của provider/channel/tool ZeroClaw cần đi qua proxy mà không xuất biến env proxy cấp process.

Tool calls:

```json
{"action":"set","enabled":true,"scope":"zeroclaw","http_proxy":"http://127.0.0.1:7890","https_proxy":"http://127.0.0.1:7890","no_proxy":["localhost","127.0.0.1"]}
{"action":"get"}
```

Hành vi kỳ vọng:

- Runtime proxy hoạt động cho các HTTP client của ZeroClaw.
- Không cần xuất `HTTP_PROXY` / `HTTPS_PROXY` vào env của process.

---

## Mode B — Chỉ Proxy Cho Các Dịch Vụ Cụ Thể

Dùng khi chỉ một phần hệ thống cần đi qua proxy (ví dụ provider/tool/channel cụ thể).

### Nhắm vào dịch vụ cụ thể

```json
{"action":"set","enabled":true,"scope":"services","services":["provider.openai","tool.http_request","channel.telegram"],"all_proxy":"socks5h://127.0.0.1:1080","no_proxy":["localhost","127.0.0.1",".internal"]}
{"action":"get"}
```

### Nhắm theo selector

```json
{"action":"set","enabled":true,"scope":"services","services":["provider.*","tool.*"],"http_proxy":"http://127.0.0.1:7890"}
{"action":"get"}
```

Hành vi kỳ vọng:

- Chỉ các service khớp mới dùng proxy.
- Các service không khớp bỏ qua proxy.

---

## Mode C — Proxy Cho Toàn Bộ Môi Trường Process

Dùng khi bạn cần xuất tường minh các biến env của process (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, `NO_PROXY`) cho các tích hợp runtime.

### Cấu hình và áp dụng environment scope

```json
{"action":"set","enabled":true,"scope":"environment","http_proxy":"http://127.0.0.1:7890","https_proxy":"http://127.0.0.1:7890","no_proxy":"localhost,127.0.0.1,.internal"}
{"action":"apply_env"}
{"action":"get"}
```

Hành vi kỳ vọng:

- Runtime proxy hoạt động.
- Các biến môi trường được xuất cho process.

---

## Rollback

### Tắt proxy (hành vi an toàn mặc định)

```json
{"action":"disable"}
{"action":"get"}
```

### Tắt proxy và xóa cưỡng bức các biến env

```json
{"action":"disable","clear_env":true}
{"action":"get"}
```

### Giữ proxy bật nhưng chỉ xóa các biến env đã xuất

```json
{"action":"clear_env"}
{"action":"get"}
```

---

## Công thức vận hành thường dùng

### Chuyển từ proxy toàn environment sang proxy chỉ service

```json
{"action":"set","enabled":true,"scope":"services","services":["provider.openai","tool.http_request"],"all_proxy":"socks5://127.0.0.1:1080"}
{"action":"get"}
```

### Thêm một dịch vụ proxied

```json
{"action":"set","scope":"services","services":["provider.openai","tool.http_request","channel.slack"]}
{"action":"get"}
```

### Đặt lại danh sách `services` với selector

```json
{"action":"set","scope":"services","services":["provider.*","channel.telegram"]}
{"action":"get"}
```

---

## Xử lý sự cố

- **Lỗi:** `proxy.scope='services' requires a non-empty proxy.services list`
  - Khắc phục: đặt ít nhất một service key cụ thể hoặc selector.

- **Lỗi:** invalid proxy URL scheme
  - Scheme được chấp nhận: `http`, `https`, `socks5`, `socks5h`.

- **Proxy không áp dụng như kỳ vọng**
  - Chạy `{"action":"list_services"}` và xác minh tên/selector dịch vụ.
  - Chạy `{"action":"get"}` và kiểm tra giá trị snapshot `runtime_proxy` và `environment`.

---

## Tài liệu liên quan

- [[001-i18n-vi-getting-started-readme|README]] — Chỉ mục tài liệu và phân loại.
- [[068-ops-network-deployment|network-deployment]] — Hướng dẫn triển khai mạng đầu-cuối và topology tunnel.
- [[083-ops-resource-limits|resource-limits]] — Giới hạn an toàn runtime cho ngữ cảnh thực thi mạng/tool.

---

## Ghi chú bảo trì

- **Chủ sở hữu:** maintainer runtime và tooling.
- **Điều kiện cập nhật:** các hành động `proxy_config` mới, ngữ nghĩa phạm vi proxy, hoặc thay đổi selector dịch vụ được hỗ trợ.
- **Lần review cuối:** 2026-02-18.
