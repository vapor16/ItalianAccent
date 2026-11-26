#!/usr/bin/env python3
"""ItalianAccent repository validator (development/CI tool, never needed at runtime).

Usage:
  python scripts/validate.py              # full validation, exit 1 on errors
  python scripts/validate.py --profile ID # validate a single dialect profile
  python scripts/validate.py --stats      # print real knowledge-base statistics (Markdown)
  python scripts/validate.py --zip        # build dist/italianaccent-<version>.zip (skill folder only)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "italianaccent"
REFS = SKILL_DIR / "references"
DIALECTS = REFS / "dialects"
SCHEMAS = ROOT / "schemas"
SOURCES_FILE = ROOT / "research" / "sources.json"

COLLECTIONS = {
    "lexicon.json": "lexicon.schema.json",
    "proverbs.json": "proverbs.schema.json",
    "profanity.json": "profanity.schema.json",
}
REQUIRED_PROFILE_FILES = ["metadata.json", "profile.md", "lexicon.json", "proverbs.json",
                          "profanity.json", "examples.md", "sources.md"]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def normalize(text: str) -> str:
    """Case-, accent-, apostrophe- and punctuation-insensitive key."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", text)


def load_json(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def parse_frontmatter(text: str) -> dict:
    import yaml  # dev dependency

    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter ('---')")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter is not closed")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def validator_for(schema_name: str):
    from jsonschema import Draft202012Validator

    schema = load_json(SCHEMAS / schema_name)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def schema_errors(data, schema_name: str) -> list[str]:
    v = validator_for(schema_name)
    return [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}" for e in v.iter_errors(data)]


def source_ids() -> set[str]:
    if not SOURCES_FILE.exists():
        return set()
    return {s["id"] for s in load_json(SOURCES_FILE).get("sources", [])}


def validate_skill(rep: Report) -> dict:
    path = SKILL_DIR / "SKILL.md"
    if not path.exists():
        rep.err("skills/italianaccent/SKILL.md missing")
        return {}
    text = path.read_text(encoding="utf-8")
    try:
        fm = parse_frontmatter(text)
    except Exception as exc:  # noqa: BLE001
        rep.err(f"SKILL.md: {exc}")
        return {}
    name = fm.get("name")
    if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
        rep.err(f"SKILL.md: invalid name {name!r}")
    if name != SKILL_DIR.name:
        rep.err("SKILL.md: name must match parent directory")
    desc = fm.get("description")
    if not isinstance(desc, str) or not (1 <= len(desc) <= 1024):
        rep.err("SKILL.md: description must be 1..1024 characters")
    if len(text.splitlines()) > 500:
        rep.warn("SKILL.md longer than 500 lines; move detail into references/")
    # every referenced local file must exist
    for ref in re.findall(r"\(?(references/[A-Za-z0-9_./<>-]+\.(?:md|json))", text):
        if "<" in ref:
            continue
        if not (SKILL_DIR / ref).exists():
            rep.err(f"SKILL.md references missing file {ref}")
    return fm


def validate_catalog(rep: Report) -> list[dict]:
    path = REFS / "catalog.json"
    if not path.exists():
        rep.err("catalog.json missing")
        return []
    cat = load_json(path)
    for e in schema_errors(cat, "catalog.schema.json"):
        rep.err(f"catalog.json: {e}")
    seen: dict[str, str] = {}
    for mode in cat.get("modes", []):
        keys = {normalize(mode["id"]), normalize(mode["display_name"])} | {normalize(a) for a in mode.get("aliases", [])}
        for k in keys:
            if k in seen and seen[k] != mode["id"]:
                rep.err(f"catalog: alias/id collision '{k}' between {seen[k]} and {mode['id']}")
            seen[k] = mode["id"]
        pdir = DIALECTS / mode["id"]
        if mode["available"]:
            if mode["maturity"] == "planned":
                rep.err(f"catalog: {mode['id']} is planned but marked available")
            if not pdir.is_dir():
                rep.err(f"catalog: available mode {mode['id']} has no profile directory")
        if pdir.is_dir() and mode.get("path") and mode["path"] != f"references/dialects/{mode['id']}/":
            rep.err(f"catalog: {mode['id']} path mismatch")
    for d in DIALECTS.iterdir() if DIALECTS.exists() else []:
        if d.is_dir() and d.name not in {m["id"] for m in cat.get("modes", [])}:
            rep.err(f"profile directory {d.name} not present in catalog")
    return cat.get("modes", [])


