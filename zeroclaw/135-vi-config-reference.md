---
title: Tham khảo cấu hình ZeroClaw
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/config-reference.md
source: git
fetched_at: 2026-05-02T14:52:29.812803769-03:00
rendered_js: false
word_count: 2969
summary: Tài liệu cung cấp tham khảo toàn diện về cấu hình ZeroClaw, chi tiết cài đặt file TOML, ghi đè biến môi trường và tham số cụ thể cho agents, runtime, quan sát và quản lý chi phí.
tags:
    - zeroclaw
    - configuration
    - toml
    - reference
    - environment-variables
    - agents
    - cli-tools
    - vi-docs
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tham khảo cấu hình ZeroClaw

Các mục cấu hình thường dùng và giá trị mặc định.

Xác minh lần cuối: **2026-02-19**

## Thứ tự tìm config khi khởi động

1. Biến `ZEROCLAW_WORKSPACE` (nếu được đặt)
2. Marker `~/.zeroclaw/active_workspace.toml` (nếu có)
3. Mặc định `~/.zeroclaw/config.toml`

ZeroClaw ghi log đường dẫn config đã giải quyết khi khởi động ở mức `INFO`:
- `Config loaded` với các trường: `path`, `workspace`, `source`, `initialized`

Lệnh xuất schema:
- `zeroclaw config schema` (xuất JSON Schema draft 2020-12 ra stdout)

---

## Khóa chính

| Khóa | Mặc định | Ghi chú |
|---|---|---|
| `default_provider` | `openrouter` | ID hoặc bí danh provider |
| `default_model` | `anthropic/claude-sonnet-4-6` | Model định tuyến qua provider đã chọn |
| `default_temperature` | `0.7` | Nhiệt độ model |

---

## `[observability]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `backend` | `none` | Backend quan sát: `none`, `noop`, `log`, `prometheus`, `otel`, `opentelemetry`, `otlp` |
| `otel_endpoint` | `http://localhost:4318` | Endpoint OTLP HTTP khi backend là `otel` |
| `otel_service_name` | `zeroclaw` | Tên dịch vụ gửi đến OTLP collector |

> [!note]
> - `backend = "otel"` dùng OTLP HTTP export với blocking exporter client
> - Bí danh `opentelemetry` và `otlp` trỏ đến cùng backend OTel

Ví dụ:

```toml
[observability]
backend = "otel"
otel_endpoint = "http://localhost:4318"
otel_service_name = "zeroclaw"
```

---

## Ghi đè provider qua biến môi trường

Thứ tự ưu tiên:

1. `ZEROCLAW_PROVIDER` (ghi đè tường minh, luôn thắng)
2. `PROVIDER` (dự phòng kiểu cũ)
3. `default_provider` trong `config.toml`

> [!note] Người dùng container
> Nếu `config.toml` đặt provider tùy chỉnh, biến `PROVIDER=openrouter` mặc định từ container không thay thế được nó. Dùng `ZEROCLAW_PROVIDER` khi muốn ghi đè.

---

## `[agent]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `compact_context` | `false` | Khi bật: bootstrap_max_chars=6000, rag_chunk_limit=2 (dùng cho model 13B trở xuống) |
| `max_tool_iterations` | `10` | Số vòng lặp tool-call tối đa mỗi tin nhắn trên CLI, gateway và channels |
| `max_history_messages` | `50` | Số tin nhắn lịch sử tối đa giữ lại mỗi phiên |
| `parallel_tools` | `false` | Bật thực thi tool song song trong một lượt |
| `tool_dispatcher` | `auto` | Chiến lược dispatch tool |

> [!note]
> - Đặt `max_tool_iterations = 0` sẽ dùng giá trị mặc định an toàn `10`
> - Nếu tin nhắn kênh vượt giá trị này, runtime trả về: `Agent exceeded maximum tool iterations (<value>)`
> - `parallel_tools` áp dụng cho API `Agent::turn()`, không ảnh hưởng vòng lặp runtime

---

## `[agents.<name>]`

Cấu hình agent phụ (sub-agent). Mỗi khóa dưới `[agents]` định nghĩa một agent phụ.

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `provider` | _bắt buộc_ | Tên provider (ví dụ `"ollama"`, `"openrouter"`, `"anthropic"`) |
| `model` | _bắt buộc_ | Tên model cho agent phụ |
| `system_prompt` | chưa đặt | System prompt tùy chỉnh (tùy chọn) |
| `api_key` | chưa đặt | API key tùy chỉnh (mã hóa khi `secrets.encrypt = true`) |
| `temperature` | chưa đặt | Temperature tùy chỉnh |
| `max_depth` | `3` | Độ sâu đệ quy tối đa cho ủy quyền lồng nhau |
| `agentic` | `false` | Bật chế độ vòng lặp tool-call nhiều lượt |
| `allowed_tools` | `[]` | Danh sách tool được phép ở chế độ agentic |
| `max_iterations` | `10` | Số vòng tool-call tối đa cho chế độ agentic |

