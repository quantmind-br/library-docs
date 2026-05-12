---
title: Config reference
title_vi: Tham chiếu cấu hình ZeroClaw
url: https://github.com/openagen/zeroclaw/blob/master/docs/reference/api/config-reference.md
source: git
fetched_at: 2026-05-02T14:51:55.803750537-03:00
rendered_js: false
word_count: 4324
summary: This document provides a comprehensive reference for configuring the ZeroClaw operator, detailing core keys, observability settings, security protocols, agent delegation, and runtime environment overrides.
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - configuration
  - zeroclaw
  - reference
  - observability
  - security
  - agent-orchestration
  - toml
category: configuration
---
# ZeroClaw Config Reference (Operator-Oriented)

> [!info] Tóm tắt
> Tài liệu tham chiếu cấu hình ZeroClaw, bao gồm các khóa chính, cài đặt quan sát, giao thức bảo mật, ủy quyền agent và ghi đè môi trường runtime.

**Đường dẫn config khi khởi động:**
1. `ZEROCLAW_WORKSPACE` (nếu set)
2. `~/.zeroclaw/active_workspace.toml` (nếu tồn tại)
3. `~/.zeroclaw/config.toml` (mặc định)

ZeroClaw ghi log config đã load ở mức `INFO` với các trường: `path`, `workspace`, `source`, `initialized`

**Xuất schema:**
```bash
zeroclaw config schema
```

## Core Keys

| Key | Default | Ghi chú |
|------|---------|---------|
| `default_provider` | `openrouter` | ID provider hoặc alias |
| `default_model` | `anthropic/claude-sonnet-4-6` | Model được định tuyến qua provider đã chọn |
| `default_temperature` | `0.7` | Nhiệt độ model |

## `[observability]`

| Key | Default | Mục đích |
|------|---------|----------|
| `backend` | `none` | Backend quan sát: `none`, `noop`, `log`, `prometheus`, `otel`, `opentelemetry`, `otlp` |
| `otel_endpoint` | `http://localhost:4318` | Endpoint OTLP HTTP khi `backend = "otel"` |
| `otel_service_name` | `zeroclaw` | Tên service gửi tới OTLP collector |
| `runtime_trace_mode` | `none` | Chế độ lưu trace runtime: `none`, `rolling`, `full` |
| `runtime_trace_path` | `state/runtime-trace.jsonl` | Đường dẫn trace JSONL (tương đối với workspace trừ khi là đường dẫn tuyệt đối) |
| `runtime_trace_max_entries` | `200` | Số lượng sự kiện tối đa khi `runtime_trace_mode = "rolling"` |

> [!note]
> - `backend = "otel"` sử dụng OTLP HTTP export với client exporter chặn để spans và metrics có thể phát ra an toàn từ ngữ cảnh non-Tokio
> - `opentelemetry` và `otlp` là alias cho cùng backend OTel
> - Runtime traces dùng để debug lỗi tool-call và payload tool model bị lỗi. Có thể chứa output model, nên tắt mặc định trên hosts chia sẻ
> - Truy vấn runtime traces:
>   - `zeroclaw doctor traces --limit 20`
>   - `zeroclaw doctor traces --event tool_call_result --contains "error"`
>   - `zeroclaw doctor traces --id <trace-id>`

**Ví dụ:**
```toml
[observability]
backend = "otel"
otel_endpoint = "http://localhost:4318"
otel_service_name = "zeroclaw"
runtime_trace_mode = "rolling"
runtime_trace_path = "state/runtime-trace.jsonl"
runtime_trace_max_entries = 200
```

## Ghi đè Provider bằng môi trường

Thứ tự ghi đè provider:
1. `ZEROCLAW_PROVIDER` (ghi đè tường minh, luôn thắng khi non-empty)
2. `PROVIDER` (fallback legacy, chỉ áp dụng khi config provider chưa set hoặc vẫn là `openrouter`)
3. `default_provider` trong `config.toml`

> [!note] Ghi chú cho người dùng container
> Nếu `config.toml` set provider tùy chỉnh như `custom:https://.../v1`, biến môi trường `PROVIDER=openrouter` mặc định từ Docker/container sẽ không ghi đè được nữa. Dùng `ZEROCLAW_PROVIDER` khi muốn ghi đè runtime env lên provider đã cấu hình non-default.

