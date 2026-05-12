---
title: README
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/getting-started/README.md
source: git
fetched_at: 2026-05-02T14:51:15.753132703-03:00
rendered_js: false
word_count: 194
summary: This document provides a foundational guide for new users to install, configure, and initialize the Zeroclaw environment.
tags:
    - getting-started
    - installation-guide
    - cli-setup
    - onboarding
    - configuration
    - initialization
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tài liệu Bắt đầu

> [!info] Tóm lược
> Hướng dẫn cài đặt, cấu hình và khởi tạo môi trường ZeroClaw cho người dùng mới.

## Mục đích

Tài liệu cung cấp lộ trình nhanh chóng để cài đặt, cấu hình và vận hành ZeroClaw lần đầu tiên.

## Lộ trình bắt đầu

1. Tổng quan hệ thống: [[030-vi-readme|README.vi]]
2. Cài đặt nhanh bằng lệnh bootstrap: [[144-setup-guides-one-click-bootstrap.vi|One click bootstrap.vi]]
3. Tìm lệnh theo tác vụ: [[134-vi-commands-reference|Commands reference]]

## Lựa chọn cài đặt

| Tình huống | Lệnh sử dụng |
|------------|--------------|
| Có API key, muốn cài nhanh | `zeroclaw onboard --api-key sk-... --provider openrouter` |
| Muốn hướng dẫn tương tác từng bước | `zeroclaw onboard --interactive` |
| Đã có config, chỉnh sửa kênh | `zeroclaw onboard --channels-only` |
| Dùng xác thực subscription | Xem [Subscription Auth](https://github.com/openagen/zeroclaw/blob/master/docs/README.md#subscription-auth-openai-codex--claude-code) |

## Thiết lập và xác minh

- Thiết lập nhanh: `zeroclaw onboard --api-key "sk-..." --provider openrouter`
- Thiết lập tương tác: `zeroclaw onboard --interactive`
- Kiểm tra môi trường: `zeroclaw status` + `zeroclaw doctor`

## Tiếp theo

- Vận hành runtime: [[028-vi-operations-readme|README]]
- Tra cứu tham khảo: [[031-vi-reference-readme|README]]

#zeroclaw #getting-started #installation-guide #cli-setup