> [!note]
> - `agentic = false`: hành vi ủy quyền prompt→response đơn lượt
> - `agentic = true`: yêu cầu ít nhất một mục khớp trong `allowed_tools`
> - Tool `delegate` bị loại khỏi allowlist để tránh vòng lặp ủy quyền

Ví dụ:

```toml
[agents.researcher]
provider = "openrouter"
model = "anthropic/claude-sonnet-4-6"
system_prompt = "You are a research assistant."
max_depth = 2
agentic = true
allowed_tools = ["web_search", "http_request", "file_read"]
max_iterations = 8

[agents.coder]
provider = "ollama"
model = "qwen2.5-coder:32b"
temperature = 0.2
```

---

## `[runtime]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `reasoning_enabled` | chưa đặt (`None`) | Ghi đè toàn cục cho reasoning/thinking trên provider hỗ trợ |

> [!note]
> - `reasoning_enabled = false`: tắt tường minh reasoning phía provider
> - `reasoning_enabled = true`: yêu cầu reasoning tường minh
> - Để trống giữ mặc định của provider

---

## `[skills]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `open_skills_enabled` | `false` | Cho phép tải/đồng bộ kho `open-skills` cộng đồng |
| `open_skills_dir` | chưa đặt | Đường dẫn cục bộ cho `open-skills` (mặc định `$HOME/open-skills` khi bật) |

> [!note] Ghi đè biến môi trường
> - `ZEROCLAW_OPEN_SKILLS_ENABLED`: chấp nhận `1/0`, `true/false`, `yes/no`, `on/off`
> - `ZEROCLAW_OPEN_SKILLS_DIR`: ghi đè đường dẫn kho
> - Thứ tự ưu tiên: biến môi trường → config.toml → mặc định `false`

---

## `[composio]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `enabled` | `false` | Bật công cụ OAuth do Composio quản lý |
| `api_key` | chưa đặt | API key Composio cho tool `composio` |
| `entity_id` | `default` | `user_id` mặc định gửi khi gọi connect/execute |

> [!note]
> - Tương thích ngược: `enable = true` kiểu cũ tương đương `enabled = true`
> - Nếu `enabled = false` hoặc thiếu `api_key`, tool `composio` không được đăng ký
> - ZeroClaw yêu cầu Composio v3 tools với `toolkit_versions=latest`

Luồng thông thường:
1. Gọi `connect`
2. Hoàn tất OAuth trên trình duyệt
3. Chạy `execute` cho hành động mong muốn

Nếu lỗi thiếu connected-account, gọi `list_accounts` (tùy chọn với `app`) và truyền `connected_account_id` trả về cho `execute`.

---

## `[cost]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `enabled` | `false` | Bật theo dõi chi phí |
| `daily_limit_usd` | `10.00` | Giới hạn chi tiêu hàng ngày (USD) |
| `monthly_limit_usd` | `100.00` | Giới hạn chi tiêu hàng tháng (USD) |
| `warn_at_percent` | `80` | Cảnh báo khi chi tiêu đạt tỷ lệ phần trăm này |
| `allow_override` | `false` | Cho phép vượt ngân sách khi dùng cờ `--override` |

> [!note]
> - Runtime theo dõi ước tính chi phí mỗi yêu cầu
> - Tại ngưỡng `warn_at_percent`, cảnh báo được gửi nhưng yêu cầu vẫn tiếp tục
> - Khi đạt giới hạn, yêu cầu bị từ chối trừ khi `allow_override = true` và cờ `--override` được truyền

---

## `[identity]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `format` | `openclaw` | Định dạng danh tính: `"openclaw"` hoặc `"aieos"` |
| `aieos_path` | chưa đặt | Đường dẫn file AIEOS JSON (tương đối với workspace) |
| `aieos_inline` | chưa đặt | AIEOS JSON nội tuyến (thay thế cho đường dẫn file) |

> [!note]
> - Dùng `format = "aieos"` với `aieos_path` hoặc `aieos_inline`
> - Chỉ nên đặt một trong hai; `aieos_path` được ưu tiên

---

