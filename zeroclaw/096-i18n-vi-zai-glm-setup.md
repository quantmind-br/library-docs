---
title: Zai glm setup
authors:
  - ZeroClaw Team
tags:
  - zeroclaw
  - z-ai
  - glm-models
  - api-configuration
  - ai-integration
  - cli-setup
  - llm-provider
  - openai-compatible
category: configuration
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 644
---
# Thiết lập Z.AI GLM cho ZeroClaw

> ZeroClaw hỗ trợ các model GLM của Z.AI thông qua các endpoint tương thích OpenAI.

## Tóm tắt nhanh

Cấu hình ZeroClaw sử dụng các model GLM (glm-5, glm-4.7, glm-4.6, glm-4.5-air) từ Z.AI thông qua API tương thích OpenAI.

**Cấu hình nhanh:**

```bash
zeroclaw onboard \
  --provider "zai" \
  --api-key "YOUR_ZAI_API_KEY"
```

## Tổng quan

ZeroClaw cung cấp hỗ trợ tích hợp sẵn cho các model GLM của Z.AI thông qua các endpoint tương thích OpenAI:

| Provider Alias | Endpoint | Khu vực |
|----------------|----------|--------|
| `zai` | `https://api.z.ai/api/coding/paas/v4` | Toàn cầu |
| `zai-cn` | `https://open.bigmodel.cn/api/paas/v4` | Trung Quốc |

> [!note]
> Để cấu hình base URL tùy chỉnh, xem [[098-setup-guides-zai-glm-setup|zai-glm-setup]] hoặc [[102-i18n-vi-custom-providers|custom-providers]].

## Các Model Hiện Có

| Model | Mô tả | Trường hợp sử dụng |
|-------|-------|-------------------|
| `glm-5` | Model suy luận mạnh nhất, mặc định | Tác vụ phức tạp, sản xuất |
| `glm-4.7` | Chất lượng đa năng cao | Mục đích chung |
| `glm-4.6` | Model cơ bản cân bằng | Tiết kiệm chi phí |
| `glm-4.5-air` | Tùy chọn độ trễ thấp | Phản hồi nhanh, chịu tải quota cao |

> [!important]
> Tính khả dụng của model phụ thuộc vào tài khoản và khu vực. Sử dụng API `/models` để kiểm tra các model có sẵn.

## Cấu hình Nhanh

### 1. Onboard qua CLI

```bash
# Endpoint toàn cầu (khuyến nghị)
zeroclaw onboard \
  --provider "zai" \
  --api-key "YOUR_ZAI_API_KEY"

# Endpoint Trung Quốc
zeroclaw onboard \
  --provider "zai-cn" \
  --api-key "YOUR_ZAI_API_KEY"
```

### 2. Cấu hình Thủ công

Chỉnh sửa file `~/.zeroclaw/config.toml`:

```toml
[providers.zai]
enabled = true
api_key = "YOUR_ZAI_API_KEY"
default_model = "glm-5"
default_temperature = 0.7
base_url = "https://api.z.ai/api/coding/paas/v4"

[providers.default]
provider = "zai"

[agents.default]
provider = "zai"
model = "glm-5"
```

### 3. Biến Môi trường

Thêm vào file `.env`:

```bash
# Khóa API Z.AI chính
ZAI_API_KEY=your-id.secret

# Khóa chung (dùng bởi nhiều providers)
API_KEY=your-id.secret
```

> [!info]
> Định dạng khóa: `id.secret` (ví dụ: `abc123.xyz789`)

## Xác minh Cấu hình

### Kiểm tra với curl

```bash
# Kiểm tra endpoint tương thích OpenAI
curl -X POST "https://api.z.ai/api/coding/paas/v4/chat/completions" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-5",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

**Phản hồi thành công:**

```json
{
  "choices": [{
    "message": {
      "content": "Hello! How can I help you today?",
      "role": "assistant"
    }
  }]
}
```

### Kiểm tra với CLI ZeroClaw

```bash
# Kiểm tra agent trực tiếp
echo "Hello" | zeroclaw agent

# Kiểm tra trạng thái provider
zeroclaw providers list
zeroclaw providers status zai

# Kiểm tra model cụ thể
zeroclaw chat --model glm-5 --message "What is Rust?"
```

## Cấu hình Nâng cao

### Nhiều Providers

```toml
[providers.zai]
enabled = true
api_key = "global-key.secret"
default_model = "glm-5"

[providers.zai-cn]
enabled = true
api_key = "china-key.secret"
default_model = "glm-4.7"
base_url = "https://open.bigmodel.cn/api/paas/v4"

