---
title: Hướng dẫn chia nhỏ tài liệu
url: https://docs.bmad-method.org/vi-vn/how-to/shard-large-documents/
source: sitemap
fetched_at: 2026-04-08T11:32:19.594053979-03:00
rendered_js: false
word_count: 264
summary: This document explains when and how to use the `bmad-shard-doc` tool to split large markdown files into smaller, organized chunks based on section headings. It details the process and outlines how BMad's workflow system detects and prioritizes both whole documents and segmented ones.
tags:
    - markdown-sharding
    - document-chunking
    - bmad-tool
    - context-management
    - workflow-guide
category: tutorial
---

Sử dụng công cụ `bmad-shard-doc` nếu bạn cần tách các tệp markdown lớn thành nhiều tệp nhỏ có tổ chức để quản lý context tốt hơn.

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

Chỉ dùng cách này nếu bạn nhận thấy tổ hợp công cụ / model bạn đang dùng không thể nạp và đọc đầy đủ tất cả tài liệu đầu vào khi cần.

## Chia nhỏ tài liệu là gì?

[Phần tiêu đề “Chia nhỏ tài liệu là gì?”](#chia-nh%E1%BB%8F-t%C3%A0i-li%E1%BB%87u-l%C3%A0-g%C3%AC)

Chia nhỏ tài liệu là việc tách các tệp markdown lớn thành nhiều tệp nhỏ có tổ chức dựa trên các tiêu đề cấp 2 (`## Tiêu đề`).

```text

Trước khi chia nhỏ:
_bmad-output/planning-artifacts/
└── PRD.md (tệp lớn 50k token)
Sau khi chia nhỏ:
_bmad-output/planning-artifacts/
└── prd/
├── index.md                    # Mục lục kèm mô tả
├── overview.md                 # Phần 1
├── user-requirements.md        # Phần 2
├── technical-requirements.md   # Phần 3
└── ...                         # Các phần bổ sung
```

## Các bước thực hiện

[Phần tiêu đề “Các bước thực hiện”](#c%C3%A1c-b%C6%B0%E1%BB%9Bc-th%E1%BB%B1c-hi%E1%BB%87n)

### 1. Chạy công cụ Shard-Doc

[Phần tiêu đề “1. Chạy công cụ Shard-Doc”](#1-ch%E1%BA%A1y-c%C3%B4ng-c%E1%BB%A5-shard-doc)

### 2. Làm theo quy trình tương tác

[Phần tiêu đề “2. Làm theo quy trình tương tác”](#2-l%C3%A0m-theo-quy-tr%C3%ACnh-t%C6%B0%C6%A1ng-t%C3%A1c)

```text

Agent: Bạn muốn chia nhỏ tài liệu nào?
User: docs/PRD.md
Agent: Thư mục đích mặc định: docs/prd/
Chấp nhận mặc định? [y/n]
User: y
Agent: Đang chia nhỏ PRD.md...
✓ Đã tạo 12 tệp theo từng phần
✓ Đã tạo index.md
✓ Hoàn tất!
```

## Cơ chế workflow tìm tài liệu

[Phần tiêu đề “Cơ chế workflow tìm tài liệu”](#c%C6%A1-ch%E1%BA%BF-workflow-t%C3%ACm-t%C3%A0i-li%E1%BB%87u)

Workflow của BMad dùng **hệ thống phát hiện kép**:

1. **Thử tài liệu nguyên khối trước** - Tìm `document-name.md`
2. **Kiểm tra bản đã chia nhỏ** - Tìm `document-name/index.md`
3. **Quy tắc ưu tiên** - Bản nguyên khối được ưu tiên nếu cả hai cùng tồn tại; hãy xóa bản nguyên khối nếu bạn muốn workflow dùng bản đã chia nhỏ

## Hỗ trợ trong workflow

[Phần tiêu đề “Hỗ trợ trong workflow”](#h%E1%BB%97-tr%E1%BB%A3-trong-workflow)

Tất cả workflow BMM đều hỗ trợ cả hai định dạng:

- Tài liệu nguyên khối
- Tài liệu đã chia nhỏ
- Tự động nhận diện
- Trong suốt với người dùng