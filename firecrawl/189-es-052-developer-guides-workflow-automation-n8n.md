---
title: Firecrawl + n8n - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/workflow-automation/n8n
source: sitemap
fetched_at: 2026-03-23T07:27:25.612393-03:00
rendered_js: false
word_count: 3707
summary: This guide explains how to integrate Firecrawl with n8n to automate web scraping workflows without writing code, covering account setup and platform configuration.
tags:
    - web-scraping
    - n8n
    - firecrawl
    - automation
    - api-integration
    - no-code
category: tutorial
---

## Introducción a Firecrawl y n8n

La automatización del web scraping se ha vuelto esencial para las empresas modernas. Ya sea que necesites monitorear precios de la competencia, recopilar contenido, generar leads o potenciar aplicaciones de IA con datos en tiempo real, la combinación de Firecrawl y n8n ofrece una solución potente sin requerir conocimientos de programación. ![Integración de Firecrawl y n8n](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=cb863000a893ef260cfe023e2455c88c) **¿Qué es n8n?** n8n es una plataforma de automatización de flujos de trabajo de código abierto que conecta distintas herramientas y servicios. Piénsalo como un entorno de programación visual donde arrastras y sueltas nodos sobre un lienzo, los conectas y creas flujos de trabajo automatizados. Con más de 400 integraciones, n8n te permite construir automatizaciones complejas sin escribir código.

## ¿Por qué usar Firecrawl con n8n?

El scraping web tradicional presenta varios desafíos. Los scripts personalizados se rompen cuando los sitios web actualizan su estructura. Los sistemas antibots bloquean las solicitudes automatizadas. Los sitios con mucho JavaScript no se renderizan correctamente. La infraestructura requiere mantenimiento constante. Firecrawl se encarga de estas complejidades técnicas en la parte de scraping, mientras que n8n proporciona el framework de automatización. Juntos te permiten crear flujos de trabajo listos para producción que:

- Extraen datos de cualquier sitio web de forma fiable
- Conectan los datos extraídos con otras herramientas empresariales
- Se ejecutan por programación o al activarse por eventos
- Escalan desde tareas simples hasta canalizaciones complejas

Esta guía te explicará cómo configurar ambas plataformas y crear tu primer flujo de trabajo de scraping desde cero.

## Paso 1: Crea tu cuenta de Firecrawl

Firecrawl ofrece capacidades de web scraping para tus flujos de trabajo. Configuremos tu cuenta y obtengamos tus credenciales de API.

### Regístrate en Firecrawl

