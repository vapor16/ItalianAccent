# ItalianAccent v1.0.0 behavioral evaluation (SCORES)

> **AI-assisted evaluation. Model-judged, NOT native-speaker validated.** The judge is an AI model reading the transcripts and the repo's own `profile.md`/lexicon as reference; it cannot hear speech or verify regional usage. Treat the numbers as relative signals (with vs without skill), not as linguistic ground truth. Sample is small: 5 prompts for mena and wallera, 2 for belin, bischero, boiade, pirla, pota, one run each, so differences of 0.5 are within noise. `trimone` has no transcripts and was not scored.

Scale 1-5 per `tests/behavioral/eval-cases.yaml` (authenticity, naturalness, vocabulary, grammar, syntax, regional_consistency, contextual_profanity, proverb_relevance, humor, technical_accuracy). Scores are my per-mode averages over the prompts available (half-points allowed). `without` = same model, dialect requested explicitly, no skill.

Reading note: judgments of tameness are made against the default vulgarity 5; judgments of authenticity against the profile text, so the 'with' side is partly measured by the same document that shaped it (possible bias in its favor).

## Mena (Leccese/Salentino) - 5 prompts

| criterion | with skill | without |
|---|---|---|
| authenticity | 4 | 2.5 |
| naturalness | 3.5 | 3 |
| vocabulary | 3.5 | 3.5 |
| grammar | 4 | 2.5 |
| syntax | 4 | 3 |
| regional_consistency | 4.5 | 2 |
| contextual_profanity | 3 | 4 |
| proverb_relevance | 3 | 3 |
| humor | 2.5 | 4 |
| technical_accuracy | 4.5 | 4 |
| **average** | **3.65** | **3.15** |

- With: dense, mostly profile-consistent Salentino: `ddh`-free but correct `ete`, `cu`+finite verb (`cu bbiti cce tte spetta`), `nu` negation, `cchiu`/`moi`/`osce`/`crai`, no schwa. Without: heavy contamination from other southern varieties: `mbare`, `uagno`, `fiju miu`, `ce minchia l'e passatu` (Sicilian), `quarcunu` (Roman), `mannaggia lu cazzu` repeated, `ci nasce tunnu nu' mmore quadratu` mixed with Italian syntax.
- With: the same two proverbs recur across prompts: `Nu nc'ete rosa senza spine, nu nc'ete omu senza uai` in p1, p3 and p5, and `Ci ae a cchianu, ae sanu e bae luntanu` in p3 and p7. `Mena` is used as vocative in almost every answer (`Mena, cce ssorte!`, `Mena, provala!`) and `Cazzu!` opens p3, p7 and p8. Over-repetition and tameness: p1 and p5 are short, with one `Mmerda` as the only vulgarity.
- With: p3 (car defect) is technically strong and correct as far as I can judge (24 months legal warranty, 12-month presumption, art. 1490 c.c., 8-day report, 1-year action). But the register drops into near-Italian (`Ai la garanzia legale di conformita: 24 mesi`, `la riduzione del prezzo o la risoluzione del contratto`) inside the technical body. p5 invents an explanation for a proverb (`rrimanire comu la zzita de Turre... modu te ddire te Scorrano`), which is confusing and reads as a hallucinated gloss.
- Without: far more vivid and funnier, with real local color (`pasticciotto`, `Santu Oronzu`, `Torre dell'Orso`, `nigroamaro`; the p8 story is a real narrative) and uncensored profanity. But p3 contains a non-sequitur (`Pe' le parolacce nu' tegnu bisognu de dirtelu`) and a mocking-the-seller tone with no actual legal content; Java in p7 is correct and richer (two versions, main), the reversal outputs are right (`Lecce`->`eccel`).

## Wallera (Neapolitan) - 5 prompts

| criterion | with skill | without |
|---|---|---|
| authenticity | 4.5 | 3.5 |
| naturalness | 4 | 3.5 |
| vocabulary | 4 | 3.5 |
| grammar | 4.5 | 3.5 |
| syntax | 4 | 3.5 |
| regional_consistency | 4.5 | 3.5 |
| contextual_profanity | 3 | 4.5 |
| proverb_relevance | 3.5 | 3 |
| humor | 3.5 | 4.5 |
| technical_accuracy | 4 | 3.5 |
| **average** | **3.95** | **3.65** |

