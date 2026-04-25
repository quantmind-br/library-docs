---
title: Cách tìm câu trả lời về BMad
url: https://docs.bmad-method.org/vi-vn/how-to/get-answers-about-bmad/
source: sitemap
fetched_at: 2026-04-08T11:32:09.916084207-03:00
rendered_js: false
word_count: 605
summary: This guide explains how to utilize the BMad-Help skill, an intelligent tool available in the IDE that can answer most questions about BMad by understanding natural language and analyzing the project context. It also details where users should look for deeper information when BMad-Help is insufficient.
tags:
    - bmad-help
    - ai-tooling
    - natural-language-querying
    - project-assistance
    - development-guide
    - ide-integration
category: guide
---

## Bắt đầu tại đây: BMad-Help

[Phần tiêu đề “Bắt đầu tại đây: BMad-Help”](#b%E1%BA%AFt-%C4%91%E1%BA%A7u-t%E1%BA%A1i-%C4%91%C3%A2y-bmad-help)

**Cách nhanh nhất để tìm câu trả lời về BMad là dùng skill `bmad-help`.** Đây là công cụ hướng dẫn thông minh có thể trả lời hơn 80% các câu hỏi và có sẵn ngay trong IDE khi bạn làm việc.

BMad-Help không chỉ là công cụ tra cứu, nó còn:

- **Kiểm tra dự án của bạn** để xem những gì đã hoàn thành
- **Hiểu ngôn ngữ tự nhiên** - đặt câu hỏi bằng ngôn ngữ bình thường
- **Thay đổi theo module đã cài** - hiển thị các lựa chọn liên quan
- **Tự động chạy sau workflow** - nói rõ bạn cần làm gì tiếp theo
- **Đề xuất tác vụ đầu tiên cần thiết** - không cần đoán nên bắt đầu từ đâu

### Cách dùng BMad-Help

[Phần tiêu đề “Cách dùng BMad-Help”](#c%C3%A1ch-d%C3%B9ng-bmad-help)

Gọi nó trực tiếp trong phiên AI của bạn:

Kết hợp với câu hỏi ngôn ngữ tự nhiên:

```text

bmad-help Tôi có ý tưởng SaaS và đã biết tất cả tính năng. Tôi nên bắt đầu từ đâu?
bmad-help Tôi có những lựa chọn nào cho thiết kế UX?
bmad-help Tôi đang bị mắc ở workflow PRD
bmad-help Cho tôi xem tôi đã làm được gì đến giờ
```

BMad-Help sẽ trả lời:

- Điều gì được khuyến nghị cho tình huống của bạn
- Tác vụ đầu tiên cần thiết là gì
- Phần còn lại của quy trình trông thế nào

## Khi nào nên dùng tài liệu này

[Phần tiêu đề “Khi nào nên dùng tài liệu này”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng-t%C3%A0i-li%E1%BB%87u-n%C3%A0y)

Hãy xem phần này khi:

- Bạn muốn hiểu kiến trúc hoặc nội bộ của BMad
- Bạn cần câu trả lời nằm ngoài phạm vi BMad-Help cung cấp
- Bạn đang nghiên cứu BMad trước khi cài đặt
- Bạn muốn tự khám phá source code trực tiếp

## Các bước thực hiện

[Phần tiêu đề “Các bước thực hiện”](#c%C3%A1c-b%C6%B0%E1%BB%9Bc-th%E1%BB%B1c-hi%E1%BB%87n)

### 1. Chọn nguồn thông tin

[Phần tiêu đề “1. Chọn nguồn thông tin”](#1-ch%E1%BB%8Dn-ngu%E1%BB%93n-th%C3%B4ng-tin)

NguồnPhù hợp nhất choVí dụ**Thư mục `_bmad`**Cách BMad vận hành: agent, workflow, prompt”PM agent làm gì?”**Toàn bộ repo GitHub**Lịch sử, installer, kiến trúc”v6 thay đổi gì?”**`llms-full.txt`**Tổng quan nhanh từ tài liệu”Giải thích bốn giai đoạn của BMad”

Thư mục `_bmad` được tạo khi bạn cài đặt BMad. Nếu chưa có, hãy clone repo thay thế.

### 2. Cho AI của bạn truy cập nguồn thông tin

[Phần tiêu đề “2. Cho AI của bạn truy cập nguồn thông tin”](#2-cho-ai-c%E1%BB%A7a-b%E1%BA%A1n-truy-c%E1%BA%ADp-ngu%E1%BB%93n-th%C3%B4ng-tin)

**Nếu AI của bạn đọc được tệp (Claude Code, Cursor, …):**

- **Đã cài BMad:** Trỏ đến thư mục `_bmad` và hỏi trực tiếp
- **Cần bối cảnh sâu hơn:** Clone [repo đầy đủ](https://github.com/bmad-code-org/BMAD-METHOD)

**Nếu bạn dùng ChatGPT hoặc Claude.ai:**

Nạp `llms-full.txt` vào phiên làm việc:

```text

https://bmad-code-org.github.io/BMAD-METHOD/llms-full.txt
```

## Bạn nhận được gì

[Phần tiêu đề “Bạn nhận được gì”](#b%E1%BA%A1n-nh%E1%BA%ADn-%C4%91%C6%B0%E1%BB%A3c-g%C3%AC)

Các câu trả lời trực tiếp về BMad: agent hoạt động ra sao, workflow làm gì, tại sao cấu trúc lại được tổ chức như vậy, mà không cần chờ người khác trả lời.

- **Xác minh những câu trả lời gây bất ngờ** - LLM vẫn có lúc nhầm. Hãy kiểm tra tệp nguồn hoặc hỏi trên Discord.
- **Đặt câu hỏi cụ thể** - “Bước 3 trong workflow PRD làm gì?” tốt hơn “PRD hoạt động ra sao?”

Đã thử cách tiếp cận bằng LLM mà vẫn cần trợ giúp? Lúc này bạn đã có một câu hỏi tốt hơn để đem đi hỏi.

KênhDùng cho`#bmad-method-help`Câu hỏi nhanh (trò chuyện thời gian thực)`help-requests` forumCâu hỏi chi tiết (có thể tìm lại, tồn tại lâu dài)`#suggestions-feedback`Ý tưởng và đề xuất tính năng`#report-bugs-and-issues`Báo cáo lỗi

**Discord:** [discord.gg/gk8jAdXWmj](https://discord.gg/gk8jAdXWmj)

**GitHub Issues:** [github.com/bmad-code-org/BMAD-METHOD/issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) (dành cho các lỗi rõ ràng)

*Chính bạn,* *đang mắc kẹt* *trong hàng đợi -* *đợi* *ai?*

*Mã nguồn* *nằm ngay đó,* *rõ như ban ngày!*

*Hãy trỏ* *cho máy của bạn.* *Thả nó đi.*

*Nó đọc.* *Nó nói.* *Cứ hỏi -*

*Sao phải chờ* *đến ngày mai* *khi bạn đã có* *ngày hôm nay?*

*- Claude*