## `[multimodal]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `max_images` | `4` | Số marker ảnh tối đa mỗi yêu cầu |
| `max_image_size_mb` | `5` | Giới hạn kích thước ảnh trước khi mã hóa base64 |
| `allow_remote_fetch` | `false` | Cho phép tải ảnh từ URL `http(s)` trong marker |

> [!note] Vận hành
> - Runtime chấp nhận marker ảnh: ``[IMAGE:<source>]``
> - Nguồn: đường dẫn file cục bộ, Data URI, URL từ xa (khi `allow_remote_fetch = true`)
> - Kiểu MIME: `image/png`, `image/jpeg`, `image/webp`, `image/gif`, `image/bmp`
> - Nếu provider không hỗ trợ vision, yêu cầu thất bại với lỗi capability (`capability=vision`)

---

## `[browser]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `enabled` | `false` | Bật tool `browser_open` (mở URL trong trình duyệt mặc định) |
| `allowed_domains` | `[]` | Tên miền cho phép cho `browser_open` |
| `session_name` | chưa đặt | Tên phiên trình duyệt |
| `backend` | `agent_browser` | Backend tự động hóa: `"agent_browser"`, `"rust_native"`, `"computer_use"`, `"auto"` |
| `native_headless` | `true` | Chế độ headless cho backend rust-native |
| `native_webdriver_url` | `http://127.0.0.1:9515` | URL endpoint WebDriver cho backend rust-native |
| `native_chrome_path` | chưa đặt | Đường dẫn Chrome/Chromium tùy chọn |

### `[browser.computer_use]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `endpoint` | `http://127.0.0.1:8787/v1/actions` | Endpoint sidecar cho hành động computer-use |
| `api_key` | chưa đặt | Bearer token tùy chọn (mã hóa khi lưu) |
| `timeout_ms` | `15000` | Thời gian chờ mỗi hành động (mili giây) |
| `allow_remote_endpoint` | `false` | Cho phép endpoint từ xa/công khai |
| `window_allowlist` | `[]` | Danh sách cho phép tiêu đề cửa sổ/tiến trình gửi đến sidecar |
| `max_coordinate_x` | chưa đặt | Giới hạn trục X cho hành động dựa trên tọa độ |
| `max_coordinate_y` | chưa đặt | Giới hạn trục Y cho hành động dựa trên tọa độ |

> [!note]
> - Khi `backend = "computer_use"`, agent ủy quyền hành động trình duyệt cho sidecar
> - `allow_remote_endpoint = false` từ chối mọi endpoint không phải loopback
> - Dùng `window_allowlist` để giới hạn cửa sổ OS có thể tương tác

---

## `[http_request]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `enabled` | `false` | Bật tool `http_request` cho tương tác API |
| `allowed_domains` | `[]` | Tên miền cho phép (khớp chính xác hoặc subdomain) |
| `max_response_size` | `1000000` | Kích thước response tối đa (byte, mặc định: 1 MB) |
| `timeout_secs` | `30` | Thời gian chờ yêu cầu (giây) |

> [!note]
> - Mặc định từ chối tất cả: nếu `allowed_domains` rỗng, mọi yêu cầu HTTP bị từ chối
> - Dùng khớp tên miền chính xác hoặc subdomain

---

## `[gateway]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `host` | `127.0.0.1` | Địa chỉ bind |
| `port` | `3000` | Cổng lắng nghe gateway |
| `require_pairing` | `true` | Yêu cầu ghép nối trước khi xác thực bearer |
| `allow_public_bind` | `false` | Chặn lộ public do vô ý |

---

## `[autonomy]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `level` | `supervised` | `read_only`, `supervised` hoặc `full` |
| `workspace_only` | `true` | Giới hạn ghi/lệnh trong phạm vi workspace |
| `allowed_commands` | _bắt buộc_ | Danh sách lệnh được phép |
| `forbidden_paths` | `[]` | Danh sách đường dẫn bị cấm |
| `max_actions_per_hour` | `100` | Ngân sách hành động mỗi giờ |
| `max_cost_per_day_cents` | `1000` | Giới hạn chi tiêu mỗi ngày (cent) |
| `require_approval_for_medium_risk` | `true` | Yêu cầu phê duyệt cho lệnh rủi ro trung bình |
| `block_high_risk_commands` | `true`` | Chặn cứng lệnh rủi ro cao |
| `auto_approve` | `[]` | Thao tác tool luôn được tự động phê duyệt |
| `always_ask` | `[]` | Thao tác tool luôn yêu cầu phê duyệt |

> [!note]
> - `level = "full"` bỏ qua phê duyệt rủi ro trung bình cho shell execution
> - Phân tích toán tử/dấu phân cách shell nhận biết dấu ngoặc kép
> - Toán tử chuỗi shell không trích dẫn vẫn được kiểm tra bởi policy

---

## `[memory]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `backend` | `sqlite` | `sqlite`, `lucid`, `markdown`, `none` |
| `auto_save` | `true` | Chỉ lưu đầu vào người dùng (đầu ra assistant bị loại) |
| `embedding_provider` | `none` | `none`, `openai` hoặc endpoint tùy chỉnh |
| `embedding_model` | `text-embedding-3-small` | ID model embedding |
| `embedding_dimensions` | `1536` | Kích thước vector mong đợi |
| `vector_weight` | `0.7` | Trọng số vector trong xếp hạng kết hợp |
| `keyword_weight` | `0.3` | Trọng số từ khóa trong xếp hạng kết hợp |