[agents.default]
provider = "zai"

[agents.china]
provider = "zai-cn"
model = "glm-4.7"
```

### Cài đặt Provider Cụ thể

```toml
[providers.zai]
api_key = "YOUR_API_KEY"
base_url = "https://api.z.ai/api/coding/paas/v4"
default_model = "glm-5"
max_tokens = 4096
temperature = 0.7
top_p = 0.9
frequency_penalty = 0.1
presence_penalty = 0.1

# Cấu hình retry
max_retries = 3
retry_delay_ms = 1000
```

## Xử lý Sự cố

### Lỗi Rate Limiting

**Triệu chứng:**
- Lỗi `rate_limited`
- Phản hồi chậm
- Yêu cầu bị từ chối

**Giải pháp:**
1. Chờ và thử lại
2. Kiểm tra gói Z.AI
3. Sử dụng model độ trễ thấp: `glm-4.5-air`
4. Giảm tần suất yêu cầu

**Ví dụ cấu hình:**

```toml
[providers.zai]
max_retries = 5
retry_delay_ms = 2000
```

### Lỗi Xác thực (401/403)

**Triệu chứng:**
- Lỗi `401 Unauthorized`
- Lỗi `403 Forbidden`
- "Invalid API key"

**Giải pháp:**
1. Xác minh định dạng khóa: `id.secret` (ví dụ: `abc123.xyz789`)
2. Kiểm tra khóa hết hạn
3. Xóa khoảng trắng trong khóa
4. Kiểm tra quyền khóa trên dashboard Z.AI

**Kiểm tra xác thực:**

```bash
curl -I "https://api.z.ai/api/coding/paas/v4/models" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY"
```

### Model Không Tìm Thấy

**Triệu chứng:**
- Lỗi "Model not found"
- Model không khả dụng

**Giải pháp:**
1. Liệt kê model có sẵn:

```bash
curl -s "https://api.z.ai/api/coding/paas/v4/models" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY" | jq '.data[].id'
```

2. Kiểm tra gói đăng ký
3. Sử dụng model dự phòng: `glm-4.6` hoặc `glm-4.5-air`

### Vấn đề Kết nối

**Triệu chứng:**
- Timeouts kết nối
- Lỗi DNS
- Lỗi SSL

**Giải pháp:**
1. Kiểm tra kết nối mạng
2. Xác minh chứng chỉ SSL
3. Kiểm tra tường lửa/proxy
4. Thử endpoint khác

## Lấy API Key

1. Truy cập [https://z.ai](https://z.ai)
2. Đăng ký gói Coding
3. Truy cập Bảng điều khiển API
4. Tạo khóa API (định dạng: `id.secret`)
5. Cấu hình ZeroClaw:

```bash
zeroclaw onboard --provider zai --api-key YOUR_API_KEY
```

## Các Mẹo Tốt Nhất

### Bảo mật
- Sử dụng biến môi trường cho khóa API
- Xoay khóa định kỳ (90 ngày)
- Sử dụng khóa khác nhau cho mỗi môi trường
- Hạn chế quyền khóa trên dashboard Z.AI

### Hiệu suất
- Chọn model phù hợp:
  - `glm-5`: Tác vụ phức tạp
  - `glm-4.7`: Cân bằng
  - `glm-4.6`: Tiết kiệm chi phí
  - `glm-4.5-air`: Độ trễ thấp
- Cài đặt temperature:
  - `0.0-0.3`: Xác định
  - `0.3-0.7`: Cân bằng
  - `0.7-1.0`: Sáng tạo

### Tối ưu Chi phí
- Cache responses
- Gom cụm yêu cầu
- Giám sát sử dụng
- Thiết lập cảnh báo thanh toán

## Tài liệu Liên quan

- [[098-setup-guides-zai-glm-setup|zai-glm-setup]]
- [[100-vi-zai-glm-setup|zai-glm-setup-vi]]
- [[102-i18n-vi-custom-providers|custom-providers]]
- [[118-i18n-vi-providers-reference|providers-reference]]
- [[114-i18n-vi-config-reference|config-reference]]

## Tham khảo

- [Z.AI Official Website](https://z.ai)
- [Z.AI API Documentation](https://z.ai/docs)
- [OpenAI API Compatibility](https://platform.openai.com/docs/api-reference)
- [ZeroClaw Provider Configuration](https://github.com/openagen/zeroclaw/blob/main/docs/providers/README.md)

#zeroclaw #z-ai #glm-models #api-configuration #ai-integration #cli-setup #llm-provider #openai-compatible