## `[agent]`

| Key | Default | Mục đích |
|------|---------|----------|
| `compact_context` | `false` | Khi true: `bootstrap_max_chars=6000`, `rag_chunk_limit=2`. Dùng cho model 13B hoặc nhỏ hơn |
| `max_tool_iterations` | `10` | Số vòng lặp tool tối đa mỗi tin nhắn người dùng qua CLI, gateway, channels |
| `max_history_messages` | `50` | Số tin nhắn lịch sử tối đa giữ lại mỗi session |
| `parallel_tools` | `false` | Kích hoạt thực thi tool song song trong một vòng lặp |
| `tool_dispatcher` | `auto` | Chiến lược dispatch tool |

> [!note]
> - `max_tool_iterations = 0` fallback về mặc định an toàn là `10`
> - Nếu tin nhắn channel vượt quá giá trị này, runtime trả về: `Agent exceeded maximum tool iterations (<value>)`
> - Trong CLI, gateway, channel, nhiều tool call độc lập được thực thi song song theo mặc định khi tool pending không yêu cầu approval gating; thứ tự kết quả vẫn ổn định
> - `parallel_tools` áp dụng cho bề mặt API `Agent::turn()`. Không gắn kết vòng lặp runtime dùng bởi CLI, gateway, channel handlers

## `[security.otp]`

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt gating OTP cho actions/miền nhạy cảm |
| `method` | `totp` | Phương thức OTP (`totp`, `pairing`, `cli-prompt`) |
| `token_ttl_secs` | `30` | Thời gian window TOTP (giây) |
| `cache_valid_secs` | `300` | Window cache cho code OTP đã validate gần đây |
| `gated_actions` | `["shell","file_write","browser_open","browser","memory_forget"]` | Tool actions được bảo vệ bởi OTP |
| `gated_domains` | `[]` | Mẫu miền yêu cầu OTP (`*.example.com`, `login.example.com`) |
| `gated_domain_categories` | `[]` | Danh mục preset miền (`banking`, `medical`, `government`, `identity_providers`) |

> [!note]
> - Mẫu miền hỗ trợ wildcard `*`
> - Danh mục preset mở rộng thành tập miền đã biên soạn trong quá trình validation
> - Glob miền không hợp lệ hoặc danh mục không xác định fail nhanh khi khởi động
> - Khi `enabled = true` và không có secret OTP, ZeroClaw sinh secret và in URI đăng ký một lần

**Ví dụ:**
```toml
[security.otp]
enabled = true
method = "totp"
token_ttl_secs = 30
cache_valid_secs = 300
gated_actions = ["shell", "browser_open"]
gated_domains = ["*.chase.com", "accounts.google.com"]
gated_domain_categories = ["banking"]
```

## `[security.estop]`

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt state machine khẩn cấp và CLI |
| `state_file` | `~/.zeroclaw/estop-state.json` | Đường dẫn state estop lưu trữ |
| `require_otp_to_resume` | `true` | Yêu cầu validation OTP trước khi resume operations |

> [!note]
> - State estop được lưu trữ nguyên tử và tải lại khi khởi động
> - State estop bị lỗi/không đọc được fallback về chế độ fail-closed `kill_all`
> - Sử dụng CLI: `zeroclaw estop` để kích hoạt, `zeroclaw estop resume` để xóa levels

## `[agents.<name>]`

Cấu hình sub-agent ủy quyền. Mỗi key dưới `[agents]` định nghĩa một sub-agent được ủy quyền bởi agent chính.

| Key | Default | Mục đích |
|------|---------|----------|
| `provider` | _required_ | Tên provider (ví dụ: `"ollama"`, `"openrouter"`, `"anthropic"`) |
| `model` | _required_ | Tên model cho sub-agent |
| `system_prompt` | unset | Ghi đè prompt hệ thống cho sub-agent |
| `api_key` | unset | Ghi đè API key (lưu trữ mã hóa khi `secrets.encrypt = true`) |
| `temperature` | unset | Ghi đè nhiệt độ cho sub-agent |
| `max_depth` | `3` | Độ sâu đệ quy tối đa cho ủy quyền lồng nhau |
| `agentic` | `false` | Kích hoạt chế độ vòng lặp tool-call đa vòng cho sub-agent |
| `allowed_tools` | `[]` | Danh sách allow tool cho chế độ agentic |
| `max_iterations` | `10` | Số vòng lặp tool tối đa cho chế độ agentic |

