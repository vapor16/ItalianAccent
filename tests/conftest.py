import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("ia_validate", ROOT / "scripts" / "validate.py")
validate = importlib.util.module_from_spec(_spec)
sys.modules["ia_validate"] = validate
_spec.loader.exec_module(validate)


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def v():
    return validate


@pytest.fixture(scope="session")
def catalog():
    return load(validate.REFS / "catalog.json")


@pytest.fixture(scope="session")
def available_modes(catalog):
    return [m for m in catalog["modes"] if m["available"]]


@pytest.fixture(scope="session")
def profile_dirs():
    return sorted(d for d in validate.DIALECTS.iterdir() if d.is_dir()) if validate.DIALECTS.exists() else []