def validate_profile(pid: str, rep: Report, catalog_entry: dict | None = None, srcs: set[str] | None = None) -> None:
    pdir = DIALECTS / pid
    if srcs is None:
        srcs = source_ids()
        raw = ROOT / "research" / "raw" / f"{pid}-sources.json"
        if raw.exists():
            srcs |= {s["id"] for s in load_json(raw).get("sources", [])}
    missing = [f for f in REQUIRED_PROFILE_FILES if not (pdir / f).exists()]
    for f in missing:
        rep.err(f"{pid}: missing {f}")
    if (pdir / "metadata.json").exists():
        meta = load_json(pdir / "metadata.json")
        for e in schema_errors(meta, "metadata.schema.json"):
            rep.err(f"{pid}/metadata.json: {e}")
        if meta.get("id") != pid:
            rep.err(f"{pid}/metadata.json: id mismatch")
        if meta.get("maturity") in {"community-reviewed", "verified"} and not meta.get("reviews"):
            rep.err(f"{pid}: maturity {meta['maturity']} requires documented reviews")
        for rel in meta.get("resources", {}).values():
            if not (pdir / rel).exists():
                rep.err(f"{pid}/metadata.json: resource {rel} missing")
        for s in meta.get("sources", []):
            if srcs and s not in srcs:
                rep.err(f"{pid}/metadata.json: unknown source {s}")
        if catalog_entry is not None:
            for k in ("display_name", "maturity", "available"):
                if catalog_entry.get(k) != meta.get(k):
                    rep.err(f"{pid}: catalog/{k} ({catalog_entry.get(k)!r}) != metadata ({meta.get(k)!r})")
    for fname, schema in COLLECTIONS.items():
        fp = pdir / fname
        if not fp.exists():
            continue
        try:
            data = load_json(fp)
        except json.JSONDecodeError as exc:
            rep.err(f"{pid}/{fname}: invalid JSON: {exc}")
            continue
        for e in schema_errors(data, schema):
            rep.err(f"{pid}/{fname}: {e}")
        if data.get("dialect") != pid:
            rep.err(f"{pid}/{fname}: dialect field must be '{pid}'")
        ids, keys = set(), {}
        for entry in data.get("entries", []):
            eid = entry.get("id")
            if eid in ids:
                rep.err(f"{pid}/{fname}: duplicate id {eid}")
            ids.add(eid)
            text = entry.get("term") or entry.get("original") or ""
            # homographs are allowed when the part of speech differs
            k = normalize(text) + "|" + normalize(entry.get("part_of_speech", ""))
            if k in keys:
                rep.err(f"{pid}/{fname}: duplicate entry '{text}' ({keys[k]} / {eid})")
            keys[k] = eid
            prov = entry.get("provenance")
            es = entry.get("sources", [])
            if prov in {"attested", "documented-rule"} and not es:
                rep.err(f"{pid}/{fname}:{eid}: provenance '{prov}' requires sources")
            for s in es:
                if srcs and s not in srcs:
                    rep.err(f"{pid}/{fname}:{eid}: unknown source {s}")
            if entry.get("verification_status") in {"community-reviewed", "native-reviewed"}:
                rep.err(f"{pid}/{fname}:{eid}: review status claimed without review record")
    if (pdir / "profile.md").exists():
        txt = (pdir / "profile.md").read_text(encoding="utf-8")
        if len(txt.splitlines()) < 60:
            rep.warn(f"{pid}/profile.md is very short ({len(txt.splitlines())} lines)")
        if re.search(r"[A-Za-zÀ-ÿ]\*+[A-Za-zÀ-ÿ]", txt):
            rep.err(f"{pid}/profile.md contains asterisk-censored words")


def validate_sources(rep: Report) -> set[str]:
    if not SOURCES_FILE.exists():
        rep.err("research/sources.json missing")
        return set()
    data = load_json(SOURCES_FILE)
    for e in schema_errors(data, "sources.schema.json"):
        rep.err(f"sources.json: {e}")
    ids = [s["id"] for s in data.get("sources", [])]
    dup = {i for i in ids if ids.count(i) > 1}
    for d in dup:
        rep.err(f"sources.json: duplicate id {d}")
    for s in data.get("sources", []):
        if s.get("redistribution") == "not-permitted" and s.get("used_by"):
            rep.warn(f"sources.json: {s['id']} is citation-only; ensure no verbatim copying")
    return set(ids)


