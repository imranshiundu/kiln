# Changelog

All notable changes to KILN are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the
project versions with the repository.

## [0.3.0] — The Third Firing — 2026-11-20

Every phase deepened: six new crafts, accessibility both as a
skill and in the library itself, the checker made self-testing,
and the install path live-verified. 25 skills across the seven
fires plus meta.

### Added — six new crafts

- **`read-the-codebase`** (gather) — deliberate exploration of
  unfamiliar terrain: the repo's own story first, entry points,
  one real request traced end to end, the seams mapped, tests read
  as intent, and a written brief with every assumption labeled.
  *(Spinellis' Code Reading; Hermans' The Programmer's Brain.)*
- **`estimate-with-ranges`** (spec) — honest numbers for planning:
  decompose until comparable, anchor on history, ranges with
  explicit confidence, assumptions named, re-estimates as the cone
  narrows. *(Boehm's cone of uncertainty, via McConnell.)*
- **`commit-with-care`** (build) — the commit as a work artifact:
  one logical change per commit, every commit green, the message
  carries the why. *(Tim Pope's commit-message note; git bisect.)*
- **`make-it-accessible`** (build) — interfaces everyone can use:
  semantics first, keyboard-complete journeys, named controls,
  measured contrast, state announced, and both automated and human
  testing before done. *(WCAG 2.2; Pickering's Inclusive
  Components; Deque's axe.)*
- **`test-the-edges`** (verify) — the boundaries happy paths miss:
  boundary tables with the oracle decided first, invariants as
  properties, failures shrunk to the smallest case, rejections
  tested with their errors. *(Myers; QuickCheck, Claessen and
  Hughes 2000; the Hypothesis lineage.)*
- **`tend-the-dependencies`** (tend) — current by evidence, not by
  badge: changelogs read before bumping, tiered by semver
  distance, one batch per verification run, lockfile committed,
  majors planned, security bumps jumping every queue. *(SemVer;
  the Renovate and Dependabot discipline.)*

### Added — the bar holds itself

- **The checker's own test suite** (`tests/run.sh`): a miniature
  seven-skill library broken fourteen different ways, each break
  asserted caught with the right complaint — plus the golden
  inventory snapshot, so metadata drift is a diff to review, not a
  surprise. A checker that cannot fail is a rubber stamp.
- **`firetest.py --list / --json / --strict / --root`** — the
  inventory for humans and machines, the no-warnings bar for
  pre-push, and the same Fire Test available to any skills library.
- **New mechanical checks**: duplicate trigger openings (two doors
  on one hinge), empty phases, H1 titles that drift from their
  names. The duplicate-trigger check caught a real collision
  (`commit-with-care` vs `review-the-work`) within minutes of
  landing.
- **CI grows**: Python 3.9–3.13 portability matrix, a changelog
  gate (the shipped version must have an entry), manual dispatch,
  and a release workflow that publishes GitHub releases from tags
  with the CHANGELOG section as notes — gated on tag/version match.

### Added — the library opens up

- **Live-verified installs**: the skills CLI (v1.9.0) ran a real
  install of this repository — all 25 skills discovered and copied
  intact to the Claude Code and Codex/shared targets, with the
  shared lockfile recording per-skill hashes. Recorded with
  outputs in [`docs/install-matrix.md`](docs/install-matrix.md).
- **The skills.sh finding**: there is no submission process —
  listings fill from real install telemetry. The door we went
  looking for doesn't exist; the library walks in through use.
- **Issue and PR templates** shaped like the Fire Test; the
  propose-a-craft form is the bar in question form.
- **`docs/glossary.md`** — the vocabulary pinned (fire, craft,
  trigger, gate, receipt, the bar); **SECURITY.md** scoped to what
  a Markdown library actually is; CODEOWNERS; Dependabot on the CI
  actions; a Makefile front door (`make check`).
- **Docs deepened**: description-writing guide with three rewrites
  (fails → better → passes); the Fire Test's mechanical mapping;
  the common loops (bug, drift, migration); a worked example of one
  bug report walking all seven fires; every research credit linked
  to its source; a README contents list and FAQ.

### Changed — accessibility, in the library itself

- The mark (`assets/kiln.svg`) carries a `<title>` and `<desc>`
  wired with `aria-labelledby`.
- Badges pass contrast: the amber `f59e0b` (2.15:1 with white
  text) became the family's dark amber `92610a` (5.33:1), and the
  agents badge links to the list it cites. The CI badge is now the
  live workflow status, not a static picture.

### Fixed — every word intentional

- The three over-budget bodies (`cut-thin-slices` 507, `fire-a-skill`
  509, `review-the-work` 515) tightened back under ~500 with no
  content lost — the budget is enforced by the checker and kept by
  hand.
- `fire-a-skill` and `refactor-with-care` now hold the five-section
  contract exactly (folded in 0.2.0, verified here against the new
  checker).

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
