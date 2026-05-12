---
title: Zai glm setup
authors:
  - ZeroClaw Team
tags:
  - zeroclaw
  - z-ai
  - glm
  - configuration
  - api-integration
  - cli-setup
  - llm-provider
  - openai-compatible
category: configuration
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 1216
---
# Hướng dẫn Thiết lập Z.AI GLM cho ZeroClaw

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
> Để cấu hình base URL tùy chỉnh, xem [[098-setup-guides-zai-glm-setup|zai-glm-setup]] hoặc [[151-contributing-custom-providers|custom-providers]].

## Các Model Hiện Có

| Model ID | Mô tả | Trường hợp sử dụng | Mặc định |
|----------|-------|-------------------|----------|
| `glm-5` | Mạnh nhất về khả năng suy luận | Tác vụ phức tạp, sản xuất | ✅ |
| `glm-4.7` | Chất lượng đa năng cao | Hiệu suất cân bằng | ❌ |
| `glm-4.6` | Model cơ bản cân bằng | Tiết kiệm chi phí | ❌ |
| `glm-4.5-air` | Tùy chọn độ trễ thấp | Phản hồi nhanh | ❌ |

> [!important]
> Tính khả dụng của model phụ thuộc vào tài khoản và khu vực. Sử dụng API `/models` để kiểm tra các model có sẵn trong tài khoản của bạn.

## Cấu hình

### Phương pháp 1: Onboarding Nhanh (Khuyến nghị)

```bash
# Endpoint toàn cầu (khuyến nghị cho hầu hết người dùng)
zeroclaw onboard \
  --provider "zai" \
  --api-key "YOUR_ZAI_API_KEY"

# Endpoint Trung Quốc (cho người dùng tại Trung Quốc)
zeroclaw onboard \
  --provider "zai-cn" \
  --api-key "YOUR_ZAI_API_KEY"
```

### Phương pháp 2: Cấu hình Thủ công

Chỉnh sửa file `~/.zeroclaw/config.toml`:

```toml
# Cấu hình provider
[providers.zai]
enabled = true
api_key = "YOUR_ZAI_API_KEY"
default_model = "glm-5"
default_temperature = 0.7
base_url = "https://api.z.ai/api/coding/paas/v4"

# Cấu hình agent mặc định
[agents.default]
provider = "zai"
model = "glm-5"

# Đặt provider mặc định
[providers.default]
provider = "zai"
```

### Phương pháp 3: Biến Môi trường

Thêm vào file `.env` của bạn:

```bash
# Khóa API Z.AI chính (khuyến nghị)
ZAI_API_KEY=your-id.secret

# Khóa chung (dùng bởi nhiều provider)
API_KEY=your-id.secret
```

> [!info]
> Định dạng khóa: `id.secret` (ví dụ: `abc123.xyz789`)

## Xác minh Cấu hình

### Kiểm tra với curl

Xác minh khóa API và endpoint:

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

**Phản hồi thành công mong đợi:**

```json
{
  "object": "chat.completion",
  "model": "glm-5",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 12,
    "total_tokens": 22
  }
}
```

### Kiểm tra với CLI ZeroClaw

```bash
# Kiểm tra agent trực tiếp
echo "Xin chào từ ZeroClaw!" | zeroclaw agent

# Kiểm tra trạng thái provider
zeroclaw providers list
zeroclaw providers status zai

# Kiểm tra model cụ thể
zeroclaw chat --model glm-5 --message "Ngôn ngữ lập trình Rust là gì?"

# Kiểm tra cấu hình
zeroclaw config show
```

## Cấu hình Nâng cao

### Nhiều Providers

Cấu hình cả endpoint toàn cầu và Trung Quốc:

```toml
[providers.zai]
enabled = true
api_key = "${ZAI_API_KEY}"
default_model = "glm-5"
base_url = "https://api.z.ai/api/coding/paas/v4"

[providers.zai-cn]
enabled = true
api_key = "${ZAI_CN_API_KEY}"
default_model = "glm-4.7"
base_url = "https://open.bigmodel.cn/api/paas/v4"

# Sử dụng các model khác nhau cho các agents khác nhau
[agents.default]
provider = "zai"
model = "glm-5"

[agents.china]
provider = "zai-cn"
model = "glm-4.7"
```

### Cài đặt Cụ thể Provider

```toml
[providers.zai]
api_key = "YOUR_API_KEY"
base_url = "https://api.z.ai/api/coding/paas/v4"
default_model = "glm-5"

# Tham số model
max_tokens = 4096
temperature = 0.7
top_p = 0.9
frequency_penalty = 0.1
presence_penalty = 0.1

# Cấu hình retry
max_retries = 3
retry_delay_ms = 1000

# Cài đặt timeout
request_timeout_sec = 30
connect_timeout_sec = 10
```

## Xử lý Sự cố

### Lỗi Rate Limiting

**Triệu chứng:**
- Lỗi `rate_limited` trong logs
- Phản hồi chậm
- Yêu cầu bị từ chối với mã 429

