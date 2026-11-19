# Security Policy

## What this repository is

KILN is a library of Markdown skill files plus two Python scripts
(`scripts/firetest.py`, `tests/build_fixtures.py`) and a test runner.
Nothing here executes on install: a skill is text an agent reads,
not code an agent runs. The scripts run only when a contributor
invokes them from a checkout.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting on this repository
(Report a vulnerability, under the Security tab). That reaches the
maintainer directly and lets us coordinate a fix and disclosure.

Please include what you found, reproduction steps, and impact. If
you are unsure whether something is a vulnerability, report it
anyway - triage is our job, not yours.

## Scope

In scope:

- Anything in this repository that runs: the Fire Test and the
  fixture builder (path handling, fixture mutations, CI wiring).
- The skill files' content, if a flaw could mislead an agent into
  destructive behavior (a workflow step that, followed literally,
  damages a user's project).

Out of scope:

- How agents interpret or execute skill text in their own runtime -
  that is the agent's security model, not the library's.
- Vulnerabilities in tools the skills *describe* using (git, test
  runners, profilers); the skill text points at them, it does not
  ship them.

## Preferred languages

English.
