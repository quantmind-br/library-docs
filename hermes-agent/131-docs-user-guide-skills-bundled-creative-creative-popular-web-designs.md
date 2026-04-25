---
title: Popular Web Designs — 54 production-quality design systems extracted from real websites | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/creative/creative-popular-web-designs
source: crawler
fetched_at: 2026-04-24T17:05:30.94072665-03:00
rendered_js: false
word_count: 719
summary: This document serves as a reference catalog showcasing 54 production-quality design system templates extracted from popular websites. It explains how these ready-made HTML/CSS assets can be used to quickly replicate a site's entire visual identity, including color palettes and typography.
tags:
    - design-system
    - html-css
    - web-templates
    - visual-identity
    - ui-kit
    - reference-guide
category: reference
---

54 production-quality design systems extracted from real websites. Load a template to generate HTML/CSS that matches the visual identity of sites like Stripe, Linear, Vercel, Notion, Airbnb, and more. Each template includes colors, typography, components, layout rules, and ready-to-use CSS values.

SourceBundled (installed by default)Path`skills/creative/popular-web-designs`Version`1.0.0`AuthorHermes Agent + Teknium (design systems sourced from VoltAgent/awesome-design-md)LicenseMIT

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Popular Web Designs

54 real-world design systems ready for use when generating HTML/CSS. Each template captures a site's complete visual language: color palette, typography hierarchy, component styles, spacing system, shadows, responsive behavior, and practical agent prompts with exact CSS values.

## How to Use[​](#how-to-use "Direct link to How to Use")

1. Pick a design from the catalog below
2. Load it: `skill_view(name="popular-web-designs", file_path="templates/<site>.md")`
3. Use the design tokens and component specs when generating HTML
4. Pair with the `generative-widgets` skill to serve the result via cloudflared tunnel

Each template includes a **Hermes Implementation Notes** block at the top with:

- CDN font substitute and Google Fonts `<link>` tag (ready to paste)
- CSS font-family stacks for primary and monospace
- Reminders to use `write_file` for HTML creation and `browser_vision` for verification

## HTML Generation Pattern[​](#html-generation-pattern "Direct link to HTML Generation Pattern")

```html
<!DOCTYPEhtml>
<htmllang="en">
<head>
<metacharset="UTF-8">
<metaname="viewport"content="width=device-width, initial-scale=1.0">
<title>Page Title</title>
<!-- Paste the Google Fonts <link> from the template's Hermes notes -->
<linkhref="https://fonts.googleapis.com/css2?family=..."rel="stylesheet">
<style>
/* Apply the template's color palette as CSS custom properties */
:root{
--color-bg:#ffffff;
--color-text:#171717;
--color-accent:#533afd;
/* ... more from template Section 2 */
}
/* Apply typography from template Section 3 */
body{
font-family:'Inter', system-ui, sans-serif;
color:var(--color-text);
background:var(--color-bg);
}
/* Apply component styles from template Section 4 */
/* Apply layout from template Section 5 */
/* Apply shadows from template Section 6 */
</style>
</head>
<body>
<!-- Build using component specs from the template -->
</body>
</html>
```

Write the file with `write_file`, serve with the `generative-widgets` workflow (cloudflared tunnel), and verify the result with `browser_vision` to confirm visual accuracy.

## Font Substitution Reference[​](#font-substitution-reference "Direct link to Font Substitution Reference")

Most sites use proprietary fonts unavailable via CDN. Each template maps to a Google Fonts substitute that preserves the design's character. Common mappings:

Proprietary FontCDN SubstituteCharacterGeist / Geist SansGeist (on Google Fonts)Geometric, compressed trackingGeist MonoGeist Mono (on Google Fonts)Clean monospace, ligaturessohne-var (Stripe)Source Sans 3Light weight eleganceBerkeley MonoJetBrains MonoTechnical monospaceAirbnb Cereal VFDM SansRounded, friendly geometricCircular (Spotify)DM SansGeometric, warmfigmaSansInterClean humanistPin Sans (Pinterest)DM SansFriendly, roundedNVIDIA-EMEAInter (or Arial system)Industrial, cleanCoinbaseDisplay/SansDM SansGeometric, trustworthyUberMoveDM SansBold, tightHashiCorp SansInterEnterprise, neutralwaldenburgNormal (Sanity)Space GroteskGeometric, slightly condensedIBM Plex Sans/MonoIBM Plex Sans/MonoAvailable on Google FontsRubik (Sentry)RubikAvailable on Google Fonts

When a template's CDN font matches the original (Inter, IBM Plex, Rubik, Geist), no substitution loss occurs. When a substitute is used (DM Sans for Circular, Source Sans 3 for sohne-var), follow the template's weight, size, and letter-spacing values closely — those carry more visual identity than the specific font face.

## Design Catalog[​](#design-catalog "Direct link to Design Catalog")

### AI & Machine Learning[​](#ai--machine-learning "Direct link to AI & Machine Learning")