> [!note]
> - `agentic = false` giữ hành vi ủy quyền single prompt→response hiện tại
> - `agentic = true` yêu cầu ít nhất một entry khớp trong `allowed_tools`
> - Tool `delegate` bị loại trừ khỏi danh sách allow của sub-agent để ngăn vòng lặp ủy quyền tái diễn

**Ví dụ:**
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

## `[runtime]`

| Key | Default | Mục đích |
|------|---------|----------|
| `reasoning_enabled` | unset (`None`) | Ghi đè reasoning/thinking toàn cục cho providers hỗ trợ điều khiển rõ ràng |

> [!note]
> - `reasoning_enabled = false` tắt hẳn reasoning phía provider (hiện tại chỉ `ollama`, qua trường request `think: false`)
> - `reasoning_enabled = true` yêu cầu reasoning cho providers hỗ trợ (`think: true` trên `ollama`)
> - Unset giữ mặc định provider

## `[skills]`

| Key | Default | Mục đích |
|------|---------|----------|
| `open_skills_enabled` | `false` | Tải/sync repository `open-skills` cộng đồng (opt-in) |
| `open_skills_dir` | unset | Đường dẫn local tùy chọn cho `open-skills` (mặc định `$HOME/open-skills` khi enabled) |
| `prompt_injection_mode` | `full` | Độ chi tiết prompt skill: `full` (hướng dẫn/tools inline) hoặc `compact` (chỉ tên/mô tả/vị trí) |

> [!note]
> - Mặc định bảo mật: ZeroClaw KHÔNG clone hoặc sync `open-skills` trừ khi `open_skills_enabled = true`
> - Ghi đè môi trường:
>   - `ZEROCLAW_OPEN_SKILLS_ENABLED` chấp nhận `1/0`, `true/false`, `yes/no`, `on/off`
>   - `ZEROCLAW_OPEN_SKILLS_DIR` ghi đè đường dẫn repository khi non-empty
>   - `ZEROCLAW_SKILLS_PROMPT_MODE` chấp nhận `full` hoặc `compact`
> - Thứ tự ưu tiên cho flag enable: `ZEROCLAW_OPEN_SKILLS_ENABLED` → `skills.open_skills_enabled` trong `config.toml` → mặc định `false`
> - `prompt_injection_mode = "compact"` được khuyến nghị cho model local low-context để giảm kích thước prompt khởi động trong khi vẫn giữ sẵn file skill theo nhu cầu
> - Tải skill và `zeroclaw skills install` đều áp dụng kiểm toán bảo mật tĩnh. Skills chứa symlink, file script, payload shell nguy hiểm, hoặc unsafe markdown link traversal bị từ chối

## `[composio]`

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt Composio quản lý tools OAuth |
| `api_key` | unset | API key Composio dùng bởi tool `composio` |
| `entity_id` | `default` | `user_id` mặc định gửi trong calls connect/execute |

> [!note]
> - Tương thích ngược: `enable = true` cũ được chấp nhận như alias cho `enabled = true`
> - Nếu `enabled = false` hoặc `api_key` missing, tool `composio` không được đăng ký
> - ZeroClaw request Composio v3 tools với `toolkit_versions=latest` và thực thi tools với `version="latest"` để tránh stale default tool revisions
> - Luồng điển hình: gọi `connect`, hoàn thành OAuth trình duyệt, sau đó chạy `execute` cho action tool mong muốn
> - Nếu Composio trả về lỗi missing connected-account reference, gọi `list_accounts` (tùy chọn với `app`) và truyền `connected_account_id` trả về tới `execute`

## `[cost]`

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt tracking chi phí |
| `daily_limit_usd` | `10.00` | Giới hạn chi tiêu hàng ngày (USD) |
| `monthly_limit_usd` | `100.00` | Giới hạn chi tiêu hàng tháng (USD) |
| `warn_at_percent` | `80` | Cảnh báo khi chi tiêu đạt % này của giới hạn |
| `allow_override` | `false` | Cho phép request vượt ngân sách với flag `--override` |

