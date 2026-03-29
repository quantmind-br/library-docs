---
description: Auto-generated documentation index for OLX API Integration
generated: 2026-02-07T15:22:19.235221
source: https://developers.olx.com.br/
total_docs: 87
categories: 18
---

# OLX API Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence from basic setup to advanced integration.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://developers.olx.com.br/ |
| **Generated** | 2026-02-07T15:18:36.233500352-03:00 |
| **Organized** | 2026-02-07T15:22:19.235221 |
| **Total Documents** | 87 |
| **Categories** | 18 |
| **Organization Method** | Sequential Numbering |

---

## Quick Navigation

| Category | Files | Range |
|----------|-------|-------|
| Welcome & Overview | 2 | 001-002 |
| Quick Start & Getting Started | 3 | 003-005 |
| Authentication & Security | 3 | 006-008 |
| Core API - Advertisement Management | 8 | 009-016 |
| Webhooks & Notifications | 5 | 017-021 |
| Chat Integration | 3 | 022-024 |
| Leads Integration | 5 | 025-029 |
| Ad Highlights & Features | 4 | 030-033 |
| Ad Renewals | 1 | 034-034 |
| Vehicle History (HV) | 3 | 035-037 |
| Real Estate - JSON Import | 8 | 038-045 |
| Real Estate - API & XML | 12 | 046-057 |
| Autos & Vehicles - JSON | 9 | 058-066 |
| Autos & Vehicles - API | 8 | 067-074 |
| Lead Descriptions - Autos | 3 | 075-077 |
| Agro & Industry | 4 | 078-081 |
| Electronics | 2 | 082-083 |
| Deprecated APIs | 4 | 084-087 |

---

## Document Index by Category

### 1. Welcome & Overview (001-002)
*Portal entry point and general documentation overview*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | Portal de integração OLX | This document serves as the central landing page for the OLX integration portal,... | olx-api, developer-portal, integration-hub, webhooks, rate-limiting |
| 002 | `002-faq-home.md` | Perguntas Frequentes | This document provides a directory of links to frequently asked questions and te... | olx-api, faq, rate-limiting, image-specifications, integration-support |

### 2. Quick Start & Getting Started (003-005)
*Getting started guides for ad integration*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-anuncio-home.md` | Documentação para a Importação de Anúncios da OLX | This document outlines the available methods for third-party ad integration on O... | olx-integration, ad-import, api-reference, xml-integration, json-integration |
| 004 | `004-anuncio-api-home.md` | Documentação da API de Integração de Anúncios da OLX | This document provides an overview of the OLX Ad Integration API, detailing its ... | olx-api, ad-integration, inventory-management, oauth, webhooks |
| 005 | `005-anuncio-json-home.md` | Importação de Anúncios via Arquivo JSON | This document outlines the technical requirements and procedures for importing a... | olx-integration, json-import, ad-management, data-synchronization, bulk-upload |

### 3. Authentication & Security (006-008)
*OAuth authentication and security guidelines*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-anuncio-api-oauth.md` | Autenticação na API olx.com.br | This document provides a comprehensive guide for implementing OAuth 2.0 authenti... | oauth-2-0, api-authentication, olx-api, web-application, authorization-flow |
| 007 | `007-chat-oauth-chat.md` | Autenticação do chat na API olx.com.br | This document outlines the authentication and authorization process for OLX chat... | authentication, authorization, oauth-2-0, olx-api, chat-integration |
| 008 | `008-faq-rate-limit.md` | Limitação de Taxa (Rate Limit) na API | This document outlines the rate limiting policy for OLX APIs, specifying request... | olx-api, rate-limiting, api-throttling, status-429, ip-based-limit |

