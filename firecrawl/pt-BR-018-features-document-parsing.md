---
title: Processamento de Documentos | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/document-parsing
source: sitemap
fetched_at: 2026-03-23T07:21:44.995538-03:00
rendered_js: false
word_count: 361
summary: Este documento detalha as capacidades do Firecrawl para a extração e conversão automatizada de diversos formatos de arquivos em Markdown estruturado.
tags:
    - firecrawl
    - data-extraction
    - document-parsing
    - pdf-processing
    - markdown-conversion
    - web-scraping
category: guide
---

O Firecrawl oferece recursos poderosos de parsing de documentos, permitindo extrair conteúdo estruturado de diversos formatos. Esse recurso é particularmente útil para processar arquivos como planilhas, documentos do Word e muito mais.

## Formatos de documentos suportados

Atualmente, o Firecrawl oferece suporte aos seguintes formatos de documentos:

- **Planilhas do Excel** (`.xlsx`, `.xls`)
  
  - Cada planilha é convertida em uma tabela HTML
  - As planilhas são separadas por títulos H2 com o nome da aba
  - Preserva a formatação das células e os tipos de dados
- **Documentos do Word** (`.docx`, `.doc`, `.odt`, `.rtf`)
  
  - Extrai o conteúdo de texto preservando a estrutura do documento
  - Mantém títulos, parágrafos, listas e tabelas
  - Preserva formatação e estilos básicos
- **Documentos PDF** (`.pdf`)
  
  - Extrai o conteúdo de texto com informações de layout
  - Preserva a estrutura do documento, incluindo seções e parágrafos
  - Lida com PDFs baseados em texto e digitalizados (com suporte a OCR)
  - Oferece a opção `mode` para controlar a estratégia de parsing: `fast` (apenas texto), `auto` (texto com fallback de OCR, padrão) ou `ocr` (forçar OCR)
  - Custa 1 crédito por página. Consulte a [tabela de preços](https://docs.firecrawl.dev/pricing) para detalhes.

### Modos de processamento de PDF

Use a opção `parsers` para controlar como os PDFs são processados:

ModoDescrição`auto`Tenta primeiro uma extração rápida baseada em texto e, se necessário, recorre ao OCR. Este é o modo padrão.`fast`Processamento apenas baseado em texto (texto embutido). É a opção mais rápida, mas não extrai texto de páginas digitalizadas ou com muitas imagens.`ocr`Força o uso de OCR em todas as páginas. Use para documentos digitalizados ou quando `auto` classificar uma página incorretamente.

```
// Sintaxe de objeto com modo
parsers: [{ type: "pdf", mode: "ocr", maxPages: 20 }]

// Padrão (modo automático)
parsers: [{ type: "pdf" }]
```

## Como usar a análise de documentos

A análise de documentos no Firecrawl é automática quando você fornece uma URL que aponta para um tipo de documento compatível. O sistema detecta o tipo de arquivo com base na extensão da URL ou no cabeçalho Content-Type e o processa conforme necessário.

### Exemplo: Fazendo scraping de um arquivo Excel

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-SUA-CHAVE-API" });

const doc = await firecrawl.scrape('https://example.com/data.xlsx');

console.log(doc.markdown);

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-SUA-CHAVE-API" });

const doc = await firecrawl.scrape('https://example.com/data.docx');

console.log(doc.markdown);
```

## Formato de saída

Todos os tipos de documentos compatíveis são convertidos em Markdown limpo e estruturado. Por exemplo, um arquivo Excel com várias planilhas pode ser convertido em:

```
## Planilha1

| Nome  | Valor |
|-------|-------|
| Item 1 | 100   |
| Item 2 | 200   |

## Planilha2

| Data       | Descrição    |
|------------|--------------|
| 2023-01-01 | Primeiro trimestre|
```

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções automatizadas de onboarding.