- With: the most convincing mode. Consistent articles `'o/'a/'e`, circumflex contractions (`ô`, `ê`, `hê`, `sî`) per profile, enclitics (`mammeta`), `tené`/`avé 'a` (`Dimme che hê 'a fà`), `nun`, metaphony (`pisce`-type forms not forced); proverb `Pe' n'aceno 'e sale se perde 'a menesta` is a real Neapolitan one and fits (p1). Without: acceptable Neapolitan but flatter orthography and calques of Italian proverbs (`Chi nasce tondo nun po' murì quadro`, `Chi tene 'a lengua, a Roma va`), `scarrafone` proverb used in p2, p4 and p7-style filler.
- With: p6 (ex) switches off the jokes and gives sober, empathetic advice, which is context-appropriate, but vulgarity is then nearly absent (default vulgarity 5). p4 (roast) is good (`'o forno sta sempe stutato e 'o telefono chiamma 'a pizzeria`) but milder than the without roast, which has more escalation (`San Gennaro`, `ragu`, `Pulcinella`). Activation messages are multi-line (p4 lists the full command set), not the one-line confirmation of act-01.
- Technical: p2 Docker bar metaphor with correct commands and a sound VM-vs-container explanation; p7 Java is correct and adds a real pitfall (surrogate pairs). Small defect: `reverse("Napule")` is commented as `eluapN` (should be `elupaN`) and a typo `quinno`. Without: the same example is commented `eluapaN` (wrong) and the Docker answer is decent but adds emoji and `Kubernetes e nu burdello`.
- Without: lively, with Neapolitan cultural references (`Duchesca`, `Pino Daniele`), emojis, and a closing proverb stack. Humor is higher; authenticity/regional consistency lower (Italian bleed such as `famme veni' a casa mia`, `Se te serve pure 'a versione`, `ve mannammo 'a quel paese`).

## Belin (Genoese) - 2 prompts

| criterion | with skill | without |
|---|---|---|
| authenticity | 3.5 | 3 |
| naturalness | 3 | 3 |
| vocabulary | 3 | 3.5 |
| grammar | 3.5 | 2.5 |
| syntax | 3.5 | 3 |
| regional_consistency | 3.5 | 2 |
| contextual_profanity | 2 | 4.5 |
| proverb_relevance | 3 | 2.5 |
| humor | 2 | 4 |
| technical_accuracy | 4.5 | 4 |
| **average** | **3.15** | **3.20** |

- With: genuinely Genoese morphology and clitics (`ti g'ae`, `ti ste a pesta`, `a-a riga`, hyphenated contractions, `o` for article), and uses the profile's own idiom `pesta l'aegua in to morta`. But p4 mixes spellings (`cattou`, `Into to pignatta`, `unna`, `ti peu`/`ti veu`) and `a pignatta agguita a no bogge mai` looks like a calque of the Italian `pentola guardata non bolle mai`, not a documented proverb.
- With: tame. p1 has no `belin` in the answer body and only `Va tutto a bagasce`; p4 is a thin roast (`gh'e solo aegua e bratta`) with the pun `abelinou` but no escalation. Without: much stronger humor, but caricature: `belin` and `belinon` appear 6+ times, plus `o grandiscimo figgio de 'na bagascia`, `Ma vanni a cagare`.
- Without: contamination and invention. `pelandron`, `mazzon` look Lombard/Piedmontese, `Un belinon o l'e bon solo a mangia` and `Chi no sa cheuxe, o se fa invita da-i atri` are not documented proverbs, and spelling varies (`ûn/un`, `ê/e`). It also adds an English-style disclaimer `(Nota onesta...)` out of persona.

## Bischero (Florentine) - 2 prompts

| criterion | with skill | without |
|---|---|---|
| authenticity | 4 | 3.5 |
| naturalness | 4 | 3.5 |
| vocabulary | 4 | 3.5 |
| grammar | 4 | 3 |
| syntax | 4 | 3.5 |
| regional_consistency | 4.5 | 3.5 |
| contextual_profanity | 2.5 | 4.5 |
| proverb_relevance | 3.5 | 3 |
| humor | 3.5 | 4 |
| technical_accuracy | 4.5 | 4 |
| **average** | **3.85** | **3.60** |

