---
title: Agents
url: https://docs.bmad-method.org/vi-vn/reference/agents/
source: sitemap
fetched_at: 2026-04-08T11:32:23.668913523-03:00
rendered_js: false
word_count: 392
summary: This document serves as a reference guide listing the default agents available within the BMM agile suite, detailing their corresponding skill IDs, associated trigger codes, and primary workflows. It also explains the two types of triggers—workflow and conversational—and when parameters are required for each.
tags:
    - agent-reference
    - bmm-suite
    - skill-ids
    - trigger-types
    - workflow-guide
category: reference
---

## Các Agent Mặc Định

[Phần tiêu đề “Các Agent Mặc Định”](#c%C3%A1c-agent-m%E1%BA%B7c-%C4%91%E1%BB%8Bnh)

Trang này liệt kê các agent mặc định của BMM (bộ Agile suite) được cài cùng với BMad Method, bao gồm skill ID, trigger menu và workflow chính của chúng. Mỗi agent được gọi dưới dạng một skill.

- Mỗi agent đều có sẵn dưới dạng một skill do trình cài đặt tạo ra. Skill ID, ví dụ `bmad-dev`, được dùng để gọi agent.
- Trigger là các mã menu ngắn, ví dụ `CP`, cùng với các fuzzy match hiển thị trong menu của từng agent.
- Việc tạo test QA do workflow skill `bmad-qa-generate-e2e-tests` đảm nhận, khả dụng thông qua Developer agent. Module Test Architect (TEA) đầy đủ nằm trong một module riêng.

AgentSkill IDTriggerWorkflow chínhAnalyst (Mary)`bmad-analyst``BP`, `RS`, `CB`, `WB`, `DP`Brainstorm Project, Research, Create Brief, PRFAQ Challenge, Document ProjectProduct Manager (John)`bmad-pm``CP`, `VP`, `EP`, `CE`, `IR`, `CC`Create/Validate/Edit PRD, Create Epics and Stories, Implementation Readiness, Correct CourseArchitect (Winston)`bmad-architect``CA`, `IR`Create Architecture, Implementation ReadinessDeveloper (Amelia)`bmad-agent-dev``DS`, `QD`, `QA`, `CR`, `SP`, `CS`, `ER`Dev Story, Quick Dev, QA Test Generation, Code Review, Sprint Planning, Create Story, Epic RetrospectiveUX Designer (Sally)`bmad-ux-designer``CU`Create UX DesignTechnical Writer (Paige)`bmad-tech-writer``DP`, `WD`, `US`, `MG`, `VD`, `EC`Document Project, Write Document, Update Standards, Mermaid Generate, Validate Doc, Explain Concept

## Các Loại Trigger

[Phần tiêu đề “Các Loại Trigger”](#c%C3%A1c-lo%E1%BA%A1i-trigger)

Trigger trong menu agent dùng hai kiểu gọi khác nhau. Biết trigger thuộc kiểu nào sẽ giúp bạn cung cấp đúng đầu vào.

### Trigger workflow (không cần tham số)

[Phần tiêu đề “Trigger workflow (không cần tham số)”](#trigger-workflow-kh%C3%B4ng-c%E1%BA%A7n-tham-s%E1%BB%91)

Phần lớn trigger sẽ nạp một file workflow có cấu trúc. Bạn gõ mã trigger, agent sẽ bắt đầu workflow và nhắc bạn nhập thông tin ở từng bước.

Ví dụ: `CP` (Create PRD), `DS` (Dev Story), `CA` (Create Architecture), `QD` (Quick Dev)

### Trigger hội thoại (cần tham số)

[Phần tiêu đề “Trigger hội thoại (cần tham số)”](#trigger-h%E1%BB%99i-tho%E1%BA%A1i-c%E1%BA%A7n-tham-s%E1%BB%91)

Một số trigger sẽ mở cuộc hội thoại tự do thay vì chạy workflow có cấu trúc. Khi đó bạn cần mô tả yêu cầu của mình cùng với mã trigger.

AgentTriggerNội dung cần cung cấpTechnical Writer (Paige)`WD`Mô tả tài liệu cần viếtTechnical Writer (Paige)`US`Sở thích hoặc quy ước muốn thêm vào standardsTechnical Writer (Paige)`MG`Mô tả sơ đồ và loại sơ đồ (sequence, flowchart, v.v.)Technical Writer (Paige)`VD`Tài liệu cần kiểm tra và các vùng trọng tâmTechnical Writer (Paige)`EC`Tên khái niệm cần giải thích

**Ví dụ:**

```text

WD Write a deployment guide for our Docker setup
MG Create a sequence diagram showing the auth flow
EC Explain how the module system works
```