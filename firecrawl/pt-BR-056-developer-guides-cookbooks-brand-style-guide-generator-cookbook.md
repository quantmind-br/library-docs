---
title: Criando um Gerador de Guia de Estilo de Marca com Firecrawl - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/cookbooks/brand-style-guide-generator-cookbook
source: sitemap
fetched_at: 2026-03-23T07:37:46.743021-03:00
rendered_js: false
word_count: 573
summary: This guide demonstrates how to build a Node.js application that uses the Firecrawl branding endpoint to automatically extract visual design tokens from a website and compile them into a professional PDF style guide.
tags:
    - web-scraping
    - design-tokens
    - pdf-generation
    - firecrawl
    - branding-extraction
    - typescript
    - nodejs
category: tutorial
---

Crie um gerador de guia de estilo de marca que extrai automaticamente cores, tipografia, espaçamentos e identidade visual de qualquer site e compila tudo em um documento PDF profissional. ![Gerador de PDF de guia de estilo de marca usando o formato de branding do Firecrawl para extrair o sistema de design](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/brand-style-guide-pdf-generator-firecrawl.gif?s=2c8e0a9d223ea655238b17442c7bf41b)

## O que você vai construir

Uma aplicação Node.js que recebe a URL de qualquer site, extrai toda a identidade de marca usando o formato de branding do Firecrawl e gera um PDF de guia de estilo de marca profissional com:

- Paleta de cores com valores hex
- Sistema de tipografia (fontes, tamanhos, pesos)
- Especificações de espaçamento e layout
- Logo e imagens de marca
- Informações de tema (modo claro/escuro)

![Exemplo de PDF de guia de estilo de marca gerado com cores, tipografia e espaçamento](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/generated-brand-style-guide-pdf-example.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=de8be5319be990d6630591afa3fc2dc2)

## Pré-requisitos

- Node.js 18 ou superior instalado
- Uma chave de API do Firecrawl obtida em [firecrawl.dev](https://firecrawl.dev)
- Conhecimentos básicos de TypeScript e Node.js

## Como funciona

1. **Entrada de URL**: O gerador recebe a URL do site de destino
2. **Firecrawl Scrape**: Chama o endpoint `/scrape` com o formato `branding`
3. **Análise de marca**: O Firecrawl analisa o CSS, as fontes e os elementos visuais da página
4. **Retorno de dados**: Retorna um objeto `BrandingProfile` estruturado com todos os design tokens

### Processo de Geração de PDF

1. **Criação do Cabeçalho**: Gera um cabeçalho colorido usando a cor principal da marca
2. **Obtensão do Logotipo**: Faz o download e incorpora o logotipo ou favicon, se disponível
3. **Paleta de Cores**: Renderiza cada cor como uma amostra visual com metadados
4. **Seção de Tipografia**: Documenta famílias de fontes, tamanhos e pesos
5. **Informações de Espaçamento**: Inclui unidades base, raio de borda e modo do tema

### Estrutura do Perfil de Branding

O [formato de branding](https://docs.firecrawl.dev/features/scrape#%2Fscrape-with-branding-endpoint) retorna informações detalhadas sobre a marca:

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

## Principais funcionalidades

O gerador identifica e categoriza todas as cores da marca:

- **Primárias e secundárias**: Cores principais da marca
- **Destaque (accent)**: Cores de destaque e de chamada para ação (CTA)
- **Fundo e texto**: Cores base da interface
- **Cores semânticas**: Estados de sucesso, aviso e erro

### Documentação de Tipografia

Abrange todo o sistema tipográfico:

- **Famílias tipográficas**: fontes primárias, de títulos e monoespaçadas
- **Escala de tamanhos**: todos os tamanhos de texto de títulos e corpo
- **Pesos tipográficos**: variações de peso disponíveis

### Resultado visual

O PDF inclui:

- Cabeçalho colorido que corresponde à marca
- Logotipo inserido quando disponível
- Layout profissional com hierarquia clara
- Rodapé com metadados e data de geração

![Comparação lado a lado entre o site original e o PDF gerado do guia de estilo da marca](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/website-to-brand-style-guide-comparison.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=90153b3c2c920eceb8cd454eb266f9d0)

## Ideias de customização

### Adicionar documentação de componentes

Estenda o gerador para incluir estilos dos componentes de UI:

```
// Adicionar após a seção Spacing & Theme
if (b.components) {
  doc.addPage();
  doc.fontSize(20).fillColor("#333").text("UI Components", 50, 50);

  // Documentar estilos de botão
  if (b.components.buttonPrimary) {
    const btn = b.components.buttonPrimary;
    doc.fontSize(14).text("Primary Button", 50, 90);
    doc.rect(50, 110, 120, 40).fill(btn.background);
    doc.fontSize(12).fillColor(btn.textColor).text("Button", 50, 120, { width: 120, align: "center" });
  }
}
```

### Exportar em vários formatos

Adicione exportação em JSON além do PDF:

```
// Adicionar antes de doc.end()
fs.writeFileSync("brand-data.json", JSON.stringify(b, null, 2));
```

### Processamento em lote

Crie guias para vários sites:

```
const websites = [
  "https://stripe.com",
  "https://linear.app",
  "https://vercel.com"
];

for (const site of websites) {
  const { branding } = await fc.scrape(site, { formats: ["branding"] }) as any;
  // Gere PDF para cada site...
}
```

### Temas de PDF personalizados

Crie diferentes estilos de PDF a partir do tema extraído:

```
const isDarkMode = b.colorScheme === "dark";
const headerBg = isDarkMode ? b.colors?.background : b.colors?.primary;
const textColor = isDarkMode ? "#fff" : "#333";
```

## Boas práticas

1. **Trate dados ausentes**: Nem todos os sites expõem informações completas de branding. Sempre forneça valores padrão para propriedades ausentes.
2. **Respeite os rate limits**: Ao processar vários sites em lote, adicione intervalos entre as requisições para respeitar os rate limits do Firecrawl.
3. **Armazene em cache os resultados**: Guarde os dados de branding extraídos para evitar chamadas repetidas à API para o mesmo site.
4. **Tratamento de formatos de imagem**: Alguns logos podem estar em formatos que o PDFKit não suporta (como SVG). Considere adicionar conversão de formato ou alternativas adequadas.
5. **Tratamento de erros**: Envolva o processo de geração em blocos try-catch e forneça mensagens de erro claras e informativas.

* * *