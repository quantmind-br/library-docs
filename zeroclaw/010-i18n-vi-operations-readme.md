---
optimized: true
optimized_at: 2026-05-05T00:00:00Z
title: Tài liệu vận hành và triển khai
tags:
  - zeroclaw
  - operations-guide
  - deployment-procedures
  - system-maintenance
  - troubleshooting
  - production-support
category: guide
word_count: 109
---
# Tài liệu vận hành và triển khai

Dành cho operator vận hành ZeroClaw liên tục hoặc trên production.

## Vận hành cốt lõi

- [[041-i18n-vi-operations-runbook|Sổ tay Day-2]]
- [[../release-process|Sổ tay Release]]
- [[../troubleshooting|Ma trận xử lý sự cố]]
- [[../network-deployment|Triển khai mạng/gateway an toàn]]
- [[../mattermost-setup|Thiết lập Mattermost (dành riêng cho channel)]]

## Luồng thường gặp

1. Xác thực runtime (`status`, `doctor`, `channel doctor`)
2. Áp dụng từng thay đổi config một lần
3. Khởi động lại service/daemon
4. Xác minh tình trạng channel và gateway
5. Rollback nhanh nếu hành vi bị hồi quy

## Liên quan

- [[../config-reference|Tham chiếu config]]
- [[../security/README|Bộ sưu tập bảo mật]]
