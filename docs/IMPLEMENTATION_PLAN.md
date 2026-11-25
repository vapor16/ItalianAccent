# ItalianAccent — v1.0.0 final plan (scope simplified by the user)

## Context
The user simplified scope: ItalianAccent is a fun, irreverent, lightweight Agent Skill, not an academic project. Freeze the catalog at the **11 existing usable modes**, apply the corrections from an external audit (ChatGPT deep research, `ITALIANACCENT_RESEARCH.md`, pasted in chat), make the personality more natural/funny/non-caricatural, test practically, and publish **v1.0.0**. Supersedes the old M5–M14 breadth plan (no new dialects). Profiles stay `experimental` (no native review).

## Current state (read-only check)
- origin/main at `bdfa633`; 11 available modes in catalog: mbare, trimone, wallera, daje, mena, minchia, belin, bischero, boiade, pirla, pota. Validation/tests green at last ship.
- Untracked partial research: `dialects/{pataca,socmel,ostrega}/`, `research/raw/{pataca,socmel}-*`. Pataca is complete; socmel/ostrega cut off by usage limit.
- Mena profile.md:230 contains the wrong claim "centre-north Apulian … no metaphony". No explicit B→P rule found by grep.
- Blockers unchanged: topics (proxy 403) and workflows (`workflow` scope) → owner commands in `ci/README.md` / progress.json.

## Execution (autonomous, Sonnet subagents ≤3 concurrent, Python for deterministic work, incremental commits+push)

### 1. Freeze catalog & preserve research
- Move `dialects/{pataca,socmel,ostrega}` → `research/future-profiles/<id>/` (outside the shipped skill), with raw sources/logs kept in `research/raw/`. Commit `chore: park unfinished profiles for future releases`.
- Catalog: keep the 11 available modes; keep other varieties as `planned` (roadmap). Pataca/socmel/ostrega stay `planned` with a note "research parked in research/future-profiles".
- Mena display: name stays `Mena`; variety → "Leccese — Salentino centrale" (catalog `variety` + metadata description/geographical_area). Mode IDs unchanged.
- Save the audit as `research/ITALIANACCENT_RESEARCH.md` (user asked to keep the file); log in research-log.md.

### 2. Apply audit corrections (verify disputed claims against cited sources first; edit existing files only)
One Sonnet agent per group, each edits only its profiles; brief = audit section + "verify, then minimally correct; no new architecture/params":
- **A — Mena + Trimone + Wallera**
  - Mena P0: remove "no metaphony" (Treccani: metaphony exists in centre-north Apulian); state explicitly B→P is NOT a rule; investigate actual generated B→P (run sample generations from profile/examples, grep examples for p-for-b forms) and fix the source of it; add the two Turre expressions to proverbs.json (source `https://www.dialettosalentino.it/turre_1.html`, Presicce; area "Scorrano, referring to Torrepaduli (Ruffano)", verify accents on the page) and add them to profile §10 quick-use with trigger "preparation ruined at the last minute / absurd solution".
  - Trimone: soften non/nan rule; phonetic changes only on attested lexemes.
  - Wallera: unverified blasphemy → `generation_allowed:false` (or keep unverified, not in palette); avoid stereotyped spellings.
- **B — Mbare + Minchia + Daje**
  - Mbare/Minchia P0: preconsonantal r assimilation = lexically constrained (closed list of attested forms), never a general rule; Palermo comparison made non-absolute (also resolves the open cajni issue); `minchia` not obligatory token.
  - Daje P1: `mb→mm` rare, `ld→ll` residual; default contemporary Romanesco, Belli/historical forms not by default.
- **C — Bischero + Boia dé + Belin + Pirla + Potà**
  - Bischero: no `h` gorgia spelling by default (remove from intensity-5 guidance).
  - Boia dé: `dé` natural not obsessive, `boia dé` not a fixed formula, /k/ elision only on documented words.
  - Belin: `belin` occasional, readable spelling by default.
  - Pirla: default contemporary urban Milanese; classical Cherubini/Porta forms only as reference.
  - Potà: no automatic accent rewriting; keep no f→h.
- All agents: also fix unnatural/repetitive expressions in examples.md, mark unsupported vocabulary/profanity `unverified` or remove; enrich only with reliable sources when useful.
- After each group: `python3 scripts/validate.py --integrate <id>` (sources.md/catalog sync), pytest, commit per profile, push.

### 3. Personality pass (SKILL.md / behavior.md — small edits, no new params)
- Add a short "Sound like a person from the city" section: spontaneous, sarcastic, irreverent; vary interjections; never repeat mode name/same interjection each sentence; no historical language or phonetic caricature by default; grammar/syntax/vocabulary genuinely dialectal; phonetic changes only on attested forms listed in the profile.
- Keep defaults 5/5, uncensored profanity, proverbs/idioms, technical integrity.

### 4. Practical testing (existing infrastructure)
- Extend `tests/behavioral/eval-cases.yaml` with ~8 practical prompts (user's examples: semicolon debugging, Docker at the bar, broken car, can't cook, cancelled party, disastrous day, ex, Java function + persistence/switch/off).
- Deterministic regression tests (tests/linguistic): Mena profile has no "no metaphony" claim and no B→P rule; Turre entries carry Scorrano/Torrepaduli provenance; Bischero default has no h-gorgia instruction; Daje marks mb→mm rare; Mbare/Minchia r-assimilation described as lexical; no `blasphemy` entry with `verification_status: unverified` and `generation_allowed` true; examples don't repeat the mode identifier more than N times per answer.
- AI-assisted eval (Sonnet evaluator agents, ≤3): install skill into scratch HOME via `npx skills add . --skill italianaccent -a claude-code -y`, then run `claude -p` headless with the installed skill for 5–8 prompts per dialect (sample, budget-aware: full set for 3–4 dialects, 2–3 prompts for the others) **with vs without** ItalianAccent (same model, same dialect explicitly requested in both). Independent Sonnet judge scores with existing rubric. Store transcripts+scores in `tests/behavioral/results/v1.0.0/` labelled AI-assisted. If `claude -p` can't run in this env, fall back to subagents simulating the host by reading the installed files, and say so.
- Fix meaningful problems found; re-run failing cases.

### 5. Release v1.0.0
- Bump version to 1.0.0 (pyproject, SKILL.md metadata, plugin.json, marketplace.json, catalog), CHANGELOG `[1.0.0]`.
- README.md + README.it.md (write Italian README): 11 modes table (via `--readme`), install (skills CLI, plugin, manual Win/macOS/Linux, Claude.ai ZIP), commands, config, examples (short comparison from results), limitations (experimental, no native review), privacy, roadmap (future dialects parked), GitHub blockers. THIRD_PARTY_NOTICES.md. Update docs mentions of v0.1.0 → 1.0.0 where relevant.
- Checks: `python scripts/validate.py && pytest`; skill-scanner/secret grep; `claude plugin validate .`; build ZIP; `npx skills add vapor16/ItalianAccent --list` (after push).
- Push, tag `v1.0.0`, `gh release create v1.0.0 dist/italianaccent-1.0.0.zip` (if proxy blocks release creation → report owner command).
- Update progress.json/checklist; final concise Italian report: corrections, test results (real), install, limitations, release URL, manual owner actions (topics, workflows activation; GitHub Actions not claimed operational).

## Verification
- `python3 scripts/validate.py` 0 errors; `pytest -q` green, including new regression tests.
- Installed-skill eval transcripts present with/without comparison and scores.
- `npx skills add vapor16/ItalianAccent --list` lists italianaccent; release visible via `gh release view v1.0.0`.
