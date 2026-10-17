---
name: model-the-data
description: Designs entities, relationships, lifecycle states, and invariants on paper before code - because data outlives every implementation of it. Use when persistent state, schemas, core domain objects, or state machines take shape.
license: MIT
metadata:
  phase: design
---

# Model the Data

## North Star

The data design exists written down — entities, relationships, lifecycles,
invariants, and the migration story — and it answers questions the UI
hasn't asked yet. Code will be rewritten five times; this shape will be
migrated in production at 3am. It deserves better than being discovered
incrementally by accident.

## When to fire

- A new database, schema, file format, or core domain object is being
  defined.
- Entities acquire new fields, states, or relationships.
- Behavior keeps tripping over "what if it's in two states at once".
- You are about to derive the data model from the current screen design.

## Workflow

1. **List the entities as nouns** from the spec and name them precisely.
   Naming is the first design act: a name that needs a footnote is a
   wrong name.
2. **State each relationship with its cardinality and ownership** —
   who holds the foreign key, what happens to the child when the parent
   goes away.
3. **Draw the lifecycle of each entity** — states as a machine
   (`draft → published → archived`), with the events that transition
   them. Every state must be reachable and must be able to end.
   Stringly-typed state fields with no machine behind them are how
   impossible states become production incidents.
4. **Write the invariants** — the statements that must always be true
   ("a published item always has an owner"; "balance never negative").
   For each: where is it enforced? If the answer is "nowhere", that is
   the finding.
5. **Query-first sanity check.** Write the three queries the UI will
   actually run — the list view, the search, the aggregate — against the
   model on paper. If they need three joins across two denormalized
   hops, reshape now, while reshaping is cheap.
6. **Plan the first migration.** How does today's data (even "no data")
   become this shape? What does version two of this model do to version
   one's data? A model with no migration story is a demo, not a design.
7. **Write it down** — a `docs/data-model.md` sketch or the migration
   file itself, reviewed before the code that populates it.

## Red flags

- Modeling from the UI's current shape — screens churn; the data is what
  remains.
- Entities with one giant "status" string and no defined transitions.
- Invariants enforced only by application code that one bad script can
  sidestep.
- Booleans pretending to be states (`isActive`, `isArchived`, `isDeleted`
  all true at once).

## Exit criteria

- Entities, relationships, lifecycles, and invariants written down and
  reviewed before implementation.
- The three load-bearing queries checked on paper against the model.
- The first migration story exists — even if the answer is "drop and
  recreate, because we have zero users and a time machine".
