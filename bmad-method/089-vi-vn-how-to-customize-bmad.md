---
title: Cách tùy chỉnh BMad
url: https://docs.bmad-method.org/vi-vn/how-to/customize-bmad/
source: sitemap
fetched_at: 2026-04-08T11:32:05.428176375-03:00
rendered_js: false
word_count: 662
summary: This document details how to customize the behavior, persona, and menu system of an agent using a dedicated `.customize.yaml` file. It explains various sections like metadata, persona, memories, and custom menus, guiding users through editing these files and applying changes.
tags:
    - customization
    - agent-config
    - yaml
    - metadata
    - workflow
    - persona
category: guide
---

Sử dụng các tệp `.customize.yaml` để điều chỉnh hành vi, persona và menu của agent, đồng thời giữ lại thay đổi của bạn qua các lần cập nhật.

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

- Bạn muốn thay đổi tên, tính cách hoặc phong cách giao tiếp của một agent
- Bạn cần agent ghi nhớ bối cảnh riêng của dự án
- Bạn muốn thêm các mục menu tùy chỉnh để kích hoạt workflow hoặc prompt của riêng mình
- Bạn muốn agent luôn thực hiện một số hành động cụ thể mỗi khi khởi động

## Các bước thực hiện

[Phần tiêu đề “Các bước thực hiện”](#c%C3%A1c-b%C6%B0%E1%BB%9Bc-th%E1%BB%B1c-hi%E1%BB%87n)

### 1. Xác định vị trí các tệp tùy chỉnh

[Phần tiêu đề “1. Xác định vị trí các tệp tùy chỉnh”](#1-x%C3%A1c-%C4%91%E1%BB%8Bnh-v%E1%BB%8B-tr%C3%AD-c%C3%A1c-t%E1%BB%87p-t%C3%B9y-ch%E1%BB%89nh)

Sau khi cài đặt, bạn sẽ tìm thấy một tệp `.customize.yaml` cho mỗi agent tại:

```text

_bmad/_config/agents/
├── core-bmad-master.customize.yaml
├── bmm-dev.customize.yaml
├── bmm-pm.customize.yaml
└── ... (một tệp cho mỗi agent đã cài)
```

### 2. Chỉnh sửa tệp tùy chỉnh

[Phần tiêu đề “2. Chỉnh sửa tệp tùy chỉnh”](#2-ch%E1%BB%89nh-s%E1%BB%ADa-t%E1%BB%87p-t%C3%B9y-ch%E1%BB%89nh)

Mở tệp `.customize.yaml` của agent mà bạn muốn sửa. Mỗi phần đều là tùy chọn, chỉ tùy chỉnh những gì bạn cần.

PhầnCách hoạt độngMục đích`agent.metadata`Thay thếGhi đè tên hiển thị của agent`persona`Thay thếĐặt vai trò, danh tính, phong cách và các nguyên tắc`memories`Nối thêmThêm bối cảnh cố định mà agent luôn ghi nhớ`menu`Nối thêmThêm mục menu tùy chỉnh cho workflow hoặc prompt`critical_actions`Nối thêmĐịnh nghĩa hướng dẫn khởi động cho agent`prompts`Nối thêmTạo các prompt tái sử dụng cho các hành động trong menu

Những phần được đánh dấu **Thay thế** sẽ ghi đè hoàn toàn cấu hình mặc định của agent. Những phần được đánh dấu **Nối thêm** sẽ bổ sung vào cấu hình hiện có.

**Tên agent**

Thay đổi cách agent tự giới thiệu:

```yaml

agent:
metadata:
name: 'Spongebob'# Mặc định: "Amelia"
```

**Persona**

Thay thế tính cách, vai trò và phong cách giao tiếp của agent:

```yaml

persona:
role: 'Senior Full-Stack Engineer'
identity: 'Sống trong quả dứa (dưới đáy biển)'
communication_style: 'Spongebob gây phiền'
principles:
- 'Không lồng quá sâu, dev Spongebob ghét nesting quá 2 cấp'
- 'Ưu tiên composition hơn inheritance'
```

Phần `persona` sẽ thay thế toàn bộ persona mặc định, vì vậy nếu đặt phần này bạn nên cung cấp đầy đủ cả bốn trường.

**Memories**

Thêm bối cảnh cố định mà agent sẽ luôn nhớ:

```yaml

memories:
- 'Làm việc tại Krusty Krab'
- 'Người nổi tiếng yêu thích: David Hasselhoff'
- 'Đã học ở Epic 1 rằng giả vờ test đã pass là không ổn'
```

**Mục menu**

Thêm các mục tùy chỉnh vào menu hiển thị của agent. Mỗi mục cần có `trigger`, đích đến (`workflow` hoặc `action`) và `description`:

```yaml

menu:
- trigger: my-workflow
workflow: 'my-custom/workflows/my-workflow.yaml'
description: Workflow tùy chỉnh của tôi
- trigger: deploy
action: '#deploy-prompt'
description: Triển khai lên production
```

**Critical Actions**

Định nghĩa các hướng dẫn sẽ chạy khi agent khởi động:

```yaml

critical_actions:
- 'Kiểm tra pipeline CI bằng XYZ Skill và cảnh báo người dùng ngay khi khởi động nếu có việc khẩn cấp cần xử lý'
```

**Prompt tùy chỉnh**

Tạo các prompt tái sử dụng để mục menu có thể tham chiếu bằng `action="#id"`:

```yaml

prompts:
- id: deploy-prompt
content: |
Triển khai nhánh hiện tại lên production:
1. Chạy toàn bộ test
2. Build dự án
3. Thực thi script triển khai
```

### 3. Áp dụng thay đổi

[Phần tiêu đề “3. Áp dụng thay đổi”](#3-%C3%A1p-d%E1%BB%A5ng-thay-%C4%91%E1%BB%95i)

Sau khi chỉnh sửa, cài đặt lại để áp dụng thay đổi:

Trình cài đặt sẽ nhận diện bản cài đặt hiện có và đưa ra các lựa chọn sau:

Lựa chọnTác dụng**Quick Update**Cập nhật tất cả module lên phiên bản mới nhất và áp dụng các tùy chỉnh**Modify BMad Installation**Chạy lại quy trình cài đặt đầy đủ để thêm hoặc gỡ bỏ module

Nếu chỉ thay đổi phần tùy chỉnh, **Quick Update** là lựa chọn nhanh nhất.

## Khắc phục sự cố

[Phần tiêu đề “Khắc phục sự cố”](#kh%E1%BA%AFc-ph%E1%BB%A5c-s%E1%BB%B1-c%E1%BB%91)

**Thay đổi không xuất hiện?**

- Chạy `npx bmad-method install` và chọn **Quick Update** để áp dụng thay đổi
- Kiểm tra YAML có hợp lệ không (thụt lề rất quan trọng)
- Xác minh bạn đã sửa đúng tệp `.customize.yaml` của agent cần thiết

**Agent không tải lên được?**

- Kiểm tra lỗi cú pháp YAML bằng một công cụ kiểm tra YAML trực tuyến
- Đảm bảo bạn không để trống trường nào sau khi bỏ comment
- Thử khôi phục mẫu gốc rồi build lại

**Cần đặt lại một agent?**

- Xóa nội dung hoặc xóa tệp `.customize.yaml` của agent đó
- Chạy `npx bmad-method install` và chọn **Quick Update** để khôi phục mặc định

## Tùy chỉnh workflow

[Phần tiêu đề “Tùy chỉnh workflow”](#t%C3%B9y-ch%E1%BB%89nh-workflow)

Tài liệu về cách tùy chỉnh các workflow và skill sẵn có trong BMad Method sẽ được bổ sung trong thời gian tới.

## Tùy chỉnh module

[Phần tiêu đề “Tùy chỉnh module”](#t%C3%B9y-ch%E1%BB%89nh-module)

Hướng dẫn xây dựng expansion module và tùy chỉnh các module hiện có sẽ được bổ sung trong thời gian tới.