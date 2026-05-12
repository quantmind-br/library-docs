---
title: Tài liệu tham khảo Channels
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/channels-reference.md
source: git
fetched_at: 2026-05-02T14:52:26.611484076-03:00
rendered_js: false
word_count: 1449
summary: Tài liệu này cung cấp hướng dẫn chi tiết về cấu hình, quản lý runtime và thiết lập các channel truyền tin cho nền tảng ZeroClaw.
tags:
    - zeroclaw
    - configuration
    - messaging-channels
    - bot-setup
    - matrix
    - telegram
    - discord
    - api-integration
    - vi-docs
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tài liệu tham khảo Channels

> [!info] Hướng dẫn chuyên biệt
> Với các phòng Matrix được mã hóa, xem [[matrix-e2ee-guide|Hướng dẫn Matrix E2EE]]

## Truy cập nhanh

- Cần config đầy đủ theo channel: xem [[#4-cấu-hình-theo-từng-channel]]
- Cần chẩn đoán khi không nhận phản hồi: xem [[#6-danh-sách-kiểm-tra-xử-lý-sự-cố]]
- Cần hỗ trợ phòng Matrix mã hóa: dùng [[matrix-e2ee-guide|Hướng dẫn Matrix E2EE]]
- Cần triển khai/mạng (polling vs webhook): xem [[network-deployment|Network Deployment]]

## FAQ: Cấu hình Matrix thành công nhưng không có phản hồi

Triệu chứng phổ biến nhất (tương tự issue #499). Kiểm tra theo thứ tự:

1. **Allowlist không khớp**: `allowed_users` không bao gồm người gửi (hoặc để trống)
2. **Room đích sai**: bot chưa tham gia room được cấu hình `room_id` / alias
3. **Token/tài khoản không khớp**: token hợp lệ nhưng thuộc tài khoản Matrix khác
4. **Thiếu E2EE device identity**: `whoami` không trả về `device_id` và config không cung cấp giá trị này
5. **Thiếu key sharing/trust**: các khóa room chưa được chia sẻ cho thiết bị bot
6. **Trạng thái runtime cũ**: config thay đổi nhưng `zeroclaw daemon` chưa khởi động lại

---

## 1. Namespace cấu hình

Tất cả cài đặt channel nằm trong `channels_config` trong `~/.zeroclaw/config.toml`.

```toml
[channels_config]
cli = true
```

Mỗi channel được bật bằng cách tạo sub-table tương ứng (ví dụ: `[channels_config.telegram]`).

---

## 2. Chuyển đổi model runtime trong chat

Khi chạy `zeroclaw channel start` (hoặc chế độ daemon), Telegram và Discord hỗ trợ chuyển đổi runtime theo phạm vi người gửi:

- `/models` — hiển thị providers hiện có và lựa chọn hiện tại
- `/models <provider>` — chuyển provider cho phiên người gửi hiện tại
- `/model` — hiển thị model hiện tại và các model ID đã cache
- `/model <model-id>` — chuyển model cho phiên người gửi hiện tại

> [!note]
> - Chỉ xóa lịch sử hội thoại trong bộ nhớ của người gửi đó
> - Xem trước bộ nhớ cache model từ `zeroclaw models refresh --provider <ID>`
> - Đây là lệnh chat runtime, không phải lệnh con CLI

---

## 3. Giao thức marker hình ảnh đầu vào

ZeroClaw hỗ trợ đầu vào multimodal qua marker nội tuyến:

- Cú pháp: ``[IMAGE:<source>]``
- `<source>` có thể là:
  - Đường dẫn file cục bộ
  - Data URI (`data:image/...;base64,...`)
  - URL từ xa (khi `multimodal.allow_remote_fetch = true`)

> [!note] Vận hành
> - Marker được phân tích trước khi gọi provider
> - Nếu provider không hỗ trợ vision, request thất bại với lỗi capability (`capability=vision`)
> - Media type `image/*` từ Linq webhook được chuyển đổi sang định dạng marker

---

## 4. Chế độ phân phối tóm tắt

| Channel | Chế độ nhận | Cần cổng inbound công khai? |
|---|---|---|
| CLI | local stdin/stdout | Không |
| Telegram | polling | Không |
| Discord | gateway/websocket | Không |
| Slack | events API | Không (token-based) |
| Mattermost | polling | Không |
| Matrix | sync API (hỗ trợ E2EE) | Không |
| Signal | signal-cli HTTP bridge | Không (endpoint bridge cục bộ) |
| WhatsApp | webhook (Cloud API) hoặc websocket (Web mode) | Cloud API: Có (HTTPS callback), Web mode: Không |
| Webhook | gateway endpoint (`/webhook`) | Thường là có |
| Email | IMAP polling + SMTP send | Không |
| IRC | IRC socket | Không |
| Lark/Feishu | websocket (mặc định) hoặc webhook | Chỉ ở chế độ Webhook |
| DingTalk | stream mode | Không |
| QQ | bot gateway | Không |
| iMessage | tích hợp cục bộ | Không |

---

## 5. Ngữ nghĩa allowlist

Với các channel có allowlist người gửi:

- Allowlist trống: từ chối tất cả tin nhắn đầu vào
- `"*"`: cho phép tất cả người gửi (chỉ tạm thời)
- Danh sách tường minh: chỉ cho phép những người gửi được liệt kê

Tên trường theo channel:

- `allowed_users` (Telegram/Discord/Slack/Mattermost/Matrix/IRC/Lark/DingTalk/QQ)
- `allowed_from` (Signal)
- `allowed_numbers` (WhatsApp)
- `allowed_senders` (Email)
- `allowed_contacts` (iMessage)

---

## 6. Cấu hình theo từng channel

### 6.1 Telegram

```toml
[channels_config.telegram]
bot_token = "123456:telegram-token"
allowed_users = ["*"]
stream_mode = "off"               # Tùy chọn: off | partial
mention_only = false              # Tùy chọn: yêu cầu @mention trong nhóm
interrupt_on_new_message = false  # Tùy chọn: hủy yêu cầu đang xử lý cùng người gửi
```

> [!note] Lưu ý
> - `interrupt_on_new_message = true` giữ lại lượt người dùng bị gián đoạn
> - Phạm vi gián đoạn: cùng người gửi trong cùng chat

### 6.2 Discord

```toml
[channels_config.discord]
bot_token = "discord-bot-token"
allowed_users = ["*"]
```

### 6.3 Slack

```toml
[channels_config.slack]
bot_token = "xoxb-..."
app_token = "xapp-..."             # Tùy chọn
channel_id = "C1234567890"         # Tùy chọn
allowed_users = ["*"]
```

### 6.4 Mattermost

```toml
[channels_config.mattermost]
url = "https://mm.example.com"
bot_token = "mattermost-token"
channel_id = "channel-id"          # Bắt buộc để lắng nghe
allowed_users = ["*"]
```

### 6.5 Matrix

```toml
[channels_config.matrix]
homeserver = "https://matrix.example.com"
access_token = "syt_..."
user_id = "@zeroclaw:matrix.example.com"   # Tùy chọn, khuyến nghị cho E2EE
room_id = "!room:matrix.example.com"       # hoặc room alias
allowed_users = ["*"]
```

> [!tip] Xử lý sự cố
> Xem [[matrix-e2ee-guide|Hướng dẫn Matrix E2EE]]

### 6.6 Signal

```toml
[channels_config.signal]
http_url = "http://127.0.0.1:8686"
account = "+1234567890"
allowed_from = ["*"]
```

### 6.7 WhatsApp

ZeroClaw hỗ trợ hai backend:

**Chế độ Cloud API:**

```toml
[channels_config.whatsapp]
access_token = "EAAB..."
phone_number_id = "123456789012345"
verify_token = "your-verify-token"
allowed_numbers = ["*"]
```

**Chế độ WhatsApp Web:**

```toml
[channels_config.whatsapp]
session_path = "~/.zeroclaw/state/whatsapp-web/session.db"
allowed_numbers = ["*"]
```

> [!note]
> - WhatsApp Web yêu cầu build flag `whatsapp-web`
> - Nếu cả Cloud lẫn Web đều cấu hình, Cloud được ưu tiên

### 6.8 Webhook Channel

```toml
[channels_config.webhook]
port = 8080
secret = "optional-shared-secret"
```

### 6.9 Email

```toml
[channels_config.email]
imap_host = "imap.example.com"
imap_port = 993
smtp_host = "smtp.example.com"
username = "bot@example.com"
password = "email-password"
from_address = "bot@example.com"
poll_interval_secs = 60
allowed_senders = ["*"]
```

### 6.10 IRC

```toml
[channels_config.irc]
server = "irc.libera.chat"
port = 6697
nickname = "zeroclaw-bot"
channels = ["#zeroclaw"]
allowed_users = ["*"]
```

### 6.11 Lark / Feishu

```toml
[channels_config.lark]
app_id = "cli_xxx"
app_secret = "xxx"
allowed_users = ["*"]
receive_mode = "websocket"          # hoặc "webhook"
port = 8081                          # bắt buộc ở chế độ webhook
```

> [!note] Onboarding tương tác
> ```bash
> zeroclaw onboard --interactive
> ```

### 6.12 DingTalk

```toml
[channels_config.dingtalk]
client_id = "ding-app-key"
client_secret = "ding-app-secret"
allowed_users = ["*"]
```

### 6.13 QQ

```toml
[channels_config.qq]
app_id = "qq-app-id"
app_secret = "qq-app-secret"
allowed_users = ["*"]
```

### 6.14 iMessage

```toml
[channels_config.imessage]
allowed_contacts = ["*"]
```

---

## 7. Quy trình xác thực

1. Cấu hình channel với allowlist rộng (`"*"`) để xác minh ban đầu
2. Chạy:
   ```bash
   zeroclaw onboard --channels-only
   zeroclaw daemon
   ```
3. Gửi tin nhắn từ người gửi dự kiến
4. Xác nhận nhận được phản hồi
5. Siết chặt allowlist từ `"*"` thành các ID cụ thể

---

## 8. Danh sách kiểm tra xử lý sự cố

Nếu channel kết nối nhưng không phản hồi:

1. Xác nhận danh tính người gửi được allowlist cho phép
2. Xác nhận tài khoản bot đã là thành viên/có quyền trong room/channel
3. Xác nhận token/secret hợp lệ (không hết hạn/bị thu hồi)
4. Xác nhận chế độ truyền tải:
   - Polling/websocket: không cần HTTP inbound công khai
   - Webhook: cần HTTPS callback có thể truy cập
5. Khởi động lại `zeroclaw daemon` sau thay đổi config

Đặc biệt với phòng Matrix mã hóa, xem [[matrix-e2ee-guide|Hướng dẫn Matrix E2EE]]

---

## 9. Phụ lục vận hành: Bảng từ khóa log

Dùng để phân loại sự cố nhanh. Khớp từ khóa log trước, sau đó thực hiện bước xử lý sự cố.

### 9.1 Lệnh capture khuyến nghị

```bash
RUST_LOG=info zeroclaw daemon 2>&1 | tee /tmp/zeroclaw.log
```

Sau đó lọc:

```bash
rg -n "Matrix|Telegram|Discord|Slack|Mattermost|Signal|WhatsApp|Email|IRC|Lark|DingTalk|QQ|iMessage|Webhook|Channel" /tmp/zeroclaw.log
```

### 9.2 Bảng từ khóa

| Thành phần | Tín hiệu khởi động / hoạt động bình thường | Tín hiệu ủy quyền / chính sách | Tín hiệu truyền tải / lỗi |
|---|---|---|---|
| Telegram | `Telegram channel listening for messages...` | `Telegram: ignoring message from unauthorized user:` | `Telegram poll error:` / `Telegram parse error:` |
| Discord | `Discord: connected and identified` | `Discord: ignoring message from unauthorized user:` | `Discord: received Reconnect (op 7)` / `Discord: received Invalid Session (op 9)` |
| Slack | `Slack channel listening on #` | `Slack: ignoring message from unauthorized user:` | `Slack poll error:` / `Slack parse error:` |
| Mattermost | `Mattermost channel listening on` | `Mattermost: ignoring message from unauthorized user:` | `Mattermost poll error:` / `Mattermost parse error:` |
| Matrix | `Matrix channel listening on room` / `Matrix room ... is encrypted; E2EE decryption is enabled` | `Matrix whoami failed; falling back to configured session hints` | `Matrix sync error: ... retrying...` |
| Signal | `Signal channel listening via SSE on` | (kiểm tra allowlist bởi `allowed_from`) | `Signal SSE returned ...` / `Signal SSE connect error:` |
| WhatsApp | `WhatsApp channel active (webhook mode)` / `WhatsApp Web connected successfully` | `WhatsApp: ignoring message from unauthorized number:` | `WhatsApp send failed:` / `WhatsApp Web stream error:` |
| Webhook | `WhatsApp webhook verified successfully` | `Webhook: rejected — not paired / invalid bearer token` | `Webhook JSON parse error:` |
| Email | `Email polling every ...` / `Email sent to ...` | `Blocked email from ...` | `Email poll failed:` / `Email poll task panicked:` |
| IRC | `IRC channel connecting to ...` | (kiểm tra allowlist bởi `allowed_users`) | `IRC SASL authentication failed` / `IRC nickname ... is in use` |
| Lark/Feishu | `Lark: WS connected` / `Lark event callback server listening on` | `Lark WS: ignoring ... (not in allowed_users)` | `Lark: ping failed, reconnecting` / `Lark: heartbeat timeout` |
| DingTalk | `DingTalk: connected and listening for messages...` | `DingTalk: ignoring message from unauthorized user:` | `DingTalk WebSocket error:` |
| QQ | `QQ: connected and identified` | `QQ: ignoring C2C message from unauthorized user:` | `QQ: received Reconnect (op 7)` / `QQ: message channel closed` |
| iMessage | `iMessage channel listening (AppleScript bridge)...` | (allowlist bởi `allowed_contacts`) | `iMessage poll error:` |

### 9.3 Từ khóa runtime supervisor

Nếu channel task bị crash:

- `Channel <name> exited unexpectedly; restarting`
- `Channel <name> error: ...; restarting`
- `Channel message worker crashed:`

Kiểm tra log trước đó để tìm nguyên nhân gốc rễ.
