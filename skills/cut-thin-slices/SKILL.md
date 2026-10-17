---
name: cut-thin-slices
description: Implements in thin vertical slices that each run end to end and could ship - walking skeleton first, then slice by slice with a commit at every safe stopping point. Use when implementation begins on anything bigger than a one-liner, or when work spans multiple layers or files.
license: MIT
metadata:
  phase: build
---

# Cut Thin Slices

## North Star

The project walks before it runs: a smallest end-to-end skeleton is live
early, and every slice after it — small, vertical, demonstrably working —
leaves the system better than the previous commit found it. At any
moment, "how much is done?" is answerable by *what works*, not by
percentage guesses.

## When to fire

- Implementation is starting and the plan has more than one step.
- The work spans layers (UI, API, data) — the exact setup for the
  layer-by-layer trap.
- Someone proposes "first we build all the models, then all the
  endpoints, then we wire it up".
- A branch has gone more than a day without a demonstrable end-to-end
  path.

## Workflow

1. **Build the walking skeleton first.** The thinnest path that touches
   every layer and does one real thing — one endpoint that persists one
   row and returns it; one page that reads and renders it. Ugly is
   allowed; nonexistent integration is not. The skeleton's job is to
   prove the *seams*, not to impress.
2. **Cut the work into vertical slices** — each slice walks end to end
   (touches every layer it needs) and could ship on its own. "Users can
   log in" is a slice. "The data layer" is not a slice; it is a layer
   costume.
3. **Implement one slice at a time.** Implement → verify it works
   end-to-end → commit. Never hold two unfinished slices — the
   integration debt compounds and hides.
4. **Make every commit a safe stopping point.** Tests green, system
   runs, story intact. A stranger landing on any commit should be able
   to build, run, and see *something* work.
5. **Fake what you must, name what you faked.** In-memory store for the
   first slice, a hardcoded value for the second — fine, if the fake is
   named and the slice is real. A vertical slice may contain a
   horizontal shortcut; it may not contain a missing seam.
6. **When a slice feels too big to hold, cut it again.** If you can't
   describe the slice in one sentence, it's two slices. If you can't
   finish it in one sitting, it's two slices.
7. **Demo each slice before starting the next.** Show the working thing
   — run it, show the output, get the nod. A slice nobody has seen
   working is a slice that may not work.

## Red flags

- "80% done" for three consecutive days — layer-by-layer building
  wearing a progress costume.
- The integration deferred to the end, as a surprise.
- Commits that don't run ("broken, will fix in next commit") — the
  rollback story just died.
- Slices so thin they don't touch reality (a slice of pure plumbing
  with no visible behavior).

## Exit criteria

- A walking skeleton ran end to end before any slice work began.
- Every slice was demonstrated working (with command output or visible
  evidence) before the next began.
- Every commit in the history builds and runs.
- "How much is done?" is answered by listing what works.
