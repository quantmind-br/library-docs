---
title: Navigateur | Firecrawl
url: https://docs.firecrawl.dev/fr/features/browser
source: sitemap
fetched_at: 2026-03-23T07:24:09.58011-03:00
rendered_js: false
word_count: 1078
summary: This document describes the Firecrawl browser sandbox, an infrastructure-free, cloud-based environment that allows AI agents to interact with the web using tools like Playwright and agent-browser.
tags:
    - firecrawl
    - browser-sandbox
    - ai-agents
    - web-automation
    - playwright
    - headless-browser
    - api-reference
category: guide
---

Le bac à sable de navigateur Firecrawl offre à vos agents un environnement de navigateur sécurisé où ils peuvent interagir avec le web. Remplissez des formulaires, cliquez sur des boutons, authentifiez-vous, et plus encore. Aucune configuration locale, aucune installation de Chromium, aucun problème de compatibilité de driver. agent-browser et Playwright sont préinstallés. Disponible via l’[API](https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-create), la [CLI](https://docs.firecrawl.dev/fr/sdks/cli#browser) (Bash / agent-browser, Python, Node), le [SDK Node](https://docs.firecrawl.dev/fr/sdks/node#browser), le [SDK Python](https://docs.firecrawl.dev/fr/sdks/python#browser), le [Vercel AI SDK](https://docs.firecrawl.dev/fr/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk) et le [serveur MCP](https://docs.firecrawl.dev/fr/mcp-server). Pour ajouter la prise en charge du navigateur à un agent de codage IA (Claude Code, Codex, Open Code, Cursor, etc.), installez la compétence Firecrawl :

```
npx -y firecrawl-cli@latest init --all --browser
```

Chaque session s’exécute dans un bac à sable isolé, jetable ou persistant, qui passe à l’échelle sans avoir à gérer d’infrastructure.

## Démarrage rapide

Créez une session, exécutez du code, puis fermez-la :

- **Aucune installation de driver requise** — Pas de binaire Chromium, pas de `playwright install`, pas de problèmes de compatibilité de driver
- **Python, JavaScript & Bash** — Envoyez du code via l’API, la CLI ou le SDK et récupérez les résultats. Les trois langages s’exécutent à distance dans la sandbox
- **agent-browser** — CLI préinstallée avec plus de 60 commandes. Les agents d’IA écrivent de simples commandes bash au lieu de code Playwright
- **Playwright préinstallé** — Playwright est déjà disponible dans la sandbox. Les agents peuvent écrire du code Playwright s’ils le préfèrent.
- **Accès CDP** — Connectez votre propre instance Playwright via WebSocket lorsque vous avez besoin d’un contrôle total
- **Vue en direct** — Suivez les sessions en temps réel via une URL de flux intégrable
- **Vue en direct interactive** — Permettez aux utilisateurs d’interagir directement avec le navigateur via un flux en direct interactif intégrable

## Lancer une session

Retourne un ID de session, une URL CDP et une URL de visualisation en direct.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

## Exécuter le code

Exécutez du code Python, JavaScript ou bash dans votre session. Output est renvoyé via `stdout` ; pour Node.js, la valeur de la dernière expression est également disponible dans `result`.

```
{
  "success": true,
  "stdout": "",
  "result": "Example Domain",
  "stderr": "",
  "exitCode": 0,
  "killed": false
}
```

### Gestion des téléchargements de fichiers

Les fichiers téléchargés au cours d’une session peuvent être capturés et renvoyés en base64. Utilisez l’API de téléchargement de Playwright via le point de terminaison `execute` :

## agent-browser (Mode Bash)

[agent-browser](https://github.com/vercel-labs/agent-browser) est une CLI de navigateur headless préinstallée dans chaque sandbox. Au lieu d’écrire du code Playwright, les agents envoient de simples commandes Bash. La CLI injecte automatiquement `--cdp` pour permettre à agent-browser de se connecter à votre session active.

### Raccourci

La méthode la plus rapide pour utiliser `browser`. Le raccourci et `execute` envoient tous les deux des commandes à `agent-browser` automatiquement. Le raccourci se contente d’omettre `execute` et de lancer automatiquement une session si nécessaire :

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

### CLI

La forme explicite utilise `execute`. Les commandes sont envoyées automatiquement à `agent-browser` : vous n’avez pas besoin de saisir `agent-browser` ni d’utiliser `--bash` :

### API & SDK

Utilisez `language: "bash"` pour exécuter des commandes agent-browser via l’API ou les SDK :

## Gestion des sessions

### Sessions persistantes

Par défaut, chaque session de navigateur démarre dans un état vierge. Avec `profile`, vous pouvez enregistrer et réutiliser l’état du navigateur entre les sessions. C’est utile pour rester connecté et conserver les préférences. Pour enregistrer ou sélectionner un profil, utilisez le paramètre `profile` lors de la création d’une session.

ParamètreValeur par défautDescription`name`—Un nom pour le profil persistant. Les sessions portant le même nom partagent le stockage.`saveChanges``true`Lorsque `true`, l’état du navigateur est enregistré dans le profil à la clôture. Définissez `false` pour charger les données existantes sans écrire — utile lorsque vous avez besoin de plusieurs lecteurs simultanés.

L’état de la session du navigateur n’est enregistré qu’une fois la session close. Nous vous recommandons donc de clore la session du navigateur lorsque vous avez terminé afin qu’elle puisse être réutilisée. Une fois une session close, son ID de session n’est plus valide — vous ne pouvez pas le réutiliser. Créez plutôt une nouvelle session avec le même nom de profil et utilisez le nouvel ID de session renvoyé dans la réponse. Pour l’enregistrer et la clore :

### Lister les sessions

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
      "liveViewUrl": "https://liveview.firecrawl.dev/...",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
      "createdAt": "2025-01-15T10:30:00Z",
      "lastActivity": "2025-01-15T10:35:00Z"
    }
  ]
}
```

### Configuration du TTL

Les sessions ont deux paramètres de TTL :

ParamètreValeur par défautDescription`ttl`600s (10 min)Durée de vie maximale de la session (30-3600s)`activityTtl`300s (5 min)Fermeture automatique après inactivité (10-3600s)

### Clore une session

## Vue en direct

Chaque session renvoie un `liveViewUrl` dans la réponse, que vous pouvez intégrer pour observer le navigateur en temps réel. Pratique pour le débogage, les démonstrations ou la création d’interfaces utilisateur pilotées par le navigateur.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}

<iframe src="LIVE_VIEW_URL" width="100%" height="600" />
```

