---
title: Pokročilá elicitace
url: https://docs.bmad-method.org/cs/explanation/advanced-elicitation/
source: sitemap
fetched_at: 2026-04-08T11:29:04.242261463-03:00
rendered_js: false
word_count: 280
summary: Tento dokument popisuje koncept pokročilé elicitace, což je strukturovaný proces zpětné kontroly, při kterém uživatel místo obecného požádání o vylepšení vybere konkrétní metodu uvažování, kterou AI aplikuje na vlastní výstup. To zajišťuje hloubkový a cílenější přehled materiálu.
tags:
    - pokročilá-elicitace
    - metody-uvažování
    - proces-zpětné-kontroly
    - nlp-techniky
    - llm-optimalizace
category: concept
---

Přimějte LLM přehodnotit, co právě vygeneroval. Vyberete metodu uvažování, LLM ji aplikuje na svůj vlastní výstup, a vy rozhodnete, zda si vylepšení ponecháte.

## Co je pokročilá elicitace?

[Section titled “Co je pokročilá elicitace?”](#co-je-pokro%C4%8Dil%C3%A1-elicitace)

Strukturovaný druhý průchod. Místo žádání AI, aby „to zkusila znovu“ nebo „to zlepšila“, vyberete specifickou metodu uvažování a AI přezkoumá svůj vlastní výstup přes tento objektiv.

Rozdíl je podstatný. Vágní požadavky produkují vágní revize. Pojmenovaná metoda vynucuje konkrétní úhel útoku, odhaluje postřehy, které by generický pokus přehlédl.

- Poté, co workflow vygeneruje obsah a chcete alternativy
- Když výstup vypadá v pořádku, ale tušíte, že je v něm víc hloubky
- K zátěžovému testování předpokladů nebo nalezení slabých míst
- Pro důležitý obsah, kde přehodnocení pomáhá

Workflow nabízejí pokročilou elicitaci v rozhodovacích bodech — poté, co LLM něco vygeneruje, budete dotázáni, zda ji chcete spustit.

1. LLM navrhne 5 relevantních metod pro váš obsah
2. Vyberete jednu (nebo zamícháte pro jiné možnosti)
3. Metoda je aplikována, vylepšení zobrazena
4. Přijměte nebo zahoďte, opakujte nebo pokračujte

K dispozici jsou desítky metod uvažování. Několik příkladů:

- **Pre-mortem analýza** — Předpokládejte, že projekt už selhal, a zpětně hledejte proč
- **Myšlení z prvních principů** — Odstraňte předpoklady, znovu postavte od základní pravdy
- **Inverze** — Zeptejte se, jak zaručit selhání, a poté se tomu vyhněte
- **Red Team vs Blue Team** — Napadněte vlastní práci, pak ji braňte
- **Sokratovské dotazování** — Zpochybněte každé tvrzení otázkou „proč?“ a „jak víte?“
- **Odstranění omezení** — Odstraňte všechna omezení, podívejte se, co se změní, selektivně je přidejte zpět
- **Mapování zainteresovaných stran** — Přehodnoťte z perspektivy každé zainteresované strany
- **Analogické uvažování** — Najděte paralely v jiných oblastech a aplikujte jejich lekce

A mnoho dalších. AI vybírá nejrelevantnější možnosti pro váš obsah — vy si vyberete, kterou spustit.