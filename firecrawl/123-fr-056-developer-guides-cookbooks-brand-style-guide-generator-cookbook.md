---
title: Créer un générateur de charte graphique de marque avec Firecrawl - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/cookbooks/brand-style-guide-generator-cookbook
source: sitemap
fetched_at: 2026-03-23T07:38:49.811625-03:00
rendered_js: false
word_count: 653
summary: This document explains how to build a Node.js application that uses the Firecrawl API to extract visual branding data from any website and automatically compile it into a professional PDF style guide.
tags:
    - web-scraping
    - brand-identity
    - design-tokens
    - pdf-generation
    - nodejs
    - firecrawl-api
    - automation
category: tutorial
---

Créez un générateur de charte graphique de marque qui extrait automatiquement les couleurs, la typographie, les espacements et l’identité visuelle de n’importe quel site web, puis les rassemble dans un document PDF professionnel. ![Générateur de charte graphique de marque en PDF utilisant le format de branding de Firecrawl pour extraire le système de design](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/brand-style-guide-pdf-generator-firecrawl.gif?s=2c8e0a9d223ea655238b17442c7bf41b)

## Ce que vous allez créer

Une application Node.js qui prend n’importe quelle URL de site web, extrait l’ensemble de son identité de marque en utilisant le format de branding de Firecrawl, et génère un guide de style PDF soigné avec :

- Palette de couleurs avec valeurs hexadécimales
- Système typographique (polices, tailles, graisses)
- Spécifications d’espacement et de mise en page
- Logo et visuels de marque
- Informations de thème (mode clair/sombre)

![Exemple de guide de style de marque au format PDF généré avec couleurs, typographie et espacements](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/generated-brand-style-guide-pdf-example.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=de8be5319be990d6630591afa3fc2dc2)

## Prérequis

- Node.js 18 ou une version ultérieure installé
- Une clé API Firecrawl obtenue sur [firecrawl.dev](https://firecrawl.dev)
- Des connaissances de base en TypeScript et Node.js

<!--THE END-->

1. **Saisie de l’URL** : le générateur reçoit l’URL du site web cible
2. **Scraping avec Firecrawl** : appelle l’endpoint `/scrape` avec le format `branding`
3. **Analyse de la marque** : Firecrawl analyse le CSS, les polices et les éléments visuels de la page
4. **Retour des données** : renvoie un objet structuré `BrandingProfile` contenant tous les design tokens

### Processus de génération de PDF

1. **Création de l’en-tête** : Génère un en-tête coloré en utilisant la couleur principale de la marque
2. **Récupération du logo** : Télécharge et intègre le logo ou le favicon si disponible
3. **Palette de couleurs** : Affiche chaque couleur sous forme d’échantillon visuel avec ses métadonnées
4. **Section typographie** : Documente les familles de polices, les tailles et les graisses de police
5. **Informations d’espacement** : Inclut les unités de base, le rayon de bordure et le mode du thème

### Structure du profil de marque

Le [format de branding](https://docs.firecrawl.dev/features/scrape#%2Fscrape-with-branding-endpoint) retourne des informations détaillées sur la marque :

```
{
  colorScheme: "dark" | "light",
  logo: "https://example.com/logo.svg",
  colors: {
    primary: "#FF6B35",
    secondary: "#004E89",
    accent: "#F77F00",
    background: "#1A1A1A",
    textPrimary: "#FFFFFF",
    textSecondary: "#B0B0B0"
  },
  typography: {
    fontFamilies: { primary: "Inter", heading: "Inter", code: "Roboto Mono" },
    fontSizes: { h1: "48px", h2: "36px", body: "16px" },
    fontWeights: { regular: 400, medium: 500, bold: 700 }
  },
  spacing: {
    baseUnit: 8,
    borderRadius: "8px"
  },
  images: {
    logo: "https://example.com/logo.svg",
    favicon: "https://example.com/favicon.ico"
  }
}
```

## Principales fonctionnalités

Le générateur identifie et classe toutes les couleurs de la marque :

- **Primaires & Secondaires** : Couleurs principales de la marque
- **Accent** : Couleurs d’accentuation et d’appel à l’action (CTA)
- **Arrière-plan & Texte** : Couleurs de base de l’interface
- **Couleurs sémantiques** : États de succès, d’avertissement et d’erreur

### Documentation de la typographie

Présente l’ensemble du système typographique :

- **Familles de polices** : principale, titres et monospace
- **Échelle de tailles** : toutes les tailles de texte pour les titres et le corps
- **Graisses de police** : variantes de graisses disponibles

### Rendu visuel

Le PDF inclut :

- En-tête coloré assorti à la marque
- Logo intégré lorsqu’il est disponible
- Mise en page professionnelle avec hiérarchie claire
- Pied de page contenant les métadonnées et la date de génération

![Comparaison côte à côte entre le site web d’origine et le PDF du guide de style de marque généré](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/website-to-brand-style-guide-comparison.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=90153b3c2c920eceb8cd454eb266f9d0)

## Idées de personnalisation

### Ajouter la documentation des composants

Étendez le générateur afin d’inclure les styles des composants d’interface utilisateur :

```
// Ajouter après la section Espacement et Thème
if (b.components) {
  doc.addPage();
  doc.fontSize(20).fillColor("#333").text("UI Components", 50, 50);

  // Documenter les styles de boutons
  if (b.components.buttonPrimary) {
    const btn = b.components.buttonPrimary;
    doc.fontSize(14).text("Primary Button", 50, 90);
    doc.rect(50, 110, 120, 40).fill(btn.background);
    doc.fontSize(12).fillColor(btn.textColor).text("Button", 50, 120, { width: 120, align: "center" });
  }
}
```

### Exporter plusieurs formats

Ajoutez un export JSON en plus du PDF :

```
// Ajouter avant doc.end()
fs.writeFileSync("brand-data.json", JSON.stringify(b, null, 2));
```

### Traitement par lots

Générez des guides pour plusieurs sites web :

```
const websites = [
  "https://stripe.com",
  "https://linear.app",
  "https://vercel.com"
];

for (const site of websites) {
  const { branding } = await fc.scrape(site, { formats: ["branding"] }) as any;
  // Générer un PDF pour chaque site...
}
```

### Thèmes PDF personnalisés

Créez différents styles de PDF en fonction du thème extrait :

```
const isDarkMode = b.colorScheme === "dark";
const headerBg = isDarkMode ? b.colors?.background : b.colors?.primary;
const textColor = isDarkMode ? "#fff" : "#333";
```

## Bonnes pratiques

1. **Gérer les données manquantes** : tous les sites web n’exposent pas des informations complètes sur la marque. Prévoyez toujours des valeurs de repli pour les propriétés manquantes.
2. **Respecter les limites de débit** : lors du traitement par lots de plusieurs sites, ajoutez des délais entre les requêtes pour respecter les limites de débit de Firecrawl.
3. **Mettre en cache les résultats** : stockez les données de marque extraites pour éviter des appels répétés à l’API pour un même site.
4. **Gestion des formats d’image** : certains logos peuvent être dans des formats que PDFKit ne prend pas en charge (comme le SVG). Envisagez d’ajouter une conversion de format ou des solutions de repli adaptées.
5. **Gestion des erreurs** : encapsulez le processus de génération dans des blocs try-catch et fournissez des messages d’erreur explicites.

* * *