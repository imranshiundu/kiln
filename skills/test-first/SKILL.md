---
name: test-first
description: Drives logic with red-green-refactor - write the failing test, watch it fail, write the minimal code to pass, refactor under the safety net. Use when writing logic that must not break - business rules, parsers, state machines, bug fixes - and when a behavior change needs a permanent guard.
license: MIT
metadata:
  phase: build
---

# Test First

## North Star

The behavior exists twice: once as a failing test that names it, then
once as code that makes it pass. Every behavior you must not break is
guarded by a test that fails if it breaks — and the suite says so in
seconds, forever.

## When to fire

- Writing business logic, data transforms, parsers, or state machines.
- Fixing any bug that must never return (the guard is part of the fix).
- Changing behavior whose regression would be embarrassing or expensive.
- You are about to write code *and then* tests "to be safe" — stop;
  you're about to test your implementation instead of your intent.

## Workflow

1. **Write one failing test** that names the behavior in plain words:
   `withdraw_more_than_balance_is_rejected`. Not `test_utils_2`.
2. **Watch it fail.** Run it. A test you haven't watched fail can't
   prove it tests anything — it may be passing for the wrong reason.
   This step is the whole discipline; skipping it turns TDD into
   superstition.
3. **Write the minimal code that passes.** Resist the adjacent
   refactor, the "while I'm here" feature. The test says what's needed;
   nothing else is needed yet.
4. **Run it green.** All of it — the new test and the whole suite.
5. **Refactor under the net.** Now improve names, remove duplication,
   simplify. The green suite is what makes the refactor honest. Stop
   when the suite is green and the shame is gone.
6. **Test behavior, not implementation.** Call the public surface the
   way a consumer would. A test coupled to internals breaks on every
   refactor and guards nothing.
7. **Choose the test's altitude deliberately.** Many unit tests for
   logic, some integration tests for seams, a few end-to-end tests for
   the paths users actually take. The pyramid is a budget, not a
   religion — but inverted pyramids (everything E2E) are how suites
   become slow enough to be skipped.
8. **Know the honest exceptions.** Exploratory spikes, throwaway
   prototypes, and pure visual tweaks may not deserve tests first — but
   the moment a spike graduates into real code, it gets a failing test
   *retroactively*, before its next change.

## Red flags

- Tests written after the code "for coverage" — they encode whatever
  the code does, bugs included.
- A failing test deleted or skipped to go green. That is the guard
  falling so the alarm would stop.
- Tests asserting private internals, call counts, or mock invocation
  theater.
- A suite so slow nobody runs it. Slow is a bug in the suite.

## Exit criteria

- For each behavior: evidence of the test failing (before) and the
  suite passing (after).
- The regression guard for any bug fix is committed in the same change
  as the fix.
- The suite runs green in one command, and you ran it — the last run's
  output is in the record.
