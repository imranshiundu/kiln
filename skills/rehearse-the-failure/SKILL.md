---
name: rehearse-the-failure
description: Meets the feared failure modes on your terms - each fear stated as a testable hypothesis, failure injected in a controlled environment with abort conditions set first, and the runbook's gaps found by rehearsal instead of incident. Use when the system is about to face reality - a launch, a migration, a high-stakes weekend - and the rollback plan has never been executed.
license: MIT
metadata:
  phase: ship
---

# Rehearse the Failure

## North Star

The failures you feared have already happened — in an environment
you controlled, at a dose you chose, with an abort switch in
hand. The rollback plan was executed, not merely written; the
runbook's gaps were found by rehearsal; and the numbers you'll
need during the real thing — detect time, respond time, recover
time — already exist.

## When to fire

- The system is about to face reality: a launch, a migration, an
  event that cannot be rescheduled.
- A rollback or DR plan exists that no one has ever executed.
- Critical dependencies are assumed reliable because they always
  have been.
- `harden-the-edges` enumerated the boundaries; rehearsal is how
  the list gets tested.

## Workflow

1. **Turn each fear into a hypothesis**: "if the primary database
   dies, checkout still serves from cache for ten minutes." A
   drill without a stated claim is vandalism with a calendar
   invite. (The Principles of Chaos Engineering: experiments test
   a hypothesis about steady state.)
2. **Define blast radius and abort conditions before anything
   breaks** — what you may hurt, how you'll know to stop, who can
   pull the switch. A drill that takes staging down unrecoverably
   was worse than the incident it simulated.
3. **Inject at the smallest dose and ramp.** Kill one instance
   before the region; add latency before removing capacity.
4. **Watch the real metrics** — the drill's product is data:
   time-to-detect, time-to-respond, time-to-recover, and what
   actually degraded first.
5. **Follow the runbook as written.** Every place it lies, every
   step it lacks, is a finding — fix the doc or the system; the
   drill found the gap for free.
6. **Execute the rollback for real.** Flip it, watch, verify,
   flip back. "Rehearsed" means performed, not read.
7. **Record hypothesis, injection, observed times, gaps, and
   owners** — the drill's short report, filed next to the plan.

## Red flags

- Random breakage without a hypothesis — chaos as theater.
- Abort conditions written after the pain started.
- The drill that never opened the runbook.
- Rollback "rehearsed" by reading it aloud.
- Findings with no owner — a drill that teaches nothing twice.

## Exit criteria

- Hypotheses written before any injection.
- Abort conditions and blast radius documented before the start.
- Detect/respond/recover times recorded per scenario.
- Runbook gaps found, each fixed or owned.
- The rollback executed and reverted, with evidence.
