---
name: review-the-work
description: A hostile self-review pass before declaring anything done - reread the full diff, tag findings by severity, verify every claim with a command. Use when work is about to be presented as complete, a milestone is claimed, or a change is about to be merged.
license: MIT
metadata:
  phase: verify
---

# Review the Work

## North Star

The work has been reread as a hostile reviewer — not as its author —
findings are tagged by severity and resolved or consciously accepted, and
every claim in the completion report is backed by a command you ran and
output you can paste. What you present can survive a skeptic.

## When to fire

- You are about to say "done", "ready", or "this should work".
- A change is about to be committed as final or merged.
- A task's completion is about to be reported to anyone, including you.

## Workflow

1. **Reread the entire diff**, from the top, as someone who wants it to
   fail review. Start at the seams — the boundaries, the error paths —
   because that is where the author's attention faded.
2. **Check the five axes, in order:**
   - **Correctness** — does it do what the spec's acceptance criteria
     say, including the edge cases and the failure paths?
   - **Tests** — do they assert the *behavior* promised, or just the
     code that exists? Would the key tests fail if the feature broke?
   - **Security & data** — every new input, every new store, every new
     boundary: is the boundary enumerated and checked?
   - **Ripple** — what did this change touch that it didn't mean to?
     Stale docs, renamed callers, config that expects the old shape?
   - **Scope** — is anything here that nobody asked for? Scope creep is
     a defect wearing a helpful costume.
3. **Tag every finding:** `BLOCKER` (wrong, unsafe, or incomplete —
   stops the show), `SHOULD-FIX` (fix now, cheap and worthwhile), `NIT`
   (note it and move on). Untagged politeness helps nobody.
4. **Resolve, then re-verify.** Fix the blockers and should-fixes, and
   rerun the review on the *new* diff. Fixes introduce their own
   findings; the pass ends when it comes back clean.
5. **Verify every claim with a command.** "Tests pass" — run them.
   "Builds" — build it. "Handles the empty case" — demonstrate it.
   Any claim you can't evidence, downgrade to "unverified" in the
   report — or go verify it.
6. **Report honestly:** what works (with evidence), what is untested
   (named), what is unfinished (named). The report is the review's
   product; make it a document a skeptic can audit.

## Red flags

- "Looks good" with no findings — the reviewer who finds nothing was
  not reading.
- Reviewing the parts you just wrote with the same attention that wrote
  them — which is to say, with none.
- A completion report with adjectives ("robust", "clean") and no
  commands.
- Fixing only the findings that were easy, and silently promoting the
  rest to "fine".
- Claims about code you did not run this session.

## Exit criteria

- A findings list exists — even an empty one is written down, with the
  five axes checked.
- Blockers resolved and re-reviewed on the fresh diff.
- The completion report contains: claims, the command that verifies
  each, and output. Unverified items are labeled unverified.
- Scope checked: everything in the diff was asked for, or was flagged
  as deliberate addition.
