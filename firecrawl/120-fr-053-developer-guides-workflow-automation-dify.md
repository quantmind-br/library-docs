---
title: Firecrawl + Dify - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/workflow-automation/dify
source: sitemap
fetched_at: 2026-03-23T07:38:41.525701-03:00
rendered_js: false
word_count: 211
summary: This document provides an overview of integrating the Firecrawl plugin with the Dify platform to enable web scraping and crawling capabilities within AI workflows and agent-based applications.
tags:
    - dify
    - firecrawl
    - web-scraping
    - llm-applications
    - data-extraction
    - ai-agents
    - workflow-automation
category: guide
---

## Aperçu de l’intégration Dify

Dify est une plateforme open source de développement d’applications LLM. Le plugin officiel Firecrawl permet l’exploration et le scraping du web directement dans vos workflows d’IA.

## Bien démarrer

## Modèles d’utilisation

- Applications Chatflow
- Applications Workflow
- Applications Agent

**Intégration visuelle de pipeline**

1. Ajoutez le nœud Firecrawl à votre pipeline
2. Sélectionnez l’action (Map, Crawl, Scrape)
3. Définissez les variables d’entrée
4. Exécutez le pipeline de manière séquentielle

**Exemple de flux :**

```
Saisie utilisateur → Firecrawl (Scrape) → Traitement par LLM → Réponse
```

**Traitement automatisé des données**Créez des workflows multi-étapes avec :

- Scraping planifié
- Transformation des données
- Stockage en base de données
- Notifications

**Exemple de flux :**

```
Déclencheur planifié → Firecrawl (Crawl) → Traitement des données → Stockage
```

**Accès web propulsé par l’IA**Donnez aux agents des capacités de scraping web en temps réel :

1. Ajoutez l’outil Firecrawl à l’agent
2. L’agent décide de manière autonome quand scraper
3. Le LLM analyse le contenu extrait
4. L’agent fournit des réponses étayées

**Cas d’usage :** Agents du support client s’appuyant sur une documentation à jour

## Cas d’usage courants

## Actions Firecrawl

OutilDescriptionIdéal pour**Scrape**Extraction de données d’une page uniqueCapture rapide de contenu**Crawl**Exploration récursive multi‑pagesExtraction complète d’un site**Map**Découverte d’URL et cartographie du siteAnalyse SEO, listes d’URL**Crawl Job**Gestion de tâches asynchronesOpérations de longue durée

## Bonnes pratiques

## Dify vs autres plateformes

FonctionnalitéDifyMakeZapiern8n**Type**Plateforme d’applications LLMAutomatisation de workflowsAutomatisation de workflowsAutomatisation de workflows**Idéal pour**Agents IA et chatbotsWorkflows visuelsAutomatisations rapidesContrôle développeur**Tarification**Open source + CloudÀ l’opérationÀ la tâcheForfait mensuel**Natif IA**OuiPartielPartielPartiel**Auto‑hébergé**OuiNonNonOui