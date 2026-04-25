---
title: Cách cài đặt BMad
url: https://docs.bmad-method.org/vi-vn/how-to/install-bmad/
source: sitemap
fetched_at: 2026-04-08T11:32:11.246870034-03:00
rendered_js: false
word_count: 442
summary: This guide explains how to install BMad into a project using the command line tool, detailing steps for running the installer, selecting installation paths and required AI tools, and verifying the setup afterward.
tags:
    - bmad-installation
    - ai-tooling
    - project-setup
    - command-line-guide
category: tutorial
---

Sử dụng lệnh `npx bmad-method install` để thiết lập BMad trong dự án của bạn với các module và công cụ AI theo lựa chọn.

Nếu bạn muốn dùng trình cài đặt không tương tác và cung cấp toàn bộ tùy chọn ngay trên dòng lệnh, xem [hướng dẫn này](https://docs.bmad-method.org/vi-vn/how-to/non-interactive-installation/).

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

- Bắt đầu một dự án mới với BMad
- Thêm BMad vào một codebase hiện có
- Cập nhật bản cài đặt BMad hiện tại

## Các bước thực hiện

[Phần tiêu đề “Các bước thực hiện”](#c%C3%A1c-b%C6%B0%E1%BB%9Bc-th%E1%BB%B1c-hi%E1%BB%87n)

### 1. Chạy trình cài đặt

[Phần tiêu đề “1. Chạy trình cài đặt”](#1-ch%E1%BA%A1y-tr%C3%ACnh-c%C3%A0i-%C4%91%E1%BA%B7t)

### 2. Chọn vị trí cài đặt

[Phần tiêu đề “2. Chọn vị trí cài đặt”](#2-ch%E1%BB%8Dn-v%E1%BB%8B-tr%C3%AD-c%C3%A0i-%C4%91%E1%BA%B7t)

Trình cài đặt sẽ hỏi bạn muốn đặt các tệp BMad ở đâu:

- Thư mục hiện tại (khuyến nghị cho dự án mới nếu bạn tự tạo thư mục và chạy lệnh từ bên trong nó)
- Đường dẫn tùy chọn

### 3. Chọn công cụ AI

[Phần tiêu đề “3. Chọn công cụ AI”](#3-ch%E1%BB%8Dn-c%C3%B4ng-c%E1%BB%A5-ai)

Chọn các công cụ AI bạn đang dùng:

- Claude Code
- Cursor
- Các công cụ khác

Mỗi công cụ có cách tích hợp skill riêng. Trình cài đặt sẽ tạo các tệp prompt nhỏ để kích hoạt workflow và agent, và đặt chúng vào đúng vị trí mà công cụ của bạn mong đợi.

Trình cài đặt sẽ hiện các module có sẵn. Chọn những module bạn cần - phần lớn người dùng chỉ cần **BMad Method** (module phát triển phần mềm).

### 5. Làm theo các prompt

[Phần tiêu đề “5. Làm theo các prompt”](#5-l%C3%A0m-theo-c%C3%A1c-prompt)

Trình cài đặt sẽ hướng dẫn các bước còn lại - cài đặt, tích hợp công cụ, và các tùy chọn khác.

## Bạn nhận được gì

[Phần tiêu đề “Bạn nhận được gì”](#b%E1%BA%A1n-nh%E1%BA%ADn-%C4%91%C6%B0%E1%BB%A3c-g%C3%AC)

```text

du-an-cua-ban/
├── _bmad/
│   ├── bmm/            # Các module bạn đã chọn
│   │   └── config.yaml # Cài đặt module (nếu bạn cần thay đổi sau này)
│   ├── core/           # Module core bắt buộc
│   └── ...
├── _bmad-output/       # Các artifact được tạo ra
├── .claude/            # Claude Code skills (nếu dùng Claude Code)
│   └── skills/
│       ├── bmad-help/
│       ├── bmad-persona/
│       └── ...
└── .cursor/            # Cursor skills (nếu dùng Cursor)
└── skills/
└── ...
```

## Xác minh cài đặt

[Phần tiêu đề “Xác minh cài đặt”](#x%C3%A1c-minh-c%C3%A0i-%C4%91%E1%BA%B7t)

Chạy `bmad-help` để xác minh mọi thứ hoạt động và xem bạn nên làm gì tiếp theo.

**BMad-Help là công cụ hướng dẫn thông minh** sẽ:

- Xác nhận bản cài đặt hoạt động đúng
- Hiển thị những gì có sẵn dựa trên module đã cài
- Đề xuất bước đầu tiên của bạn

Bạn cũng có thể hỏi nó:

```text

bmad-help Tôi vừa cài xong, giờ nên làm gì đầu tiên?
bmad-help Tôi có những lựa chọn nào cho một dự án SaaS?
```

## Khắc phục sự cố

[Phần tiêu đề “Khắc phục sự cố”](#kh%E1%BA%AFc-ph%E1%BB%A5c-s%E1%BB%B1-c%E1%BB%91)

**Trình cài đặt báo lỗi** - Sao chép toàn bộ output vào trợ lý AI của bạn và để nó phân tích.

**Cài đặt xong nhưng sau đó có thứ không hoạt động** - AI của bạn cần bối cảnh BMad để hỗ trợ. Xem [Cách tìm câu trả lời về BMad](https://docs.bmad-method.org/vi-vn/how-to/get-answers-about-bmad/) để biết cách cho AI truy cập đúng nguồn thông tin.