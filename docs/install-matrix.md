# KILN Install Matrix — per agent

One skill format, many agents. This page says, per agent, **how KILN
installs** and **what has actually been verified** — no blank claims.
Statuses mean:

| Status | Meaning |
| :- | :- |
| **VERIFIED** | Demonstrated with evidence in this repository or its sibling projects. |
| **DOCUMENTED** | The install path is the tool's own documented interface; not yet live-tested for KILN. |
| **UNTESTED** | Believed to work; nobody has run it. Fix that by running it and PR-ing the result. |

## Any agent — the skills CLI (recommended)

```bash
npx skills add imranshiundu/kiln          # all 19 skills
npx skills add imranshiundu/kiln --list   # browse first
npx skills add imranshiundu/kiln -s hunt-the-bug   # one craft
```

The open [skills CLI](https://github.com/vercel-labs/skills) installs
into [75+ agents](https://github.com/vercel-labs/skills#supported-agents)
— Claude Code, OpenCode, Cursor, Codex, GitHub Copilot, Amp, Gemini
CLI, and the rest.

**Status: VERIFIED** for the layout contract. The CLI installs from
`skills/<name>/SKILL.md` at the repo root; KILN follows exactly that
layout, and the identical layout is proven in production by the
sibling repo [imranshiundu/OCD](https://github.com/imranshiundu/OCD)
(same author, same layout, listed on skills.sh). Per-agent behavior
after install: **DOCUMENTED**, not yet live-tested for all 19 skills —
see the checklist below.

## Claude Code

```
/plugin marketplace add imranshiundu/kiln
/plugin install kiln@kiln
```

Or per-project: `npx skills add imranshiundu/kiln` inside the project,
or copy `skills/<name>/` into `.claude/skills/` (project) or
`~/.claude/skills/` (personal).

**Status: VERIFIED** that `.claude-plugin/plugin.json` and
`marketplace.json` parse and carry the current version and skill count
(CI checks this on every push). **DOCUMENTED** for the marketplace
commands themselves.

## OpenCode

```bash
npx skills add imranshiundu/kiln
```

Or copy `skills/<name>/` into `~/.config/opencode/skills/` (global) or
the project's `.opencode/skills/`.

**Status: DOCUMENTED.**

## Cursor

```bash
npx skills add imranshiundu/kiln
```

Or copy `skills/<name>/` into `~/.cursor/skills/` (global) or
`.cursor/skills/` (project).

**Status: DOCUMENTED.**

## Codex / Copilot / Amp

```bash
npx skills add imranshiundu/kiln
```

Or copy `skills/<name>/` into `.agents/skills/` (project-level, shared
by most newer agents).

**Status: DOCUMENTED.**

## The checklist this page exists to shrink

- [ ] Live-install in Claude Code; confirm all 19 skills listed; note
      the exact command output (trimmed) here.
- [ ] Live-install in OpenCode; same.
- [ ] Live-install in Cursor; same.
- [ ] Live-install in Codex; same.
- [ ] `npx skills update -y -g` upgrades a v0.1 install to v0.2.

Each box checked moves one row from DOCUMENTED to VERIFIED, with the
transcript linked. That is the whole method: no row gets promoted
without evidence.

## Why plain Markdown wins here

Every KILN skill is a folder with one `SKILL.md` — YAML frontmatter
(`name`, `description`, `license`, `metadata.phase`) plus five
sections. No includes, no scripts, no runtime dependencies. Anything
that can read a file can load KILN; the matrix above is only about
*convenience*, not capability.
