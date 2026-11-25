import yaml

REQUIRED_BEHAVIORS = {"activation", "deactivation", "mode-switching", "session-persistence", "dialect-intensity",
                      "profanity-intensity", "proverbs", "idioms", "humor", "sarcasm", "translation",
                      "technical-accuracy", "code-integrity", "formal-writing", "unknown-mode", "repetition-avoidance"}


def _cases(v):
    return yaml.safe_load((v.ROOT / "tests" / "behavioral" / "eval-cases.yaml").read_text(encoding="utf-8"))


def test_eval_cases_cover_all_behaviors(v):
    data = _cases(v)
    assert REQUIRED_BEHAVIORS <= {c["behavior"] for c in data["cases"]}


def test_eval_cases_well_formed(v):
    data = _cases(v)
    ids = set()
    for c in data["cases"]:
        assert c["id"] not in ids
        ids.add(c["id"])
        assert c["turns"] and all(isinstance(t, str) for t in c["turns"])
        assert c["expectations"]


def test_rubric(v):
    data = _cases(v)
    assert set(data["rubric"]["criteria"]) == {"authenticity", "naturalness", "vocabulary", "grammar", "syntax",
                                               "regional_consistency", "contextual_profanity", "proverb_relevance",
                                               "humor", "technical_accuracy"}
    assert data["rubric"]["scale"] == [1, 5]