> [!note]
> - Khi `enabled = true`, runtime theo dõi ước tính chi phí mỗi request và thực thi giới hạn hàng ngày/tháng
> - Tại ngưỡng `warn_at_percent`, cảnh báo được phát ra nhưng request vẫn tiếp tục
> - Khi giới hạn đạt, request bị từ chối trừ khi `allow_override = true` và flag `--override` được truyền

## `[identity]`

| Key | Default | Mục đích |
|------|---------|----------|
| `format` | `openclaw` | Định dạng identity: `"openclaw"` (mặc định) hoặc `"aieos"` |
| `aieos_path` | unset | Đường dẫn tới file AIEOS JSON (tương đối với workspace) |
| `aieos_inline` | unset | AIEOS JSON inline (thay thế cho đường dẫn file) |

> [!note]
> - Dùng `format = "aieos"` với `aieos_path` hoặc `aieos_inline` để load document identity AIEOS/OpenClaw
> - Chỉ nên set một trong `aieos_path` hoặc `aieos_inline`; `aieos_path` ưu tiên hơn

## `[multimodal]`

| Key | Default | Mục đích |
|------|---------|----------|
| `max_images` | `4` | Số lượng marker ảnh tối đa chấp nhận mỗi request |
| `max_image_size_mb` | `5` | Giới hạn kích thước mỗi ảnh trước khi encode base64 |
| `allow_remote_fetch` | `false` | Cho phép fetch URL ảnh `http(s)` từ markers |

> [!note]
> - Runtime chấp nhận marker ảnh trong tin nhắn người dùng với cú pháp: ``[IMAGE:<source>]``
> - Nguồn hỗ trợ:
>   - Đường dẫn file local (ví dụ ``[IMAGE:/tmp/screenshot.png]``)
>   - Data URI (ví dụ ``[IMAGE:data:image/png;base64,...]``)
>   - URL remote chỉ khi `allow_remote_fetch = true`
> - MIME types cho phép: `image/png`, `image/jpeg`, `image/webp`, `image/gif`, `image/bmp`
> - Khi provider active không hỗ trợ vision, request fail với lỗi capability có cấu trúc (`capability=vision`) thay vì drop ảnh im lặng

## `[browser]`

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt tool `browser_open` (mở URL trong trình duyệt hệ thống mà không scrape) |
| `allowed_domains` | `[]` | Domains cho phép cho `browser_open` (match exact/subdomain, hoặc `"*"` cho tất cả domains public) |
| `session_name` | unset | Tên session trình duyệt (cho automation agent-browser) |
| `backend` | `agent_browser` | Backend automation trình duyệt: `"agent_browser"`, `"rust_native"`, `"computer_use"`, hoặc `"auto"` |
| `native_headless` | `true` | Chế độ headless cho backend rust-native |
| `native_webdriver_url` | `http://127.0.0.1:9515` | Endpoint WebDriver cho backend rust-native |
| `native_chrome_path` | unset | Đường dẫn executable Chrome/Chromium tùy chọn cho backend rust-native |

### `[browser.computer_use]`

| Key | Default | Mục đích |
|------|---------|----------|
| `endpoint` | `http://127.0.0.1:8787/v1/actions` | Endpoint sidecar cho actions computer-use (mouse/keyboard/screenshot mức OS) |
| `api_key` | unset | Bearer token tùy chọn cho sidecar computer-use (lưu trữ mã hóa) |
| `timeout_ms` | `15000` | Timeout request mỗi action (milliseconds) |
| `allow_remote_endpoint` | `false` | Cho phép endpoint remote/public cho sidecar computer-use |
| `window_allowlist` | `[]` | Danh sách allowlist title/process window forward tới policy sidecar |
| `max_coordinate_x` | unset | Giới hạn trục X tùy chọn cho actions dựa coordinate |
| `max_coordinate_y` | unset | Giới hạn trục Y tùy chọn cho actions dựa coordinate |

