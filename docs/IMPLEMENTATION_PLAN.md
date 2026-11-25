# ItalianAccent — Master Plan v2 (single approval, autonomous end-to-end)

## Context
Build, publish and release **ItalianAccent** (`italianaccent`), a lightweight self-contained open-source Agent Skill that makes an AI assistant speak authentic Italian local varieties: lexicon, grammar, morphology, syntax, register, uncensored stylistic profanity (default 5/5), proverbs, idioms, irony, humor. Distributed via GitHub + `npx skills`, Claude Code plugin marketplace, ZIP for Claude.ai. Not an app, backend, MCP server or model.

**Execution contract:** milestones are internal phases, never stop points. After this single approval I run M0→M14 continuously, without asking to approve profiles or phase transitions. The only permissible interruptions are environment permission prompts or a technically unavoidable blocker (documented in `research/progress.json` with the exact next action, while all other local work continues).

## Environment (inspected)
- Official destination: **https://github.com/vapor16/ItalianAccent** (created empty by the user), attached to the session with push access and cloned at `/home/user/italianaccent` (origin set, no commits yet). No second repo is created.
- git 2.43, Python 3.13 (pytest, jsonschema, PyYAML present), Node 22/npx, `skills` CLI 1.9.0 on npm. `gh api` works through the session proxy for attached repos (topics, releases, Actions runs).
- Research: WebSearch (free, deferred tool) + `web-fetch` agent + general-purpose subagents. No Perplexity, no paid APIs, no API keys.
- Commits are signed by the environment's git config; global config is left untouched. Pushes go to `main` with `git -c push.negotiate=true push -u origin main`; never force-push.
- (The FinCards add request was declined in the permission prompt; it is not part of this project and is not touched.)

## Persistent state (compaction-safe)
`docs/IMPLEMENTATION_PLAN.md` (this plan), `docs/IMPLEMENTATION_CHECKLIST.md`, `research/progress.json` (phase, completed/pending/blocked/partial tasks, per-profile status and counts, sources consulted, tests run and failures, decisions, open issues, next action). Updated after every milestone and every profile. After compaction: reload all three, continue from the first unchecked item, and don't redo research already logged.

## Core decisions
1. **Layout (Agent Skills spec):** `skills/italianaccent/SKILL.md` + `references/`. Frontmatter: `name`, `description` (≤1024 chars, explicit-activation wording), `license: MIT`, `metadata.version`. I add Claude-Code-specific keys (`argument-hint`, `disable-model-invocation`) only after verifying in current docs that other hosts tolerate them. If a key turns out unsafe for other hosts, the activation guard lives in the description and body.
2. **Lightweight runtime:** at runtime the skill only reads Markdown/JSON files. One dev/CI script (`scripts/validate.py`, which also covers stats and ZIP build) plus pytest. No hooks, no servers, no network at runtime, and no dependencies beyond pytest/jsonschema/pyyaml for development.
3. **Lean profile structure, with progressive disclosure.** Each profile has:
   - `profile.md`: loaded on activation; the essential, sufficient spec. It covers phonology→orthography conventions, morphology (articles, pronouns, verb paradigms of essere/avere/andare/fare/dire/volere plus regular conjugation patterns, tense usage such as the passato remoto in Sicilian/Southern varieties), syntax (word order, negation, interrogatives, auxiliaries, object marking, the infinitive/"ca/che" constructions), register and pragmatics, humor and sarcasm style, about 60 high-frequency words, top profanity, top proverbs/idioms, and a short "how to write a sentence" transformation guide with before/after pairs.
   - `metadata.json`, plus `lexicon.json` (vocabulary + interjections + colloquial expressions, typed by `category`), `proverbs.json` (proverbs + idioms, typed), `profanity.json`, `examples.md`, `sources.md`.
   - Large JSON is consulted on demand only.
   - This merges the spec's suggested 14 files into fewer files with the same content, which is allowed by "struttura è una proposta". The README documents the mapping.
