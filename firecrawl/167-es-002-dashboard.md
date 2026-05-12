---
title: Panel de control | Firecrawl
url: https://docs.firecrawl.dev/es/dashboard
source: sitemap
fetched_at: 2026-03-23T07:26:26.171926-03:00
rendered_js: false
word_count: 449
summary: This document provides an overview of the Firecrawl control panel, explaining how to manage account settings, monitor API usage, configure team roles, and utilize integrated tools like the playground and autonomous agent.
tags:
    - firecrawl
    - dashboard-overview
    - account-management
    - team-collaboration
    - api-monitoring
    - web-scraping-tools
category: guide
---

El [panel de control de Firecrawl](https://www.firecrawl.dev/app) es donde gestionas tu cuenta, pruebas endpoints y supervisas el uso. A continuación, se muestra un recorrido rápido por cada sección.

## Playground

El playground te permite probar los endpoints de Firecrawl directamente en el navegador antes de integrarlos en tu código.

- [**Scrape**](https://www.firecrawl.dev/app/playground?endpoint=scrape) — Extrae contenido de una sola página.
- [**Search**](https://www.firecrawl.dev/app/playground?endpoint=search) — Busca en la web y obtén resultados extraídos.
- [**Crawl**](https://www.firecrawl.dev/app/playground?endpoint=crawl) — Rastrea un sitio web completo y extrae contenido de cada página.
- [**Map**](https://www.firecrawl.dev/app/playground?endpoint=map) — Descubre todas las URL de un sitio web.

## Navegador

[Interactúa con la web](https://www.firecrawl.dev/app/browser) mediante una sesión activa del navegador. Puedes crear perfiles persistentes, ejecutar acciones y tomar capturas de pantalla, lo que resulta útil para páginas que requieren autenticación o interacciones complejas.

## Agent

El [Agent](https://www.firecrawl.dev/app/agent) es una herramienta de investigación impulsada por IA que puede navegar por la web de forma autónoma, seguir enlaces y extraer datos estructurados a partir de un prompt.

## Registros de actividad

[Registros de actividad](https://www.firecrawl.dev/app/logs) muestran el historial de tus solicitudes recientes a la API, incluido el estado, la duración y los créditos consumidos.

## Uso

La página de [Uso](https://www.firecrawl.dev/app/usage) muestra tu consumo de créditos a lo largo del tiempo y los totales del ciclo de facturación actual.

## Claves de API

Desde la página de [API Keys](https://www.firecrawl.dev/app/api-keys) puedes crear, ver y revocar las claves de API de tu equipo.

## Configuración

La página de [Settings](https://www.firecrawl.dev/app/settings) tiene tres pestañas:

- **Equipo** — Invita a miembros, asigna roles y gestiona tu equipo. Consulta [Gestión del equipo y roles](#team-management--roles) más abajo.
- **Billing** — Puedes ver tu plan actual, las facturas, la configuración de auto-recharge y aplicar cupones. Consulta también [Billing](https://docs.firecrawl.dev/es/billing).
- **Avanzado** — Secreto de firma del webhook y eliminación del equipo.

* * *

## Gestión del equipo y roles

Firecrawl te permite invitar a compañeros de equipo a colaborar en una cuenta compartida. Desde la pestaña **Team** en Configuración, puedes invitar a miembros, asignar roles y gestionar tu equipo.

### Roles

A cada miembro del equipo se le asigna uno de estos dos roles: **Administrador** o **Miembro**. Eliges el rol al enviar una invitación.

CapacidadAdministradorMiembro**General**Usar las claves de API y los recursos compartidos del equipo✓✓**Gestión del equipo**Ver la lista de miembros del equipo✓✓Salir del equipo✓✓Invitar a nuevos miembros al equipo✓✗Eliminar miembros del equipo✓✗Cambiar el rol de un miembro✓✗Revocar invitaciones pendientes✓✗Editar el nombre del equipo✓✗**Facturación**Ver las facturas y el uso✓✓Aplicar cupones de crédito✓✓Gestionar la suscripción y el portal de facturación✓✗**Configuración**Ver el secreto de firma del webhook✓✓Regenerar el secreto de firma del webhook✓✗Eliminar el equipo✓✗

En resumen, los **Administradores** tienen control total sobre la gestión del equipo, la facturación y la configuración, mientras que los **Miembros** pueden usar los recursos del equipo, ver el uso y aplicar cupones, pero no pueden modificar el equipo ni la suscripción.