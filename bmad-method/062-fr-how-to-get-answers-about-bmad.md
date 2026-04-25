---
title: Comment obtenir des réponses à propos de BMad
url: https://docs.bmad-method.org/fr/how-to/get-answers-about-bmad/
source: sitemap
fetched_at: 2026-04-08T11:30:37.589907144-03:00
rendered_js: false
word_count: 510
summary: This guide explains how to obtain answers about BMad using the `bmad-help` skill, which can answer many questions by inspecting projects and understanding natural language. It also details alternative methods for deeper research, such as pointing an AI tool toward specific source files or repositories.
tags:
    - bmad
    - help-skill
    - natural-language
    - research-guide
    - ai-integration
    - project-workflow
category: guide
---

## Commencez ici : BMad-Help

[Section intitulée « Commencez ici : BMad-Help »](#commencez-ici--bmad-help)

**Le moyen le plus rapide d’obtenir des réponses sur BMad est le skill `bmad-help`.** Ce guide intelligent répondra à plus de 80 % de toutes les questions et est disponible directement dans votre IDE pendant que vous travaillez.

BMad-Help est bien plus qu’un outil de recherche — il :

- **Inspecte votre projet** pour voir ce qui a déjà été réalisé
- **Comprend le langage naturel** — posez vos questions en français courant
- **S’adapte à vos modules installés** — affiche les options pertinentes
- **Se lance automatiquement après les workflows** — vous indique exactement quoi faire ensuite
- **Recommande la première tâche requise** — plus besoin de deviner par où commencer

Appelez-le par son nom dans votre session IA :

Combinez-le avec une requête en langage naturel :

```plaintext

bmad-help J'ai une idée de SaaS et je connais toutes les fonctionnalités. Par où commencer ?
bmad-help Quelles sont mes options pour le design UX ?
bmad-help Je suis bloqué sur le workflow PRD
bmad-help Montre-moi ce qui a été fait jusqu'à maintenant
```

BMad-Help répond avec :

- Ce qui est recommandé pour votre situation
- Quelle est la première tâche requise
- À quoi ressemble le reste du processus

## Quand utiliser ce guide

[Section intitulée « Quand utiliser ce guide »](#quand-utiliser-ce-guide)

Utilisez cette section lorsque :

- Vous souhaitez comprendre l’architecture ou les éléments internes de BMad
- Vous avez besoin de réponses au-delà de ce que BMad-Help fournit
- Vous faites des recherches sur BMad avant l’installation
- Vous souhaitez explorer le code source directement

### 1. Choisissez votre source

[Section intitulée « 1. Choisissez votre source »](#1-choisissez-votre-source)

SourceIdéal pourExemples**Dossier `_bmad`**Comment fonctionne BMad — agents, workflows, prompts”Que fait l’agent Analyste ?”**Repo GitHub complet**Historique, installateur, architecture”Qu’est-ce qui a changé dans la v6 ?”**`llms-full.txt`**Aperçu rapide depuis la documentation”Expliquez les quatre phases de BMad”

Le dossier `_bmad` est créé lorsque vous installez BMad. Si vous ne l’avez pas encore, clonez le repo à la place.

### 2. Pointez votre IA vers la source

[Section intitulée « 2. Pointez votre IA vers la source »](#2-pointez-votre-ia-vers-la-source)

**Si votre IA peut lire des fichiers (Claude Code, Cursor, etc.) :**

- **BMad installé :** Pointez vers le dossier `_bmad` et posez vos questions directement
- **Vous voulez plus de contexte :** Clonez le [repo complet](https://github.com/bmad-code-org/BMAD-METHOD)

**Si vous utilisez ChatGPT ou Claude.ai (LLM en ligne) :**

Importez `llms-full.txt` dans votre session :

```text

https://bmad-code-org.github.io/BMAD-METHOD/llms-full.txt
```

### 3. Posez votre question

[Section intitulée « 3. Posez votre question »](#3-posez-votre-question)

Des réponses directes sur BMad — comment fonctionnent les agents, ce que font les workflows, pourquoi les choses sont structurées ainsi — sans attendre la réponse de quelqu’un.

- **Vérifiez les réponses surprenantes** — Les LLM font parfois des erreurs. Consultez le fichier source ou posez la question sur Discord.
- **Soyez précis** — “Que fait l’étape 3 du workflow PRD ?” est mieux que “Comment fonctionne le PRD ?”

Avez-vous essayé l’approche LLM et avez encore besoin d’aide ? Vous avez maintenant une bien meilleure question à poser.

CanalUtilisé pour`#bmad-method-help`Questions rapides (chat en temps réel)Forum `help-requests`Questions détaillées (recherchables, persistants)`#suggestions-feedback`Idées et demandes de fonctionnalités`#report-bugs-and-issues`Rapports de bugs

**Discord :** [discord.gg/gk8jAdXWmj](https://discord.gg/gk8jAdXWmj)

**GitHub Issues :** [github.com/bmad-code-org/BMAD-METHOD/issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) (pour les bugs clairs)

*Toi !* *Bloqué* *dans la file d’attente—* *qui* *attends-tu ?*

*La source* *est là,* *facile à voir !*

*Pointez* *votre machine.* *Libérez-la.*

*Elle lit.* *Elle parle.* *Demandez—*

*Pourquoi attendre* *demain* *quand tu as déjà* *cette journée ?*

*—Claude*