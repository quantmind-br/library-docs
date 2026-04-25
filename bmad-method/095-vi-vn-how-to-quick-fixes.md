---
title: Quick Fixes
url: https://docs.bmad-method.org/vi-vn/how-to/quick-fixes/
source: sitemap
fetched_at: 2026-04-08T11:32:17.652529613-03:00
rendered_js: false
word_count: 589
summary: This document guides users on when and how to use the 'Quick Dev' process for making small, targeted changes like bug fixes or minor refactors without following a full workflow. It details a step-by-step execution flow from initializing a chat session to reviewing and pushing changes.
tags:
    - quick-dev
    - refactoring
    - bug-fixing
    - workflow-guide
    - development-process
category: tutorial
---

Sử dụng **Quick Dev** cho sửa lỗi, refactor, hoặc các thay đổi nhỏ có mục tiêu rõ ràng mà không cần quy trình BMad Method đầy đủ.

## Khi nào nên dùng

[Phần tiêu đề “Khi nào nên dùng”](#khi-n%C3%A0o-n%C3%AAn-d%C3%B9ng)

- Sửa lỗi khi nguyên nhân đã rõ ràng
- Refactor nhỏ (đổi tên, tách hàm, tái cấu trúc) nằm trong một vài tệp
- Điều chỉnh tính năng nhỏ hoặc thay đổi cấu hình
- Cập nhật dependency

## Các bước thực hiện

[Phần tiêu đề “Các bước thực hiện”](#c%C3%A1c-b%C6%B0%E1%BB%9Bc-th%E1%BB%B1c-hi%E1%BB%87n)

### 1. Bắt đầu một phiên chat mới

[Phần tiêu đề “1. Bắt đầu một phiên chat mới”](#1-b%E1%BA%AFt-%C4%91%E1%BA%A7u-m%E1%BB%99t-phi%C3%AAn-chat-m%E1%BB%9Bi)

Mở **một phiên chat mới** trong AI IDE của bạn. Tái sử dụng một phiên từ workflow trước dễ gây xung đột context.

### 2. Mô tả ý định của bạn

[Phần tiêu đề “2. Mô tả ý định của bạn”](#2-m%C3%B4-t%E1%BA%A3-%C3%BD-%C4%91%E1%BB%8Bnh-c%E1%BB%A7a-b%E1%BA%A1n)

Quick Dev nhận ý định dạng tự do - trước, cùng lúc, hoặc sau khi gọi workflow. Ví dụ:

```text

run quick-dev — Sửa lỗi validate đăng nhập cho phép mật khẩu rỗng.
```

```text

run quick-dev — fix https://github.com/org/repo/issues/42
```

```text

run quick-dev — thực hiện ý định trong _bmad-output/implementation-artifacts/my-intent.md
```

```text

Tôi nghĩ vấn đề nằm ở auth middleware, nó không kiểm tra hạn của token.
Để tôi xem... đúng rồi, src/auth/middleware.ts dòng 47 bỏ qua
hoàn toàn phần kiểm tra exp. run quick-dev
```

```text

run quick-dev
> Bạn muốn làm gì?
Refactor UserService sang dùng async/await thay vì callbacks.
```

Văn bản thường, đường dẫn tệp, URL issue GitHub, liên kết bug tracker - bất kỳ thứ gì LLM có thể suy ra thành một ý định cụ thể.

### 3. Trả lời câu hỏi và phê duyệt

[Phần tiêu đề “3. Trả lời câu hỏi và phê duyệt”](#3-tr%E1%BA%A3-l%E1%BB%9Di-c%C3%A2u-h%E1%BB%8Fi-v%C3%A0-ph%C3%AA-duy%E1%BB%87t)

Quick Dev có thể đặt câu hỏi làm rõ hoặc đưa ra một bản spec ngắn để bạn phê duyệt trước khi triển khai. Hãy trả lời và phê duyệt khi bạn thấy kế hoạch đã ổn.

### 4. Review và push

[Phần tiêu đề “4. Review và push”](#4-review-v%C3%A0-push)

Quick Dev sẽ triển khai thay đổi, tự review công việc của mình, sửa các vấn đề phát hiện được và commit vào local. Khi hoàn thành, nó sẽ mở các tệp bị ảnh hưởng trong editor.

- Xem nhanh diff để xác nhận thay đổi đúng với ý định của bạn
- Nếu có gì không ổn, nói cho agent biết cần sửa gì - nó có thể lặp lại ngay trong cùng phiên

Khi đã hài lòng, push commit. Quick Dev sẽ đề xuất push và tạo PR cho bạn.

## Bạn nhận được gì

[Phần tiêu đề “Bạn nhận được gì”](#b%E1%BA%A1n-nh%E1%BA%ADn-%C4%91%C6%B0%E1%BB%A3c-g%C3%AC)

- Các tệp nguồn đã được sửa với bản fix hoặc refactor
- Test đã pass (nếu dự án có bộ test)
- Một commit sẵn sàng để push, dùng conventional commit message

## Công việc trì hoãn

[Phần tiêu đề “Công việc trì hoãn”](#c%C3%B4ng-vi%E1%BB%87c-tr%C3%AC-ho%C3%A3n)

Quick Dev giữ mỗi lần chạy tập trung vào một mục tiêu duy nhất. Nếu yêu cầu của bạn có nhiều mục tiêu độc lập, hoặc review phát hiện các vấn đề tồn tại sẵn không liên quan đến thay đổi hiện tại, Quick Dev sẽ đưa chúng vào tệp `deferred-work.md` trong thư mục implementation artifacts thay vì cố gắng xử lý tất cả một lúc.

Hãy kiểm tra tệp này sau mỗi lần chạy - đó là backlog các việc bạn cần quay lại sau. Mỗi mục trì hoãn có thể được đưa vào một lần chạy Quick Dev mới.

## Khi nào nên nâng cấp lên quy trình lập kế hoạch đầy đủ

[Phần tiêu đề “Khi nào nên nâng cấp lên quy trình lập kế hoạch đầy đủ”](#khi-n%C3%A0o-n%C3%AAn-n%C3%A2ng-c%E1%BA%A5p-l%C3%AAn-quy-tr%C3%ACnh-l%E1%BA%ADp-k%E1%BA%BF-ho%E1%BA%A1ch-%C4%91%E1%BA%A7y-%C4%91%E1%BB%A7)

Cân nhắc dùng toàn bộ BMad Method khi:

- Thay đổi ảnh hưởng nhiều hệ thống hoặc cần cập nhật đồng bộ trên nhiều tệp
- Bạn chưa chắc phạm vi và cần làm rõ yêu cầu trước
- Bạn cần ghi lại tài liệu hoặc quyết định kiến trúc cho cả nhóm

Xem [Quick Dev](https://docs.bmad-method.org/vi-vn/explanation/quick-dev/) để hiểu rõ hơn Quick Dev nằm ở đâu trong BMad Method.