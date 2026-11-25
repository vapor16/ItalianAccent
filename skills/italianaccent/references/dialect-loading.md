# ItalianAccent — loading and state

## Files per profile

`references/dialects/<id>/`

| File | When to read | Content |
|---|---|---|
| `metadata.json` | optional, for `status`/`help` details | identity, classification, maturity |
| `profile.md` | **always on activation**, again after compaction | orthography, phonology, morphology, verbs, syntax, core lexicon, interjections, profanity palette, quick proverbs, humor devices, intensity & transformation guides, contamination guard |
| `lexicon.json` | when you need a specific word | `entries[]`: `term`, `variants`, `category`, `meaning_it`, `meaning_en`, `register`, `vulgarity` |
| `proverbs.json` | when a proverb/idiom would help | `entries[]`: `type`, `original`, `meaning_it`/`meaning_en`, `usage_context`, `vulgarity` |
| `profanity.json` | when choosing vulgar expressions | `entries[]`: `original`, `intensity` (1–5), `usage.friendly/hostile`, `blasphemy`, `generation_allowed` |
| `examples.md` | optional calibration of tone | AI-illustrative sample conversations |
| `sources.md` | only if the user asks about sources | bibliography |

Prefer targeted search (grep/find tools, or reading the relevant part) over loading large JSON files whole.

## Fallbacks

- If the host cannot read files: tell the user ItalianAccent needs file access to the skill directory, and stop.
- If a profile file is missing: use what exists, mention the gap once, never fill it by inventing.
- If `catalog.json` cannot be read: accept only the five core ids (`mbare`, `trimone`, `wallera`, `daje`, `mena`)
  and tell the user the catalog is unavailable.

## Conversation state

Keep this state in mind (no files are written):

```
active_mode: <id | null>
dialect_intensity: 1-5   vulgarity: 0-5
proverbs, idioms, humor, sarcasm, translation: on/off
used_proverbs: [...]     # avoid repetition
```

- The state lives in the conversation only. On a new session ItalianAccent is off.
- Optional, user-initiated persistence: if the user explicitly asks for ItalianAccent to be always on, explain
  they can add a line such as `Always use the italianaccent skill in <mode> mode.` to their own agent
  instructions file (e.g. `CLAUDE.md`, `AGENTS.md`). Never edit those files yourself unless the user asks.
