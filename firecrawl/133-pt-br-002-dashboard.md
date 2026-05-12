---
title: Painel | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/dashboard
source: sitemap
fetched_at: 2026-03-23T07:26:22.194462-03:00
rendered_js: false
word_count: 429
summary: This document provides an overview of the Firecrawl dashboard features, including management of API keys, team roles, usage monitoring, and the built-in playground for testing endpoints.
tags:
    - dashboard-overview
    - account-management
    - team-roles
    - api-keys
    - web-scraping
    - usage-tracking
category: guide
---

O [painel do Firecrawl](https://www.firecrawl.dev/app) é onde você gerencia sua conta, testa endpoints e monitora o uso. Abaixo está uma visão geral rápida de cada seção.

## Playground

O playground permite que você teste os endpoints do Firecrawl diretamente no navegador antes de integrá-los ao seu código.

- [**Scrape**](https://www.firecrawl.dev/app/playground?endpoint=scrape) — Extraia conteúdo de uma única página.
- [**Search**](https://www.firecrawl.dev/app/playground?endpoint=search) — Faça uma busca na web e obtenha resultados extraídos.
- [**Crawl**](https://www.firecrawl.dev/app/playground?endpoint=crawl) — Faça o rastreamento de um site inteiro e extraia conteúdo de cada página.
- [**Map**](https://www.firecrawl.dev/app/playground?endpoint=map) — Descubra todas as URLs de um site.

## Navegador

[Interaja com a web](https://www.firecrawl.dev/app/browser) por meio de uma sessão de navegador ao vivo. Você pode criar perfis persistentes, executar ações e tirar capturas de tela — recursos úteis para páginas que exigem autenticação ou interação complexa.

## Agent

O [Agent](https://www.firecrawl.dev/app/agent) é uma ferramenta de pesquisa com IA que pode navegar pela web de forma autônoma, seguir links e extrair dados estruturados com base em um prompt.

## Logs de atividade

[Logs de atividade](https://www.firecrawl.dev/app/logs) mostram o histórico das suas requisições recentes à API, incluindo status, duração e credits consumidos.

## Uso

A página de [Uso](https://www.firecrawl.dev/app/usage) mostra seu consumo de créditos ao longo do tempo e os totais atuais do ciclo de cobrança.

## Chaves de API

Na página [Chaves de API](https://www.firecrawl.dev/app/api-keys), você pode criar, ver e revogar chaves de API da sua equipe.

## Configurações

A página [Configurações](https://www.firecrawl.dev/app/settings) tem três abas:

- **Equipe** — Convide membros, atribua funções e gerencie sua equipe. Veja [Gerenciamento de equipe e funções](#team-management--roles) abaixo.
- **Cobrança** — Veja seu plan atual, faturas, configurações de auto-recharge e aplique cupons. Veja também [Cobrança](https://docs.firecrawl.dev/pt-BR/billing).
- **Avançado** — Segredo de assinatura do Webhook e exclusão da equipe.

* * *

## Gerenciamento de equipe & roles

O Firecrawl permite que você convide colegas de equipe para colaborar em uma conta compartilhada. Na aba **equipe**, em configuração, você pode convidar membros, atribuir funções e gerenciar sua equipe.

### Funções

Cada membro da equipe recebe uma de duas funções: **Admin** ou **Member**. Você escolhe a função ao enviar um convite.

PermissãoAdminMember**Geral**Usar as API keys da equipe e os recursos compartilhados✓✓**Gerenciamento da equipe**Ver a lista de membros da equipe✓✓Sair da equipe✓✓Convidar novos membros da equipe✓✗Remover membros da equipe✓✗Alterar a função de um membro✓✗Revogar convites pendentes✓✗Editar o nome da equipe✓✗**Cobrança**Ver faturas e uso✓✓Aplicar cupons de crédito✓✓Gerenciar a assinatura e o portal de cobrança✓✗**Configurações**Ver o segredo de assinatura do Webhook✓✓Gerar um novo segredo de assinatura do Webhook✓✗Excluir a equipe✓✗

Em resumo, **Admins** têm controle total sobre o gerenciamento da equipe, a cobrança e as configurações, enquanto **Members** podem usar os recursos da equipe, ver o uso e aplicar cupons, mas não podem alterar a equipe nem a assinatura.