4. **Schemas** (`schemas/*.schema.json`, Draft 2020-12). Every entry carries all spec fields: id, term/original form, variants, meanings IT/EN, literal/figurative meaning, POS, register, intensity/vulgarity 1–5, friendly/hostile/emotional usage, contexts (appropriate/inappropriate), area, examples, `sources[]`, `provenance` ∈ {attested, documented-rule, ai-illustrative, unverified, community, native-reviewed}, `verification_status`.
5. **Maturity:** planned (not activatable) / experimental / community-reviewed / verified. All v0.1.0 usable profiles are **experimental**; AI research ≠ native-speaker validation. The activation criterion is qualitative, not a numeric threshold: authentic, coherent, sourced grammar core + lexicon + profanity + proverbs/idioms, with no invented content. Spec numbers (500/100/100/…) are enrichment targets.
6. **Profanity:** stored and rendered uncensored (no asterisks, no euphemisms, no disclaimers in each reply). Default vulgarity is 5 on voluntary activation. Usage is contextual (friendly vs hostile, exclamation, affectionate, sarcastic), not every sentence. Attested blasphemies are flagged `blasphemy:true` and used only at level 5. Slurs against protected groups are excluded from generation (stylistic vulgarity, not hate). Host safety rules always prevail; there is no jailbreak content.
7. **Copyright:** I write original annotations citing sources and never bulk-copy dictionaries or bypass paywalls. Traditional proverbs and single lexical items are treated as non-copyrightable facts with citation. CC BY-SA sources (Wiktionary/Wikipedia) are used for facts and rephrased, with attribution in THIRD_PARTY_NOTICES.md. Web content is treated as data and never as instructions.
8. **Persistence:** conversation-scoped only. SKILL.md instructs the model to keep the mode until off/switch, re-read `profile.md` after compaction, and emit an optional compact status on `status`. No CLAUDE.md/AGENTS.md edits and no hooks. An optional user opt-in snippet is documented but never applied automatically.
9. **Identity:** the LICENSE copyright is "ItalianAccent contributors". No personal data goes in the repo. `wallera` is mandatory for Napoletano, and attested spellings (e.g. "uallera") are documented as variants.

## Catalog: 22 initial modes, all v0.1.0 implementation targets
mbare (Catanese), trimone (Barese), wallera (Napoletano), daje (Romanesco), mena (Salentino), minchia (Palermitano), belin (Genovese), bischero (Fiorentino), boiade "Boia dé" (Livornese), pirla (Milanese), pota "Potà" (Bergamasco), socmel (Bolognese), pataca (Romagnolo), ostrega (Veneziano, localized in research), neh (Piemontese/Torinese), mandi (Friulano), mona (Triestino), ajo "Ajò" (Sardinian variety, localized: likely Campidanese or Logudorese, decided on evidence), frechete (Abruzzese local variety), ntamato "'Ntamato" (Calabrese local variety), freghi (Perugino), cio "Ció" (Trentino).

**Regions still uncovered** after these 22: Basilicata, Molise, Marche, Valle d'Aosta (Trentino-Alto Adige is covered by cio). For each, research a documented local variety and an attested, recognizable identifier word, with candidates to verify:
- Lucano (Potentino/Materano).
- Molisano (Campobassano).
- Marchigiano (Anconetano/Ascolano).
- Valdostan Francoprovençal (patoué).

Names are chosen only if attested; nothing is invented. If no reliable identifier is found, I use a transparent descriptive ID and document why. Result: target ≥1 usable experimental mode per each of the 20 regions. Other provincial/municipal varieties from spec §9 go into the catalog as `planned` + roadmap.

Name↔variety associations are verified during research. Any correction, for example a word that actually belongs to a different area, is documented in `docs/linguistic-methodology.md` and the catalog. Mandated names are kept: ItalianAccent, mbare, trimone, wallera, daje, mena.

## Milestones (continuous; S = sequential, P = parallel)

### M0 — Bootstrap [S]
- In `/home/user/italianaccent`: create the plan/checklist/progress files, `.gitignore`, MIT LICENSE, `pyproject.toml`, README stub.
- `git checkout -b main`, commit `chore: initialize ItalianAccent repository`, push to verify write access.
- Set description + 13 topics via `gh repo edit` (or the REST `PUT /repos/vapor16/ItalianAccent/topics`).
- If the proxy blocks metadata edits: record it, continue, and ask the user only for that single step at the end.

### M1 — Spec verification [P with M2]
Read the official sources:
- agentskills.io + /specification
- code.claude.com/docs/en/skills
- Claude Code plugin and marketplace docs
- github.com/anthropics/skills
- skills.sh
- github.com/vercel-labs/skills (exact `npx skills add` syntax and flags such as `--skill`/`--list`, plus discovery paths)

Record the findings in `docs/platform-compatibility.md` + `research/research-log.md` with access dates.

