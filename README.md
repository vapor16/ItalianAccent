# ItalianAccent

**Artificial Intelligence. Authentic Italian Attitude.**

ItalianAccent is an open-source [Agent Skill](https://agentskills.io) that makes your AI assistant speak an authentic
Italian local variety — Neapolitan, Barese, Catanese, Romanesco, Salentino and many more — with real grammar and
syntax, local vocabulary, traditional proverbs, idioms, irony, and **uncensored** stylistic profanity.

It is not a translator and not "standard Italian with one dialect word on top": once a mode is active, the whole
conversation (including technical explanations and debugging) is rebuilt in the chosen variety, while code,
commands and technical facts stay exactly correct.

[Leggi in italiano](README.it.md)

> [!WARNING]
> **Explicit language.** ItalianAccent contains and generates vulgar language, insults, imprecations and (at the
> maximum level) blasphemies that are attested in popular speech. This is a deliberate, opt-in feature: nothing
> changes until **you** activate a mode, and the vulgarity level can be lowered to 0 at any time
> (`/italianaccent vulgarity 0`). The host model's safety rules always apply; ItalianAccent contains no jailbreaks.

## Features

- **Real dialect, whole answer** — vocabulary, morphology, verb paradigms, syntax, word order, negation and
  discourse particles per variety, at 5 intensity levels.
- **Uncensored profanity, configurable 0–5** — default 5 on activation; contextual (friendly vs hostile, frustration,
  surprise, affection), never asterisks, never disclaimers.
- **Proverbs & idioms** — traditional sayings used spontaneously when they sharpen the point, with source,
  meaning and register for every entry.
- **Humor & sarcasm** through language devices, not regional stereotypes.
- **Developer-safe** — code blocks, identifiers, SQL, shell commands, paths and errors are never altered.
- **Documented, sourced knowledge base** — JSON Schema–validated entries, each with provenance and sources.
- **Lightweight & private** — Markdown + JSON only. No server, no API key, no telemetry, no network at runtime.

## Supported modes

<!-- CATALOG:START -->
| Mode | Variety | Region | Meaning of the mode name | Status |
|---|---|---|---|---|
| **Wallera** (`wallera`) | Napoletano | Campania | Neapolitan 'hernia / scrotum'; used in 'scassare 'a uallera' = to bust one's balls (commercial spelling of uallera) | experimental |
| **Daje** (`daje`) | Romanesco | Lazio | Roman 'come on! let's go!' | experimental |
| **Belin** (`belin`) | Genovese | Liguria | Genoese vulgar 'dick', all-purpose exclamation | experimental |
| **Pirla** (`pirla`) | Milanese | Lombardia | Milanese 'idiot, jerk' | experimental |
| **Potà** (`pota`) | Bergamasco | Lombardia | Bergamasque all-purpose interjection (originally vulgar 'female genitals') | experimental |
| **Mena** (`mena`) | Leccese — Salentino centrale | Puglia | Salentine 'come on / go on!' (from menare) | experimental |
| **Trimone** (`trimone`) | Barese | Puglia | Barese insult: 'idiot, dumbass' | experimental |
| **Mbare** (`mbare`) | Catanese | Sicilia | Sicilian vocative 'mate, buddy' (from 'cumpari/'mbari, godfather/companion) | experimental |
| **Minchia** (`minchia`) | Palermitano | Sicilia | Sicilian vulgar 'dick', used as all-purpose exclamation | experimental |
| **Bischero** (`bischero`) | Fiorentino | Toscana | Florentine 'fool, sucker' | experimental |
| **Boia dé** (`boiade`) | Livornese | Toscana | Livornese exclamation 'damn!, wow!' (boia = executioner, used as an intensifier, + the interjection dé) | experimental |

**11 available modes covering 7 of 20 regions** (Campania, Lazio, Liguria, Lombardia, Puglia, Sicilia, Toscana). 67 further varieties are listed as `planned` in [catalog.json](skills/italianaccent/references/catalog.json) and are not activatable yet.
<!-- CATALOG:END -->

Every mode name is an authentic local word chosen to be memorable; the *Meaning* column explains it for non-Italian
speakers. Many of these varieties are, linguistically, independent Romance languages or dialects — see
[Linguistic methodology](docs/linguistic-methodology.md). "Italian dialects" is used as the popular umbrella term.

## Installation

The installable unit is the folder **`skills/italianaccent/`** (not the whole repository).

### With the Skills CLI (Claude Code, Codex, Cursor and other agents) — Linux, macOS, Windows

Requires Node.js 22.20+.

```bash
npx skills add vapor16/ItalianAccent --skill italianaccent
```

Useful flags (from the [skills CLI docs](https://github.com/vercel-labs/skills)): `-a claude-code` / `-a codex` /
`-a cursor` to choose the agent, `-g` for a global (user-level) install, `--list` to only list the skills in the repo.

### As a Claude Code plugin

```text
/plugin marketplace add vapor16/ItalianAccent
/plugin install italianaccent@italianaccent
```

Plugin skills are namespaced: invoke with `/italianaccent:italianaccent <mode>`.

### Manual / git clone

macOS / Linux:

```bash
git clone https://github.com/vapor16/ItalianAccent.git
mkdir -p ~/.claude/skills && cp -R ItalianAccent/skills/italianaccent ~/.claude/skills/
```

Windows (PowerShell):

```powershell
git clone https://github.com/vapor16/ItalianAccent.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse ItalianAccent\skills\italianaccent "$env:USERPROFILE\.claude\skills\"
```

For other agents, copy the same folder into that agent's skills directory (e.g. `.agents/skills/` or the path your
agent documents).

### Claude.ai

Download `italianaccent-1.0.0.zip` from the [v1.0.0 release](https://github.com/vapor16/ItalianAccent/releases/tag/v1.0.0)
and upload it in **Customize → Skills → Upload a skill** (code execution must be enabled). Then activate in natural
language: *"Activate ItalianAccent in Wallera mode."*

## Quick start

```text
/italianaccent                 # help + catalog
/italianaccent wallera         # Neapolitan, intensity 5, vulgarity 5, proverbs on
Che cos'è Docker?
/italianaccent vulgarity 2     # tone it down
/italianaccent daje            # switch to Romanesco
/italianaccent off             # back to normal
```

Natural language works too: *"Activate ItalianAccent in Wallera mode."* · *"Attiva ItalianAccent in modalità
Trimone."* · *"Rispondimi utilizzando il dialetto catanese con ItalianAccent."*

## Commands

| Command | Description |
|---|---|
| `/italianaccent`, `help` | Help and catalog of available modes |
| `list` | Available (and planned) modes |
| `<mode>` | Activate or switch mode (case/accent-insensitive; aliases like `uallera`, `boia dé`, `potà`) |
| `<mode> --intensity N --vulgarity N` | Activate with options (also `--proverbs`, `--idioms`, `--humor`, `--sarcasm`, `--translation on/off`) |
| `random` | Random available mode |
| `status` | Current mode and configuration |
| `intensity 1-5` | Dialect intensity |
| `vulgarity 0-5` | Profanity level |
| `proverbs on/off`, `idioms on/off`, `humor on/off`, `sarcasm on/off` | Toggle features |
| `translation on/off` | Short Italian glosses after proverbs and hard sentences |
| `reset` | Restore defaults, keep the mode |
| `off` | Deactivate ItalianAccent |

On platforms without slash commands, say the same thing in words ("ItalianAccent: list modes").

## Configuration

Defaults applied when you activate a mode ([`defaults.json`](skills/italianaccent/references/defaults.json)):

```json
{ "dialect_intensity": 5, "vulgarity": 5, "proverbs": true, "idioms": true, "humor": true,
  "sarcasm": true, "italian_translation": false, "stylistic_censorship": false }
```

| Dialect intensity | | Vulgarity | |
|---|---|---|---|
| 1 | Italian with light local touches | 0 | none |
| 2 | Regional Italian | 1 | light |
| 3 | Natural Italian ↔ dialect alternation | 2 | moderate colloquial |
| 4 | Dialect-dominant | 3 | natural vulgar speech |
| 5 | Maximum authenticity the resources allow | 4 | strongly vulgar |
| | | 5 | maximum stylistic intensity, uncensored spelling |

## Usage examples

Same prompt, different modes — see [examples/](examples/) and each profile's `examples.md`. All examples are
**AI-generated illustrations** of the documented rules, not transcriptions of native speakers.

<!-- EXAMPLES:START -->
<!-- EXAMPLES:END -->

## Platform compatibility

<!-- COMPAT:START -->
| Platform | Status |
|---|---|
| Claude Code (skill and plugin) | Documented · structurally compatible · locally validated |
| Claude.ai (ZIP upload) | Documented · structurally compatible · not yet tested |
| Codex, Cursor (via Skills CLI) | Documented by the CLI · structurally compatible · not yet tested |
| Other Agent Skills hosts | Structurally compatible · not yet tested |
<!-- COMPAT:END -->

Details and persistence notes: [docs/platform-compatibility.md](docs/platform-compatibility.md).

**Persistence:** a mode stays active for the whole conversation (the skill re-reads its profile after context
compaction). It does not carry over to new sessions; re-activate it. ItalianAccent never edits your `CLAUDE.md`,
`AGENTS.md` or settings.

## Linguistic methodology & profile maturity

Profiles are researched from dictionaries, academic and institutional resources, Wiktionary/Wikipedia, public-domain
literature and (for colloquial and vulgar items, with lower reliability) popular sources. Every entry records its
provenance and sources; meanings are original annotations, not copied dictionary text. See
[methodology](docs/linguistic-methodology.md), [source policy](docs/source-policy.md),
[sources registry](research/sources.json) and [third-party notices](THIRD_PARTY_NOTICES.md).

| Maturity | Meaning |
|---|---|
| `planned` | Listed, not usable yet |
| `experimental` | Researched from documented sources; **no native-speaker review yet** |
| `community-reviewed` | Reviewed by ≥2 local speakers (linked public reviews) |
| `verified` | Community-reviewed + linguist or broad speaker review |

**All v1.0.0 modes are `experimental`.**

## Limitations

- No profile has been reviewed by native speakers yet. Expect mistakes, especially in spelling (most varieties
  have no standard orthography) and in rare forms. Please report them!
- Knowledge bases are much smaller than a real dictionary; coverage targets are documented per profile.
- Each profile follows one reference norm (usually the main city); local variation is large.
- Profanity sources are mostly popular/community sources.
- Output quality depends on the host model; tested behaviour is documented in `tests/behavioral/results/`.
- Persistence is per conversation.

## Privacy

ItalianAccent is plain files. It does not collect data, send conversations anywhere, require an account, a server,
an API key, a database or extra MCP servers. (The third-party Skills CLI has its own anonymous install telemetry,
which you can disable with `DISABLE_TELEMETRY=1`.)

## Contributing

Local speakers, linguists and developers are very welcome: add words, proverbs, profanity, fix grammar, report
invented forms or contamination, or review a profile. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/adding-a-dialect.md](docs/adding-a-dialect.md).

```bash
python -m pip install pytest jsonschema pyyaml
python scripts/validate.py && python -m pytest
```

## Roadmap

- **v1.0.0** (this release): eleven experimental modes covering Apulia, Campania, Lazio, Liguria, Lombardy, Sicily
  and Tuscany; configurable profanity, proverbs, idioms, commands, tests, documentation, distribution.
- **Next**: native-speaker reviews and corrections (first `community-reviewed` profiles), richer vocabularies and
  proverb collections.
- **Future modes**: research already started for Romagnolo (*pataca*), Bolognese (*socmel*) and Venetian (*ostrega*)
  is parked in [`research/future-profiles/`](research/future-profiles/); more regional varieties are listed as
  `planned` in the catalog. New modes ship only when they are authentic and sourced.

## License

[MIT](LICENSE) for ItalianAccent's code and original content. Third-party material keeps its own license — see
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
