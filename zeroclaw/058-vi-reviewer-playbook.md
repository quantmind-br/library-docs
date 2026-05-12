---
title: Reviewer playbook
date: 2026-05-05T00:00:00Z
optimized: true
tags:
  - pull-request-workflow
  - code-review
  - risk-management
  - maintainer-guide
  - triage-process
  - developer-productivity
---

# Sổ tay Reviewer

Tài liệu hướng dẫn vận hành cho reviewer nhằm chuẩn hóa quy trình đánh giá mã nguồn.

Để điều hướng tài liệu rộng hơn, xem [[055-vi-pr-workflow|pr-workflow]].

## Tóm tắt

- **Mục đích:** định nghĩa mô hình vận hành reviewer mang tính quyết định, duy trì chất lượng review cao khi khối lượng PR lớn.
- **Đối tượng:** maintainer, reviewer và reviewer có hỗ trợ agent.
- **Phạm vi:** triage intake, phân tuyến rủi ro-sang-độ-sâu, kiểm tra review sâu, ghi đè tự động hóa và giao thức bàn giao.
- **Ngoài phạm vi:** thay thế thẩm quyền chính sách PR trong `CONTRIBUTING.md` hoặc thẩm quyền workflow trong các file CI.

---

## Lối tắt theo tình huống review

### Intake thất bại trong 5 phút đầu

1. Để lại comment dạng checklist hành động được.
2. Dừng review sâu cho đến khi các vấn đề intake được sửa.

