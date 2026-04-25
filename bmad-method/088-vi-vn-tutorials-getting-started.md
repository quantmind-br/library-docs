---
title: Bắt đầu
url: https://docs.bmad-method.org/vi-vn/tutorials/getting-started/
source: sitemap
fetched_at: 2026-04-08T11:32:37.196760162-03:00
rendered_js: false
word_count: 1241
summary: This guide teaches users how to speed up software development using AI-operated workflows and specialized agents. It details a structured, multi-phase process—from initial concept brainstorming through planning, solutioning, and final implementation—using the BMad Method framework.
tags:
    - ai-workflows
    - software-development
    - bmad-method
    - agent-assistance
    - product-planning
    - development-lifecycle
category: guide
---

Xây dựng phần mềm nhanh hơn bằng các workflow vận hành bởi AI, với những agent chuyên biệt hướng dẫn bạn qua các bước lập kế hoạch, kiến trúc và triển khai.

## Bạn Sẽ Học Được Gì

[Phần tiêu đề “Bạn Sẽ Học Được Gì”](#b%E1%BA%A1n-s%E1%BA%BD-h%E1%BB%8Dc-%C4%91%C6%B0%E1%BB%A3c-g%C3%AC)

- Cài đặt và khởi tạo BMad Method cho một dự án mới
- Dùng **BMad-Help** — trợ lý thông minh biết bước tiếp theo bạn nên làm gì
- Chọn nhánh lập kế hoạch phù hợp với quy mô dự án
- Đi qua các phase từ yêu cầu đến code chạy được
- Sử dụng agent và workflow hiệu quả

## Làm Quen Với BMad-Help: Người Dẫn Đường Thông Minh Của Bạn

[Phần tiêu đề “Làm Quen Với BMad-Help: Người Dẫn Đường Thông Minh Của Bạn”](#l%C3%A0m-quen-v%E1%BB%9Bi-bmad-help-ng%C6%B0%E1%BB%9Di-d%E1%BA%ABn-%C4%91%C6%B0%E1%BB%9Dng-th%C3%B4ng-minh-c%E1%BB%A7a-b%E1%BA%A1n)

**BMad-Help là cách nhanh nhất để bắt đầu với BMad.** Bạn không cần phải nhớ workflow hay phase nào cả, chỉ cần hỏi, và BMad-Help sẽ:

- **Kiểm tra dự án của bạn** để xem những gì đã hoàn thành
- **Hiển thị các lựa chọn** dựa trên những module bạn đã cài
- **Đề xuất bước tiếp theo** — bao gồm cả tác vụ bắt buộc đầu tiên
- **Trả lời câu hỏi** như “Tôi có ý tưởng cho một sản phẩm SaaS, tôi nên bắt đầu từ đâu?”

### Cách Dùng BMad-Help

[Phần tiêu đề “Cách Dùng BMad-Help”](#c%C3%A1ch-d%C3%B9ng-bmad-help)

Chạy trong AI IDE của bạn bằng cách gọi skill:

Hoặc ghép cùng câu hỏi để nhận hướng dẫn có ngữ cảnh:

```text

bmad-help I have an idea for a SaaS product, I already know all the features I want. where do I get started?
```

BMad-Help sẽ trả lời:

- Điều gì được khuyến nghị trong tình huống của bạn
- Tác vụ bắt buộc đầu tiên là gì
- Phần còn lại của quy trình sẽ trông như thế nào

### Nó Cũng Điều Khiển Workflow

[Phần tiêu đề “Nó Cũng Điều Khiển Workflow”](#n%C3%B3-c%C5%A9ng-%C4%91i%E1%BB%81u-khi%E1%BB%83n-workflow)

BMad-Help không chỉ trả lời câu hỏi — **nó còn tự động chạy ở cuối mỗi workflow** để cho bạn biết chính xác bước tiếp theo cần làm là gì. Không phải đoán, không phải lục tài liệu, chỉ có chỉ dẫn rõ ràng về workflow bắt buộc tiếp theo.

BMad giúp bạn xây dựng phần mềm thông qua các workflow có hướng dẫn với những AI agent chuyên biệt. Quy trình gồm bốn phase:

PhaseTênĐiều xảy ra1AnalysisBrainstorming, nghiên cứu, product brief hoặc PRFAQ *(tùy chọn)*2PlanningTạo tài liệu yêu cầu (PRD hoặc spec)3SolutioningThiết kế kiến trúc *(chỉ dành cho BMad Method/Enterprise)*4ImplementationXây dựng theo từng epic, từng story

[**Mở Workflow Map**](https://docs.bmad-method.org/vi-vn/reference/workflow-map/) để khám phá các phase, workflow và cách quản lý context.

Dựa trên độ phức tạp của dự án, BMad cung cấp ba nhánh lập kế hoạch:

NhánhPhù hợp nhất vớiTài liệu được tạo**Quick Flow**Sửa lỗi, tính năng đơn giản, phạm vi rõ ràng (1-15 story)Chỉ spec**BMad Method**Sản phẩm, nền tảng, tính năng phức tạp (10-50+ story)PRD + Architecture + UX**Enterprise**Yêu cầu tuân thủ, hệ thống đa tenant (30+ story)PRD + Architecture + Security + DevOps

Mở terminal trong thư mục dự án và chạy:

Nếu bạn muốn dùng bản prerelease mới nhất thay vì kênh release mặc định, hãy dùng `npx bmad-method@next install`.

Khi được hỏi chọn module, hãy chọn **BMad Method**.

Trình cài đặt sẽ tạo hai thư mục:

- `_bmad/` — agents, workflows, tasks và cấu hình
- `_bmad-output/` — hiện tại để trống, nhưng đây là nơi các artifact của bạn sẽ được lưu

## Bước 1: Tạo Kế Hoạch

[Phần tiêu đề “Bước 1: Tạo Kế Hoạch”](#b%C6%B0%E1%BB%9Bc-1-t%E1%BA%A1o-k%E1%BA%BF-ho%E1%BA%A1ch)

Đi qua các phase 1-3. **Dùng chat mới cho từng workflow.**

### Phase 1: Analysis (Tùy chọn)

[Phần tiêu đề “Phase 1: Analysis (Tùy chọn)”](#phase-1-analysis-t%C3%B9y-ch%E1%BB%8Dn)

Tất cả workflow trong phase này đều là tùy chọn. [**Chưa chắc nên dùng cái nào?**](https://docs.bmad-method.org/vi-vn/explanation/analysis-phase/)

- **brainstorming** (`bmad-brainstorming`) — Gợi ý ý tưởng có hướng dẫn
- **research** (`bmad-market-research` / `bmad-domain-research` / `bmad-technical-research`) — Nghiên cứu thị trường, miền nghiệp vụ và kỹ thuật
- **product-brief** (`bmad-product-brief`) — Tài liệu nền tảng được khuyến nghị khi concept của bạn đã rõ
- **prfaq** (`bmad-prfaq`) — Bài kiểm tra Working Backwards để stress-test và rèn sắc concept sản phẩm của bạn

### Phase 2: Planning (Bắt buộc)

[Phần tiêu đề “Phase 2: Planning (Bắt buộc)”](#phase-2-planning-b%E1%BA%AFt-bu%E1%BB%99c)

**Với nhánh BMad Method và Enterprise:**

1. Gọi **PM agent** (`bmad-agent-pm`) trong một chat mới
2. Chạy workflow `bmad-create-prd` (`bmad-create-prd`)
3. Kết quả: `PRD.md`

**Với nhánh Quick Flow:**

- Chạy `bmad-quick-dev` — workflow này gộp cả planning và implementation trong một lần, nên bạn có thể chuyển thẳng sang triển khai

### Phase 3: Solutioning (BMad Method/Enterprise)

[Phần tiêu đề “Phase 3: Solutioning (BMad Method/Enterprise)”](#phase-3-solutioning-bmad-methodenterprise)

**Tạo Architecture**

1. Gọi **Architect agent** (`bmad-agent-architect`) trong một chat mới
2. Chạy `bmad-create-architecture` (`bmad-create-architecture`)
3. Kết quả: tài liệu kiến trúc chứa các quyết định kỹ thuật

**Tạo Epics và Stories**

1. Gọi **PM agent** (`bmad-agent-pm`) trong một chat mới
2. Chạy `bmad-create-epics-and-stories` (`bmad-create-epics-and-stories`)
3. Workflow sẽ dùng cả PRD lẫn Architecture để tạo story có đủ ngữ cảnh kỹ thuật

**Kiểm tra mức sẵn sàng để triển khai** *(Rất nên dùng)*

1. Gọi **Architect agent** (`bmad-agent-architect`) trong một chat mới
2. Chạy `bmad-check-implementation-readiness` (`bmad-check-implementation-readiness`)
3. Xác nhận tính nhất quán giữa toàn bộ tài liệu lập kế hoạch

## Bước 2: Xây Dựng Dự Án

[Phần tiêu đề “Bước 2: Xây Dựng Dự Án”](#b%C6%B0%E1%BB%9Bc-2-x%C3%A2y-d%E1%BB%B1ng-d%E1%BB%B1-%C3%A1n)

Sau khi lập kế hoạch xong, chuyển sang implementation. **Mỗi workflow nên chạy trong một chat mới.**

### Khởi Tạo Sprint Planning

[Phần tiêu đề “Khởi Tạo Sprint Planning”](#kh%E1%BB%9Fi-t%E1%BA%A1o-sprint-planning)

Gọi **Developer agent** (`bmad-agent-dev`) và chạy `bmad-sprint-planning` (`bmad-sprint-planning`). Workflow này sẽ tạo `sprint-status.yaml` để theo dõi toàn bộ epic và story.

### Chu Trình Xây Dựng

[Phần tiêu đề “Chu Trình Xây Dựng”](#chu-tr%C3%ACnh-x%C3%A2y-d%E1%BB%B1ng)

Với mỗi story, lặp lại chu trình này trong chat mới:

BướcAgentWorkflowLệnhMục đích1DEV`bmad-create-story``bmad-create-story`Tạo file story từ epic2DEV`bmad-dev-story``bmad-dev-story`Triển khai story3DEV`bmad-code-review``bmad-code-review`Kiểm tra chất lượng *(khuyến nghị)*

Sau khi hoàn tất tất cả story trong một epic, hãy gọi **Developer agent** (`bmad-agent-dev`) và chạy `bmad-retrospective` (`bmad-retrospective`).

## Bạn Đã Hoàn Thành Những Gì

[Phần tiêu đề “Bạn Đã Hoàn Thành Những Gì”](#b%E1%BA%A1n-%C4%91%C3%A3-ho%C3%A0n-th%C3%A0nh-nh%E1%BB%AFng-g%C3%AC)

Bạn đã nắm được nền tảng để xây dựng với BMad:

- Đã cài BMad và cấu hình cho IDE của bạn
- Đã khởi tạo dự án theo nhánh lập kế hoạch phù hợp
- Đã tạo các tài liệu lập kế hoạch (PRD, Architecture, Epics và Stories)
- Đã hiểu chu trình triển khai trong implementation

Dự án của bạn bây giờ sẽ có dạng:

```text

your-project/
├── _bmad/                                   # Cấu hình BMad
├── _bmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md                           # Tài liệu yêu cầu của bạn
│   │   ├── architecture.md                  # Các quyết định kỹ thuật
│   │   └── epics/                           # Các file epic và story
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml               # Theo dõi sprint
│   └── project-context.md                   # Quy tắc triển khai (tùy chọn)
└── ...
```

WorkflowLệnhAgentMục đích**`bmad-help`** ⭐`bmad-help`Bất kỳ**Người dẫn đường thông minh của bạn — hỏi gì cũng được!**`bmad-create-prd``bmad-create-prd`PMTạo tài liệu yêu cầu sản phẩm`bmad-create-architecture``bmad-create-architecture`ArchitectTạo tài liệu kiến trúc`bmad-generate-project-context``bmad-generate-project-context`AnalystTạo file project context`bmad-create-epics-and-stories``bmad-create-epics-and-stories`PMPhân rã PRD thành epics`bmad-check-implementation-readiness``bmad-check-implementation-readiness`ArchitectKiểm tra độ nhất quán của kế hoạch`bmad-sprint-planning``bmad-sprint-planning`DEVKhởi tạo theo dõi sprint`bmad-create-story``bmad-create-story`DEVTạo file story`bmad-dev-story``bmad-dev-story`DEVTriển khai một story`bmad-code-review``bmad-code-review`DEVReview phần code đã triển khai

## Câu Hỏi Thường Gặp

[Phần tiêu đề “Câu Hỏi Thường Gặp”](#c%C3%A2u-h%E1%BB%8Fi-th%C6%B0%E1%BB%9Dng-g%E1%BA%B7p)

**Lúc nào cũng cần kiến trúc à?** Chỉ với nhánh BMad Method và Enterprise. Quick Flow bỏ qua bước kiến trúc và chuyển thẳng từ spec sang implementation.

**Tôi có thể đổi kế hoạch về sau không?** Có. Workflow `bmad-correct-course` (`bmad-correct-course`) xử lý thay đổi phạm vi giữa chừng.

**Nếu tôi muốn brainstorming trước thì sao?** Gọi Analyst agent (`bmad-agent-analyst`) và chạy `bmad-brainstorming` (`bmad-brainstorming`) trước khi bắt đầu PRD.

**Tôi có cần tuân theo đúng thứ tự tuyệt đối không?** Không hẳn. Khi đã quen flow, bạn có thể chạy workflow trực tiếp bằng bảng Tra Cứu Nhanh ở trên.

- **Trong workflow** — Các agent sẽ hướng dẫn bạn bằng câu hỏi và giải thích
- **Cộng đồng** — [Discord](https://discord.gg/gk8jAdXWmj) (#bmad-method-help, #report-bugs-and-issues)

## Những Điểm Cần Ghi Nhớ

[Phần tiêu đề “Những Điểm Cần Ghi Nhớ”](#nh%E1%BB%AFng-%C4%91i%E1%BB%83m-c%E1%BA%A7n-ghi-nh%E1%BB%9B)

Sẵn sàng bắt đầu chưa? Hãy cài BMad, gọi `bmad-help`, và để người dẫn đường thông minh của bạn đưa bạn đi tiếp.