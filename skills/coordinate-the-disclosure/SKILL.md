---
name: coordinate-the-disclosure
description: Handles an inbound vulnerability report as a coordinated disclosure - fast acknowledgment, method-scored severity, fix and advisory built in private, released together with credit on an agreed date. Use when a vulnerability report arrives, you find a flaw serious enough to disclose yourself, or an embargo clock is running.
license: MIT
metadata:
  phase: ship
---

# Coordinate the Disclosure

## North Star

A report arrived and became a handled disclosure: acknowledged
within a day, severity scored with a method, fix and advisory
built in private, released together — patch, advisory, and credit
on the same day — with the reporter thanked and users told what
to do. Nothing about it was improvised under pressure.

## When to fire

- A vulnerability report arrives — security@, a private channel,
  a GitHub security advisory.
- You found something serious in your own system and must
  disclose it responsibly.
- An embargo is running and the clock is loud.

## Workflow

1. **Acknowledge within a day, before you understand the bug.**
   Reporters volunteer their time; silence tells them the channel
   is dead — and the next report goes public first. (CERT's CVD
   guidance: contact is the first move.)
2. **Score severity with a method, not adrenaline** —
   exploitability, exposure, impact, on a named scale. The score
   sets the clock: fix-and-publish in days or weeks, not vibes.
3. **Reproduce before fixing** — the `hunt-the-bug` discipline; a
   patch for an unreproducible report is a guess wearing a
   changelog entry.
4. **Fix in private:** minimal diff, regression test included,
   advisory drafted alongside — affected versions, what breaks,
   the workaround users can apply today.
5. **Agree the embargo date with the reporter** — commonly 90
   days from the report — and hold it or renegotiate in writing,
   never silently.
6. **Release in one coordinated move:** ship the fix, publish the
   advisory, credit the reporter — the same day. The gap between
   patch and advisory is where users get hurt.
7. **After publication:** watch for exploitation, answer the
   questions, and teach the test suite the class of bug so it
   cannot quietly return.

## Red flags

- Silence as triage.
- Fixing in the public repo before release — showing exploiters
  the door before locking it.
- "Fixed an issue" advisories: users cannot act on politeness.
- Credit forgotten after the reporter's work was used.
- Whoever saw the email first became the incident commander.

## Exit criteria

- Acknowledgment timestamped within a day of the report.
- Severity scored on a named method, recorded.
- Fix merged with a regression test, private until release.
- Advisory published with affected versions, workaround, credit.
- Embargo honored or renegotiated in writing.