Xem: [[058-vi-reviewer-playbook#triage-intake-năm-phút|Triage intake]]

### Rủi ro cao hoặc không rõ ràng

1. Mặc định coi là `risk: high`.
2. Yêu cầu review sâu và bằng chứng rollback rõ ràng.

Xem: [[058-vi-reviewer-playbook#ma-trận-quyết-định-độ-sâu-review|Ma trận quyết định]]

### Kết quả tự động hóa sai/ồn ào

1. Áp dụng giao thức ghi đè (`risk: manual`, loại bỏ trùng lặp comment/nhãn).
2. Tiếp tục review với lý do rõ ràng.

Xem: [[058-vi-reviewer-playbook#ghi-đè-tự-động-hóa|Ghi đè tự động hóa]]

### Cần bàn giao review

1. Bàn giao với phạm vi/rủi ro/validation/vấn đề chặn.
2. Giao hành động tiếp theo cụ thể.

Xem: [[058-vi-reviewer-playbook#giao-thức-bàn-giao|Giao thức bàn giao]]

---

## Ma trận quyết định độ sâu review

| Nhãn rủi ro | Đường dẫn thường gặp | Độ sâu review tối thiểu | Bằng chứng bắt buộc |
|---|---|---|---|
| `risk: low` | docs/tests/chore, thay đổi không ảnh hưởng runtime | 1 reviewer + gate CI | validation cục bộ nhất quán + không mơ hồ hành vi |
| `risk: medium` | `src/providers/**`, `src/channels/**`, `src/memory/**`, `src/config/**` | 1 reviewer có hiểu biết hệ thống con + xác minh hành vi | bằng chứng kịch bản tập trung + tác dụng phụ rõ ràng |
| `risk: high` | `src/security/**`, `src/runtime/**`, `src/gateway/**`, `src/tools/**`, `.github/workflows/**` | triage nhanh + review sâu + sẵn sàng rollback | kiểm tra bảo mật/failure mode + rõ ràng về rollback |

Khi không chắc chắn, coi là `risk: high`.

Nếu việc gán nhãn rủi ro tự động không đúng ngữ cảnh, maintainer có thể áp dụng `risk: manual` và đặt nhãn `risk:*` cuối cùng một cách tường minh.

---

## Quy trình review tiêu chuẩn

### Triage intake năm phút

Cho mỗi PR mới:

1. Xác nhận độ đầy đủ template (`summary`, `validation`, `security`, `rollback`).
2. Xác nhận nhãn hiện diện và hợp lý:
   - `size:*`, `risk:*`
   - nhãn phạm vi (ví dụ `provider`, `channel`, `security`)
   - nhãn module (`channel:*`, `provider:*`, `tool:*`)
   - nhãn contributor khi áp dụng
3. Xác nhận trạng thái tín hiệu CI (`CI Required Gate`).
4. Xác nhận phạm vi là một mối quan tâm (từ chối mega-PR hỗn hợp trừ khi có lý do).
5. Xác nhận các yêu cầu tính riêng tư/vệ sinh dữ liệu đã được thỏa mãn.

Nếu bất kỳ yêu cầu intake nào thất bại, để lại comment dạng checklist hành động thay vì review sâu.

### Checklist fast-lane (tất cả PR)

- Ranh giới phạm vi rõ ràng và đáng tin cậy.
- Các lệnh validation hiện diện và kết quả nhất quán.
- Các thay đổi hành vi hướng người dùng đã được ghi lại.
- Tác giả thể hiện hiểu biết về hành vi và blast radius.
- Đường dẫn rollback cụ thể (không chỉ là "revert").
- Tác động tương thích/migration rõ ràng.
- Không có rò rỉ dữ liệu cá nhân/nhạy cảm trong diff artifact.
- Nếu có ngôn ngữ liên quan đến danh tính, sử dụng vai trò gốc ZeroClaw/dự án.
- Quy ước đặt tên và ranh giới kiến trúc tuân theo hợp đồng dự án (`AGENTS.md`, `CONTRIBUTING.md`).

### Checklist review sâu (rủi ro cao)

Với PR rủi ro cao, xác minh ít nhất một ví dụ cụ thể trong mỗi hạng mục:

- **Ranh giới bảo mật:** hành vi deny-by-default được bảo tồn, không mở rộng phạm vi ngẫu nhiên.
- **Failure mode:** xử lý lỗi rõ ràng và suy giảm an toàn.
- **Ổn định hợp đồng:** tương thích CLI/config/API được bảo tồn hoặc migration được ghi lại.
- **Observability:** lỗi có thể chẩn đoán mà không rò rỉ secret.
- **An toàn rollback:** đường dẫn revert và blast radius rõ ràng.

### Phong cách kết quả comment review

Ưu tiên comment dạng checklist với kết quả rõ ràng:

- **Sẵn sàng merge** (giải thích lý do).
- **Cần tác giả hành động** (danh sách vấn đề chặn có thứ tự).
- **Cần review bảo mật/runtime sâu hơn** (nêu rõ rủi ro và bằng chứng yêu cầu).

Tránh comment mơ hồ tạo ra độ trễ qua lại không cần thiết.

---

## Triage issue và quản trị backlog

### Sổ tay nhãn triage issue

Dùng nhãn để giữ backlog có thể hành động:

- `r:needs-repro` cho báo cáo lỗi chưa đầy đủ.
- `r:support` cho câu hỏi sử dụng/hỗ trợ nên chuyển hướng ngoài bug backlog.
- `duplicate` / `invalid` cho trùng lặp/nhiễu không thể hành động.
- `no-stale` cho công việc đã được chấp nhận đang chờ vấn đề chặn bên ngoài.
- Yêu cầu biên tập khi log/payload chứa định danh cá nhân hoặc dữ liệu nhạy cảm.

### Giao thức cắt tỉa backlog PR

Khi nhu cầu review vượt quá năng lực, áp dụng thứ tự ưu tiên:

1. Giữ PR bug/security đang hoạt động (`size: XS/S`) ở đầu hàng đợi.
2. Yêu cầu các PR chồng chéo hợp nhất; đóng các PR cũ hơn là `superseded` sau khi xác nhận.
3. Đánh dấu PR ngủ đông là `stale-candidate` trước khi cửa sổ stale bắt đầu.
4. Yêu cầu rebase + validation mới trước khi mở lại công việc kỹ thuật stale/superseded.

---

## Ghi đè tự động hóa

Dùng khi kết quả tự động hóa tạo ra tác dụng phụ cho review:

1. **Nhãn rủi ro sai:** thêm `risk: manual`, rồi đặt nhãn `risk:*` mong muốn.
2. **Tự đóng sai trên triage issue:** mở lại issue, xóa nhãn route, để lại comment làm rõ.
3. **Spam/nhiễu nhãn:** giữ comment maintainer chuẩn tắc và xóa nhãn route dư thừa.
4. **Phạm vi PR mơ hồ:** yêu cầu chia nhỏ trước khi review sâu.

---

## Giao thức bàn giao

Nếu bàn giao review cho maintainer/agent khác, bao gồm:

1. Tóm tắt phạm vi.
2. Phân loại rủi ro hiện tại và lý do.
3. Những gì đã được validate.
4. Các vấn đề chặn mở.
5. Hành động tiếp theo được đề xuất.

---

## Vệ sinh hàng đợi hàng tuần

- Review hàng đợi stale và chỉ áp dụng `no-stale` cho công việc đã được chấp nhận nhưng bị chặn.
- Ưu tiên PR bug/security `size: XS/S` trước.
- Chuyển đổi các issue hỗ trợ tái diễn thành cập nhật tài liệu và hướng dẫn auto-response.

---

## Tài liệu liên quan

- [[001-i18n-vi-getting-started-readme|README]] — phân loại và điều hướng tài liệu.
- [[055-vi-pr-workflow|pr-workflow]] — workflow quản trị và hợp đồng merge.
- [[106-vi-ci-map|ci-map]] — bản đồ quyền sở hữu và triage CI.
- [[101-i18n-vi-actions-source-policy|actions-source-policy]] — chính sách allowlist nguồn action.

---

## Ghi chú bảo trì

- **Chủ sở hữu:** các maintainer chịu trách nhiệm về chất lượng review và thông lượng hàng đợi.
- **Kích hoạt cập nhật:** thay đổi chính sách PR, thay đổi mô hình phân tuyến rủi ro hoặc thay đổi hành vi ghi đè tự động hóa.
- **Lần review cuối:** 2026-02-18.