> [!note]
> - Khi `backend = "computer_use"`, agent ủy quyền actions trình duyệt tới sidecar tại `computer_use.endpoint`
> - `allow_remote_endpoint = false` (mặc định) từ chối bất kỳ endpoint non-loopback nào để ngăn exposure public ngoài ý muốn
> - Dùng `window_allowlist` để hạn chế những cửa sổ OS nào sidecar có thể tương tác

## `[http_request]`

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt tool `http_request` cho tương tác API |
| `allowed_domains` | `[]` | Domains cho phép cho HTTP requests (match exact/subdomain, hoặc `"*"` cho tất cả domains public) |
| `max_response_size` | `1000000` | Kích thước response tối đa (bytes, mặc định: 1MB) |
| `timeout_secs` | `30` | Timeout request (giây) |

> [!note]
> - Deny-by-default: nếu `allowed_domains` rỗng, tất cả HTTP requests bị từ chối
> - Dùng exact domain hoặc subdomain matching (ví dụ: `"api.example.com"`, `"example.com"`), hoặc `"*"` để cho phép bất kỳ domain public nào
> - Target local/private vẫn bị chặn ngay cả khi `"*"` được cấu hình

## `[gateway]`

| Key | Default | Mục đích |
|------|---------|----------|
| `host` | `127.0.0.1` | Địa chỉ bind |
| `port` | `42617` | Cổng lắng nghe gateway |
| `require_pairing` | `true` | Yêu cầu pairing trước khi xác thực bearer |
| `allow_public_bind` | `false` | Chặn exposure public ngoài ý muốn |

## `[autonomy]`

| Key | Default | Mục đích |
|------|---------|----------|
| `level` | `supervised` | `read_only`, `supervised`, hoặc `full` |
| `workspace_only` | `true` | Từ chối đường dẫn tuyệt đối trừ khi tắt explicit |
| `allowed_commands` | _required for shell execution_ | Danh sách allow executable names, đường dẫn executable rõ ràng, hoặc `"*"` |
| `forbidden_paths` | built-in protected list | Danh sách deny path rõ ràng (system paths + sensitive dotdirs mặc định) |
| `allowed_roots` | `[]` | roots bổ sung cho phép ngoài workspace sau canonicalization |
| `max_actions_per_hour` | `20` | ngân sách action mỗi policy |
| `max_cost_per_day_cents` | `500` | rào cản chi tiêu mỗi policy (cent) |
| `require_approval_for_medium_risk` | `true` | gate approval cho commands medium-risk |
| `block_high_risk_commands` | `true` | block cứng commands high-risk |
| `auto_approve` | `[]` | operations tool luôn auto-approved |
| `always_ask` | `[]` | operations tool luôn yêu cầu approval |

> [!note]
> - `level = "full"` bỏ qua gate approval medium-risk cho shell execution, trong khi vẫn thực thi rào cản cấu hình
> - Truy cập ngoài workspace yêu cầu `allowed_roots`, ngay cả khi `workspace_only = false`
> - `allowed_roots` hỗ trợ đường dẫn tuyệt đối, `~/...`, và đường dẫn tương đối workspace
> - `allowed_commands` entries có thể là tên command (ví dụ: `"git"`), đường dẫn executable rõ ràng (ví dụ: `"/usr/bin/antigravity"`), hoặc `"*"` để cho phép bất kỳ tên/path command nào (rào cản risk vẫn áp dụng)
> - Phân tích tách shell quote-aware. Ký tự như `;` bên trong arguments quoted được xử lý như literals, không phải tách command
> - Unquoted shell chaining/operators vẫn bị enforced bởi policy checks (`;`, `|`, `&&`, `||`, background chaining, redirects)

**Ví dụ:**
```toml
[autonomy]
workspace_only = false
forbidden_paths = ["/etc", "/root", "/proc", "/sys", "~/.ssh", "~/.gnupg", "~/.aws"]
allowed_roots = ["~/Desktop/projects", "/opt/shared-repo"]
```

## `[memory]`

| Key | Default | Mục đích |
|------|---------|----------|
| `backend` | `sqlite` | `sqlite`, `lucid`, `markdown`, `none` |
| `auto_save` | `true` | chỉ lưu inputs người dùng (output assistant bị loại trừ) |
| `embedding_provider` | `none` | `none`, `openai`, hoặc endpoint tùy chỉnh |
| `embedding_model` | `text-embedding-3-small` | ID model embedding, hoặc `hint:<name>` route |
| `embedding_dimensions` | `1536` | kích thước vector expected cho model embedding đã chọn |
| `vector_weight` | `0.7` | trọng số ranking vector hybrid |
| `keyword_weight` | `0.3` | trọng số ranking keyword hybrid |

