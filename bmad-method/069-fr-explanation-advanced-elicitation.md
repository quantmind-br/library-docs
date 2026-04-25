---
title: Élicitation Avancée
url: https://docs.bmad-method.org/fr/explanation/advanced-elicitation/
source: sitemap
fetched_at: 2026-04-08T11:30:11.303791653-03:00
rendered_js: false
word_count: 347
summary: This document explains Advanced Elicitation, which is a structured second pass where the user selects a specific reasoning method to have an LLM re-examine its own output, allowing for deeper analysis than simple revision requests.
tags:
    - advanced-elicitation
    - llm-reasoning
    - thought-processes
    - critical-thinking
    - prompt-engineering
category: concept
---

Faites repenser au LLM ce qu’il vient de générer. Vous choisissez une méthode de raisonnement, il l’applique à sa propre sortie, et vous décidez de conserver ou non les améliorations.

## Qu’est-ce que l’Élicitation Avancée ?

[Section intitulée « Qu’est-ce que l’Élicitation Avancée ? »](#quest-ce-que-l%C3%A9licitation-avanc%C3%A9e)

Un second passage structuré. Au lieu de demander à l’IA de “réessayer” ou de “faire mieux”, vous sélectionnez une méthode de raisonnement spécifique et l’IA réexamine sa propre sortie à travers ce prisme.

La différence est importante. Les demandes vagues produisent des révisions vagues. Une méthode nommée impose un angle d’attaque particulier, mettant en lumière des perspectives qu’un simple réajustement générique aurait manquées.

- Après qu’un workflow a généré du contenu et vous souhaitez des alternatives
- Lorsque la sortie semble correcte mais que vous soupçonnez qu’il y a davantage de profondeur
- Pour tester les hypothèses ou trouver des faiblesses
- Pour du contenu à enjeux élevés où la réflexion approfondie aide

Les workflows offrent l’élicitation aux points de décision - après que le LLM ait généré quelque chose, on vous demandera si vous souhaitez l’exécuter.

1. Le LLM suggère 5 méthodes pertinentes pour votre contenu
2. Vous en choisissez une (ou remélangez pour différentes options)
3. La méthode est appliquée, les améliorations sont affichées
4. Acceptez ou rejetez, répétez ou continuez

Des dizaines de méthodes de raisonnement sont disponibles. Quelques exemples :

- **Analyse Pré-mortem** - Suppose que le projet a déjà échoué, revient en arrière pour trouver pourquoi
- **Pensée de Premier Principe** - Élimine les hypothèses, reconstruit à partir de la vérité de terrain
- **Inversion** - Demande comment garantir l’échec, puis les évite
- **Équipe Rouge vs Équipe Bleue** - Attaque votre propre travail, puis le défend
- **Questionnement Socratique** - Conteste chaque affirmation avec “pourquoi ?” et “comment le savez-vous ?”
- **Suppression des Contraintes** - Abandonne toutes les contraintes, voit ce qui change, les réajoute sélectivement
- **Cartographie des Parties Prenantes** - Réévalue depuis la perspective de chaque partie prenante
- **Raisonnement Analogique** - Trouve des parallèles dans d’autres domaines et applique leurs leçons

Et bien d’autres. L’IA choisit les options les plus pertinentes pour votre contenu - vous choisissez lesquelles exécuter.