---
title: README
tags:
  - operational-guide
  - production-deployment
  - system-maintenance
  - troubleshooting
  - zeroclaw-ops
  - infrastructure-management
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/operations/README.md
source: git
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
word_count: 121
---
# Tài liệu vận hành và triển khai

Dành cho operator vận hành ZeroClaw liên tục hoặc trên production.

## Vận hành cốt lõi

- Sổ tay Day-2: [[../operations-runbook|operations runbook]]
- Sổ tay Release: [[../release-process|release process]]
- Ma trận xử lý sự cố: [[../troubleshooting|troubleshooting]]
- Triển khai mạng/gateway an toàn: [[../network-deployment|network deployment]]
- Thiết lập Mattermost (dành riêng cho channel): [[../mattermost-setup|Mattermost setup]]

## Luồng thường gặp

1. Xác thực runtime (`status`, `doctor`, `channel doctor`)
2. Áp dụng từng thay đổi config một lần
3. Khởi động lại service/daemon
4. Xác minh tình trạng channel và gateway
5. Rollback nhanh nếu hành vi bị hồi quy

## Liên quan

- Tham chiếu config: [[../config-reference|config reference]]
- Bộ sưu tập bảo mật: [[../security|security]]
