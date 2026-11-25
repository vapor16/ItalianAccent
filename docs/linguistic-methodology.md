# Linguistic methodology

## Terminology

"Italian dialects" is the popular name used by this project. Linguistically, most of these varieties are
**Italo-Romance languages or dialects that developed from Latin independently of Tuscan/standard Italian** —
they are not "dialects of Italian". Several have official or scholarly recognition as distinct languages
(e.g. Sardinian, Friulian, Ladin, Franco-Provençal under Italian Law 482/1999; Neapolitan and Sicilian are
classified as distinct languages by UNESCO and ISO 639-3 codes `nap`, `scn`). Others (Tuscan, Romanesco) are
close to standard Italian. Regional Italian (*italiano regionale*) — standard Italian with local features — is a
different thing, and corresponds to ItalianAccent's intensity levels 1–2.

Each profile states its classification in `metadata.json` and `profile.md` §1.

## Research process (per profile)

1. **Localization**: identify the exact variety the mode represents (city or area) and the neighbouring varieties
   it must not be confused with.
2. **Source discovery** with free tools only (web search, direct reading of pages). Priority: public-domain
   historical dictionaries, academic/institutional pages, Wikipedia/Wiktionary (Italian and regional-language
   editions), cultural associations, public-domain literature; popular sites only for colloquial/vulgar items.
3. **Extraction as facts**: we note *that* a word/rule/proverb exists and what it means, and write our own
   description. No dictionary text is copied.
4. **Classification**: each entry carries `provenance` (attested, documented-rule, ai-illustrative, unverified,
   community, native-reviewed) and `verification_status`.
5. **Synthesis**: `profile.md` turns the documented rules into operational instructions for the model,
   with AI-illustrative example sentences clearly labelled.
6. **Contamination check**: forms are checked against neighbouring varieties.
7. **Validation**: schemas + tests (structure, references, duplicates, provenance). These checks guarantee
   consistency, **not linguistic authenticity**.
8. **Behavioral evaluation**: AI-assisted runs of the skill with a rubric (see `tests/behavioral/`).
9. **Human review** (pending for all profiles): local speakers review via issues/PRs; only then can maturity rise.

## Orthography

Most of these varieties have no single standard orthography. Each profile adopts one convention (documented in
`profile.md` §2) and lists attested alternatives as `variants`. The commercial mode name (e.g. `wallera`) is a
product name and may differ from scholarly spelling (`uallera`); this is stated in `metadata.identifier_word`.

## Limits

- All v1.0.0 profiles are **experimental**: researched by AI agents from documented sources, not reviewed by
  native speakers.
- Sources on profanity are mostly popular/community sources and have lower reliability.
- Local variation inside a province or city is large; profiles describe one reference norm.
- AI-illustrative examples demonstrate documented rules; they are not transcriptions of real speech.

## Catalog corrections

Any correction to the association between a mode name and a variety is recorded here and in `catalog.json`.
