---
name: measure-then-optimize
description: Forces a measurement before any optimization - profile the real workload, find the actual cost, change one thing, measure again. Use when anything is slow and a fix is being proposed, guessed, or defended without numbers.
license: MIT
metadata:
  phase: verify
---

# Measure Then Optimize

## North Star

Every performance change carries its evidence with it: the profile
that chose the target, the baseline before, the number after, the
workload and machine both ran on. "Faster" is a claim with a method
attached — or it isn't made.

## When to fire

- Anything is slow, and a fix is already being proposed.
- A change is defended with "it should be faster" or "obviously it
  helps".
- The word "optimize" appears before the word "measure" has been said
  even once.
- Speed is about to be traded against clarity, and the trade is being
  priced by feeling.

## Workflow

1. **Define the target as a number.** p95 latency, throughput,
   allocations, wall time — attached to a named workload. "Make it
   faster" is not a target; "p95 under 200ms at 100 rps on the
   checkout path" is.
2. **Profile before touching anything.** Reproduce the slowness, then
   profile it — profiler, flame graph, query plan, allocator stats.
   Record where the time actually goes. Knuth's warning
   ("premature optimization is the root of all evil", 1974) is about
   optimizing without this step, and it has not expired.
3. **Name the bottleneck in one sentence.** If the profile leaves two
   candidates, measure to separate them — never guess between two
   guesses.
4. **Change one thing.** One optimization per run, so the next number
   can attribute the improvement. Gregg's systems-performance
   discipline: change, measure, compare — serially.
5. **Measure again — properly.** Same workload, same machine class,
   several runs, variance reported. A single run of a benchmark is an
   anecdote.
6. **Ship or revert by evidence.** Improvement within noise: revert
   the change and say so. "No impact" claims need numbers too —
   absence of a measurement is not absence of impact.
7. **Commit the numbers with the change** — workload, environment,
   before, after, method — in the PR or commit message. A performance
   change without its numbers is a rumor with a diff.

## Red flags

- Optimizing code the profile never named.
- Micro-optimizations against an unprofiled macro cost.
- Benchmarks run on toy inputs, once, on a laptop.
- "Faster" with no workload, no hardware, no variance.
- Complexity added permanently for a gain within the noise band.

## Exit criteria

- Baseline and after numbers, same workload, variance shown, committed
  alongside the change.
- The profile output that selected the bottleneck, named and saved.
- One change per measured delta; noise-level results reverted, with
  the revert visible in history.
