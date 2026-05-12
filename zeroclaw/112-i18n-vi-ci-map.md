---
title: Ci map
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/ci-map.md
source: git
fetched_at: 2026-05-02T14:51:05.726012239-03:00
rendered_js: false
word_count: 1672
summary: Tài liệu này cung cấp bản đồ chi tiết về các GitHub Actions workflows, phân loại chúng theo vai trò kiểm soát merge và các quy trình tự động hóa bảo trì cho repository.
tags:
    - github-actions
    - ci-cd
    - workflow-automation
    - merge-gate
    - repository-management
    - rust-development
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Bản đồ CI Workflow

Tài liệu này giải thích từng GitHub workflow làm gì, khi nào chạy và liệu nó có nên chặn merge hay không.

> [!tip]
> Để biết hành vi phân phối theo từng sự kiện qua PR, merge, push và release, xem [[149-contributing-ci-map|.github/workflows/master-branch-flow.md]].

---

## 1. Chặn merge và Tùy chọn

Các kiểm tra chặn merge nên giữ nhỏ và mang tính quyết định. Các kiểm tra tùy chọn hữu ích cho tự động hóa và bảo trì, nhưng không nên chặn phát triển bình thường.

### 1.1 Chặn merge

| Workflow | Tên Gate | Mục đích | Merge Gate |
|---|---|---|---|
| `.github/workflows/ci-run.yml` | `CI` | Rust validation (`cargo fmt --all -- --check`, `cargo clippy --locked --all-targets -- -D clippy::correctness`, strict delta lint gate trên các dòng Rust thay đổi, `test`, kiểm tra smoke release build) + kiểm tra chất lượng tài liệu khi tài liệu thay đổi (`markdownlint` chỉ chặn các vấn đề trên dòng thay đổi; link check chỉ quét các link mới được thêm trên dòng thay đổi) | `CI Required Gate` |
| `.github/workflows/workflow-sanity.yml` | `Workflow Sanity` | Lint các file GitHub workflow (`actionlint`, kiểm tra tab) | Khuyến nghị cho các PR thay đổi workflow |
| `.github/workflows/pr-intake-checks.yml` | `PR Intake Checks` | Kiểm tra PR an toàn trước CI (độ đầy đủ template, tab/trailing-whitespace/conflict marker trên dòng thêm) với comment sticky phản hồi ngay lập tức | Khuyến nghị |

**Hành vi bổ sung:**
- Đối với PR và push ảnh hưởng Rust, `CI Required Gate` yêu cầu `lint` + `test` + `build` (không có shortcut chỉ build trên PR)
- Các PR thay đổi `.github/workflows/**` yêu cầu ít nhất một review phê duyệt từ login trong `WORKFLOW_OWNER_LOGINS` (fallback biến repository: `theonlyhennygod,JordanTheJet,SimianAstronaut7`)
- Lint gate chạy trước `test`/`build`; khi lint/docs gate thất bại trên PR, CI đăng comment phản hồi hành động được với tên gate thất bại và các lệnh sửa cục bộ

### 1.2 Quan trọng nhưng không chặn

| Workflow | Tên Gate | Mục đích |
|---|---|---|
| `.github/workflows/pub-docker-img.yml` | `Docker` | Kiểm tra Docker smoke trên PR lên `master` và publish image khi push tag (`v*`) only |
| `.github/workflows/sec-audit.yml` | `Security Audit` | Advisory phụ thuộc (`rustsec/audit-check`, SHA được pin) và kiểm tra chính sách/giấy phép (`cargo deny`) |
| `.github/workflows/sec-codeql.yml` | `CodeQL Analysis` | Phân tích tĩnh theo lịch/thủ công để phát hiện vấn đề bảo mật |
| `.github/workflows/sec-vorpal-reviewdog.yml` | `Sec Vorpal Reviewdog` | Quét phản hồi secure-coding thủ công cho các file non-Rust được hỗ trợ (`.py`, `.js`, `.jsx`, `.ts`, `.tsx`) sử dụng annotation reviewdog. Kiểm soát nhiễu: loại trừ các đường dẫn test/fixture phổ biến và pattern file test theo mặc định (`include_tests=false`) |
| `.github/workflows/pub-release.yml` | `Release` | Build release artifact ở chế độ xác minh (thủ công/theo lịch) và publish GitHub release khi push tag hoặc chế độ publish thủ công |
| `.github/workflows/pub-homebrew-core.yml` | `Pub Homebrew Core` | Luồng PR bump formula Homebrew core thủ công, do bot sở hữu cho các tagged release. Bảo vệ: release tag phải khớp version `Cargo.toml` |
| `.github/workflows/pr-label-policy-check.yml` | `Label Policy Sanity` | Xác thực chính sách bậc contributor dùng chung trong `.github/label-policy.json` và đảm bảo các label workflow sử dụng chính sách đó |
| `.github/workflows/test-rust-build.yml` | `Rust Reusable Job` | Rust setup/cache có thể tái sử dụng + trình chạy lệnh cho các workflow-call consumer |

