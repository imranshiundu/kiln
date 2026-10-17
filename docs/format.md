# The KILN Skill Format — the Roots

Every KILN skill follows one format, so any skills-compatible agent can
load any skill with zero learning. The format extends the open
[Agent Skills](https://agentskills.io) standard — it adds conventions, not
incompatible fields.

## Anatomy

A skill is a folder whose name is the skill's identifier, containing a
single `SKILL.md`:

```
skills/
└── hunt-the-bug/
    └── SKILL.md
```

`SKILL.md` is YAML frontmatter followed by a Markdown body:

```yaml
---
name: hunt-the-bug
description: Drives a four-step root-cause hunt - reproduce, reduce,
  hypothesize, guard - and forbids fixing until the cause is proven.
  Use when behavior is wrong and the cause is unknown.
license: MIT
metadata:
  phase: verify
---

# Hunt the Bug

## North Star
...
```

## Frontmatter contract

Only fields from the Agent Skills standard are used, so every skill loads
in every compatible agent (Claude Code, OpenCode, Cursor, Codex, Gemini
CLI, Copilot, and the rest):

| Field | Rule |
| :- | :- |
| `name` | Kebab-case, verb-object where possible (`hunt-the-bug`, `test-first`). Must match the folder name. |
| `description` | Two sentences maximum: **what it does**, then `Use when…` with concrete triggers. This is the only thing agents see before deciding to load the skill — write it as the trigger, not the abstract. Under 1024 characters. |
| `license` | Always `MIT`. |
| `metadata.phase` | One of `gather`, `spec`, `design`, `build`, `verify`, `ship`, `tend`, `meta`. Carries the lifecycle organization without nesting directories. |

Anything else — tool grants, hooks, model overrides — is deliberately
absent. Tool-specific frontmatter breaks portability, and KILN trades
per-agent power for works-everywhere.

## Body anatomy

Five sections, always the same five, always in this order:

1. **`## North Star`** — one paragraph: what the finished state looks
   like. The skill's definition of success.
2. **`## When to fire`** — the concrete trigger conditions, mirroring and
   expanding the `description`.
3. **`## Workflow`** — numbered steps an agent can actually follow, with
   the gates inline: "stop until X".
4. **`## Red flags`** — the recognizable smells of doing this craft badly.
   Agents pattern-match well; name the anti-patterns.
5. **`## Exit criteria`** — the evidence required before declaring the
   skill's work complete. Observable or it doesn't count.

## The Fire Test

A skill ships only if it passes all six:

1. **One craft.** The skill does one thing. If the name needs an "and",
   split it.
2. **Triggerable.** The `description` names concrete situations an agent
   can match against real requests. "Helps with code quality" fails;
   "Use when behavior is wrong and the cause is unknown" passes.
3. **A workflow, not prose.** Steps, gates, and order. If a step can't be
   followed or skipped deliberately, it's decoration.
4. **Evidence over claims.** Exit criteria demand observable proof —
   commands run, output shown, files written. "Seems right" is not an
   exit state.
5. **Lean.** Body under ~500 words. A loaded skill rides in context on
   every turn of its phase; every line is a recurring tax.
6. **Credited.** Where a craft distills known practice, the source is
   named in the body. Craft knowledge is inherited, not invented.

## Conventions

- **Flat layout.** All skills live at `skills/<name>/SKILL.md` — no
  category folders. The lifecycle lives in `metadata.phase` and in
  [`lifecycle.md`](lifecycle.md). Flat keeps every skill one copy-paste
  away from any agent's skill directory.
- **Plain Markdown only.** No includes, no scripts, no runtime
  dependencies. A skill must work as bare text in a bare terminal.
- **Stack-agnostic voice.** Skills may show *examples* in any stack, but
  must never recommend one. The user's stack is the user's call.
- **Numbered gates in workflows.** Steps may carry a gate (`stop until…`);
  skipping a gate silently is the one sin a skill always names.

## Versioning

Skills version with the repository (see [`../ROADMAP.md`](../ROADMAP.md)).
Breaking changes to a skill's workflow are avoided; when unavoidable, the
`description` changes so old triggers no longer match a renamed craft.

## Why so strict

Skills compete for the scarcest resource an agent has: context. A library
that is predictable in structure, tiny in body, and honest about evidence
pays for itself on every load. The format is strict so the skills can be
small, and small so they actually get used.
