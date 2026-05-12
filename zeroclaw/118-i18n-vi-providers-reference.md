---
title: Providers reference
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/providers-reference.md
source: git
fetched_at: 2026-05-02T14:51:27.727734932-03:00
rendered_js: false
word_count: 1108
summary: This document serves as a comprehensive reference for ZeroClaw providers, detailing provider IDs, aliases, environment variable configuration, authentication precedence, and specific integration notes for various AI services.
tags:
    - zeroclaw
    - provider-reference
    - api-authentication
    - environment-variables
    - configuration
    - llm-integration
category: reference
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Tài liệu tham khảo Providers — ZeroClaw

Tài liệu này liệt kê các provider ID, alias và biến môi trường chứa thông tin xác thực.

> [!info]
> Cập nhật lần cuối: **2026-03-10**

---

## 1. Cách liệt kê các Provider

```bash
zeroclaw providers
```

---

## 2. Thứ tự ưu tiên khi giải quyết thông tin xác thực

Thứ tự ưu tiên tại runtime:

1. Thông tin xác thực tường minh từ config/CLI
2. Biến môi trường dành riêng cho provider
3. Biến môi trường dự phòng chung: `ZEROCLAW_API_KEY`, sau đó là `API_KEY`

> [!note]
> Với chuỗi provider dự phòng (`reliability.fallback_providers`), mỗi provider dự phòng tự giải quyết thông tin xác thực của mình độc lập. Key xác thực của provider chính không tự động dùng cho provider dự phòng.

---

## 3. Danh mục Provider

| Canonical ID | Alias | Cục bộ | Biến môi trường dành riêng |
|---|---|---:|---|
| `openrouter` | — | Không | `OPENROUTER_API_KEY` |
| `anthropic` | — | Không | `ANTHROPIC_OAUTH_TOKEN`, `ANTHROPIC_API_KEY` |
| `openai` | — | Không | `OPENAI_API_KEY` |
| `ollama` | — | Có | `OLLAMA_API_KEY` (tùy chọn) |
| `gemini` | `google`, `google-gemini` | Không | `GEMINI_API_KEY`, `GOOGLE_API_KEY` |
| `venice` | — | Không | `VENICE_API_KEY` |
| `vercel` | `vercel-ai` | Không | `VERCEL_API_KEY` |
| `cloudflare` | `cloudflare-ai` | Không | `CLOUDFLARE_API_KEY` |
| `moonshot` | `kimi` | Không | `MOONSHOT_API_KEY` |
| `kimi-code` | `kimi_coding`, `kimi_for_coding` | Không | `KIMI_CODE_API_KEY`, `MOONSHOT_API_KEY` |
| `synthetic` | — | Không | `SYNTHETIC_API_KEY` |
| `opencode` | `opencode-zen` | Không | `OPENCODE_API_KEY` |
| `opencode-go` | — | Không | `OPENCODE_GO_API_KEY` |
| `zai` | `z.ai` | Không | `ZAI_API_KEY` |
| `glm` | `zhipu` | Không | `GLM_API_KEY` |
| `minimax` | `minimax-intl`, `minimax-io`, `minimax-global`, `minimax-cn`, `minimaxi`, `minimax-oauth`, `minimax-oauth-cn`, `minimax-portal`, `minimax-portal-cn` | Không | `MINIMAX_OAUTH_TOKEN`, `MINIMAX_API_KEY` |
| `bedrock` | `aws-bedrock` | Không | `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY` (tùy chọn: `AWS_REGION`) |
| `qianfan` | `baidu` | Không | `QIANFAN_API_KEY` |
| `qwen` | `dashscope`, `qwen-intl`, `dashscope-intl`, `qwen-us`, `dashscope-us`, `qwen-code`, `qwen-oauth`, `qwen_oauth` | Không | `QWEN_OAUTH_TOKEN`, `DASHSCOPE_API_KEY` |
| `groq` | — | Không | `GROQ_API_KEY` |
| `mistral` | — | Không | `MISTRAL_API_KEY` |
| `xai` | `grok` | Không | `XAI_API_KEY` |
| `deepseek` | — | Không | `DEEPSEEK_API_KEY` |
| `together` | `together-ai` | Không | `TOGETHER_API_KEY` |
| `fireworks` | `fireworks-ai` | Không | `FIREWORKS_API_KEY` |
| `perplexity` | — | Không | `PERPLEXITY_API_KEY` |
| `cohere` | — | Không | `COHERE_API_KEY` |
| `copilot` | `github-copilot` | Không | (dùng config/`API_KEY` fallback với GitHub token) |
| `lmstudio` | `lm-studio` | Có | (tùy chọn; mặc định là cục bộ) |
| `nvidia` | `nvidia-nim`, `build.nvidia.com` | Không | `NVIDIA_API_KEY` |