### 1.3 Tự động hóa repository tùy chọn

| Workflow | Tên Gate | Mục đích |
|---|---|---|
| `.github/workflows/pr-labeler.yml` | `PR Labeler` | Nhãn phạm vi/đường dẫn + nhãn kích thước/rủi ro + nhãn module chi tiết (`<module>: <component>`). Mô tả nhãn được quản lý tự động như tooltip khi di chuột để giải thích từng quy tắc phán đoán tự động. Từ khóa liên quan đến provider trong các thay đổi provider/config/onboard/integration được thăng cấp lên nhãn `provider:*` (ví dụ `provider:kimi`, `provider:deepseek`). Loại bỏ trùng lặp phân cấp chỉ giữ nhãn phạm vi cụ thể nhất (ví dụ `tool:composio` triệt tiêu `tool:core` và `tool`). Namespace module được nén gọn — một module cụ thể giữ `prefix:component`; nhiều module cụ thể thu gọn thành chỉ `prefix`. Áp dụng bậc contributor trên PR theo số PR đã merge (`trusted` >=5, `experienced` >=10, `principal` >=20, `distinguished` >=50). Bộ nhãn cuối cùng được sắp xếp theo ưu tiên (`risk:*` đầu tiên, sau đó `size:*`, rồi bậc contributor, cuối là nhãn module/đường dẫn). Màu nhãn được quản lý theo thứ tự hiển thị để tạo gradient trái-phải mượt mà khi có nhiều nhãn. Quản trị thủ công: hỗ trợ `workflow_dispatch` với `mode=audit|repair` để kiểm tra/sửa metadata nhãn được quản lý drift trên toàn repository. Nhãn rủi ro + kích thước được tự sửa khi chỉnh sửa nhãn PR thủ công (sự kiện `labeled`/`unlabeled`); áp dụng `risk: manual` khi maintainer cố ý ghi đè lựa chọn rủi ro tự động. Đường dẫn heuristic rủi ro cao: `src/security/**`, `src/runtime/**`, `src/gateway/**`, `src/tools/**`, `.github/workflows/**`. Bảo vệ: maintainer có thể áp dụng `risk: manual` để đóng băng tính toán lại rủi ro tự động |
| `.github/workflows/pr-auto-response.yml` | `PR Auto Responder` | Giới thiệu contributor lần đầu + phân tuyến dựa trên nhãn (`r:support`, `r:needs-repro`, v.v.). Áp dụng bậc contributor trên issue theo số PR đã merge (`trusted` >=5, `experienced` >=10, `principal` >=20, `distinguished` >=50), khớp chính xác ngưỡng bậc PR. Nhãn bậc contributor được coi là do tự động hóa quản lý (thêm/xóa thủ công trên PR/issue bị tự sửa). Bảo vệ: các luồng đóng dựa trên nhãn chỉ dành cho issue; PR không bao giờ bị tự đóng bởi nhãn route |
| `.github/workflows/pr-check-stale.yml` | `Stale` | Tự động hóa vòng đời issue/PR stale |
| `.github/dependabot.yml` | `Dependabot` | PR cập nhật phụ thuộc được nhóm, giới hạn tốc độ (Cargo + GitHub Actions) |
| `.github/workflows/pr-check-status.yml` | `PR Hygiene` | Nhắc nhở các PR stale-nhưng-còn-hoạt-động để rebase/re-run các kiểm tra bắt buộc trước khi hàng đợi bị đói |

---

## 2. Bản đồ Trigger

| Workflow | Trigger |
|---|---|
| `CI` | Push lên `master`, PR lên `master` |
| `Docker` | Push tag (`v*`) để publish, PR lên `master` tương ứng để smoke build, dispatch thủ công chỉ smoke |
| `Release` | Push tag (`v*`), lịch hàng tuần (chỉ xác minh), dispatch thủ công (xác minh hoặc publish) |
| `Pub Homebrew Core` | Dispatch thủ công only |
| `Security Audit` | Push lên `master`, PR lên `master`, lịch hàng tuần |
| `Sec Vorpal Reviewdog` | Dispatch thủ công only |
| `Workflow Sanity` | PR/push khi `.github/workflows/**`, `.github/*.yml` hoặc `.github/*.yaml` thay đổi |
| `PR Intake Checks` | `pull_request_target` khi opened/reopened/synchronize/edited/ready_for_review |
| `Label Policy Sanity` | PR/push khi `.github/label-policy.json`, `.github/workflows/pr-labeler.yml` hoặc `.github/workflows/pr-auto-response.yml` thay đổi |
| `PR Labeler` | Sự kiện vòng đời `pull_request_target` |
| `PR Auto Responder` | Issue opened/labeled, `pull_request_target` opened/labeled |
| `Stale PR Check` | Lịch hàng ngày, dispatch thủ công |
| `Dependabot` | Tất cả PR cập nhật nhắm vào `master` |
| `PR Hygiene` | Lịch mỗi 12 giờ, dispatch thủ công |

