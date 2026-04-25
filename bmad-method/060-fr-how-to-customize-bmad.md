---
title: Comment personnaliser BMad
url: https://docs.bmad-method.org/fr/how-to/customize-bmad/
source: sitemap
fetched_at: 2026-04-08T11:30:33.342537919-03:00
rendered_js: false
word_count: 595
summary: This document provides a comprehensive guide on using `.customize.yaml` files to tailor the behavior, persona, and menu structure of AI agents while ensuring changes persist through updates. It details which sections modify default settings (like `persona` or `memories`) and how to apply these customizations.
tags:
    - agent-customization
    - yaml-configuration
    - behavior-modification
    - workflow-setup
    - ai-agents
    - technical-guide
category: guide
---

Utilisez les fichiers `.customize.yaml` pour adapter le comportement, les personas[1](#user-content-fn-1) et les menus des agents tout en préservant vos modifications lors des mises à jour.

## Quand utiliser cette fonctionnalité

[Section intitulée « Quand utiliser cette fonctionnalité »](#quand-utiliser-cette-fonctionnalit%C3%A9)

- Vous souhaitez modifier le nom, la personnalité ou le style de communication d’un agent
- Vous avez besoin que les agents se souviennent du contexte spécifique au projet
- Vous souhaitez ajouter des éléments de menu personnalisés qui déclenchent vos propres workflows ou prompts
- Vous voulez que les agents effectuent des actions spécifiques à chaque démarrage

### 1. Localiser les fichiers de personnalisation

[Section intitulée « 1. Localiser les fichiers de personnalisation »](#1-localiser-les-fichiers-de-personnalisation)

Après l’installation, vous trouverez un fichier `.customize.yaml` par agent dans :

```text

_bmad/_config/agents/
├── bmm-analyst.customize.yaml
├── bmm-architect.customize.yaml
└── ... (un fichier par agent installé)
```

### 2. Modifier le fichier de personnalisation

[Section intitulée « 2. Modifier le fichier de personnalisation »](#2-modifier-le-fichier-de-personnalisation)

Ouvrez le fichier `.customize.yaml` de l’agent que vous souhaitez modifier. Chaque section est facultative — personnalisez uniquement ce dont vous avez besoin.

SectionComportementObjectif`agent.metadata`RemplaceRemplacer le nom d’affichage de l’agent`persona`RemplaceDéfinir le rôle, l’identité, le style et les principes`memories`AjouteAjouter un contexte persistant que l’agent se rappelle toujours`menu`AjouteAjouter des éléments de menu personnalisés pour les workflows ou prompts`critical_actions`AjouteDéfinir les instructions de démarrage de l’agent`prompts`AjouteCréer des prompts réutilisables pour les actions du menu

Les sections marquées **Remplace** écrasent entièrement les valeurs par défaut de l’agent. Les sections marquées **Ajoute** s’ajoutent à la configuration existante.

**Nom de l’agent**

Modifier la façon dont l’agent se présente :

```yaml

agent:
metadata:
name: 'Bob l’éponge'# Par défaut : "Mary"
```

**Persona**

Remplacer la personnalité, le rôle et le style de communication de l’agent :

```yaml

persona:
role: 'Ingénieur Full-Stack Senior'
identity: 'Habite dans un ananas (au fond de la mer)'
communication_style: 'Style agaçant de Bob l’Éponge'
principles:
- 'Jamais de nidification, les devs Bob l’Éponge détestent plus de 2 niveaux d’imbrication'
- 'Privilégier la composition à l’héritage'
```

La section `persona`[1](#user-content-fn-1) remplace entièrement le persona par défaut, donc incluez les quatre champs si vous la définissez.

**Souvenirs**

Ajouter un contexte persistant que l’agent gardera toujours en mémoire :

```yaml

memories:
- 'Travaille au Krusty Krab'
- 'Célébrité préférée : David Hasselhoff'
- 'Appris dans l’Epic 1 que ce n’est pas cool de faire semblant que les tests ont passé'
```

**Éléments de menu**

Ajouter des entrées personnalisées au menu d’affichage de l’agent. Chaque élément nécessite un `trigger`, une cible (chemin `workflow` ou référence `action`), et une `description` :

```yaml

menu:
- trigger: my-workflow
workflow: 'my-custom/workflows/my-workflow.yaml'
description: Mon workflow personnalisé
- trigger: deploy
action: '#deploy-prompt'
description: Déployer en production
```

**Actions critiques**

Définir des instructions qui s’exécutent au démarrage de l’agent :

```yaml

critical_actions:
- 'Vérifier les pipelines CI avec le Skill XYZ et alerter l’utilisateur au réveil si quelque chose nécessite une attention urgente'
```

**Prompts personnalisés**

Créer des prompts réutilisables que les éléments de menu peuvent référencer avec `action="#id"` :

```yaml

prompts:
- id: deploy-prompt
content: |
Déployer la branche actuelle en production :
1. Exécuter tous les tests
2. Build le projet
3. Exécuter le script de déploiement
```

### 3. Appliquer vos modifications

[Section intitulée « 3. Appliquer vos modifications »](#3-appliquer-vos-modifications)

Après modification, réinstallez pour appliquer les changements :

L’installateur détecte l’installation existante et propose ces options :

OptionCe qu’elle fait**Quick Update**Met à jour tous les modules vers la dernière version et applique les personnalisations**Modify BMad Installation**Flux d’installation complet pour ajouter ou supprimer des modules

Pour des modifications de personnalisation uniquement, **Quick Update** est l’option la plus rapide.

## Résolution des problèmes

[Section intitulée « Résolution des problèmes »](#r%C3%A9solution-des-probl%C3%A8mes)

**Les modifications n’apparaissent pas ?**

- Exécutez `npx bmad-method install` et sélectionnez **Quick Update** pour appliquer les modifications
- Vérifiez que votre syntaxe YAML est valide (l’indentation compte)
- Assurez-vous d’avoir modifié le bon fichier `.customize.yaml` pour l’agent

**L’agent ne se charge pas ?**

- Vérifiez les erreurs de syntaxe YAML à l’aide d’un validateur YAML en ligne
- Assurez-vous de ne pas avoir laissé de champs vides après les avoir décommentés
- Essayez de revenir au modèle d’origine et de reconstruire

**Besoin de réinitialiser un agent ?**

- Effacez ou supprimez le fichier `.customize.yaml` de l’agent
- Exécutez `npx bmad-method install` et sélectionnez **Quick Update** pour restaurer les valeurs par défaut

## Personnalisation des workflows

[Section intitulée « Personnalisation des workflows »](#personnalisation-des-workflows)

La personnalisation des workflows et skills existants de la méthode BMad arrive bientôt.

## Personnalisation des modules

[Section intitulée « Personnalisation des modules »](#personnalisation-des-modules)

Les conseils sur la création de modules d’extension et la personnalisation des modules existants arrivent bientôt.

1. Persona : définition de la personnalité, du rôle et du style de communication d’un agent IA. Permet d’adapter le comportement et les réponses de l’agent selon les besoins du projet. [↩](#user-content-fnref-1) [↩2](#user-content-fnref-1-2)