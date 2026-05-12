---
title: Crear un generador de guías de estilo de marca con Firecrawl - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/cookbooks/brand-style-guide-generator-cookbook
source: sitemap
fetched_at: 2026-03-23T07:39:17.972765-03:00
rendered_js: false
word_count: 590
summary: This document provides a tutorial on building a Node.js application that extracts brand identity tokens—such as colors, typography, and spacing—from websites using the Firecrawl branding API and compiles them into a professional PDF style guide.
tags:
    - web-scraping
    - brand-identity
    - pdf-generation
    - firecrawl
    - design-tokens
    - automation
    - node-js
category: tutorial
---

Crea un generador de guías de estilo de marca que extrae automáticamente colores, tipografía, espaciado e identidad visual de cualquier sitio web y los compila en un documento PDF profesional. ![Generador de PDF de guía de estilo de marca usando el formato de branding de Firecrawl para extraer el sistema de diseño](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/brand-style-guide-pdf-generator-firecrawl.gif?s=2c8e0a9d223ea655238b17442c7bf41b)

## Qué vas a construir

Una aplicación de Node.js que toma la URL de cualquier sitio web, extrae toda su identidad de marca usando el formato de branding de Firecrawl y genera una guía de estilo en PDF profesional con:

- Paleta de colores con valores hex
- Sistema de tipografía (fuentes, tamaños, pesos)
- Especificaciones de espaciado y diseño
- Logotipo e imágenes de la marca
- Información del tema (modo claro/oscuro)

![Ejemplo de PDF de guía de estilo de marca generado con colores tipografía y espaciado](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/generated-brand-style-guide-pdf-example.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=de8be5319be990d6630591afa3fc2dc2)

## Requisitos previos

- Node.js 18 o superior instalado
- Una clave de API de Firecrawl de [firecrawl.dev](https://firecrawl.dev)
- Conocimientos básicos de TypeScript y Node.js

## Cómo funciona

1. **Entrada de URL**: El generador recibe la URL de un sitio web de destino
2. **Firecrawl Scrape**: Llama al endpoint `/scrape` con el formato `branding`
3. **Análisis de marca**: Firecrawl analiza el CSS, las fuentes y los elementos visuales de la página
4. **Retorno de datos**: Devuelve un objeto `BrandingProfile` estructurado con todos los tokens de diseño

### Proceso de generación de PDF

1. **Creación del encabezado**: Genera un encabezado de color usando el color principal de la marca
2. **Obtención del logotipo**: Descarga e inserta el logotipo o favicon si está disponible
3. **Paleta de colores**: Muestra cada color como una muestra visual con metadatos
4. **Sección de tipografía**: Documenta familias tipográficas, tamaños y grosores
5. **Información de espaciado**: Incluye unidades base, radio de los bordes y modo del tema

### Estructura del perfil de branding

El [formato de branding](https://docs.firecrawl.dev/features/scrape#%2Fscrape-with-branding-endpoint) devuelve información detallada de la marca:

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

## Características clave

El generador identifica y clasifica todos los colores de la marca:

- **Primarios y Secundarios**: Colores principales de la marca
- **Acento**: Colores de énfasis y de llamado a la acción (CTA)
- **Fondo y Texto**: Colores base de la interfaz
- **Colores Semánticos**: Estados de éxito, advertencia y error

### Documentación sobre tipografía

Recoge el sistema tipográfico completo:

- **Familias tipográficas**: Fuentes primarias, para encabezados y monoespaciadas
- **Escala de tamaños**: Todos los tamaños de texto de encabezado y cuerpo
- **Pesos tipográficos**: Variaciones de grosor disponibles

### Salida visual

El PDF incluye:

- Encabezado con colores de la marca
- Logotipo integrado cuando esté disponible
- Diseño profesional con jerarquía clara
- Pie de página con metadatos y fecha de generación

![Comparación en paralelo del sitio web original y el PDF de la guía de estilo de marca generado](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/website-to-brand-style-guide-comparison.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=90153b3c2c920eceb8cd454eb266f9d0)

## Ideas de personalización

### Agregar documentación de componentes

Extiende el generador para incluir estilos de componentes de interfaz de usuario:

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
    doc.fontSize(12).fillColor(btn.textColor).text("Botón", 50, 120, { width: 120, align: "center" });
  }
}
```

### Exportar en varios formatos

Añade exportación en JSON además del PDF:

```
// Agregar antes de doc.end()
fs.writeFileSync("brand-data.json", JSON.stringify(b, null, 2));
```

### Procesamiento por lotes

Genera guías para varios sitios web:

```
const websites = [
  "https://stripe.com",
  "https://linear.app",
  "https://vercel.com"
];

for (const site of websites) {
  const { branding } = await fc.scrape(site, { formats: ["branding"] }) as any;
  // Generar PDF para cada sitio...
}
```

### Temas personalizados de PDF

Crea diferentes estilos de PDF a partir del tema extraído:

```
const isDarkMode = b.colorScheme === "dark";
const headerBg = isDarkMode ? b.colors?.background : b.colors?.primary;
const textColor = isDarkMode ? "#fff" : "#333";
```

## Mejores prácticas

1. **Gestionar datos faltantes**: No todos los sitios web exponen información de marca completa. Proporciona siempre valores de reserva para las propiedades faltantes.
2. **Respetar los límites de tasa**: Al procesar por lotes varios sitios, añade pausas entre solicitudes para respetar los límites de tasa de Firecrawl.
3. **Almacenar resultados en caché**: Guarda los datos de marca extraídos para evitar llamadas repetidas a la API para el mismo sitio.
4. **Gestión del formato de imagen**: Algunos logotipos pueden estar en formatos que PDFKit no admite (como SVG). Considera añadir conversión de formato o alternativas de reserva adecuadas.
5. **Gestión de errores**: Envuelve el proceso de generación en bloques try-catch y proporciona mensajes de error descriptivos.

* * *