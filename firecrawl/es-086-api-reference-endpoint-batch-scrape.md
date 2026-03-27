---
title: Raspado en lote - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:18:14.097692-03:00
rendered_js: false
word_count: 1031
summary: This document provides a comprehensive technical reference for the batch scraping API, detailing the configuration parameters, request structure, and available output formats for web data extraction.
tags:
    - web-scraping
    - api-documentation
    - batch-processing
    - data-extraction
    - firecrawl
category: reference
---

[Saltar al contenido principal](#content-area)

Scrapear varias URL y, opcionalmente, extraer información mediante un LLM

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Cuerpo

La URL que se va a extraer

Un objeto de especificación de un webhook.

Número máximo de scrapes simultáneos. Este parámetro te permite establecer un límite de concurrencia para este scrape por lotes. Si no se especifica, el scrape por lotes usa el límite de concurrencia definido para tu equipo.

ignoreInvalidURLs

boolean

predeterminado:true

Si se especifican URLs no válidas en el array urls, se ignorarán. En lugar de hacer que falle toda la solicitud, se creará un scraping por lotes con las URLs válidas restantes y las URLs no válidas se devolverán en el campo invalidURLs de la respuesta.

formats

(Markdown · object | Summary · object | HTML · object | Raw HTML · object | Links · object | Images · object | Screenshot · object | JSON · object | Change Tracking · object | Branding · object)\[]

Formatos de salida que se incluirán en la respuesta. Puedes especificar uno o varios formatos, ya sea como cadenas (p. ej., `'markdown'`) o como objetos con opciones adicionales (p. ej., `{ type: 'json', schema: {...} }`). Algunos formatos requieren configurar opciones específicas. Ejemplo: `['markdown', { type: 'json', schema: {...} }]`.

- Markdown
- Summary
- HTML
- Raw HTML
- Links
- Images
- Screenshot
- JSON
- Change Tracking
- Branding

onlyMainContent

boolean

predeterminado:true

Devuelve solo el contenido principal de la página, sin incluir encabezados, navegación, pies de página, etc.

Etiquetas que se incluirán en la salida.

Etiquetas que se excluirán de la salida.

maxAge

integer

predeterminado:172800000

Devuelve una versión en caché de la página si su antigüedad es menor que este valor en milisegundos. Si la versión en caché de la página es más antigua que este valor, se hará scraping de la página. Si no necesitas datos extremadamente recientes, habilitar esto puede acelerar tus procesos de scraping hasta un 500 %. El valor predeterminado es de 2 días.

&lt;\[ { "key": "0", "translation": "Cuando se establece, la solicitud solo consulta la caché y nunca inicia una nueva extracción. El valor se expresa en milisegundos y especifica la antigüedad mínima que deben tener los datos almacenados en caché. Si existen datos en caché que coinciden, se devuelven al instante. Si no se encuentran datos en caché, se devuelve un 404 con el código de error SCRAPE\_NO\_CACHED\_DATA. Establécelo en 1 para aceptar cualquier dato en caché, independientemente de su antigüedad." } ]&lt;/&gt;

Encabezados que se enviarán en la solicitud. Pueden usarse para enviar cookies, user-agent, etc.

Especifica un tiempo de espera en milisegundos antes de obtener el contenido, dando a la página tiempo suficiente para cargarse. Este tiempo de espera es adicional a la función de espera inteligente de Firecrawl.

mobile

boolean

predeterminado:false

Defínelo en true si quieres emular el scraping desde un dispositivo móvil. Útil para probar páginas responsive y tomar capturas de pantalla móviles.

skipTlsVerification

boolean

predeterminado:true

Omitir la verificación de certificados TLS al realizar solicitudes.

timeout

integer

predeterminado:30000

Tiempo de espera en milisegundos para la solicitud. El mínimo es 1000 (1 segundo). El valor predeterminado es 30000 (30 segundos). El máximo es 300000 (300 segundos).

Rango requerido: `1000 <= x <= 300000`

Controla cómo se procesan los archivos durante el scraping. Cuando se incluye "pdf" (valor predeterminado), se extrae el contenido del PDF y se convierte a formato Markdown, con la facturación basada en el número de páginas (1 crédito por página). Cuando se pasa un array vacío, el archivo PDF se devuelve codificado en base64 con una tarifa fija de 1 crédito por todo el PDF.

actions

(Wait by Duration · object | Wait for Element · object | Screenshot · object | Click · object | Write text · object | Press a key · object | Scroll · object | Scrape · object | Execute JavaScript · object | Generate PDF · object)\[]

Acciones que se realizarán en la página antes de extraer el contenido

- Wait by Duration
- Wait for Element
- Screenshot
- Click
- Write text
- Press a key
- Scroll
- Scrape
- Execute JavaScript
- Generate PDF

Configuración de ubicación para la solicitud. Cuando se especifica, se utilizará un proxy adecuado si está disponible y se emularán la configuración de idioma y la zona horaria correspondientes. De manera predeterminada será "US" si no se especifica.

removeBase64Images

boolean

predeterminado:true

Elimina todas las imágenes en base64 de la salida en markdown, que puede ser excesivamente larga. Esto no afecta a los formatos html ni rawHtml. El texto alternativo de la imagen permanece en la salida, pero la URL se sustituye por un marcador de posición.

blockAds

boolean

predeterminado:true

Habilita el bloqueo de anuncios y de ventanas emergentes de cookies.

proxy

enum&lt;string&gt;

predeterminado:auto

Especifica el tipo de proxy que se usará.

- basic: Proxies para hacer scraping de sitios con poca o ninguna protección antibots. Son rápidos y suelen funcionar bien.
- enhanced: Proxies avanzados para hacer scraping de sitios con soluciones antibots más sofisticadas. Son más lentos, pero más fiables en ciertos sitios. Pueden costar hasta 5 créditos por solicitud.
- auto: Firecrawl reintentará automáticamente el scraping con proxies mejorados si el proxy básico falla. Si el reintento con enhanced tiene éxito, se cobrarán 5 créditos por el scraping. Si el primer intento con basic tiene éxito, solo se cobrará el coste normal.

Opciones disponibles:

`basic`,

`enhanced`,

`auto`

storeInCache

boolean

predeterminado:true

Si es true, la página se almacenará en el índice y la caché de Firecrawl. Establecerlo en false es útil si tu actividad de scraping puede plantear problemas relacionados con la protección de datos. El uso de algunos parámetros asociados con scraping de datos sensibles (por ejemplo, acciones, headers) hará que este parámetro sea false.

zeroDataRetention

boolean

predeterminado:false

Si es true, se desactivará la retención de datos para este scraping por lotes. Para habilitar esta función, comunícate con [help@firecrawl.dev](mailto:help@firecrawl.dev)

#### Respuesta

Si ignoreInvalidURLs es true, este será un array que contiene las URL no válidas que se especificaron en la solicitud. Si no hubo URL no válidas, será un array vacío. Si ignoreInvalidURLs es false, este campo será undefined.