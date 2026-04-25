---
title: Project Context
url: https://docs.bmad-method.org/vi-vn/explanation/project-context/
source: sitemap
fetched_at: 2026-04-08T11:31:59.748058951-03:00
rendered_js: false
word_count: 951
summary: This document explains the purpose and usage of 'project-context.md', a crucial file that acts as a project's constitution for AI agents, ensuring code generation remains consistent by documenting technical rules, patterns, and best practices.
tags:
    - ai-agent
    - code-generation
    - best-practices
    - technical-rules
    - llm-guidance
    - project-context
category: guide
---

Tệp `project-context.md` là kim chỉ nam cho việc triển khai của các agent AI trong dự án của bạn. Tương tự như một “bản hiến pháp” trong các hệ thống phát triển khác, nó ghi lại các quy tắc, pattern và ưu tiên giúp việc sinh mã được nhất quán trong mọi workflow.

Các agent AI liên tục đưa ra quyết định triển khai - theo pattern nào, tổ chức code ra sao, dùng quy ước gì. Nếu không có hướng dẫn rõ ràng, chúng có thể:

- Làm theo best practice chung chung không khớp với codebase của bạn
- Đưa ra quyết định không nhất quán giữa các story
- Bỏ sót yêu cầu hoặc ràng buộc đặc thù của dự án

Tệp `project-context.md` giải quyết vấn đề này bằng cách tài liệu hóa những gì agent cần biết trong định dạng ngắn gọn, tối ưu cho LLM.

## Nó hoạt động như thế nào