> [!note]
> - Memory context injection bỏ qua legacy keys `assistant_resp*` auto-save để ngăn old model-authored summaries bị xử lý như facts

## `[[model_routes]]` và `[[embedding_routes]]`

Dùng route hints để integrations giữ tên ổn định trong khi model IDs tiến hóa.

### `[[model_routes]]`

| Key | Default | Mục đích |
|------|---------|----------|
| `hint` | _required_ | Tên hint task (ví dụ: `"reasoning"`, `"fast"`, `"code"`, `"summarize"`) |
| `provider` | _required_ | Provider để route tới (phải match tên provider đã biết) |
| `model` | _required_ | Model để dùng với provider đó |
| `api_key` | unset | API key ghi đè tùy chọn cho route provider này |

### `[[embedding_routes]]`

| Key | Default | Mục đích |
|------|---------|----------|
| `hint` | _required_ | Tên route hint (ví dụ: `"semantic"`, `"archive"`, `"faq"`) |
| `provider` | _required_ | Provider embedding (`"none"`, `"openai"`, hoặc `"custom:<url>"`) |
| `model` | _required_ | Model embedding để dùng với provider đó |
| `dimensions` | unset | Ghi đè dimension embedding tùy chọn cho route này |
| `api_key` | unset | API key ghi đè tùy chọn cho provider route này |

**Ví dụ:**
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

**Chiến lược nâng cấp:**
1. Giữ hints ổn định (`hint:reasoning`, `hint:semantic`)
2. Chỉ update `model = "...new-version..."` trong entries route
3. Validate với `zeroclaw doctor` trước restart/rollout

**Cấu hình ngôn ngữ tự nhiên:**
- Trong cuộc trò chuyện agent bình thường, yêu cầu assistant rewire routes bằng ngôn ngữ tự nhiên
- Runtime có thể persist updates này qua tool `model_routing_config` (defaults, scenarios, delegate sub-agents) mà không cần chỉnh sửa TOML thủ công

**Yêu cầu ví dụ:**
- `Set conversation to provider kimi, model moonshot-v1-8k.`
- `Set coding to provider openai, model gpt-5.3-codex, and auto-route when message contains code blocks.`
- `Create a coder sub-agent using openai/gpt-5.3-codex with tools file_read,file_write,shell.`

## `[query_classification]`

Tự động routing hint model — map tin nhắn người dùng tới giá trị hint `[[model_routes]]` dựa trên patterns nội dung.

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt phân loại query tự động |
| `rules` | `[]` | Rules phân loại (đánh giá theo thứ tự ưu tiên) |

Mỗi rule trong `rules`:

| Key | Default | Mục đích |
|------|---------|----------|
| `hint` | _required_ | Phải match giá trị hint `[[model_routes]]` |
| `keywords` | `[]` | Matches substring không phân biệt hoa thường |
| `patterns` | `[]` | Matches literal phân biệt hoa thường (cho code fences, keywords như `"fn "`) |
| `min_length` | unset | Chỉ match nếu length tin nhắn ≥ N ký tự |
| `max_length` | unset | Chỉ match nếu length tin nhắn ≤ N ký tự |
| `priority` | `0` | Rules ưu tiên cao được kiểm tra trước |

**Ví dụ:**
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

## `[channels_config]`

Tùy chọn channel cấp cao được cấu hình dưới `channels_config`.

| Key | Default | Mục đích |
|------|---------|----------|
| `message_timeout_secs` | `300` | Timeout base (giây) cho xử lý tin nhắn channel; runtime scale timeout này với depth vòng lặp tool (lên tới 4x) |

**Ví dụ channel:**
- `[channels_config.telegram]`
- `[channels_config.discord]`
- `[channels_config.whatsapp]`
- `[channels_config.linq]`
- `[channels_config.nextcloud_talk]`
- `[channels_config.email]`
- `[channels_config.nostr]`

