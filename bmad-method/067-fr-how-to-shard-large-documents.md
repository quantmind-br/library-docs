---
title: Guide de Division de Documents
url: https://docs.bmad-method.org/fr/how-to/shard-large-documents/
source: sitemap
fetched_at: 2026-04-08T11:30:47.436531722-03:00
rendered_js: false
word_count: 194
summary: This document explains the process and necessity of using the `bmad-shard-doc` tool to split large markdown files into smaller, contextually organized chunks based on level 2 headings.
tags:
    - markdown-splitting
    - context-management
    - document-sharding
    - tool-usage
    - content-organization
category: guide
---

Utilisez l’outil `bmad-shard-doc` si vous avez besoin de diviser des fichiers markdown volumineux en fichiers plus petits et organisés pour une meilleure gestion du contexte.

Utilisez ceci uniquement si vous remarquez que votre combinaison outil / modèle ne parvient pas à charger et lire tous les documents en entrée lorsque c’est nécessaire.

## Qu’est-ce que la Division de Documents ?

[Section intitulée « Qu’est-ce que la Division de Documents ? »](#quest-ce-que-la-division-de-documents)

La division de documents divise les fichiers markdown volumineux en fichiers plus petits et organisés basés sur les titres de niveau 2 (`## Titre`).

```text

Avant Division :
_bmad-output/planning-artifacts/
└── PRD.md (fichier volumineux de 50k tokens)
Après Division :
_bmad-output/planning-artifacts/
└── prd/
├── index.md                    # Table des matières avec descriptions
├── overview.md                 # Section 1
├── user-requirements.md        # Section 2
├── technical-requirements.md   # Section 3
└── ...                         # Sections supplémentaires
```

### 1. Exécuter l’Outil Shard-Doc

[Section intitulée « 1. Exécuter l’Outil Shard-Doc »](#1-ex%C3%A9cuter-loutil-shard-doc)

### 2. Suivre le Processus Interactif

[Section intitulée « 2. Suivre le Processus Interactif »](#2-suivre-le-processus-interactif)

```text

Agent : Quel document souhaitez-vous diviser ?
Utilisateur : docs/PRD.md
Agent : Destination par défaut : docs/prd/
Accepter la valeur par défaut ? [y/n]
Utilisateur : y
Agent : Division de PRD.md...
✓ 12 fichiers de section créés
✓ index.md généré
✓ Terminé !
```

Les workflows BMad utilisent un **système de découverte double** :

1. **Essaye d’abord le document entier** - Rechercher `document-name.md`
2. **Vérifie la version divisée** - Rechercher `document-name/index.md`
3. **Règle de priorité** - Le document entier a la priorité si les deux existent - supprimez le document entier si vous souhaitez que la version divisée soit utilisée à la place

Tous les workflows BMM prennent en charge les deux formats :

- Documents entiers
- Documents divisés
- Détection automatique
- Transparent pour l’utilisateur