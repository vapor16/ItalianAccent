import re

SKIP_DIRS = {".git", "node_modules", "dist", "__pycache__", ".pytest_cache"}
TEXT_EXT = {".md", ".json", ".py", ".yml", ".yaml", ".toml", ".txt", ""}
SECRET_PATTERNS = [
    r"ghp_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{30,}", r"sk-[A-Za-z0-9]{20,}", r"sk-ant-[A-Za-z0-9-]{20,}",
    r"AKIA[0-9A-Z]{16}", r"xox[baprs]-[A-Za-z0-9-]{10,}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"AIza[0-9A-Za-z_-]{35}",
]
ABS_PATHS = [r"/home/[a-z]", r"/root/", r"/Users/[A-Za-z]", r"C:\\\\Users\\\\", r"/tmp/claude"]
EMAIL = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}"
ALLOWED_EMAILS = {"noreply@anthropic.com"}


def _files(v):
    for p in v.ROOT.rglob("*"):
        if p.is_file() and not (set(p.relative_to(v.ROOT).parts) & SKIP_DIRS) and p.suffix in TEXT_EXT:
            if p.name in {"test_security.py"}:
                continue
            yield p


def test_no_secrets(v):
    for p in _files(v):
        t = p.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            assert not re.search(pat, t), f"possible secret in {p}"


def test_no_absolute_local_paths(v):
    for p in _files(v):
        if p.name == "IMPLEMENTATION_PLAN.md":
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        for pat in ABS_PATHS:
            assert not re.search(pat, t), f"absolute local path in {p}: {pat}"


def test_no_personal_emails(v):
    for p in _files(v):
        t = p.read_text(encoding="utf-8", errors="ignore")
        for m in re.findall(EMAIL, t):
            assert m in ALLOWED_EMAILS or m.endswith("@example.com") or m.endswith("@users.noreply.github.com"), f"email {m} in {p}"


def test_no_personal_config_files(v):
    bad = {".env", "credentials.json", "settings.local.json", ".npmrc", ".pypirc", "id_rsa"}
    for p in v.ROOT.rglob("*"):
        if ".git" in p.parts:
            continue
        assert p.name not in bad, p


def test_skill_has_no_runtime_network_or_exec(v):
    # runtime instruction files only; example conversations may legitimately show shell commands
    for p in [v.SKILL_DIR / "SKILL.md", *v.REFS.glob("*.md")]:
        t = p.read_text(encoding="utf-8").lower()
        for bad in ["curl ", "wget ", "fetch(", "pip install", "npm install", "invoke-webrequest"]:
            assert bad not in t, f"{p} contains runtime instruction {bad!r}"


def test_no_jailbreak_language(v):
    for p in v.SKILL_DIR.rglob("*.md"):
        t = p.read_text(encoding="utf-8").lower()
        for bad in ["ignore previous instructions", "ignore your safety", "jailbreak", "disable safety", "dan mode"]:
            assert bad not in t, f"{p}: {bad}"
