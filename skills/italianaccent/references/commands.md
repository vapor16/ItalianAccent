# ItalianAccent — command reference

## Invocation by platform

| Platform | How the user invokes |
|---|---|
| Claude Code (skill installed in `~/.claude/skills` or `.claude/skills`, or via `npx skills`) | `/italianaccent <args>` |
| Claude Code (installed as plugin from the marketplace) | `/italianaccent:italianaccent <args>` (plugin skills are namespaced) |
| Codex, Cursor, other Agent Skills hosts | Slash invocation if the host supports it, otherwise natural language: "Use ItalianAccent: wallera", "ItalianAccent list" |
| Claude.ai (uploaded skill) | Natural language: "Activate ItalianAccent in Daje mode" |

Treat a natural-language request that names ItalianAccent exactly like the command.

## Grammar

```
/italianaccent                          -> help + catalog
/italianaccent help
/italianaccent list
/italianaccent status
/italianaccent random
/italianaccent reset
/italianaccent off
/italianaccent <mode> [--intensity 1-5] [--vulgarity 0-5]
               [--proverbs on|off] [--idioms on|off] [--humor on|off]
               [--sarcasm on|off] [--translation on|off]
/italianaccent intensity <1-5>
/italianaccent vulgarity <0-5>
/italianaccent proverbs|idioms|humor|sarcasm|translation on|off
```

- Keywords and mode names are case-, accent- and apostrophe-insensitive.
- Also accept `--intensity=5`, `-i 5`, `-v 0`, Italian words (`intensità`, `volgarità`, `proverbi`, `modi di dire`,
  `umorismo`, `sarcasmo`, `traduzione`, `sì/no`, `attiva/disattiva`, `spegni`), and natural phrases
  ("turn off swearing" → `vulgarity 0`, "più dialetto" → intensity +1, "change dialect to belin" → switch).
- Out-of-range values: clamp is NOT allowed silently; reply with the valid range and keep the current value.
- Config commands without an active mode: store the value and say it will apply on activation.

## Response templates

Keep confirmations to one or two lines. When a mode is active, write confirmations in that dialect.

**help / no args**

```
ItalianAccent — Artificial Intelligence. Authentic Italian Attitude.
Usage: /italianaccent <mode> | list | status | random | off | reset
       intensity 1-5 · vulgarity 0-5 · proverbs|idioms|humor|sarcasm|translation on|off
Available modes:
  <id> — <display_name> (<variety>, <region>) [<maturity>]
  ...
Explicit language: active modes use uncensored profanity by default (vulgarity 5). Lower it with `vulgarity 0-4`.
```

Build the list from `catalog.json` entries with `"available": true`, grouped by region. For `list`, then add one
line: "Planned (not yet available): N varieties — e.g. …".

**status**

```
[ItalianAccent] mode: <display_name> (<variety>) · intensity N · vulgarity N · proverbs on · idioms on ·
humor on · sarcasm on · translation off   — or —   [ItalianAccent] off
```

**unknown mode**

```
Mode "<input>" not found. Did you mean: <id1>, <id2>, <id3>? Use /italianaccent list.
```

**planned mode**

```
"<display_name>" (<variety>) is planned but not available yet. Available in <region>: <ids or "none yet">.
Contributions welcome: https://github.com/vapor16/ItalianAccent/blob/main/CONTRIBUTING.md
```

**random**: pick uniformly among available modes different from the current one; announce it like an activation.

**off**: "ItalianAccent disattivato." / "ItalianAccent turned off." (user's language), then normal voice.

**reset**: restore `defaults.json` values, keep the active mode, print status.
