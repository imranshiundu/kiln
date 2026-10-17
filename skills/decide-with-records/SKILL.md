---
name: decide-with-records
description: Makes cross-cutting choices once, from real options with explicit trade-offs, and records each as a short decision record (context, decision, consequences, reversibility). Use when choosing technologies, architectures, data shapes, or any decision future builders must know was deliberate.
license: MIT
metadata:
  phase: spec
---

# Decide with Records

## North Star

Every decision that shapes the work exists as a short written record: the
context, the real options considered, the choice, what it optimizes for,
and how hard it would be to reverse. Nobody ever re-litigates a decision
by accident again — only deliberately, with the record in hand.

## When to fire

- A technology, library, architecture, or data-shape choice is pending
  that will be expensive to reverse.
- The same question has been asked (and answered differently) twice.
- You are about to pick "whatever I know best" without naming it as a
  choice with alternatives.
- A decision affects more than the file you are currently editing.

## Workflow

1. **Name the decision as a question** — "where does session state
   live?", not "use Redis".
2. **List the real options.** At least two, at most four. "Do nothing"
   counts as an option and sometimes wins. An option no one would defend
   is padding — cut it.
3. **State each option's trade-off in one line**: what it optimizes for
   and what it costs. Trade-offs without costs are sales copy.
4. **Check your own defaults.** If your leaning is the stack you know
   best, say so out loud — familiarity is a legitimate cost factor, but
   only when named as one.
5. **Choose, and record.** One decision per record, in the format:
   - **Context** — what forced this choice, in two sentences.
   - **Decision** — one sentence, in the active voice.
   - **Consequences** — what we get, what we accept, what gets harder.
   - **Reversibility** — cheap (try it and see) or expensive (assume
     permanent). Prefer cheap decisions when the stakes are unclear.
6. **Prefer reversibility over certainty.** When two options are close,
   pick the one that's easier to undo. Boring choices are allowed to win
   because they are boring.
7. **Store records beside the code** (`docs/decisions/NNNN-name.md`),
   numbered in the order decided. Link from the spec; reference from
   code comments where the decision bites.

## Red flags

- Deciding by vibes and writing the record as a justification afterward.
- The one-option decision record — a choice with no alternatives
  considered is an event, not a decision.
- Choosing the loudest technology when the quiet one is reversible.
- Records that never mention reversibility — the reader can't tell a
  whim from a wall.

## Exit criteria

- A record exists for every cross-cutting decision, in the standard
  format, committed where future builders will find it.
- Each record names at least two genuinely considered options.
- The chosen option states what it optimizes for, and its reversibility
  is labeled.
