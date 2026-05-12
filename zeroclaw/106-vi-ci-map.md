---
title: Ci map
title_vi: Bản đồ CI Workflow
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/ci-map.md
source: git
fetched_at: 2026-05-02T14:52:27.794439244-03:00
rendered_js: false
word_count: 1103
summary: This document provides a comprehensive overview of the GitHub workflows configured for the repository, categorizing them by their function, trigger conditions, and whether they act as mandatory merge gates.
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - github-actions
  - ci-cd
  - workflow-management
  - automation
  - rust-development
  - merge-gates
category: configuration
---
# Bản đồ CI Workflow

> [!info] Tóm tắt
> Tài liệu giải thích từng GitHub workflow, chức năng, trigger, và liệu nó có chặn merge hay không.

## Danh sách Workflow

### Workflow chặn merge

| Workflow | Mô tả | Merge Gate |
|----------|-------|------------|
| `.github/workflows/ci-run.yml` | Rust validation (fmt, clippy, test, smoke build), docs quality, markdown lint, link check | `CI Required Gate` |
| `.github/workflows/workflow-sanity.yml` | Lint GitHub workflow files (`actionlint`, kiểm tra tab) | `Workflow Sanity` |
| `.github/workflows/pr-intake-checks.yml` | Kiểm tra PR an toàn trước CI (template, whitespace, conflict markers) | `PR Intake Checks` |

**Chi tiết `ci-run.yml`:**
- Chạy `cargo fmt --all -- --check`, `cargo clippy --locked --all-targets -- -D clippy::correctness`
- Strict delta lint gate trên các dòng Rust thay đổi
- `test` + smoke release build
- Kiểm tra chất lượng tài liệu khi tài liệu thay đổi (`markdownlint` chỉ chặn vấn đề trên dòng thay đổi; link check chỉ quét link mới thêm trên dòng thay đổi)
- PR/Rust push yêu cầu `lint` + `test` + `build`
- PR thay đổi workflow yêu cầu review từ login trong `WORKFLOW_OWNER_LOGINS`
- Lint gate chạy trước `test`/`build`; thất bại trên PR đăng comment phản hồi hành động với tên gate thất bại và lệnh sửa cục bộ

### Workflow quan trọng nhưng không chặn

| Workflow | Mục đích | Trigger |
|----------|----------|---------|
| `.github/workflows/pub-docker-img.yml` | Kiểm tra smoke Docker trên PR master, publish image khi push tag (`v*`) | Push tag, PR master |
| `.github/workflows/sec-audit.yml` | Advisory phụ thuộc (`rustsec/audit-check` SHA pinned) và kiểm tra chính sách/giấy phép (`cargo deny`) | Push PR master, lịch tuần |
| `.github/workflows/sec-codeql.yml` | Phân tích tĩnh bảo mật theo lịch/thủ công | Lịch, thủ công |
| `.github/workflows/sec-vorpal-reviewdog.yml` | Quét phản hồi secure-coding thủ công cho files non-Rust (`.py`, `.js`, `.ts`, `.tsx`) | Thủ công |
| `.github/workflows/pub-release.yml` | Build release artifact (xác minh/thủ công/theo lịch), publish GitHub release khi push tag | Push tag, thủ công |
| `.github/workflows/pub-homebrew-core.yml` | PR bump formula Homebrew core thủ công | Thủ công |
| `.github/workflows/pr-label-policy-check.yml` | Xác thực chính sách label contributor | Push/PR thay đổi label policy |
| `.github/workflows/test-rust-build.yml` | Rust setup/cache có thể tái sử dụng | Tái sử dụng trong workflows khác |

### Tự động hóa repository tùy chọn

| Workflow | Mục đích | Chi tiết |
|----------|----------|----------|
| `.github/workflows/pr-labeler.yml` | Tự động gán label phạm vi/đường dẫn/rủi ro/kích thước/module | Hỗ trợ `workflow_dispatch` mode `audit|repair`; loại bỏ trùng lặp phân cấp nhãn; áp dụng bậc contributor theo PR đã merge; heuristic rủi ro cao: `src/security/**`, `src/runtime/**`, `src/gateway/**`, `src/tools/**`, `.github/workflows/**` |
| `.github/workflows/pr-auto-response.yml` | Giới thiệu contributor lần đầu + phân tuyến dựa label | Áp dụng bậc contributor trên issue theo PR đã merge; nhãn bậc contributor được quản lý tự động |
| `.github/workflows/pr-check-stale.yml` | Tự động hóa vòng đời stale issue/PR | - |
| `.github/dependabot.yml` | PR cập nhật phụ thuộc được nhóm, giới hạn tốc độ | Cập nhật Cargo + GitHub Actions |
| `.github/workflows/pr-check-status.yml` | Nhắc nhở PR stale-nhưng-còn-hoạt-động rebase/re-run kiểm tra | - |

## Bản đồ Trigger

