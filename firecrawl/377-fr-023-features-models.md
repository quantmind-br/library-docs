---
title: Modèles d'agents | Firecrawl
url: https://docs.firecrawl.dev/fr/features/models
source: sitemap
fetched_at: 2026-03-23T07:23:55.017023-03:00
rendered_js: false
word_count: 348
summary: Ce document présente les deux modèles d'IA disponibles pour Firecrawl Agent, Spark-1-Mini et Spark-1-Pro, en aidant les utilisateurs à choisir l'option optimale selon leurs besoins de précision, de complexité et de budget.
tags:
    - firecrawl-agent
    - model-selection
    - data-extraction
    - ai-models
    - cost-optimization
    - api-configuration
category: concept
---

Firecrawl Agent propose deux modèles optimisés pour différents cas d’usage. Choisissez le modèle adapté en fonction de la complexité de votre extraction et de vos contraintes budgétaires.

## Modèles disponibles

ModèleCoûtPrécisionIdéal pour`spark-1-mini`**60 % moins cher**StandardLa plupart des tâches (par défaut)`spark-1-pro`StandardPlus élevéeRecherche complexe, extractions à fort enjeu

## Spark 1 Mini (par défaut)

`spark-1-mini` est notre modèle efficace, idéal pour les tâches d’extraction de données simples. **Utilisez Mini lorsque :**

- Vous extrayez des données simples (coordonnées, tarifs, etc.)
- Vous travaillez avec des sites web bien structurés
- La maîtrise des coûts est une priorité
- Vous exécutez des tâches d’extraction à grande échelle

**Exemples d’utilisation :**

- Extraire les prix des produits à partir de sites e-commerce
- Collecter les coordonnées à partir de pages d’entreprise
- Récupérer des métadonnées basiques depuis des articles
- Effectuer des recherches de données simples

## Spark 1 Pro

`spark-1-pro` est notre modèle phare, conçu pour une précision maximale sur les tâches d’extraction complexes. **Utilisez Pro lorsque :**

- Effectuer une analyse concurrentielle complexe
- Extraire des données qui nécessitent un raisonnement poussé
- La précision est critique pour votre cas d’utilisation
- Traiter des données ambiguës ou difficiles à trouver

**Exemples de cas d’utilisation :**

- Analyse concurrentielle sur plusieurs domaines
- Tâches de recherche complexes nécessitant un raisonnement approfondi
- Extraction d’informations nuancées à partir de multiples sources
- Collecte d’informations stratégiques critiques pour l’entreprise

## Spécifier un modèle

Passez le paramètre `model` pour choisir le modèle à utiliser :

## Comparaison des modèles

FonctionnalitéSpark 1 MiniSpark 1 Pro**Coût**60 % moins cherStandard**Précision**StandardPlus élevée**Vitesse**RapideRapide**Idéal pour**La plupart des tâchesTâches complexes**Raisonnement**StandardAvancé**Multidomaine**BonExcellent

## Tarification par modèle

Les deux modèles utilisent une tarification dynamique basée sur des crédits, qui s’adapte à la complexité de la tâche :

- **Spark 1 Mini** : utilise environ 60 % de crédits en moins que Pro pour des tâches équivalentes
- **Spark 1 Pro** : consommation de crédits standard pour une précision maximale

## Choisir le modèle adapté

```
                    ┌─────────────────────────────────┐
                    │   Quel type de tâche ?          │
                    └─────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  Simple/Direct  │           │ Complexe/Recherche│
          │  extraction     │           │ multi-domaine   │
          └─────────────────┘           └─────────────────┘
                    │                             │
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  spark-1-mini   │           │  spark-1-pro    │
          │  (60 % moins cher)│         │  (précision sup.)│
          └─────────────────┘           └─────────────────┘
```

## Référence de l’API

Consultez la [référence de l’API Agent](https://docs.firecrawl.dev/fr/api-reference/endpoint/agent) pour la documentation complète des paramètres. Vous vous demandez quel modèle utiliser ? Écrivez à [help@firecrawl.com](mailto:help@firecrawl.com).

> Êtes-vous un agent d’IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.