- With: good Florentine markers used naturally: `icche`, `codesta`, `i' compilatore`, `l'e`, `tu ... te tu eri`, subject clitic `un`, lexicon `rigovernare`, `desinare`, `berciare`, `c'e furia`; the proverb `poco e spesso empie il borsello` is documented and fits. Minor slips: `c'e' arrivato`, `mette' a bolli`, `ni' quartiere`.
- With: tameness is the main defect: the only profanity is `Maremma maiala` and the roast (p4) has no vulgar punch, even at vulgarity 5. Without: `Boia deh`, `Madonna ladra`, `coglione`, `pistola!`, plus Florentine food references (`lampredotto`, `ribollita`, `bistecca`) and stronger comic escalation, but `'un` apostrophe style differs from the profile, `ciccio`/`citto`/`bimbo` vary, and the proverb `chi 'un fa 'un falla` is unclear.
- Technical advice in p1 is correct and equal in both (linter, previous line, bisect).

## Boia de (Livornese) - 2 prompts

| criterion | with skill | without |
|---|---|---|
| authenticity | 4 | 2.5 |
| naturalness | 3.5 | 3.5 |
| vocabulary | 3.5 | 3 |
| grammar | 3.5 | 3 |
| syntax | 3.5 | 3 |
| regional_consistency | 4 | 2.5 |
| contextual_profanity | 2 | 4.5 |
| proverb_relevance | 2.5 | 2.5 |
| humor | 3 | 4 |
| technical_accuracy | 4.5 | 4 |
| **average** | **3.40** | **3.25** |

- With: distinctively Livornese per profile (`ir/'r` articles, `caa`, `ni` for gli, `pula`, `de`, `oimmei`, `scazzata`, `pòo`), and `Boia`/`de` are used sparingly as the profile demands. Weak points: some sentences are incoherent (`Ir tu' sugo e robba da torta`, `Sei sempre a rovina l'acqua ber bollita`) and `'n fu ma' bona` as a proverb is unexplained and apparently invented; the roast in p4 is under-spiced and the p1 turn-2 opening (`Ni voglio bene, ar punto e virgola`) is confusing.
- Without: generic Tuscan with Roman/standard intrusions (`cojoni`, `Er mi' nonno`, `Un sai cucina`, `Just Eat`, `ciofeca`), and invented sayings (`Meglio un asino vivo che un dottore morto`, `Chi un sa cucina, un sa nemmeno campa`). It is funnier and more vulgar, but not clearly Livornese beyond `cacciucco` and `Calafuria`.
- Activation text is longer than one line and p1 `Dé, attivato.` precedes the header.

## Pirla (Milanese) - 2 prompts

| criterion | with skill | without |
|---|---|---|
| authenticity | 3.5 | 3 |
| naturalness | 3.5 | 3.5 |
| vocabulary | 3.5 | 3.5 |
| grammar | 3.5 | 3 |
| syntax | 3.5 | 3 |
| regional_consistency | 3.5 | 2.5 |
| contextual_profanity | 3 | 4.5 |
| proverb_relevance | 3.5 | 3.5 |
| humor | 3.5 | 4 |
| technical_accuracy | 4.5 | 4 |
| **average** | **3.55** | **3.45** |

- With: Milanese morphology as per profile (`mi a ...`, subject clitics `el/te`, post-verbal `minga`, doubled long vowels `faa`, `andaa`, `ancamo`, `quaresima` idiom), correct technical advice (previous line, linter, `git bisect`). Inconsistent spelling between `u` and `u` with umlaut (`cusinaa` vs `cusinet`), `tt` typo in `l'e tt un laura`, and p4 is brief and not very sharp.
- Without: real Milanese proverbs (`Ofelee, fa el to mestee`, `chi la fa l'aspetta`) and words (`bauscia`, `ciula`, `barlafus`, `va a ciapa i ratt`) but with contamination (`tusa/tusòn`, `balòss` Piedmontese, `Hin pussee i pirla che i sciuri` apparently invented) and repeated `pirla/ciula/bauscia` in one answer (over-use of the mode word).
- With: the mode word `pirla` is used once per answer, in line with the profile; Without: `pirla` four times in p4 plus emoji.

## Pota (Bergamasco) - 2 prompts

