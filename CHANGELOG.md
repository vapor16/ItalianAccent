# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- `PRIVACY.md`; directory listing metadata in `plugin.json` (displayName, icon, privacy/support/documentation URLs, keywords); `claude-directory/` package for the Claude Public Directory.

## [1.0.0] - 2026-11-25

First public release.

### Added
- `italianaccent` Agent Skill: explicit activation, `/italianaccent` commands (help, list, status, random, off,
  reset, mode selection, intensity 1–5, vulgarity 0–5, proverbs/idioms/humor/sarcasm/translation toggles, combined
  flags), natural-language activation, alias/accent-insensitive mode resolution, progressive disclosure.
- Eleven experimental dialect modes: Trimone (Barese), Mbare (Catanese), Wallera (Napoletano), Daje (Romanesco),
  Mena (Leccese — Salentino centrale), Minchia (Palermitano), Belin (Genovese), Bischero (Fiorentino),
  Boia dé (Livornese), Pirla (Milanese), Potà (Bergamasco).
- Sourced knowledge base per mode (lexicon, proverbs and idioms, uncensored profanity with intensity levels),
  JSON Schemas, source registry and per-profile bibliographies.
- Claude Code plugin and marketplace manifests; installable ZIP for Claude.ai.
- Validator (`scripts/validate.py`), pytest suites (structural, linguistic, security, behavioral-format),
  installed-skill AI-assisted evaluation runner and results.
- Documentation (EN/IT), contribution guide, issue/PR templates, GitHub Actions workflows (validate on push/PR, release-check on tags; read-only permissions).

### Changed
- Linguistic corrections from an external audit (`research/ITALIANACCENT_RESEARCH.md`): phonetic rules made
  lexically constrained, contemporary speech by default, corrected Apulian metaphony statement, Turre expressions
  added to Mena with Scorrano/Torrepaduli provenance, personality guidance against repetition and caricature.
- Final colloquial pass: contemporary slang, vulgar idioms and banter for all eleven modes (e.g. the Neapolitan
  *bucchino* family in Wallera; *minchia* constructions in Minchia; VRC-D Romanesco banter in Daje; Garrisi
  *cazzu* compounds in Mena; *bale* family in Potà; *bauscia/casciavit* in Pirla), each with pragmatic uses and
  sources; community-sourced items are marked `unverified`.

### Known limitations
- All profiles are `experimental`: no native-speaker review yet.
