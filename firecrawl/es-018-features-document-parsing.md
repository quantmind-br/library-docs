---
title: Análisis de documentos | Firecrawl
url: https://docs.firecrawl.dev/es/features/document-parsing
source: sitemap
fetched_at: 2026-03-23T07:25:52.776784-03:00
rendered_js: false
word_count: 367
summary: This document outlines Firecrawl's capabilities for parsing and extracting structured content from various file formats, including Excel, Word, and PDF, into clean Markdown.
tags:
    - document-parsing
    - firecrawl
    - data-extraction
    - file-conversion
    - markdown-output
    - ocr-processing
category: guide
---

Firecrawl ofrece potentes capacidades de análisis de documentos que te permiten extraer contenido estructurado de diversos formatos. Esta función es especialmente útil para procesar archivos como hojas de cálculo, documentos de Word y más.

## Formatos de documentos compatibles

Firecrawl actualmente admite los siguientes formatos de documentos:

- **Hojas de cálculo de Excel** (`.xlsx`, `.xls`)
  
  - Cada hoja de cálculo se convierte en una tabla HTML
  - Las hojas se separan con encabezados H2 con el nombre de la hoja
  - Conserva el formato de las celdas y los tipos de datos
- **Documentos de Word** (`.docx`, `.doc`, `.odt`, `.rtf`)
  
  - Extrae el contenido de texto preservando la estructura del documento
  - Mantiene encabezados, párrafos, listas y tablas
  - Conserva el formato y el estilo básicos
- **Documentos PDF** (`.pdf`)
  
  - Extrae el contenido de texto con información de diseño
  - Conserva la estructura del documento, incluidas secciones y párrafos
  - Procesa tanto PDFs basados en texto como escaneados (con OCR)
  - Admite la opción `mode` para controlar la estrategia de análisis: `fast` (solo texto), `auto` (texto con fallback a OCR, por defecto) o `ocr` (forzar OCR)
  - Precio de 1 crédito por página. Consulta la [tarifa](https://docs.firecrawl.dev/pricing) para más detalles.

### Modos de análisis de PDF

Usa la opción `parsers` para controlar cómo se procesan los PDF:

ModoDescripción`auto`Intenta primero una extracción rápida basada en texto y recurre a OCR si es necesario. Este es el valor predeterminado.`fast`Análisis solo basado en texto (texto incrustado). Es la opción más rápida, pero no extraerá texto de páginas escaneadas o con muchas imágenes.`ocr`Fuerza el análisis por OCR en cada página. Úsalo para documentos escaneados o cuando `auto` clasifique incorrectamente una página.

```
// Sintaxis de objeto con modo
parsers: [{ type: "pdf", mode: "ocr", maxPages: 20 }]

// Predeterminado (modo auto)
parsers: [{ type: "pdf" }]
```

## Cómo usar el análisis de documentos

El análisis de documentos en Firecrawl se ejecuta automáticamente cuando proporcionas una URL que apunte a un tipo de documento compatible. El sistema detectará el tipo de archivo según la extensión de la URL o el encabezado Content-Type y lo procesará en consecuencia.

### Ejemplo: Raspado de un archivo de Excel

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-TU-CLAVE-API" });

const doc = await firecrawl.scrape('https://example.com/data.xlsx');

console.log(doc.markdown);

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-TU-CLAVE-API" });

const doc = await firecrawl.scrape('https://example.com/data.docx');

console.log(doc.markdown);
```

## Formato de salida

Todos los tipos de documentos compatibles se convierten en Markdown limpio y estructurado. Por ejemplo, un archivo de Excel con varias hojas podría convertirse en:

```
## Hoja1

| Nombre | Valor |
|--------|-------|
| Elemento 1 | 100   |
| Elemento 2 | 200   |

## Hoja2

| Fecha      | Descripción  |
|------------|--------------|
| 2023-01-01 | Primer trimestre|
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automática.