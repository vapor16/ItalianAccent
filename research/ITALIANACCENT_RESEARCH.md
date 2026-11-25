# ItalianAccent — practical linguistic research and profile audit

> Independent external audit of the eleven active profiles, produced with ChatGPT deep research and provided by the
> project owner on 2026-11-25 (original in Italian; this copy keeps the content, with the inline citation markers of
> the original tool removed). It is **research material**, not an architecture specification: every disputed claim is
> verified against the referenced sources before corrections are applied (see `research/research-log.md`).

## Method and reliability criteria

The audit covers only the eleven active modes: Trimone, Mbare, Wallera, Daje, Mena, Minchia, Belin, Bischero, Boia dé,
Pirla and Potà, all `experimental`, without native-speaker review. Attestation, linguistic inference and original
examples must never be mixed. Popular sources are useful for interjections, insults and profanity, but a productive
grammatical or phonetic rule should rest mainly on lexicography, dialectological studies or institutional resources.

Files read: every `profile.md`; for Mena also `lexicon.json`, `profanity.json`, `proverbs.json`; for Mbare also
`lexicon.json` (branch `main`, 2026-11-25).

## Southern Italy

### Trimone — Barese
- Sources: profile; Treccani "Dialetti pugliesi" (https://www.treccani.it/enciclopedia/dialetti-pugliesi_(Enciclopedia-dell'Italiano)/) distinguishes centre-north Apulian from Salentino systems and describes vowel reduction and **metaphony**; Patrimoni Linguistici (https://patrimonilinguistici.it/trimone/) documents trimone/trmòn as insult/joking term.
- Final unstressed vowel reduction and metaphony are strong signals but must not become indiscriminate substitution.
- Recognizable lexicon: trimone/trmòn, uagnóne, local particles — better than constant spelling deformation.
- Error: the profile's split "non = city / nan = province" is too rigid to be a rule without a targeted urban corpus; folk etymologies must not become generative rules.
- Fix: build the effect mainly with attested morphosyntax and lexicon; phonetic transformations only on controlled lexemes.

### Wallera — Neapolitan
- Sources: profile (correctly separates commercial id `wallera` from `uallera/guallera`, Naples city norm); Universal Dependencies Neapolitan treebank (https://universaldependencies.org/nap/index.html) for grammar/tokenization.
- Metaphony, reduced unstressed vowels, local articles and pronouns are more reliable than theatrical word-by-word spelling.
- Error/risk: at least one blasphemous formula is marked **unverified** in the profile; it must not enter the "documented and generable" set. Avoid stereotyped spellings.
- Fix: keep the dubious formula only as data to verify or remove it from the generative path; render Neapolitan mainly through syntax, clitics, negation and lexicon.

### Mena — Leccese / peri-Leccese
- Sources: profile (target Lecce/peri-Leccese; -ll- outcomes, gemination, `cu` + finite verb); lexicon entries (ièu, tie, iddhu) marked "Lecce (Salentino centrale)"; profanity and proverbs files distinguish attested vs ai-illustrative and record locality.
- https://www.dialettosalentino.it/turre_1.html — author **Giuseppe Presicce**, material on "il dialetto salentino come si parla a Scorrano"; explains that **Turre = Torrepaduli, frazione di Ruffano**. Good local source for Scorrano and for how Scorrano refers to Torrepaduli; it does not prove a phrase belongs to Lecce city.
- **B→P**: no general B→P rule appears in the current profile; it must not be introduced. A global b→p substitution would be over-generalization producing artificial forms. -ll-→ddh, Salentine vowels and `cu` + finite verb are better founded but must also be applied only in documented contexts.
- **Turre expressions**: Presicce attests «rrimanire comu la zzita de Turre» (to prepare carefully and then, at the last moment, be unable to take part). The same page attests the exchange «Comu facimu?» answered with the Turre story of cutting off the bride's head: «Comu fìcera a Turre, ca ne taiàra la capu alla zzita!» (content and meaning confirmed; exact accents could not be verified byte-by-byte due to mojibake). The story: a Torrepaduli bride too tall to enter the church, and the absurd solution of cutting off her head. Both must be marked as **collected in Scorrano, referring to Torrepaduli (Ruffano)**, not as generic Lecce proverbs.
- **P0 error**: the contamination guard (≈ line 194/230) says centre-north Apulian dialects have schwa and "no metaphony". The absolute negation is wrong: Treccani describes metaphony as a relevant phenomenon in centre-north Apulian.
- Fix: remove "no metaphony"; no productive B→P; add explicit provenance and locality to the Turre items; do not turn Scorrano/Torrepaduli into "Lecce city".

## Sicily

### Mbare — Catanese
- Sources: profile (Catania and province, 'mbari/'mpari vocative, eastern Sicilian); lexicon (taliari, accattari, travagghiari, manciari, addumari); Treccani "siciliano" (https://www.treccani.it/enciclopedia/siciliano_(Enciclopedia-dell'Italiano)/): Sicilian traits are not uniformly distributed.
- Main issue: preconsonantal r. The profile (≈ line 24) presents carta→catta, corda→codda, carne→canni, porcu→poccu, merda→medda almost as a general transformation. A good descriptive marker, dangerous as an algorithm on arbitrary words; the same holds for d→r.
- Fix: rewrite as "strong Catanese tendency, applied to attested forms or explicitly validated classes; never a universal regex". Proper names, technical terms, anglicisms and words not in the lexicon are not modified by analogy.

### Minchia — Palermitano
- Sources: profile (Palermo city; minchia pan-Sicilian, authentic but not exclusively Palermitan); Treccani; Cademia Siciliana (https://cademiasiciliana.org/faq/) for supra-local spelling.
- The profile's opposition "Catania assimilates / Palermo preserves" for preconsonantal r should be less absolute: the Catanese profile has a much stronger assimilation tendency; Palermitan must not inherit those forms automatically — without claiming every Palermitan r+C is always intact.
- `minchia` must not become an obligatory token. Palermitan diphthongization can be described without making it an orthographic obligation.
- Fix: controlled list of attested lexemes; no transformations by analogy; keep the name Minchia.

## Centre and Tuscany

### Daje — Romanesco
- Sources: profile; Paolo D'Achille, "Italiano e dialetto a Roma", Treccani (https://www.treccani.it/enciclopedia/italiano-e-dialetto-a-roma_(Enciclopedia-dell'Italiano)/).
- nd→nn, gli→j, infinitive apocope, article `er` are still robust; **mb→mm is rare and ld→ll residual** (D'Achille).
- Historical material (Belli, Porena) is documentation, not to be projected automatically onto contemporary speech.
- Fix: mark mb→mm `rare`, ld→ll `residual/lexicalized`; default modern, lightly code-switching; historical layer only on request or at very high intensity.

### Bischero — Florentine
- Sources: profile; Treccani "Dialetti toscani" (https://www.treccani.it/enciclopedia/dialetti-toscani_(Enciclopedia-dell'Italiano)/) and vocabulary entry "bischero" (https://www.treccani.it/vocabolario/bischero/).
- `noi si + 3sg` and gorgia are recognizable; gorgia is a phonetic phenomenon, not a normal spelling with `h`.
- Error: the profile allows one or two `h` at intensity 5 to render gorgia — a stylization, not a natural convention.
- Fix: no phonetic `h` by default.

### Boia dé — Livornese
- Sources: profile (Pisan-Livornese group, `dé`); Treccani confirms the group and the vitality of `dé` in Livorno; /k/ weakening in the Pisan-Livornese area can reach deletion.
- `ir`, `dé`, some /k/ outcomes are useful, but /k/ deletion must not be "replace every intervocalic c with an apostrophe".
- Fix: `dé` relatively free but not obsessive; `boia` by emotion; elision only on documented forms; `boia dé` not a fixed formula in every line.

## North

### Belin — Genoese
- Sources: profile (Genoa city; Académia Ligùstica do Brénno spelling); Treccani "Dialetti liguri" (https://www.treccani.it/enciclopedia/dialetti-liguri_(Enciclopedia-dell'Italiano)/) describes belìn as vulgarism/filler and implicitly warns about its use as hyper-characterization.
- Fix: `belin` occasional, never "once per sentence"; readable colloquial spelling by default, denser official spelling only at high intensity.

### Pirla — Milanese
- Sources: profile (mixes classical tradition and modern urban use); Treccani "Dialetti lombardi" (https://www.treccani.it/enciclopedia/dialetti-lombardi_(Enciclopedia-dell'Italiano)/) documents the history of Italianization; Treccani vocabulary "pirla" (https://www.treccani.it/vocabolario/pirla/). Cherubini's dictionary (archive.org PDF) could not be fetched directly; a University of Milan lexicographic study reports `birlo`/`pirlapirla` (spinning top) and `pirla` as a shortened form, with obscene allusions already in 19th-century tradition.
- Error: mixing classical grammar and modern urban lexicon indiscriminately.
- Fix: default contemporary urban Milanese; classical forms only on request.

### Potà — Bergamasque
- Sources: profile (Eastern Lombard, city/lowland, pota/potà discourse marker); Treccani "Dialetti lombardi".
- The profile's s→h in some lowland areas and its warning that "h for f" is wrong are useful and must stay.
- Error: the prosodic stress-shift rule must not become automatic rewriting of every pòta/potà.
- Fix: keep attested variants; no global accent choice; no f→h.

## Suggested test specifications (not results)
1. Mena intensity 4, no blasphemy, explain a failed deploy — Salentine-central lexicon/syntax; no systematic B→P; no Scorrano proverb presented as Lecce city.
2. Same bug in Mbare then Minchia — distinguishable; no universal r+C regex.
3. Pirla: "I deleted the wrong branch, tease me like a Milanese colleague" — contemporary usage; no automatic 19th-century grammar.
4. Daje intensity 2: race condition — light contemporary Romanesco; no mb→mm/ld→ll pile-up.
5. Bischero and Boia dé on the same compile error — distinct; no systematic h; natural dé.
6. Belin: colloquial non-caricatural code review — occasional belin.
7. Wallera vulgarity 3: broken test — attested profanity; no unverified item promoted.
8. Trimone among friends: tease me for a typo — friendly tone; no slurs; no pseudo-Barese by vowel mutation only.

## Priorities
- P0: Mena metaphony statement, Turre provenance, B→P explicitly not productive; Mbare/Minchia preconsonantal r as lexically constrained.
- P1: Daje mb→mm rare / ld→ll residual; Bischero no h gorgia by default; Wallera unverified blasphemy not generated; Pirla historical vs contemporary; Belin density; boia dé not fixed formula.
- P2: uniform `geographical_area`, `register`, `provenance`, `verification_status`, `generation_allowed`.

## Operative bibliography
ItalianAccent repository; G. Presicce, *Il dialetto salentino come si parla a Scorrano* (https://www.dialettosalentino.it/turre_1.html); Treccani entries on Apulian, Sicilian, Lombard, Ligurian, Tuscan dialects and contemporary Romanesco; Cademia Siciliana FAQ; Universal Dependencies Neapolitan; F. Cherubini, *Vocabolario milanese-italiano* (archive.org scan, access limited). Dictionaries and collections must not be reproduced extensively.
