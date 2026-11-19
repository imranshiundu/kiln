---
name: sound-the-verify
description: Reproduces, reduces, and root-causes before any fix is applied. Use when behavior is wrong and the cause is unknown.
license: MIT
metadata:
  phase: verify
---

# Sound the Verify

## North Star

The craft is done when its exit criteria hold — observable, not
felt. This fixture exists to be broken by the test suite; its
baseline is green.

## When to fire

- The situation matches the trigger in the description.

## Workflow

1. Restate the work in one sentence.
2. Do the craft, one gate at a time.

## Red flags

- Declaring the craft complete without evidence.

## Exit criteria

- The gate held; the evidence is written down.