> [!note]
> Chèn ngữ cảnh memory bỏ qua khóa auto-save `assistant_resp*` kiểu cũ

---

## `[[model_routes]]` và `[[embedding_routes]]`

Route hint giúp tên tích hợp ổn định khi model ID thay đổi.

### `[[model_routes]]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `hint` | _bắt buộc_ | Tên hint tác vụ (ví dụ `"reasoning"`, `"fast"`, `"code"`, `"summarize"`) |
| `provider` | _bắt buộc_ | Provider đích |
| `model` | _bắt buộc_ | Model sử dụng với provider đó |
| `api_key` | chưa đặt | API key tùy chỉnh cho provider của route này |

### `[[embedding_routes]]`

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `hint` | _bắt buộc_ | Tên route hint (ví dụ `"semantic"`, `"archive"`, `"faq"`) |
| `provider` | _bắt buộc_ | Embedding provider (`"none"`, `"openai"` hoặc `"custom:<url>"`) |
| `model` | _bắt buộc_ | Model embedding sử dụng với provider đó |
| `dimensions` | chưa đặt | Ghi đè kích thước embedding cho route này |
| `api_key` | chưa đặt | API key tùy chỉnh cho provider của route này |

Ví dụ:

```toml
[memory]
embedding_model = "hint:semantic"

[[model_routes]]
hint = "reasoning"
provider = "openrouter"
model = "provider/model-id"

[[embedding_routes]]
hint = "semantic"
provider = "openai"
model = "text-embedding-3-small"
dimensions = 1536
```

> [!tip] Chiến lược nâng cấp
> 1. Giữ hint ổn định (`hint:reasoning`, `hint:semantic`)
> 2. Chỉ cập nhật `model = "...phiên-bản-mới..."` trong mục route
> 3. Kiểm tra bằng `zeroclaw doctor` trước khi khởi động lại

---

## `[query_classification]`

Tự động định tuyến tin nhắn đến hint `[[model_routes]]` theo mẫu nội dung.

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `enabled` | `false` | Bật phân loại truy vấn tự động |
| `rules` | `[]` | Quy tắc phân loại (đánh giá theo thứ tự ưu tiên) |

Mỗi rule trong `rules`:

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `hint` | _bắt buộc_ | Phải khớp giá trị hint trong `[[model_routes]]` |
| `keywords` | `[]` | Khớp chuỗi con không phân biệt hoa thường |
| `patterns` | `[]` | Khớp chuỗi chính xác phân biệt hoa thường |
| `min_length` | chưa đặt | Chỉ khớp nếu độ dài tin nhắn ≥ N ký tự |
| `max_length` | chưa đặt | Chỉ khớp nếu độ dài tin nhắn ≤ N ký tự |
| `priority` | `0` | Rule ưu tiên cao hơn được kiểm tra trước |

Ví dụ:

```toml
[query_classification]
enabled = true

[[query_classification.rules]]
hint = "reasoning"
keywords = ["explain", "analyze", "why"]
min_length = 200
priority = 10

[[query_classification.rules]]
hint = "fast"
keywords = ["hi", "hello", "thanks"]
max_length = 50
priority = 5
```

---

## `[channels_config]`

Cấu hình kênh cấp cao nằm dưới `channels_config`.

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `message_timeout_secs` | `300` | Thời gian chờ cơ bản (giây) cho xử lý tin nhắn kênh |

> [!note]
> - Mặc định `300s` tối ưu cho LLM chạy cục bộ (Ollama)
> - Ngân sách timeout runtime là `message_timeout_secs * scale` (scale = min(max_tool_iterations, 4))
> - Nếu dùng cloud API, có thể giảm xuống `60` hoặc thấp hơn
> - Giá trị dưới `30` bị giới hạn thành `30`
> - Khi timeout xảy ra, người dùng nhận: `⚠️ Request timed out while waiting for the model. Please try again.`
> - Channel runtime theo dõi `config.toml` và áp dụng thay đổi nóng

