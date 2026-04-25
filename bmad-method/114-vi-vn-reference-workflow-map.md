---
title: Workflow Map
url: https://docs.bmad-method.org/vi-vn/reference/workflow-map/
source: sitemap
fetched_at: 2026-04-08T11:32:33.763147571-03:00
rendered_js: false
word_count: 723
summary: This document details the BMad Method (BMM), a structured, multi-phase process designed to guide AI agent workflows from initial concept analysis through to final implementation by systematically building and passing context between sequential phases.
tags:
    - bmad-method
    - context-engineering
    - ai-agent
    - software-development
    - workflow-planning
    - process-guide
category: guide
---

BMad Method (BMM) là một module trong hệ sinh thái BMad, tập trung vào các thực hành tốt nhất của context engineering và lập kế hoạch. AI agent hoạt động hiệu quả nhất khi có ngữ cảnh rõ ràng và có cấu trúc. Hệ thống BMM xây dựng ngữ cảnh đó theo tiến trình qua 4 phase riêng biệt. Mỗi phase, cùng với nhiều workflow tùy chọn bên trong phase đó, tạo ra các tài liệu làm đầu vào cho phase kế tiếp, nhờ vậy agent luôn biết phải xây gì và vì sao.

Lý do và các khái niệm nền tảng ở đây đến từ các phương pháp agile đã được áp dụng rất thành công trong toàn ngành như một khung tư duy.

Nếu có lúc nào bạn không chắc nên làm gì, skill `bmad-help` sẽ giúp bạn giữ đúng hướng hoặc biết bước tiếp theo. Bạn vẫn có thể dùng trang này để tham chiếu, nhưng `bmad-help` mang tính tương tác đầy đủ và nhanh hơn nhiều nếu bạn đã cài BMad Method. Ngoài ra, nếu bạn đang dùng thêm các module mở rộng BMad Method hoặc các module bổ sung khác, `bmad-help` cũng sẽ phát triển theo để biết mọi thứ đang có sẵn và đưa ra lời khuyên tốt nhất tại thời điểm đó.

Lưu ý quan trọng cuối cùng: mọi workflow dưới đây đều có thể chạy trực tiếp bằng công cụ bạn chọn thông qua skill, hoặc bằng cách nạp agent trước rồi chọn mục tương ứng trong menu agent.

[Mở sơ đồ trong tab mới ↗](https://docs.bmad-method.org/workflow-map-diagram.html)

## Phase 1: Analysis (Tùy chọn)

[Phần tiêu đề “Phase 1: Analysis (Tùy chọn)”](#phase-1-analysis-t%C3%B9y-ch%E1%BB%8Dn)

Khám phá không gian vấn đề và xác nhận ý tưởng trước khi cam kết đi vào lập kế hoạch. [**Tìm hiểu từng công cụ làm gì và nên dùng khi nào**](https://docs.bmad-method.org/vi-vn/explanation/analysis-phase/).

WorkflowMục đíchTạo ra`bmad-brainstorming`Brainstorm ý tưởng dự án với sự điều phối của brainstorming coach`brainstorming-report.md``bmad-domain-research`, `bmad-market-research`, `bmad-technical-research`Xác thực giả định về thị trường, kỹ thuật hoặc miền nghiệp vụKết quả nghiên cứu`bmad-product-brief`Ghi lại tầm nhìn chiến lược — phù hợp nhất khi concept của bạn đã rõ`product-brief.md``bmad-prfaq`Working Backwards — stress-test và rèn sắc concept sản phẩm của bạn`prfaq-{project}.md`

## Phase 2: Planning

[Phần tiêu đề “Phase 2: Planning”](#phase-2-planning)

Xác định cần xây gì và xây cho ai.

WorkflowMục đíchTạo ra`bmad-create-prd`Xác định yêu cầu (FR/NFR)`PRD.md``bmad-create-ux-design`Thiết kế trải nghiệm người dùng khi UX là yếu tố quan trọng`ux-spec.md`

## Phase 3: Solutioning

[Phần tiêu đề “Phase 3: Solutioning”](#phase-3-solutioning)

Quyết định cách xây và chia nhỏ công việc thành stories.

WorkflowMục đíchTạo ra`bmad-create-architecture`Làm rõ các quyết định kỹ thuật`architecture.md` kèm ADR`bmad-create-epics-and-stories`Phân rã yêu cầu thành các phần việc có thể triển khaiCác file epic chứa stories`bmad-check-implementation-readiness`Cổng kiểm tra trước khi triển khaiQuyết định PASS/CONCERNS/FAIL

## Phase 4: Implementation

[Phần tiêu đề “Phase 4: Implementation”](#phase-4-implementation)

Xây dựng từng story một. Tự động hóa toàn bộ phase 4 sẽ sớm ra mắt.

WorkflowMục đíchTạo ra`bmad-sprint-planning`Khởi tạo theo dõi, thường chạy một lần mỗi dự án để sắp thứ tự chu trình dev`sprint-status.yaml``bmad-create-story`Chuẩn bị story tiếp theo cho implementation`story-[slug].md``bmad-dev-story`Triển khai storyCode chạy được + tests`bmad-code-review`Kiểm tra chất lượng phần triển khaiĐược duyệt hoặc yêu cầu thay đổi`bmad-correct-course`Xử lý thay đổi lớn giữa sprintKế hoạch cập nhật hoặc định tuyến lại`bmad-sprint-status`Theo dõi tiến độ sprint và trạng thái storyCập nhật trạng thái sprint`bmad-retrospective`Review sau khi hoàn tất epicBài học rút ra

## Quick Flow (Nhánh Song Song)

[Phần tiêu đề “Quick Flow (Nhánh Song Song)”](#quick-flow-nh%C3%A1nh-song-song)

Bỏ qua phase 1-3 đối với những việc nhỏ, rõ và đã hiểu đầy đủ.

WorkflowMục đíchTạo ra`bmad-quick-dev`Luồng nhanh hợp nhất — làm rõ yêu cầu, lập kế hoạch, triển khai, review và trình bày`spec-*.md` + mã nguồn

## Quản Lý Context

[Phần tiêu đề “Quản Lý Context”](#qu%E1%BA%A3n-l%C3%BD-context)

Mỗi tài liệu sẽ trở thành context cho phase tiếp theo. PRD cho architect biết những ràng buộc nào quan trọng. Architecture chỉ cho dev agent những pattern cần tuân theo. File story cung cấp context tập trung và đầy đủ cho việc triển khai. Nếu không có cấu trúc này, agent sẽ đưa ra quyết định thiếu nhất quán.

### Project Context

[Phần tiêu đề “Project Context”](#project-context)

**Cách tạo:**

- **Thủ công** — Tạo `_bmad-output/project-context.md` với stack công nghệ và các quy tắc triển khai của bạn
- **Tự sinh** — Chạy `bmad-generate-project-context` để sinh tự động từ architecture hoặc codebase

[**Tìm hiểu thêm về project-context.md**](https://docs.bmad-method.org/vi-vn/explanation/project-context/)