---
title: Créer un assistant de recherche IA avec Firecrawl et l’AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/cookbooks/ai-research-assistant-cookbook
source: sitemap
fetched_at: 2026-03-23T07:35:40.509987-03:00
rendered_js: false
word_count: 707
summary: Ce guide explique comment développer un assistant de recherche IA capable d'utiliser des outils de navigation web et de scraping en temps réel grâce au SDK Vercel AI et Firecrawl.
tags:
    - ai-sdk
    - web-scraping
    - nextjs
    - openai
    - firecrawl
    - chatbot-development
    - tool-calling
category: guide
---

Créez un assistant de recherche complet alimenté par l’IA, capable d’extraire des informations depuis des sites web et d’effectuer des recherches en ligne pour répondre aux questions. L’assistant décide automatiquement quand utiliser des outils de scraping ou de recherche pour rassembler des informations, puis fournit des réponses complètes basées sur les données collectées. ![Interface de chatbot d’assistant de recherche IA montrant un scraping web en temps réel avec Firecrawl et des réponses conversationnelles propulsées par OpenAI](https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b)

## Ce que vous allez construire

Une interface de chat IA où les utilisateurs peuvent poser des questions sur n’importe quel sujet. L’assistant IA décide automatiquement quand utiliser le scraping web ou la recherche pour rassembler des informations, puis fournit des réponses complètes basées sur les données collectées.

## Prérequis

- Node.js 18 ou version ultérieure installé
- Une clé API OpenAI depuis [platform.openai.com](https://platform.openai.com)
- Une clé API Firecrawl depuis [firecrawl.dev](https://firecrawl.dev)
- Des notions de base de React et de Next.js

### Flux des messages

1. **L’utilisateur envoie un message** : l’utilisateur saisit une question et clique sur Envoyer
2. **Le frontend envoie la requête** : `useChat` envoie le message à `/api/chat` avec le modèle sélectionné et le paramètre de recherche web
3. **Le backend traite le message** : la route d’API reçoit le message et appelle `streamText`
4. **L’IA choisit des outils** : le modèle analyse la question et décide d’utiliser `scrapeWebsite` ou `searchWeb` (uniquement si la recherche web est activée)
5. **Exécution des outils** : si des outils sont appelés, Firecrawl effectue un scraping ou une recherche sur le web
6. **L’IA génère une réponse** : le modèle analyse les résultats des outils et génère une réponse en langage naturel
7. **Le frontend affiche les résultats** : l’interface affiche les appels d’outils et la réponse finale en temps réel

Le système d’appel d’outils de l’AI SDK ([ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools)) fonctionne comme suit :

1. Le modèle reçoit le message de l’utilisateur ainsi que les descriptions des outils disponibles
2. Si le modèle détermine qu’un outil est nécessaire, il génère un appel d’outil avec des paramètres
3. Le SDK exécute la fonction d’outil avec ces paramètres
4. Le résultat de l’outil est renvoyé au modèle
5. Le modèle utilise ce résultat pour générer sa réponse finale

Tout cela se fait automatiquement dans un seul appel à `streamText`, avec des résultats diffusés vers le frontend en temps réel.

## Principales fonctionnalités

### Sélection du modèle

L’application prend en charge plusieurs modèles OpenAI :

- **GPT-5 Mini (Thinking)** : modèle OpenAI récent avec des capacités de raisonnement avancées
- **GPT-4o Mini** : modèle rapide et économique

Les utilisateurs peuvent passer d’un modèle à l’autre via le menu déroulant.

### Interrupteur de recherche web

Le bouton Search détermine si l’IA peut utiliser les outils Firecrawl :

- **Activé** : l’IA peut appeler les outils `scrapeWebsite` et `searchWeb` selon les besoins
- **Désactivé** : l’IA répond uniquement à partir de ses données d’entraînement

Cela permet aux utilisateurs de décider quand utiliser des données web plutôt que les connaissances intégrées du modèle.

## Idées de personnalisation

Étendez l’assistant avec des outils supplémentaires :

- Requêtes dans la base de données pour les données internes de l’entreprise
- Intégration au CRM pour récupérer les informations client
- Envoi d’e-mails
- Génération de documents

Chaque outil suit le même modèle : définir un schéma avec Zod, implémenter la fonction execute, puis l’enregistrer dans l’objet `tools`.

### Changer le modèle d’IA

Remplacez OpenAI par un autre prestataire :

```
import { anthropic } from "@ai-sdk/anthropic";

const result = streamText({
  model: anthropic("claude-4.5-sonnet"),
  // ... reste de la config
});
```

Le SDK d’IA prend en charge plus de 20 fournisseurs via la même API. En savoir plus : [ai-sdk.dev/docs/foundations/providers-and-models](https://ai-sdk.dev/docs/foundations/providers-and-models).

### Personnaliser l’interface utilisateur

Les composants AI Elements sont basés sur shadcn/ui ; vous pouvez donc :

- Modifier les styles des composants dans les fichiers des composants
- Ajouter de nouvelles variantes aux composants existants
- Créer des composants personnalisés qui correspondent au design system

## Bonnes pratiques

1. **Utilisez les outils appropriés** : Choisissez `searchWeb` pour trouver d’abord des pages pertinentes, `scrapeWebsite` pour des pages individuelles, ou laissez l’IA décider.
2. **Surveillez l’utilisation de l’API** : Suivez votre consommation des API Firecrawl et OpenAI pour éviter des coûts inattendus.
3. **Gérez les erreurs avec souplesse** : Les outils intègrent une gestion des erreurs, mais envisagez d’ajouter des messages d’erreur visibles par l’utilisateur.
4. **Optimisez les performances** : Utilisez le streaming pour fournir un retour immédiat et envisagez de mettre en cache le contenu fréquemment consulté.
5. **Définissez des limites raisonnables** : `stopWhen: stepCountIs(5)` empêche les appels d’outil excessifs et les coûts incontrôlés.

* * *