### 4. Core API - Advertisement Management (009-016)
*Primary API endpoints for ad CRUD operations and status*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 009 | `009-anuncio-api-import.md` | Importação de Anúncios (Inserção/Edição/Deleção) | This document provides technical instructions for programmatically inserting, up... | olx-api, ad-management, oauth-authentication, json-import, api-integration |
| 010 | `010-anuncio-api-ads.md` | Consulta de status da publicação | This document explains how to monitor and query the status of advertisements pub... | olx-api, ad-status, import-process, webhooks, api-integration |
| 011 | `011-anuncio-api-publishing-status.md` | Consulta de status da Importação | Explains how to query the publication status of ads after an import process on t... | olx-api, publication-status, ad-import, autoupload, api-reference |
| 012 | `012-anuncio-api-published-ads.md` | Listagem de Publicação | This document describes the OLX Publication Listing API, detailing how to system... | olx-api, listing-api, pagination, ad-management, api-reference |
| 013 | `013-anuncio-api-published-ads-status.md` | Consulta do status de Anúncios Publicados | This document provides technical specifications for the OLX API endpoint used to... | olx-api, ad-status, rest-api, authentication, json-response |
| 014 | `014-faq-xml-json-insertion.md` | Inferência de operações | This document explains the logic used by OLX to process advertisement insertions... | olx-integration, xml-import, json-import, ad-management, data-synchronization |
| 015 | `015-faq-category.md` | Alteração de categoria | Explains that a listing's category cannot be changed once it has been created an... | listing-management, category-change, ad-policy, marketplace-rules |
| 016 | `016-faq-images.md` | Especificação de Imagens | This document outlines the technical specifications for images uploaded via inte... | image-specifications, olx-integration, file-requirements, technical-standards, image-dimensions |

### 5. Webhooks & Notifications (017-021)
*Real-time notifications and webhook configuration*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 017 | `017-webhooks-home.md` | Notificação via Webhooks | This document explains how to integrate and receive automated notifications abou... | webhooks, api-integration, notifications, ad-status, http-post |
| 018 | `018-webhooks-notifications-configuration.md` | Configuração de Notificações | This document explains how to set up and manage webhook notifications for advert... | olx-api, webhooks, notification-configuration, oauth-authentication, ad-status |
| 019 | `019-webhooks-notifications-model.md` | Modelo de notificações | This document defines the structure and data format of webhook notifications, in... | webhook-notifications, json-payload, api-integration, ad-status, event-notifications |
| 020 | `020-webhooks-notifications-ad-status.md` | Notificação de Status de Anúncios | This document describes the structure and field definitions for advertisement st... | ad-status, notifications, api-reference, integration, olx-api |
| 021 | `021-webhooks-url-encoding.md` | Codificação de URL | This document outlines the required URL structures and formatting for configurin... | url-encoding, endpoint-configuration, notification-api, advertiser-id, integration-setup |

### 6. Chat Integration (022-024)
*Bidirectional chat messaging between OLX and CRMs*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 022 | `022-chat-home.md` | Documentação para a Integração de Chat | This document provides an overview of the OLX chat integration, detailing how to... | olx-api, chat-integration, oauth-authentication, crm-integration, messaging |
| 023 | `023-chat-receive-message.md` | Recebendo mensagens do chat (OLX → CRM) | This document explains how to configure and receive OLX chat messages via webhoo... | olx-integration, webhook-configuration, chat-api, crm-integration, http-protocol |
| 024 | `024-chat-send-message.md` | Respondendo à um chat (CRM → OLX) | This document provides the technical specification for the OLX Auto Service API ... | olx-api, crm-integration, chat-messaging, api-endpoint, http-post |

### 7. Leads Integration (025-029)
*Lead delivery and CRM integration*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 025 | `025-lead-home.md` | Documentação para a Integração de Leads com a OLX | This document provides an overview of how CRMs and management software can integ... | olx-leads, crm-integration, lead-management, api-documentation, lead-delivery |
| 026 | `026-lead-how-to.md` | Integrar lead na OLX | Explica como configurar e gerenciar endpoints para o recebimento de leads da OLX... | olx-leads, api-integration, oauth-authentication, lead-configuration, webhooks |
| 027 | `027-lead-leads.md` | Envio de Leads | This document outlines the technical specifications for integrating OLX leads vi... | api-integration, lead-generation, json-payload, olx-platform, webhook |
| 028 | `028-lead-leads-enriched.md` | Leads com informações detalhadas do anúncio | This document explains the integration of lead data with an additional 'adsInfo'... | lead-integration, ads-info, api-payload, autos-category, olx-integration |
| 029 | `029-lead-support.md` | Contato | This document explains the process for configuring lead delivery URLs and obtain... | olx-integration, lead-homologation, api-configuration, technical-support, endpoint-setup |

