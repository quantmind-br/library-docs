---
title: Ngăn xung đột giữa các agent
url: https://docs.bmad-method.org/vi-vn/explanation/preventing-agent-conflicts/
source: sitemap
fetched_at: 2026-04-08T11:31:57.291477571-03:00
rendered_js: false
word_count: 515
summary: Tài liệu này giải thích cách kiến trúc hệ thống đóng vai trò là bối cảnh chung để ngăn chặn các xung đột kỹ thuật phát sinh khi nhiều agent AI cùng phát triển. Nó nhấn mạnh tầm quan trọng của việc sử dụng ADR, tiêu chuẩn hóa quy ước và tài liệu hóa rõ ràng các quyết định về API, cơ sở dữ liệu và quản lý state.
tags:
    - system-architecture
    - conflict-prevention
    - adr-documentation
    - technical-standards
    - ai-development
    - design-patterns
category: guide
---

Khi nhiều agent AI cùng triển khai các phần khác nhau của hệ thống, chúng có thể đưa ra các quyết định kỹ thuật mâu thuẫn nhau. Tài liệu kiến trúc ngăn điều đó bằng cách thiết lập các tiêu chuẩn dùng chung.

## Các kiểu xung đột phổ biến

[Phần tiêu đề “Các kiểu xung đột phổ biến”](#c%C3%A1c-ki%E1%BB%83u-xung-%C4%91%E1%BB%99t-ph%E1%BB%95-bi%E1%BA%BFn)

### Xung đột về phong cách API

[Phần tiêu đề “Xung đột về phong cách API”](#xung-%C4%91%E1%BB%99t-v%E1%BB%81-phong-c%C3%A1ch-api)

Không có kiến trúc:

- Agent A dùng REST với `/users/{id}`
- Agent B dùng GraphQL mutations
- Kết quả: pattern API không nhất quán, người dùng API bị rối

Có kiến trúc:

- ADR quy định: “Dùng GraphQL cho mọi giao tiếp client-server”
- Tất cả agent theo cùng một mẫu

### Xung đột về thiết kế cơ sở dữ liệu

[Phần tiêu đề “Xung đột về thiết kế cơ sở dữ liệu”](#xung-%C4%91%E1%BB%99t-v%E1%BB%81-thi%E1%BA%BFt-k%E1%BA%BF-c%C6%A1-s%E1%BB%9F-d%E1%BB%AF-li%E1%BB%87u)

Không có kiến trúc:

- Agent A dùng tên cột theo snake\_case
- Agent B dùng camelCase
- Kết quả: schema không nhất quán, truy vấn khó hiểu

Có kiến trúc:

- Tài liệu standards quy định quy ước đặt tên
- Tất cả agent theo cùng một pattern

### Xung đột về quản lý state

[Phần tiêu đề “Xung đột về quản lý state”](#xung-%C4%91%E1%BB%99t-v%E1%BB%81-qu%E1%BA%A3n-l%C3%BD-state)

Không có kiến trúc:

- Agent A dùng Redux cho global state
- Agent B dùng React Context
- Kết quả: nhiều cách quản lý state song song, độ phức tạp tăng cao

Có kiến trúc:

- ADR quy định cách quản lý state
- Tất cả agent triển khai thống nhất

## Kiến trúc ngăn xung đột bằng cách nào

[Phần tiêu đề “Kiến trúc ngăn xung đột bằng cách nào”](#ki%E1%BA%BFn-tr%C3%BAc-ng%C4%83n-xung-%C4%91%E1%BB%99t-b%E1%BA%B1ng-c%C3%A1ch-n%C3%A0o)

### 1. Quyết định rõ ràng thông qua ADR

[Phần tiêu đề “1. Quyết định rõ ràng thông qua ADR”](#1-quy%E1%BA%BFt-%C4%91%E1%BB%8Bnh-r%C3%B5-r%C3%A0ng-th%C3%B4ng-qua-adr)

Mỗi lựa chọn công nghệ quan trọng đều được ghi lại với:

- Context (vì sao quyết định này quan trọng)
- Các lựa chọn đã cân nhắc (có những phương án nào)
- Quyết định (ta đã chọn gì)
- Lý do (tại sao lại chọn như vậy)
- Hệ quả (các đánh đổi được chấp nhận)

### 2. Hướng dẫn riêng cho FR/NFR

[Phần tiêu đề “2. Hướng dẫn riêng cho FR/NFR”](#2-h%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-ri%C3%AAng-cho-frnfr)

Kiến trúc ánh xạ mỗi functional requirement sang cách tiếp cận kỹ thuật:

- FR-001: User Management → GraphQL mutations
- FR-002: Mobile App → Truy vấn tối ưu

### 3. Tiêu chuẩn và quy ước

[Phần tiêu đề “3. Tiêu chuẩn và quy ước”](#3-ti%C3%AAu-chu%E1%BA%A9n-v%C3%A0-quy-%C6%B0%E1%BB%9Bc)

Tài liệu hóa rõ ràng về:

- Cấu trúc thư mục
- Quy ước đặt tên
- Cách tổ chức code
- Pattern kiểm thử

## Kiến trúc như một bối cảnh dùng chung

[Phần tiêu đề “Kiến trúc như một bối cảnh dùng chung”](#ki%E1%BA%BFn-tr%C3%BAc-nh%C6%B0-m%E1%BB%99t-b%E1%BB%91i-c%E1%BA%A3nh-d%C3%B9ng-chung)

Hãy xem kiến trúc là bối cảnh dùng chung mà tất cả agent đều đọc trước khi triển khai:

```text

PRD: "Cần xây gì"
↓
Kiến trúc: "Xây như thế nào"
↓
Agent A đọc kiến trúc → triển khai Epic 1
Agent B đọc kiến trúc → triển khai Epic 2
Agent C đọc kiến trúc → triển khai Epic 3
↓
Kết quả: Triển khai nhất quán
```

## Các chủ đề ADR quan trọng

[Phần tiêu đề “Các chủ đề ADR quan trọng”](#c%C3%A1c-ch%E1%BB%A7-%C4%91%E1%BB%81-adr-quan-tr%E1%BB%8Dng)

Những quyết định phổ biến giúp tránh xung đột:

Chủ đềVí dụ quyết địnhAPI StyleGraphQL hay REST hay gRPCDatabasePostgreSQL hay MongoDBAuthJWT hay SessionState ManagementRedux hay Context hay ZustandStylingCSS Modules hay Tailwind hay Styled ComponentsTestingJest + Playwright hay Vitest + Cypress

## Anti-pattern cần tránh

[Phần tiêu đề “Anti-pattern cần tránh”](#anti-pattern-c%E1%BA%A7n-tr%C3%A1nh)