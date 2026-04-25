---
title: Gérer le contexte du projet
url: https://docs.bmad-method.org/fr/how-to/project-context/
source: sitemap
fetched_at: 2026-04-08T11:30:43.765044029-03:00
rendered_js: false
word_count: 478
summary: Ce document explique comment utiliser le fichier `project-context.md` pour s'assurer que les agents d'IA respectent de manière cohérente les préférences techniques et les règles spécifiques à un projet tout au long des workflows de développement.
tags:
    - gestion-de-contexte
    - agents-ia
    - règles-d-implémentation
    - documentation-projet
    - best-practices
category: guide
---

Utilisez le fichier `project-context.md` pour garantir que les agents IA respectent les préférences techniques et les règles d’implémentation de votre projet tout au long des workflows. Pour vous assurer qu’il est toujours disponible, vous pouvez également ajouter la ligne `Le contexte et les conventions importantes du projet se trouvent dans [chemin vers le contexte du projet]/project-context.md` à votre fichier de contexte ou de règles permanentes (comme `AGENTS.md`).

## Quand utiliser cette fonctionnalité

[Section intitulée « Quand utiliser cette fonctionnalité »](#quand-utiliser-cette-fonctionnalit%C3%A9)

- Vous avez des préférences techniques fortes avant de commencer l’architecture
- Vous avez terminé l’architecture et souhaitez consigner les décisions pour l’implémentation
- Vous travaillez sur une base de code existante avec des patterns établis
- Vous remarquez que les agents prennent des décisions incohérentes entre les stories

## Étape 1 : Choisissez votre approche

[Section intitulée « Étape 1 : Choisissez votre approche »](#%C3%A9tape-1--choisissez-votre-approche)

**Création manuelle** — Idéal lorsque vous savez exactement quelles règles vous souhaitez documenter

**Génération après l’architecture** — Idéal pour capturer les décisions prises lors du solutioning

**Génération pour les projets existants** — Idéal pour découvrir les patterns dans les bases de code existantes

## Étape 2 : Créez le fichier

[Section intitulée « Étape 2 : Créez le fichier »](#%C3%A9tape-2--cr%C3%A9ez-le-fichier)

### Option A : Création manuelle

[Section intitulée « Option A : Création manuelle »](#option-a--cr%C3%A9ation-manuelle)

Créez le fichier à l’emplacement `_bmad-output/project-context.md` :

```bash

mkdir-p_bmad-output
touch_bmad-output/project-context.md
```

Ajoutez votre pile technologique et vos règles d’implémentation :

```markdown

---
project_name: 'MonProjet'
user_name: 'VotreNom'
date: '2026-02-15'
sections_completed: ['technology_stack', 'critical_rules']
---
# Contexte de Projet pour Agents IA
## Pile Technologique & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State : Zustand
- Tests : Vitest, Playwright
- Styles : Tailwind CSS
## Règles d'Implémentation Critiques
**TypeScript :**
- Mode strict activé, pas de types `any`
- Utiliser `interface` pour les API publiques, `type` pour les unions
**Organisation du Code :**
- Composants dans `/src/components/` avec tests co-localisés
- Les appels API utilisent le singleton `apiClient` — jamais de fetch direct
**Tests :**
- Tests unitaires axés sur la logique métier
- Tests d'intégration utilisent MSW pour le mock API
```

### Option B : Génération après l’architecture

[Section intitulée « Option B : Génération après l’architecture »](#option-b--g%C3%A9n%C3%A9ration-apr%C3%A8s-larchitecture)

Exécutez le workflow dans une nouvelle conversation :

```bash

bmad-generate-project-context
```

Le workflow analyse votre document d’architecture et vos fichiers projet pour générer un fichier de contexte qui capture les décisions prises.

### Option C : Génération pour les projets existants

[Section intitulée « Option C : Génération pour les projets existants »](#option-c--g%C3%A9n%C3%A9ration-pour-les-projets-existants)

Pour les projets existants, exécutez :

```bash

bmad-generate-project-context
```

Le workflow analyse votre base de code pour identifier les conventions, puis génère un fichier de contexte que vous pouvez réviser et affiner.

## Étape 3 : Vérifiez le contenu

[Section intitulée « Étape 3 : Vérifiez le contenu »](#%C3%A9tape-3--v%C3%A9rifiez-le-contenu)

Révisez le fichier généré et assurez-vous qu’il capture :

- Les versions correctes des technologies
- Vos conventions réelles (pas les bonnes pratiques génériques)
- Les règles qui évitent les erreurs courantes
- Les patterns spécifiques aux frameworks

Modifiez manuellement pour ajouter les éléments manquants ou supprimer les inexactitudes.

Un fichier `project-context.md` qui :

- Garantit que tous les agents suivent les mêmes conventions
- Évite les décisions incohérentes entre les stories
- Capture les décisions d’architecture pour l’implémentation
- Sert de référence pour les patterns et règles de votre projet

<!--THE END-->

- [**Explication du contexte projet**](https://docs.bmad-method.org/fr/explanation/project-context/) — En savoir plus sur son fonctionnement
- [**Carte des workflows**](https://docs.bmad-method.org/fr/reference/workflow-map/) — Voir quels workflows chargent le contexte projet