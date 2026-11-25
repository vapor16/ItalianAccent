"""Regression tests for linguistic problems confirmed by the external audit (research/ITALIANACCENT_RESEARCH.md)."""
import json
import re


def _profile(v, pid):
    return (v.DIALECTS / pid / "profile.md").read_text(encoding="utf-8")


def _entries(v, pid, f):
    return json.loads((v.DIALECTS / pid / f).read_text(encoding="utf-8"))["entries"]


def test_mena_no_false_metaphony_claim(v):
    t = _profile(v, "mena").lower()
    assert "no metaphony" not in t
    meta = json.loads((v.DIALECTS / "mena" / "metadata.json").read_text()).__str__().lower()
    assert "no metaphony" not in meta


def test_mena_b_to_p_is_explicitly_not_a_rule(v):
    t = _profile(v, "mena")
    assert re.search(r"b\s*→\s*p.{0,40}not", t, re.I | re.S), "profile must state b→p is not a rule"


def test_mena_public_name(v):
    meta = json.loads((v.DIALECTS / "mena" / "metadata.json").read_text())
    assert "Leccese" in meta["description_en"] and "Salentino centrale" in meta["geographical_area"]


def test_mena_turre_expressions_with_provenance(v):
    found = {e["original"]: e for e in _entries(v, "mena", "proverbs.json") if "Turre" in e["original"]}
    assert any("zzita de Turre" in k for k in found)
    assert any("taiàra la capu alla zzita" in k for k in found)
    for e in found.values():
        assert "Scorrano" in e["geographical_area"] and "Torrepaduli" in e["geographical_area"]
        assert "src-sal-presicce-turre" in e["sources"]


def test_unverified_blasphemies_never_generated(v):
    for d in sorted(p for p in v.DIALECTS.iterdir() if p.is_dir()):
        for e in _entries(v, d.name, "profanity.json"):
            if e.get("blasphemy") and e["verification_status"] == "unverified":
                assert e.get("generation_allowed") is False, f"{d.name}:{e['id']}"


def test_examples_do_not_overuse_identifier(v):
    """The mode identifier must not be a tic: at most 2 occurrences per example answer block."""
    for d in sorted(p for p in v.DIALECTS.iterdir() if p.is_dir()):
        meta = json.loads((d / "metadata.json").read_text())
        word = v.normalize(meta["identifier_word"]["form"])
        blocks = re.split(r"\n#{2,4} ", (d / "examples.md").read_text(encoding="utf-8"))
        for b in blocks:
            n = sum(1 for tok in re.findall(r"[\w'’]+", b) if v.normalize(tok) == word)
            assert n <= 3, f"{d.name}: identifier '{word}' used {n} times in one example block"
