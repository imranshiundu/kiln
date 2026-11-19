# The Field Guide — common situations, routed

The [lifecycle map](lifecycle.md) is a compass; this page is the
routes you actually walk. Ten situations that arrive at every
project, each routed through the skills that carry it — in order,
with the reason in a clause. When your situation isn't here, read
the map: classify the work, find the phase, fire the skill whose
trigger matches.

## Starting something new

`question-first` interrogates the ask until acceptance criteria
exist → `write-the-spec` compresses the agreement into one page →
`decide-with-records` pins the cross-cutting choices →
`model-the-data` and `design-the-interface` shape what will
outlive the code → `cut-thin-slices` walks the skeleton first.
Skipping ahead feels fast; the demo always bills you for it.

## Taking over an unknown repo

`read-the-codebase` traces one real request end to end before
anything is edited → `ground-truth` verifies the claims worth
building on → `review-the-work` gives the inherited state a
severity-tagged baseline → findings that survive go to the debt
ledger, not a heroic rewrite.

## A bug report arrives

`hunt-the-bug` reproduces, reduces, and root-causes before any
fix is written → `test-first` turns the reduction into the
permanent guard → `test-the-contract` pins the boundary if the
fix changed a published shape → `open-the-gates` ships the fix
small → `document-the-why` leaves the cause where the next
hunter finds it. If the incident hurt, `run-the-postmortem`
closes the loop.

## "It's slow"

`measure-then-optimize` profiles before anything is touched and
commits the numbers with the change → if the question is capacity
rather than code, `find-the-ceiling` turns "will it hold" into a
rate-at-bar with a named failure order → `observe-the-system`
wires the alert that watches the trend line.

## We ship tomorrow

`review-the-work` is the hostile pass over the whole diff →
`harden-the-edges` enumerates the boundaries one last time →
`rehearse-the-failure` executes the rollback plan that has been
sitting there, unread → `open-the-gates` versions, notes, and
stages the release.

## Production is down (or just came back)

Mitigate first — stabilize, then diagnose. `observe-the-system`
is where the answers already live (or where the finding is that
they don't) → `hunt-the-bug` finds the cause while evidence is
warm → `run-the-postmortem` converts the pain into owned action
items — blameless, or you purchase silence next time.

## The schema has to change

`model-the-data` re-states the invariants the new shape must
hold → `migrate-gently` carries the change as expand, migrate,
contract — reversible steps, counted backfills →
`test-the-contract` holds the published boundary steady across
the whole window.

## Newcomers are struggling

`guide-the-reader` separates the docs into their four modes and
verifies the first-success path by running it in a clean
environment → `document-the-why` keeps the why-docs pointed at
the decision records. A question answered in chat three times is
a doc that doesn't exist.

## A security report lands

`coordinate-the-disclosure` runs the whole arc — acknowledge
within a day, score with a method, fix in private, release patch
and advisory and credit together → `hunt-the-bug` is the
reproduce-before-fix discipline inside it → `harden-the-edges`
teaches the test suite the class of bug so it can't quietly
return.

## Dependencies are piling up

`tend-the-dependencies` tiers the updates by semver distance,
reads every changelog, and bumps in verified batches →
`test-the-contract` proves published boundaries survived →
`commit-with-care` keeps each batch one logical change, green,
with its why.

---

The pattern under all ten routes: **classify the work, fire one
craft at a time, honor its exit criteria with evidence.** The
routes are examples of the method, not a replacement for it —
when reality differs from the route, believe reality and read
the triggers.
