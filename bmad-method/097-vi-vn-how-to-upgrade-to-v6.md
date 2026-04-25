---
title: Cách nâng cấp lên v6
url: https://docs.bmad-method.org/vi-vn/how-to/upgrade-to-v6/
source: sitemap
fetched_at: 2026-04-08T11:32:21.486744184-03:00
rendered_js: false
word_count: 505
summary: This guide explains the step-by-step process of upgrading from BMad v4 to the v6 architecture. It covers running the installer, handling old installations, cleaning up deprecated IDE skills, migrating planning artifacts, and moving ongoing development work while detailing the new v6 structure.
tags:
    - upgrade-guide
    - bmad-migration
    - v4-to-v6
    - planning-artifacts
    - development-workflow
category: guide
---

Sử dụng trình cài đặt BMad để nâng cấp từ v4 lên v6, bao gồm khả năng tự động phát hiện bản cài đặt cũ và hỗ trợ di chuyển.

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

- Bạn đang dùng BMad v4 (thư mục `.bmad-method`)
- Bạn muốn chuyển sang kiến trúc v6 mới
- Bạn có các planning artifact hiện có cần giữ lại

## Các bước thực hiện

[Phần tiêu đề “Các bước thực hiện”](#c%C3%A1c-b%C6%B0%E1%BB%9Bc-th%E1%BB%B1c-hi%E1%BB%87n)

### 1. Chạy trình cài đặt

[Phần tiêu đề “1. Chạy trình cài đặt”](#1-ch%E1%BA%A1y-tr%C3%ACnh-c%C3%A0i-%C4%91%E1%BA%B7t)

Làm theo [Hướng dẫn cài đặt](https://docs.bmad-method.org/vi-vn/how-to/install-bmad/).

### 2. Xử lý bản cài đặt cũ

[Phần tiêu đề “2. Xử lý bản cài đặt cũ”](#2-x%E1%BB%AD-l%C3%BD-b%E1%BA%A3n-c%C3%A0i-%C4%91%E1%BA%B7t-c%C5%A9)

Khi v4 được phát hiện, bạn có thể:

- Cho phép trình cài đặt sao lưu và xóa `.bmad-method`
- Thoát và tự xử lý dọn dẹp thủ công

Nếu trước đây bạn đặt tên thư mục BMad khác - bạn sẽ phải tự xóa thư mục đó.

### 3. Dọn dẹp skill IDE cũ

[Phần tiêu đề “3. Dọn dẹp skill IDE cũ”](#3-d%E1%BB%8Dn-d%E1%BA%B9p-skill-ide-c%C5%A9)

Tự xóa các command/skill IDE cũ của v4 - ví dụ nếu bạn dùng Claude Code, hãy tìm các thư mục lồng nhau bắt đầu bằng `bmad` và xóa chúng:

- `.claude/commands/`

Các skill v6 mới sẽ được cài tại:

- `.claude/skills/`

### 4. Di chuyển planning artifacts

[Phần tiêu đề “4. Di chuyển planning artifacts”](#4-di-chuy%E1%BB%83n-planning-artifacts)

**Nếu bạn có tài liệu lập kế hoạch (Brief/PRD/UX/Architecture):**

Di chuyển chúng vào `_bmad-output/planning-artifacts/` với tên mô tả rõ ràng:

- Tên tệp PRD nên chứa `PRD`
- Tên tệp tương ứng nên chứa `brief`, `architecture`, hoặc `ux-design`
- Tài liệu đã chia nhỏ có thể đặt trong các thư mục con đặt tên phù hợp

**Nếu bạn đang lập kế hoạch dở dang:** Hãy cân nhắc bắt đầu lại với workflow v6. Bạn vẫn có thể dùng các tài liệu hiện có làm input - các workflow discovery tiên tiến trong v6, kết hợp web search và chế độ plan trong IDE, cho kết quả tốt hơn.

### 5. Di chuyển công việc phát triển đang dở dang

[Phần tiêu đề “5. Di chuyển công việc phát triển đang dở dang”](#5-di-chuy%E1%BB%83n-c%C3%B4ng-vi%E1%BB%87c-ph%C3%A1t-tri%E1%BB%83n-%C4%91ang-d%E1%BB%9F-dang)

Nếu bạn đã có các story được tạo hoặc đã triển khai:

1. Hoàn thành cài đặt v6
2. Đặt `epics.md` hoặc `epics/epic*.md` vào `_bmad-output/planning-artifacts/`
3. Chạy workflow `bmad-sprint-planning` của Scrum Master
4. Nói rõ với SM những epic/story nào đã hoàn thành

## Bạn nhận được gì

[Phần tiêu đề “Bạn nhận được gì”](#b%E1%BA%A1n-nh%E1%BA%ADn-%C4%91%C6%B0%E1%BB%A3c-g%C3%AC)

**Cấu trúc thống nhất của v6:**

```text

du-an-cua-ban/
├── _bmad/               # Thư mục cài đặt duy nhất
│   ├── _config/         # Các tùy chỉnh của bạn
│   │   └── agents/      # Tệp tùy chỉnh agent
│   ├── core/            # Framework core dùng chung
│   ├── bmm/             # Module BMad Method
│   ├── bmb/             # BMad Builder
│   └── cis/             # Creative Intelligence Suite
└── _bmad-output/        # Thư mục output (là thư mục docs trong v4)
```

## Di chuyển module

[Phần tiêu đề “Di chuyển module”](#di-chuy%E1%BB%83n-module)

Module v4Trạng thái trong v6`.bmad-2d-phaser-game-dev`Đã được tích hợp vào module BMGD`.bmad-2d-unity-game-dev`Đã được tích hợp vào module BMGD`.bmad-godot-game-dev`Đã được tích hợp vào module BMGD`.bmad-infrastructure-devops`Đã bị ngừng hỗ trợ - agent DevOps mới sắp ra mắt`.bmad-creative-writing`Chưa được điều chỉnh - module v6 mới sắp ra mắt

## Các thay đổi chính

[Phần tiêu đề “Các thay đổi chính”](#c%C3%A1c-thay-%C4%91%E1%BB%95i-ch%C3%ADnh)

Khái niệmv4v6**Core**`_bmad-core` thực chất là BMad Method`_bmad/core/` là framework dùng chung**Method**`_bmad-method``_bmad/bmm/`**Config**Sửa trực tiếp các tệp`config.yaml` theo từng module**Documents**Cần thiết lập trước cho bản chia nhỏ hoặc nguyên khốiLinh hoạt hoàn toàn, tự động quét