---
name: tend-the-dependencies
description: Keeps dependencies current without chaos - changelogs read before bumping, risk tiered by semver distance, one batch per commit, majors planned alone. Use when updates are pending, a lockfile drifts, or a major bump is being pushed through in a hurry.
license: MIT
metadata:
  phase: tend
---

# Tend the Dependencies

## North Star

The project rides current, known ground: every direct dependency a
conscious choice, each bump verified against the project's own bar,
majors migrated deliberately with their guides — never as a
surprise inside someone's Friday PR. "Up to date" is a state of
evidence, not a date on a badge.

## When to fire

- Updates are pending — patch, minor, major, or security.
- A lockfile is drifting, or someone proposes regenerating it
  wholesale.
- A major version bump is being pushed "real quick".
- A new dependency is about to be added — adoption is the heaviest
  bump of all.

## Workflow

1. **Inventory and tier.** List direct dependencies and their
   available updates; tier by semver distance — patches (bug
   fixes), minors (features, meant to be compatible), majors
   (breaking). The tier is the risk; the batch size follows it.
2. **Read the release notes before bumping.** A version number is
   a claim; the changelog is the evidence. What changed, what
   breaks, what is deprecated. An unread bump is a coin flip with
   extra steps.
3. **Bump in small batches.** Patches together; minors together,
   watched; one major at a time, never mixed with anything else.
   One batch, one commit, one verification run.
4. **Run the project's own verification after every batch** — the
   tests, build, and checks the repo already trusts. Green is the
   only evidence a bump is safe; "it's only a patch" is not.
5. **Commit the lockfile.** The indirect graph is part of the
   build. Reproducibility is cheaper than any debugging session a
   drifting graph will eventually cause.
6. **Plan majors like projects, not chores.** Read the migration
   guide, carve out time, expect behavior changes, keep the
   rollback path intact until the new major has survived real use.
   Security bumps jump every queue — the exception that outranks
   the calendar.

Craft sources: the SemVer specification (Preston-Werner) — a
contract worth holding libraries to; the automation discipline of
Renovate and Dependabot, which this skill runs by hand where the
project doesn't run them by machine.

## Red flags

- "Update all" in one commit, majors included.
- Floating ranges in a published library's own manifest.
- A lockfile regenerated to make conflicts disappear.
- A major upgrade snuck into a dependency-refresh PR.
- Security advisories parked behind feature bumps.

## Exit criteria

- Release notes read for every bumped package — noted in the
  commit or PR, not implied.
- Each batch verified green by the project's own checks.
- Majors migrated on their own branches, migration guide linked.
- Lockfile committed and reviewed like code.
