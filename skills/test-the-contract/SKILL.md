---
name: test-the-contract
description: Pins every published boundary - endpoint, event, schema, CLI flag - with a test that fails in the producer's CI when the contract breaks. Use when an interface is published to consumers outside your test suite, or a boundary change is about to ship.
license: MIT
metadata:
  phase: verify
---

# Test the Contract

## North Star

Every published boundary is pinned by a test that fails loudly, in the
producer's own CI, the moment the promise breaks — before a consumer
discovers the break in production. The contract is enforced by
machinery, not remembered by people.

## When to fire

- An endpoint, event schema, message format, CLI surface, or exported
  library API is published — anything a consumer outside your test
  suite depends on.
- A boundary change is about to ship: adding, renaming, retyping, or
  removing anything observable.
- The integration suite is slow and flaky enough that the team stopped
  trusting it — contract tests pin the same seams for a fraction of
  the cost.
- A consumer reports "your API changed" and no test failed. That
  sentence is this skill's whole reason.

## Workflow

1. **List the boundaries** from the interface design: REST and RPC
   endpoints, events and their schemas, CLI flags, exported library
   symbols. Each one gets a contract; the list is the inventory.
2. **Write each contract from the consumer's view** — the fields they
   read, the failure shapes they meet, not your internal structure.
   Hyrum's Law applies: consumers will eventually observe everything
   observable, so pin exactly what is observable. (The pattern is
   Ian Robinson's consumer-driven contracts; Fowler wrote the
   canonical sketch; Pact popularized the machinery.)
3. **Assert the whole promise per boundary:** request shape, response
   and event shape on success *and* on each error case, and the
   status or exit codes. Additive changes pass; removals, retypes,
   and narrowed enums fail.
4. **Run the contracts in the producer's CI on every PR** that touches
   the boundary. The point of the craft is who finds out first: the
   producer, in CI — not the consumer, in production.
5. **Break the promise deliberately, once.** Rename a field in the
   implementation and watch the contract fail. A contract that has
   never failed is a contract that has never been tested.
6. **When the change is genuinely breaking:** version the boundary,
   keep the old contract green through the deprecation window, and
   let the contract's diff *be* the changelog of the promise.

## Red flags

- Contracts that assert implementation details instead of published
  shape.
- Happy-path-only contracts — the error shapes are half the promise.
- A boundary change shipped without its contract changing. Nothing
  silent about a promise is good.
- End-to-end suites doing a contract's job at a hundred times the
  cost, once a week, flakily.

## Exit criteria

- The boundary inventory written down; every entry has a named
  contract test.
- The deliberate-break drill passed: a field rename shown failing the
  contract in CI, then reverted.
- Breaking changes carry a version bump, with the old version's
  contract green through deprecation.
