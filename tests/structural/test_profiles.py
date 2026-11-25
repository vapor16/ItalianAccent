import pytest


def _ids(v):
    return sorted(d.name for d in v.DIALECTS.iterdir() if d.is_dir()) if v.DIALECTS.exists() else []


def pytest_generate_tests(metafunc):
    if "pid" in metafunc.fixturenames:
        from ia_validate import DIALECTS
        ids = sorted(d.name for d in DIALECTS.iterdir() if d.is_dir()) if DIALECTS.exists() else []
        metafunc.parametrize("pid", ids)


def test_profile_valid(v, pid, catalog):
    entry = next(m for m in catalog["modes"] if m["id"] == pid)
    rep = v.Report()
    v.validate_profile(pid, rep, entry)
    assert not rep.errors, "\n".join(rep.errors)


def test_profile_md_sections(v, pid):
    txt = (v.DIALECTS / pid / "profile.md").read_text(encoding="utf-8").lower()
    for kw in ["orthograph", "morpholog", "verb", "syntax", "lexicon", "profanity", "proverb", "contamination"]:
        assert kw in txt, f"{pid}/profile.md lacks a section about {kw}"


def test_examples_marked_illustrative(v, pid):
    txt = (v.DIALECTS / pid / "examples.md").read_text(encoding="utf-8").lower()
    assert "illustrative" in txt


def test_available_profiles_have_core_content(v, pid, catalog):
    import json
    entry = next(m for m in catalog["modes"] if m["id"] == pid)
    if not entry["available"]:
        pytest.skip("planned profile")
    d = v.DIALECTS / pid
    for f in ["lexicon.json", "proverbs.json", "profanity.json"]:
        assert json.loads((d / f).read_text())["entries"], f"{pid}/{f} is empty"
