---
name: find-the-ceiling
description: Finds where the system actually breaks under load - real-workload ramp, latency bar defined first, ceiling recorded as a number with the first thing to degrade named. Use when the system must survive real load - a launch, a peak, an event - and someone asks whether it will hold.
license: MIT
metadata:
  phase: verify
---

# Find the Ceiling

## North Star

The ceiling is a number, not a vibe: at X requests per second the
p95 crosses the bar, and the first subsystem to degrade is named
and known. Shipping decisions are made against the ceiling,
alerts sit just under it, and every release that changes the
system re-measures it.

## When to fire

- A launch, a campaign, a Friday peak is coming and someone asks
  "will it hold?"
- Capacity is being planned and the numbers are guesses.
- Performance work just finished; the claim "we have headroom"
  needs proof.
- An SLO exists that no load has ever been measured against.

## Workflow

1. **Define the workload from reality** — the endpoint mix, the
   request sizes, the data shapes, the arrival pattern. A ceiling
   measured against uniform synthetic traffic is a fantasy number
   for a fantasy system.
2. **Define the bar before the test:** which metric, at which
   threshold, means "broken" — p95 over 200ms, error rate over
   0.1%. The ceiling is the load where the bar is crossed; no
   bar, no ceiling.
3. **Ramp in steps and hold each step to steady state.** Queues,
   caches, and garbage collectors take minutes to tell the truth;
   the knee hides behind the first two. A single big-bang test
   measures your load generator, not your system.
4. **Record the ceiling and the failure order.** The rate where
   the bar crosses is the ceiling; the first thing to degrade
   (connections? heap? a lock?) is what you fix or shard first
   when the ceiling must rise.
5. **Test against production shape:** production-like data
   volume, production-like infrastructure. A ceiling from a
   laptop with three rows is a unit test wearing a lab coat.
6. **Re-measure on material change.** Ceilings drift with every
   release; the number is only alive if it carries a date and a
   commit.
7. **Report honestly, then wire it:** the number with variance
   goes into the release notes; the alert near the ceiling
   belongs to `observe-the-system`.

## Red flags

- "It handled 10k rps" — no latency bar, no error budget, no
  variance.
- Load tested on dev-sized data.
- One spike test, one number, no steady state.
- Ceiling measured at launch, never again.
- The dashboard nobody ever looked at during the launch.

## Exit criteria

- Workload, bar, and ramp plan written before the run.
- Ceiling recorded: rate-at-bar, with variance, dated.
- Failure order named.
- The number attached where decisions are made — release notes,
  runbook, or capacity plan.
- A re-measure trigger defined for the next material change.