> [!note]
> - Mặc định `300s` được tối ưu cho LLMs on-device (Ollama) chậm hơn APIs cloud
> - Ngân sách timeout runtime là `message_timeout_secs * scale`, trong đó `scale = min(max_tool_iterations, 4)` và tối thiểu là `1`
> - Việc scale này tránh timeout sai khi vòng lặp LLM đầu tiên chậm/được retry nhưng vòng lặp tool sau vẫn cần hoàn thành
> - Nếu dùng APIs cloud (OpenAI, Anthropic, etc.), có thể giảm xuống `60` hoặc thấp hơn
> - Giá trị dưới `30` bị clamp về `30` để tránh timeout churn ngay lập tức
> - Khi timeout xảy ra, users nhận: `⚠️ Request timed out while waiting for the model. Please try again.`
> - Hành vi interruption Telegram-only được điều khiển bởi `channels_config.telegram.interrupt_on_new_message` (mặc định `false`). Khi enabled, tin nhắn mới hơn từ cùng sender trong cùng chat hủy request đang chạy và preserve context user bị gián đoạn
> - Trong khi `zeroclaw channel start` đang chạy, updates tới `default_provider`, `default_model`, `default_temperature`, `api_key`, `api_url`, và `reliability.*` được hot-applied từ `config.toml` trên tin nhắn inbound tiếp theo

### `[channels_config.nostr]`

| Key | Default | Mục đích |
|------|---------|----------|
| `private_key` | _required_ | Nostr private key (hex hoặc `nsec1…` bech32); lưu trữ mã hóa khi `secrets.encrypt = true` |
| `relays` | xem ghi chú | Danh sách URL WebSocket relay; mặc định: `relay.damus.io`, `nos.lol`, `relay.primal.net`, `relay.snort.social` |
| `allowed_pubkeys` | `[]` (deny all) | Sender allowlist (hex hoặc `npub1…`); dùng `"*"` để cho phép tất cả senders |

> [!note]
> - Hỗ trợ cả NIP-04 (DMs mã hóa legacy) và NIP-17 (private messages gift-wrapped). Phản hồi mirror protocol của sender tự động
> - `private_key` là secret giá trị cao; giữ `secrets.encrypt = true` (mặc định) trong production

Xem [111-i18n-vi-channels-reference|channels-reference] để matrix channel chi tiết và hành vi allowlist.

### `[channels_config.whatsapp]`

WhatsApp hỗ trợ hai backends dưới một bảng config.

**Chế độ Cloud API (Meta webhook):**

| Key | Required | Mục đích |
|------|---------|----------|
| `access_token` | Yes | Bearer token Meta Cloud API |
| `phone_number_id` | Yes | ID số điện thoại Meta |
| `verify_token` | Yes | Token verification webhook |
| `app_secret` | Optional | Kích hoạt verification chữ ký webhook (`X-Hub-Signature-256`) |
| `allowed_numbers` | Recommended | Số điện thoại inbound cho phép (`[]` = deny all, `"*"` = allow all) |

**Chế độ WhatsApp Web (client native):**

| Key | Required | Mục đích |
|------|---------|----------|
| `session_path` | Yes | Đường dẫn session SQLite persistent |
| `pair_phone` | Optional | Số điện thoại flow pair (digits only) |
| `pair_code` | Optional | Mã pair tùy chỉnh (nếu không auto-generated) |
| `allowed_numbers` | Recommended | Số điện thoại inbound cho phép (`[]` = deny all, `"*"` = allow all) |

> [!note]
> - WhatsApp Web yêu cầu flag build `whatsapp-web`
> - Nếu cả Cloud và Web fields tồn tại, Cloud mode thắng vì tương thích ngược

### `[channels_config.linq]`

Tích hợp Linq Partner V3 API cho iMessage, RCS, SMS.

| Key | Required | Mục đích |
|------|---------|----------|
| `api_token` | Yes | Bearer token API Linq Partner |
| `from_phone` | Yes | Số điện thoại gửi (format E.164) |
| `signing_secret` | Optional | Secret ký webhook cho HMAC-SHA256 verification chữ ký |
| `allowed_senders` | Recommended | Số điện thoại inbound cho phép (`[]` = deny all, `"*"` = allow all) |

