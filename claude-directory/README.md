# ItalianAccent

**Artificial Intelligence. Authentic Italian Attitude.**

ItalianAccent is an open-source Agent Skill that makes Claude answer like someone from an Italian city: the local
variety's grammar, syntax and vocabulary, plus slang, proverbs, idioms, humor, sarcasm and uncensored profanity.
It is a declarative skill (Markdown and JSON only, no executable code).

> **Adults only — explicit language.** Active modes use vulgar language, insults and imprecations by default
> (vulgarity 5). Nothing changes until you explicitly activate a mode, and you can lower vulgarity to 0 or switch
> ItalianAccent off at any time. The host model's safety rules always apply.

## Modes

| Mode | Variety | Region |
|---|---|---|
| `trimone` | Barese | Puglia |
| `mena` | Leccese (Salentino centrale) | Puglia |
| `wallera` | Napoletano | Campania |
| `daje` | Romanesco | Lazio |
| `mbare` | Catanese | Sicilia |
| `minchia` | Palermitano | Sicilia |
| `belin` | Genovese | Liguria |
| `bischero` | Fiorentino | Toscana |
| `boiade` (Boia dé) | Livornese | Toscana |
| `pirla` | Milanese | Lombardia |
| `pota` (Potà) | Bergamasco | Lombardia |

All modes are **experimental**: researched from documented sources but not yet reviewed by native speakers, so
expect mistakes and local differences.

## Install

```text
/plugin install italianaccent --marketplace vapor16/italianaccent
```

## Usage

Installed as a plugin, the command is namespaced:

```text
/italianaccent:italianaccent                   help and list of modes
/italianaccent:italianaccent wallera           activate (dialect intensity 5, vulgarity 5)
/italianaccent:italianaccent daje --intensity 3 --vulgarity 2
/italianaccent:italianaccent vulgarity 0       no profanity, dialect kept
/italianaccent:italianaccent intensity 2       regional Italian instead of full dialect
/italianaccent:italianaccent proverbs off      also: idioms, humor, sarcasm, translation on|off
/italianaccent:italianaccent status
/italianaccent:italianaccent off               back to normal
```

Natural language also works: "Activate ItalianAccent in Daje mode." Code, commands and technical facts are never
altered; only the prose around them changes.

## Links

- Documentation: https://github.com/vapor16/ItalianAccent/blob/main/README.md
- Privacy policy: https://github.com/vapor16/ItalianAccent/blob/main/PRIVACY.md
- Support: https://github.com/vapor16/ItalianAccent/issues
- License: MIT (see LICENSE). Third-party sources: THIRD_PARTY_NOTICES.md
