import json

REVIEW_STATES = {"community-reviewed", "native-reviewed"}


def _profiles(v):
    return sorted(d for d in v.DIALECTS.iterdir() if d.is_dir()) if v.DIALECTS.exists() else []


def _entries(d, f):
    return json.loads((d / f).read_text(encoding="utf-8"))["entries"]


def test_sources_registry(v):
    rep = v.Report()
    v.validate_sources(rep)
    assert not rep.errors, rep.errors


def test_sources_metadata_complete(v):
    for s in json.loads(v.SOURCES_FILE.read_text())["sources"]:
        for k in ["title", "url", "access_date", "license", "redistribution", "reliability", "source_type"]:
            assert s.get(k), f"{s['id']} missing {k}"


def test_every_profile_source_resolves(v):
    ids = v.source_ids()
    for d in _profiles(v):
        meta = json.loads((d / "metadata.json").read_text())
        assert set(meta["sources"]) <= ids, f"{d.name}: {set(meta['sources']) - ids}"
        for f in ["lexicon.json", "proverbs.json", "profanity.json"]:
            for e in _entries(d, f):
                assert set(e.get("sources", [])) <= ids, f"{d.name}/{f}:{e['id']}"


def test_attested_entries_have_sources(v):
    for d in _profiles(v):
        for f in ["lexicon.json", "proverbs.json", "profanity.json"]:
            for e in _entries(d, f):
                if e["provenance"] in {"attested", "documented-rule"}:
                    assert e.get("sources"), f"{d.name}/{f}:{e['id']}"


def test_no_unrecorded_reviews(v):
    for d in _profiles(v):
        meta = json.loads((d / "metadata.json").read_text())
        if meta["maturity"] in {"community-reviewed", "verified"}:
            assert meta["reviews"]
        for f in ["lexicon.json", "proverbs.json", "profanity.json"]:
            for e in _entries(d, f):
                assert e["verification_status"] not in REVIEW_STATES or meta["reviews"]


def test_no_duplicates_within_files(v):
    for d in _profiles(v):
        for f, key in [("lexicon.json", "term"), ("proverbs.json", "original"), ("profanity.json", "original")]:
            seen = set()
            for e in _entries(d, f):
                k = v.normalize(e[key]) + "|" + v.normalize(e.get("part_of_speech", ""))
                assert k not in seen, f"{d.name}/{f}: duplicate {e[key]}"
                seen.add(k)


def test_profanity_levels_and_flags(v):
    for d in _profiles(v):
        for e in _entries(d, "profanity.json"):
            assert 1 <= e["intensity"] <= 5
            if e["category"] == "blasphemy":
                assert e.get("blasphemy") is True, f"{d.name}:{e['id']} blasphemy flag"
            if e.get("blasphemy"):
                assert e["intensity"] >= 4, f"{d.name}:{e['id']} blasphemy must be level >= 4"
            assert "*" not in e["original"], f"{d.name}:{e['id']} censored spelling"


def test_meanings_present(v):
    for d in _profiles(v):
        for f in ["lexicon.json", "proverbs.json", "profanity.json"]:
            for e in _entries(d, f):
                assert e["meaning_it"].strip() and e["meaning_en"].strip()


def test_metadata_area_matches_catalog(v, catalog):
    by = {m["id"]: m for m in catalog["modes"]}
    for d in _profiles(v):
        meta = json.loads((d / "metadata.json").read_text())
        assert meta["region"] == by[d.name]["region"], d.name
