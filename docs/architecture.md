# Architecture

ItalianAccent is a single [Agent Skill](https://agentskills.io/specification): Markdown instructions plus JSON/Markdown
knowledge files. There is no backend, server, database, MCP server, network call or runtime script.

```
skills/italianaccent/              <- the installable skill (this folder is what gets copied/zipped)
├── SKILL.md                       <- entry point: activation guard, commands, resolution, loading order, rules
└── references/
    ├── catalog.json               <- every mode: id, display name, aliases, variety, region, maturity, availability
    ├── defaults.json              <- default configuration (intensity 5, vulgarity 5, ...)
    ├── commands.md                <- full command grammar and response templates
    ├── behavior.md                <- intensity/vulgarity levels, proverbs/humor rules, technical integrity, situations
    ├── dialect-loading.md         <- per-file loading guide, fallbacks, conversation state
    └── dialects/<id>/             <- one self-contained profile per mode
        ├── metadata.json  profile.md  lexicon.json  proverbs.json  profanity.json  examples.md  sources.md
schemas/                           <- JSON Schema (Draft 2020-12) for every structured file
scripts/validate.py                <- dev/CI validator, stats and ZIP builder (never used at runtime)
tests/                             <- pytest: structural, linguistic, security, behavioral-format; behavioral eval cases
research/                          <- sources registry, progress state, research logs (not shipped in the skill)
.claude-plugin/                    <- Claude Code plugin + marketplace manifests (repo root = plugin root)
```

## Progressive disclosure

1. At startup the host loads only `name` + `description` (~100 tokens). The description restricts activation to
   explicit requests.
2. On invocation the host loads `SKILL.md` (~120 lines).
3. On activation of a mode the agent reads `defaults.json`, `behavior.md` and the profile's `profile.md` — the
   compact, sufficient specification of the variety.
4. Large JSON files are consulted on demand (a word, a proverb, a profanity at a given intensity). Other dialects
   are never loaded together.

## Runtime state

The active mode and configuration live in the conversation (see `dialect-loading.md`). No files are written; no
hooks; no global config edits. Persistence across sessions is opt-in and manual.

## Design decisions

| Decision | Reason |
|---|---|
| Only portable frontmatter keys | Claude.ai uploads and the Skills API reject Claude-Code-only keys; activation guard is in the description and body instead of `disable-model-invocation`. |
| `profile.md` per dialect as the main runtime spec | One read gives the model the grammar, syntax and style it needs; JSON is for lookup. |
| Merged files (idioms→proverbs.json, interjections→lexicon.json, grammar/syntax/personality→profile.md) | Fewer reads, same information; every field required by the specification is kept in the schemas. |
| Catalog holds planned varieties | Shows real coverage honestly; planned modes are not activatable. |
| Repo root is also the plugin root | `marketplace.json` with `"source": "./"`; the default `skills/` scan finds the skill. |
| Python only for validation | Keeps the skill self-contained; CI needs no secrets. |
