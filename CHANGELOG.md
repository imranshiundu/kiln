# Changelog

All notable changes to KILN are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the
project versions with the repository.

## [0.2.0] — The Second Firing — 2026-11-20

Deepens the phases real projects burn most: data, interfaces, and the
running system. Four new crafts, the Fire Test made mechanical, and
CI to hold the bar.

### Added

- **`observe-the-system`** (ship) — the three signals (structured
  logs, metrics, traces) chosen *with* the first feature, questions
  first, boundaries instrumented, alerts wired to answers, verified
  by a black-box drill. Craft sources: the Google SRE book's
  monitoring discipline, Sridharan's observability writing,
  OpenTelemetry's signal model.
- **`measure-then-optimize`** (verify) — no performance claim without
  a number: profile the real workload before touching anything, one
  change per measured delta, variance reported, noise-level results
  reverted. Craft sources: Knuth (1974) on premature optimization;
  Gregg's systems-performance discipline.
- **`test-the-contract`** (verify) — every published boundary pinned
  by a test that fails in the producer's CI when the promise breaks,
  including the deliberate-break drill. Craft sources: Robinson's
  consumer-driven contracts, Fowler's canonical sketch, Pact's
  machinery, Hyrum's Law.
- **`migrate-gently`** (tend) — expand, migrate, contract: reversible
  steps for changing persistent data and interfaces, idempotent
  batched backfills with count checks, old shape dropped only on
  evidence of zero usage. Craft sources: Sato's expand-migrate-
  contract, Fowler's Parallel Change.
- **`scripts/firetest.py`** — the Fire Test, made mechanical:
  frontmatter contract, five-section anatomy, word budget, and
  cross-reference integrity across README, AGENTS.md, and the
  lifecycle map. Stdlib-only Python, exits non-zero on any failure.
- **CI** (`.github/workflows/ci.yml`) — the Fire Test runs on every
  push and PR, on Linux, macOS, and Windows. A skill that breaks the
  format contract can no longer reach `main` silently.
- **`docs/install-matrix.md`** — per-agent install commands with
  honest status labels: what is verified, what is documented only.
- This changelog.

### Fixed

- `fire-a-skill` and `refactor-with-care` carried extra body sections
  ("Before writing", "When *not* to fire") outside the five-section
  contract — both folded back into the standard anatomy with no
  content lost. The Fire Test caught it; that is what it is for.
- The lifecycle map never referenced the meta-skill; the map now has
  an explicit "eighth skill — meta" section.
- `.claude-plugin` manifests updated to 0.2.0 and the current skill
  count (19).

## [0.1.0] — The First Firing — 2026-10-17

The library exists and can be used by anyone, anywhere.

### Added

- 15 skills covering all seven lifecycle phases (plus the meta-skill).
- The format spec and Fire Test quality bar (`docs/format.md`).
- The lifecycle map (`docs/lifecycle.md`).
- Agent doctrine (`AGENTS.md`).
- Installs via `npx skills add imranshiundu/kiln` (75+ agents).
- Installs as a Claude Code plugin marketplace.
- Research survey with all prior art credited (`docs/research.md`).
