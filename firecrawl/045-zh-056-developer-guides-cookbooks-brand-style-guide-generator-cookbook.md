---
title: 使用 Firecrawl 构建品牌风格指南生成器 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/cookbooks/brand-style-guide-generator-cookbook
source: sitemap
fetched_at: 2026-03-23T07:37:12.595291-03:00
rendered_js: false
word_count: 151
summary: This tutorial demonstrates how to build a Node.js application that uses Firecrawl's branding API to extract design tokens from a website and generate a professional PDF style guide.
tags:
    - web-scraping
    - node-js
    - pdf-generation
    - brand-identity
    - design-systems
    - typescript
    - firecrawl
category: tutorial
---

构建一个品牌风格指南生成器，能够自动从任意网站中提取配色、字体排版、间距和品牌视觉形象，并将其整理成一份专业的 PDF 文档。 ![使用 Firecrawl branding 格式提取设计系统的品牌风格指南 PDF 生成器](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/brand-style-guide-pdf-generator-firecrawl.gif?s=2c8e0a9d223ea655238b17442c7bf41b)

## 你将构建的内容

一个 Node.js 应用，它接受任意网站 URL，使用 Firecrawl 的 Branding 格式提取其完整品牌识别信息，并生成一份精美的 PDF 品牌样式指南，内容包括：

- 含十六进制值的配色方案
- 字体系统（字体、字号、字重）
- 间距与布局规范
- Logo 与品牌图像
- 主题信息（浅色/深色模式）

![生成的品牌样式指南 PDF 示例，包含颜色、字体和间距](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/generated-brand-style-guide-pdf-example.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=de8be5319be990d6630591afa3fc2dc2)

## 前提条件

- 已安装 Node.js 18 或更高版本
- 拥有来自 [firecrawl.dev](https://firecrawl.dev) 的 Firecrawl API 密钥
- 具备 TypeScript 和 Node.js 的基础知识

## 工作原理

1. **URL 输入**：生成器接收目标网站的 URL
2. **Firecrawl 抓取**：调用 `/scrape` 端点，并使用 `branding` 格式
3. **品牌分析**：Firecrawl 分析页面的 CSS、字体和视觉元素
4. **返回数据**：返回一个结构化的 `BrandingProfile` 对象，其中包含所有设计 tokens

### PDF 生成流程

1. **页眉生成**：使用主品牌色生成彩色页眉区域
2. **Logo 获取**：下载并嵌入 logo 或网站图标（favicon，若有）
3. **配色方案**：将每种颜色渲染为带元数据的色块
4. **排版信息**：记录字体系列、字号和字重
5. **间距信息**：包含基础间距单位、圆角半径和主题模式

### 品牌配置结构

[品牌配置格式](https://docs.firecrawl.dev/features/scrape#%2Fscrape-with-branding-endpoint) 会返回详细的品牌信息：

```
{
  colorScheme: "dark" | "light",
  logo: "https://example.com/logo.svg",
  colors: {
    primary: "#FF6B35",
    secondary: "#004E89",
    accent: "#F77F00",
    background: "#1A1A1A",
    textPrimary: "#FFFFFF",
    textSecondary: "#B0B0B0"
  },
  typography: {
    fontFamilies: { primary: "Inter", heading: "Inter", code: "Roboto Mono" },
    fontSizes: { h1: "48px", h2: "36px", body: "16px" },
    fontWeights: { regular: 400, medium: 500, bold: 700 }
  },
  spacing: {
    baseUnit: 8,
    borderRadius: "8px"
  },
  images: {
    logo: "https://example.com/logo.svg",
    favicon: "https://example.com/favicon.ico"
  }
}
```

## 核心功能

生成器会识别并归类所有品牌色：

- **Primary & Secondary**: 品牌主色与辅助色
- **Accent**: 强调色和 CTA 颜色
- **Background & Text**: 作为 UI 基础的背景色与文本色
- **Semantic Colors**: 表示成功、警告和错误状态的语义色

### 排版规范文档

涵盖完整的文字排版系统：

- **Font Families**：主字体、标题字体和等宽字体
- **Size Scale**：所有标题和正文字号
- **Font Weights**：所有可用字重

### 视觉输出

该 PDF 包含：

- 与品牌配色相匹配的彩色页眉
- 在可用时嵌入品牌 Logo
- 具有清晰层级结构的专业版式
- 带有生成日期元数据的页脚

![原始网站与生成的品牌风格指南 PDF 的并排对比](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/website-to-brand-style-guide-comparison.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=90153b3c2c920eceb8cd454eb266f9d0)

## 自定义方案示例

### 添加组件文档

扩展生成器，使其包含 UI 组件样式：

```
// 在间距与主题部分之后添加
if (b.components) {
  doc.addPage();
  doc.fontSize(20).fillColor("#333").text("UI Components", 50, 50);

  // 文档化按钮样式
  if (b.components.buttonPrimary) {
    const btn = b.components.buttonPrimary;
    doc.fontSize(14).text("Primary Button", 50, 90);
    doc.rect(50, 110, 120, 40).fill(btn.background);
    doc.fontSize(12).fillColor(btn.textColor).text("Button", 50, 120, { width: 120, align: "center" });
  }
}
```

### 导出多种 formats

在现有 PDF 导出的基础上增加 JSON 导出：

```
// 在 doc.end() 前添加
fs.writeFileSync("brand-data.json", JSON.stringify(b, null, 2));
```

### 批量处理

为多个网站批量生成指南：

```
const websites = [
  "https://stripe.com",
  "https://linear.app",
  "https://vercel.com"
];

for (const site of websites) {
  const { branding } = await fc.scrape(site, { formats: ["branding"] }) as any;
  // 为每个网站生成 PDF...
}
```

### 自定义 PDF 主题

根据提取的主题创建不同的 PDF 样式：

```
const isDarkMode = b.colorScheme === "dark";
const headerBg = isDarkMode ? b.colors?.background : b.colors?.primary;
const textColor = isDarkMode ? "#fff" : "#333";
```

## 最佳实践

1. **处理缺失数据**：并非所有网站都会暴露完整的品牌信息。务必为缺失的属性提供后备值（默认值）。
2. **遵守速率限制**：在批量处理多个站点时，在请求之间添加延迟，以遵守 Firecrawl 的速率限制。
3. **缓存结果**：将提取到的品牌数据进行缓存，避免针对同一站点重复调用 API。
4. **处理图片格式**：某些 Logo 可能采用 PDFKit 不支持的格式（例如 SVG）。考虑添加格式转换或设计优雅的降级方案。
5. **错误处理**：将生成流程包裹在 try-catch 块中，并提供有意义的错误信息。

* * *