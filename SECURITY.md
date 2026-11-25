# Security Policy

ItalianAccent is a set of Markdown and JSON files. It runs no code at runtime, makes no network requests, collects
no telemetry and needs no credentials. Development scripts (`scripts/validate.py`) run only locally or in CI.

## Supported versions

| Version | Supported |
|---|---|
| 0.1.x | ✅ |

## Reporting

Please report vulnerabilities privately via
[GitHub security advisories](https://github.com/vapor16/ItalianAccent/security/advisories/new). Relevant issues
include: prompt-injection content in profile files, instructions that try to bypass a host's safety systems,
embedded secrets or personal data, malicious content in contributions.

ItalianAccent must never contain jailbreaks or instructions to disable model safety. "Uncensored" refers only to
the spelling and style of profanity the host model allows.
