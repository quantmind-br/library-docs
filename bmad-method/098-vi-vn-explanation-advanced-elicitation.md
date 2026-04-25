---
title: Khai thác nâng cao
url: https://docs.bmad-method.org/vi-vn/explanation/advanced-elicitation/
source: sitemap
fetched_at: 2026-04-08T11:31:43.489777012-03:00
rendered_js: false
word_count: 496
summary: Bài viết giải thích khái niệm "Khai thác nâng cao" là một phương pháp xem xét lại có cấu trúc, nơi người dùng áp dụng các phương pháp lập luận cụ thể lên output của LLM để tìm ra những cải tiến sâu sắc mà việc thử lại chung chung có thể bỏ sót.
tags:
    - llm-review
    - argumentation-methods
    - advanced-extraction
    - critical-thinking
    - content-refinement
category: guide
---

Buộc LLM xem xét lại những gì nó vừa tạo ra. Bạn chọn một phương pháp lập luận, nó áp dụng phương pháp đó lên chính output của mình, rồi bạn quyết định có giữ các cải tiến hay không.

## Khai thác nâng cao là gì?

[Phần tiêu đề “Khai thác nâng cao là gì?”](#khai-th%C3%A1c-n%C3%A2ng-cao-l%C3%A0-g%C3%AC)

Đây là một lần xem xét lại có cấu trúc. Thay vì bảo AI “thử lại” hoặc “làm cho nó tốt hơn”, bạn chọn một phương pháp lập luận cụ thể và AI sẽ xem lại output của chính nó dưới góc đó.

Khác biệt này rất quan trọng. Yêu cầu mơ hồ sẽ tạo ra bản sửa đổi mơ hồ. Một phương pháp được gọi tên buộc AI tấn công vấn đề theo một hướng cụ thể, qua đó phát hiện những ý tưởng mà một lần thử lại chung chung sẽ bỏ lỡ.

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

- Sau khi workflow tạo nội dung và bạn muốn có phương án thay thế
- Khi output có vẻ ổn nhưng bạn nghi vẫn còn có thể đào sâu hơn
- Để stress-test các giả định hoặc tìm điểm yếu
- Với nội dung quan trọng, nơi mà việc nghĩ lại sẽ có giá trị

Các workflow sẽ đưa ra tùy chọn khai thác nâng cao tại các điểm quyết định - sau khi LLM tạo một kết quả, bạn sẽ được hỏi có muốn chạy nó hay không.

## Nó hoạt động như thế nào

[Phần tiêu đề “Nó hoạt động như thế nào”](#n%C3%B3-ho%E1%BA%A1t-%C4%91%E1%BB%99ng-nh%C6%B0-th%E1%BA%BF-n%C3%A0o)

1. LLM đề xuất 5 phương pháp phù hợp với nội dung của bạn
2. Bạn chọn một phương pháp (hoặc đảo lại để xem lựa chọn khác)
3. Phương pháp được áp dụng, các cải tiến được hiện ra
4. Chấp nhận hoặc bỏ đi, lặp lại hoặc tiếp tục

## Các phương pháp tích hợp sẵn

[Phần tiêu đề “Các phương pháp tích hợp sẵn”](#c%C3%A1c-ph%C6%B0%C6%A1ng-ph%C3%A1p-t%C3%ADch-h%E1%BB%A3p-s%E1%BA%B5n)

Có hàng chục phương pháp lập luận có sẵn. Một vài ví dụ:

- **Pre-mortem Analysis** - Giả sử dự án đã thất bại rồi lần ngược lại để tìm lý do
- **First Principles Thinking** - Loại bỏ giả định, xây lại từ sự thật nền tảng
- **Inversion** - Hỏi cách nào chắc chắn dẫn đến thất bại, rồi tránh những điều đó
- **Red Team vs Blue Team** - Tự tấn công công việc của chính mình, rồi tự bảo vệ nó
- **Socratic Questioning** - Chất vấn mọi khẳng định bằng “tại sao?” và “làm sao bạn biết?”
- **Constraint Removal** - Bỏ hết ràng buộc, xem điều gì thay đổi, rồi thêm lại có chọn lọc
- **Stakeholder Mapping** - Đánh giá lại từ góc nhìn của từng bên liên quan
- **Analogical Reasoning** - Tìm điểm tương đồng ở lĩnh vực khác và áp dụng bài học của chúng

Và còn nhiều nữa. AI sẽ chọn những lựa chọn phù hợp nhất với nội dung của bạn - bạn quyết định chạy cái nào.