# KILN Install Matrix — per agent

One skill format, many agents. This page says, per agent, **how KILN
installs** and **what has actually been verified** — no blank claims.
Statuses mean:

| Status | Meaning |
| :- | :- |
| **VERIFIED** | Demonstrated with the output recorded below. |
| **DOCUMENTED** | The install path is the tool's own documented interface; not yet live-tested for KILN. |

## Any agent — the skills CLI (recommended)

```bash
npx skills add imranshiundu/kiln          # all 25 skills
npx skills add imranshiundu/kiln --list   # browse first
npx skills add imranshiundu/kiln -s hunt-the-bug   # one craft
```

The open [skills CLI](https://github.com/vercel-labs/skills) installs
into [75+ agents](https://github.com/vercel-labs/skills#supported-agents)
— Claude Code, OpenCode, Cursor, Codex, GitHub Copilot, Amp, Gemini
CLI, and the rest.

**Status: VERIFIED — live run, skills CLI v1.9.0 (2026-11-20).**

```
$ skills add <kiln source> --agent claude-code -y --global
│  Source: <kiln source>
│  Local path validated
│  Found 25 skills
●  Installing all 25 skills
│  ✓ commit-with-care (copied)  → ~/.claude/skills/commit-with-care
│  ✓ ... all 25 ...
└  Done!
```

The run discovered all 25 skills from the repository layout
(`skills/<name>/SKILL.md` at the root), copied every folder intact —
frontmatter and body byte-identical — and wrote the shared lockfile
(`~/.agents/.skill-lock.json`, format v3) with a per-skill content
hash for `skills update` to diff against. The remote `npx skills add
imranshiundu/kiln` flow is the same machinery plus a GitHub fetch;
the fetch path is proven by the sibling repo
[imranshiundu/OCD](https://github.com/imranshiundu/OCD) (same layout
family, same author), whose remote install — sourceType `github`,
commit pinned — sits in the same lockfile.

## Claude Code

```
/plugin marketplace add imranshiundu/kiln
/plugin install kiln@kiln
```

Or per-project: `npx skills add imranshiundu/kiln` inside the project,
or copy `skills/<name>/` into `.claude/skills/` (project) or
`~/.claude/skills/` (personal).

**Status: VERIFIED** — the CLI run above installed all 25 skills into
`~/.claude/skills/`; a directory listing after the run shows 25
folders, and a spot-checked `SKILL.md` is byte-identical to the repo.
The `.claude-plugin/plugin.json` and `marketplace.json` parse and
carry the current version and skill count (CI checks this on every
push). The `/plugin marketplace` commands themselves: **DOCUMENTED**.

## OpenCode

```bash
npx skills add imranshiundu/kiln
```

Or copy `skills/<name>/` into `~/.config/opencode/skills/` (global) or
the project's `.opencode/skills/`.

**Status: DOCUMENTED.** The CLI run targeting `--agent opencode`
completed and updated the lockfile, but this machine had no OpenCode
installation for the files to land in — a run on a box with OpenCode
present is the remaining step.

## Cursor

```bash
npx skills add imranshiundu/kiln
```

Or copy `skills/<name>/` into `~/.cursor/skills/` (global) or
`.cursor/skills/` (project).

**Status: DOCUMENTED.** Same story as OpenCode: the CLI run completed;
no Cursor installation existed to receive the files.

## Codex / Copilot / Amp

```bash
npx skills add imranshiundu/kiln
```

Or copy `skills/<name>/` into `.agents/skills/` (project-level, shared
by most newer agents).

**Status: VERIFIED** — the CLI run targeting `--agent codex` installed
all 25 skills into `~/.agents/skills/`, with the lockfile at
`~/.agents/.skill-lock.json` carrying source, commit, and per-skill
hashes.

## The checklist this page exists to shrink

- [x] Live install via the skills CLI — all 25 skills discovered,
      copied intact, lockfile written (2026-11-20, v1.9.0).
- [x] Claude Code target directory (`~/.claude/skills/`) — 25/25.
- [x] Codex / shared `.agents` target — 25/25, lockfile hashes.
- [ ] OpenCode on a machine with OpenCode installed.
- [ ] Cursor on a machine with Cursor installed.
- [ ] Remote run of `npx skills add imranshiundu/kiln` itself
      (verified by sibling OCD's remote install; run once for KILN).
- [ ] `npx skills update -y -g` upgrades a v0.2 install to v0.3.

Each box checked moves one row up a status level, with the output
recorded here. That is the whole method: no row gets promoted without
evidence.

## Why plain Markdown wins here

Every KILN skill is a folder with one `SKILL.md` — YAML frontmatter
(`name`, `description`, `license`, `metadata.phase`) plus five
sections. No includes, no scripts, no runtime dependencies. Anything
that can read a file can load KILN; the matrix above is only about
*convenience*, not capability.