1. Ve a [firecrawl.dev](https://firecrawl.dev) en tu navegador
2. Haz clic en el botón “Get Started” o “Sign Up”
3. Crea una cuenta con tu correo electrónico o con tu cuenta de GitHub
4. Verifica tu correo electrónico si se te solicita

### Obtén tu clave de API

Después de iniciar sesión, necesitas una clave de API para conectar Firecrawl con n8n:

1. Ve a tu panel de Firecrawl
2. Ve a la [página de API Keys](https://www.firecrawl.dev/app/api-keys)
3. Haz clic en “Create New API Key”
4. Asigna a tu clave un nombre descriptivo (p. ej., “Integración con n8n”)
5. Copia la clave de API generada y guárdala en un lugar seguro

![Sección de clave de API de Firecrawl](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-api-key-creation-dashboard.gif?s=2c04559b9027dfe825e3ba7d78af8527)

Firecrawl ofrece créditos gratuitos al registrarte, suficientes para probar tus flujos de trabajo y completar este tutorial.

## Paso 2: Configurar n8n

n8n ofrece dos opciones de despliegue: en la nube o autohospedado. Para principiantes, la versión en la nube es la forma más rápida de empezar.

### Elige tu versión de n8n

**n8n Cloud (recomendado para principiantes):**

- No requiere instalación
- Plan gratuito disponible
- Infraestructura gestionada
- Actualizaciones automáticas

**Autoalojado:**

- Control total de los datos
- Ejecútalo en tus propios servidores
- Requiere Docker
- Ideal para usuarios avanzados con requisitos de seguridad específicos

Elige la opción que mejor se adapte a tus necesidades. Ambos caminos te llevarán a la misma interfaz del editor de flujos de trabajo.

### Opción A: n8n Cloud (recomendado para principiantes)

1. Visita [n8n.cloud](https://n8n.cloud)
2. Haz clic en “Start Free” o “Sign Up”
3. Regístrate con tu correo electrónico o con GitHub
4. Completa la verificación
5. Serás dirigido a tu panel de n8n

![Página principal de n8n Cloud mostrando las opciones de registro](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7965f6fab8bd1d48b81db7c1dbed1e7f) El plan gratuito incluye todo lo necesario para crear y probar flujos de trabajo. Puedes actualizar más adelante si necesitas más tiempo de ejecución o funciones avanzadas.

### Opción B: Autohospedado con Docker

Si prefieres ejecutar n8n en tu propia infraestructura, puedes configurarlo rápidamente con Docker. **Requisitos previos:**

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado en tu equipo
- Conocimientos básicos de la línea de comandos/terminal

**Pasos de instalación:**

1. Abre tu terminal o consola de comandos
2. Crea un volumen de Docker para conservar los datos de tus flujos de trabajo:

```
docker volume create n8n_data
```

Este volumen guarda tus flujos de trabajo, credenciales e historial de ejecución para que se conserven incluso si reinicias el contenedor.

3. Ejecuta el contenedor de Docker de n8n:

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

![Terminal showing the docker commands being executed with n8n starting up](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-docker-self-hosted-installation.gif?s=4968ecd0996ef3e76dc0abb886ae52ca)

4. Espera a que n8n se inicie. Verás un mensaje indicando que el servidor está en ejecución.
5. Abre tu navegador y ve a `http://localhost:5678`.
6. Crea tu cuenta de n8n registrándote con un correo electrónico.

![n8n self-hosted welcome screen at localhost:5678](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=163949933d76425a68ec728639e767ea) Tu instancia autogestionada de n8n ahora se está ejecutando localmente. La interfaz es idéntica a n8n Cloud, por lo que puedes seguir el resto de esta guía independientemente de la opción que hayas elegido.

### Comprender la interfaz de n8n

Cuando inicies sesión por primera vez en n8n, verás el panel principal: ![n8n dashboard showing the workflow list view with "Create new workflow" button](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5d92092b94fd021c2cebf163c2ef4d01) Elementos clave de la interfaz:

- **Workflows**: Aquí aparecen tus automatizaciones guardadas
- **Executions**: Historial de ejecuciones de workflows
- **Credentials**: Claves de API y tokens de autenticación almacenados
- **Settings**: Configuración de la cuenta y del espacio de trabajo

Haz clic en “Create New Workflow” para abrir el editor de workflows.

### El lienzo del flujo de trabajo

El editor de flujos de trabajo es donde crearás tus automatizaciones: ![Lienzo de flujo de trabajo vacío de n8n con el botón "+" visible en el centro](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7508078e88b57ccedc2a4d4a258fddf8) Elementos importantes:

- **Lienzo**: El área principal donde ubicas y conectas nodos
- **Botón Agregar nodo (+)**: Haz clic para añadir nuevos nodos a tu flujo de trabajo
- **Panel de nodos**: Se abre al hacer clic en “+” y muestra todos los nodos disponibles
- **Ejecutar flujo de trabajo**: Ejecuta tu flujo de trabajo manualmente para pruebas
- **Guardar**: Guarda la configuración de tu flujo de trabajo

Construyamos tu primer flujo de trabajo añadiendo el nodo Firecrawl.

## Paso 3: Instalar y configurar el nodo de Firecrawl

n8n incluye compatibilidad nativa con Firecrawl. Instalarás el nodo y lo conectarás a tu cuenta de Firecrawl usando la clave de API que creaste anteriormente.

### Añade el nodo de Firecrawl a tu flujo de trabajo

1. En el lienzo de tu nuevo flujo de trabajo, haz clic en el botón ”**+**” en el centro
2. Se abrirá el panel de selección de nodos en el lado derecho
3. En la barra de búsqueda de la parte superior, escribe “**Firecrawl**”
4. Verás el nodo de Firecrawl en los resultados de búsqueda

<!--THE END-->

![Haciendo clic en el botón +, escribiendo "Firecrawl" en la búsqueda y apareciendo el nodo de Firecrawl](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-search-install-firecrawl-node.gif?s=6d81f8bf967429cfaf2bcf22c3976fbf)

5. Haz clic en “**Install**” junto al nodo de Firecrawl
6. Espera a que finalice la instalación (tardará unos segundos)
7. Una vez instalado, haz clic en el nodo de Firecrawl para añadirlo a tu lienzo

![Nodo de Firecrawl añadido al lienzo, mostrado como un recuadro con el logotipo de Firecrawl](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-node-added-canvas.gif?s=d7480ebf8ef357fba9a0c5ee5123ffc8) El nodo de Firecrawl aparecerá en tu lienzo como un recuadro con el logotipo de Firecrawl. Este nodo representa una operación individual de Firecrawl en tu flujo de trabajo.

### Conecta tu clave de API de Firecrawl

Antes de poder usar el nodo de Firecrawl, debes autenticarlo con tu clave de API:

1. Haz clic en el recuadro del nodo de Firecrawl para abrir su panel de configuración a la derecha
2. En la parte superior, verás un menú desplegable “Credential to connect with”
3. Como es tu primera vez, haz clic en “**Create New Credential**”

<!--THE END-->

![Panel de configuración del nodo de Firecrawl que muestra el menú desplegable de credenciales con la opción "Create New Credential"](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-api-credentials-setup.gif?s=547bda13daeb17dd963160a8ef4bbf48)

4. Se abre una ventana de configuración de credenciales
5. Ingresa un nombre para esta credencial (p. ej., “Mi cuenta de Firecrawl”)
6. Pega tu clave de API de Firecrawl en el campo “API Key”
7. Haz clic en “**Save**” en la parte inferior

La credencial ahora se guardó en n8n. No tendrás que ingresar tu clave de API nuevamente para futuros nodos de Firecrawl.

### Prueba tu conexión

Verifiquemos que tu nodo de Firecrawl esté correctamente conectado:

1. Con el nodo de Firecrawl aún seleccionado, revisa el panel de configuración
2. En el menú desplegable “Resource”, selecciona “**Scrape a url and get its content**”
3. En el campo “URL”, introduce: `https://firecrawl.dev`
4. Deja el resto de ajustes con sus valores predeterminados por ahora
5. Haz clic en el botón “**Test step**” en la esquina inferior derecha del nodo

![Selecting Scrape operation, entering example.com URL, and clicking Test step button](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-test-connection-scrape.gif?s=a5a832a971778744a6ceaf9d2ff0cdb1) Si todo está configurado correctamente, verás que el contenido extraído de example.com aparece en el panel de salida debajo del nodo. ¡Enhorabuena! Tu nodo de Firecrawl ya está conectado y funcionando.

## Paso 4: Crea tu bot de Telegram

Antes de construir tu primer flujo de trabajo, necesitarás un bot de Telegram para recibir notificaciones. Los bots de Telegram son gratuitos y fáciles de crear mediante BotFather de Telegram.

### Crea un bot con BotFather

1. Abre Telegram en tu teléfono o en el escritorio
2. Busca “**@BotFather**” (el bot oficial de Telegram)
3. Inicia una conversación con BotFather haciendo clic en “**Start**”
4. Envía el comando `/newbot` para crear un bot nuevo
5. BotFather te pedirá que elijas un nombre para tu bot (es el nombre que verán los usuarios)
6. Introduce un nombre como “**My Firecrawl Bot**”
7. Luego, elige un nombre de usuario para tu bot. Debe terminar en “bot” (p. ej., “**my\_firecrawl\_updates\_bot**”)
8. Si el nombre de usuario está disponible, BotFather creará tu bot y te enviará un mensaje con el token de tu bot

![Creación de un bot con BotFather, mostrando todo el flujo de la conversación](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=45ee39deae96fbc3eac5fdb2eeba2e0b)

### Obtén tu ID de chat

Para enviarte mensajes a ti mismo, necesitas tu ID de chat de Telegram:

1. Abre tu navegador web y visita esta URL (sustituye `YOUR_BOT_TOKEN` por el token real de tu bot):
   
   ```
   https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
   ```
2. Deja abierta esta pestaña del navegador
3. Ahora, busca en Telegram el nombre de usuario de tu bot (el que acabas de crear)
4. Inicia una conversación con tu bot haciendo clic en “**Start**”
5. Envía cualquier mensaje a tu bot (p. ej., «hola»)
6. Vuelve a la pestaña del navegador y recarga la página
7. Busca el campo `"chat":{"id":` en la respuesta JSON
8. El número junto a `"id":` es tu ID de chat (p. ej., `123456789`)
9. Guarda este ID de chat para más adelante

![Browser showing Telegram API getUpdates response with chat ID highlighted](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-api-get-chat-id-browser.gif?s=e074ecf1a659bdfa7284e86c923be06f)

Ahora ya tienes todo lo necesario para integrar Telegram con tus flujos de trabajo de n8n.

## Paso 5: Crea flujos de trabajo prácticos con Telegram

Ahora construiremos tres flujos de trabajo reales que envían información directamente a tu Telegram. Estos ejemplos muestran distintas operaciones de Firecrawl y cómo integrarlas con notificaciones de Telegram.

### Ejemplo 1: Resumen diario de actualizaciones de producto de Firecrawl

Recibe cada mañana en tu Telegram un resumen diario de las actualizaciones de producto de Firecrawl. **Lo que vas a crear:**

- Rastrea el blog de actualizaciones de producto de Firecrawl a las 9:00 AM todos los días
- Usa IA para generar un resumen del contenido
- Envía el resumen a tu Telegram

**Paso a paso:**

1. Crea un nuevo workflow en n8n
2. Agrega un nodo **Schedule Trigger**:
   
   - Haz clic en el botón ”**+**” en el lienzo
   - Busca “**Schedule Trigger**”
   - Configura: Todos los días a las 9:00 AM

<!--THE END-->

![Schedule Trigger configured for daily 9 AM execution](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-schedule-trigger-daily-cron.gif?s=ae68cd74cdf14a1d012861df8319b245)

3. Agrega el nodo **Firecrawl**:
   
   - Haz clic en ”**+**” junto a Schedule Trigger
   - Busca y agrega “**Firecrawl**”
   - Selecciona tu credencial de Firecrawl
   - Configura:
     
     - **Resource**: Extraer una URL y obtener su contenido
     - **URL**: `https://www.firecrawl.dev/blog/category/product-updates`
     - **Formats**: Selecciona “Summary”

<!--THE END-->

![Adding and configuring Firecrawl node with the blog URL and Summary format selected](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-scrape-blog-summary.gif?s=ad1684f165aacd7ab5d1530cdac73962)

4. Agrega el nodo **Telegram**:
   
   - Haz clic en ”**+**” junto a Firecrawl
   - Busca “**Telegram**”
   - Haz clic en “**Send a text message**” para agregarlo al lienzo
5. Configura las credenciales de Telegram:
   
   - Haz clic en el nodo de Telegram para abrir su configuración
   - En el desplegable “Credential to connect with”, haz clic en “**Create New Credential**”
   - Pega el token de tu bot desde BotFather
   - Haz clic en “**Save**”

<!--THE END-->

![Telegram credential configuration with bot token field](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-telegram-bot-token-credentials.gif)

6. Configura el mensaje de Telegram:
   
   - **Operation**: Send Message
   - **Chat ID**: Ingresa tu ID de chat
   - **Text**: Déjalo con un mensaje de “hello” por ahora
   - Haz clic en **Execute step** para probar el envío de un mensaje mientras recibes el resumen de Firecrawl.

<!--THE END-->

![Configuring Telegram node and mapping the summary field to the message text](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-test-telegram-message-firecrawl.gif)

- Ahora, con la estructura del resumen de Firecrawl, agrega el resumen al texto del mensaje arrastrando el campo `summary` desde la salida del nodo de Firecrawl.

<!--THE END-->

7. Prueba el workflow:
   
   - Haz clic en “**Execute Workflow**”
   - Revisa tu Telegram para ver el mensaje con el resumen

<!--THE END-->

![Complete workflow showing Schedule Trigger → Firecrawl → Telegram with all nodes connected](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=1c3eacbcb705c21c6265ae3ecbd59d59)

8. Activa el workflow activando el interruptor “**Active**”

Tu bot de Telegram ahora te enviará un resumen diario de las actualizaciones de producto de Firecrawl todas las mañanas a las 9:00 AM.

### Ejemplo 2: Búsqueda de noticias de IA a Telegram

Este flujo de trabajo usa la operación Search de Firecrawl para encontrar noticias de IA y enviar los resultados formateados a Telegram. **Diferencias clave con el Ejemplo 1:**

- Usa un **Manual Trigger** en lugar de Schedule (se ejecuta bajo demanda)
- Usa la operación **Search** en lugar de Scrape
- Incluye un nodo **Code** para formatear varios resultados

**Crea el flujo de trabajo:**

1. Crea un flujo de trabajo nuevo y agrega un nodo **Manual Trigger**
2. Agrega un nodo **Firecrawl** con estas configuraciones:
   
   - **Resource**: Search and optionally scrape search results
   - **Query**: `ai news`
   - **Limit**: 5

<!--THE END-->

![Firecrawl Search node configuration with "ai news" query](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-search-ai-news-results.gif?s=23eb224783b0b3155d179a0342839621)

3. Agrega un nodo **Code** para formatear los resultados de la búsqueda:
   
   - Selecciona “Run Once for All Items”
   - Pega este código:

```
const results = $input.all();
let message = "Últimas noticias de IA:\n\n";

results.forEach((item) => {
  const webData = item.json.data.web;
  webData.forEach((article, index) => {
    message += `${index + 1}. ${article.title}\n`;
    message += `${article.description}\n`;
    message += `${article.url}\n\n`;
  });
});

return [{ json: { message } }];
```

![Agregar el nodo Code y pegar el script de formateo](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-code-node-format-news-articles.gif?s=cafb96e0b7f2ef27a09ae2957390799b)

4. Actualiza el nodo **Telegram** (usando tu credencial guardada):
   
   - **Text**: Arrastra el campo `message` desde el nodo Code

![Ejecución completa del flujo con noticias de IA enviadas a Telegram](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-execute-workflow-telegram-delivery.gif)

### Ejemplo 3: Resumen de noticias con IA

Este flujo de trabajo añade IA al Ejemplo 2, usando OpenAI para generar resúmenes inteligentes de las últimas noticias sobre IA antes de enviarlas a Telegram. **Cambios clave respecto al Ejemplo 2:**

- Añade la configuración de **credenciales de OpenAI**
- Añade un nodo **AI Agent** entre Code y Telegram
- AI Agent analiza y resume todas las noticias de forma inteligente
- Telegram recibe el resumen generado por IA en lugar de la lista de noticias sin procesar

**Modifica el flujo de trabajo:**

1. **Obtén tu clave de API de OpenAI**:
   
   - Ve a [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Inicia sesión o crea una cuenta
   - Haz clic en “**Create new secret key**”
   - Asígnale un nombre (p. ej., “n8n Integration”)
   - Copia la clave de API de inmediato (no la volverás a ver)

<!--THE END-->

![OpenAI dashboard showing API key creation](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/openai-api-key-creation-dashboard.gif?s=8222a339a403f85272102256fa91fc27)

2. **Añade y conecta el nodo AI Agent**:
   
   - Haz clic en ”**+**” después del nodo Code
   - Busca “**Basic LLM Chain**” o “**AI Agent**”
   - Arrastra el campo `message` desde el nodo Code al campo de prompt de entrada del AI Agent
   - Selecciona **OpenAI** como proveedor de LLM

<!--THE END-->

![Adding AI Agent node, dragging input from Code node, and connecting OpenAI as LLM](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-agent-openai-llm-setup.gif)

3. **Añade tus credenciales de OpenAI**:
   
   - Haz clic en “**Create New Credential**” para OpenAI
   - Pega tu clave de API de OpenAI
   - Selecciona el modelo: **gpt-5-mini** (rentable) o **gpt-5** (más capaz)
   - Haz clic en “**Save**”

<!--THE END-->

![Adding OpenAI credentials to the AI Agent node](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-openai-credentials-gpt-model.gif?s=c97249f572e8d530583918ebc3357d53)

4. **Añade el prompt del sistema al AI Agent**:
   
   - En el nodo AI Agent, añade este prompt del sistema:

```
Eres un analista de noticias de IA. Analiza los artículos de noticias de IA proporcionados y crea un resumen conciso
y perspicaz que destaque los desarrollos y tendencias más importantes.
Agrupa los temas relacionados y proporciona contexto sobre por qué estos desarrollos son importantes.
Mantén el resumen conversacional y atractivo, de aproximadamente 3-4 párrafos.
```

![Agregar el prompt del sistema al nodo AI Agent](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-ai-agent-system-prompt-configuration.gif?s=45c34c7010aa6319f8d4dde84c6e5ab9)

5. **Actualiza el nodo de Telegram y realiza una prueba**:
   
   - Actualiza el nodo de Telegram:
     
     - **Text**: Arrastra la salida del AI Agent (el resumen generado)
     - Elimina el mapeo anterior al mensaje del nodo Code
   - Haz clic en “**Execute Workflow**” para probar
   - La IA analizará todos los artículos de noticias y generará un resumen
   - Revisa tu Telegram para ver el resumen generado por la IA

![Ejecución completa del flujo con resumen generado por la IA enviado a Telegram](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-summary-telegram-workflow-execution.gif)

## Entender las operaciones de Firecrawl

Ahora que has creado algunos flujos de trabajo, exploremos las distintas operaciones de Firecrawl disponibles en n8n. Cada operación está diseñada para casos de uso específicos de extracción web.

Extrae contenido de una única página web y lo devuelve en varios formatos. **Qué hace:**

- Realiza scraping de una sola URL
- Devuelve Markdown limpio, HTML o resúmenes generados por IA
- Puede tomar capturas de pantalla y extraer enlaces

**Ideal para:**

- Extracción de artículos
- Monitoreo de páginas de producto
- Scraping de publicaciones de blog
- Generación de resúmenes de páginas

**Ejemplo de caso de uso:** Resúmenes diarios de blogs (como en el Ejemplo 1 anterior)

Realiza búsquedas en la web y devuelve resultados con extracción opcional de contenido. **Qué hace:**

- Busca en la web, en noticias o en imágenes
- Devuelve títulos, descripciones y URL
- Puede extraer el contenido completo de los resultados

**Ideal para:**

- Automatización de investigación
- Seguimiento de noticias
- Detección de tendencias
- Encontrar contenido relevante

**Ejemplo de uso:** agregación de noticias con IA (como en el Ejemplo 2 anterior)

### Rastrear un sitio web

Descubre y extrae de forma recursiva múltiples páginas de un sitio web. **Qué hace:**

- Sigue enlaces automáticamente
- Extrae múltiples páginas en una sola operación
- Puede filtrar URL por patrones

**Ideal para:**

- Extracción completa de documentación
- Archivado de sitios
- Recopilación de datos de múltiples páginas

### Mapear un sitio web y obtener URLs

Devuelve todas las URLs encontradas en un sitio web sin extraer contenido. **Qué hace:**

- Descubre todos los enlaces del sitio
- Devuelve una lista limpia de URLs
- Rápido y liviano

**Ideal para:**

- Descubrimiento de URLs
- Generación de sitemaps
- Planificación de rastreos a gran escala

Usa IA para extraer información estructurada según instrucciones o esquemas personalizados. **Qué hace:**

- Extracción de datos con IA
- Devuelve los datos en el formato que indiques
- Funciona en varias páginas

**Ideal para:**

- Extracción de datos personalizada
- Creación de bases de datos
- Obtención de información estructurada

Extrae varias URL en paralelo de forma eficiente. **Qué hace:**

- Procesa varias URL a la vez
- Más eficiente que usar bucles
- Devuelve todos los resultados a la vez

**Ideal para:**

- Procesar listas de URL
- Recolección de datos masiva
- Proyectos de scraping a gran escala

### Agente

Utiliza un agente de IA para navegar y extraer datos de sitios web de forma autónoma a partir de un prompt en lenguaje natural. **Qué hace:**

- Acepta un prompt que describe qué datos necesitas
- El agente de IA navega y extrae información de forma autónoma
- Disponible en modo **Sync** (espera los resultados) y modo **Async** (devuelve un ID de trabajo inmediatamente)
- Usa **Get Agent Status** para consultar los resultados cuando uses el modo Async

**Mejor para:**

- Recolección de datos compleja y en múltiples páginas guiada por un prompt
- Extraer información cuando no conoces la estructura exacta de la página
- Tareas de investigación que requieren navegar por múltiples páginas

**Sync vs. Async:**

- **Agent (Sync)** inicia el trabajo y espera el resultado en un solo paso: es lo más sencillo para la mayoría de los casos de uso. El parámetro **Max Wait Time** controla durante cuánto tiempo el nodo consulta el estado antes de agotar el tiempo de espera (predeterminado: 300 segundos; máximo: 600 segundos). Si el trabajo del agente tarda más que esto, el nodo devuelve un estado de tiempo de espera agotado aunque el trabajo aún pueda completarse del lado de Firecrawl. Para trabajos que puedan superar los 10 minutos, usa el modo async en su lugar.
- **Agent (Async)** devuelve un ID de trabajo inmediatamente. Agrega un segundo nodo de Firecrawl con la operación **Get Agent Status** para obtener los resultados una vez que el trabajo se complete.

Para más detalles sobre la función de agente, consulta la [documentación de Agent](https://docs.firecrawl.dev/es/features/agent).

## Plantillas y ejemplos de flujos de trabajo

En lugar de crear desde cero, puedes comenzar con plantillas ya preparadas. La comunidad de n8n ha creado numerosos flujos de trabajo de Firecrawl que puedes copiar y personalizar.

### Plantillas destacadas

### Cómo importar plantillas

Para usar una plantilla de la comunidad de n8n:

1. Haz clic en un enlace de plantilla de flujo de trabajo
2. Haz clic en el botón “**Import template to localhost:5678 self-hosted instance**” en la página de la plantilla
3. El flujo de trabajo se abrirá en tu instancia de n8n
4. Configura las credenciales de cada nodo
5. Personaliza los ajustes para tu caso de uso
6. Activa el flujo de trabajo

![Importar una plantilla desde n8n.io, mostrando el botón de importación y el flujo de trabajo que aparece en n8n](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-import.gif?s=5bd77d25fa2dc525e0032a483803fd00)

## Mejores prácticas

Sigue estas pautas para crear flujos de trabajo fiables y eficientes:

### Pruebas y depuración

- Siempre prueba los flujos de trabajo manualmente antes de activar las programaciones
- Usa el botón “**Execute Workflow**” para probar todo el flujo
- Verifica los datos de salida en cada nodo para comprobar la corrección
- Usa la pestaña “**Executions**” para revisar ejecuciones anteriores y depurar problemas

![Pestaña Executions que muestra el historial de ejecuciones del flujo de trabajo con marcas de tiempo y estado](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-debugging.gif?s=2962335b6f72ea39cf6cb68cb6ed83c3)

### Manejo de errores

- Agrega nodos Error Trigger para detectar y manejar errores
- Configura notificaciones cuando fallen los flujos de trabajo
- Usa la opción “**Continue On Fail**” para nodos no críticos
- Supervisa con regularidad las ejecuciones de tu flujo de trabajo

### Optimización del rendimiento

- Usa Batch Scrape para varias URL en lugar de bucles
- Establece límites de velocidad adecuados para no saturar los sitios de destino
- Almacena en caché los datos cuando sea posible para reducir solicitudes innecesarias
- Programa los flujos de trabajo más intensivos en horas de baja demanda

### Seguridad

- Nunca expongas claves de API en las configuraciones de flujos de trabajo
- Usa el sistema de credenciales de n8n para almacenar la autenticación de forma segura
- Ten cuidado al compartir flujos de trabajo públicamente
- Respeta los términos del servicio y el archivo robots.txt de los sitios web de destino

## Próximos pasos

Ya tienes las bases para crear automatizaciones de web scraping con Firecrawl y n8n. Aquí tienes cómo seguir aprendiendo:

### Explora funciones avanzadas

- Revisa las configuraciones de webhooks para el procesamiento de datos en tiempo real
- Prueba la extracción con IA usando prompts e esquemas
- Crea flujos de trabajo complejos de varios pasos con lógica ramificada

<!--THE END-->

- [Firecrawl Discord](https://discord.gg/firecrawl) - Obtén ayuda con Firecrawl y habla sobre web scraping
- [Foro de la comunidad de n8n](https://community.n8n.io/) - Haz preguntas sobre automatización de flujos de trabajo
- Comparte tus flujos de trabajo y aprende de los demás

### Ruta de aprendizaje recomendada

1. Completa los flujos de trabajo de ejemplo de esta guía
2. Modifica plantillas de la biblioteca de la comunidad
3. Crea un flujo de trabajo para resolver un problema real de tu trabajo
4. Explora las operaciones avanzadas de Firecrawl
5. Contribuye con tus propias plantillas para ayudar a otros

## Recursos adicionales

- [Documentación de la API de Firecrawl](https://docs.firecrawl.dev/es/api-reference/v2-introduction)
- [Documentación de n8n](https://docs.n8n.io/)
- [Mejores prácticas de web scraping](https://www.firecrawl.dev/blog)