### Vue en direct interactive

La réponse inclut également un `interactiveLiveViewUrl`. Contrairement à la vue en direct standard, qui est en lecture seule, la vue en direct interactive permet aux utilisateurs de cliquer, de saisir du texte et d’interagir avec la session de navigation directement via le flux intégré. C’est utile pour créer des interfaces de navigateur destinées aux utilisateurs finaux, pour le débogage collaboratif, ou pour tout scénario où la personne qui consulte la session doit contrôler le navigateur.

```
<iframe src="INTERACTIVE_LIVE_VIEW_URL" width="100%" height="600" />
```

## Connexion via CDP

Chaque session expose une URL WebSocket CDP. L’API `execute` et l’option `--bash` couvrent la plupart des cas d’utilisation, mais si vous avez besoin d’un contrôle complet en local, vous pouvez vous connecter directement.

## Quand utiliser Browser

Cas d’usageOutil adaptéExtraire le contenu d’une URL connue[Scrape](https://docs.firecrawl.dev/fr/features/scrape)Rechercher sur le Web et obtenir des résultats[Search](https://docs.firecrawl.dev/fr/features/search)Naviguer dans la pagination, remplir des formulaires, cliquer au fil des parcours**Browser**Workflows multi-étapes avec interaction**Browser**Navigation en parallèle sur de nombreux sites**Browser** (chaque session est isolée)

## Cas d’utilisation

- **Veille concurrentielle** - Parcourir les sites concurrents, naviguer dans les formulaires et filtres de recherche, extraire les tarifs et les fonctionnalités sous forme de données structurées
- **Ingestion de base de connaissances** - Naviguer dans les centres d’aide, la documentation et les portails d’assistance qui nécessitent des clics, de la pagination ou une authentification
- **Études de marché** - Lancer des sessions de navigation parallèles pour constituer des jeux de données à partir de sites d’offres d’emploi, d’annonces immobilières ou de bases de données juridiques

## Tarification

Tarification simple : 2 crédits par minute de navigateur. Les utilisateurs du plan gratuit disposent de 5 heures d’utilisation offertes.

## Limites de débit

Pour le lancement initial, nous autorisons jusqu’à 20 sessions de navigateur concurrentes pour tous les plans.

## Référence de l’API

- [Créer une session de navigateur](https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-create)
- [Exécuter du code dans le navigateur](https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-execute)
- [Lister les sessions de navigateur](https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-list)
- [Supprimer une session de navigateur](https://docs.firecrawl.dev/fr/api-reference/endpoint/browser-delete)

* * *

Vous avez des retours ou besoin d’aide ? Envoyez-nous un e-mail à [help@firecrawl.com](mailto:help@firecrawl.com) ou contactez-nous sur [Discord](https://discord.gg/firecrawl).

> Vous êtes un agent IA qui a besoin d’une API key Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour les instructions d’onboarding automatisé.