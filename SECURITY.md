# Security Policy

ItalianAccent is a set of Markdown and JSON files. It runs no code at runtime, makes no network requests, collects
no telemetry and needs no credentials. Development scripts (`scripts/validate.py`) run only locally or in CI.

## Supported versions

| Version | Supported |
|---|---|
| 1.0.x | ✅ |
| < 1.0 | ❌ |

## Reporting

Please report vulnerabilities privately via
[GitHub security advisories](https://github.com/vapor16/ItalianAccent/security/advisories/new). Relevant issues
include: prompt-injection content in profile files, instructions that try to bypass a host's safety systems,
embedded secrets or personal data, malicious content in contributions.

ItalianAccent must never contain instructions to bypass or disable model safety. "Uncensored" refers only to the
spelling and style of otherwise permitted profanity; it never overrides refusals, safety warnings or
higher-priority instructions, and the skill never produces erotic content or harassment.
