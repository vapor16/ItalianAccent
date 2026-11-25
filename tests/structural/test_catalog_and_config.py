import json

MANDATED = {"mbare", "trimone", "wallera", "daje", "mena"}


def test_schemas_are_valid(v):
    for s in v.SCHEMAS.glob("*.json"):
        v.validator_for(s.name)


def test_catalog_schema(v, catalog):
    assert v.schema_errors(catalog, "catalog.schema.json") == []


def test_mandated_mode_names(catalog):
    ids = {m["id"] for m in catalog["modes"]}
    assert MANDATED <= ids
    nap = next(m for m in catalog["modes"] if m["id"] == "wallera")
    assert nap["variety"] == "Napoletano"
    assert "guaglio" not in {m["id"] for m in catalog["modes"]}


def test_unique_ids_and_aliases(v, catalog):
    seen = {}
    for m in catalog["modes"]:
        keys = {v.normalize(m["id"]), v.normalize(m["display_name"])} | {v.normalize(a) for a in m["aliases"]}
        for k in keys:
            assert seen.get(k, m["id"]) == m["id"], f"collision on {k}: {seen.get(k)} vs {m['id']}"
            seen[k] = m["id"]


def test_available_modes_have_profiles(v, available_modes):
    for m in available_modes:
        assert m["maturity"] != "planned"
        assert (v.DIALECTS / m["id"]).is_dir()


def test_planned_modes_not_available(catalog):
    for m in catalog["modes"]:
        if m["maturity"] == "planned":
            assert m["available"] is False


def test_defaults(v):
    d = json.loads((v.REFS / "defaults.json").read_text())
    assert v.schema_errors(d, "defaults.schema.json") == []
    assert d["dialect_intensity"] == 5 and d["vulgarity"] == 5
    assert d["proverbs"] and d["idioms"] and d["humor"] and d["sarcasm"]
    assert d["italian_translation"] is False and d["stylistic_censorship"] is False


def test_manifests(v):
    root = v.ROOT
    plugin = json.loads((root / ".claude-plugin" / "plugin.json").read_text())
    market = json.loads((root / ".claude-plugin" / "marketplace.json").read_text())
    assert plugin["name"] == "italianaccent"
    assert market["name"] and market["owner"]["name"]
    entry = market["plugins"][0]
    assert entry["name"] == plugin["name"] and entry["source"] == "./"


def test_versions_consistent(v):
    rep = v.Report()
    fm = v.parse_frontmatter((v.SKILL_DIR / "SKILL.md").read_text())
    v.validate_versions(rep, fm)
    assert not rep.errors, rep.errors


def test_full_validation_passes(v):
    rep = v.run_all()
    assert not rep.errors, "\n".join(rep.errors)
