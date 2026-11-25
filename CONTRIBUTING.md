# Contributing to ItalianAccent

Grazie! ItalianAccent lives on contributions from **local speakers, linguists and developers**. Local differences
between towns and provinces are a value, not a problem.

## Ways to contribute

| You want to… | Use |
|---|---|
| Request a new dialect | Issue form "Request a new dialect" |
| Add / correct a word, proverb, vulgar expression or grammar rule | Issue forms, or a PR editing the profile files |
| Report an invented expression, a wrong area, or contamination between dialects | Issue forms "Report invented expression" / "Geographical inaccuracy" / "Dialect contamination" |
| Review a profile as a native speaker | Issue form "Native-speaker review" — this is how profiles become `community-reviewed` |
| Fix code, tests, docs | PR |

## Adding a new mode

Read **[docs/adding-a-dialect.md](docs/adding-a-dialect.md)** — it is self-contained: naming conventions,
required metadata, JSON schemas, source and license requirements, profile sections, validation commands and the
maturity levels. In short:

1. Copy an existing profile folder (`skills/italianaccent/references/dialects/<id>/`) to your new `<id>`.
2. Add the mode to `skills/italianaccent/references/catalog.json`.
3. Add your sources to `research/sources.json`.
4. Run the checks:
   ```bash
   python -m pip install pytest jsonschema pyyaml
   python scripts/validate.py
   python -m pytest
   ```

## Rules for linguistic content

- **Never invent** words, rules or proverbs; mark uncertain items `"provenance": "unverified"`.
- Cite sources; write meanings in your own words; don't copy dictionaries.
- Do not impose a single spelling when legitimate variants exist: add them to `variants`.
- No stereotypes about people of any area. Profanity is welcome and uncensored; slurs against protected groups
  are not generated (`"generation_allowed": false`).
- Native speakers: please state in the PR the town/area your usage comes from. No personal data needed.

## Review process

1. CI must pass (validation + tests).
2. A maintainer checks sources, licenses and format.
3. For linguistic changes, at least one other speaker of the same area is invited to review when possible.
4. Maturity changes (`experimental` → `community-reviewed` → `verified`) require linked public reviews recorded in
   `metadata.json` → `reviews`. See the table in `docs/adding-a-dialect.md`.

## Commit style

[Conventional Commits](https://www.conventionalcommits.org/): `feat: add Belin proverbs`, `fix: correct Barese
plural`, `docs: …`, `test: …`.

By contributing you agree your contribution is licensed under the MIT License and that you have the right to
submit it.
