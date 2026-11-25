# Research log

Dates are access dates. Per-profile logs: `research/raw/<id>-log.md`.

## 2026-11-25 — Platform and specification research (M1)

Read (via web fetch):
- https://agentskills.io/specification — frontmatter fields (`name` ≤64 chars `[a-z0-9-]`, must match folder; `description` 1–1024; optional `license`, `compatibility` ≤500, `metadata` string map, `allowed-tools`), SKILL.md under 500 lines, references one level deep.
- https://code.claude.com/docs/en/skills — Claude Code extensions (`disable-model-invocation`, `argument-hint`, `$ARGUMENTS`…), skill locations, plugin namespacing `/plugin:skill`. Summary indicated that only the portable keys are accepted outside Claude Code → portable keys only.
- https://code.claude.com/docs/en/plugins, /plugin-marketplaces, /plugins/manifest-reference, /plugins/marketplace-reference — plugin.json (`name` required), marketplace.json (`name`, `owner.name`, `plugins[]` with `name` + `source`), install commands.
- https://github.com/vercel-labs/skills (README, docs/commands.md, docs/creating-skills.md) — `npx skills add <owner/repo>` with `-s/--skill`, `-l/--list`, `-g`, `-a`, `-y`, `--copy`; discovery in `skills/` (up to 3 levels) and plugin manifests; anonymous telemetry, opt-out `DISABLE_TELEMETRY=1`.
- https://skills.sh — public directory/leaderboard ranked by install counts.
- https://github.com/anthropics/skills — reference layout and marketplace.json.
- https://support.claude.com/en/articles/12512180-using-skills-in-claude — ZIP upload of the skill folder.

`claude plugin validate .` run locally: passed.
