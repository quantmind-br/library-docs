---
title: Agents
url: https://docs.bmad-method.org/fr/reference/agents/
source: sitemap
fetched_at: 2026-04-08T11:30:51.605538226-03:00
rendered_js: false
word_count: 404
summary: This document lists the five default BMM agents installed via BMad and details how they can be invoked using skill IDs and menu triggers. It differentiates between workflow triggers (which require no arguments) and conversational triggers (which require descriptive input).
tags:
    - bmm-agents
    - skill-ids
    - workflow-triggers
    - menu-triggers
    - agent-invocation
    - system-reference
category: reference
---

Cette page liste les cinq agents BMM (suite Agile) par défaut installés avec la méthode BMad, ainsi que leurs identifiants de skill, déclencheurs de menu et workflows principaux. Chaque agent est invoqué en tant que skill.

- Chaque agent est disponible en tant que skill, généré par l’installateur. L’identifiant de skill (par exemple, `bmad-analyst`) est utilisé pour invoquer l’agent.
- Les déclencheurs sont les codes courts de menu (par exemple, `BP`) et les correspondances approximatives affichés dans chaque menu d’agent.
- La génération de tests QA est gérée par le skill de workflow `bmad-qa-generate-e2e-tests`. L’architecte de tests complet (TEA) se trouve dans son propre module.

AgentIdentifiant de skillDéclencheursWorkflows principauxAnalyste (Mary)`bmad-analyst``BP`, `MR`, `DR`, `TR`, `CB`, `DP`Brainstorming du projet, Recherche marché/domaine/technique, Création du brief[1](#user-content-fn-1), Documentation du projetArchitecte (Winston)`bmad-architect``CA`, `IR`Créer l’architecture, Préparation à l’implémentationDéveloppeur (Amelia)`bmad-dev``DS`, `QD`, `CR`Dev Story, Quick Dev, Code ReviewDesigner UX (Sally)`bmad-ux-designer``CU`Création du design UX[2](#user-content-fn-2)Rédacteur Technique (Paige)`bmad-tech-writer``DP`, `WD`, `US`, `MG`, `VD`, `EC`Documentation du projet, Rédaction de documents, Mise à jour des standards, Génération de diagrammes Mermaid, Validation de documents, Explication de concepts

Les déclencheurs de menu d’agent utilisent deux types d’invocation différents. Connaître le type utilisé par un déclencheur vous aide à fournir la bonne entrée.

### Déclencheurs de workflow (aucun argument nécessaire)

[Section intitulée « Déclencheurs de workflow (aucun argument nécessaire) »](#d%C3%A9clencheurs-de-workflow-aucun-argument-n%C3%A9cessaire)

La plupart des déclencheurs chargent un fichier de workflow structuré. Tapez le code du déclencheur et l’agent démarre le workflow, vous demandant de saisir les informations à chaque étape.

Exemples : `BP` (Brainstorm Project), `CA` (Create Architecture), `CU` (Create UX Design)

### Déclencheurs conversationnels (arguments requis)

[Section intitulée « Déclencheurs conversationnels (arguments requis) »](#d%C3%A9clencheurs-conversationnels-arguments-requis)

Certains déclencheurs lancent une conversation libre au lieu d’un workflow structuré. Ils s’attendent à ce que vous décriviez ce dont vous avez besoin à côté du code du déclencheur.

AgentDéclencheurCe qu’il faut fournirRédacteur Technique (Paige)`WD`Description du document à rédigerRédacteur Technique (Paige)`US`Préférences ou conventions à ajouter aux standardsRédacteur Technique (Paige)`MG`Description et type de diagramme (séquence, organigramme, etc.)Rédacteur Technique (Paige)`VD`Document à valider et domaines à examinerRédacteur Technique (Paige)`EC`Nom du concept à expliquer

**Exemple :**

```text

WD Rédige un guide de déploiement pour notre configuration Docker
MG Crée un diagramme de séquence montrant le flux d’authentification
EC Explique le fonctionnement du système de modules
```

1. Brief : document synthétique qui formalise le contexte, les objectifs, le périmètre et les contraintes d’un projet ou d’une demande, afin d’aligner rapidement les parties prenantes avant le travail détaillé. [↩](#user-content-fnref-1)
2. UX (User Experience) : expérience utilisateur, englobant l’ensemble des interactions et perceptions d’un utilisateur face à un produit. Le design UX vise à créer des interfaces intuitives, efficaces et agréables en tenant compte des besoins, comportements et contexte d’utilisation. [↩](#user-content-fnref-2)