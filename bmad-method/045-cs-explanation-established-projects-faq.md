---
title: FAQ pro existující projekty
url: https://docs.bmad-method.org/cs/explanation/established-projects-faq/
source: sitemap
fetched_at: 2026-04-08T11:29:07.465891582-03:00
rendered_js: false
word_count: 251
summary: This document is an FAQ addressing common questions about working with existing projects using the BMad Method (BMM). It provides guidance on prerequisite setup, utilizing Quick Flow in legacy codebases, and handling code that deviates from established best practices.
tags:
    - bmad-method
    - faq
    - existing-projects
    - quick-flow
    - code-practices
category: guide
---

Rychlé odpovědi na časté otázky o práci na existujících projektech s BMad Method (BMM).

- [Musím nejdřív spustit document-project?](#mus%C3%ADm-nejd%C5%99%C3%ADv-spustit-document-project)
- [Co když zapomenu spustit document-project?](#co-kdy%C5%BE-zapomenu-spustit-document-project)
- [Mohu použít Quick Flow pro existující projekty?](#mohu-pou%C5%BE%C3%ADt-quick-flow-pro-existuj%C3%ADc%C3%AD-projekty)
- [Co když můj existující kód nedodržuje osvědčené postupy?](#co-kdy%C5%BE-m%C5%AFj-existuj%C3%ADc%C3%AD-k%C3%B3d-nedodr%C5%BEuje-osv%C4%9Bd%C4%8Den%C3%A9-postupy)

### Musím nejdřív spustit document-project?

[Section titled “Musím nejdřív spustit document-project?”](#mus%C3%ADm-nejd%C5%99%C3%ADv-spustit-document-project)

Vysoce doporučeno, zejména pokud:

- Neexistuje žádná dokumentace
- Dokumentace je zastaralá
- AI agenti potřebují kontext o existujícím kódu

Můžete to přeskočit, pokud máte komplexní, aktuální dokumentaci včetně `docs/index.md` nebo budete používat jiné nástroje nebo techniky k usnadnění discovery pro agenta stavějícího na existujícím systému.

Nedělejte si starosti — můžete to udělat kdykoli. Můžete to udělat i během nebo po projektu, aby pomohl udržet dokumentaci aktuální.

### Mohu použít Quick Flow pro existující projekty?

[Section titled “Mohu použít Quick Flow pro existující projekty?”](#mohu-pou%C5%BE%C3%ADt-quick-flow-pro-existuj%C3%ADc%C3%AD-projekty)

Ano! Quick Flow funguje skvěle pro existující projekty. Umí:

- Automaticky detekovat váš existující stack
- Analyzovat existující vzory kódu
- Detekovat konvence a požádat o potvrzení
- Generovat kontextově bohatou specifikaci, která respektuje existující kód

Ideální pro opravy chyb a malé funkce v existujících kódových bázích.

### Co když můj existující kód nedodržuje osvědčené postupy?

[Section titled “Co když můj existující kód nedodržuje osvědčené postupy?”](#co-kdy%C5%BE-m%C5%AFj-existuj%C3%ADc%C3%AD-k%C3%B3d-nedodr%C5%BEuje-osv%C4%9Bd%C4%8Den%C3%A9-postupy)

Quick Flow detekuje vaše konvence a zeptá se: „Mám dodržovat tyto existující konvence?“ Rozhodujete vy:

- **Ano** → Zachovat konzistenci se současnou kódovou bází
- **Ne** → Zavést nové standardy (zdokumentujte proč ve specifikaci)

BMM respektuje vaši volbu — nevynucuje modernizaci, ale nabídne ji.

**Máte otázku, na kterou jste zde nenašli odpověď?** Prosím [vytvořte issue](https://github.com/bmad-code-org/BMAD-METHOD/issues) nebo se zeptejte na [Discordu](https://discord.gg/gk8jAdXWmj), abychom ji mohli přidat!