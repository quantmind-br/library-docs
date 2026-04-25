---
title: Skills
url: https://docs.bmad-method.org/vi-vn/reference/commands/
source: sitemap
fetched_at: 2026-04-08T11:32:25.42261661-03:00
rendered_js: false
word_count: 972
summary: This document explains what 'Skills' are within the BMad environment—pre-built prompts used to load agents, run workflows, or execute tasks in an IDE. It details the differences between invoking skills directly versus using agent triggers, and describes how the BMad installer generates these skills for various module types.
tags:
    - bmad-skills
    - ide-integration
    - workflow-automation
    - agent-loading
    - skill-management
    - development-guide
category: guide
---

Skills là các prompt dựng sẵn để nạp agent, chạy workflow hoặc thực thi task bên trong IDE của bạn. Trình cài đặt BMad sinh chúng từ các module bạn đã chọn tại thời điểm cài đặt. Nếu sau này bạn thêm, xóa hoặc thay đổi module, hãy chạy lại trình cài đặt để đồng bộ skills (xem [Khắc phục sự cố](#kh%E1%BA%AFc-ph%E1%BB%A5c-s%E1%BB%B1-c%E1%BB%91)).

BMad cung cấp hai cách để bắt đầu công việc, và chúng phục vụ những mục đích khác nhau.

Cơ chếCách gọiĐiều xảy ra**Skill**Gõ tên skill, ví dụ `bmad-help`, trong IDENạp trực tiếp agent, chạy workflow hoặc thực thi task**Trigger menu agent**Nạp agent trước, sau đó gõ mã ngắn như `DS`Agent diễn giải mã đó và bắt đầu workflow tương ứng trong khi vẫn giữ đúng persona

Trigger trong menu agent yêu cầu bạn đang ở trong một phiên agent đang hoạt động. Dùng skill khi bạn đã biết mình muốn workflow nào. Dùng trigger khi bạn đang làm việc với một agent và muốn đổi tác vụ mà không rời khỏi cuộc hội thoại.

## Skills Được Tạo Ra Như Thế Nào

[Phần tiêu đề “Skills Được Tạo Ra Như Thế Nào”](#skills-%C4%91%C6%B0%E1%BB%A3c-t%E1%BA%A1o-ra-nh%C6%B0-th%E1%BA%BF-n%C3%A0o)

Khi bạn chạy `npx bmad-method install`, trình cài đặt sẽ đọc manifest của mọi module được chọn rồi tạo một skill cho mỗi agent, workflow, task và tool. Mỗi skill là một thư mục chứa file `SKILL.md`, hướng dẫn AI nạp file nguồn tương ứng và làm theo chỉ dẫn trong đó.

Trình cài đặt dùng template cho từng loại skill:

Loại skillFile được tạo sẽ làm gì**Agent launcher**Nạp file persona của agent, kích hoạt menu của nó và giữ nguyên vai trò**Workflow skill**Nạp cấu hình workflow và làm theo các bước**Task skill**Nạp một file task độc lập và làm theo hướng dẫn**Tool skill**Nạp một file tool độc lập và làm theo hướng dẫn

## File Skill Nằm Ở Đâu

[Phần tiêu đề “File Skill Nằm Ở Đâu”](#file-skill-n%E1%BA%B1m-%E1%BB%9F-%C4%91%C3%A2u)

Trình cài đặt sẽ ghi file skill vào một thư mục dành riêng cho IDE bên trong dự án. Đường dẫn chính xác phụ thuộc vào IDE bạn chọn khi cài.

IDE / CLIThư mục skillClaude Code`.claude/skills/`Cursor`.cursor/skills/`Windsurf`.windsurf/skills/`IDE khácXem output của trình cài đặt để biết đường dẫn đích

Mỗi skill là một thư mục chứa file `SKILL.md`. Ví dụ với Claude Code, cấu trúc sẽ như sau:

```text

.claude/skills/
├── bmad-help/
│   └── SKILL.md
├── bmad-create-prd/
│   └── SKILL.md
├── bmad-agent-dev/
│   └── SKILL.md
└── ...
```

Tên thư mục quyết định tên skill trong IDE. Ví dụ thư mục `bmad-agent-dev/` sẽ đăng ký skill `bmad-agent-dev`.

## Cách Tìm Danh Sách Skill Của Bạn

[Phần tiêu đề “Cách Tìm Danh Sách Skill Của Bạn”](#c%C3%A1ch-t%C3%ACm-danh-s%C3%A1ch-skill-c%E1%BB%A7a-b%E1%BA%A1n)

Gõ tên skill trong IDE để gọi nó. Một số nền tảng yêu cầu bạn bật skills trong phần cài đặt trước khi chúng xuất hiện.

Chạy `bmad-help` để nhận hướng dẫn có ngữ cảnh về bước tiếp theo.

Agent skills nạp một persona AI chuyên biệt với vai trò, phong cách giao tiếp và menu workflow xác định sẵn. Sau khi được nạp, agent sẽ giữ đúng vai trò và phản hồi qua các trigger trong menu.

Ví dụ skillAgentVai trò`bmad-agent-dev`Amelia (Developer)Triển khai story với mức tuân thủ đặc tả nghiêm ngặt`bmad-pm`John (Product Manager)Tạo và kiểm tra PRD`bmad-architect`Winston (Architect)Thiết kế kiến trúc hệ thống

Xem [Agents](https://docs.bmad-method.org/vi-vn/reference/agents/) để biết danh sách đầy đủ các agent mặc định và trigger của chúng.

### Workflow Skills

[Phần tiêu đề “Workflow Skills”](#workflow-skills)

Workflow skills chạy một quy trình có cấu trúc, nhiều bước mà không cần nạp persona agent trước. Chúng nạp cấu hình workflow rồi thực hiện theo từng bước.

Ví dụ skillMục đích`bmad-product-brief`Tạo product brief — phiên discovery có hướng dẫn khi concept của bạn đã rõ`bmad-prfaq`Bài kiểm tra Working Backwards PRFAQ để stress-test concept sản phẩm`bmad-create-prd`Tạo Product Requirements Document`bmad-create-architecture`Thiết kế kiến trúc hệ thống`bmad-create-epics-and-stories`Tạo epics và stories`bmad-dev-story`Triển khai một story`bmad-code-review`Chạy code review`bmad-quick-dev`Luồng nhanh hợp nhất — làm rõ yêu cầu, lập kế hoạch, triển khai, review và trình bày

Xem [Workflow Map](https://docs.bmad-method.org/vi-vn/reference/workflow-map/) để có tài liệu workflow đầy đủ theo từng phase.

### Task Skills Và Tool Skills

[Phần tiêu đề “Task Skills Và Tool Skills”](#task-skills-v%C3%A0-tool-skills)

Tasks và tools là các thao tác độc lập, không yêu cầu ngữ cảnh agent hay workflow.

**BMad-Help: người dẫn đường thông minh của bạn**

`bmad-help` là giao diện chính để bạn khám phá nên làm gì tiếp theo. Nó kiểm tra dự án, hiểu truy vấn ngôn ngữ tự nhiên và đề xuất bước bắt buộc hoặc tùy chọn tiếp theo dựa trên các module đã cài.

**Các task và tool lõi khác**

Module lõi có 11 công cụ tích hợp sẵn — review, nén tài liệu, brainstorming, quản lý tài liệu và nhiều hơn nữa. Xem [Core Tools](https://docs.bmad-method.org/vi-vn/reference/core-tools/) để có tài liệu tham chiếu đầy đủ.

## Quy Ước Đặt Tên

[Phần tiêu đề “Quy Ước Đặt Tên”](#quy-%C6%B0%E1%BB%9Bc-%C4%91%E1%BA%B7t-t%C3%AAn)

Mọi skill đều dùng tiền tố `bmad-` theo sau là tên mô tả, ví dụ `bmad-agent-dev`, `bmad-create-prd`, `bmad-help`. Xem [Modules](https://docs.bmad-method.org/vi-vn/reference/modules/) để biết các module hiện có.

## Khắc Phục Sự Cố

[Phần tiêu đề “Khắc Phục Sự Cố”](#kh%E1%BA%AFc-ph%E1%BB%A5c-s%E1%BB%B1-c%E1%BB%91)

**Skills không xuất hiện sau khi cài đặt.** Một số nền tảng yêu cầu bật skills thủ công trong phần cài đặt. Hãy kiểm tra tài liệu IDE của bạn hoặc hỏi trợ lý AI cách bật skills. Bạn cũng có thể cần khởi động lại IDE hoặc reload cửa sổ.

**Thiếu skill mà bạn mong đợi.** Trình cài đặt chỉ tạo skill cho những module bạn đã chọn. Hãy chạy lại `npx bmad-method install` và kiểm tra lại phần chọn module. Đồng thời xác nhận rằng file skill thực sự tồn tại trong thư mục dự kiến.

**Skill từ module đã bỏ vẫn còn xuất hiện.** Trình cài đặt không tự xóa các file skill cũ. Hãy xóa các thư mục lỗi thời trong thư mục skills của IDE, hoặc xóa toàn bộ thư mục skills rồi chạy lại trình cài đặt để có tập skill sạch.