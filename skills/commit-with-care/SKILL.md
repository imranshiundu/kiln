---
name: commit-with-care
description: Treats the commit as a work artifact - one logical change per commit, every commit green, the message explains why. Use when committing work, a branch has become one blob before merging, or history will ever need bisecting.
license: MIT
metadata:
  phase: build
---

# Commit with Care

## North Star

The history reads like a story a teammate could follow commit by
commit: each one a single logical change, green when made, its
message saying why it exists. `git bisect` lands on culprits, not
on rubble. The diff is the what; the commit message is the only
place the why survives.

## When to fire

- Work is about to be saved — any work, on any branch.
- A branch has become one multi-thousand-line blob and merge looms.
- History will need bisecting, reverting, or reviewing — which is
  all history, eventually.

## Workflow

1. **Stage one logical change.** If the commit message would need
   an "and", unstage half. Refactor and behavior change never share
   a commit — entangled, neither can be proven or reverted alone.
2. **Keep every commit green.** The suite passes at each commit on
   the branch. A red middle commit turns bisect into guesswork and
   reverts into archaeology.
3. **Write the message for the why.** Subject line: what, in the
   imperative, short. Body: why this change, what was considered
   and rejected, what the reader should double-check. The diff
   already knows what happened.
4. **Commit before you feel done.** Small safe points beat one
   heroic save — this is thin slices at the history level, every
   commit a rollback point.
5. **Clean your own unpushed mess; respect shared history.**
   Rebase and reword freely before push; after push, history is
   public property — append, never rewrite.
6. **Review each commit as a unit before moving on:** `git show`
   it. Stray debugging, half a feature, a file that wandered in —
   caught now for free, caught later for a session.

Craft sources: Tim Pope's note on git commit messages — still the
canonical form; and `git bisect` itself, whose entire value depends
on step 2 being kept.

## Red flags

- "wip" pushed to a shared branch.
- A 3,000-line commit titled "misc" or "final fixes".
- Messages narrating the diff ("changes file.js") — the diff saw
  itself.
- Refactor and fix entangled in one commit, unreviewable forever.
- Fixups stacked on fixups because reading history felt expensive.
  It is expensive; that is why it is worth it.

## Exit criteria

- One logical change per commit, checked with `git show` across
  the branch.
- Every commit green — spot-check at least the tip and the middle.
- Messages that answer why; a stranger could follow the branch as
  a narrative.
