---
title: JSON 模式 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/llm-extract
source: sitemap
fetched_at: 2026-03-23T07:20:37.066336-03:00
rendered_js: false
word_count: 168
summary: This document explains how to extract structured data from web pages using Firecrawl's /scrape endpoint, detailing the use of JSON schemas, prompts, and best practices for consistent LLM-based output.
tags:
    - web-scraping
    - data-extraction
    - json-schema
    - firecrawl
    - api-integration
    - llm-structured-output
category: guide
---

Firecrawl 借助 AI 通过 3 个步骤从网页获取结构化数据：

1. **设置 Schema（可选）：** 定义一个 JSON Schema（采用 OpenAI 的格式）来明确所需数据；如果不需要严格的 Schema，也可仅提供一个 `prompt`，并附上网页 URL。
2. **发起请求：** 使用 JSON 模式将你的 URL 和 Schema 发送到我们的 /scrape 端点。查看方法： [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
3. **获取数据：** 返回与你的 Schema 匹配的干净、结构化数据，可直接使用。

这使你能快速、轻松地按所需 formats 获取网页数据。

### 通过 /scrape 的 JSON 模式

用于从抓取的页面中提取结构化数据。

输出：

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI 赋能的网页抓取与数据抽取",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI 赋能的网页抓取与数据抽取",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI 赋能的网页抓取与数据抽取",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### 无需 schema 的结构化数据

你也可以只向端点传入一个 `prompt`，在没有 schema 的情况下进行提取。LLM 会自行确定数据结构。

输出：

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI 驱动的网页抓取与数据抽取",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI 驱动的网页抓取与数据抽取",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI 驱动的网页抓取与数据抽取",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

下面是一个从网站提取结构化公司信息的完整示例：

输出：

```
{
  "success": true,
  "data": {
    "json": {
      "company_mission": "将网站转换为 LLM 可用数据",
      "supports_sso": true,
      "is_open_source": true,
      "is_in_yc": true
    }
  }
}
```

### JSON 格式选项

在 v2 中使用 JSON 模式时，需要在 `formats` 中直接包含一个内嵌 schema 的对象： `formats: [{ type: 'json', schema: { ... }, prompt: '...' }]` 参数：

- `schema`: 描述所需结构化输出的 JSON Schema（基于 schema 的提取为必填）。
- `prompt`: 可选提示，用于引导提取（也用于无 schema 的提取）。

**重要说明：** 与 v1 不同，v2 中没有单独的 `jsonOptions` 参数。schema 必须直接包含在 `formats` 数组中的 format 对象内。

如果你在使用 JSON 抽取时遇到结果不一致或不完整的情况，可以参考以下做法：

- **让提示词简短且聚焦。** 带有大量规则的长提示会增加结果的不确定性。将具体约束 (如允许值) 移入 schema 本身。
- **使用简洁的属性名。** 避免在属性名中嵌入说明或枚举列表。用类似 `"installation_type"` 这样的简短键名，并把允许值放在 `enum` 数组中。
- **为受限字段添加 `enum` 数组。** 当某个字段只有固定取值时，将它们列在 `enum` 中，并确保与页面上显示的文本完全匹配。
- **在字段描述中包含 null 处理逻辑。** 在每个字段的 `description` 中添加 `"Return null if not found on the page."`，以避免模型猜测缺失值。
- **添加位置信息提示。** 告诉模型在页面上哪里查找数据，例如 `"Flow rate in GPM from the Specifications table."`。
- **将大型 schema 拆分成多个请求。** 字段很多 (例如 30+) 的 schema 通常会产生更不稳定的结果。将其拆成 2–3 个请求，每个请求包含 10–15 个字段。

**结构良好的 schema 示例：**

```
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": ["string", "null"],
      "description": "Full descriptive product name as shown on the page. Return null if not found."
    },
    "installation_type": {
      "type": ["string", "null"],
      "description": "Installation type from the Specifications section. Return null if not found.",
      "enum": ["Deck-mount", "Wall-mount", "Countertop", "Drop-in", "Undermount"]
    },
    "flow_rate_gpm": {
      "type": ["string", "null"],
      "description": "Flow rate in GPM from the Specifications section. Return null if not found."
    }
  }
}
```

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。