### M2 — Architecture skeleton [S]
- Schemas, `references/catalog.json` (22 modes + 4 regional additions + planned varieties), `defaults.json` (spec §20), `references/commands.md`, `references/behavior.md` (intensity/vulgarity levels with concrete behavior, technical integrity §22, formal/emotional situations §23), `references/dialect-loading.md`.
- `docs/architecture.md`, `docs/linguistic-methodology.md`, `docs/source-policy.md`, `research/sources.json`.

### M3 — Working SKILL.md early [S, right after M2]
SKILL.md covers:
- An activation guard.
- The full command grammar: `/italianaccent`, help, list, status, random, off, reset, `<mode>`, intensity 1–5, vulgarity 0–5, proverbs/idioms/humor/sarcasm/translation on|off, combined `--intensity/--vulgarity` flags, and natural-language activation in IT and EN.
- ID/alias resolution: case-, accent- and apostrophe-insensitive, with nearest-match suggestions; planned modes are refused politely.
- The loading order and the defaults.
- Switching without mixing varieties, and `off` that restores the normal voice.
- Persistence rules and the host-safety clause.

Kept under ~250 lines. Commit `feat: implement core agent skill architecture`.

### M4 — Pilots: validate architecture & methodology [P, 5 subagents]
- One research subagent each for trimone, mbare, wallera, daje and mena. Each writes only `dialects/<id>/` + `research/raw/<id>-*`.
- Deliverable: a functional minimal profile, meaning a complete `profile.md` + `metadata.json` + initial sourced lexicon/proverbs/profanity + `sources.md`.
- **Immediate skill test (M4b):** evaluator subagents load the skill exactly as a host would and run 8 behaviors per pilot: activation, dialect selection, resource loading, vulgarity 5 vs 0, proverb use, mode switch, deactivation, persistence over 3 turns. A judge subagent scores with the 1–5 rubric.
- Fix architecture/SKILL.md/methodology issues found here, then freeze the profile contract.
- Commit each pilot profile with its own `feat: add <Name> dialect profile` commit.

