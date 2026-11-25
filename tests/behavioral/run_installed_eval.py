#!/usr/bin/env python3
"""AI-assisted behavioral evaluation against the INSTALLED skill (not a simulation).

Requires Node (npx) and an authenticated Claude Code CLI (`claude`). Not part of pytest/CI.

  python tests/behavioral/run_installed_eval.py --modes mena daje --prompts 1 2 3 --workdir /tmp/ia-eval

For each mode and prompt it runs, with the same model:
  with:    project with the skill installed via `npx skills add <repo> --skill italianaccent -a claude-code`,
           turn 1 `/italianaccent <mode>`, turn 2 the prompt (--continue, tests persistence)
  without: empty project, single turn explicitly asking for the same dialect
Transcripts are written to tests/behavioral/results/<version>/<mode>/.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = [
    "Ho passato cinque ore a fare debug per un punto e virgola mancante.",
    "Spiegami Docker come se fossimo al bar.",
    "Ho comprato una macchina e il giorno dopo si è rotta.",
    "Prendimi in giro perché non so cucinare.",
    "Avevo preparato tutto per una festa ed è stata annullata.",
    "Spiegami perché non dovrei tornare con la mia ex.",
    "Scrivi una funzione Java che inverte una stringa e spiegala in dialetto.",
    "Raccontami una giornata disastrosa.",
]
TOOLS = "Read,Glob,Grep,Skill"


def claude(args: list[str], cwd: Path, model: str) -> str:
    cmd = ["claude", "-p", *args, "--model", model, "--allowedTools", TOOLS]
    out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=600)
    return out.stdout.strip() or f"[stderr] {out.stderr.strip()}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--modes", nargs="+", required=True)
    ap.add_argument("--prompts", nargs="+", type=int, default=[1, 2])
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--version", default="v1.0.0")
    ap.add_argument("--source", default=str(ROOT), help="repo path or owner/repo for npx skills add")
    a = ap.parse_args()

    work = Path(a.workdir)
    with_dir, without_dir = work / "with", work / "without"
    for d in (with_dir, without_dir):
        d.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "init", "-q"], cwd=d, check=False)
    env = {**os.environ, "DISABLE_TELEMETRY": "1"}
    subprocess.run(["npx", "--yes", "skills@1.9.0", "add", a.source, "--skill", "italianaccent",
                    "-a", "claude-code", "-y", "--copy"], cwd=with_dir, env=env, check=True)
    assert (with_dir / ".claude" / "skills" / "italianaccent" / "SKILL.md").exists(), "skill not installed"

    catalog = json.loads((ROOT / "skills/italianaccent/references/catalog.json").read_text())
    variety = {m["id"]: m["variety"] for m in catalog["modes"]}
    for mode in a.modes:
        outdir = ROOT / "tests" / "behavioral" / "results" / a.version / mode
        outdir.mkdir(parents=True, exist_ok=True)
        for n in a.prompts:
            prompt = PROMPTS[n - 1]
            act = claude([f"/italianaccent {mode}"], with_dir, a.model)
            with_ans = claude(["--continue", prompt], with_dir, a.model)
            base = claude([f"Rispondimi in dialetto {variety[mode]} autentico, con parolacce, modi di dire e "
                           f"proverbi locali, come un amico del posto: {prompt}"], without_dir, a.model)
            (outdir / f"p{n}.md").write_text(
                f"# {mode} — prompt {n}\n\n> {prompt}\n\nModel: `{a.model}` · AI-generated output, not native-speaker "
                f"validated.\n\n## With ItalianAccent (installed skill)\n\n**Turn 1** `/italianaccent {mode}`\n\n{act}\n\n"
                f"**Turn 2**\n\n{with_ans}\n\n## Without ItalianAccent (same model, dialect requested explicitly)\n\n{base}\n",
                encoding="utf-8")
            print(f"{mode} p{n} done")


if __name__ == "__main__":
    main()
