import re


def test_frontmatter_spec(v):
    text = (v.SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    fm = v.parse_frontmatter(text)
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    assert set(fm) <= allowed, f"non-portable frontmatter keys: {set(fm) - allowed}"
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", fm["name"]) and len(fm["name"]) <= 64
    assert fm["name"] == v.SKILL_DIR.name == "italianaccent"
    assert 1 <= len(fm["description"]) <= 1024
    assert len(fm.get("compatibility", "x")) <= 500
    assert all(isinstance(k, str) and isinstance(val, str) for k, val in fm["metadata"].items())


def test_skill_md_size_and_activation_guard(v):
    text = (v.SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    assert len(text.splitlines()) < 500
    fm = v.parse_frontmatter(text)
    assert "explicitly" in fm["description"]
    assert "Activation guard" in text


def test_skill_references_exist(v):
    rep = v.Report()
    v.validate_skill(rep)
    assert not rep.errors, rep.errors


def test_core_reference_files_exist(v):
    for f in ["catalog.json", "defaults.json", "behavior.md", "commands.md", "dialect-loading.md"]:
        assert (v.REFS / f).exists(), f


def test_skill_has_no_runtime_scripts(v):
    assert not any(p.suffix in {".py", ".sh", ".js", ".ps1", ".exe"} for p in v.SKILL_DIR.rglob("*"))