[Phần tiêu đề “Nó hoạt động như thế nào”](#n%C3%B3-ho%E1%BA%A1t-%C4%91%E1%BB%99ng-nh%C6%B0-th%E1%BA%BF-n%C3%A0o)

Mỗi workflow triển khai đều tự động nạp `project-context.md` nếu tệp tồn tại. Workflow architect cũng nạp tệp này để tôn trọng các ưu tiên kỹ thuật của bạn khi thiết kế kiến trúc.

**Được nạp bởi các workflow sau:**

- `bmad-create-architecture` - tôn trọng ưu tiên kỹ thuật trong giai đoạn solutioning
- `bmad-create-story` - đưa pattern của dự án vào quá trình tạo story
- `bmad-dev-story` - định hướng các quyết định triển khai
- `bmad-code-review` - đối chiếu với tiêu chuẩn của dự án
- `bmad-quick-dev` - áp dụng pattern khi triển khai các spec
- `bmad-sprint-planning`, `bmad-retrospective`, `bmad-correct-course` - cung cấp bối cảnh cấp dự án

## Khi nào nên tạo

[Phần tiêu đề “Khi nào nên tạo”](#khi-n%C3%A0o-n%C3%AAn-t%E1%BA%A1o)

Tệp `project-context.md` hữu ích ở bất kỳ giai đoạn nào của dự án:

Tình huốngKhi nào nên tạoMục đích**Dự án mới, trước kiến trúc**Tạo thủ công, trước `bmad-create-architecture`Ghi lại ưu tiên kỹ thuật để architect tôn trọng**Dự án mới, sau kiến trúc**Qua `bmad-generate-project-context` hoặc tạo thủ côngGhi lại quyết định kiến trúc cho các agent triển khai**Dự án hiện có**Qua `bmad-generate-project-context`Khám phá pattern hiện có để agent theo đúng quy ước**Dự án Quick Flow**Trước hoặc trong `bmad-quick-dev`Đảm bảo triển khai nhanh vẫn tôn trọng pattern của bạn

## Nội dung cần có trong tệp

[Phần tiêu đề “Nội dung cần có trong tệp”](#n%E1%BB%99i-dung-c%E1%BA%A7n-c%C3%B3-trong-t%E1%BB%87p)

Tệp này có hai phần chính:

### Technology Stack & Versions

[Phần tiêu đề “Technology Stack & Versions”](#technology-stack--versions)

Ghi lại framework, ngôn ngữ và công cụ dự án đang dùng, kèm phiên bản cụ thể:

```markdown

## Technology Stack & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand (không dùng Redux)
- Testing: Vitest, Playwright, MSW
- Styling: Tailwind CSS với custom design tokens
```

### Critical Implementation Rules

[Phần tiêu đề “Critical Implementation Rules”](#critical-implementation-rules)

Ghi lại những pattern và quy ước mà agent dễ bỏ sót nếu chỉ đọc qua code:

```markdown

## Critical Implementation Rules
**TypeScript Configuration:**
- Bật strict mode - không dùng `any` nếu chưa có phê duyệt rõ ràng
- Dùng `interface` cho public API, `type` cho union/intersection
**Code Organization:**
- Components đặt trong `/src/components/` và để `.test.tsx` cùng chỗ
- Utilities đặt trong `/src/lib/` cho các hàm pure có thể tái sử dụng
- Lời gọi API phải dùng `apiClient` singleton - không fetch trực tiếp
**Testing Patterns:**
- Unit test tập trung vào business logic, không soi chi tiết implementation
- Integration test dùng MSW để mock API responses
- E2E test chỉ bao phủ các user journey quan trọng
**Framework-Specific:**
- Mọi thao tác async dùng wrapper `handleError` để xử lý lỗi nhất quán
- Feature flags được truy cập qua `featureFlag()` từ `@/lib/flags`
- Route mới theo file-based routing pattern trong `/src/app/`
```

Hãy tập trung vào những gì **không hiển nhiên** - những điều agent khó suy ra chỉ từ một vài đoạn code. Không cần ghi lại các thực hành tiêu chuẩn áp dụng mọi nơi.

Bạn có ba lựa chọn:

Tạo tệp tại `_bmad-output/project-context.md` và thêm các quy tắc của bạn:

```bash

# Trong thư mục gốc của dự án
mkdir-p_bmad-output
touch_bmad-output/project-context.md
```

Sửa tệp để thêm stack công nghệ và quy tắc triển khai. Workflow architect và implementation sẽ tự động tìm và nạp nó.

### Tạo sau khi hoàn thành kiến trúc

[Phần tiêu đề “Tạo sau khi hoàn thành kiến trúc”](#t%E1%BA%A1o-sau-khi-ho%C3%A0n-th%C3%A0nh-ki%E1%BA%BFn-tr%C3%BAc)

Chạy workflow `bmad-generate-project-context` sau khi bạn hoàn tất kiến trúc:

```bash

bmad-generate-project-context
```

Nó sẽ quét tài liệu kiến trúc và tệp dự án để tạo tệp context ghi lại các quyết định đã được đưa ra.

### Tạo cho dự án hiện có

[Phần tiêu đề “Tạo cho dự án hiện có”](#t%E1%BA%A1o-cho-d%E1%BB%B1-%C3%A1n-hi%E1%BB%87n-c%C3%B3)

Với dự án hiện có, chạy `bmad-generate-project-context` để khám phá pattern sẵn có:

```bash

bmad-generate-project-context
```

Workflow sẽ phân tích codebase để nhận diện quy ước, sau đó tạo tệp context cho bạn xem lại và tinh chỉnh.

## Vì sao nó quan trọng

[Phần tiêu đề “Vì sao nó quan trọng”](#v%C3%AC-sao-n%C3%B3-quan-tr%E1%BB%8Dng)

Nếu không có `project-context.md`, các agent sẽ tự đưa ra giả định có thể không phù hợp với dự án:

Không có contextCó contextDùng pattern chung chungTheo đúng quy ước đã được xác lậpPhong cách không nhất quán giữa các storyTriển khai nhất quánCó thể bỏ sót ràng buộc đặc thùTôn trọng đầy đủ yêu cầu kỹ thuậtMỗi agent tự quyết địnhTất cả agent canh hàng theo cùng quy tắc

Điều này đặc biệt quan trọng với:

- **Quick Flow** - bỏ qua PRD và kiến trúc, nên tệp context lấp đầy khoảng trống
- **Dự án theo nhóm** - đảm bảo tất cả agent theo cùng tiêu chuẩn
- **Dự án hiện có** - tránh phá vỡ các pattern đã ổn định

## Chỉnh sửa và cập nhật

[Phần tiêu đề “Chỉnh sửa và cập nhật”](#ch%E1%BB%89nh-s%E1%BB%ADa-v%C3%A0-c%E1%BA%ADp-nh%E1%BA%ADt)

Tệp `project-context.md` là tài liệu sống. Hãy cập nhật khi:

- Quyết định kiến trúc thay đổi
- Có quy ước mới được thiết lập
- Pattern tiến hóa trong quá trình triển khai
- Bạn nhận ra lỗ hổng qua hành vi của agent

Bạn có thể sửa thủ công bất kỳ lúc nào, hoặc chạy lại `bmad-generate-project-context` để cập nhật sau các thay đổi lớn.