### 8. Ad Highlights & Features (030-033)
*Managing ad highlights and visibility features*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-destaque-home.md` | Destaques do anuncio | This document explains the Destaques feature for boosting ad visibility on the O... | olx-api, ad-visibility, highlights-pro, ad-management, integration-support |
| 031 | `031-destaque-balance-ads.md` | Consumo Saldos e Limites de Anúncios | This document explains how to use the OLX balance API to monitor ad insertion li... | olx-ads-api, balance-tracking, ad-insertion-limits, api-reference, endpoint-documentation |
| 032 | `032-destaque-bumps-get.md` | Consulta de anúncios destacados | This document provides technical specifications for the OLX API endpoint used to... | olx-api, ad-highlighting, api-reference, bump-ads, json-response |
| 033 | `033-destaque-bumps-put.md` | Aplicação de destaque em anúncio | This document provides technical specifications for the OLX Highlights API, deta... | olx-api, ad-highlighting, bump-ads, rest-api, oauth-authentication |

### 9. Ad Renewals (034-034)
*Automated ad renewal functionality*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 034 | `034-renewals-home.md` | Renovação de Anúncios | This document provides the technical specification for the OLX Ad Renewal API, e... | olx-api, ads-renewal, batch-processing, api-documentation, ad-management |

### 10. Vehicle History (HV) (035-037)
*Vehicle history reports and API integration*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 035 | `035-hv-home.md` | Histórico Veicular | This document explains the Vehicle History (HV) report, outlining its benefits f... | historico-veicular, vehicle-history, olx-integration, api-activation, automotive-sales |
| 036 | `036-hv-fluxo-importacao.md` | Via Importação do Anúncio | This document explains how to activate the Vehicle History feature during the ad... | olx-api, vehicle-history, ad-import, api-parameters, automotive-ads |
| 037 | `037-hv-rotas-api-hv.md` | Via Administração do HV | This document provides technical documentation for the Vehicle History API, deta... | api-reference, vehicle-history, endpoint-documentation, http-methods, integration-guide |

### 11. Real Estate - JSON Import (038-045)
*JSON integration for real estate listings*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 038 | `038-anuncio-json-real-estate-home.md` | JSON para Imóveis na OLX | This document outlines the requirements and category codes for importing real es... | olx-api, real-estate, json-import, data-integration, property-listings |
| 039 | `039-anuncio-json-real-estate.md` | Imóveis | This document outlines the requirements and category codes for importing real es... | olx-api, real-estate, json-import, listing-categories, integration-guide |
| 040 | `040-anuncio-json-real-estate-sub-apartment.md` | Importação de Anúncios via Arquivo JSON | This document outlines the specific parameters, data types, and required values ... | apartments, api-parameters, real-estate, data-schema, property-listings |
| 041 | `041-anuncio-json-real-estate-sub-house.md` | Importação de Anúncios via Arquivo JSON | This document defines the technical schema and parameter values required for sub... | api-reference, real-estate-listings, parameter-definitions, json-payload, property-metadata |
| 042 | `042-anuncio-json-real-estate-sub-commercial.md` | Importação de Anúncios via Arquivo JSON | This document outlines the specific parameters and configuration required for su... | api-parameters, real-estate-ads, json-payload, property-metadata, commerce-industry |
| 043 | `043-anuncio-json-real-estate-sub-land.md` | Importação de Anúncios via Arquivo JSON | This document outlines the specific parameters and data formatting required for ... | api-integration, real-estate-data, data-parameters, json-payload, listing-management |
| 044 | `044-anuncio-json-real-estate-sub-roomrent.md` | Importação de Anúncios via Arquivo JSON | This document specifies the mandatory parameters and JSON structure required to ... | room-rental, api-integration, category-parameters, json-payload, listing-management |
| 045 | `045-anuncio-json-real-estate-sub-season.md` | Importação de Anúncios via Arquivo JSON | This document defines the technical parameters and allowed values for listing re... | real-estate, api-integration, vacation-rentals, json-parameters, data-specification |

### 12. Real Estate - API & XML (046-057)
*API and XML integration for real estate*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 046 | `046-anuncio-api-real-estate-home.md` | Categoria de Imóveis | This document provides the specific category codes and documentation links requi... | olx-api, real-estate, listing-import, category-codes, integration-reference |
| 047 | `047-anuncio-xml-real-estate-home.md` | Documentação para a Importação via XML para Imóveis na OLX | This document provides technical instructions for importing real estate advertis... | xml-import, olx-integration, real-estate-ads, data-specification, technical-documentation |
| 048 | `048-anuncio-api-real-estate-sub-apartment.md` | Apartamentos | This document defines the technical parameters and data schema required for crea... | real-estate-api, ad-insertion, json-parameters, property-metadata, data-specification |
| 049 | `049-anuncio-api-real-estate-sub-house.md` | Casas | This document specifies the mandatory and optional parameters required for creat... | api-integration, real-estate-listings, json-payload, data-mapping, parameter-reference |
| 050 | `050-anuncio-api-real-estate-sub-commercial.md` | Comércio e indústria | This document specifies the mandatory parameters and configuration requirements ... | api-integration, property-listings, parameter-specification, json-payload, real-estate-api |
| 051 | `051-anuncio-api-real-estate-sub-land.md` | Terrenos, sítios e fazendas | This document defines the mandatory and optional parameters required for creatin... | real-estate-api, ad-listing, parameter-specification, json-payload, property-metadata |
| 052 | `052-anuncio-api-real-estate-sub-roomrent.md` | Aluguel de quartos | This document defines the specific configuration parameters and valid values req... | aluguel-de-quartos, api-parameters, room-rent-features, json-payload, ad-listing |
| 053 | `053-anuncio-api-real-estate-sub-season.md` | Temporada | This document specifies the mandatory and optional parameters required for creat... | season-rental, api-integration, json-schema, listing-parameters, property-listings |
| 054 | `054-anuncio-xml-real-estate-sub-apartment.md` | Apartamentos | This document specifies the XML parameters and mapping required to correctly lis... | xml-integration, real-estate, olx-api, data-mapping, property-listing |
| 055 | `055-anuncio-xml-real-estate-sub-house.md` | Casas | This document provides technical specifications and XML requirements for listing... | real-estate-integration, xml-schema, olx-api, property-listings, metadata-configuration |
| 056 | `056-anuncio-xml-real-estate-sub-commercial.md` | Comércio e indústria | This document provides technical specifications and mapping rules for listing co... | xml-integration, olx-platform, real-estate-api, data-mapping, commercial-property |
| 057 | `057-anuncio-xml-real-estate-sub-land.md` | Terrenos, sítios e fazendas | This document outlines the specific parameter requirements and XML structure for... | xml-integration, property-listings, data-mapping, real-estate-metadata, listing-configuration |

### 13. Autos & Vehicles - JSON (058-066)
*JSON integration for vehicle listings*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 058 | `058-anuncio-json-autos-home.md` | JSON para Veículos na OLX | This documentation provides instructions for importing vehicle advertisements to... | olx-api, json-import, vehicle-listings, data-integration, ads-automation |
| 059 | `059-anuncio-json-autos.md` | Automóveis | This manual provides technical guidelines and category codes for importing vehic... | olx-integration, json-import, vehicle-ads, category-mapping, api-documentation |
| 060 | `060-anuncio-json-autoparts-home.md` | JSON para Autopeças na OLX | This document provides technical guidelines and category codes for importing aut... | olx-integration, json-import, auto-parts, category-mapping, ad-insertion |
| 061 | `061-anuncio-json-autoparts.md` | Peças e acessórios | This document provides technical instructions for importing auto parts advertise... | json-import, olx-api, auto-parts, ad-integration, category-mapping |
| 062 | `062-anuncio-json-autoparts-sub-autos.md` | Carros, vans e utilitários | This document defines the specific parameters, category codes, and data requirem... | api-reference, automotive-category, metadata-schema, listing-parameters, data-validation |
| 063 | `063-anuncio-json-autoparts-sub-motorcycle.md` | Motos | This document outlines the required parameters and valid value mappings for list... | api-reference, motorcycle-category, data-specification, json-payload, listing-configuration |
| 064 | `064-anuncio-json-autoparts-sub-truck.md` | Caminhões | This document provides technical specifications and parameter requirements for i... | trucks, api-reference, metadata-parameters, automotive, json-payload |
| 065 | `065-anuncio-json-autoparts-sub-bus.md` | Ônibus | This document specifies the mandatory and optional parameters required for listi... | bus-subcategory, api-parameters, vehicle-parts, technical-specification, data-mapping |
| 066 | `066-anuncio-json-autoparts-sub-boat-plane.md` | Barcos e aeronaves | This document outlines the technical specifications and parameter requirements f... | boats-and-aircraft, api-parameters, listing-metadata, integration-reference, vehicle-attributes |

### 14. Autos & Vehicles - API (067-074)
*API integration for vehicle listings*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 067 | `067-anuncio-api-autos-home.md` | Categoria de Autos | This document explains how to correctly categorize and import automobile adverti... | olx-api, advertisement-import, autos-category, vehicle-listings, api-documentation |
| 068 | `068-anuncio-api-autos-car-models.md` | Listagem de Marcas e Modelos de Automóveis e Motos na OLX | This document provides instructions and API endpoints for retrieving standardize... | olx-api, vehicle-listing, api-reference, car-data, motorcycle-data |
| 069 | `069-anuncio-api-autos-sub-auto.md` | Carros, vans e utilitários | This document specifies the technical parameters and data requirements for creat... | olx-api, automotive-ads, api-parameters, vehicle-listings, data-schema |
| 070 | `070-anuncio-api-autos-sub-motorcycle.md` | Subcategoria Motos | This document provides the technical specifications and parameter requirements f... | olx-api, motorcycle-ads, api-parameters, vehicle-listings, data-validation |
| 071 | `071-anuncio-api-autos-sub-truck.md` | Subcategoria Caminhões | This document defines the technical parameters and mandatory values required for... | api-integration, truck-category, ad-listing, parameter-specification, data-mapping |
| 072 | `072-anuncio-api-autos-sub-bus.md` | Subcategoria Ônibus | This document specifies the mandatory and optional API parameters required for l... | api-integration, bus-listings, metadata-parameters, json-schema, classifieds-api |
| 073 | `073-anuncio-api-autos-sub-boat-plane.md` | Barcos e Aeronaves | This document details the specific parameters and configuration requirements for... | api-integration, parameter-definitions, boats-and-aircraft, data-schema, listing-configuration |
| 074 | `074-anuncio-api-autoparts-home.md` | Categoria de Autopeças | This document outlines the category IDs and subcategory parameters required for ... | auto-parts, category-mapping, olx-api, listing-import, vehicle-subcategories |

### 15. Lead Descriptions - Autos (075-077)
*Lead field definitions for automotive categories*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 075 | `075-lead-descriptions-autos-sub-auto.md` | Carros, vans e utilitários | This document defines the schema and allowed values for the adsInfo object field... | olx-api, ads-info, vehicle-data, field-definitions, api-reference |
| 076 | `076-lead-descriptions-autos-sub-motorcycle.md` | Motos | This document defines the schema and valid values for the adsInfo object when pr... | olx-api, motorcycle-listings, api-reference, adsinfo-schema, data-types |
| 077 | `077-lead-descriptions-autos-sub-truck.md` | Caminhões | This document specifies the schema and value mappings for the adsInfo field with... | api-reference, truck-listings, metadata-fields, data-specification, lead-integration |

### 16. Agro & Industry (078-081)
*Agricultural and industrial equipment listings*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 078 | `078-anuncio-json-agro-home.md` | Agro e Indústria | This technical manual provides instructions and category codes for importing adv... | olx-api, json-import, advertisement-mapping, agro-industry, integration-guide |
| 079 | `079-anuncio-api-agro-home.md` | Categoria de Agro e Indústria | This document provides the specific subcategory IDs and parameter requirements f... | olx-api, category-mapping, agriculture-industry, listing-import, subcategory-ids |
| 080 | `080-anuncio-json-agro.md` | Agro e Indústria | This document provides technical instructions and category codes for importing a... | olx-api, json-import, agro-industry, ad-integration, category-codes |
| 081 | `081-anuncio-api-agro-industrial-production.md` | Subcategoria Máquinas para produção industrial | This document outlines the required parameters and category codes for listing it... | api-integration, industrial-machinery, category-parameters, json-payload, listing-configuration |

### 17. Electronics (082-083)
*Electronics and cell phone listings*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 082 | `082-anuncio-api-electronics-home.md` | Categoria de Celulares e Telefonia | This document provides technical instructions for importing advertisements into ... | olx-api, advertisement-import, mobile-phones, category-mapping, listing-parameters |
| 083 | `083-anuncio-api-electronics-cellphone-models.md` | Listagem de Marcas e Modelos de Celulares e Smartphones na OLX | This document outlines the API endpoints and request formats for retrieving list... | olx-api, mobile-phones, smartphones, api-documentation, brand-models |

### 18. Deprecated APIs (084-087)
*Legacy and deprecated API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 084 | `084-renewals-renewals-deprecated.md` | Renovação de Anúncios | This document describes the API endpoint for programmatically renewing expired a... | olx-api, ad-renewal, patch-request, ads-management, integration |
| 085 | `085-destaque-bumps-get-deprecated.md` | Consulta de anúncios destacados (deprecated) | This document describes the legacy API endpoint for querying advertisement highl... | olx-api, ad-highlights, bumps-api, legacy-version, endpoint-reference |
| 086 | `086-destaque-bumps-put-deprecated.md` | Aplicação de destaque em anúncio (deprecated) | This document describes the deprecated API endpoint for applying highlights to a... | olx-api, ad-highlighting, bump-feature, http-put, error-handling |
| 087 | `087-anuncio-api-published-ads-deprecated.md` | Listagem de Publicação | This document describes a deprecated API endpoint for retrieving a list of activ... | olx-ads, api-endpoint, deprecated-api, published-ads, ad-retrieval |

---

## Quick Reference by Topic

| Topic | File Range | Description |
|-------|------------|-------------|
| **Authentication** | 006-008 | OAuth, rate limits, security |
| **Ad Management** | 009-016 | CRUD operations, status checks |
| **Real Estate** | 038-057 | JSON and XML for properties |
| **Vehicles** | 058-074 | Cars, trucks, motorcycles, parts |
| **Leads & Chat** | 022-029 | CRM integration, messaging |
| **Webhooks** | 017-021 | Real-time notifications |
| **Deprecated** | 084-087 | Legacy endpoints |

---

## Learning Path

### Level 1: Foundation (Start Here)
- **Read files 001-005**: Portal overview, FAQ, and getting started guides
- **Understand**: Basic concepts, integration methods (API, JSON, XML)

### Level 2: Authentication & Core Concepts
- **Read files 006-008**: OAuth authentication and rate limiting
- **Master**: Security, access tokens, API limits

### Level 3: Core API Operations
- **Read files 009-016**: Ad import, status checks, operations
- **Practice**: Creating, updating, deleting ads via API

### Level 4: Integration Features
- **Read files 017-037**: Webhooks, chat, leads, highlights, renewals
- **Implement**: Real-time notifications, messaging, lead management

### Level 5: Category-Specific Integration
- **Read files 038-083**: Real estate, vehicles, agro, electronics
- **Deep Dive**: Category-specific parameters and requirements

### Level 6: Reference & Support
- **Read files 084-087**: Deprecated endpoints and migration guides

---

## File Naming Convention

All documentation files follow the pattern: `NNN-original-name.md`

- `NNN`: 3-digit sequential number (001-087)
- `original-name`: Original filename preserved for readability
- Files are organized in logical learning sequence

---

## API Categories Overview

### Advertisement Management (`anuncio`)
- **Home/Docs**: 003-005
- **API Reference**: 004, 009-013, 067-074
- **JSON Import**: 005, 038-045, 058-066, 078-080
- **XML Import**: 047, 054-057

### Integration Features
- **Chat**: 007, 022-024
- **Leads**: 025-029, 075-077
- **Webhooks**: 017-021
- **Highlights**: 030-033
- **Renewals**: 034

### Product Categories
- **Real Estate**: 038-057
- **Vehicles (Autos)**: 058-074
- **Auto Parts**: 060-066, 074
- **Agro & Industry**: 078-081
- **Electronics**: 082-083

### Support & FAQ
- **General FAQ**: 002, 008, 014-016
- **Support**: 029

---

## Integration Methods

### 1. REST API
Direct API integration using HTTP endpoints with OAuth 2.0 authentication.
- **Primary**: Files 009-013, 067-074
- **Authentication**: Files 006-007

### 2. JSON Import
Bulk ad import using JSON files for various categories.
- **Format**: JSON files uploaded to OLX
- **Categories**: Real estate (038-045), Vehicles (058-066), Agro (078-080)

### 3. XML Import
Legacy XML format for real estate listings.
- **Format**: XML files
- **Categories**: Real estate only (047, 054-057)

---

## Key Integration Points

### Authentication
- **OAuth 2.0**: File 006 (ads), File 007 (chat)
- **Scopes**: Different permissions for ads, chat, webhooks

### Webhooks
- **Configuration**: File 018
- **Models**: File 019
- **Ad Status**: File 020

### Lead Management
- **Delivery**: File 027
- **Enriched Data**: File 028
- **Field Definitions**: Files 075-077

### Chat Integration
- **OAuth**: File 007
- **Receiving**: File 023
- **Sending**: File 024

---

## Deprecated Endpoints

The following endpoints are deprecated and should not be used for new integrations:

| Endpoint | File | Replacement |
|----------|------|-------------|
| Renewals (deprecated) | 084 | File 034 |
| Bumps GET (deprecated) | 085 | File 032 |
| Bumps PUT (deprecated) | 086 | File 033 |
| Published Ads (deprecated) | 087 | File 012 |

---

## Additional Resources

- **Source**: https://developers.olx.com.br/
- **Total Documents**: 87
- **Categories**: 18
- **Organization Date**: {metadata['organization']['organized_at'][:10]}

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression from basic concepts to advanced integration patterns.*
