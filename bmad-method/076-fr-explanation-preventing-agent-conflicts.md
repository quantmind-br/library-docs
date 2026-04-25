---
title: Prévention des conflits entre agents
url: https://docs.bmad-method.org/fr/explanation/preventing-agent-conflicts/
source: sitemap
fetched_at: 2026-04-08T11:30:25.473527599-03:00
rendered_js: false
word_count: 470
summary: This document explains that establishing an architecture serves to prevent contradictory technical decisions when multiple AI agents build a system by providing shared standards. It details how architectural artifacts like ADRs, FR/NFRs, and coding conventions guide consistency across API styles, database design, and state management.
tags:
    - system-architecture
    - ai-agents
    - technical-standards
    - adr
    - design-patterns
    - consistency
category: guide
---

Lorsque plusieurs agents IA implémentent différentes parties d’un système, ils peuvent prendre des décisions techniques contradictoires. La documentation d’architecture prévient cela en établissant des standards partagés.

## Types de conflits courants

[Section intitulée « Types de conflits courants »](#types-de-conflits-courants)

### Conflits de style d’API

[Section intitulée « Conflits de style d’API »](#conflits-de-style-dapi)

Sans architecture :

- L’agent A utilise REST avec `/users/{id}`
- L’agent B utilise des mutations GraphQL
- Résultat : Patterns d’API incohérents, consommateurs confus

Avec architecture :

- L’ADR[1](#user-content-fn-1) spécifie : « Utiliser GraphQL pour toute communication client-serveur »
- Tous les agents suivent le même pattern

### Conflits de conception de base de données

[Section intitulée « Conflits de conception de base de données »](#conflits-de-conception-de-base-de-donn%C3%A9es)

Sans architecture :

- L’agent A utilise des noms de colonnes en snake\_case
- L’agent B utilise des noms de colonnes en camelCase
- Résultat : Schéma incohérent, requêtes illisibles

Avec architecture :

- Un document de standards spécifie les conventions de nommage
- Tous les agents suivent les mêmes patterns

### Conflits de gestion d’état

[Section intitulée « Conflits de gestion d’état »](#conflits-de-gestion-d%C3%A9tat)

Sans architecture :

- L’agent A utilise Redux pour l’état global
- L’agent B utilise React Context
- Résultat : Multiples approches de gestion d’état, complexité

Avec architecture :

- L’ADR spécifie l’approche de gestion d’état
- Tous les agents implémentent de manière cohérente

### 1. Décisions explicites via les ADR[1](#user-content-fn-1)

[Section intitulée « 1. Décisions explicites via les ADR1 »](#1-d%C3%A9cisions-explicites-via-les-adr1)

Chaque choix technologique significatif est documenté avec :

- Contexte (pourquoi cette décision est importante)
- Options considérées (quelles alternatives existent)
- Décision (ce qui a été choisi)
- Justification (pourquoi cela a-t-il été choisi)
- Conséquences (compromis acceptés)

### 2. Guidance spécifique aux FR/NFR[2](#user-content-fn-2)

[Section intitulée « 2. Guidance spécifique aux FR/NFR2 »](#2-guidance-sp%C3%A9cifique-aux-frnfr2)

L’architecture associe chaque exigence fonctionnelle à une approche technique :

- FR-001 : Gestion des utilisateurs → Mutations GraphQL
- FR-002 : Application mobile → Requêtes optimisées

### 3. Standards et conventions

[Section intitulée « 3. Standards et conventions »](#3-standards-et-conventions)

Documentation explicite de :

- La structure des répertoires
- Les conventions de nommage
- L’organisation du code
- Les patterns de test

## L’architecture comme contexte partagé

[Section intitulée « L’architecture comme contexte partagé »](#larchitecture-comme-contexte-partag%C3%A9)

Considérez l’architecture comme le contexte partagé que tous les agents lisent avant d’implémenter :

```text

PRD : "Que construire"
↓
Architecture : "Comment le construire"
↓
L'agent A lit l'architecture → implémente l'Epic 1
L'agent B lit l'architecture → implémente l'Epic 2
L'agent C lit l'architecture → implémente l'Epic 3
↓
Résultat : Implémentation cohérente
```

Décisions courantes qui préviennent les conflits :

SujetExemple de décisionStyle d’APIGraphQL vs REST vs gRPCBase de donnéesPostgreSQL vs MongoDBAuthentificationJWT vs SessionsGestion d’étatRedux vs Context vs ZustandStylingCSS Modules vs Tailwind vs Styled ComponentsTestsJest + Playwright vs Vitest + Cypress

## Anti-patterns à éviter

[Section intitulée « Anti-patterns à éviter »](#anti-patterns-%C3%A0-%C3%A9viter)

1. ADR (Architecture Decision Record) : document qui consigne une décision d’architecture, son contexte, les options envisagées, le choix retenu et ses conséquences, afin d’assurer la traçabilité et la compréhension des décisions techniques dans le temps. [↩](#user-content-fnref-1) [↩2](#user-content-fnref-1-2)
2. FR / NFR (Functional / Non-Functional Requirement) : exigences décrivant respectivement **ce que le système doit faire** (fonctionnalités, comportements attendus) et **comment il doit le faire** (contraintes de performance, sécurité, fiabilité, ergonomie, etc.). [↩](#user-content-fnref-2)