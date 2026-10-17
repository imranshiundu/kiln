# The Seven Fires — KILN's Lifecycle Map

Every whole thing — an app, a service, a library, a side project — passes
through the same fires. This map is KILN's spine: every skill hangs on one
of these phases, and the map is how you know which skill is missing.

```
 GATHER ──▶ SPEC ──▶ DESIGN ──▶ BUILD ──▶ VERIFY ──▶ SHIP ──▶ TEND
 (clay)   (wedge)   (shape)    (fire)   (sound)   (open)   (keep)
```

The map is a compass, not a rail. Real work loops: a bug found in `ship`
sends you back to `hunt-the-bug`; a spec that keeps changing means
`question-first` never finished. The only real failure is skipping a fire
*silently* — doing the work without the craft the phase demands.

---

## 1. GATHER — the clay

**Purpose.** Understand the terrain before you shape anything: what is
actually being asked, and what is actually true.

**Inputs.** A request, a codebase, a claim, an idea.

**Outputs.** A confirmed problem statement with testable acceptance
criteria; a context brief separating what is verified from what is assumed.

**Skills.** `question-first`, `ground-truth`

**The smell of skipping it.** The first demo reveals the user wanted a
different thing entirely; the code was written against a library API that
stopped existing two major versions ago.

## 2. SPEC — the wedge

**Purpose.** Align on what will be built and why — in writing, briefly,
before code makes the design expensive to change.

**Inputs.** A confirmed problem statement.

**Outputs.** A one-page spec (problem, users, non-goals, acceptance
criteria); decision records for the choices that shape everything after.

**Skills.** `write-the-spec`, `decide-with-records`

**The smell of skipping it.** "Scope creep" that was really always the
requirements; two contributors building toward different invisible specs;
decisions re-litigated weekly because nobody remembers why they were made.

## 3. DESIGN — the shape

**Purpose.** Model the things that outlive the code: the data, the
interfaces. Code is rewritten constantly; data and public contracts are
nearly impossible to rewrite.

**Inputs.** The spec; the decision records.

**Outputs.** Entities, relations, invariants, and a migration story; a
contract-first interface design with failure cases, not just happy paths.

**Skills.** `model-the-data`, `design-the-interface`

**The smell of skipping it.** The schema can't answer a question the UI
obviously needs; every consumer of the API discovers a different wrong
behavior for the same error.

## 4. BUILD — the fire

**Purpose.** Make it real, slice by slice, with the safety net woven
before the acrobatics.

**Inputs.** The spec, the design, the ground-truth brief.

**Outputs.** A walking skeleton, then a sequence of thin vertical slices —
each demonstrably working, each a safe rollback point. Logic that must not
break, guarded by tests written before it.

**Skills.** `cut-thin-slices`, `test-first`

**The smell of skipping it.** Three weeks of "80% done" with nothing that
runs; a green checkmark that tests nothing; the integration scheduled for
the last day, as a surprise for everyone.

## 5. VERIFY — the sound

**Purpose.** Prove the work: find what's actually wrong, review what was
actually built — not what you remember building.

**Inputs.** Slices that claim to work.

**Outputs.** Reproduced, root-caused, regression-guarded bug fixes; a
review pass with findings tagged by severity and claims verified by
commands.

**Skills.** `hunt-the-bug`, `review-the-work`

**The smell of skipping it.** "It should work" as a status; bugs that get
re-closed twice; the diff reviewed by the same attention that wrote it,
which is to say, not reviewed.

## 6. SHIP — the opening

**Purpose.** Put the work in front of reality — real users, real data,
real adversaries — in a way it can survive and come back from.

**Inputs.** Verified work.

**Outputs.** Hardened boundaries; a versioned release with user-facing
notes, a staged rollout, and a rollback plan that has actually been
touched.

**Skills.** `harden-the-edges`, `open-the-gates`

**The smell of skipping it.** The Friday 5pm deploy "because it's a small
change"; secrets committed temporarily; the first user finding the first
vulnerability before they find the feature.

## 7. TEND — the keeping

**Purpose.** Keep the thing alive and comprehensible: improve structure
without changing behavior, and leave behind more understanding than you
found.

**Inputs.** Software running in reality.

**Outputs.** Behavior-preserving refactors with green tests on both sides
of the change; documentation that answers *why* for the reader who arrives
at 2am during an incident.

**Skills.** `refactor-with-care`, `document-the-why`

**The smell of skipping it.** The rewrite-in-place nobody asked for, mixing
"cleanup" with behavior changes; comments that narrate the code instead of
explaining it; a README whose setup instructions haven't worked since v0.3.

---

## Why seven

Fewer phases and crafts fall through the cracks. The map is deliberately
tool- and stack-agnostic: whether you build in Rust, Rails, or React, data
still needs modeling, edges still need hardening, and done still needs
evidence. When a new craft can't honestly live under one of these phases,
the map itself is wrong — say so, and propose the change.
