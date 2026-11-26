"""The Claude Public Directory package (claude-directory/) must be a generated, text-only copy of the skill."""
import filecmp
import json
import re


def _files(base):
    return sorted(p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file())


def test_directory_skill_is_identical_to_source(v):
    pkg = v.ROOT / "claude-directory" / "skills" / "italianaccent"
    assert _files(pkg) == _files(v.SKILL_DIR), "run: python scripts/validate.py --directory"
    for rel in _files(v.SKILL_DIR):
        assert filecmp.cmp(v.SKILL_DIR / rel, pkg / rel, shallow=False), f"out of sync: {rel}"


def test_directory_contains_only_allowed_files(v):
    base = v.ROOT / "claude-directory"
    top = {p.relative_to(base).parts[0] for p in base.rglob("*") if p.is_file()}
    assert top == {".claude-plugin", "skills", "LICENSE", "THIRD_PARTY_NOTICES.md", "README.md"}
    assert sorted(p.name for p in (base / ".claude-plugin").iterdir()) == ["icon.png", "plugin.json"]
    for p in base.rglob("*"):
        if p.is_file():
            assert p.suffix in {".md", ".json", ".png", ""}, p
            assert not (p.stat().st_mode & 0o111), f"executable bit: {p}"


def test_directory_manifest_and_icon(v):
    base = v.ROOT / "claude-directory" / ".claude-plugin"
    assert json.loads((base / "plugin.json").read_text()) == json.loads((v.ROOT / ".claude-plugin" / "plugin.json").read_text())
    data = (base / "icon.png").read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) < 2 * 1024 * 1024
    assert int.from_bytes(data[16:20], "big") == 1024 and int.from_bytes(data[20:24], "big") == 1024


def test_directory_has_no_outside_references(v):
    base = v.ROOT / "claude-directory"
    for p in base.rglob("*"):
        if p.suffix in {".md", ".json"}:
            t = p.read_text(encoding="utf-8")
            assert '"$schema"' not in t and "../" not in t, p
            for m in re.finditer(r"(?<![/\w])(research|scripts|tests|docs|schemas)/", t):
                line = t[max(0, t.rfind("\n", 0, m.start())):m.end() + 40]
                assert "github.com" in line, f"{p}: {line.strip()}"
