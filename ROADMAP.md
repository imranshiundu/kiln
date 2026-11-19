# KILN Roadmap — the Direction

KILN is built in firings — releases named like the process they describe.

## v0.1 — The First Firing (now)

The library exists and can be used by anyone, anywhere.

- [x] 15 skills covering all seven lifecycle phases (plus the meta-skill)
- [x] The format spec and Fire Test quality bar ([docs/format.md](docs/format.md))
- [x] The lifecycle map ([docs/lifecycle.md](docs/lifecycle.md))
- [x] Agent doctrine ([AGENTS.md](AGENTS.md))
- [x] Installs via `npx skills add imranshiundu/kiln` (75+ agents)
- [x] Installs as a Claude Code plugin marketplace
- [x] Research survey with all prior art credited ([docs/research.md](docs/research.md))

## v0.2 — The Second Firing (shipped 2026-11-20)

Deepen the phases that real projects burn most: data, interfaces, and the
running system.

- [x] `observe-the-system` (ship) — logging, metrics, and tracing chosen
      *with* the first feature, not after the first incident
- [x] `measure-then-optimize` (verify) — profile before optimizing;
      no performance claim without a number
- [x] `test-the-contract` (verify) — contract tests at the boundaries
      the interface design promised
- [x] `migrate-gently` (tend) — data migrations that never lose data,
      one reversible step at a time
- [x] The Fire Test runs mechanically in CI on every push and PR
      (`scripts/firetest.py`), pulled forward from v1.0 because four new
      skills needed the bar enforced, not remembered
- [x] A tested install matrix: the skills CLI live-run is recorded
      (Claude Code and Codex targets verified; OpenCode and Cursor
      documented, pending a machine with those agents) —
      [docs/install-matrix.md](docs/install-matrix.md)
- [x] A `npx skills` listing page and skills.sh submission —
      resolved by finding in 0.3: no submission exists; listings
      fill from install telemetry

## v0.3 — The Third Firing (shipped 2026-11-20)

Every phase deepened; the library opens up.

- [x] `read-the-codebase` (gather) — the traced request as the unit
      of understanding, and a written brief with assumptions labeled
- [x] `estimate-with-ranges` (spec) — honest numbers: ranges,
      confidence, assumptions, re-estimates
- [x] `commit-with-care` (build) — the commit as a work artifact
- [x] `make-it-accessible` (build) — semantics first, keyboard
      complete, measured contrast, both kinds of testing
- [x] `test-the-edges` (verify) — boundary tables and properties
      that shrink their failures
- [x] `tend-the-dependencies` (tend) — current by evidence, not by
      badge
- [x] The checker holds itself: a test suite that breaks a
      miniature library fourteen ways (`tests/run.sh`), a golden
      inventory snapshot, `--list/--json/--strict/--root`, and new
      routing checks — which caught a real trigger collision on
      their first run
- [x] Live-verified installs (skills CLI v1.9.0, two agent
      targets) with outputs recorded in
      [docs/install-matrix.md](docs/install-matrix.md)
- [x] The skills.sh item, resolved by finding: there is no
      submission process — listings fill from real install
      telemetry, so the listing arrives with the users

## v1.0 — The Mature Kiln (later)

Trustworthy because measured, not merely written.

- [ ] One eval scenario per skill: a scripted session that demonstrates
      the craft firing correctly — and a failing baseline without the
      skill
- [x] A contribution pipeline with the Fire Test as an actual checklist
      in CI (frontmatter validation, word budget, section anatomy) —
      shipped early, in v0.2
- [ ] Real adoption notes: which skills fire most, which get ignored,
      and what that teaches the map
- [ ] Translations of the doctrine (AGENTS.md) for non-English-first teams

## Non-goals — what KILN will never be

- **Not a methodology.** KILN won't tell you *how* to run your team or
  which process to enforce. It teaches crafts; you compose them. (For an
  enforced methodology, see superpowers — with respect.)
- **Not a catalog.** No 1000-skill awesome list. If a craft doesn't pass
  the Fire Test, it isn't here; if it isn't load-bearing for building a
  whole thing, it doesn't belong at all.
- **Not stack-specific.** No React skill, no Rails skill, no vendor
  skills. Stack knowledge lives in stack-specific libraries where it can
  be deep; KILN's skills work beside them, not instead of them.
- **Not a prompt dump.** No "write better emails" skills. The lifecycle
  is software because that's the honest boundary of this library's
  research; widening it requires redoing the survey, not just appending
  folders.

## Naming the direction in one line

**KILN grows by firing one skill at a time — each one earning its place
in the map, tested live in real agents, or it doesn't ship.**
