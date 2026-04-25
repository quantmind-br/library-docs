---
title: Quản lý Project Context
url: https://docs.bmad-method.org/vi-vn/how-to/project-context/
source: sitemap
fetched_at: 2026-04-08T11:32:15.733986349-03:00
rendered_js: false
word_count: 536
summary: Tài liệu này hướng dẫn cách tạo và sử dụng tệp `project-context.md` để đảm bảo các agent AI tuân thủ nhất quán về các quy tắc kỹ thuật, stack công nghệ, và quyết định kiến trúc của dự án qua mọi giai đoạn phát triển.
tags:
    - project-context
    - ai-agent-guidance
    - implementation-rules
    - architecture-documentation
    - codebase-pattern
category: guide
---

Sử dụng tệp `project-context.md` để đảm bảo các agent AI tuân theo ưu tiên kỹ thuật và quy tắc triển khai của dự án trong suốt mọi workflow. Để đảm bảo tệp này luôn sẵn có, bạn cũng có thể thêm dòng `Important project context and conventions are located in [path to project context]/project-context.md` vào file context của công cụ hoặc file always rules của bạn (như `AGENTS.md`).

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

- Bạn có các ưu tiên kỹ thuật rõ ràng trước khi bắt đầu làm kiến trúc
- Bạn đã hoàn thành kiến trúc và muốn ghi lại các quyết định để phục vụ triển khai
- Bạn đang làm việc với một codebase hiện có có những pattern đã ổn định
- Bạn thấy các agent đưa ra quyết định không nhất quán giữa các story

## Bước 1: Chọn cách tiếp cận

[Phần tiêu đề “Bước 1: Chọn cách tiếp cận”](#b%C6%B0%E1%BB%9Bc-1-ch%E1%BB%8Dn-c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn)

**Tự tạo bằng tay** - Phù hợp nhất khi bạn biết rõ cần tài liệu hóa quy tắc nào

**Tạo sau kiến trúc** - Phù hợp để ghi lại các quyết định đã được đưa ra trong giai đoạn solutioning

**Tạo cho dự án hiện có** - Phù hợp để khám phá pattern trong các codebase đã tồn tại

## Bước 2: Tạo tệp

[Phần tiêu đề “Bước 2: Tạo tệp”](#b%C6%B0%E1%BB%9Bc-2-t%E1%BA%A1o-t%E1%BB%87p)

### Lựa chọn A: Tạo thủ công

[Phần tiêu đề “Lựa chọn A: Tạo thủ công”](#l%E1%BB%B1a-ch%E1%BB%8Dn-a-t%E1%BA%A1o-th%E1%BB%A7-c%C3%B4ng)

Tạo tệp tại `_bmad-output/project-context.md`:

```bash

mkdir-p_bmad-output
touch_bmad-output/project-context.md
```

Thêm stack công nghệ và các quy tắc triển khai của bạn:

```markdown

---
project_name: 'MyProject'
user_name: 'YourName'
date: '2026-02-15'
sections_completed: ['technology_stack', 'critical_rules']
---
# Project Context for AI Agents
## Technology Stack & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand
- Testing: Vitest, Playwright
- Styling: Tailwind CSS
## Critical Implementation Rules
**TypeScript:**
- Strict mode enabled, no `any` types
- Use `interface` for public APIs, `type` for unions
**Code Organization:**
- Components in `/src/components/` with co-located tests
- API calls use `apiClient` singleton — never fetch directly
**Testing:**
- Unit tests focus on business logic
- Integration tests use MSW for API mocking
```

### Lựa chọn B: Tạo sau khi hoàn thành kiến trúc

[Phần tiêu đề “Lựa chọn B: Tạo sau khi hoàn thành kiến trúc”](#l%E1%BB%B1a-ch%E1%BB%8Dn-b-t%E1%BA%A1o-sau-khi-ho%C3%A0n-th%C3%A0nh-ki%E1%BA%BFn-tr%C3%BAc)

Chạy workflow trong một phiên chat mới:

```bash

bmad-generate-project-context
```

Workflow sẽ quét tài liệu kiến trúc và tệp dự án để tạo tệp context ghi lại các quyết định đã được đưa ra.

### Lựa chọn C: Tạo cho dự án hiện có

[Phần tiêu đề “Lựa chọn C: Tạo cho dự án hiện có”](#l%E1%BB%B1a-ch%E1%BB%8Dn-c-t%E1%BA%A1o-cho-d%E1%BB%B1-%C3%A1n-hi%E1%BB%87n-c%C3%B3)

Với các dự án hiện có, chạy:

```bash

bmad-generate-project-context
```

Workflow sẽ phân tích codebase để nhận diện quy ước, sau đó tạo tệp context để bạn xem lại và chỉnh sửa.

## Bước 3: Xác minh nội dung

[Phần tiêu đề “Bước 3: Xác minh nội dung”](#b%C6%B0%E1%BB%9Bc-3-x%C3%A1c-minh-n%E1%BB%99i-dung)

Xem lại tệp được tạo và đảm bảo nó ghi đúng:

- Các phiên bản công nghệ chính xác
- Đúng các quy ước thực tế của bạn (không phải các best practice chung chung)
- Các quy tắc giúp tránh những lỗi thường gặp
- Các pattern đặc thù framework

Chỉnh sửa thủ công để thêm phần còn thiếu hoặc loại bỏ những chỗ không chính xác.

## Bạn nhận được gì

[Phần tiêu đề “Bạn nhận được gì”](#b%E1%BA%A1n-nh%E1%BA%ADn-%C4%91%C6%B0%E1%BB%A3c-g%C3%AC)

Một tệp `project-context.md` sẽ:

- Đảm bảo tất cả agent tuân theo cùng một bộ quy ước
- Ngăn các quyết định không nhất quán giữa các story
- Ghi lại các quyết định kiến trúc cho giai đoạn triển khai
- Làm tài liệu tham chiếu cho các pattern và quy tắc của dự án

<!--THE END-->

- [**Giải thích về Project Context**](https://docs.bmad-method.org/vi-vn/explanation/project-context/) - Tìm hiểu sâu hơn cách nó hoạt động
- [**Bản đồ workflow**](https://docs.bmad-method.org/vi-vn/reference/workflow-map/) - Xem workflow nào sử dụng project context