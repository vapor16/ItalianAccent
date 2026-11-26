# ItalianAccent

**Artificial Intelligence. Authentic Italian Attitude.**

Declarative Agent Skill (Markdown + JSON only, no executable code) that makes Claude speak one of eleven Italian
local varieties with their grammar, vocabulary, proverbs, idioms, humor and **uncensored profanity**: Trimone
(Barese), Mbare (Catanese), Wallera (Napoletano), Daje (Romanesco), Mena (Leccese), Minchia (Palermitano),
Belin (Genovese), Bischero (Fiorentino), Boia dé (Livornese), Pirla (Milanese), Potà (Bergamasco).

**Explicit language, opt-in only.** Nothing changes until you activate a mode; vulgarity can be lowered to 0 at any
time. The host model's safety rules always apply. All modes are experimental (no native-speaker review yet).

## Install

```text
/plugin install italianaccent --marketplace vapor16/italianaccent
```

## Usage

```text
/italianaccent:italianaccent              help and list of modes
/italianaccent:italianaccent wallera      activate (intensity 5, vulgarity 5)
/italianaccent:italianaccent vulgarity 2  tone it down
/italianaccent:italianaccent off          back to normal
```

Natural language also works: "Activate ItalianAccent in Daje mode."

Source, documentation and contributions: https://github.com/vapor16/ItalianAccent — MIT License (see LICENSE);
third-party sources in THIRD_PARTY_NOTICES.md.
