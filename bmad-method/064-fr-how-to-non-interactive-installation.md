---
title: Installation non-interactive
url: https://docs.bmad-method.org/fr/how-to/non-interactive-installation/
source: sitemap
fetched_at: 2026-04-08T11:30:41.301884023-03:00
rendered_js: false
word_count: 646
summary: This document details how to perform non-interactive installations of BMad using command-line options, covering necessary arguments for deployment pipelines and providing comprehensive guidance on configuration parameters, path resolution, and troubleshooting common errors.
tags:
    - command-line-interface
    - installation-guide
    - ci-cd-deployment
    - bmad-configuration
    - non-interactive
    - cli-options
category: guide
---

Utilisez les options de ligne de commande pour installer BMad de manière non-interactive. Cela est utile pour :

## Quand utiliser cette méthode

[Section intitulée « Quand utiliser cette méthode »](#quand-utiliser-cette-m%C3%A9thode)

- Déploiements automatisés et pipelines CI/CD
- Installations scriptées
- Installations par lots sur plusieurs projets
- Installations rapides avec des configurations connues

### Options d’installation

[Section intitulée « Options d’installation »](#options-dinstallation)

OptionDescriptionExemple`--directory <chemin>`Répertoire d’installation`--directory ~/projects/myapp``--modules <modules>`IDs de modules séparés par des virgules`--modules bmm,bmb``--tools <outils>`IDs d’outils/IDE séparés par des virgules (utilisez `none` pour ignorer)`--tools claude-code,cursor` ou `--tools none``--action <type>`Action pour les installations existantes : `install` (par défaut), `update`, ou `quick-update``--action quick-update`

### Configuration principale

[Section intitulée « Configuration principale »](#configuration-principale)

OptionDescriptionPar défaut`--user-name <nom>`Nom à utiliser par les agentsNom d’utilisateur système`--communication-language <langue>`Langue de communication des agentsAnglais`--document-output-language <langue>`Langue de sortie des documentsAnglais`--output-folder <chemin>`Chemin du dossier de sortie (voir les règles de résolution ci-dessous)`_bmad-output`

#### Résolution du chemin du dossier de sortie

[Section intitulée « Résolution du chemin du dossier de sortie »](#r%C3%A9solution-du-chemin-du-dossier-de-sortie)

La valeur passée à `--output-folder` (ou saisie de manière interactive) est résolue selon ces règles :

Type d’entréeExempleRésolu commeChemin relatif (par défaut)`_bmad-output``<racine-du-projet>/_bmad-output`Chemin relatif avec traversée`../../shared-outputs`Chemin absolu normalisé — ex. `/Users/me/shared-outputs`Chemin absolu`/Users/me/shared-outputs`Utilisé tel quel — la racine du projet n’est **pas** ajoutée

Le chemin résolu est ce que les agents et les workflows vont utiliser lors de l’écriture des fichiers de sortie. L’utilisation d’un chemin absolu ou d’un chemin relatif avec traversée vous permet de diriger tous les artefacts générés vers un répertoire en dehors de l’arborescence de votre projet — utile pour les configurations partagées ou les monorepos.

OptionDescription`-y, --yes`Accepter tous les paramètres par défaut et ignorer les invites`-d, --debug`Activer la sortie de débogage pour la génération du manifeste

IDs de modules disponibles pour l’option `--modules` :

- `bmm` — méthode BMad Master
- `bmb` — BMad Builder

Consultez le [registre BMad](https://github.com/bmad-code-org) pour les modules externes disponibles.

IDs d’outils disponibles pour l’option `--tools` :

**Recommandés :** `claude-code`, `cursor`

Exécutez `npx bmad-method install` de manière interactive une fois pour voir la liste complète actuelle des outils pris en charge, ou consultez la [configuration des codes de la plateforme](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml).

ModeDescriptionExempleEntièrement non-interactifFournir toutes les options pour ignorer toutes les invites`npx bmad-method install --directory . --modules bmm --tools claude-code --yes`Semi-interactifFournir certains options ; BMad demande les autres`npx bmad-method install --directory . --modules bmm`Paramètres par défaut uniquementAccepter tous les paramètres par défaut avec `-y``npx bmad-method install --yes`Sans outilsIgnorer la configuration des outils/IDE`npx bmad-method install --modules bmm --tools none`

### Installation dans un pipeline CI/CD

[Section intitulée « Installation dans un pipeline CI/CD »](#installation-dans-un-pipeline-cicd)

```bash

#!/bin/bash
npxbmad-methodinstall\
--directory"${GITHUB_WORKSPACE}"\
--modulesbmm\
--toolsclaude-code\
--user-name"CI Bot"\
--communication-languageFrançais\
--document-output-languageFrançais\
--output-folder_bmad-output\
--yes
```

### Mettre à jour une installation existante

[Section intitulée « Mettre à jour une installation existante »](#mettre-%C3%A0-jour-une-installation-existante)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionupdate\
--modulesbmm,bmb,custom-module
```

### Mise à jour rapide (conserver les paramètres)

[Section intitulée « Mise à jour rapide (conserver les paramètres) »](#mise-%C3%A0-jour-rapide-conserver-les-param%C3%A8tres)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionquick-update
```

- Un répertoire `_bmad/` entièrement configuré dans votre projet
- Des agents et des flux de travail configurés pour vos modules et outils sélectionnés
- Un dossier `_bmad-output/` pour les artefacts générés

## Validation et gestion des erreurs

[Section intitulée « Validation et gestion des erreurs »](#validation-et-gestion-des-erreurs)

BMad valide toutes les options fournis :

- **Directory** — Doit être un chemin valide avec des permissions d’écriture
- **Modules** — Avertit des IDs de modules invalides (mais n’échoue pas)
- **Tools** — Avertit des IDs d’outils invalides (mais n’échoue pas)
- **Action** — Doit être l’une des suivantes : `install`, `update`, `quick-update`

Les valeurs invalides entraîneront soit :

1. L’affichage d’un message d’erreur suivi d’un exit (pour les options critiques comme le répertoire)
2. Un avertissement puis la continuation de l’installation (pour les éléments optionnels)
3. Un retour aux invites interactives (pour les valeurs requises manquantes)

## Résolution des problèmes

[Section intitulée « Résolution des problèmes »](#r%C3%A9solution-des-probl%C3%A8mes)

### L’installation échoue avec “Invalid directory”

[Section intitulée « L’installation échoue avec “Invalid directory” »](#linstallation-%C3%A9choue-avec-invalid-directory)

- Le chemin du répertoire doit exister (ou son parent doit exister)
- Vous avez besoin des permissions d’écriture
- Le chemin doit être absolu ou correctement relatif au répertoire actuel

<!--THE END-->

- Vérifiez que l’ID du module est correct
- Les modules externes doivent être disponibles dans le registre