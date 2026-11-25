# Correction brief (v1.0.0)

ItalianAccent is a fun, irreverent skill: the user should feel they talk to someone from the city, not read a textbook. Your job: apply the audit corrections for YOUR profiles only, minimally and verifiably.

Read: `research/ITALIANACCENT_RESEARCH.md` (sections for your profiles), `docs/adding-a-dialect.md` (contract), your profiles' files in `skills/italianaccent/references/dialects/<id>/`.

Rules:
1. Verify each disputed claim against the source cited in the audit (WebFetch/WebSearch, free tools only) before changing it. If you cannot verify, apply the conservative option (soften/mark as tendency, or mark entry `unverified` / `generation_allowed: false`), never invent.
2. Edit existing files only. No new files, parameters, schemas or architecture. Keep JSON schema-valid. Do not touch catalog.json, research/sources.json, SKILL.md, sources.md or other profiles. New sources → `research/raw/<id>-sources.json` (same format). No git.
3. In profile.md: turn phonetic rules into *lexically constrained* guidance (apply only to attested forms listed in the profile/lexicon; never to arbitrary words, names, technical terms). Default to the contemporary spoken variety; historical/classical forms only as reference.
4. Personality: in profile.md add or sharpen a short "How to sound like a local" note in §11 (humor/irony): spontaneous, sarcastic, varied interjections; the mode identifier word and any single interjection appear at most about once per answer; no phonetic caricature.
5. examples.md: fix unnatural or repetitive lines (e.g. identifier or the same interjection repeated in every sentence, caricatural spellings, forms contradicting the corrected rules). Keep it AI-illustrative, uncensored, technically correct. Don't rewrite what is fine.
6. Profanity: entries that are `unverified` AND `blasphemy: true` must get `"generation_allowed": false` unless you verify them; remove them from profile palettes.
7. Run `python3 scripts/validate.py --profile <id>` for each profile (0 errors expected) and `python3 -m pytest -q tests/structural tests/linguistic`.

Final reply ≤ 15 lines: per profile, what you verified (with URL), what you changed, what you left and why.
