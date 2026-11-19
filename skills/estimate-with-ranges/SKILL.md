---
name: estimate-with-ranges
description: Estimates as evidence-backed ranges with stated confidence - decomposed, anchored on comparable history, re-estimated as evidence lands, drift reported the day it appears. Use when anyone asks how long, how much, or whether it fits.
license: MIT
metadata:
  phase: spec
---

# Estimate with Ranges

## North Star

Estimates are ranges with confidence and named assumptions — used
for decisions, never mistaken for promises. When reality diverges,
the divergence is reported the day it is known, not discovered at
the deadline. Nobody is surprised; that is the entire craft.

## When to fire

- Anyone asks how long, how much, or whether it fits.
- A plan is being built whose dates will be repeated upward
  unchanged.
- Scope is still moving — and someone wants a number anyway.

## Workflow

1. **Decompose until pieces are comparable** to work the team has
   already done. Estimation by analogy is the only method with a
   track record; estimation by optimism has a track record too.
2. **Anchor on history, not hope.** Find the similar past work and
   what it actually took. If nothing comparable exists, that fact
   is the estimate's first line: unknown territory, wider range.
3. **Give a range with explicit confidence.** "Two to four days,
   nine times out of ten" or "six weeks at P50, eleven at P90". A
   single-point estimate is a range with the uncertainty hidden
   inside it — the one place uncertainty must never be.
4. **Name the assumptions.** What the estimate believes about scope,
   dependencies, and the world. Assumptions are the failure points;
   an estimate without them cannot be wrong until it is too late,
   which is worse.
5. **Re-estimate at every milestone.** The cone of uncertainty
   narrows only when fed with real evidence; each finished slice is
   evidence. McConnell's *Software Estimation* is the full
   treatment — the cone is Boehm's.
6. **Keep estimate and commitment separate.** The estimate informs
   the commitment; the deadline is a decision made with the range
   on the table. Collapsing the two is how ranges become lies.

## Red flags

- A single date with no confidence and no assumptions.
- Padding smuggled into the number instead of stated as risk.
- The estimate that conveniently matches the deadline it was
  asked after.
- Silence as scope grows past what was estimated.
- Treating an early range as a promise, then shooting the
  messenger.

## Exit criteria

- Range and confidence recorded where the team can see them.
- Assumptions listed alongside, each one checkable.
- Decomposition and historical anchors shown, not implied.
- Re-estimates logged as milestones land; drift reported the day
  it is found.
