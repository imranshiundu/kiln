---
name: read-the-codebase
description: Explores unfamiliar code deliberately - the repo's own story first, entry points, one real request traced end to end, the seams and tests mapped - and leaves a written brief. Use when work starts in a repository you do not know, or answers keep citing code nobody has opened.
license: MIT
metadata:
  phase: gather
---

# Read the Codebase

## North Star

You can explain the system in five sentences and point at the three
riskiest places to change — because you traced a real request end to
end, not because you pattern-matched the filenames. The brief you
leave behind separates what you verified from what you assumed, and
the next reader starts from your map instead of from zero.

## When to fire

- Work begins in a repository you have not read before.
- Answers about the codebase keep citing code nobody has opened.
- A bug, a feature, or a review lands in a project whose
  architecture is unknown to the room.
- "It's similar to the other repo" is offered as understanding.
  It never is.

## Workflow

1. **Read the repo's own story first:** README, CI config, module
   layout, the last month of commits. The repository documents its
   intent everywhere except the code — start where it says it out
   loud. The commit log also tells you what is actively rotting.
2. **Find the entry points.** main, routes, handlers, exports — the
   places the outside world touches first. Everything else hangs
   off them; reading from the edges inward is reading the novel
   backwards.
3. **Trace one real request end to end.** Pick a common path and
   follow it — input to output, reading only what the path touches.
   One traced request teaches more than a hundred skimmed files.
4. **Map the seams.** Where code crosses boundaries — processes,
   networks, disks, queues — is where behavior lives and breaks.
   List them; they are your future debugging map.
5. **Read the tests as documentation of intent.** A test suite is
   the code describing itself; what is untested is at least as
   informative as what is.
6. **Write the brief.** Five sentences of architecture, the traced
   request's path, the seams, the three riskiest spots, and every
   assumption labeled as assumed. Labeling is the craft's honesty:
   verified and assumed are different currencies.

Craft sources: Spinellis' *Code Reading* — reading as an engineering
skill in its own right; Hermans' *The Programmer's Brain* — what
working memory can and cannot hold while navigating unfamiliar code,
and why a written brief beats a heroic memory.

## Red flags

- Editing files before tracing any path through them.
- Trusting names over reading bodies. `handleSync` that doesn't
  sync is a tale as old as names.
- The brief skipped because "it's clear now" — it is not, tomorrow
  it won't be, and the brief was the point.
- Confident claims about code nobody opened this week.

## Exit criteria

- The brief written and shared: architecture, traced path, seams,
  risks, assumptions labeled.
- One real request traced end to end, its path listed in the brief.
- Every architecture claim in the brief marked verified or assumed.