**Giải pháp:**
1. Chờ và thử lại
2. Kiểm tra gói Z.AI
3. Sử dụng model độ trễ thấp
4. Giảm tần suất yêu cầu
5. Triển khai backoff theo cấp số nhân

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
- "Invalid API key" trong thông báo

**Giải pháp:**
1. Xác minh định dạng khóa API
2. Kiểm tra khoảng trắng
3. Kiểm tra khóa hết hạn
4. Kiểm tra quyền khóa
5. Kiểm tra xác thực trực tiếp:

```bash
curl -I "https://api.z.ai/api/coding/paas/v4/models" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY"
```

### Lỗi Model Không Tìm Thấy

**Triệu chứng:**
- "Model not found" errors
- Model không khả dụng trong tài khoản

**Giải pháp:**
1. Liệt kê model có sẵn:

```bash
curl -s "https://api.z.ai/api/coding/paas/v4/models" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY" | jq '.data[].id'
```

2. Kiểm tra gói đăng ký
3. Sử dụng model dự phòng
4. Xác minh khu vực

### Vấn đề Kết nối

**Triệu chứng:**
- Timeouts kết nối
- Lỗi phân giải DNS
- Lỗi SSL
- Không thể kết nối tới endpoints Z.AI

**Giải pháp:**
1. Kiểm tra kết nối mạng
2. Xác minh chứng chỉ SSL
3. Kiểm tra tường lửa/proxy
4. Thử endpoint khác
5. Kiểm tra phân giải DNS

## Lấy API Key

### Hướng dẫn Từng Bước

1. Truy cập Z.AI:
   [https://z.ai](https://z.ai)

2. Đăng ký gói Coding:
   - Chọn "Coding Plan"
   - Hoàn tất đăng ký

3. Truy cập Bảng điều khiển API:
   - Đăng nhập
   - Điều hướng tới "API Keys"
   - Nhấp "Create API Key"

4. Sao chép khóa API:
   - Định dạng: `id.secret`
   - Lưu trữ an toàn
   - Không commit vào version control

5. Cấu hình ZeroClaw:

```bash
zeroclaw onboard --provider zai --api-key YOUR_API_KEY
```

## Các Mẹo Tốt Nhất

### Bảo mật
- Sử dụng biến môi trường cho khóa API
- Xoay khóa định kỳ (90 ngày)
- Sử dụng khóa khác nhau cho môi trường dev/staging/prod
- Hạn chế quyền khóa trên dashboard Z.AI
- Giám sát sử dụng khóa

### Hiệu suất
- Chọn model phù hợp:
  - `glm-5`: Tác vụ suy luận phức tạp
  - `glm-4.7`: Hiệu suất cân bằng
  - `glm-4.6`: Tiết kiệm chi phí
  - `glm-4.5-air`: Độ trễ thấp

- Cài đặt temperature:
  - `0.0-0.3`: Đầu ra xác định
  - `0.3-0.7`: Cân bằng
  - `0.7-1.0`: Sáng tạo

- Sử dụng max_tokens để giới hạn độ dài phản hồi

### Tối ưu Chi phí
- Cache responses cho truy vấn lặp lại
- Gom cụm yêu cầu
- Giám sát sử dụng qua dashboard Z.AI
- Thiết lập cảnh báo thanh toán
- Sử dụng model chi phí thấp cho tác vụ đơn giản

## So sánh Model

| Model | Suy luận | Sáng tạo | Chi phí | Độ trễ | Tốt nhất cho |
|-------|----------|----------|---------|---------|--------------|
| `glm-5` | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Cao | Trung bình | Sản xuất, tác vụ phức tạp |
| `glm-4.7` | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Trung bình | Trung bình | Mục đích chung |
| `glm-4.6` | ⭐⭐⭐ | ⭐⭐⭐ | Thấp | Thấp | Tác vụ đơn giản, tiết kiệm chi phí |
| `glm-4.5-air` | ⭐⭐ | ⭐⭐ | Thấp | Rất thấp | Phản hồi nhanh, khối lượng cao |

## Tài liệu Liên quan

- [[096-i18n-vi-zai-glm-setup|zai-glm-setup-vi]]
- [[098-setup-guides-zai-glm-setup|zai-glm-setup-en]]
- [[151-contributing-custom-providers|custom-providers]]
- [[118-i18n-vi-providers-reference|providers-reference]]
- [[114-i18n-vi-config-reference|config-reference]]
- [[002-setup-guides-readme|setup-guides-readme]]

## Tham khảo

- [Z.AI Official Website](https://z.ai)
- [Z.AI API Documentation](https://z.ai/docs)
- [Tương thích API OpenAI](https://platform.openai.com/docs/api-reference)
- [Hệ thống Provider ZeroClaw](https://github.com/openagen/zeroclaw/blob/main/docs/providers/README.md)
- [Tài liệu Model GLM](https://github.com/THUDM/GLM)

#zeroclaw #z-ai #glm #configuration #api-integration #cli-setup #llm-provider #openai-compatible