---

## 4. Ghi chú chi tiết theo provider

### 4.1 Gemini

- **Provider ID:** `gemini` (alias: `google`, `google-gemini`)
- **Xác thực:** Có thể dùng `GEMINI_API_KEY`, `GOOGLE_API_KEY`, hoặc Gemini CLI OAuth cache (`~/.gemini/oauth_creds.json`)
- **Endpoint:**
  - API key: `generativelanguage.googleapis.com/v1beta`
  - OAuth: `cloudcode-pa.googleapis.com/v1internal` (theo chuẩn Code Assist)

### 4.2 Ollama Vision

- **Provider ID:** `ollama`
- **Hỗ trợ đa phương tiện:** Có (qua marker nội tuyến ``[IMAGE:<source>]``)
- **Cơ chế:** Sau khi chuẩn hóa multimodal, ZeroClaw gửi payload hình ảnh qua trường `messages[].images` gốc của Ollama
- **Lỗi capability:** Nếu provider không hỗ trợ vision, ZeroClaw trả về lỗi rõ ràng thay vì âm thầm bỏ qua hình ảnh

### 4.3 Bedrock (AWS)

- **Provider ID:** `bedrock` (alias: `aws-bedrock`)
- **API:** [Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
- **Xác thực:** AWS AKSK (không phải API key đơn lẻ)
  - Bắt buộc: `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY`
  - Tùy chọn: `AWS_SESSION_TOKEN`, `AWS_REGION` hoặc `AWS_DEFAULT_REGION` (mặc định: `us-east-1`)
- **Model mặc định:** `anthropic.claude-sonnet-4-5-20250929-v1:0`
- **Tính năng:** Native tool calling, prompt caching (`cachePoint`), cross-region inference profiles (ví dụ: `us.anthropic.claude-*`)
- **Định dạng model:** `anthropic.claude-sonnet-4-6`, `anthropic.claude-opus-4-6-v1`

### 4.4 Ollama Reasoning Control

Kiểm soát hành vi reasoning/thinking của Ollama từ `config.toml`:

```toml
[runtime]
reasoning_enabled = false
```

**Hành vi:**
- `false`: gửi `think: false` đến `/api/chat`
- `true`: gửi `think: true`
- Không đặt: bỏ qua `think` và giữ nguyên mặc định của Ollama/model

### 4.5 Kimi Code

- **Provider ID:** `kimi-code`
- **Endpoint:** `https://api.kimi.com/coding/v1`
- **Model mặc định:** `kimi-for-coding` (thay thế: `kimi-k2.5`)
- **User-Agent:** Tự động thêm `User-Agent: KimiCLI/0.77`

### 4.6 NVIDIA NIM

- **Canonical ID:** `nvidia`
- **Alias:** `nvidia-nim`, `build.nvidia.com`
- **Base API URL:** `https://integrate.api.nvidia.com/v1`
- **Cách khám phá model:** `zeroclaw models refresh --provider nvidia`

**Model ID khởi đầu được khuyến nghị (đã xác minh 2026-02-18):**
- `meta/llama-3.3-70b-instruct`
- `deepseek-ai/deepseek-v3.2`
- `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- `nvidia/llama-3.1-nemotron-ultra-253b-v1`

---

## 5. Endpoint Tùy chỉnh

### 5.1 OpenAI-compatible

```toml
default_provider = "custom:https://your-api.example.com"
```

### 5.2 Anthropic-compatible

```toml
default_provider = "anthropic-custom:https://your-api.example.com"
```

---

## 6. Cấu hình OAuth chuyên biệt

### 6.1 MiniMax OAuth

Đặt provider MiniMax và OAuth placeholder trong config:

```toml
default_provider = "minimax-oauth"
api_key = "minimax-oauth"
```

**Thứ tự ưu tiên giải quyết thông tin xác thực:**
1. `MINIMAX_OAUTH_TOKEN` (ưu tiên, access token trực tiếp)
2. `MINIMAX_API_KEY` (token tĩnh/cũ)
3. `MINIMAX_OAUTH_REFRESH_TOKEN` (tự động làm mới access token)

**Tùy chọn:**
- `MINIMAX_OAUTH_REGION=global` hoặc `cn` (mặc định theo alias)
- `MINIMAX_OAUTH_CLIENT_ID` để ghi đè client id mặc định

> [!note]
> Đối với các cuộc trò chuyện channel được hỗ trợ bởi MiniMax, lịch sử runtime được chuẩn hóa để duy trì thứ tự lượt hợp lệ `user`/`assistant`. Hướng dẫn phân phối đặc thù của channel được hợp nhất vào system prompt đầu tiên.

### 6.2 Qwen Code OAuth

Đặt chế độ Qwen Code OAuth trong config:

```toml
default_provider = "qwen-code"
api_key = "qwen-oauth"
```

**Thứ tự ưu tiên giải quyết thông tin xác thực:**
1. Giá trị `api_key` tường minh (nếu không phải placeholder `qwen-oauth`)
2. `QWEN_OAUTH_TOKEN`
3. `~/.qwen/oauth_creds.json` (tái sử dụng cache OAuth)
4. `QWEN_OAUTH_REFRESH_TOKEN` (hoặc refresh token đã cache)
5. `DASHSCOPE_API_KEY` làm dự phòng

**Tùy chọn ghi đè endpoint:**
- `QWEN_OAUTH_RESOURCE_URL` (chuẩn hóa thành `https://.../v1` nếu cần)

---

## 7. Định tuyến Model (`hint:<name>`)

Định tuyến các lời gọi model theo hint bằng `[[model_routes]]`:

```toml
[[model_routes]]
hint = "reasoning"
provider = "openrouter"
model = "anthropic/claude-opus-4-20250514"

[[model_routes]]
hint = "fast"
provider = "groq"
model = "llama-3.3-70b-versatile"
```

**Cách gọi:**
```text
hint:reasoning
```

---

## 8. Định tuyến Embedding (`hint:<name>`)

Định tuyến các lời gọi embedding theo cùng mẫu hint bằng `[[embedding_routes]]`.
Đặt `[memory].embedding_model` thành giá trị `hint:<name>` để kích hoạt định tuyến.

```toml
[memory]
embedding_model = "hint:semantic"

[[embedding_routes]]
hint = "semantic"
provider = "openai"
model = "text-embedding-3-small"
dimensions = 1536

[[embedding_routes]]
hint = "archive"
provider = "custom:https://embed.example.com/v1"
model = "your-embedding-model-id"
dimensions = 1024
```

**Embedding provider được hỗ trợ:**
- `none`
- `openai`
- `custom:<url>` (endpoint tương thích OpenAI)

**Ghi đè key theo route:**
```toml
[[embedding_routes]]
hint = "semantic"
provider = "openai"
model = "text-embedding-3-small"
api_key = "sk-route-specific"
```

---

## 9. Nâng cấp Model An toàn

**Quy trình khuyến nghị:**

1. Giữ nguyên các call site (`hint:reasoning`, `hint:semantic`)
2. Chỉ thay đổi model đích trong `[[model_routes]]` hoặc `[[embedding_routes]]`
3. Chạy kiểm tra:
   - `zeroclaw doctor`
   - `zeroclaw status`
4. Smoke test một luồng đại diện trước khi triển khai

**Lợi ích:**
- Giảm thiểu rủi ro phá vỡ vì các tích hợp và prompt không cần thay đổi
- Các model ID cũ có thể ngừng hoạt động mà không ảnh hưởng đến call site

#tags #zeroclaw #provider-reference #api-authentication #environment-variables #configuration #llm-integration