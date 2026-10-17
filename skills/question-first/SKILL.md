---
name: question-first
description: Interviews the user one question at a time to turn a vague request into precise, testable requirements. Use when a request has no acceptance criteria, could mean several materially different things, or the user says "build me X" without constraints.
license: MIT
metadata:
  phase: gather
---

# Question First

## North Star

The request has been transformed into a written problem statement with
testable acceptance criteria, confirmed by the user in their own words.
The expensive misunderstandings — the ones that survive until the demo —
are already dead.

## When to fire

- The user asks for something new: a feature, an app, a script, a page.
- You cannot state, in one sentence, what "done" looks like.
- Two reasonable readings of the request lead to materially different work.
- The user has described *what* they want but never *why* they want it.

## Workflow

1. Restate the request in one sentence and say what you believe they want.
   If you cannot, that is your first question.
2. Ask **one question at a time**. Never a list, never a form. Each answer
   changes what the next question should be. Batched questions get
   batched answers; you want considered ones.
3. Prefer questions about *why* and *for whom* over questions about
   *how*. The why constrains the how; the reverse is not true.
4. Play your understanding back after each meaningful answer — one or two
   sentences, corrected until the user confirms. Do not bank corrections
   for later.
5. Probe the edges explicitly, one at a time: what should it never do
   (non-goals), what happens at the extremes (scale, empty, failure), who
   besides the requester will touch it.
6. Stop interviewing when you can write acceptance criteria that a
   third party could grade without asking anyone. Then write them, show
   them, and get the user's confirmation that this is what they meant.
7. If the ask is small and fully specified already, say so and skip to
   work — but say it, don't just go silent.

## Red flags

- Accepting the user's first framing without asking what problem it
  serves. Framings are drafts, not requirements.
- Inventing requirements to fill silence. If you must assume, label it
  "assumed" and confirm it in writing.
- Asking questions you could answer yourself by reading the repo, the
  code, or the docs. Wasted questions spend the user's patience.
- Interviewing past the point of grading criteria. Precision theater is
  its own failure.

## Exit criteria

- A written problem statement (three sentences maximum) and a list of
  testable acceptance criteria, both confirmed by the user.
- Non-goals stated. Assumptions labeled as assumptions.
- If the user will not engage, their refusal is recorded in the work
  summary — never silently guessed around.
