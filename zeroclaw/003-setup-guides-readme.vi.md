---
title: README.vi
url: https://github.com/openagen/zeroclaw/blob/master/docs/setup-guides/README.vi.md
source: git
fetched_at: 2026-05-02T14:52:13.729808174-03:00
rendered_js: false
word_count: 174
summary: This document serves as an onboarding guide for new users of the Zeroclaw platform, outlining the installation procedures, command-line setup options, and environment verification steps.
tags:
    - getting-started
    - onboarding
    - cli-commands
    - setup-guide
    - configuration
    - environment-check
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tài liệu Bắt đầu

> [!info] Mục đích
> Hướng dẫn onboarding cho người dùng mới, bao gồm quy trình cài đặt, tùy chọn setup CLI và kiểm tra môi trường.

## Lộ trình bắt đầu

1. Tổng quan hệ thống: [[030-vi-readme|README]]
2. Cài đặt nhanh bằng bootstrap: [[144-setup-guides-one-click-bootstrap.vi|One click bootstrap.vi]]
3. Tìm lệnh theo tác vụ: [[134-vi-commands-reference|Commands reference]]

## Chọn hướng đi

| Tình huống | Lệnh sử dụng |
|------------|--------------|
| Có API key, cài nhanh nhất | `zeroclaw onboard --api-key sk-... --provider openrouter` |
| Muốn hướng dẫn tương tác từng bước | `zeroclaw onboard --interactive` |
| Đã có config, sửa kênh | `zeroclaw onboard --channels-only` |
| Dùng xác thực subscription | Xem [Subscription Auth](https://github.com/openagen/zeroclaw/blob/master/docs/README.vi.md#subscription-auth-openai-codex--claude-code) |

## Thiết lập và xác minh

- Thiết lập nhanh: `zeroclaw onboard --api-key "sk-..." --provider openrouter`
- Thiết lập tương tác: `zeroclaw onboard --interactive`
- Kiểm tra môi trường: `zeroclaw status` + `zeroclaw doctor`

## Tiếp theo

- Vận hành runtime: [[016-ops-readme|README]]
- Tra cứu tham khảo: [[031-vi-reference-readme|README]]

#zeroclaw #getting-started #onboarding #setup-guide