<p align="center">
  <img src="assets/kiln.svg" width="110" alt="The KILN mark" />
</p>

<h1 align="center">KILN</h1>

<p align="center">
  <strong>Raw ideas in. Finished software out.</strong><br>
  A research-backed open library of agent skills for building complete software —<br>
  from the first question to the shipped release.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-8a5a2b.svg"></a>
  <a href="https://agentskills.io"><img alt="Follows the Agent Skills standard" src="https://img.shields.io/badge/follows-Agent%20Skills-92610a.svg"></a>
  <a href="https://github.com/vercel-labs/skills#supported-agents"><img alt="Works with 75+ agents" src="https://img.shields.io/badge/works%20with-75%2B%20agents-6b5a3e.svg"></a>
  <a href="https://github.com/imranshiundu/kiln/actions/workflows/ci.yml"><img alt="CI status: the Fire Test" src="https://github.com/imranshiundu/kiln/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/imranshiundu/kiln/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/imranshiundu/kiln?color=92610a"></a>
</p>

---

A kiln turns soft clay into enduring craft. **KILN turns a capable agent into a complete builder.**

Agents write code fast. What they skip — unless taught — are the crafts that make software last: interrogating the request before building, reading an unfamiliar codebase before editing it, writing the spec, modeling the data, testing first, committing with care, hunting root causes instead of symptoms, testing the edges and the contracts, making interfaces everyone can use, observing the running system, releasing deliberately, migrating gently, documenting the why. KILN is those crafts, written down as agent skills: **one craft per skill, each a workflow with gates and evidence requirements, not an essay.**

This is not a pile of prompts. It is a *lifecycle* — a researched map of what it takes to build a whole thing, with a skill waiting at every phase.

## Contents

