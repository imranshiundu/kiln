---
name: design-the-interface
description: Designs APIs and module boundaries contract-first - the consumer's experience before the implementation, including failure cases. Use when an API, public function set, module boundary, plugin surface, or CLI contract is born or extended.
license: MIT
metadata:
  phase: design
---

# Design the Interface

## North Star

The interface exists as a written contract with request and response
*examples* — including failure cases — designed from the consumer's
chair, and walked through by at least one real consumer before it is
frozen. The implementation is negotiable; this contract is the promise.

## When to fire

- Any new API, library surface, module boundary, CLI, or plugin contract.
- An internal function grows a second caller outside its original file.
- Consumers keep misusing an endpoint the same predictable way — that is
  the interface confessing.
- You are about to let the implementation's convenience dictate the
  consumer's experience.

## Workflow

1. **Start from the consumer's call site.** Write the code the consumer
   *wishes* existed — in their language, in their idioms. That wish is
   the design. Then work backwards.
2. **Design the happy path, then the failure paths, in writing.** For
   every operation: what does the consumer receive when the thing is
   missing, forbidden, malformed, rate-limited, or half-broken?
   Undocumented failure behavior becomes folklore, then load-bearing
   folklore.
3. **Assume Hyrum's Law.** Every observable behavior — every error
   message, ordering, and status code — will someday be depended on by
   someone. Only promise what you intend to keep. Where you must expose
   something incidental, mark it.
4. **Name for the reader who is in a hurry.** Consistent naming,
   consistent casing, consistent error shape across the whole surface.
   A booleganger (`process(skipCheck)`) deserves a name that says what it
   really wants to be.
5. **Shrink the surface.** If a consumer can construct the wrong state
   through the API, redesign so they cannot. Smallest public surface that
   covers the spec; everything else is internal until a second consumer
   proves otherwise.
6. **State the versioning stance** in one sentence: what changes are
   breaking, and what the consumer may safely rely on. "No stance" is a
   stance — the worst one.
7. **Walk one real consumer through.** Take the contract and write one
   nontrivial consumer against it, on paper or in code. Every sharp edge
   you find is an edge you no longer ship.

## Red flags

- Implementation-shaped interfaces (mirrors your internal classes,
  leaks your database's column names).
- Error handling that varies per endpoint — or per week.
- A contract documented only by its tests' incidental behavior.
- Parameters that are booleans today and will need "sometimes" next
  quarter — make the enum now, while it's cheap.

## Exit criteria

- The contract is written with concrete request/response examples for
   both success and each failure class.
- One consumer walkthrough completed and its findings folded back in.
- The versioning stance is written down.
- The public surface has no member a second reviewer couldn't justify
   keeping.
