# Testing That a Skill Works — the live-fire protocol

A skill is instructions, not guarantees. The Fire Test checks the
*format* mechanically; this page is the protocol for the other half
of the bar: **does the skill actually fire, and does firing actually
change anything?** It is the expanded form of `fire-a-skill`'s step
8, the evidence every new skill's PR carries, and the groundwork for
the per-skill eval scenarios on the [v1.0 roadmap](../ROADMAP.md).

## The two-session test

Every skill must pass both sessions, and the transcripts (trimmed)
are the evidence:

**Session A — it should fire.** Construct a real task that matches
the skill's `Use when` triggers — not a mention of the skill by
name, the *situation*. The agent must load the skill unprompted and
its workflow must visibly change what happens: a gate enforced, an
output produced, a step refused until evidence exists. Record:

```
Task given:        (one line)
Skills available:  (list — the skill under test among them)
Fired:             yes/no — and what observable difference it made
                       (the gate it enforced, the artifact it produced)
Evidence:          (the trimmed transcript excerpt)
```

**Session B — it must stay silent.** Construct a task deliberately
*adjacent* — same domain, but one the triggers should not match. A
skill that fires on everything is noise; one that never fires is a
file. Record the same three lines; "Fired: no" is the pass.

A skill without both transcripts is a draft. That rule is not
cruelty — it is the only honest definition of "works".

## What "observable difference" means

Firing is not loading. The bar for session A is a *behavioral*
delta: name the concrete thing the skill changed —

- a gate that stopped work until its evidence existed ("refused to
  declare done; ran the verifier first"),
- an artifact that exists only because the workflow demanded it
  (the boundary table, the timeline, the count check, the
  first-success receipt),
- a named bad outcome avoided (the fix that waited for a
  reproduction; the merge that didn't mix kinds of change).

"The agent seemed more careful" is not a difference; it is a mood.

## The v1.0 ambition: scripted evals

Author transcripts are evidence of one run on one day. The v1.0
roadmap item is the industrial version — for each skill:

1. **A scripted scenario** — the task, the setup, the fixture repo
   or environment it runs against.
2. **A failing baseline** — the same scenario, skill absent: the
   observable difference that *doesn't* happen.
3. **The run with the skill** — the difference, captured.
4. **The silence run** — the adjacent task where it must not load.

The two-session test is the manual form of exactly this; evals are
its automation. Until they exist, this document states plainly
what the library's evidence is and is not: **format — mechanically
enforced; install path — live-verified; firing behavior — author
transcripts, per this protocol.** No row gets promoted without its
receipt.
