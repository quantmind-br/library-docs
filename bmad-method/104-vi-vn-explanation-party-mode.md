---
title: Party Mode
url: https://docs.bmad-method.org/vi-vn/explanation/party-mode/
source: sitemap
fetched_at: 2026-04-08T11:31:55.257486085-03:00
rendered_js: false
word_count: 474
summary: This document introduces "Party Mode," a feature that brings together multiple specialized AI agents like PMs, Architects, Developers, and UX Designers into a single conversation for collaborative brainstorming, complex decision-making, or post-mortem analysis.
tags:
    - ai-collaboration
    - party-mode
    - brainstorming
    - team-simulation
    - decision-making
    - agent-system
category: tutorial
---

Đưa tất cả agent AI của bạn vào cùng một cuộc trò chuyện.

## Party Mode là gì?

[Phần tiêu đề “Party Mode là gì?”](#party-mode-l%C3%A0-g%C3%AC)

Chạy `bmad-party-mode` và bạn sẽ có cả đội AI trong cùng một phòng - PM, Architect, Dev, UX Designer, bất kỳ ai bạn cần. BMad Master điều phối, chọn các agent liên quan cho từng tin nhắn. Các agent trả lời đúng vai, đồng ý, phản biện, và bổ sung ý tưởng cho nhau.

Cuộc trò chuyện tiếp tục lâu đến mức bạn muốn. Bạn có thể hỏi tiếp, phản biện câu trả lời, đổi hướng thảo luận - đó là một cuộc qua lại thật sự với các agent của bạn cho đến khi xong.

**Phù hợp cho:**

- Các quyết định lớn có đánh đổi
- Các phiên động não ý tưởng
- Post-mortem khi mọi thứ đi sai
- Retrospective và lập kế hoạch sprint

### Gọi tên kiến trúc tệ

[Phần tiêu đề “Gọi tên kiến trúc tệ”](#g%E1%BB%8Di-t%C3%AAn-ki%E1%BA%BFn-tr%C3%BAc-t%E1%BB%87)

**Bạn:** “Được rồi cả đội, sprint vừa rồi là một thảm họa. Dịch vụ xác thực sập ba lần. Ai đã làm hỏng chuyện này?”

**Architect:** “Thiết kế vẫn ổn - xác thực phân tán với cơ chế fallback hợp lý. Nếu phần triển khai lệch khỏi spec…”

**Dev:** “Tôi đã làm đúng theo tài liệu kiến trúc. Spec không tính đến race condition khi vô hiệu hóa session đồng thời.”

**PM:** “Cả hai người đều bỏ sót vấn đề lớn hơn - chúng ta không xác thực đúng yêu cầu quản lý session trong PRD. **Lỗi này là do tôi** không bắt được sớm hơn.”

**TEA:** “Và tôi đáng ra phải bắt được nó trong integration test. Các kịch bản test đã không bao phủ trường hợp vô hiệu hóa đồng thời.”

### Động não sáng tạo

[Phần tiêu đề “Động não sáng tạo”](#%C4%91%E1%BB%99ng-n%C3%A3o-s%C3%A1ng-t%E1%BA%A1o)

**Bạn:** “Làm sao để quá trình onboarding có cảm giác kỳ diệu thay vì nhàm chán?”

**UX Designer:** “Bắt đầu bằng progressive disclosure - hiện tính năng khi người dùng cần, thay vì tung một tutorial dày đặc.”

**Storyteller:** “Nếu onboarding là một câu chuyện thì sao? Mỗi bước mở ra hành trình của một nhân vật - người dùng CHÍNH là người hùng.”

**Game Designer:** “Nối tiếp ý đó - nếu ‘nhiệm vụ’ đầu tiên thực chất giải quyết một vấn đề thật của người dùng thì sao? Họ học bằng cách làm ra giá trị ngay.”

### Quyết định kỹ thuật

[Phần tiêu đề “Quyết định kỹ thuật”](#quy%E1%BA%BFt-%C4%91%E1%BB%8Bnh-k%E1%BB%B9-thu%E1%BA%ADt)

**Bạn:** “MVP nên dùng monolith hay microservices?”

**Architect:** “Bắt đầu bằng monolith. Microservices thêm độ phức tạp mà bạn chưa cần ở mức 1000 người dùng.”

**PM:** “Đồng ý. Tốc độ ra thị trường quan trọng hơn khả năng mở rộng lý thuyết.”

**Dev:** “Monolith nhưng có ranh giới module rõ ràng. Nếu cần, mình có thể tách service sau.”