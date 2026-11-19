---
name: test-the-edges
description: Attacks the boundaries happy-path suites miss - empty, one, many, maximum, unicode, time, concurrency - with example tables and property checks that shrink failures to the smallest case. Use when a suite is green but trust is low, or inputs arrive from outside your control.
license: MIT
metadata:
  phase: verify
---

# Test the Edges

## North Star

The suite does not only prove the happy path — it holds a boundary
table for every public input and a property for every invariant,
and when a generated case breaks the system, the failure arrives
reduced to its smallest form. Green now means something.

## When to fire

- A suite is green but trust in it is low.
- Input arrives from outside your control: users, networks, files,
  clocks, other systems.
- A parser, validator, or serializer — anything with "handle any
  input" energy — is being written.
- The same class of bug keeps recurring at the same boundaries.

## Workflow

1. **Build the boundary table per public input:** empty and absent,
   one, many, maximum, negative, zero, unicode and right-to-left
   text, the largest sane value, the smallest weird one. Two
   columns: the edge, and what correct behavior is there. Decide
   the oracle first — a boundary without a defined correct answer
   is a decoration.
2. **Turn the table into named examples that live in the suite
   forever.** Each row becomes a case a future reader can learn
   the contract from.
3. **State the invariants as properties.** Round-trips return the
   original. Validation is idempotent. Sorted output never drops a
   duplicate the input kept. State the claim, then let a generator
   throw thousands of inputs at it — the QuickCheck discipline.
4. **Shrink.** When a generated case fails, reduce it to the
   minimal failing input before touching the code. A failure you
   cannot shrink is a failure you cannot fix; the smallest case is
   half the diagnosis — the same reduction as `hunt-the-bug`.
5. **Test the rejections too.** An edge the system must reject
   deserves a test asserting the rejection and its error message —
   "fails loudly and helpfully" is part of the contract.
6. **Bound the special worlds:** time (frozen, skewed, far future),
   concurrency (the same key twice, interleaved writes), locale.
   Each is an edge dressed as a context.

Craft sources: boundary value analysis from the classic testing
literature (Myers); property-based testing from QuickCheck
(Claessen and Hughes, 2000), with Hypothesis carrying the
discipline into mainstream stacks.

## Red flags

- Only "normal user" examples; zero never tested.
- Generated tests without shrinking — failures arrive as
  thousand-character blobs.
- Properties with no oracle — asserting "does not crash" and
  calling it correctness.
- Concurrency "tested" with sleeps instead of interleavings.
- Time mocked in one test and real in its neighbor.

## Exit criteria

- A boundary table committed for every public input, each row a
  named test.
- At least one property per core invariant, shrinking demonstrated
  on a seeded fault.
- Rejection paths tested with their error messages asserted.
