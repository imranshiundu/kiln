---
name: open-the-gates
description: Releases deliberately - version, user-facing notes, migration warnings, staged rollout, and a rollback plan that has been touched, not just imagined. Use when a release is going out to real users, or when "just deploying this real quick" is being said.
license: MIT
metadata:
  phase: ship
---

# Open the Gates

## North Star

The release went out and can come back. Version, notes, migration
warnings, staged rollout, and a rollback plan that has been rehearsed or
dry-run — because "smaller releases are safer releases" is not a slogan,
it's physics.

## When to fire

- Anything is being deployed for others to use.
- A breaking change, migration, or schema change is riding along.
- The phrase "just deploy it real quick" appears. That phrase deploys
  incidents.

## Workflow

1. **Freeze and name the change.** One sentence: what is in this
   release, and is it breaking? If it needs a paragraph, it's two
   releases — split them while it's still free.
2. **Write user-facing release notes** — written for the *user's*
   change: what's new, what changed, what might surprise them. "Refactored
   internals" is not a user note; "exports now include headers" is.
   Breaking changes lead the notes, in bold, with the migration step
   next to each.
3. **Confirm the gates are green:** tests, review, hardening pass —
   whatever the project's definition of done is, it ran *on this exact
   artifact*, not on the branch last Tuesday.
4. **Stage the rollout.** A canary cohort or percentage, then watch the
   signals you'd watch (errors, latency, key user actions) for long
   enough to see normal noise. If there's no staging mechanism, there's
   a feature flag; if there's neither, the rollout plan is "yolo" —
   write that down honestly and let the user decide.
5. **Rehearse the rollback before the release, not during the
   incident.** Actually touch it: what command reverts, does data
   survive the reverse migration, and who is authorized to pull the
   trigger? A rollback plan that exists only as prose is a hope with a
   filename.
6. **Watch the gates after opening.** The first real traffic is the
   first real test. Stay present for the first meaningful window; the
   most dangerous deploy is the unwatched one.
7. **Log the release:** tag, date, notes link, who shipped it. Future
   archaeologists will ask.

## Red flags

- The Friday-afternoon unattended deploy "because it's a small change"
  — small changes are the ones nobody watches.
- Migration in the same release as four features — if anything fails,
  everything's stuck together.
- Rollback by reverting the commit on a schema that already migrated.
- Release notes that only a developer of this repo could decode.

## Exit criteria

- A version tag and user-facing notes published, breaking changes
  leading with migration steps.
- Staged rollout executed (or its absence explicitly chosen by the
  user, in writing).
- Rollback demonstrated or dry-run, with the exact command and the
   data-survival answer recorded.
- Post-deploy signals checked once real traffic arrived, with
  observations noted in the release log.
