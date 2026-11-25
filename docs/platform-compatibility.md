# Platform compatibility

Status legend: **Documented** = the platform's official docs describe this mechanism · **Structurally compatible**
= the package follows the format the platform documents · **Locally tested** = installed/validated in this
project's environment · **Behaviorally tested** = the skill was exercised by a model on that platform ·
**Not yet tested** · **Unsupported**.

| Platform | Install method | Status (v0.1.0) | Invocation | Persistence |
|---|---|---|---|---|
| Claude Code (skill) | `npx skills add vapor16/ItalianAccent --skill italianaccent -a claude-code`, or copy `skills/italianaccent` to `~/.claude/skills/` | Documented · Structurally compatible · Locally tested (skills CLI discovery) · Behaviorally tested (AI-assisted, see tests/behavioral/results) | `/italianaccent <args>` or natural language | Within a conversation; re-activate in new sessions; re-read after compaction |
| Claude Code (plugin) | `/plugin marketplace add vapor16/ItalianAccent` then `/plugin install italianaccent@italianaccent` | Documented · Structurally compatible · Locally tested (`claude plugin validate .` passed) | `/italianaccent:italianaccent <args>` | Same |
| Claude.ai (web/desktop/mobile) | Upload `italianaccent-0.1.0.zip` from the GitHub release in Customize → Skills (requires code execution enabled) | Documented · Structurally compatible (portable frontmatter only) · Not yet tested | Natural language ("Activate ItalianAccent in Daje mode") | Within a conversation |
| Codex (OpenAI) | `npx skills add vapor16/ItalianAccent --skill italianaccent -a codex` | Documented by the skills CLI · Structurally compatible · Not yet tested | Natural language or host skill invocation | Host-dependent |
| Cursor | `npx skills add vapor16/ItalianAccent --skill italianaccent -a cursor` | Documented by the skills CLI · Structurally compatible · Not yet tested | Natural language or host skill invocation | Host-dependent |
| Other Agent Skills hosts | Copy the `skills/italianaccent` folder into the host's skills directory | Structurally compatible · Not yet tested | Host-dependent | Host-dependent |

Requirements: the host must be able to read files inside the skill folder (progressive disclosure). No network,
scripts or extra MCP servers are needed.

Notes:
- The skills CLI collects anonymous install telemetry (opt out with `DISABLE_TELEMETRY=1`); ItalianAccent itself has
  no telemetry.
- Appearing on the skills.sh leaderboard depends on that directory's indexing; installability from GitHub does not
  imply a listing.
