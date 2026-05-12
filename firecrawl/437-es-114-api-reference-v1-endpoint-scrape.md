---
title: Scrapear - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/scrape
source: sitemap
fetched_at: 2026-03-23T07:16:28.641986-03:00
rendered_js: false
word_count: 696
summary: This document describes the parameters and configuration options for the Firecrawl scrape API endpoint, which allows users to extract content from URLs with customizable settings for headers, proxies, and processing actions.
tags:
    - web-scraping
    - api-reference
    - data-extraction
    - proxy-settings
    - http-requests
    - automation
category: api
---

[Saltar al contenido principal](#content-area)

Realiza scraping de una única URL y, opcionalmente, extrae información usando un LLM

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/scrape) con funciones y rendimiento mejorados.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Cuerpo

La URL que se va a rastrear

onlyMainContent

boolean

predeterminado:true

Devuelve únicamente el contenido principal de la página, excluyendo encabezados, elementos de navegación, pies de página, etc.

Etiquetas que se deben incluir en la salida.

Etiquetas que se excluirán de la salida.

Devuelve una versión en caché de la página si su antigüedad es menor que este valor, en milisegundos. Si la versión en caché de la página es más antigua que este valor, la página se volverá a scrapear. Si no necesitas datos extremadamente recientes, activar esta opción puede acelerar tus procesos de scraping hasta un 500 %. El valor predeterminado es 0, lo que desactiva la caché.

Cabeceras que se enviarán con la solicitud. Pueden usarse para enviar cookies, user-agent, etc.

Especifica un retraso, en milisegundos, antes de obtener el contenido, permitiendo que la página tenga tiempo suficiente para cargarse.

mobile

boolean

predeterminado:false

Configúralo en `true` si quieres emular el scraping desde un dispositivo móvil. Es útil para probar páginas responsive y tomar capturas de pantalla en dispositivos móviles.

skipTlsVerification

boolean

predeterminado:false

Omitir la verificación del certificado TLS al realizar solicitudes

timeout

integer

predeterminado:30000

Tiempo de espera de la solicitud en milisegundos

parsePDF

boolean

predeterminado:true

Controla cómo se procesan los archivos PDF durante el scraping. Cuando es true, el contenido del PDF se extrae y se convierte al formato Markdown, y la facturación se basa en el número de páginas (1 crédito por página). Cuando es false, el archivo PDF se devuelve codificado en base64 con una tarifa plana total de 1 crédito.

actions

(Wait · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Acciones que se ejecutarán en la página antes de extraer el contenido

- Wait
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Configuración de ubicación de la solicitud. Cuando se especifique, usará un proxy adecuado si está disponible y emulará la configuración de idioma y zona horaria correspondientes. Si no se especifica, el valor predeterminado es 'US'.

removeBase64Images

boolean

predeterminado:true

Elimina todas las imágenes en formato base64 de la salida, que pueden hacerla excesivamente larga. El texto alternativo de la imagen se conserva en la salida, pero la URL se reemplaza por un marcador de posición.

blockAds

boolean

predeterminado:true

Habilita el bloqueo de anuncios y ventanas emergentes de cookies.

Especifica el tipo de proxy que se va a utilizar.

- basic: Proxies para hacer scraping de sitios con sistemas anti‑bots nulos o básicos. Es rápido y suele funcionar.
- enhanced: Proxies mejorados para hacer scraping de sitios con sistemas anti‑bots avanzados. Es más lento, pero más fiable en ciertos sitios. Cuesta hasta 5 créditos por solicitud.
- auto: Firecrawl reintentará automáticamente el scraping con proxies mejorados si el proxy básico falla. Si el reintento con enhanced tiene éxito, se cobrarán 5 créditos por la extracción. Si el primer intento con basic tiene éxito, solo se cobrará el coste estándar.

Si no especificas un proxy, Firecrawl usará basic por defecto.

Opciones disponibles:

`basic`,

`enhanced`,

`auto`

storeInCache

boolean

predeterminado:true

Si es true, la página se almacenará en el índice y la caché de Firecrawl. Establecerlo en false es útil si tu actividad de scraping puede implicar problemas de protección de datos. El uso de algunos parámetros asociados con scraping sensible (acciones, headers) hará que este parámetro tenga que ser false.

Formatos que se incluirán en el resultado.

Opciones disponibles:

`markdown`,

`html`,

`rawHtml`,

`links`,

`screenshot`,

`screenshot@fullPage`,

`json`,

`changeTracking`

Opciones de seguimiento de cambios (Beta). Solo aplicable cuando 'changeTracking' está incluido en los formatos. El formato 'markdown' también debe especificarse al usar el seguimiento de cambios.

zeroDataRetention

boolean

predeterminado:false

Si se establece en true, se habilitará la no conservación de datos para esta extracción. Para activar esta función, ponte en contacto con [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Respuesta