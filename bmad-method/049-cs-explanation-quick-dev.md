---
title: Quick Dev
url: https://docs.bmad-method.org/cs/explanation/quick-dev/
source: sitemap
fetched_at: 2026-04-08T11:29:09.609053119-03:00
rendered_js: false
word_count: 744
summary: This document describes the 'bmad-quick-dev' workflow, a method designed to balance model autonomy with necessary human oversight by compressing initial intentions and limiting mandatory human review points to only the most critical stages.
tags:
    - llm-workflow
    - human-in-the-loop
    - intent-compression
    - autonomous-development
    - system-revision
    - agent-design
category: guide
---

Záměr na vstupu, změny kódu na výstupu, s co nejmenším počtem human-in-the-loop kroků — bez obětování kvality.

Umožňuje modelu běžet déle mezi kontrolními body a poté přivede člověka zpět pouze tehdy, když úkol nemůže bezpečně pokračovat bez lidského úsudku nebo když je čas zkontrolovat konečný výsledek.

![Diagram workflow Quick Dev](https://docs.bmad-method.org/diagrams/quick-dev-diagram.png)

Human-in-the-loop kroky jsou nutné a nákladné.

Současné LLM stále selhávají předvídatelnými způsoby: chybně čtou záměr, vyplňují mezery sebevědomými odhady, odchylují se k nesouvisející práci a generují šumový výstup revize. Současně neustálá lidská intervence limituje rychlost vývoje. Lidská pozornost je úzké hrdlo.

`bmad-quick-dev` přenastavuje tento kompromis. Důvěřuje modelu, aby běžel bez dozoru delší úseky, ale pouze poté, co workflow vytvořil dostatečně silnou hranici, aby to bylo bezpečné.

### 1. Nejprve komprimujte záměr

[Section titled “1. Nejprve komprimujte záměr”](#1-nejprve-komprimujte-z%C3%A1m%C4%9Br)

Workflow začíná tím, že člověk a model zkomprimují požadavek do jednoho koherentního cíle. Vstup může začínat jako hrubé vyjádření záměru, ale předtím, než workflow poběží autonomně, musí být dostatečně malý, jasný a bez protimluvů pro provedení.

Záměr může přijít v mnoha formách: pár frází, odkaz na bug tracker, výstup z plan mode, text zkopírovaný z chatové relace, nebo dokonce číslo story z BMAD vlastního `epics.md`. V posledním případě workflow nepochopí sémantiku sledování stories BMAD, ale stále může vzít samotnou story a pracovat s ní.

Tento workflow neodstraňuje lidskou kontrolu. Přemisťuje ji na malý počet vysoce hodnotných momentů:

- **Vyjasnění záměru** — přeměna nepřehledného požadavku na jeden koherentní cíl bez skrytých protimluvů
- **Schválení specifikace** — potvrzení, že zmrazené porozumění je správná věc k budování
- **Revize konečného produktu** — primární kontrolní bod, kde člověk rozhoduje, zda je výsledek přijatelný

### 2. Nasměrujte na nejmenší bezpečnou cestu

[Section titled “2. Nasměrujte na nejmenší bezpečnou cestu”](#2-nasm%C4%9Brujte-na-nejmen%C5%A1%C3%AD-bezpe%C4%8Dnou-cestu)

Jakmile je cíl jasný, workflow rozhodne, zda jde o skutečnou jednorázovou změnu nebo zda potřebuje plnější cestu. Malé změny s nulovým blast-radius mohou jít přímo k implementaci. Vše ostatní prochází plánováním, aby model měl silnější hranici před tím, než poběží déle samostatně.

### 3. Běžte déle s menším dozorem

[Section titled “3. Běžte déle s menším dozorem”](#3-b%C4%9B%C5%BEte-d%C3%A9le-s-men%C5%A1%C3%ADm-dozorem)

Po tomto rozhodnutí o směrování může model nést více práce samostatně. Na plnější cestě se schválená specifikace stává hranicí, proti které model provádí s menším dozorem, což je celý smysl designu.

### 4. Diagnostikujte selhání na správné vrstvě

[Section titled “4. Diagnostikujte selhání na správné vrstvě”](#4-diagnostikujte-selh%C3%A1n%C3%AD-na-spr%C3%A1vn%C3%A9-vrstv%C4%9B)

Pokud je implementace špatná, protože byl špatný záměr, oprava kódu je špatná oprava. Pokud je kód špatný, protože specifikace byla slabá, oprava diffu je také špatná oprava. Workflow je navržen tak, aby diagnostikoval, kde selhání vstoupilo do systému, vrátil se na tu vrstvu a přegeneroval odtamtud.

Nálezy revize se používají k rozhodnutí, zda problém pochází ze záměru, generování specifikace nebo lokální implementace. Pouze skutečně lokální problémy se opravují lokálně.

### 5. Přiveďte člověka zpět pouze když je potřeba

[Section titled “5. Přiveďte člověka zpět pouze když je potřeba”](#5-p%C5%99ive%C4%8Fte-%C4%8Dlov%C4%9Bka-zp%C4%9Bt-pouze-kdy%C5%BE-je-pot%C5%99eba)

Interview o záměru je human-in-the-loop, ale není to stejný druh přerušení jako opakující se kontrolní bod. Workflow se snaží udržet tyto opakující se kontrolní body na minimu. Po úvodním formování záměru se člověk vrací hlavně tehdy, když workflow nemůže bezpečně pokračovat bez úsudku a na konci, když je čas zkontrolovat výsledek.

- **Řešení mezer v záměru** — vstoupení zpět, když revize prokáže, že workflow nemohl bezpečně odvodit, co bylo myšleno

Vše ostatní je kandidátem na delší autonomní provádění. Tento kompromis je záměrný. Starší vzory věnují více lidské pozornosti nepřetržitému dozoru. Quick Dev věnuje více důvěry modelu, ale šetří lidskou pozornost pro momenty, kde má lidské uvažování nejvyšší páku.

## Proč systém revize záleží

[Section titled “Proč systém revize záleží”](#pro%C4%8D-syst%C3%A9m-revize-z%C3%A1le%C5%BE%C3%AD)

Fáze revize není jen pro hledání chyb. Je tu pro směrování korekce bez ničení momentum.

Tento workflow funguje nejlépe na platformě, která může spouštět sub-agenty, nebo alespoň vyvolat jiné LLM přes příkazovou řádku a čekat na výsledek. Pokud to vaše platforma nativně nepodporuje, můžete přidat skill, který to udělá. Bezcontextové sub-agenty jsou základním kamenem designu revize.

Agentní revize často selhávají dvěma způsoby:

- Generují příliš mnoho nálezů, čímž nutí člověka prosévat šum.
- Vychýlí aktuální změnu odhalením nesouvisejících problémů a přemění každý běh na ad-hoc úklidový projekt.

Quick Dev řeší obojí tím, že s revizí zachází jako s triáží.

Některé nálezy patří k aktuální změně. Některé ne. Pokud je nález náhodný spíše než kauzálně vázaný na aktuální práci, workflow ho může odložit místo nucení člověka ho okamžitě řešit. To udržuje běh zaměřený a zabraňuje náhodným tangentám ve spotřebování rozpočtu pozornosti.

Ta triáž bude někdy nedokonalá. To je přijatelné. Obvykle je lepší špatně posoudit některé nálezy než zaplavit člověka tisíci nízkohodnotných revizních komentářů. Systém optimalizuje pro kvalitu signálu, ne vyčerpávající recall.