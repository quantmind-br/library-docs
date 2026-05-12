---
title: Actions source policy
title_vi: Chính sách nguồn Actions (Giai đoạn 1)
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/actions-source-policy.md
source: git
fetched_at: 2026-05-02T14:50:59.733343879-03:00
rendered_js: false
word_count: 461
summary: Tài liệu này xác định chính sách kiểm soát nguồn GitHub Actions giai đoạn 1, bao gồm danh sách các action được phép (allowlist), quy trình quản lý thay đổi và chiến lược bảo mật cho workflow trong repository.
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - github-actions
  - security-policy
  - supply-chain-security
  - ci-cd-governance
  - workflow-automation
  - allowlist-management
category: configuration
---
# Chính sách nguồn Actions (Giai đoạn 1)

> [!info] Tóm tắt
> Chính sách kiểm soát nguồn GitHub Actions giai đoạn 1, xác định allowlist action, quy trình quản lý thay đổi và chiến lược bảo mật cho repository.

## Chính sách hiện tại

- **Quyền Actions repository**: enabled
- **Chế độ action cho phép**: selected
- **Yêu cầu pin SHA**: false (Giai đoạn 2)

### Allowlist action

| Action | Mô tả |
|--------|-------|
| `actions/*` | First-party actions (cache, checkout, artifacts, etc.) |
| `docker/*` | Docker official actions |
| `dtolnay/rust-toolchain@*` | Rust toolchain installer |
| `DavidAnson/markdownlint-cli2-action@*` | Markdown linting |
| `lycheeverse/lychee-action@*` | Link checker |
| `EmbarkStudios/cargo-deny-action@*` | Cargo dependency audit |
| `rustsec/audit-check@*` | Security audit checker |
| `rhysd/actionlint@*` | GitHub Actions linter |
| `softprops/action-gh-release@*` | GitHub release automation |
| `sigstore/cosign-installer@*` | Cosign installer for artifact signing |
| `useblacksmith/*` | Self-hosted runner infrastructure (Blacksmith) |

## Xuất kiểm soát thay đổi

```bash
# Xuất cấu hình hiện tại
gh api repos/zeroclaw-labs/zeroclaw/actions/permissions
gh api repos/zeroclaw-labs/zeroclaw/actions/permissions/selected-actions
```

Ghi lại mỗi thay đổi chính sách với:
- Ngày/giờ thay đổi (UTC)
- Tác nhân
- Lý do
- Delta allowlist (mẫu thêm/xóa)
- Ghi chú rollback

## Mục đích giai đoạn này

- Giảm rủi ro chuỗi cung ứng từ marketplace action chưa review
- Bảo tồn CI/CD hiện tại với chi phí migration thấp
- Chuẩn bị cho Giai đoạn 2 pin SHA đầy đủ

## Bảo vệ workflow agentic

Do repository có khối lượng thay đổi do agent tạo ra cao:

- PR thêm/thay đổi `uses:` action phải bao gồm ghi chú tác động allowlist
- Action bên thứ ba mới yêu cầu review maintainer tường minh
- Chỉ mở rộng allowlist cho action bị thiếu đã xác minh
- Tránh wildcard rộng; giữ hướng dẫn rollback trong mô tả PR

## Checklist xác thực sau thay đổi allowlist

1. `CI`
2. `Docker`
3. `Security Audit`
4. `Workflow Sanity`
5. `Release` (khi an toàn)

**Failure mode**: `action is not allowed by policy`

Nếu gặp lỗi, chỉ thêm action tin cậy còn thiếu cụ thể, chạy lại và ghi lý do.

## Ghi chú quét gần đây

- **2026-02-17**: Cache phụ thuộc Rust migrate từ `Swatinem/rust-cache` sang `useblacksmith/rust-cache`
  - Không cần allowlist mới (`useblacksmith/*` đã có)

- **2026-02-16**: Phụ thuộc ẩn phát hiện trong `release-beta-on-push.yml`: `sigstore/cosign-installer@...`
  - Đã thêm: `sigstore/cosign-installer@*`

- **2026-02-16**: Migration Blacksmith chặn thực thi
  - Đã thêm: `useblacksmith/*`
  - Actions: `useblacksmith/setup-docker-builder@v1`, `useblacksmith/build-push-action@v2`

- **2026-02-17**: Cập nhật security audit
  - Đã thêm: `rustsec/audit-check@*`
  - Thay thế `cargo install cargo-audit` bằng `rustsec/audit-check@69366f33c96575abad1ee0dba8212993eecbe998` trong `security.yml`

## Rollback khẩn cấp

1. Tạm thời đặt chính sách Actions về `all`
2. Khôi phục allowlist đã chọn sau khi xác định mục còn thiếu
3. Ghi lại sự cố và delta allowlist cuối cùng

#zeroclaw #github-actions #security-policy #ci-cd