def validate_versions(rep: Report, fm: dict) -> None:
    import tomllib

    versions = {}
    versions["pyproject"] = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]
    if fm:
        versions["SKILL.md"] = str((fm.get("metadata") or {}).get("version"))
    for f in [ROOT / ".claude-plugin" / "plugin.json"]:
        if f.exists():
            versions[f.name] = load_json(f).get("version")
    mk = ROOT / ".claude-plugin" / "marketplace.json"
    if mk.exists():
        for p in load_json(mk).get("plugins", []):
            if p.get("version"):
                versions["marketplace.json"] = p["version"]
    if len(set(versions.values())) > 1:
        rep.err(f"version mismatch: {versions}")
    cl = ROOT / "CHANGELOG.md"
    if cl.exists() and f"[{versions['pyproject']}]" not in cl.read_text():
        rep.err("CHANGELOG.md has no entry for current version")


def validate_defaults(rep: Report) -> None:
    p = REFS / "defaults.json"
    if not p.exists():
        rep.err("defaults.json missing")
        return
    for e in schema_errors(load_json(p), "defaults.schema.json"):
        rep.err(f"defaults.json: {e}")


def run_all() -> Report:
    rep = Report()
    for s in SCHEMAS.glob("*.json"):
        try:
            validator_for(s.name)
        except Exception as exc:  # noqa: BLE001
            rep.err(f"schema {s.name}: {exc}")
    for p in ROOT.rglob("*.json"):
        if any(part in {".git", "node_modules", "dist"} for part in p.parts):
            continue
        try:
            load_json(p)
        except json.JSONDecodeError as exc:
            rep.err(f"{p.relative_to(ROOT)}: invalid JSON: {exc}")
    fm = validate_skill(rep)
    srcs = validate_sources(rep)
    validate_defaults(rep)
    modes = validate_catalog(rep)
    for m in modes:
        if (DIALECTS / m["id"]).is_dir():
            validate_profile(m["id"], rep, m, srcs)
    validate_versions(rep, fm)
    return rep


