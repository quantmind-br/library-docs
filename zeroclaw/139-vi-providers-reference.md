---
optimized: true
optimized_at: 2026-05-05T00:00:00Z
title: Providers reference
url: https://github.com/openagen/zeroclaw/blob/master/docs/vi/providers-reference.md
source: git
fetched_at: 2026-05-02T14:52:49.570326991-03:00
rendered_js: false
word_count: 840
summary: This document serves as a comprehensive reference for ZeroClaw providers, detailing configuration, environment variable requirements, authentication precedence, and provider-specific features.
tags:
    - zeroclaw
    - provider-reference
    - api-authentication
    - environment-variables
    - configuration
    - llm-integrations
category: reference
---
# Tài liệu tham khảo Providers — ZeroClaw

Cập nhật lần cuối: **2026-03-10**.

## Liệt kê providers

```bash
zeroclaw providers
```

## Thứ tự ưu tiên xác thực runtime

1. Thông tin xác thực tường minh từ config/CLI
2. Biến môi trường dành riêng cho provider
3. Biến môi trường dự phòng chung: `ZEROCLAW_API_KEY`, sau đó là `API_KEY`

Với chuỗi provider dự phòng (`reliability.fallback_providers`), mỗi provider tự giải quyết thông tin xác thực độc lập. Key chính không tự động dùng cho provider dự phòng.

## Danh mục providers

| Canonical ID | Alias | Cục bộ | Biến môi trường dành riêng |
|--------------|-------|--------|---------------------------|
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
| `copilot` | `github-copilot` | Không | Dùng config/`API_KEY` fallback với GitHub token |
| `lmstudio` | `lm-studio` | Có | Tùy chọn; mặc định cục bộ |
| `nvidia` | `nvidia-nim`, `build.nvidia.com` | Không | `NVIDIA_API_KEY` |

### Ghi chú Gemini

- Provider ID: `gemini` (alias: `google`, `google-gemini`)
- Xác thực: `GEMINI_API_KEY`, `GOOGLE_API_KEY`, hoặc Gemini CLI OAuth cache (`~/.gemini/oauth_creds.json`)
- API key → endpoint: `generativelanguage.googleapis.com/v1beta`
- OAuth → endpoint: `cloudcode-pa.googleapis.com/v1internal`

### Ghi chú Ollama Vision

- Provider ID: `ollama`
- Hỗ trợ hình ảnh: marker nội tuyến ``[IMAGE:<source>]``
- ZeroClaw gửi payload hình ảnh qua trường `messages[].images` gốc của Ollama
- Lỗi rõ ràng nếu provider không hỗ trợ vision

### Ghi chú Bedrock

- Provider ID: `bedrock` (alias: `aws-bedrock`)
- API: [Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
- Xác thực: AWS AKSK (không phải API key đơn lẻ)
- Tùy chọn: `AWS_SESSION_TOKEN`, `AWS_REGION` hoặc `AWS_DEFAULT_REGION` (mặc định: `us-east-1`)
- Model mặc định: `anthropic.claude-sonnet-4-5-20250929-v1:0`
- Tính năng: native tool calling, prompt caching (`cachePoint`), cross-region inference profiles
- Định dạng model: `anthropic.claude-sonnet-4-6`, `anthropic.claude-opus-4-6-v1`

### Kiểm soát reasoning của Ollama

Cấu hình trong `config.toml`:

```toml
[runtime]
reasoning_enabled = false
```

Hành vi:
- `false`: gửi `think: false` đến `/api/chat`
- `true`: gửi `think: true`
- Không đặt: bỏ qua `think` (mặc định của Ollama/model)

### Ghi chú Kimi Code

- Provider ID: `kimi-code`
- Endpoint: `https://api.kimi.com/coding/v1`
- Model mặc định: `kimi-for-coding` (thay thế: `kimi-k2.5`)
- User-Agent: `KimiCLI/0.77`

### Ghi chú NVIDIA NIM

- Canonical ID: `nvidia`
- Alias: `nvidia-nim`, `build.nvidia.com`
- Base API URL: `https://integrate.api.nvidia.com/v1`
- Khám phá model: `zeroclaw models refresh --provider nvidia`

Model ID khuyến nghị (2026-02-18):
- `meta/llama-3.3-70b-instruct`
- `deepseek-ai/deepseek-v3.2`
- `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- `nvidia/llama-3.1-nemotron-ultra-253b-v1`

## Endpoint tùy chỉnh

- OpenAI-compatible:

```toml
default_provider = "custom:https://your-api.example.com"
```

- Anthropic-compatible:

```toml
default_provider = "anthropic-custom:https://your-api.example.com"
```

## Cấu hình MiniMax OAuth

Cấu hình trong `config.toml`:

```toml
default_provider = "minimax-oauth"
api_key = "minimax-oauth"
```

Thứ tự ưu tiên xác thực:
1. `MINIMAX_OAUTH_TOKEN` (ưu tiên)
2. `MINIMAX_API_KEY`
3. `MINIMAX_OAUTH_REFRESH_TOKEN`

Tùy chọn:
- `MINIMAX_OAUTH_REGION=global` hoặc `cn` (mặc định theo alias)
- `MINIMAX_OAUTH_CLIENT_ID`

Lưu ý: Lịch sử channel được chuẩn hóa để duy trì thứ tự `user`/`assistant` hợp lệ

## Cấu hình Qwen Code OAuth

Cấu hình trong `config.toml`:

```toml
default_provider = "qwen-code"
api_key = "qwen-oauth"
```

Thứ tự ưu tiên xác thực:
1. Giá trị `api_key` tường minh (nếu không phải placeholder `qwen-oauth`)
2. `QWEN_OAUTH_TOKEN`
3. `~/.qwen/oauth_creds.json`
4. `QWEN_OAUTH_REFRESH_TOKEN`
5. `DASHSCOPE_API_KEY` (dự phòng)

Tùy chọn ghi đè endpoint: `QWEN_OAUTH_RESOURCE_URL`

## Định tuyến model (hint)

Định tuyến model theo hint sử dụng `[[model_routes]]`:

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

Gọi model:
```text
hint:reasoning
```

## Định tuyến embedding (hint)

Định tuyến embedding sử dụng `[[embedding_routes]]`.
Đặt `[memory].embedding_model = "hint:<name>"` để kích hoạt.

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

Provider hỗ trợ:
- `none`
- `openai`
- `custom:<url>` (OpenAI-compatible)

Ghi đè key theo route:

```toml
[[embedding_routes]]
hint = "semantic"
provider = "openai"
model = "text-embedding-3-small"
api_key = "sk-route-specific"
```

## Nâng cấp model an toàn

Quy trình khuyến nghị:
1. Giữ nguyên call site (`hint:reasoning`, `hint:semantic`)
2. Chỉ thay đổi model đích trong `[[model_routes]]` hoặc `[[embedding_routes]]`
3. Chạy: `zeroclaw doctor`, `zeroclaw status`
4. Smoke test trước triển khai

Cách này giảm thiểu rủi ro phá vỡ tích hợp và prompt.