---

## 3. Hướng dẫn triage nhanh

1. `CI Required Gate` thất bại: bắt đầu với [[149-contributing-ci-map|.github/workflows/ci-run.yml]].
2. Docker thất bại trên PR: kiểm tra job `pr-smoke` trong [[149-contributing-ci-map|.github/workflows/pub-docker-img.yml]].
3. Release thất bại (tag/thủ công/theo lịch): kiểm tra [[149-contributing-ci-map|.github/workflows/pub-release.yml]] và kết quả job `prepare`.
4. Lỗi publish formula Homebrew: kiểm tra output tóm tắt [[149-contributing-ci-map|.github/workflows/pub-homebrew-core.yml]] và biến bot token/fork.
5. Security thất bại: kiểm tra [[149-contributing-ci-map|.github/workflows/sec-audit.yml]] và `deny.toml`.
6. Lỗi cú pháp/lint workflow: kiểm tra [[112-i18n-vi-ci-map#workflow-sanity|Workflow Sanity]].
7. PR intake thất bại: kiểm tra comment sticky [[112-i18n-vi-ci-map#pr-intake-checks|PR Intake Checks]] và run log.
8. Lỗi parity chính sách nhãn: kiểm tra [[112-i18n-vi-ci-map#label-policy-sanity|Label Policy Sanity]].
9. Lỗi tài liệu trong CI: kiểm tra log job `docs-quality` trong [[112-i18n-vi-ci-map#ci|CI]].
10. Lỗi strict delta lint trong CI: kiểm tra log job `lint-strict-delta` và so sánh với phạm vi diff `BASE_SHA`.

---

## 4. Quy tắc bảo trì

- Giữ các kiểm tra chặn merge mang tính quyết định và tái tạo được (`--locked` khi áp dụng được).
- Tuân theo [[158-contributing-release-process|docs/release-process.md]] để kiểm tra trước khi publish và kỷ luật tag.
- Giữ chính sách chất lượng Rust chặn merge nhất quán giữa [[112-i18n-vi-ci-map#ci|CI]], `dev/ci.sh` và `.githooks/pre-push` (`./scripts/ci/rust_quality_gate.sh` + `./scripts/ci/rust_strict_delta_gate.sh`).
- Dùng `./scripts/ci/rust_strict_delta_gate.sh` (hoặc `./dev/ci.sh lint-delta`) làm merge gate nghiêm ngặt gia tăng cho các dòng Rust thay đổi.
- Chạy kiểm tra lint nghiêm ngặt đầy đủ thường xuyên qua `./scripts/ci/rust_quality_gate.sh --strict` (ví dụ qua `./dev/ci.sh lint-strict`) và theo dõi việc dọn dẹp trong các PR tập trung.
- Giữ gating markdown tài liệu theo gia tăng qua `./scripts/ci/docs_quality_gate.sh` (chặn vấn đề dòng thay đổi, báo cáo vấn đề baseline riêng).
- Giữ gating link tài liệu theo gia tăng qua `./scripts/ci/collect_changed_links.py` + lychee (chỉ kiểm tra link mới thêm trên dòng thay đổi).
- Ưu tiên quyền workflow tường minh (least privilege).
- Giữ chính sách nguồn Actions hạn chế theo allowlist đã được phê duyệt (xem [[101-i18n-vi-actions-source-policy|docs/actions-source-policy.md]]).
- Sử dụng bộ lọc đường dẫn cho các workflow tốn kém khi thực tế.
- Giữ kiểm tra chất lượng tài liệu ít nhiễu (markdown gia tăng + kiểm tra link mới thêm gia tăng).
- Giữ khối lượng cập nhật phụ thuộc được kiểm soát (nhóm + giới hạn PR).
- Tránh kết hợp tự động hóa giới thiệu/cộng đồng với logic gating merge.

---

## 5. Kiểm soát tác dụng phụ tự động hóa

- Ưu tiên tự động hóa mang tính quyết định có thể ghi đè thủ công (`risk: manual`) khi ngữ cảnh tinh tế.
- Giữ comment auto-response không trùng lặp để tránh nhiễu triage.
- Giữ hành vi tự đóng trong phạm vi issue; maintainer quyết định đóng/merge PR.
- Nếu tự động hóa sai, sửa nhãn trước, rồi tiếp tục review với lý do rõ ràng.
- Dùng nhãn `superseded` / `stale-candidate` để cắt tỉa PR trùng lặp hoặc ngủ đông trước khi review sâu.

#tags #github-actions #ci-cd #workflow-automation #merge-gate #repository-management #rust-development