---
title: Các Tùy Chọn Kiểm Thử
url: https://docs.bmad-method.org/vi-vn/reference/testing/
source: sitemap
fetched_at: 2026-04-08T11:32:31.377602613-03:00
rendered_js: false
word_count: 983
summary: 'This document compares two testing approaches from BMad: the built-in QA workflow for quick, maintainable tests in small to medium projects, and the Module Test Architect (TEA) for complex enterprise environments requiring deep strategy, risk-based planning, and traceability.'
tags:
    - qa-testing
    - test-strategy
    - enterprise-testing
    - workflow-comparison
    - api-e2e-testing
    - risk-management
category: guide
---

BMad cung cấp hai hướng kiểm thử: workflow QA tích hợp sẵn để tạo test nhanh và module Test Architect có thể cài thêm cho chiến lược kiểm thử c��p doanh nghiệp.

## Nên Dùng Cái Nào?

[Phần tiêu đề “Nên Dùng Cái Nào?”](#n%C3%AAn-d%C3%B9ng-c%C3%A1i-n%C3%A0o)

Yếu tốQA tích hợp sẵnModule TEA**Phù hợp nhất với**Dự án nhỏ-trung bình, cần bao phủ nhanhDự án lớn, miền nghiệp vụ bị ràng buộc hoặc phức tạp**Thiết lập**Không cần cài thêm, đã có sẵn trong BMMCài riêng qua `npx bmad-method install`**Cách tiếp cận**Tạo test nhanh, lặp tinh chỉnh sauLập kế hoạch trước rồi mới tạo test có truy vết**Loại test**API và E2EAPI, E2E, ATDD, NFR và nhiều loại khác**Chiến lược**Happy path + edge case quan trọngƯu tiên theo rủi ro (P0-P3)**Số workflow**1 (Automate)9 (design, ATDD, automate, review, trace và các workflow khác)

## Workflow QA Tích Hợp Sẵn

[Phần tiêu đề “Workflow QA Tích Hợp Sẵn”](#workflow-qa-t%C3%ADch-h%E1%BB%A3p-s%E1%BA%B5n)

Workflow QA tích hợp sẵn (`bmad-qa-generate-e2e-tests`) nằm trong module BMM (Agile suite), khả dụng thông qua Developer agent. Nó tạo test chạy được rất nhanh bằng framework kiểm thử hiện có của dự án, không cần thêm cấu hình hay bước cài đặt bổ sung.

**Trigger:** `QA` (thông qua Developer agent) hoặc `bmad-qa-generate-e2e-tests`

### Workflow Làm Gì

[Phần tiêu đề “Workflow Làm Gì”](#workflow-l%C3%A0m-g%C3%AC)

Workflow QA (Automate) gồm năm bước:

1. **Phát hiện framework test** — quét `package.json` và các file test hiện có để nhận ra framework của bạn như Jest, Vitest, Playwright, Cypress hoặc bất kỳ runner tiêu chuẩn nào. Nếu chưa có gì, nó sẽ phân tích stack dự án và đề xuất một lựa chọn.
2. **Xác định tính năng** — hỏi cần kiểm thử phần nào hoặc tự khám phá các tính năng trong codebase.
3. **Tạo API tests** — bao phủ status code, cấu trúc phản hồi, happy path và 1-2 trường hợp lỗi.
4. **Tạo E2E tests** — bao phủ workflow người dùng bằng semantic locator và assertion trên kết quả nhìn thấy được.
5. **Chạy và xác minh** — thực thi test vừa tạo và sửa lỗi hỏng ngay lập tức.

Workflow tạo một bản tóm tắt kiểm thử và lưu nó vào thư mục implementation artifacts của dự án.

Các test được tạo theo triết lý “đơn giản và dễ bảo trì”:

- **Chỉ dùng API chuẩn của framework** — không kéo thêm utility ngoài hay abstraction tùy chỉnh
- **Semantic locator** cho UI test — dùng role, label, text thay vì CSS selector
- **Test độc lập** — không phụ thuộc thứ tự chạy
- **Không hardcode wait hoặc sleep**
- **Mô tả rõ ràng** để test cũng đóng vai trò tài liệu tính năng

### Khi Nào Nên Dùng QA Tích Hợp S���n

[Phần tiêu đề “Khi Nào Nên Dùng QA Tích Hợp S���n”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng-qa-t%C3%ADch-h%E1%BB%A3p-sn)

- Cần bao phủ test nhanh cho một tính năng mới hoặc hiện có
- Muốn tự động hóa kiểm thử thân thiện với người mới mà không cần thiết lập phức tạp
- Muốn các pattern test chuẩn mà lập trình viên nào cũng đọc và bảo trì được
- Dự án nhỏ-trung bình, nơi chiến lược kiểm thử toàn diện là không cần thiết

## Module Test Architect (TEA)

[Phần tiêu đề “Module Test Architect (TEA)”](#module-test-architect-tea)

TEA là một module độc lập cung cấp agent chuyên gia Murat cùng chín workflow có cấu trúc cho kiểm thử cấp doanh nghiệp. Nó vượt ra ngoài việc tạo test để bao gồm chiến lược kiểm thử, lập kế hoạch theo rủi ro, quality gate và truy vết yêu cầu.

- **Tài liệu:** [TEA Module Docs](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)
- **Cài đặt:** `npx bmad-method install` rồi chọn module TEA
- **npm:** [`bmad-method-test-architecture-enterprise`](https://www.npmjs.com/package/bmad-method-test-architecture-enterprise)

### TEA Cung Cấp Gì

[Phần tiêu đề “TEA Cung Cấp Gì”](#tea-cung-c%E1%BA%A5p-g%C3%AC)

WorkflowMục đíchTest DesignTạo chiến lược kiểm thử toàn diện gắn với yêu cầuATDDPhát triển hướng acceptance test với tiêu chí của stakeholderAutomateTạo test bằng pattern và utility nâng caoTest ReviewKiểm tra chất lượng và độ bao phủ của test so với chiến lượcTraceabilityLiên kết test ngược về yêu cầu để phục vụ audit và tuân thủNFR AssessmentĐánh giá các yêu cầu phi chức năng như hiệu năng, bảo mậtCI SetupCấu hình thực thi test trong pipeline tích hợp liên tụcFramework ScaffoldingDựng hạ tầng và cấu trúc dự án kiểm thửRelease GateRa quyết định phát hành go/no-go dựa trên dữ liệu

TEA cũng hỗ trợ ưu tiên theo rủi ro P0-P3 và tích hợp tùy chọn với Playwright Utils cùng công cụ MCP.

### Khi Nào Nên Dùng TEA

[Phần tiêu đề “Khi Nào Nên Dùng TEA”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng-tea)

- Dự án cần truy vết yêu cầu hoặc tài liệu tuân thủ
- Đội ngũ cần ưu tiên kiểm thử theo rủi ro trên nhiều tính năng
- Môi trường doanh nghiệp có quality gate chính thức trước phát hành
- Miền nghiệp vụ phức tạp, nơi chiến lược kiểm thử phải được lên trước khi viết test
- Dự án đã vượt quá mô hình một workflow của QA tích hợp sẵn

## Kiểm Thử Nằm Ở Đâu Trong Workflow

[Phần tiêu đề “Kiểm Thử Nằm Ở Đâu Trong Workflow”](#ki%E1%BB%83m-th%E1%BB%AD-n%E1%BA%B1m-%E1%BB%9F-%C4%91%C3%A2u-trong-workflow)

Workflow QA Automate xuất hiện ở Phase 4 (Implementation) trong workflow map của BMad Method. Nó được thiết kế để chạy **sau khi hoàn tất trọn vẹn một epic** — tức là khi mọi story trong epic đó đã được triển khai và code review xong. Trình tự điển hình là:

1. Với mỗi story trong epic: triển khai bằng Dev (`DS`), sau đó xác nhận bằng Code Review (`CR`)
2. Sau khi epic hoàn tất: tạo test bằng `QA` (thông qua Developer agent) hoặc workflow Automate của TEA
3. Chạy retrospective (`bmad-retrospective`) để ghi nhận bài học rút ra

Workflow QA tích hợp sẵn làm việc trực tiếp từ source code mà không cần nạp tài liệu lập kế hoạch như PRD hay architecture. Các workflow của TEA có thể tích hợp với artifact lập kế hoạch ở các bước trước để phục vụ truy vết.

Để hiểu rõ hơn kiểm thử nằm ở đâu trong quy trình tổng thể, xem [Workflow Map](https://docs.bmad-method.org/vi-vn/reference/workflow-map/).