### M5 — Breadth-first: minimal functional profile for every remaining mode [P, batches ≤5 subagents]
- Batch A: minchia, belin, bischero, boiade, pirla.
- Batch B: pota, socmel, pataca, ostrega, neh.
- Batch C: mandi, mona, ajo, frechete, ntamato.
- Batch D: freghi, cio + 4 new regions (Basilicata, Molise, Marche, Valle d'Aosta).

Each mode gets the same minimal functional deliverable and is smoke-tested with the working skill: activation + 2 reference prompts, judged.

A profile becomes `experimental` and activatable when its core is authentic, coherent and sourced. If research cannot support a reliable profile, it stays `planned` with research notes, never padded. The lead consolidates `research/sources.json`, dedups entries, and checks for contamination between neighboring varieties (e.g. Livornese vs Fiorentino, Barese vs Salentino, Catanese vs Palermitano). Commit after each batch.

### M6 — Progressive enrichment of ALL profiles [P, rounds]
- Round-robin across all profiles, so the first five don't consume the budget. Each round adds, per profile: vocabulary, grammar/morphology rules, syntax, vulgar expressions & imprecations (incl. friendly/hostile/affectionate uses), proverbs, idioms, humor & sarcasm patterns, conversational examples, and technical examples (Docker, Spring Boot, Git, SQL, Kubernetes with untouched valid code).
- `examples.md` covers the 20 reference prompts, marked *illustrative AI examples*. Pilots get all 20; other profiles get a representative subset that grows each round.
- Continue rounds while sources yield new authentic material and session resources allow. Record real counts per round in progress.json. Commits: `feat: enrich <batch> profiles`, `feat: implement profanity configuration`, `feat: integrate traditional proverbs`.

### M7 — Deterministic tests [P with M5/M6]
pytest suites:
- `tests/structural`: JSON syntax, schemas, frontmatter per spec, catalog↔dirs, unique ids/aliases (normalized), required files for activatable profiles only, resource paths, defaults, manifests, version consistency.
- `tests/linguistic`: source IDs resolve, source metadata complete, duplicate terms/proverbs after normalization, intensity/register enums, meanings non-empty, provenance rules, no `verified`/`community-reviewed` status without a review record.
- `tests/security`: secret patterns, absolute/home paths, emails, no runtime network instructions, no executable runtime dependencies.
- `tests/behavioral`: eval-case YAML + rubric, with well-formedness checked deterministically.

Run continuously and fix failures. Commit `test: …`.

### M8 — Behavioral evaluation round [S after M6]
- Full AI-assisted eval: all 16 behaviors (spec §25) on the pilots, plus the smoke set on every experimental profile, with repetition-avoidance and code-integrity checks.
- Results go to `tests/behavioral/results/v0.1.0/`, labeled as AI-assisted. Human evaluation is declared pending.
- Fix issues and re-run the failing cases.

### M9 — Claude Code plugin manifests & CI [P]
- `.claude-plugin/plugin.json` + `marketplace.json` (schema verified in M1).
- `.github/workflows/validate.yml`: push/PR, `contents: read`, pytest + validate, stats in the job summary.
- `release-check.yml`: on tag, version check + ZIP artifact, no auto-publish.
- Validate the workflow YAML.

### M10 — Documentation & community [P]
- README.md (EN) + README.it.md covering every §30 section: explicit-language notice, catalog with English meanings of mode names, real counts, maturity, compatibility matrix (documented / structurally compatible / locally tested / not tested), install on Win/macOS/Linux (skills CLI, git clone, plugin marketplace, Claude.ai ZIP), commands, config, limitations, privacy, roadmap §32. No fake badges or stats.
- CONTRIBUTING.md, `docs/adding-a-dialect.md` (for contributors who don't know the architecture), CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md, THIRD_PARTY_NOTICES.md.
- 12 issue templates + PR template, and `examples/` comparing the same prompts across modes.

### M11 — Release prep & audit [S]
- Validate + pytest green, build `dist/italianaccent-0.1.0.zip` (skill folder only, gitignored).
- Run `npx skills add . --list` (or the verified equivalent) from a scratch HOME.
- Run the skill-scanner skill, a secret/privacy grep, and a license review, then check the full §36 Definition of Done and the original specification, item by item.
- Commit `chore: prepare v0.1.0 release`.

### M12 — Publication [S]
- Push `main` and confirm the GitHub Actions run is green (`gh run list/view`); fix and re-push if not.
- Verify the repo is public, topics and description are set, and the skill path is reachable on GitHub.
- Tag `v0.1.0` and `gh release create` with release notes (experimental) + ZIP.

### M13 — Distribution verification [S]
- `npx skills add vapor16/ItalianAccent --list` (and `--skill italianaccent` if supported) in a scratch HOME detects `italianaccent`.
- Install the skill into a scratch dir and check that all resources are included.
- Skills.sh public listing is claimed only if it is actually observed.

### M14 — Final delivery report [S]
- `docs/DELIVERY_REPORT.md` in Italian, covering all 30 items of §38 with real numbers from `scripts/validate.py --stats`.
- Same-prompt comparison examples for Trimone/Mbare/Wallera/Daje/Mena, showing grammar, lexicon, authentic vulgarity, proverbs, idioms, sarcasm, humor and technical accuracy.
- List what was not completed and what needs human review. Summarize in the final reply.

## Parallelism & conflict rules
- Parallel work: M1∥M2; the M4 pilots; M5 batches; M6 rounds per batch; M7∥M9∥M10 running alongside the research.
- At most 5 concurrent subagents. Subagents write only their own `dialects/<id>/` and `research/raw/<id>-*`. The lead alone edits shared files (catalog, sources.json, SKILL.md, progress, docs).
- The lead reviews each subagent's output before integrating it. Nothing is marked done unless the subagent actually finished it.

## Verification (end-to-end)
- `python scripts/validate.py && pytest -q` green locally and in GitHub Actions on `main`.
- Early (M4b) and full (M8) AI-assisted behavioral evaluations stored with scores: activation, selection, loading, vulgarity default 5, proverbs, switch, off, persistence, technical/code integrity.
- `npx skills add vapor16/ItalianAccent --list` lists `italianaccent`. Release and ZIP confirmed via `gh release view v0.1.0`.
- Security/privacy/license audit clean, and the DoD checklist fully ticked in `docs/IMPLEMENTATION_CHECKLIST.md`.

## Declared limits
- No native-speaker review, so every profile is `experimental`.
- Enrichment counts are real, not padded.
- Persistence is conversation-scoped.
- Compatibility beyond Claude Code / skills CLI is documented/structural unless tested.
- A profile is shipped as `planned` instead of usable only if research cannot support it, and the reason is documented.
