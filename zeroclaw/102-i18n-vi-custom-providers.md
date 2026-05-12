---
title: Custom providers
title_vi: Cấu hình Provider Tùy chỉnh
url: https://github.com/openagen/zeroclaw/blob/master/docs/i18n/vi/custom-providers.md
source: git
fetched_at: 2026-05-02T14:51:09.667193956-03:00
rendered_js: false
word_count: 163
summary: Tài liệu hướng dẫn cách thiết lập và cấu hình các nhà cung cấp dịch vụ LLM tùy chỉnh thông qua giao thức OpenAI hoặc Anthropic trong ZeroClaw. Nội dung bao gồm cách cấu hình qua file hoặc biến môi trường, cùng các bước khắc phục sự cố kết nối và xác thực.
optimized: true
optimized_at: 2026-05-05T00:00:00Z
tags:
  - zeroclaw
  - custom-provider
  - api-configuration
  - llm-integration
  - environment-variables
  - troubleshooting
category: configuration
---
# Cấu hình Provider Tùy chỉnh

ZeroClaw hỗ trợ endpoint API tùy chỉnh tương thích OpenAI và Anthropic.

## Các loại Provider

### OpenAI-compatible (`custom:`)

```toml
[provider]
default_provider = "custom:https://your-api.com"
api_key = "your-api-key"
default_model = "your-model-name"
```

### Anthropic-compatible (`anthropic-custom:`)

```toml
[provider]
default_provider = "anthropic-custom:https://your-api.com"
api_key = "your-api-key"
default_model = "your-model-name"
```

## Cấu hình

### File Config (`~/.zeroclaw/config.toml`)

```toml
api_key = "your-api-key"
default_provider = "anthropic-custom:https://api.example.com"
default_model = "claude-sonnet-4-6"
```

### Biến môi trường

```bash
export API_KEY="your-api-key"
# hoặc: export ZEROCLAW_API_KEY="your-api-key"
zeroclaw agent
```

## Kiểm tra

```bash
# Chế độ tương tác
zeroclaw agent

# Kiểm tra tin nhắn đơn
zeroclaw agent -m "test message"
```

## Xử lý sự cố

### Lỗi xác thực

- Kiểm tra API key
- Kiểm tra định dạng URL (phải có `http://` hoặc `https://`)
- Đảm bảo endpoint truy cập được

### Không tìm thấy Model

- Xác nhận tên model khớp provider
- Kiểm tra endpoint cung cấp model nào
- Kiểm tra model sẵn có:

```bash
curl -sS https://your-api.com/models \
  -H "Authorization: Bearer $API_KEY"
```

- Nếu provider không có `/models`, gửi request chat tối giản để kiểm tra lỗi model trả về

### Sự cố kết nối

- Kiểm tra truy cập endpoint: `curl -I https://your-api.com`
- Kiểm tra firewall/proxy
- Kiểm tra trạng thái provider

## Ví dụ cấu hình

### LLM Server cục bộ

```toml
[provider]
default_provider = "custom:http://localhost:8080"
default_model = "local-model"
```

### Proxy doanh nghiệp

```toml
[provider]
default_provider = "anthropic-custom:https://llm-proxy.corp.example.com"
api_key = "internal-token"
```

### Cloud Provider Gateway

```toml
[provider]
default_provider = "custom:https://gateway.cloud-provider.com/v1"
api_key = "gateway-api-key"
default_model = "gpt-4"
```

#zeroclaw #custom-provider #llm-integration