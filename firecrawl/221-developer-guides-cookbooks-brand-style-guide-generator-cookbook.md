---
title: Building a Brand Style Guide Generator with Firecrawl - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/cookbooks/brand-style-guide-generator-cookbook
source: sitemap
fetched_at: 2026-03-23T07:39:55.698539-03:00
rendered_js: false
word_count: 450
summary: This document provides a technical guide for building a Node.js application that uses Firecrawl's branding format to extract design tokens from a website and automatically generate a professional PDF style guide.
tags:
    - web-scraping
    - design-systems
    - pdf-generation
    - brand-identity
    - typescript
    - automation
    - node-js
    - firecrawl
category: tutorial
---

Build a brand style guide generator that automatically extracts colors, typography, spacing, and visual identity from any website and compiles it into a professional PDF document. ![Brand style guide PDF generator using Firecrawl branding format to extract design system](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/brand-style-guide-pdf-generator-firecrawl.gif?s=2c8e0a9d223ea655238b17442c7bf41b)

## What You’ll Build

A Node.js application that takes any website URL, extracts its complete brand identity using Firecrawl’s branding format, and generates a polished PDF style guide with:

- Color palette with hex values
- Typography system (fonts, sizes, weights)
- Spacing and layout specifications
- Logo and brand imagery
- Theme information (light/dark mode)

![Example of generated brand style guide PDF with colors typography and spacing](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/generated-brand-style-guide-pdf-example.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=de8be5319be990d6630591afa3fc2dc2)

## Prerequisites

- Node.js 18 or later installed
- A Firecrawl API key from [firecrawl.dev](https://firecrawl.dev)
- Basic knowledge of TypeScript and Node.js

## How It Works

1. **URL Input**: The generator receives a target website URL
2. **Firecrawl Scrape**: Calls the `/scrape` endpoint with the `branding` format
3. **Brand Analysis**: Firecrawl analyzes the page’s CSS, fonts, and visual elements
4. **Data Return**: Returns a structured `BrandingProfile` object with all design tokens

### PDF Generation Process

1. **Header Creation**: Generates a colored header using the primary brand color
2. **Logo Fetch**: Downloads and embeds the logo or favicon if available
3. **Color Palette**: Renders each color as a visual swatch with metadata
4. **Typography Section**: Documents font families, sizes, and weights
5. **Spacing Info**: Includes base units, border radius, and theme mode

### Branding Profile Structure

The [branding format](https://docs.firecrawl.dev/features/scrape#%2Fscrape-with-branding-endpoint) returns detailed brand information:

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

## Key Features

The generator identifies and categorizes all brand colors:

- **Primary & Secondary**: Main brand colors
- **Accent**: Highlight and CTA colors
- **Background & Text**: UI foundation colors
- **Semantic Colors**: Success, warning, error states

### Typography Documentation

Captures the complete type system:

- **Font Families**: Primary, heading, and monospace fonts
- **Size Scale**: All heading and body text sizes
- **Font Weights**: Available weight variations

### Visual Output

The PDF includes:

- Color-coded header matching the brand
- Embedded logo when available
- Professional layout with clear hierarchy
- Metadata footer with generation date

![Side-by-side comparison of original website and generated brand style guide PDF](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/website-to-brand-style-guide-comparison.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=90153b3c2c920eceb8cd454eb266f9d0)

## Customization Ideas

### Add Component Documentation

Extend the generator to include UI component styles:

```
// Add after the Spacing & Theme section
if (b.components) {
  doc.addPage();
  doc.fontSize(20).fillColor("#333").text("UI Components", 50, 50);

  // Document button styles
  if (b.components.buttonPrimary) {
    const btn = b.components.buttonPrimary;
    doc.fontSize(14).text("Primary Button", 50, 90);
    doc.rect(50, 110, 120, 40).fill(btn.background);
    doc.fontSize(12).fillColor(btn.textColor).text("Button", 50, 120, { width: 120, align: "center" });
  }
}
```

### Export Multiple Formats

Add JSON export alongside the PDF:

```
// Add before doc.end()
fs.writeFileSync("brand-data.json", JSON.stringify(b, null, 2));
```

### Batch Processing

Generate guides for multiple websites:

```
const websites = [
  "https://stripe.com",
  "https://linear.app",
  "https://vercel.com"
];

for (const site of websites) {
  const { branding } = await fc.scrape(site, { formats: ["branding"] }) as any;
  // Generate PDF for each site...
}
```

### Custom PDF Themes

Create different PDF styles based on the extracted theme:

```
const isDarkMode = b.colorScheme === "dark";
const headerBg = isDarkMode ? b.colors?.background : b.colors?.primary;
const textColor = isDarkMode ? "#fff" : "#333";
```

## Best Practices

1. **Handle Missing Data**: Not all websites expose complete branding information. Always provide fallback values for missing properties.
2. **Respect Rate Limits**: When batch processing multiple sites, add delays between requests to respect Firecrawl’s rate limits.
3. **Cache Results**: Store extracted branding data to avoid repeated API calls for the same site.
4. **Image Format Handling**: Some logos may be in formats PDFKit doesn’t support (like SVG). Consider adding format conversion or graceful fallbacks.
5. **Error Handling**: Wrap the generation process in try-catch blocks and provide meaningful error messages.

* * *