| criterion | with skill | without |
|---|---|---|
| authenticity | 3.5 | 2.5 |
| naturalness | 3 | 3 |
| vocabulary | 3.5 | 3 |
| grammar | 3.5 | 2.5 |
| syntax | 3.5 | 3 |
| regional_consistency | 4 | 2.5 |
| contextual_profanity | 3 | 4 |
| proverb_relevance | 3 | 2.5 |
| humor | 3 | 4 |
| technical_accuracy | 4.5 | 4 |
| **average** | **3.45** | **3.10** |

- With: Bergamasco features from the profile (`mìa` after the verb, subject clitics `ta`/`te`, voiced-s `cóṡa`, `öl`, `ghe n'è mìa di bale`, `figa`), coherent in orthography. Nonsense line in p1: `Chi sirca, tróa, ma issé l'è ü bel tròp de sirca`; p4 is mild and mixes `mìa` with `miga`.
- Without: strong code-switching with Italian (`al metterebbe`, `uno che`, `Nota: ho usato`), borrowed Milanese/Piedmontese words (`balòss`, `ve' mia`), the proverb `Chi nas tondo, mör mia quadro` is a calque, `Töt s'impara, fò che a fà ol pirla` appears invented. It is nonetheless funnier (`polenta e osei`, `Cà di Mort`, `gàlìne de Bèrghem`) and uses profanity more freely.
- With: `Pòta` as interjection is used once per answer, as the profile demands.

## Cross-mode averages (unweighted, 7 modes)

| criterion | with skill | without |
|---|---|---|
| authenticity | 3.86 | 2.93 |
| naturalness | 3.50 | 3.29 |
| vocabulary | 3.57 | 3.36 |
| grammar | 3.79 | 2.86 |
| syntax | 3.71 | 3.14 |
| regional_consistency | 4.07 | 2.64 |
| contextual_profanity | 2.64 | 4.36 |
| proverb_relevance | 3.14 | 2.86 |
| humor | 3.00 | 4.07 |
| technical_accuracy | 4.43 | 3.93 |
| **average** | **3.57** | **3.34** |

## Overall summary

**Does ItalianAccent help?** Yes on linguistic fidelity, no on entertainment. With the skill the output is more consistent with the documented variety (regional_consistency, grammar, syntax, authenticity +0.6 to +1.4 over baseline: regional_consistency 4.07 vs 2.64, grammar 3.79 vs 2.86, authenticity 3.86 vs 2.93, syntax 3.71 vs 3.14). The baseline model drifts: it blends in forms from neighbouring varieties (Sicilian/Roman words in Salentino, Piedmontese/Lombard in Genoese and Bergamasco, Roman in Livornese), writes Italian-with-dialect-words, falls back to Italian proverbs translated word for word, invents proverbs, and overuses the mode word (`belinon`, `pirla`, `mannaggia`). The skill also keeps the persona on task: the mode word and interjections appear about once, and technical content (Java, Docker, legal and linter advice) stays correct and uncluttered; baseline technical content is also correct but wrapped in emoji, glossaries and out-of-persona disclaimers (`Nota onesta`).

**Where it falls short.** (1) Tameness: at vulgarity 5 the skill answers are clearly less vulgar and less funny than the baseline (contextual_profanity 2.64 vs 4.36, humor 3.00 vs 4.07); the 'at most once per answer' rule for the mode word and interjections seems to have been over-generalised to all vulgarity, so roasts (`Prendimi in giro`) and rants (`cinque ore`) lack escalation, especially in belin, bischero and boiade. (2) Repetition across prompts: mena reuses the same proverbs (`Nu nc'ete rosa senza spine` x3, `Ci ae a cchianu` x2) and openers (`Cazzu!`); this suggests the proverb set the model draws on is narrow or not rotated. (3) Technical bodies slide toward Italian (mena p3 legal list), a drift despite 'intensity 5'. (4) Activation is often not the single-line confirmation of act-01 (wallera p4 lists the whole command set; boiade p1 `Dé, attivato.` then header; mena p3 confirms in Italian and adds an options line). (5) Some nonsense or unclear sentences remain (boiade `Ir tu' sugo è robba da torta`, pota `Chi sirca, tróa...`, mena p5 `zzita de Turre` gloss), and some spelling mixing (belin p4, pirla `u`/`ü`). (6) Both arms mis-wrote the reversed `Napule` in a Java comment in wallera (`eluapN` with, `eluapaN` without). Without a native reviewer none of the Genoese, Bergamasco and Livornese output can be called reliable.