> [!note]
> - Endpoint webhook là `POST /linq`
> - `ZEROCLAW_LINQ_SIGNING_SECRET` ghi đè `signing_secret` khi set
> - Chữ ký dùng headers `X-Webhook-Signature` và `X-Webhook-Timestamp`; timestamps cũ (>300s) bị từ chối
> - Xem [111-i18n-vi-channels-reference|channels-reference] để ví dụ config đầy đủ

### `[channels_config.nextcloud_talk]`

Tích hợp bot Nextcloud Talk native (webhook receive + OCS send API).

| Key | Required | Mục đích |
|------|---------|----------|
| `base_url` | Yes | Nextcloud base URL (ví dụ: `https://cloud.example.com`) |
| `app_token` | Yes | Bot app token dùng cho OCS bearer auth |
| `webhook_secret` | Optional | Kích hoạt verification chữ ký webhook |
| `allowed_users` | Recommended | Nextcloud actor IDs cho phép (`[]` = deny all, `"*"` = allow all) |

> [!note]
> - Endpoint webhook là `POST /nextcloud-talk`
> - `ZEROCLAW_NEXTCLOUD_TALK_WEBHOOK_SECRET` ghi đè `webhook_secret` khi set
> - Xem [nextcloud-talk-setup.md](../../setup-guides/nextcloud-talk-setup.md) để setup và troubleshooting

## `[hardware]`

Cấu hình wizard hardware cho truy cập thế giới vật lý (STM32, probe, serial).

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Cho phép truy cập hardware |
| `transport` | `none` | Chế độ transport: `"none"`, `"native"`, `"serial"`, hoặc `"probe"` |
| `serial_port` | unset | Đường dẫn port serial (ví dụ: `"/dev/ttyACM0"`) |
| `baud_rate` | `115200` | Baud rate serial |
| `probe_target` | unset | Target chip probe (ví dụ: `"STM32F401RE"`) |
| `workspace_datasheets` | `false` | Kích hoạt RAG datasheet workspace (index PDF schematics cho AI tra cứu pin) |

> [!note]
> - Dùng `transport = "serial"` với `serial_port` cho kết nối USB-serial
> - Dùng `transport = "probe"` với `probe_target` cho flashing probe debug (ví dụ: ST-Link)
> - Xem [hardware-peripherals-design.md](../../hardware/hardware-peripherals-design.md) để chi tiết protocol

## `[peripherals]`

Cấu hình peripheral cấp cao hơn. Boards trở thành tools agent khi enabled.

| Key | Default | Mục đích |
|------|---------|----------|
| `enabled` | `false` | Kích hoạt support peripheral (boards trở thành tools agent) |
| `boards` | `[]` | Cấu hình boards |
| `datasheet_dir` | unset | Đường dẫn docs datasheet (tương đối workspace) cho retrieval RAG |

Mỗi entry trong `boards`:

| Key | Default | Mục đích |
|------|---------|----------|
| `board` | _required_ | Loại board: `"nucleo-f401re"`, `"rpi-gpio"`, `"esp32"`, etc. |
| `transport` | `serial` | Transport: `"serial"`, `"native"`, `"websocket"` |
| `path` | unset | Đường dẫn cho serial: `"/dev/ttyACM0"`, `"/dev/ttyUSB0"` |
| `baud` | `115200` | Baud rate cho serial |

**Ví dụ:**
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
> - Đặt file `.md`/`.txt` datasheet đặt tên theo board (ví dụ: `nucleo-f401re.md`, `rpi-gpio.md`) trong `datasheet_dir` cho retrieval RAG
> - Xem [hardware-peripherals-design.md](../../hardware/hardware-peripherals-design.md) để chi tiết protocol board và firmware

## Mặc định liên quan bảo mật

- deny-by-default channel allowlists (`[]` nghĩa là deny all)
- pairing required trên gateway mặc định
- public bind disabled mặc định

## Lệnh validation sau chỉnh sửa config

```bash
zeroclaw status
zeroclaw doctor
zeroclaw channel doctor
zeroclaw service restart
```

## Tài liệu liên quan

- [[111-i18n-vi-channels-reference|channels-reference]]
- providers-reference.md
- operations-runbook.md
- troubleshooting.md

#zeroclaw #configuration #toml