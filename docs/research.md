# KILN Research Notes — the Receipts

KILN was designed against a survey of the agent-skills ecosystem, done in
October 2026. This document records what was examined, what each source
taught us, and what gap KILN fills. It exists so contributors can hold the
library to its sources.

## The standard

**[Agent Skills](https://agentskills.io)** — an open format (originally
developed by Anthropic, now community-governed): a folder with a
`SKILL.md` containing YAML frontmatter (`name`, `description`, at minimum)
and Markdown instructions, plus optional scripts and assets. Skills load
through *progressive disclosure*:

1. **Discovery** — the agent sees only `name` + `description`.
2. **Activation** — a matching task loads the full body.
3. **Execution** — the agent follows the instructions.

Supported across Claude Code, Claude, ChatGPT/Codex, Cursor, OpenCode,
Gemini CLI, GitHub Copilot, Amp, Goose, Kiro, OpenHands, Roo Code, VS Code,
and dozens more.

**What KILN took from it:** everything structural. KILN skills use only
spec frontmatter fields and rely on progressive disclosure — which is why
KILN skills are deliberately *small*: the body's per-turn cost is the
format's built-in tax.

## The tooling

**[vercel-labs/skills](https://github.com/vercel-labs/skills)** — the open
`npx skills` CLI. Installs skills from any GitHub repo into 75+ agents,
symlinks or copies, project-scoped or global, with a bounded 3-level
discovery walk (`skills/<category>/<name>/SKILL.md` supported — KILN
stays at 1 level for maximal portability) and
[skills.sh](https://skills.sh) as the discovery directory.

**What KILN took from it:** install reality. KILN's flat
`skills/<name>/SKILL.md` layout is copy-paste compatible with every agent
directory the CLI knows about, and `npx skills add imranshiundu/kiln` works
out of the box.

## The libraries

| Library | What it is | What KILN took |
| :- | :- | :- |
| [anthropics/skills](https://github.com/anthropics/skills) (180k★) | The official repo: document skills (docx/pdf/pptx/xlsx) and examples, plus the spec and a template | The template discipline; that complex crafts (document generation) fit the format fine |
| [obra/superpowers](https://github.com/obra/superpowers) (300k★) | A complete *methodology* built on composable skills: brainstorming → writing-plans → TDD → systematic-debugging → code review → finishing branches, with a meta-skill (`writing-skills`) and the "evidence over claims" philosophy | The philosophy (systematic over ad-hoc; verification before completion); the meta-skill pattern; that a skills library can *be* a way of working |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (107k★) | Production engineering culture encoded: DEFINE→PLAN→BUILD→VERIFY→REVIEW→SHIP lifecycle commands; anti-rationalization tables; five-axis review; Hyrum's Law in API design; Chesterton's Fence in simplification | The anti-rationalization idea (skills must name the excuses agents make); the craft sourcing from *Software Engineering at Google*; that a lifecycle gives a library a spine |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | The #1 skills library for a single domain (science) | That depth in one domain beats shallow breadth across many |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | A curated catalog of 1000+ community skills | That curation is the value; 1000 skills is a search problem, not a library |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Design-taste as a skill | That "soft" judgments (taste, voice) can be encoded as workflows too |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Type-safe skills collection | TypeScript-specific rigor — and the reminder that stack-specific libraries and stack-agnostic libraries need different shapes |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | Copilot instructions/agents/skills, long predating the standard | The pre-standard era — instruction files that wanted to be skills |

## The gap KILN fills

Every strong library occupies one pole:

- **A methodology** (superpowers): one opinionated way of working,
  enforced. Powerful, but it's *their* way.
- **A culture pack** (addyosmani): one company's engineering culture,
  faithfully encoded. Deep, but a stack-flavored point of view.
- **A catalog** (awesome lists): everything, curated by nobody in
  particular.
- **Demos** (anthropics): breadth of possibility, depth on documents.

KILN occupies the pole none of them claim: **a minimal, stack-agnostic
curriculum of the crafts themselves** — what a builder needs at every
phase, one craft per skill, each skill independent and composable, with an
agent-facing doctrine for walking the map. Use it alone, or alongside any
of the above: superpowers will happily fire `hunt-the-bug`; an
addyosmani-style constraint checklist can gate `review-the-work`.

## The craft sources

The skills themselves distill named practice, credited inside each body:

- **`question-first`** — one-question-at-a-time requirements interviewing,
  echoed by both superpowers (`brainstorming`) and addyosmani
  (`interview-me`).
- **`test-first`** — TDD's red-green-refactor (Beck), the test pyramid
  and DAMP-over-DRY (Software Engineering at Google), plus the honest
  edge: where TDD is the wrong tool.
- **`hunt-the-bug`** — four-phase root-cause discipline
  (`systematic-debugging` in superpowers; the reduce-and-fix loop
  everywhere).
- **`design-the-interface`** — contract-first design; Hyrum's Law.
- **`refactor-with-care`** — Chesterton's Fence (Boulding), small named
  moves (Fowler).
- **`review-the-work`** — severity-tagged findings, review-the-diff-not-
  the-memory (Google's eng-practices review guide).
- **`harden-the-edges`** — boundary enumeration; OWASP's mental model
  without OWASP's checklist bloat.
- **`open-the-gates`** — "faster is safer"; small releases, real rollback
  plans (Accelerate / DORA).
- **`document-the-why`** — ADRs (Nygard), docs-for-the-2am-reader.
- **`fire-a-skill`** — meta-skill pattern (superpowers `writing-skills`;
  Anthropic's skill-authoring best practices).

## Honest limits of this research

- Skills are instructions, not guarantees — the ecosystem's own eval work
  (e.g. superpowers-evals) is where efficacy gets measured. KILN v1.0
  plans per-skill eval scenarios for the same reason (see
  [ROADMAP.md](../ROADMAP.md)).
- Star counts are a popularity snapshot (October 2026), not a quality
  claim.
- The ecosystem moves weekly. When this document and reality disagree,
  believe reality, then send a PR.
