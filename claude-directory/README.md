# ItalianAccent

**Artificial Intelligence. Authentic Italian Attitude.**

ItalianAccent is an open-source Agent Skill that makes Claude answer like someone from an Italian city: the local
variety's grammar, syntax and vocabulary, plus slang, proverbs, idioms, humor, sarcasm and uncensored profanity.
It is a declarative skill (Markdown and JSON only, no executable code).

> **Adults only — explicit language.** Active modes use vulgar language, insults and imprecations by default
> (vulgarity 5). Nothing changes until you explicitly activate a mode in the current conversation, and you can lower
> vulgarity to 0 or switch ItalianAccent off at any time. "Uncensored" applies only to the spelling of otherwise
> permitted expressions: Claude's safety rules, refusals and warnings always apply. ItalianAccent is a linguistic
> and humor skill — it does not produce erotic content, harass real people or bypass safeguards.

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

## Examples

No account, sample data or external service is needed: everything works directly from the installed skill.

1. `/italianaccent:italianaccent wallera`, then *"Spiegami Docker come se fossimo al bar."* — a technically correct
   Docker explanation in Neapolitan, with local banter.
2. `/italianaccent:italianaccent mena --vulgarity 0`, then *"Dammi un consiglio con un proverbio."* — Leccese advice
   with a traditional proverb and no profanity.
3. `/italianaccent:italianaccent daje --intensity 2`, then *"Ho passato cinque ore a cercare un punto e virgola."* —
   light Roman regional Italian with debugging tips; `/italianaccent:italianaccent off` returns to normal.

## Troubleshooting

- **Command not found:** as a plugin the command is `/italianaccent:italianaccent`; or say "Activate ItalianAccent in
  Daje mode".
- **Answers in standard Italian:** re-activate the mode (state lasts only for the current conversation) or set
  `intensity 5`.
- **Too much or too little profanity:** `vulgarity 0`–`5`.
- **"Mode not found" or "planned":** run the command without arguments to see the eleven available modes.

## Privacy

ItalianAccent is text only: no data collection, network access, memory or chat-history access, credentials or
external services. See the privacy policy below.

## Links

- Documentation: https://github.com/vapor16/ItalianAccent/blob/main/README.md
- Privacy policy: https://github.com/vapor16/ItalianAccent/blob/main/PRIVACY.md
- Support: https://github.com/vapor16/ItalianAccent/issues
- License: MIT (see LICENSE). Third-party sources: THIRD_PARTY_NOTICES.md
