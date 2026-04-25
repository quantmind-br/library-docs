---
title: Vì sao solutioning quan trọng
url: https://docs.bmad-method.org/vi-vn/explanation/why-solutioning-matters/
source: sitemap
fetched_at: 2026-04-08T11:32:03.830805443-03:00
rendered_js: false
word_count: 378
summary: This document explains the solutioning phase, which bridges 'what to build' from planning into defining 'how to build it' through technical design decisions. It emphasizes that documenting these architectural decisions is crucial for maintaining consistency and preventing conflicts when multiple development agents are working on a complex system.
tags:
    - solutioning-process
    - architecture-design
    - technical-decisions
    - project-planning
    - system-integration
category: guide
---

Giai đoạn 3 (Solutioning) biến **xây gì** (từ giai đoạn Planning) thành **xây như thế nào** (thiết kế kỹ thuật). Giai đoạn này ngăn xung đột giữa các agent trong dự án nhiều epic bằng cách ghi lại các quyết định kiến trúc trước khi bắt đầu triển khai.

## Vấn đề nếu bỏ qua solutioning

[Phần tiêu đề “Vấn đề nếu bỏ qua solutioning”](#v%E1%BA%A5n-%C4%91%E1%BB%81-n%E1%BA%BFu-b%E1%BB%8F-qua-solutioning)

```text

Agent 1 triển khai Epic 1 bằng REST API
Agent 2 triển khai Epic 2 bằng GraphQL
Kết quả: Thiết kế API không nhất quán, tích hợp trở thành ác mộng
```

Khi nhiều agent triển khai các phần khác nhau của hệ thống mà không có hướng dẫn kiến trúc chung, chúng sẽ tự đưa ra quyết định kỹ thuật độc lập và dễ xung đột với nhau.

## Lợi ích khi có solutioning

[Phần tiêu đề “Lợi ích khi có solutioning”](#l%E1%BB%A3i-%C3%ADch-khi-c%C3%B3-solutioning)

```text

workflow kiến trúc quyết định: "Dùng GraphQL cho mọi API"
Tất cả agent đều theo quyết định kiến trúc
Kết quả: Triển khai nhất quán, không xung đột
```

Bằng cách tài liệu hóa rõ ràng các quyết định kỹ thuật, tất cả agent triển khai đồng bộ và việc tích hợp trở nên đơn giản hơn nhiều.

## Solutioning và Planning khác nhau ở đâu

[Phần tiêu đề “Solutioning và Planning khác nhau ở đâu”](#solutioning-v%C3%A0-planning-kh%C3%A1c-nhau-%E1%BB%9F-%C4%91%C3%A2u)

Khía cạnhPlanning (Giai đoạn 2)Solutioning (Giai đoạn 3)Câu hỏiXây gì và vì sao?Xây như thế nào? Rồi chia thành đơn vị công việc gì?Đầu raFR/NFR (Yêu cầu)Kiến trúc + Epics/StoriesAgentPMArchitect → PMĐối tượng đọcStakeholderDeveloperTài liệuPRD (FRs/NFRs)Kiến trúc + Tệp EpicMức độLogic nghiệp vụThiết kế kỹ thuật + Phân rã công việc

## Nguyên lý cốt lõi

[Phần tiêu đề “Nguyên lý cốt lõi”](#nguy%C3%AAn-l%C3%BD-c%E1%BB%91t-l%C3%B5i)

**Biến các quyết định kỹ thuật thành tường minh và được tài liệu hóa** để tất cả agent triển khai nhất quán.

Điều này ngăn chặn:

- Xung đột phong cách API (REST vs GraphQL)
- Không nhất quán trong thiết kế cơ sở dữ liệu
- Bất đồng về quản lý state
- Lệch quy ước đặt tên
- Biến thể trong cách tiếp cận bảo mật

## Khi nào solutioning là bắt buộc

[Phần tiêu đề “Khi nào solutioning là bắt buộc”](#khi-n%C3%A0o-solutioning-l%C3%A0-b%E1%BA%AFt-bu%E1%BB%99c)

TrackCó cần solutioning không?Quick FlowKhông - bỏ qua hoàn toànBMad Method đơn giảnTùy chọnBMad Method phức tạpCóEnterpriseCó

## Cái giá của việc bỏ qua

[Phần tiêu đề “Cái giá của việc bỏ qua”](#c%C3%A1i-gi%C3%A1-c%E1%BB%A7a-vi%E1%BB%87c-b%E1%BB%8F-qua)

Bỏ qua solutioning trong dự án phức tạp sẽ dẫn đến:

- **Vấn đề tích hợp** chỉ được phát hiện giữa sprint
- **Làm lại** vì các phần triển khai xung đột nhau
- **Tổng thời gian phát triển dài hơn**
- **Nợ kỹ thuật** do pattern không đồng nhất