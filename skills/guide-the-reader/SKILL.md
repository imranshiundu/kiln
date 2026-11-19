---
name: guide-the-reader
description: Builds user-facing documentation that does one job at a time - tutorials that teach, how-tos that solve, reference that answers, explanation that understands - with the newcomer's first-success path verified by running it. Use when a user must learn the thing you built, the same question keeps getting answered in chat, or the docs mix teaching with reference into mush.
license: MIT
metadata:
  phase: tend
---

# Guide the Reader

## North Star

A newcomer reaches first success — their first API call, first
build, first deploy — without asking anyone, because each doc did
exactly one job: the tutorial taught, the how-to solved, the
reference answered, the explanation built understanding. Docs
that rot carry dates, so their age is visible at a glance.

## When to fire

- Writing or overhauling user-facing docs: README, onboarding,
  API guides, user runbooks.
- The same "how do I..." question answered in chat for the third
  time.
- A doc mixes a tutorial with reference and fails at both.
- A newcomer's first hour is spent guessing.

## Workflow

1. **Name the reader and their first success** in one sentence:
   "a Python developer makes their first authenticated API call
   in ten minutes." Every later choice is judged against this.
2. **Sort pages into the four modes** — tutorial (learning by
   doing), how-to (reaching a goal), reference (looking things
   up), explanation (understanding why) — and keep each page to
   one mode. The mixing is why docs feel bad. (Diátaxis.)
3. **Write the tutorial as a held hand:** every step runs exactly
   as written, no detours, no unexplained magic; success must be
   visible so the learner knows they arrived.
4. **Make how-tos start from the goal** and stay on the path —
   assume the tutorial, link the reference, don't re-teach.
5. **Keep reference complete, neutral, and generated where
   possible** — prose in reference rots into lies; generated
   tables can't.
6. **Point explanation at the decision records** instead of
   duplicating them — `document-the-why` owns the why; this
   skill links it.
7. **Date everything that rots** — versions, commands,
   screenshots — and tie each to the release it belongs to.
8. **Verify by doing:** run the first-success path in a clean
   environment, following only what is written. The tutorial is
   a test; it must pass.

## Red flags

- A README that's an architecture tour when the reader needs a
  five-minute win.
- "It should now look something like…" in a tutorial.
- Reference written as prose paragraphs.
- Docs whose commands were never run as written.
- Undated screenshots presented as current truth.

## Exit criteria

- The four modes separated; each page declares its one job.
- First-success path executed clean in a fresh environment —
  receipt attached.
- Rot-prone artifacts dated or generated.
- The chat question that triggered this points at a doc that
  exists and works.
