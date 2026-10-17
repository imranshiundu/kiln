---
name: ground-truth
description: Establishes verified facts before building - reading the actual codebase and checking APIs against primary sources instead of trusting memory or blog posts. Use when working in an unfamiliar codebase, using a library whose version may differ from training knowledge, or building on any claim you have not personally verified.
license: MIT
metadata:
  phase: gather
---

# Ground Truth

## North Star

A short context brief exists that separates three piles: **verified**
(you ran it, read it, or tested it), **assumed** (reasonable inference,
unverified), and **risky** (would be expensive if wrong). Nothing you
build rests silently on the risky pile.

## When to fire

- You are about to build in a codebase you have not read end to end.
- You would reach for an API from memory for a library whose version you
  have not checked.
- A claim from the user, an issue, a tutorial, or your own recall is
  load-bearing for the design.
- The task says "just integrate X" and X has not been looked at.

## Workflow

1. **Read the terrain before drawing the map.** Find the entry point, run
   the build and the tests yourself, and read the tests you can't run —
   they encode the intended behavior. Read the config files and the CI
   pipeline; they are the project's actual rules, not its documentation's
   claims.
2. **Find the seams.** Where does this system end and the next begin?
   Note the conventions (naming, error handling, file layout) — you will
   follow the ones that exist, not the ones you prefer.
3. **Verify external APIs against primary sources.** For any library
   call: check the installed version, then the official docs or types for
   that version. If it matters, run a two-line snippet that calls it.
   Memory is a draft; the docs are the law.
4. **Distrust secondary sources for current-version facts.** Blog posts
   age into fiction. A tutorial is evidence of the past, not of the
   present. When you must use one, verify its claims against the primary
   source before building on them.
5. **Write the brief.** Three lists — verified, assumed, risky — each item
   one line, with how it was verified or why it's risky. Six lines is
   usually enough; twenty is a sign the task is bigger than it looked.
6. **Spend risk down before building.** Convert risky items into verified
   or changed plans *before* the design leans on them.

## Red flags

- Writing code against an API signature you have not checked in the
  installed version.
- "The docs say" with no link, and "it should work" with no run.
- Treating training-data recall of a fast-moving library as current fact.
- A context brief that is all one pile — everything verified (unlikely)
  or everything assumed (unwise).

## Exit criteria

- A context brief exists with all three piles, shown to the user before
  implementation.
- Every load-bearing external API claim has been checked against its
  primary source, and the version was confirmed.
- The build and the test suite have been run by you, and their state is
  reported honestly — green, red, or "no suite exists".