def stats() -> str:
    cat = load_json(REFS / "catalog.json")
    rows = ["| Mode | Variety | Region | Maturity | Lexicon | Interj. | Colloquial | Proverbs | Idioms/sayings | Profanity | Sources |",
            "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    tot = dict(lex=0, inter=0, coll=0, prov=0, idi=0, prof=0)
    regions = set()
    for m in cat["modes"]:
        d = DIALECTS / m["id"]
        if not d.is_dir():
            continue
        lex = load_json(d / "lexicon.json")["entries"]
        pv = load_json(d / "proverbs.json")["entries"]
        pf = load_json(d / "profanity.json")["entries"]
        meta = load_json(d / "metadata.json")
        c = dict(lex=sum(e["category"] in {"word", "function-word", "address-term", "greeting"} for e in lex),
                 inter=sum(e["category"] == "interjection" for e in lex),
                 coll=sum(e["category"] == "colloquial-expression" for e in lex),
                 prov=sum(e["type"] == "proverb" for e in pv), idi=sum(e["type"] != "proverb" for e in pv), prof=len(pf))
        for k in tot:
            tot[k] += c[k]
        if m["available"]:
            regions.add(m["region"])
        rows.append(f"| {m['display_name']} (`{m['id']}`) | {m['variety']} | {m['region']} | {m['maturity']} | "
                    f"{c['lex']} | {c['inter']} | {c['coll']} | {c['prov']} | {c['idi']} | {c['prof']} | {len(meta['sources'])} |")
    rows.append(f"| **Total** | | {len(regions)} regions | | {tot['lex']} | {tot['inter']} | {tot['coll']} | {tot['prov']} | {tot['idi']} | {tot['prof']} | {len(source_ids())} (registry) |")
    return "\n".join(rows)


def catalog_md() -> str:
    cat = load_json(REFS / "catalog.json")
    av = [m for m in cat["modes"] if m["available"]]
    rows = ["| Mode | Variety | Region | Meaning of the mode name | Status |", "|---|---|---|---|---|"]
    for m in sorted(av, key=lambda m: (m["region"], m["id"])):
        rows.append(f"| **{m['display_name']}** (`{m['id']}`) | {m['variety']} | {m['region']} | "
                    f"{m.get('identifier_meaning_en', '')} | {m['maturity']} |")
    planned = [m for m in cat["modes"] if not m["available"]]
    regions = sorted({m["region"] for m in av})
    rows += ["", f"**{len(av)} available modes covering {len(regions)} of 20 regions** "
             f"({', '.join(regions)}). {len(planned)} further varieties are listed as `planned` in "
             "[catalog.json](skills/italianaccent/references/catalog.json) and are not activatable yet."]
    return "\n".join(rows)


def update_readmes() -> None:
    block = catalog_md()
    for name in ["README.md", "README.it.md"]:
        f = ROOT / name
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8")
        t = re.sub(r"(<!-- CATALOG:START -->).*?(<!-- CATALOG:END -->)", lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", t, flags=re.S)
        f.write_text(t, encoding="utf-8")


DIRECTORY = ROOT / "claude-directory"
DIRECTORY_README = """# ItalianAccent

**Artificial Intelligence. Authentic Italian Attitude.**

ItalianAccent is an open-source Agent Skill that makes Claude answer like someone from an Italian city: the local
variety's grammar, syntax and vocabulary, plus slang, proverbs, idioms, humor, sarcasm and uncensored profanity.
It is a declarative skill (Markdown and JSON only, no executable code).

> **Adults only — explicit language.** Active modes use vulgar language, insults and imprecations by default
> (vulgarity 5). Nothing changes until you explicitly activate a mode, and you can lower vulgarity to 0 or switch
> ItalianAccent off at any time. The host model's safety rules always apply.

## Modes

| Mode | Variety | Region |
|---|---|---|
| `trimone` | Barese | Puglia |
| `mena` | Leccese (Salentino centrale) | Puglia |
| `wallera` | Napoletano | Campania |
| `daje` | Romanesco | Lazio |
| `mbare` | Catanese | Sicilia |
| `minchia` | Palermitano | Sicilia |
| `belin` | Genovese | Liguria |
| `bischero` | Fiorentino | Toscana |
| `boiade` (Boia dé) | Livornese | Toscana |
| `pirla` | Milanese | Lombardia |
| `pota` (Potà) | Bergamasco | Lombardia |

All modes are **experimental**: researched from documented sources but not yet reviewed by native speakers, so
expect mistakes and local differences.

## Install

```text
/plugin install italianaccent --marketplace vapor16/italianaccent
```

## Usage

Installed as a plugin, the command is namespaced:

```text
/italianaccent:italianaccent                   help and list of modes
/italianaccent:italianaccent wallera           activate (dialect intensity 5, vulgarity 5)
/italianaccent:italianaccent daje --intensity 3 --vulgarity 2
/italianaccent:italianaccent vulgarity 0       no profanity, dialect kept
/italianaccent:italianaccent intensity 2       regional Italian instead of full dialect
/italianaccent:italianaccent proverbs off      also: idioms, humor, sarcasm, translation on|off
/italianaccent:italianaccent status
/italianaccent:italianaccent off               back to normal
```

Natural language also works: "Activate ItalianAccent in Daje mode." Code, commands and technical facts are never
altered; only the prose around them changes.

## Links

- Documentation: https://github.com/vapor16/ItalianAccent/blob/main/README.md
- Privacy policy: https://github.com/vapor16/ItalianAccent/blob/main/PRIVACY.md
- Support: https://github.com/vapor16/ItalianAccent/issues
- License: MIT (see LICENSE). Third-party sources: THIRD_PARTY_NOTICES.md
"""


def build_directory() -> Path:
    """Generate the Claude Public Directory package from the single source of truth (never edit it by hand)."""
    import shutil

    if DIRECTORY.exists():
        shutil.rmtree(DIRECTORY)
    shutil.copytree(SKILL_DIR, DIRECTORY / "skills" / "italianaccent",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
    (DIRECTORY / ".claude-plugin").mkdir(parents=True)
    shutil.copy2(ROOT / ".claude-plugin" / "plugin.json", DIRECTORY / ".claude-plugin" / "plugin.json")
    shutil.copy2(ROOT / ".claude-plugin" / "icon.png", DIRECTORY / ".claude-plugin" / "icon.png")
    shutil.copy2(ROOT / "LICENSE", DIRECTORY / "LICENSE")
    notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8").replace(
        "`research/sources.json`",
        "https://github.com/vapor16/ItalianAccent/blob/main/research/sources.json")
    (DIRECTORY / "THIRD_PARTY_NOTICES.md").write_text(notices, encoding="utf-8")
    (DIRECTORY / "README.md").write_text(DIRECTORY_README, encoding="utf-8")
    return DIRECTORY


def build_zip() -> Path:
    fm = parse_frontmatter((SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"))
    version = (fm.get("metadata") or {}).get("version", "0.0.0")
    out = ROOT / "dist" / f"italianaccent-{version}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(SKILL_DIR.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                zf.write(f, Path("italianaccent") / f.relative_to(SKILL_DIR))
        zf.write(ROOT / "LICENSE", "italianaccent/LICENSE")
    return out


def integrate(pid: str) -> list[str]:
    """Merge research/raw/<pid>-sources.json into the registry, write sources.md, sync catalog from metadata."""
    notes = []
    pdir = DIALECTS / pid
    reg = load_json(SOURCES_FILE)
    by_id = {s["id"]: s for s in reg["sources"]}
    raw = ROOT / "research" / "raw" / f"{pid}-sources.json"
    if raw.exists():
        for s in load_json(raw).get("sources", []):
            s = dict(s)
            if s["id"] in by_id:
                used = set(by_id[s["id"]].get("used_by", [])) | {pid}
                by_id[s["id"]]["used_by"] = sorted(used)
                continue
            s["used_by"] = sorted(set(s.get("used_by", [])) | {pid})
            by_id[s["id"]] = s
            notes.append(f"added source {s['id']}")
    reg["sources"] = sorted(by_id.values(), key=lambda s: s["id"])
    SOURCES_FILE.write_text(json.dumps(reg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    meta = load_json(pdir / "metadata.json")
    used = set(meta.get("sources", []))
    for fname in COLLECTIONS:
        if (pdir / fname).exists():
            for e in load_json(pdir / fname)["entries"]:
                used |= set(e.get("sources", []))
    lines = [f"# Sources — {meta['display_name']} ({meta.get('geographical_area') or meta['region']})", "",
             "Generated from the project source registry "
             "(https://github.com/vapor16/ItalianAccent/blob/main/research/sources.json). "
             "Meanings and annotations in this profile are original; sources are cited, not copied.", "",
             "| ID | Title | Author / Publisher | Type | Reliability | License / redistribution | URL |",
             "|---|---|---|---|---|---|---|"]
    for sid in sorted(used):
        s = by_id.get(sid)
        if not s:
            notes.append(f"WARNING unknown source {sid}")
            continue
        who = " / ".join(x for x in [s.get("author", ""), s.get("publisher", "")] if x)
        lines.append(f"| `{sid}` | {s['title']} | {who} | {s['source_type']} | {s['reliability']} | "
                     f"{s['license']} ({s['redistribution']}) | <{s['url']}> |")
    lines += ["", "Access dates and full metadata: https://github.com/vapor16/ItalianAccent/blob/main/research/sources.json", ""]
    (pdir / "sources.md").write_text("\n".join(lines), encoding="utf-8")
    meta["sources"] = sorted(used & set(by_id))
    (pdir / "metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    cat_path = REFS / "catalog.json"
    cat = load_json(cat_path)
    for m in cat["modes"]:
        if m["id"] == pid:
            m["maturity"], m["available"] = meta["maturity"], meta["available"]
            m["display_name"] = meta["display_name"]
            m["path"] = f"references/dialects/{pid}/"
    cat_path.write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return notes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--zip", action="store_true")
    ap.add_argument("--integrate", metavar="ID")
    ap.add_argument("--readme", action="store_true", help="regenerate the catalog tables in the READMEs")
    ap.add_argument("--directory", action="store_true", help="regenerate claude-directory/ (Claude Public Directory package)")
    a = ap.parse_args()
    if a.stats:
        print(stats())
        return 0
    if a.directory:
        print(build_directory())
        return 0
    if a.readme:
        update_readmes()
        return 0
    if a.integrate:
        for n in integrate(a.integrate):
            print(n)
        rep = Report()
        validate_profile(a.integrate, rep)
        for e in rep.errors:
            print(f"ERROR {e}")
        return 1 if rep.errors else 0
    if a.zip:
        print(build_zip())
        return 0
    if a.profile:
        rep = Report()
        validate_profile(a.profile, rep)
    else:
        rep = run_all()
    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")
    print(f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
