---
name: document-the-why
description: Writes documentation for the reader who arrives last - README that gets a stranger running, decision records for the whys, inline comments that explain reasons instead of narrating code. Use when onboarding docs are stale, a decision needs to outlive the decision-maker, or the next reader needs more than the code says.
license: MIT
metadata:
  phase: tend
---

# Document the Why

## North Star

A stranger can clone, run, and orient without asking anyone a question.
The *why* of every non-obvious choice is findable — in the README, the
decision records, or a comment — and the docs describe the present, not
the past.

## When to fire

- A project is gaining a second contributor — including an agent, a
  teammate, or future-you.
- A non-obvious decision was just made (write it now, while you still
  remember the alternatives).
- The README's setup instructions have drifted from reality.
- Someone will ask "why is it like this?" more than once.

## Workflow

1. **Write for the reader who arrives last**: no context, no patience,
   possibly at 2am during an incident. Every sentence they'd have to
   re-read is a sentence to rewrite.
2. **The README answers three questions in order:**
   - *What is this?* — one paragraph, no vision statements.
   - *Why does it exist?* — one paragraph, the problem it solves.
   - *How do I run it?* — copy-pasteable commands, from a clean
     machine, tested by actually running them from scratch. The day
     this list stops working, it gets fixed in the same commit that
     broke it.
3. **Record the whys where they live.** Decisions go to decision
   records (see `decide-with-records`); surprising code gets a comment
   that states the *reason* — never a narration of the mechanics. The
   code is its own narration; the comment exists for the "why would
   anyone do this" that the code cannot answer.
4. **Document the failure modes**: what breaks most often, how to tell
   which one it is today, and what to check first. This section saves
   more 2am time than any other.
5. **Delete more than you write.** Stale documentation is worse than
   none — it's confident misinformation. When the code changes the
   truth, the docs change in the same commit or the docs get deleted.
   Perishable notes ("TODO 2024…", "currently investigating…") belong
   in the issue tracker where they can die properly, not in the README
   where they fossilize.
6. **Prove it works.** Give the docs to someone (or an agent) without
   your context and watch where they stumble. Each stumble is a
   documentation bug; fix it and repeat.

## Red flags

- A README whose setup commands have never been run from a clean
  machine.
- Comments that translate the code into English (`i++ # increment i`)
  while the real "why" is nowhere.
- Architecture docs describing last year's system.
- Documentation whose only reader is its author — if nobody arrives
  last, the docs are for a ghost.

## Exit criteria

- A stranger (or fresh agent session) ran the project from the README
  alone — and the stumbles found were fixed.
- Every non-obvious choice has a why within one hop of the code: a
  comment or a linked decision record.
- No stale perishables in the docs; everything there describes the
  present.
