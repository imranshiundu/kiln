---
name: refactor-with-care
description: Improves structure without changing behavior - tests green before and after, Chesterton's Fence respected, small named moves instead of rewrites. Use when cleaning up code that works, renaming for clarity, or untangling structure - without any intended behavior change.
license: MIT
metadata:
  phase: tend
---

# Refactor with Care

## North Star

The code is better, the behavior is provably identical, and the history
shows a sequence of small, individually defensible moves. Tests were
green before, green after, and the commit messages tell the story of
why.

## When to fire

- Code works but is harder to read or change than it should be.
- A change is about to be made and the ground it stands on is mush.
- Names have started lying about what things do.
- Someone proposes a "quick cleanup" — this skill is what makes it
  quick *and* safe.

## When *not* to fire

- You want different behavior. That's a feature; use the other skills.
- The code is ugly but nobody ever touches it. Untouched ugliness is
  free; refactoring it is not.

## Workflow

1. **Secure the net first.** Confirm the behavior is pinned: tests exist
   and pass before you begin. No net, no acrobatics — write the
   characterizing tests first, or refactor somewhere that has them.
2. **Understand before improving (Chesterton's Fence).** Any code that
   looks absurd had an author who survived shipping it. Before removing
   a fence, know what it was fencing. If you can't find out, that
   inability is a finding — report it, don't pave over it.
3. **Choose small, named moves** — extract function, rename, inline,
   move — the vocabulary from *Refactoring*, one move per commit. If
   your move has no name, it's a rewrite in a trench coat.
4. **Never mix kinds of change.** A commit is refactor (behavior
   identical) *or* behavior change — never both. The moment "while I
   was in there" adds a fix, you can no longer prove either.
5. **Run the net after every move.** Green → move → green. A refactor
   that's red at step four is easier to unwind than one that's red at
   step forty.
6. **Stop when the shame is gone, not when the code is fashionable.**
   The goal is code the next changer can read, not code you'd frame.
   Perfect is the enemy of done; done is the enemy of half-done.

## Red flags

- "Improvements" that arrived with a behavior change riding along.
- The rewrite that was faster than understanding — it never is; it only
  moves the understanding debt to the next person.
- Refactoring without a green net, because "the change is trivial".
  Trivial is the camouflage of the catastrophic.
- Deleting code because it's ugly and unowned — ugly was sometimes
  load-bearing.

## Exit criteria

- Tests green before, green after, run at every move — evidenced by the
  last run's output.
- One concern per commit; no commit mixes structure with behavior.
- For every removed oddity: the reason it existed (or the honest record
  that nobody knows).
- The next reader — who is often you — can follow the sequence and say
  why each move was safe.
