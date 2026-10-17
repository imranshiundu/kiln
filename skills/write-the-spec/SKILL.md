---
name: write-the-spec
description: Writes a one-page build contract - problem, users, non-goals, acceptance criteria, constraints - and gets sign-off before code. Use when an agreed idea is about to become implementation, a project or significant feature is starting, or requirements exist only in conversation.
license: MIT
metadata:
  phase: spec
---

# Write the Spec

## North Star

A one-page spec the user has signed off on. Anyone reading it — a
developer, a different agent, you in three weeks — knows what is being
built, why, what it deliberately will not do, and how success will be
judged.

## When to fire

- An idea has been agreed verbally but nothing is written down.
- A new project, service, or significant feature is starting.
- The conversation keeps circling the same unresolved questions.
- More than one builder (or agent) will touch the work.

## Workflow

1. **Hold the length.** One page is the spec's feature, not its limit.
   If it doesn't fit, the scope is too big — split the work, not the page.
2. Write these sections, in this order:
   - **Problem** — two sentences: what hurts, for whom, today.
   - **Users** — who touches this, and who is the *primary* one when
     they conflict.
   - **Non-goals** — what this deliberately will not do. A spec without
     non-goals is an invitation to scope drift.
   - **Acceptance criteria** — testable statements, each independently
     gradeable: "given X, then Y". No "should be fast" without a number.
   - **Constraints** — stack, budget, deadline, environment realities.
     Existing decisions link to their records.
3. **Leave open questions visible.** List them with owners and a
   "decided by" date. Unresolved belongs in the open-questions list, not
   in optimistic prose.
4. **Get sign-off on the spec itself, not on its existence.** Walk the
   user through the acceptance criteria. The acceptance criteria are the
   contract; everything else is commentary.
5. **Treat later spec changes as the moment to re-align.** A change gets
   written into the spec before it gets written into the code. If a
   change invalidates criteria, say what it invalidates and get that
   acknowledged.

## Red flags

- The spec that narrates features but never states how success is graded.
- Non-goals that are secretly goals ("non-goal: scalability" on a service
  that must scale).
- Sign-off by silence — you showed it, they didn't object. That is
  ambiguity, not agreement.
- A spec written *after* the code, retrofitted to match what was built.

## Exit criteria

- The spec exists in the repo (or the agreed artifact location), is one
  page, and contains all five sections.
- Every acceptance criterion is testable, and the user has explicitly
  confirmed the criteria — not just the document.
- Open questions are listed with owners, not buried.
