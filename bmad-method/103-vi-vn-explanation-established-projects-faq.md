---
title: FAQ cho dự án đã tồn tại
url: https://docs.bmad-method.org/vi-vn/explanation/established-projects-faq/
source: sitemap
fetched_at: 2026-04-08T11:31:53.260121886-03:00
rendered_js: false
word_count: 401
summary: This document provides quick answers to frequently asked questions regarding the use of the BMad Method (BMM), covering best practices for existing projects, running initial setup commands, and handling code quality deviations.
tags:
    - bmad-method
    - existing-project
    - quick-flow
    - best-practices
    - qa
    - onboarding
category: guide
---

Các câu trả lời nhanh cho những câu hỏi thường gặp khi làm việc với dự án đã tồn tại bằng BMad Method (BMM).

- [Tôi có phải chạy document-project trước không?](#toi-co-phai-chay-document-project-truoc-khong)
- [Nếu tôi quên chạy document-project thì sao?](#neu-toi-quen-chay-document-project-thi-sao)
- [Tôi có thể dùng Quick Flow cho dự án đã tồn tại không?](#toi-co-the-dung-quick-flow-cho-du-an-da-ton-tai-khong)
- [Nếu code hiện tại của tôi không theo best practices thì sao?](#neu-code-hien-tai-cua-toi-khong-theo-best-practices-thi-sao)

### Tôi có phải chạy document-project trước không?

[Phần tiêu đề “Tôi có phải chạy document-project trước không?”](#t%C3%B4i-c%C3%B3-ph%E1%BA%A3i-ch%E1%BA%A1y-document-project-tr%C6%B0%E1%BB%9Bc-kh%C3%B4ng)

Rất nên chạy, nhất là khi:

- Không có tài liệu sẵn có
- Tài liệu đã lỗi thời
- Agent AI cần context về code hiện có

Bạn có thể bỏ qua nếu đã có tài liệu đầy đủ, mới, bao gồm `docs/index.md`, hoặc bạn sẽ dùng công cụ/kỹ thuật khác để giúp agent khám phá hệ thống hiện có.

### Nếu tôi quên chạy document-project thì sao?

[Phần tiêu đề “Nếu tôi quên chạy document-project thì sao?”](#n%E1%BA%BFu-t%C3%B4i-qu%C3%AAn-ch%E1%BA%A1y-document-project-th%C3%AC-sao)

Không sao - bạn có thể chạy nó bất cứ lúc nào. Bạn thậm chí có thể chạy trong khi dự án đang diễn ra hoặc sau đó để giữ tài liệu luôn mới.

### Tôi có thể dùng Quick Flow cho dự án đã tồn tại không?

[Phần tiêu đề “Tôi có thể dùng Quick Flow cho dự án đã tồn tại không?”](#t%C3%B4i-c%C3%B3-th%E1%BB%83-d%C3%B9ng-quick-flow-cho-d%E1%BB%B1-%C3%A1n-%C4%91%C3%A3-t%E1%BB%93n-t%E1%BA%A1i-kh%C3%B4ng)

Có. Quick Flow hoạt động rất tốt với dự án đã tồn tại. Nó sẽ:

- Tự động nhận diện stack hiện có
- Phân tích pattern code hiện có
- Phát hiện quy ước và hỏi bạn để xác nhận
- Tạo spec giàu ngữ cảnh, tôn trọng code hiện có

Rất hợp với sửa lỗi và tính năng nhỏ trong codebase sẵn có.

### Nếu code hiện tại của tôi không theo best practices thì sao?

[Phần tiêu đề “Nếu code hiện tại của tôi không theo best practices thì sao?”](#n%E1%BA%BFu-code-hi%E1%BB%87n-t%E1%BA%A1i-c%E1%BB%A7a-t%C3%B4i-kh%C3%B4ng-theo-best-practices-th%C3%AC-sao)

Quick Flow sẽ nhận diện quy ước hiện có và hỏi: “Tôi có nên tuân theo những quy ước hiện tại này không?” Bạn là người quyết định:

- **Có** → Giữ tính nhất quán với codebase hiện tại
- **Không** → Đặt ra chuẩn mới, đồng thời ghi rõ lý do trong spec

BMM tôn trọng lựa chọn của bạn - nó không ép buộc hiện đại hóa, nhưng sẽ đưa ra lựa chọn đó.

**Có câu hỏi chưa được trả lời ở đây?** Hãy [mở issue](https://github.com/bmad-code-org/BMAD-METHOD/issues) hoặc hỏi trên [Discord](https://discord.gg/gk8jAdXWmj) để chúng tôi bổ sung!