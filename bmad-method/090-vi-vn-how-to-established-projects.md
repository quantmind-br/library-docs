---
title: Dự án đã tồn tại
url: https://docs.bmad-method.org/vi-vn/how-to/established-projects/
source: sitemap
fetched_at: 2026-04-08T11:32:07.558541904-03:00
rendered_js: false
word_count: 719
summary: Tài liệu này hướng dẫn quy trình chi tiết sử dụng BMad Method để on-board và làm việc hiệu quả trong các dự án phần mềm hiện có hoặc codebase legacy. Nó bao gồm các bước từ dọn dẹp tài liệu, tạo bối cảnh dự án (Project Context), đến cách duy trì tài liệu chất lượng và sử dụng công cụ trợ giúp tự động.
tags:
    - bmad-method
    - legacy-codebase
    - onboarding-guide
    - project-context
    - software-development
    - documentation
category: guide
---

Sử dụng BMad Method hiệu quả khi làm việc với các dự án hiện có và codebase legacy.

Tài liệu này mô tả workflow cốt lõi để on-board vào các dự án đã tồn tại bằng BMad Method.

## Bước 1: Dọn dẹp các tài liệu lập kế hoạch đã hoàn tất

[Phần tiêu đề “Bước 1: Dọn dẹp các tài liệu lập kế hoạch đã hoàn tất”](#b%C6%B0%E1%BB%9Bc-1-d%E1%BB%8Dn-d%E1%BA%B9p-c%C3%A1c-t%C3%A0i-li%E1%BB%87u-l%E1%BA%ADp-k%E1%BA%BF-ho%E1%BA%A1ch-%C4%91%C3%A3-ho%C3%A0n-t%E1%BA%A5t)

Nếu bạn đã hoàn thành toàn bộ epic và story trong PRD theo quy trình BMad, hãy dọn dẹp những tệp đó. Bạn có thể lưu trữ, xóa đi, hoặc dựa vào lịch sử phiên bản nếu cần. Không nên giữ các tệp này trong:

- `docs/`
- `_bmad-output/planning-artifacts/`
- `_bmad-output/implementation-artifacts/`

## Bước 2: Tạo Project Context

[Phần tiêu đề “Bước 2: Tạo Project Context”](#b%C6%B0%E1%BB%9Bc-2-t%E1%BA%A1o-project-context)

Chạy workflow tạo project context:

```bash

bmad-generate-project-context
```

Workflow này sẽ quét codebase để nhận diện:

- Stack công nghệ và các phiên bản
- Các pattern tổ chức code
- Quy ước đặt tên
- Cách tiếp cận kiểm thử
- Các pattern đặc thù framework

Bạn có thể xem lại và chỉnh sửa tệp được tạo, hoặc tự tạo tệp tại `_bmad-output/project-context.md` nếu muốn.

[Tìm hiểu thêm về project context](https://docs.bmad-method.org/vi-vn/explanation/project-context/)

## Bước 3: Duy trì tài liệu dự án chất lượng

[Phần tiêu đề “Bước 3: Duy trì tài liệu dự án chất lượng”](#b%C6%B0%E1%BB%9Bc-3-duy-tr%C3%AC-t%C3%A0i-li%E1%BB%87u-d%E1%BB%B1-%C3%A1n-ch%E1%BA%A5t-l%C6%B0%E1%BB%A3ng)

Thư mục `docs/` của bạn nên chứa tài liệu ngắn gọn, có tổ chức tốt, và phản ánh chính xác dự án:

- Mục tiêu và lý do kinh doanh
- Quy tắc nghiệp vụ
- Kiến trúc
- Bất kỳ thông tin dự án nào khác có liên quan

Với các dự án phức tạp, hãy cân nhắc dùng workflow `bmad-document-project`. Nó có các biến thể lúc chạy có thể quét toàn bộ dự án và tài liệu hóa trạng thái thực tế hiện tại của hệ thống.

## Bước 4: Nhờ trợ giúp

[Phần tiêu đề “Bước 4: Nhờ trợ giúp”](#b%C6%B0%E1%BB%9Bc-4-nh%E1%BB%9D-tr%E1%BB%A3-gi%C3%BAp)

### BMad-Help: Điểm bắt đầu của bạn

[Phần tiêu đề “BMad-Help: Điểm bắt đầu của bạn”](#bmad-help-%C4%91i%E1%BB%83m-b%E1%BA%AFt-%C4%91%E1%BA%A7u-c%E1%BB%A7a-b%E1%BA%A1n)

**Hãy chạy `bmad-help` bất cứ lúc nào bạn không chắc cần làm gì tiếp theo.** Công cụ hướng dẫn thông minh này:

- Kiểm tra dự án để xem những gì đã được hoàn thành
- Đưa ra tùy chọn dựa trên các module bạn đã cài
- Hiểu các câu hỏi bằng ngôn ngữ tự nhiên

```text

bmad-help Tôi có một ứng dụng Rails đã tồn tại, tôi nên bắt đầu từ đâu?
bmad-help Điểm khác nhau giữa quick-flow và full method là gì?
bmad-help Cho tôi xem những workflow đang có
```

BMad-Help cũng **tự động chạy ở cuối mỗi workflow**, đưa ra hướng dẫn rõ ràng về việc cần làm tiếp theo.

### Chọn cách tiếp cận

[Phần tiêu đề “Chọn cách tiếp cận”](#ch%E1%BB%8Dn-c%C3%A1ch-ti%E1%BA%BFp-c%E1%BA%ADn)

Bạn có hai lựa chọn chính, tùy thuộc vào phạm vi thay đổi:

Phạm viCách tiếp cận được khuyến nghị**Cập nhật hoặc bổ sung nhỏ**Chạy `bmad-quick-dev` để làm rõ ý định, lập kế hoạch, triển khai và review trong một workflow duy nhất. Quy trình BMad Method đầy đủ có thể là quá mức cần thiết.**Thay đổi hoặc bổ sung lớn**Bắt đầu với BMad Method, áp dụng mức độ chặt chẽ phù hợp với nhu cầu của bạn.

Khi tạo brief hoặc đi thẳng vào PRD, đảm bảo agent:

- Tìm và phân tích tài liệu dự án hiện có
- Đọc đúng bối cảnh về hệ thống hiện tại của bạn

Bạn có thể chủ động hướng dẫn agent, nhưng mục tiêu là đảm bảo tính năng mới tích hợp tốt với hệ thống đã có.

Công việc UX là tùy chọn. Quyết định này không phụ thuộc vào việc dự án có UX hay không, mà phụ thuộc vào:

- Bạn có định thay đổi UX hay không
- Bạn có cần thiết kế hay pattern UX mới đáng kể hay không

Nếu thay đổi của bạn chỉ là những cập nhật nhỏ trên các màn hình hiện có mà bạn đã hài lòng, thì không cần một quy trình UX đầy đủ.

### Cân nhắc về kiến trúc

[Phần tiêu đề “Cân nhắc về kiến trúc”](#c%C3%A2n-nh%E1%BA%AFc-v%E1%BB%81-ki%E1%BA%BFn-tr%C3%BAc)

Khi làm kiến trúc, đảm bảo kiến trúc sư:

- Sử dụng đúng các tệp tài liệu cần thiết
- Quét codebase hiện có

Cần đặc biệt chú ý để tránh tái phát minh bánh xe hoặc đưa ra quyết định không phù hợp với kiến trúc hiện tại.

- [**Quick Fixes**](https://docs.bmad-method.org/vi-vn/how-to/quick-fixes/) - Sửa lỗi và thay đổi ad-hoc
- [**Câu hỏi thường gặp cho dự án đã tồn tại**](https://docs.bmad-method.org/vi-vn/explanation/established-projects-faq/) - Những câu hỏi phổ biến khi làm việc với dự án đã tồn tại