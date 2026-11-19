---
name: migrate-gently
description: Evolves persistent data and interfaces in reversible steps - expand, migrate, contract - so no change can lose data or strand consumers. Use when a schema, model, stored format, or published interface must change while the system keeps running.
license: MIT
metadata:
  phase: tend
---

# Migrate Gently

## North Star

Data and interfaces evolve without a big-bang moment: each step
reversible, no window where data can be lost or a consumer stranded,
and rollback is a rehearsed plan, not a hope. The scary change arrives
as a sequence of boring ones.

## When to fire

- A schema, stored format, data model, or persistent interface must
  change while the system keeps serving.
- A migration is proposed that renames, retypes, or backfills in one
  step — or worse, drops the old shape in the same breath.
- Two versions of the data must coexist: rolling deploys, offline
  clients, replayed events.
- The rollback plan is "restore from backup". Backup is data loss with
  extra steps.

## Workflow

1. **Write the invariant first:** what must be true of the data
   before, during, and after — no orphaned rows, no lost writes,
   every record readable by exactly one live shape. The migration is
   judged against this invariant, not against "it ran".
2. **Expand.** Add the new shape alongside the old — new column, new
   table, new event field, new endpoint — and write to both while
   reading the new with fallback to the old. Nothing is removed, so
   nothing can break. Gate: old readers and writers still pass their
   tests.
3. **Migrate the existing data in small, resumable batches.** The
   backfill runs while traffic is live, is idempotent (safe to re-run),
   and ends with a count that adds up: rows in, rows migrated, rows
   verified — equal.
4. **Contract, in three separate deploys.** Switch readers to the new
   shape one at a time behind a flag; watch; then stop the old writes;
   then, only then, remove the old shape. This is Danilo Sato's
   expand-migrate-contract and Fowler's Parallel Change — the naming
   is theirs; the bruises that taught it are everyone's.
5. **Keep the old shape for one full release window** before dropping
   it. Rollback during that window is "flip the flag back" — and it
   must actually work: rehearse it on staging or a production copy
   once, with evidence.
6. **Drop only on zero.** Remove the old shape when monitoring shows
   zero old-shape reads and writes across the entire window — not
   when it feels quiet.

## Red flags

- One migration that renames, retypes, and backfills in a single
  transaction.
- A backfill without a count check, or one that takes a long lock on
  a live table.
- Dropping the old shape in the same release that added the new one.
- Destructive SQL written by hand, unreviewed, on a Friday.

## Exit criteria

- The steps committed separately — expand, migrate, contract — each
  revertible on its own.
- The rollback rehearsed: one flag-flip on staging shown restoring
  the previous behavior.
- The count check recorded: N in, N migrated, N verified.
- Old shape removed only with a link to the zero-usage evidence.