TemplateSiteStyle`claude.md`Anthropic ClaudeWarm terracotta accent, clean editorial layout`cohere.md`CohereVibrant gradients, data-rich dashboard aesthetic`elevenlabs.md`ElevenLabsDark cinematic UI, audio-waveform aesthetics`minimax.md`MinimaxBold dark interface with neon accents`mistral.ai.md`Mistral AIFrench-engineered minimalism, purple-toned`ollama.md`OllamaTerminal-first, monochrome simplicity`opencode.ai.md`OpenCode AIDeveloper-centric dark theme, full monospace`replicate.md`ReplicateClean white canvas, code-forward`runwayml.md`RunwayMLCinematic dark UI, media-rich layout`together.ai.md`Together AITechnical, blueprint-style design`voltagent.md`VoltAgentVoid-black canvas, emerald accent, terminal-native`x.ai.md`xAIStark monochrome, futuristic minimalism, full monospace

### Developer Tools & Platforms[​](#developer-tools--platforms "Direct link to Developer Tools & Platforms")

TemplateSiteStyle`cursor.md`CursorSleek dark interface, gradient accents`expo.md`ExpoDark theme, tight letter-spacing, code-centric`linear.app.md`LinearUltra-minimal dark-mode, precise, purple accent`lovable.md`LovablePlayful gradients, friendly dev aesthetic`mintlify.md`MintlifyClean, green-accented, reading-optimized`posthog.md`PostHogPlayful branding, developer-friendly dark UI`raycast.md`RaycastSleek dark chrome, vibrant gradient accents`resend.md`ResendMinimal dark theme, monospace accents`sentry.md`SentryDark dashboard, data-dense, pink-purple accent`supabase.md`SupabaseDark emerald theme, code-first developer tool`superhuman.md`SuperhumanPremium dark UI, keyboard-first, purple glow`vercel.md`VercelBlack and white precision, Geist font system`warp.md`WarpDark IDE-like interface, block-based command UI`zapier.md`ZapierWarm orange, friendly illustration-driven

### Infrastructure & Cloud[​](#infrastructure--cloud "Direct link to Infrastructure & Cloud")

TemplateSiteStyle`clickhouse.md`ClickHouseYellow-accented, technical documentation style`composio.md`ComposioModern dark with colorful integration icons`hashicorp.md`HashiCorpEnterprise-clean, black and white`mongodb.md`MongoDBGreen leaf branding, developer documentation focus`sanity.md`SanityRed accent, content-first editorial layout`stripe.md`StripeSignature purple gradients, weight-300 elegance

### Design & Productivity[​](#design--productivity "Direct link to Design & Productivity")

TemplateSiteStyle`airtable.md`AirtableColorful, friendly, structured data aesthetic`cal.md`Cal.comClean neutral UI, developer-oriented simplicity`clay.md`ClayOrganic shapes, soft gradients, art-directed layout`figma.md`FigmaVibrant multi-color, playful yet professional`framer.md`FramerBold black and blue, motion-first, design-forward`intercom.md`IntercomFriendly blue palette, conversational UI patterns`miro.md`MiroBright yellow accent, infinite canvas aesthetic`notion.md`NotionWarm minimalism, serif headings, soft surfaces`pinterest.md`PinterestRed accent, masonry grid, image-first layout`webflow.md`WebflowBlue-accented, polished marketing site aesthetic

### Fintech & Crypto[​](#fintech--crypto "Direct link to Fintech & Crypto")

TemplateSiteStyle`coinbase.md`CoinbaseClean blue identity, trust-focused, institutional feel`kraken.md`KrakenPurple-accented dark UI, data-dense dashboards`revolut.md`RevolutSleek dark interface, gradient cards, fintech precision`wise.md`WiseBright green accent, friendly and clear

### Enterprise & Consumer[​](#enterprise--consumer "Direct link to Enterprise & Consumer")

TemplateSiteStyle`airbnb.md`AirbnbWarm coral accent, photography-driven, rounded UI`apple.md`ApplePremium white space, SF Pro, cinematic imagery`bmw.md`BMWDark premium surfaces, precise engineering aesthetic`ibm.md`IBMCarbon design system, structured blue palette`nvidia.md`NVIDIAGreen-black energy, technical power aesthetic`spacex.md`SpaceXStark black and white, full-bleed imagery, futuristic`spotify.md`SpotifyVibrant green on dark, bold type, album-art-driven`uber.md`UberBold black and white, tight type, urban energy

## Choosing a Design[​](#choosing-a-design "Direct link to Choosing a Design")

Match the design to the content:

- **Developer tools / dashboards:** Linear, Vercel, Supabase, Raycast, Sentry
- **Documentation / content sites:** Mintlify, Notion, Sanity, MongoDB
- **Marketing / landing pages:** Stripe, Framer, Apple, SpaceX
- **Dark mode UIs:** Linear, Cursor, ElevenLabs, Warp, Superhuman
- **Light / clean UIs:** Vercel, Stripe, Notion, Cal.com, Replicate
- **Playful / friendly:** PostHog, Figma, Lovable, Zapier, Miro
- **Premium / luxury:** Apple, BMW, Stripe, Superhuman, Revolut
- **Data-dense / dashboards:** Sentry, Kraken, Cohere, ClickHouse
- **Monospace / terminal aesthetic:** Ollama, OpenCode, x.ai, VoltAgent