| Workflow | Trigger |
|----------|---------|
| `CI` | Push master, PR master |
| `Docker` | Push tag (`v*`), PR master (smoke), thủ công (smoke) |
| `Release` | Push tag (`v*`), lịch tuần (xác minh), thủ công (xác minh/publish) |
| `Pub Homebrew Core` | Thủ công |
| `Security Audit` | Push master, PR master, lịch tuần |
| `Sec Vorpal Reviewdog` | Thủ công |
| `Workflow Sanity` | PR/push thay đổi `.github/workflows/**`, `.github/*.yml`, `.github/*.yaml` |
| `PR Intake Checks` | `pull_request_target` khi opened/reopened/synchronize/edited/ready_for_review |
| `Label Policy Sanity` | PR/push thay đổi `.github/label-policy.json`, `.github/workflows/pr-labeler.yml`, `.github/workflows/pr-auto-response.yml` |
| `PR Labeler` | Sự kiện vòng đời `pull_request_target` |
| `PR Auto Responder` | Issue opened/labeled, `pull_request_target` opened/labeled |
| `Stale PR Check` | Lịch hàng ngày, thủ công |
| `Dependabot` | Tất cả PR cập nhật nhắm master |
| `PR Hygiene` | Lịch 12 giờ, thủ công |

## Hướng dẫn triage nhanh

1. **`CI Required Gate` thất bại** → Kiểm tra `.github/workflows/ci-run.yml`
2. **Docker thất bại trên PR** → Kiểm tra job `pr-smoke` trong `.github/workflows/pub-docker-img.yml`
3. **Release thất bại (tag/thủ công/lịch)** → Kiểm tra `.github/workflows/pub-release.yml` và job `prepare`
4. **Lỗi publish formula Homebrew** → Kiểm tra tóm tắt output `.github/workflows/pub-homebrew-core.yml` và biến bot token/fork
5. **Security thất bại** → Kiểm tra `.github/workflows/sec-audit.yml` và `deny.toml`
6. **Lỗi cú pháp/lint workflow** → Kiểm tra `.github/workflows/workflow-sanity.yml`
7. **PR intake thất bại** → Kiểm tra comment sticky `.github/workflows/pr-intake-checks.yml` và run log
8. **Lỗi parity chính sách nhãn** → Kiểm tra `.github/workflows/pr-label-policy-check.yml`
9. **Lỗi tài liệu trong CI** → Kiểm tra log job `docs-quality` trong `.github/workflows/ci-run.yml`
10. **Lỗi strict delta lint trong CI** → Kiểm tra log job `lint-strict-delta` và so sánh phạm vi diff `BASE_SHA`

## Quy tắc bảo trì

- Giữ kiểm tra chặn merge mang tính quyết định và tái tạo được (`--locked` khi áp dụng)
- Tuân theo `docs/release-process.md` cho kiểm tra trước publish và kỷ luật tag
- Giữ chính sách chất lượng Rust chặn merge nhất quán giữa `.github/workflows/ci-run.yml`, `dev/ci.sh` và `.githooks/pre-push`
- Dùng `./scripts/ci/rust_strict_delta_gate.sh` (hoặc `./dev/ci.sh lint-delta`) làm merge gate nghiêm ngặt gia tăng cho dòng Rust thay đổi
- Chạy kiểm tra lint nghiêm ngặt đầy đủ thường xuyên qua `./scripts/ci/rust_quality_gate.sh --strict`
- Giữ gating markdown tài liệu theo gia tăng qua `./scripts/ci/docs_quality_gate.sh`
- Giữ gating link tài liệu theo gia tăng qua `./scripts/ci/collect_changed_links.py` + lychee
- Ưu tiên quyền workflow tường minh (least privilege)
- Giữ chính sách nguồn Actions hạn chế theo allowlist đã phê duyệt
- Sử dụng bộ lọc đường dẫn cho workflows tốn kém
- Giữ kiểm tra chất lượng tài liệu ít nhiễu (markdown gia tăng + link mới thêm gia tăng)
- Giữ khối lượng cập nhật phụ thuộc được kiểm soát (nhóm + giới hạn PR)
- Tránh kết hợp tự động hóa giới thiệu/cộng đồng với logic gating merge

## Kiểm soát tác dụng phụ tự động hóa

- Ưu tiên tự động hóa mang tính quyết định có thể ghi đè thủ công (`risk: manual`) khi ngữ cảnh tinh tế
- Giữ comment auto-response không trùng lặp để tránh nhiễu triage
- Giữ hành vi tự đóng trong phạm vi issue; maintainer quyết định đóng/merge PR
- Nếu tự động hóa sai, sửa nhãn trước, rồi tiếp tục review với lý do rõ ràng
- Dùng nhãn `superseded` / `stale-candidate` để cắt tỉa PR trùng lặp hoặc ngủ đông trước review sâu

#zeroclaw #github-actions #ci-cd #automation