- [The seven fires](#the-seven-fires) — the lifecycle in one breath
- [The skills](#the-skills) — 25 crafts, by phase
- [Install](#install) — any agent, two commands
- [For agents](#for-agents) — the doctrine
- [FAQ](#faq) — the questions everyone asks
- [Roots and direction](#roots-and-direction) — format, lifecycle, research, roadmap
- [Principles](#principles) — six lines
- [Prior art](#prior-art) — the shoulders KILN stands on
- [Contribute](#contribute) — fire a skill into the library

## The seven fires

Everything that gets built — an app, a service, a library, a side project — passes through the same fires:

```
 GATHER ──▶ SPEC ──▶ DESIGN ──▶ BUILD ──▶ VERIFY ──▶ SHIP ──▶ TEND
 (clay)   (wedge)   (shape)    (fire)   (sound)   (open)   (keep)
```

Real work loops through these out of order and that is fine — the map is a compass, not a rail. What KILN refuses to do is skip a fire silently.

## The skills

27 skills, every phase deepened where real projects burn. Each fits in your agent's context with room to spare, and fires only when relevant.

| Phase | Skill | Fires when |
| :- | :- | :- |
| **gather** | [`question-first`](skills/question-first/SKILL.md) | a request arrives without acceptance criteria |
| **gather** | [`ground-truth`](skills/ground-truth/SKILL.md) | building on code, APIs, or claims that need verifying |
| **gather** | [`read-the-codebase`](skills/read-the-codebase/SKILL.md) | work starts in a repository nobody has actually read |
| **spec** | [`write-the-spec`](skills/write-the-spec/SKILL.md) | an agreed idea must become a one-page build contract |
| **spec** | [`decide-with-records`](skills/decide-with-records/SKILL.md) | a cross-cutting choice gets made once and recorded |
| **spec** | [`estimate-with-ranges`](skills/estimate-with-ranges/SKILL.md) | anyone asks how long, how much, or whether it fits |
| **design** | [`model-the-data`](skills/model-the-data/SKILL.md) | persistent state, entities, or invariants take shape |
| **design** | [`design-the-interface`](skills/design-the-interface/SKILL.md) | an API, module boundary, or public surface is born |
| **build** | [`cut-thin-slices`](skills/cut-thin-slices/SKILL.md) | implementation starts on anything bigger than a one-liner |
| **build** | [`test-first`](skills/test-first/SKILL.md) | writing logic that must not break |
| **build** | [`commit-with-care`](skills/commit-with-care/SKILL.md) | committing work, or a branch has become one blob |
| **build** | [`make-it-accessible`](skills/make-it-accessible/SKILL.md) | anything a human will see, hear, or click is being built |
| **verify** | [`hunt-the-bug`](skills/hunt-the-bug/SKILL.md) | behavior is wrong and the cause is unknown |
| **verify** | [`review-the-work`](skills/review-the-work/SKILL.md) | work is about to be presented as done |
| **verify** | [`measure-then-optimize`](skills/measure-then-optimize/SKILL.md) | something is slow and a fix is proposed without numbers |
| **verify** | [`test-the-contract`](skills/test-the-contract/SKILL.md) | a published boundary is about to change shape |
| **verify** | [`test-the-edges`](skills/test-the-edges/SKILL.md) | the suite is green but trust is low, or inputs come from outside |
| **ship** | [`harden-the-edges`](skills/harden-the-edges/SKILL.md) | the work faces real users, real data, real attackers |
| **ship** | [`open-the-gates`](skills/open-the-gates/SKILL.md) | a release must go out and come back safely |
| **ship** | [`observe-the-system`](skills/observe-the-system/SKILL.md) | a service is born without its signals, or an incident finds you blind |
| **ship** | [`rehearse-the-failure`](skills/rehearse-the-failure/SKILL.md) | the system faces reality soon, and the rollback plan has never once been run |
| **tend** | [`refactor-with-care`](skills/refactor-with-care/SKILL.md) | structure improves without behavior changing |
| **tend** | [`document-the-why`](skills/document-the-why/SKILL.md) | the next reader needs more than the code says |
| **tend** | [`migrate-gently`](skills/migrate-gently/SKILL.md) | persistent data or interfaces must change while running |
| **tend** | [`tend-the-dependencies`](skills/tend-the-dependencies/SKILL.md) | updates are pending, a lockfile drifts, or a major is being rushed |
| **tend** | [`run-the-postmortem`](skills/run-the-postmortem/SKILL.md) | an incident is over and the learning must not evaporate |
| **meta** | [`fire-a-skill`](skills/fire-a-skill/SKILL.md) | KILN itself needs a new skill |

## Install

**Any agent (recommended):**

```bash
npx skills add imranshiundu/kiln
```

The open [skills CLI](https://github.com/vercel-labs/skills) discovers and installs KILN into Claude Code, OpenCode, Cursor, Codex, GitHub Copilot, Amp, Gemini CLI, and [75+ other agents](https://github.com/vercel-labs/skills#supported-agents). Add `--list` to browse first, or `-s <skill>` to take a single craft.

The install path is live-verified — the CLI's real run copied all 25 skills intact to the Claude Code and Codex targets, with outputs recorded in [docs/install-matrix.md](docs/install-matrix.md).

**Claude Code:**

```
/plugin marketplace add imranshiundu/kiln
/plugin install kiln@kiln
```

**Manual:** copy any `skills/<name>/` folder into your agent's skill directory. Common locations: `.claude/skills/` (Claude Code, project), `~/.claude/skills/` (Claude Code, personal), `~/.config/opencode/skills/` (OpenCode), `~/.cursor/skills/` (Cursor), `.agents/skills/` (Codex, Copilot, Amp, and most newer agents, project-level). When in doubt, `npx skills` knows the path.

## For agents

KILN is written *to* agents, not merely *for* them.

- [`AGENTS.md`](AGENTS.md) — the machine-facing doctrine: how to classify work by phase, fire one skill at a time, and claim done only with evidence.
- Point any skills-compatible agent at this repository and it already knows how to use KILN.

```bash
# give KILN to your agent in one line:
npx skills add imranshiundu/kiln
```

## FAQ

**Does KILN work with my agent?**
If your agent reads `SKILL.md` files — Claude Code, OpenCode,
Cursor, Codex, Copilot, Amp, Gemini CLI, and 70+ more — yes. KILN
uses only standard frontmatter and plain Markdown: no includes, no
scripts, no vendor fields. See [docs/install-matrix.md](docs/install-matrix.md)
for per-agent commands and what has been live-verified.

**How do I use just one craft?**
`npx skills add imranshiundu/kiln -s hunt-the-bug`, or copy that
one folder out of `skills/`. Every skill is self-contained; the
library is a shelf, not a chain.

**Why is there no React skill, no Rust skill?**
Because stack knowledge belongs in stack-specific libraries, where
it can go deep. KILN's crafts are the ones that survive a stack
change: data still needs modeling, done still needs evidence,
releases still need rollback.

**How do I know a skill actually works?**
Three ways, in order of strength: the Fire Test runs mechanically
in CI on every change; the checker's own test suite proves it can
fail; and the research notes credit every craft's sources so you
can read the originals. What we don't have yet is scripted eval
scenarios per skill — that is the v1.0 roadmap, stated openly.

**Can I propose a craft?**
Yes — open an issue; the form is the Fire Test in question form.
Read [CONTRIBUTING.md](CONTRIBUTING.md) and
[skills/fire-a-skill/SKILL.md](skills/fire-a-skill/SKILL.md) first;
they are the bar.

## Roots and direction

| Doc | What it holds |
| :- | :- |
| [`docs/format.md`](docs/format.md) | **The roots** — the KILN skill format: frontmatter contract, body anatomy, and the Fire Test quality bar every skill must pass |
| [`docs/lifecycle.md`](docs/lifecycle.md) | The map — the seven fires, their inputs, outputs, and the smell of skipping each |
| [`docs/research.md`](docs/research.md) | The receipts — the field survey of the agent-skills ecosystem, every influence credited |
| [`docs/install-matrix.md`](docs/install-matrix.md) | Per-agent install commands with honest status labels — what's verified, what's documented |
| [`docs/glossary.md`](docs/glossary.md) | The vocabulary pinned — fire, craft, trigger, gate, receipt, the bar |
| [`ROADMAP.md`](ROADMAP.md) | **The direction** — where KILN goes next, and what it will never be |
| [`CHANGELOG.md`](CHANGELOG.md) | What shipped, when, and why |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to fire a new skill into the library |
| [`SECURITY.md`](SECURITY.md) | What security means for a library of prose, and how to report |

## Principles

1. **One craft per skill.** A skill does one thing deeply. If it needs an "and" in its name, it is two skills.
2. **Process, not prose.** Every skill is a workflow with steps, gates, and red flags — never a mood board.
3. **Evidence over claims.** Every skill ends in exit criteria that require observable proof. "Seems right" is not an exit state.
4. **Lean by default.** A loaded skill rides along in context. Every line is a recurring cost; budgets are enforced by the Fire Test.
5. **Tool-agnostic.** KILN follows the open [Agent Skills](https://agentskills.io) standard — no frontmatter tricks, no vendor lock, installs anywhere.
6. **Standing on shoulders.** KILN synthesizes decades of engineering practice and the best of the skills ecosystem, with prior art named in [`docs/research.md`](docs/research.md).

## How KILN maintains itself

A library that preaches evidence runs on its own medicine:

- **The Fire Test is software.** Every push and PR runs
  [`scripts/firetest.py`](scripts/firetest.py) — frontmatter
  contract, five-section anatomy, word budget, routing integrity —
  on Linux, macOS, and Windows, across Python 3.9–3.13.
- **The checker polices itself.** [`tests/run.sh`](tests/run.sh)
  breaks a miniature library fourteen ways and asserts each break
  is caught; a checker that cannot fail is a rubber stamp.
- **Metadata drift is a diff, not a surprise.** The golden inventory
  snapshot fails CI when a skill's trigger or phase changes without
  its snapshot regenerating in the same commit.
- **Releases publish themselves** from tags, with the changelog
  section as notes, gated on tag/version match. A shipped version
  without a changelog entry fails CI before it fails a user.
- **The templates are the bar in question form.** The propose-a-craft
  issue template walks a proposer through the Fire Test; a PR
  template asks for the receipts.
- **The dependencies stay current** the way `tend-the-dependencies`
  teaches: Dependabot opens the batch, CI verifies it.

## Prior art

KILN would not exist without these. They are excellent — go read them:

- [anthropics/skills](https://github.com/anthropics/skills) — the format's home, and the document skills that showed how deep a skill can go
- [obra/superpowers](https://github.com/obra/superpowers) — the proof that a skills library can *be* a methodology
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — production-grade engineering culture, encoded
- [vercel-labs/skills](https://github.com/vercel-labs/skills) — the open installer that made skills portable across 75+ agents
- [agentskills.io](https://agentskills.io) — the open standard that made any of this possible

KILN's difference: it is *lifecycle-complete but minimal* — one library that covers the whole arc of building, one craft per skill, curated rather than sprawling, with a doctrine for how agents should walk the map.

## Contribute

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), study [`docs/format.md`](docs/format.md), and bring a craft that passes the Fire Test.

## License

[MIT](LICENSE) — use KILN in your projects, teams, and tools.
