---
title: Options de Testing
url: https://docs.bmad-method.org/fr/reference/testing/
source: sitemap
fetched_at: 2026-04-08T11:30:59.48460441-03:00
rendered_js: false
word_count: 859
summary: 'This document compares two approaches to testing: an integrated QA workflow for quick test generation in smaller projects and the standalone Test Architect module (TEA) designed for comprehensive, enterprise-grade quality strategies. It details the steps of the integrated QA process versus the advanced planning and risk management capabilities offered by TEA.'
tags:
    - qa-workflow
    - test-strategy
    - enterprise-testing
    - e2e-testing
    - atdd
    - risk-based-testing
category: guide
---

BMad propose deux approches de test : un workflow QA[1](#user-content-fn-1) intégré pour une génération rapide de tests et un module Test Architect installable pour une stratégie de test de qualité entreprise.

FacteurQA IntégréModule TEA**Idéal pour**Projets petits et moyens, couverture rapideGrands projets, domaines réglementés ou complexes**Installation**Rien à installer — inclus dans BMMInstaller séparément via `npx bmad-method install`**Approche**Générer les tests rapidement, itérer ensuitePlanifier d’abord, puis générer avec traçabilité**Types de tests**Tests API et E2EAPI, E2E, ATDD[2](#user-content-fn-2), NFR, et plus**Stratégie**Chemin nominal + cas limites critiquesPriorisation basée sur les risques (P0-P3)**Nombre de workflows**1 (Automate)9 (conception, ATDD, automatisation, revue, traçabilité, et autres)

Le workflow QA intégré (`bmad-qa-generate-e2e-tests`) fait partie du module BMM (suite Agile), disponible via l’agent Developer. Il génère rapidement des tests fonctionnels en utilisant le framework de test existant de votre projet — aucune configuration ni installation supplémentaire requise.

**Déclencheur :** `QA` (via l’agent Developer) ou `bmad-qa-generate-e2e-tests`

### Ce que le Workflow QA Fait

[Section intitulée « Ce que le Workflow QA Fait »](#ce-que-le-workflow-qa-fait)

Le workflow QA exécute un processus unique (Automate) qui parcourt cinq étapes :

1. **Détecte le framework de test** — analyse `package.json` et les fichiers de test existants pour identifier votre framework (Jest, Vitest, Playwright, Cypress, ou tout runner standard). Si aucun n’existe, analyse la pile technologique du projet et en suggère un.
2. **Identifie les fonctionnalités** — demande ce qu’il faut tester ou découvre automatiquement les fonctionnalités dans le codebase.
3. **Génère les tests API** — couvre les codes de statut, la structure des réponses, le chemin nominal, et 1-2 cas d’erreur.
4. **Génére les tests E2E** — couvre les parcours utilisateur avec des localisateurs sémantiques et des assertions sur les résultats visibles.
5. **Exécute et vérifie** — lance les tests générés et corrige immédiatement les échecs.

Le workflow QA produit un résumé de test sauvegardé dans le dossier des artefacts d’implémentation de votre projet.

Les tests générés suivent une philosophie “simple et maintenable” :

- **APIs standard du framework uniquement** — pas d’utilitaires externes ni d’abstractions personnalisées
- **Localisateurs sémantiques** pour les tests UI (rôles, labels, texte plutôt que sélecteurs CSS)
- **Tests indépendants** sans dépendances d’ordre
- **Pas d’attentes ou de sleeps codés en dur**
- **Descriptions claires** qui se lisent comme de la documentation fonctionnelle

### Quand Utiliser le QA Intégré

[Section intitulée « Quand Utiliser le QA Intégré »](#quand-utiliser-le-qa-int%C3%A9gr%C3%A9)

- Couverture de test rapide pour une fonctionnalité nouvelle ou existante
- Automatisation de tests accessible aux débutants sans configuration avancée
- Patterns de test standards que tout développeur peut lire et maintenir
- Projets petits et moyens où une stratégie de test complète n’est pas nécessaire

## Module Test Architect (TEA)

[Section intitulée « Module Test Architect (TEA) »](#module-test-architect-tea)

TEA est un module autonome qui fournit un agent expert (Murat) et neuf workflows structurés pour des tests de qualité entreprise. Il va au-delà de la génération de tests pour inclure la stratégie de test, la planification basée sur les risques, les murs de qualité et la traçabilité des exigences.

- **Documentation :** [TEA Module Docs](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)
- **Installation :** `npx bmad-method install` et sélectionnez le module TEA
- **npm :** [`bmad-method-test-architecture-enterprise`](https://www.npmjs.com/package/bmad-method-test-architecture-enterprise)

WorkflowObjectifTest DesignCréer une stratégie de test complète liée aux exigencesATDDDéveloppement piloté par les tests d’acceptation avec critères des parties prenantesAutomateGénérer des tests avec des patterns et utilitaires avancésTest ReviewValider la qualité et la couverture des tests par rapport à la stratégieTraceabilityRemonter les tests aux exigences pour l’audit et la conformitéNFR AssessmentÉvaluer les exigences non-fonctionnelles (performance, sécurité)CI SetupConfigurer l’exécution des tests dans les pipelines d’intégration continueFramework ScaffoldingConfigurer l’infrastructure de test et la structure du projetRelease GatePrendre des décisions de livraison go/no-go basées sur les données

TEA supporte également la priorisation basée sur les risques P0-P3 et des intégrations optionnelles avec Playwright Utils et les outils MCP.

- Projets nécessitant une traçabilité des exigences ou une documentation de conformité
- Équipes ayant besoin d’une priorisation des tests basée sur les risques sur plusieurs fonctionnalités
- Environnements entreprise avec des murs de qualité formels avant livraison
- Domaines complexes où la stratégie de test doit être planifiée avant d’écrire les tests
- Projets ayant dépassé l’approche à workflow unique du QA intégré

Le workflow Automate du QA intégré apparaît dans la Phase 4 (Implémentation) de la carte de workflow méthode BMad. Il est conçu pour s’exécuter **après qu’un epic complet soit terminé** — une fois que toutes les stories d’un epic ont été implémentées et revues. Une séquence typique :

1. Pour chaque story de l’epic : implémenter avec Dev Story (`DS`), puis valider avec Code Review (`CR`)
2. Après la fin de l’epic : générer les tests avec `QA` (via l’agent Developer) ou le workflow Automate de TEA
3. Lancer la rétrospective (`bmad-retrospective`) pour capturer les leçons apprises

Le workflow QA travaille directement à partir du code source sans charger les documents de planification (PRD, architecture). Les workflows TEA peuvent s’intégrer avec les artefacts de planification en amont pour la traçabilité.

Pour en savoir plus sur la place des tests dans le processus global, consultez la [Carte des Workflows](https://docs.bmad-method.org/fr/reference/workflow-map/).

1. QA (Quality Assurance) : assurance qualité, ensemble des processus et activités visant à garantir que le produit logiciel répond aux exigences de qualité définies. [↩](#user-content-fnref-1)
2. ATDD (Acceptance Test-Driven Development) : méthode de développement où les tests d’acceptation sont écrits avant le code, en collaboration avec les parties prenantes pour définir les critères de réussite. [↩](#user-content-fnref-2)