Xem chi tiết tại [[channels-reference|Tài liệu tham khảo Channels]]

### `[channels_config.whatsapp]`

WhatsApp hỗ trợ hai backend:

**Chế độ Cloud API:**

| Khóa | Bắt buộc | Mục đích |
|---|---|---|
| `access_token` | Có | Bearer token Meta Cloud API |
| `phone_number_id` | Có | ID số điện thoại Meta |
| `verify_token` | Có | Token xác minh webhook |
| `app_secret` | Tùy chọn | Bật xác minh chữ ký webhook |
| `allowed_numbers` | Khuyến nghị | Số điện thoại cho phép gửi đến |

**Chế độ WhatsApp Web:**

| Khóa | Bắt buộc | Mục đích |
|---|---|---|
| `session_path` | Có | Đường dẫn phiên SQLite lưu trữ lâu dài |
| `pair_phone` | Tùy chọn | Số điện thoại cho luồng pair-code |
| `pair_code` | Tùy chọn | Mã pair tùy chỉnh |
| `allowed_numbers` | Khuyến nghị | Số điện thoại cho phép gửi đến |

> [!note]
> - WhatsApp Web yêu cầu build flag `whatsapp-web`
> - Nếu cả Cloud lẫn Web đều có cấu hình, Cloud được ưu tiên

---

## `[hardware]`

Cấu hình truy cập phần cứng vật lý.

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `enabled` | `false` | Bật truy cập phần cứng |
| `transport` | `none` | Chế độ truyền: `"none"`, `"native"`, `"serial"` hoặc `"probe"` |
| `serial_port` | chưa đặt | Đường dẫn cổng serial (ví dụ `"/dev/ttyACM0"`) |
| `baud_rate` | `115200` | Tốc độ baud serial |
| `probe_target` | chưa đặt | Chip đích cho probe (ví dụ `"STM32F401RE"`) |
| `workspace_datasheets` | `false` | Bật RAG datasheet workspace |

> [!note]
> - Dùng `transport = "serial"` với `serial_port` cho kết nối USB-serial
> - Dùng `transport = "probe"` với `probe_target` cho nạp qua debug-probe

---

## `[peripherals]`

Bo mạch ngoại vi trở thành tool agent khi được bật.

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `enabled` | `false` | Bật hỗ trợ ngoại vi |
| `boards` | `[]` | Danh sách cấu hình bo mạch |
| `datasheet_dir` | chưa đặt | Đường dẫn tài liệu datasheet (tương đối workspace) cho RAG |

Mỗi mục trong `boards`:

| Khóa | Mặc định | Mục đích |
|---|---|---|
| `board` | _bắt buộc_ | Loại bo mạch: `"nucleo-f401re"`, `"rpi-gpio"`, `"esp32"`, v.v. |
| `transport` | `serial` | Kiểu truyền: `"serial"`, `"native"`, `"websocket"` |
| `path` | chưa đặt | Đường dẫn serial: `"/dev/ttyACM0"`, `"/dev/ttyUSB0"` |
| `baud` | `115200` | Tốc độ baud cho serial |

Ví dụ:

```toml
[peripherals]
enabled = true
datasheet_dir = "docs/datasheets"

[[peripherals.boards]]
board = "nucleo-f401re"
transport = "serial"
path = "/dev/ttyACM0"
baud = 115200

[[peripherals.boards]]
board = "rpi-gpio"
transport = "native"
```

> [!note]
> - Đặt file `.md`/`.txt` datasheet đặt tên theo bo mạch trong `datasheet_dir`
> - Xem [[hardware-peripherals-design|hardware-peripherals-design]] để biết chi tiết giao thức

---

## Giá trị mặc định liên quan bảo mật

- Allowlist kênh mặc định từ chối tất cả (`[]` nghĩa là từ chối tất cả)
- Gateway mặc định yêu cầu ghép nối
- Mặc định chặn public bind

---

## Lệnh kiểm tra

Sau khi chỉnh config:

```bash
zeroclaw status
zeroclaw doctor
zeroclaw channel doctor
zeroclaw service restart
```

---

## Tài liệu liên quan

- [[channels-reference|Tài liệu tham khảo Channels]]
- [[providers-reference|providers-reference]]
- [[operations-runbook|operations-runbook]]
- [[troubleshooting|troubleshooting]]
