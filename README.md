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
  <a href="https://agentskills.io"><img alt="Follows the Agent Skills standard" src="https://img.shields.io/badge/follows-Agent%20Skills-f59e0b.svg"></a>
  <img alt="Works with 75+ agents" src="https://img.shields.io/badge/works%20with-75%2B%20agents-6b5a3e.svg">
</p>

---

A kiln turns soft clay into enduring craft. **KILN turns a capable agent into a complete builder.**

Agents write code fast. What they skip — unless taught — are the crafts that make software last: interrogating the request before building, writing the spec, modeling the data, testing first, hunting root causes instead of symptoms, hardening the edges, documenting the why. KILN is those crafts, written down as agent skills: **one craft per skill, each a workflow with gates and evidence requirements, not an essay.**

This is not a pile of prompts. It is a *lifecycle* — a researched map of what it takes to build a whole thing, with a skill waiting at every phase.

## The seven fires

Everything that gets built — an app, a service, a library, a side project — passes through the same fires:

```
 GATHER ──▶ SPEC ──▶ DESIGN ──▶ BUILD ──▶ VERIFY ──▶ SHIP ──▶ TEND
 (clay)   (wedge)   (shape)    (fire)   (sound)   (open)   (keep)
```

Real work loops through these out of order and that is fine — the map is a compass, not a rail. What KILN refuses to do is skip a fire silently.

## The skills

15 skills. Each fits in your agent's context with room to spare, and fires only when relevant.

| Phase | Skill | Fires when |
| :- | :- | :- |
| **gather** | [`question-first`](skills/question-first/SKILL.md) | a request arrives without acceptance criteria |
| **gather** | [`ground-truth`](skills/ground-truth/SKILL.md) | building on code, APIs, or claims that need verifying |
| **spec** | [`write-the-spec`](skills/write-the-spec/SKILL.md) | an agreed idea must become a one-page build contract |
| **spec** | [`decide-with-records`](skills/decide-with-records/SKILL.md) | a cross-cutting choice gets made once and recorded |
| **design** | [`model-the-data`](skills/model-the-data/SKILL.md) | persistent state, entities, or invariants take shape |
| **design** | [`design-the-interface`](skills/design-the-interface/SKILL.md) | an API, module boundary, or public surface is born |
| **build** | [`cut-thin-slices`](skills/cut-thin-slices/SKILL.md) | implementation starts on anything bigger than a one-liner |
| **build** | [`test-first`](skills/test-first/SKILL.md) | writing logic that must not break |
| **verify** | [`hunt-the-bug`](skills/hunt-the-bug/SKILL.md) | behavior is wrong and the cause is unknown |
| **verify** | [`review-the-work`](skills/review-the-work/SKILL.md) | work is about to be presented as done |
| **ship** | [`harden-the-edges`](skills/harden-the-edges/SKILL.md) | the work faces real users, real data, real attackers |
| **ship** | [`open-the-gates`](skills/open-the-gates/SKILL.md) | a release must go out and come back safely |
| **tend** | [`refactor-with-care`](skills/refactor-with-care/SKILL.md) | structure improves without behavior changing |
| **tend** | [`document-the-why`](skills/document-the-why/SKILL.md) | the next reader needs more than the code says |
| **meta** | [`fire-a-skill`](skills/fire-a-skill/SKILL.md) | KILN itself needs a new skill |

## Install

**Any agent (recommended):**

```bash
npx skills add imranshiundu/kiln
```

The open [skills CLI](https://github.com/vercel-labs/skills) discovers and installs KILN into Claude Code, OpenCode, Cursor, Codex, GitHub Copilot, Amp, Gemini CLI, and [75+ other agents](https://github.com/vercel-labs/skills#supported-agents). Add `--list` to browse first, or `-s <skill>` to take a single craft.

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

## Roots and direction

| Doc | What it holds |
| :- | :- |
| [`docs/format.md`](docs/format.md) | **The roots** — the KILN skill format: frontmatter contract, body anatomy, and the Fire Test quality bar every skill must pass |
| [`docs/lifecycle.md`](docs/lifecycle.md) | The map — the seven fires, their inputs, outputs, and the smell of skipping each |
| [`docs/research.md`](docs/research.md) | The receipts — the field survey of the agent-skills ecosystem, every influence credited |
| [`ROADMAP.md`](ROADMAP.md) | **The direction** — where KILN goes next, and what it will never be |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to fire a new skill into the library |

## Principles

1. **One craft per skill.** A skill does one thing deeply. If it needs an "and" in its name, it is two skills.
2. **Process, not prose.** Every skill is a workflow with steps, gates, and red flags — never a mood board.
3. **Evidence over claims.** Every skill ends in exit criteria that require observable proof. "Seems right" is not an exit state.
4. **Lean by default.** A loaded skill rides along in context. Every line is a recurring cost; budgets are enforced by the Fire Test.
5. **Tool-agnostic.** KILN follows the open [Agent Skills](https://agentskills.io) standard — no frontmatter tricks, no vendor lock, installs anywhere.
6. **Standing on shoulders.** KILN synthesizes decades of engineering practice and the best of the skills ecosystem, with prior art named in [`docs/research.md`](docs/research.md).

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