## Prioritized minimal fixes

1. **All profiles, §Profanity/Style rules (and SKILL.md style section):** split the 'once per answer' limit so it applies only to the mode word and signature interjections, and state explicitly that at vulgarity >=4 a roast, rant or venting prompt must contain 2-4 varied, documented swear/insult phrases aimed at the situation (not the user). Add one 'good roast' example per profile in `examples.md`.
2. **belin, bischero, boiade profiles §Humor/§Profanity:** add 3-5 ready-made level-4/5 comic images from the profile's own palette to be drawn on (e.g. belin: `ciu cu che tre bagasce`, `cervello into cu comme i agni`; boiade: documented words in the `tegame/budello` family in mock-hostile frames). These three are the tamest.
3. **mena profile §Proverbs + SKILL.md proverb rule:** require that a proverb used earlier in the session is not repeated and prefer a proverb that is actually relevant over a generic one; add a short `used-in-session` instruction. Mark `Nu nc'e rosa senza spine` and `Ci ae a cchianu` as 'use at most once per session'.
4. **mena and all profiles §Technical content:** add a rule that explanations, lists and legal/medical steps remain in dialect (verbs, articles, connectives) with only code, commands, identifiers and legal citations left in Italian; give one worked example (mena p3 style) per profile that stays dialectal.
5. **SKILL.md activation step:** enforce exactly one line `[ItalianAccent · Mode · intensity N · vulgarity N]` plus at most one short in-dialect sentence; move the command-help list behind `help`. Fixes act-01 for wallera, boiade, belin, mena p3.
6. **pota and belin profiles §Proverbs/§Orthography:** keep a single orthography per answer (belin: `cattou/cattòu` and `ti peu` vs `ti veu`; pota: `mìa` not `miga`; pirla: always `ö/ü`), and delete or flag as 'AI-illustrative, do not quote' any proverb in `proverbs.json` with `unverified` status that reads as a calque of an Italian one (e.g. belin `a pignatta agguitâ`). Add a one-line validity rule: never create a proverb; use the profile list or an idiom with a literal meaning.
7. **boiade profile §Syntax:** add 3-4 full, coherent Livornese sentences with `ir/'r`, `caa`, `ni` and warn against stacking them into non-sentences (`Ir tu' sugo è robba da torta`).
8. **Docs/tests:** add a deterministic check that `eval` results include a non-empty `trimone` folder, and update eval-cases with a 'no repeated proverb within a session' expectation and a 'roast must contain at vulgarity 5 at least two profanity items' expectation so future runs can measure fixes 1 and 3.

## Retest after fixes (lead review, AI-assisted, not native-validated)

After the fixes listed above (SKILL.md: vulgarity 4–5 must bite, no repeated proverbs, lists in dialect, short
activation; profile bite kits, proverb rotation, one spelling per answer) the weakest cases were re-run on the
installed skill: `tests/behavioral/results/v1.0.0-retest/` (belin, bischero, boiade prompt 4; mena prompt 3).

- Activation is now one status line plus one short sentence in all four runs.
- Boia dé roast: several different documented insults (testa di 'azzo, spaccascurrégge, bischero), hyperbole and a
  fitting proverb (*Minestra riscardata 'n fu ma' bona*); the earlier tameness is gone. The odd phrase
  "robba da torta" still appears (documented in the lexicon, but used loosely).
- Mena car warranty: step list kept in Leccese (only *garanzia*, *contratto* in Italian), new proverb
  (*bbatti lu fierru quannu è ccautu*), no repeated proverb, profanity contextual.
- These are spot checks by the lead, not a re-scored full evaluation.

## Final slang pass — practical tests (lead review, AI-assisted, not native-validated)

Installed skill, Sonnet, `tests/behavioral/results/v1.0.0-slang/` (wallera, pota prompt 4; trimone, minchia, daje
prompt 1). New material appears naturally and only where it fits (Daje *me dà ar cazzo*, Wallera *né pe' bevere né
pe' sciacquà* and *me staje abbuffanno 'a uallera*, Minchia *futtitinni*, *u sceccu unni cari si susi*); dialect
grammar is kept inside technical step lists; advice and tool names are correct; no identifier tic. The *bucchino*
idioms were not forced into these prompts (expected: they are context-specific dismissals/boasts).
