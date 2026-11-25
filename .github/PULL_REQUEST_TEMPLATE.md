## What does this PR change?

<!-- e.g. "Adds 30 Barese proverbs", "Fixes Napoletano plural articles", "New mode: belin" -->

## Type

- [ ] Linguistic content (vocabulary / grammar / proverbs / profanity / examples)
- [ ] New mode
- [ ] Skill instructions (SKILL.md / references)
- [ ] Tests / CI / scripts
- [ ] Documentation

## Linguistic checklist (if applicable)

- [ ] Every attested entry cites a source registered in `research/sources.json`.
- [ ] Meanings are written in my own words (no copied dictionary text).
- [ ] Nothing invented; uncertain items are marked `unverified`.
- [ ] No near-duplicates (spelling variants go into `variants`).
- [ ] No forms borrowed from neighbouring varieties.
- [ ] No stereotypes about people; slurs against protected groups have `generation_allowed: false`.
- [ ] Area/town of my usage (if I am a native speaker): ______

## Checks

- [ ] `python scripts/validate.py` passes
- [ ] `python -m pytest` passes
