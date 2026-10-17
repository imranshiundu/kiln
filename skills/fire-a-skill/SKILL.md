---
name: fire-a-skill
description: The meta-craft - authors a new KILN skill by finding the single craft, naming it, writing a trigger-first description, the five-section anatomy, and running the Fire Test quality bar before it ships. Use when a craft is missing from the library and keeps being improvised.
license: MIT
metadata:
  phase: meta
---

# Fire a Skill

## North Star

A new skill exists that passes the Fire Test, has fired in a real agent
session, and costs less than it saves. The library grew by one craft —
not by one opinion with formatting.

## When to fire

- The same craft keeps being improvised, and the improvisations differ.
- A phase has work no current skill covers honestly.
- You pasted the same instructions twice in one week — a skill wants to
  exist.

## Before writing

Check it isn't already here — or somewhere better: search KILN, then
[superpowers](https://github.com/obra/superpowers) and
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).
If it exists elsewhere, KILN points, it doesn't duplicate. And if it
isn't a craft — a stack preference, a vendor how-to, a project quirk —
it's not a KILN skill.

## Workflow

1. **Name the craft** in verb-object kebab-case, three words at most
   (`hunt-the-bug`). If the name needs "and", it's two skills — split
   now, while it's cheap.
2. **Write the `description` as a trigger, not an abstract.** What it
   does, then `Use when…` with concrete situations an agent can match
   against real requests. The description is the only thing an agent
   sees before loading you — it *is* the skill's door.
3. **Write the five sections, in order** (contract in `docs/format.md`):
   - **North Star** — the finished state, one paragraph.
   - **When to fire** — the triggers, expanded.
   - **Workflow** — numbered steps, gates inline (`stop until…`).
   - **Red flags** — the smells of doing the craft badly.
   - **Exit criteria** — evidence required to call the craft complete.
     Observable or it doesn't count.
4. **Cut to under ~500 words.** Every line rides in context on every
   turn of the phase. Delete prose that flatters; keep steps that bind.
5. **Credit the sources** in the body. Craft knowledge is inherited —
   from books, practice, other libraries. A skill that claims to have
   invented its craft is lying about its parents.
6. **Run the Fire Test**, all six, in writing: one craft; triggerable
   description; workflow, not prose; evidence over claims; lean;
   credited.
7. **Test it live, both ways.** Run a real session where the skill
   *should* fire — it must. Run one where it *shouldn't* — it must not.
   A skill that fires on everything is noise; one that never fires is a
   file. Include both transcripts, trimmed.
8. **Propose it** via `CONTRIBUTING.md`: one skill per PR, evidence
   attached.

## Red flags

- The skill that is really three skills wearing a trench coat.
- A description so broad it triggers on everything — or so narrow only
  its birth session matches.
- A body that argues instead of instructs. Skills are not essays.
- Shipping without the live-fire test — "it looks right" is exactly what
  `review-the-work` exists to catch.

## Exit criteria

- The Fire Test checklist passed, all six, in writing.
- Transcripts of the skill firing correctly in a real session — and
  correctly staying silent in one where it shouldn't.
- Committed under `skills/<name>/SKILL.md`, frontmatter matching the
  contract, README index updated.
