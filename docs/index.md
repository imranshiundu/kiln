# The Library Index

30 crafts across the seven fires plus the meta craft. One line
each: the skill, and the door it opens on. Full workflows live in each
skill's `SKILL.md`; the map they hang on is
[lifecycle.md](lifecycle.md).

## gather — understand the terrain (3)

| Skill | Fires when |
| :- | :- |
| [`ground-truth`](../skills/ground-truth/SKILL.md) | Working in an unfamiliar codebase, using a library whose version may differ from training knowledge, or building on any claim you have not personally verified. |
| [`question-first`](../skills/question-first/SKILL.md) | A request has no acceptance criteria, could mean several materially different things, or the user says "build me X" without constraints. |
| [`read-the-codebase`](../skills/read-the-codebase/SKILL.md) | Work starts in a repository you do not know, or answers keep citing code nobody has opened. |

## spec — align on what and why (3)

| Skill | Fires when |
| :- | :- |
| [`decide-with-records`](../skills/decide-with-records/SKILL.md) | Choosing technologies, architectures, data shapes, or any decision future builders must know was deliberate. |
| [`estimate-with-ranges`](../skills/estimate-with-ranges/SKILL.md) | Anyone asks how long, how much, or whether it fits. |
| [`write-the-spec`](../skills/write-the-spec/SKILL.md) | An agreed idea is about to become implementation, a project or significant feature is starting, or requirements exist only in conversation. |

## design — model what outlives the code (2)

| Skill | Fires when |
| :- | :- |
| [`design-the-interface`](../skills/design-the-interface/SKILL.md) | An API, public function set, module boundary, plugin surface, or CLI contract is born or extended. |
| [`model-the-data`](../skills/model-the-data/SKILL.md) | Persistent state, schemas, core domain objects, or state machines take shape. |

## build — make it real, slice by slice (4)

| Skill | Fires when |
| :- | :- |
| [`commit-with-care`](../skills/commit-with-care/SKILL.md) | Committing work, a branch has become one blob before merging, or history will ever need bisecting. |
| [`cut-thin-slices`](../skills/cut-thin-slices/SKILL.md) | Implementation begins on anything bigger than a one-liner, or when work spans multiple layers or files. |
| [`make-it-accessible`](../skills/make-it-accessible/SKILL.md) | Building or changing anything a human will see, hear, or click. |
| [`test-first`](../skills/test-first/SKILL.md) | Writing logic that must not break - business rules, parsers, state machines, bug fixes - and when a behavior change needs a permanent guard. |

## verify — prove the work (6)

| Skill | Fires when |
| :- | :- |
| [`find-the-ceiling`](../skills/find-the-ceiling/SKILL.md) | The system must survive real load - a launch, a peak, an event - and someone asks whether it will hold. |
| [`hunt-the-bug`](../skills/hunt-the-bug/SKILL.md) | Behavior is wrong and the cause is unknown, an error keeps resurfacing, or a fix "didn't take". |
| [`measure-then-optimize`](../skills/measure-then-optimize/SKILL.md) | Anything is slow and a fix is being proposed, guessed, or defended without numbers. |
| [`review-the-work`](../skills/review-the-work/SKILL.md) | Work is about to be presented as complete, a milestone is claimed, or a change is about to be merged. |
| [`test-the-contract`](../skills/test-the-contract/SKILL.md) | An interface is published to consumers outside your test suite, or a boundary change is about to ship. |
| [`test-the-edges`](../skills/test-the-edges/SKILL.md) | A suite is green but trust is low, or inputs arrive from outside your control. |

## ship — face reality (5)

| Skill | Fires when |
| :- | :- |
| [`coordinate-the-disclosure`](../skills/coordinate-the-disclosure/SKILL.md) | A vulnerability report arrives, you find a flaw serious enough to disclose yourself, or an embargo clock is running. |
| [`harden-the-edges`](../skills/harden-the-edges/SKILL.md) | Work faces real users, real data, or real attackers: before launch, before handling others' data, before exposing any new endpoint or surface." |
| [`observe-the-system`](../skills/observe-the-system/SKILL.md) | A service, queue, or long-running process is being built, someone debugs by print-statement, or an incident review says "we had no way to know". |
| [`open-the-gates`](../skills/open-the-gates/SKILL.md) | A release is going out to real users, or when "just deploying this real quick" is being said. |
| [`rehearse-the-failure`](../skills/rehearse-the-failure/SKILL.md) | The system is about to face reality - a launch, a migration, a high-stakes weekend - and the rollback plan has never been executed. |

## tend — keep it alive (6)

| Skill | Fires when |
| :- | :- |
| [`document-the-why`](../skills/document-the-why/SKILL.md) | Onboarding docs are stale, a decision needs to outlive the decision-maker, or the next reader needs more than the code says. |
| [`guide-the-reader`](../skills/guide-the-reader/SKILL.md) | A user must learn the thing you built, the same question keeps getting answered in chat, or the docs mix teaching with reference into mush. |
| [`migrate-gently`](../skills/migrate-gently/SKILL.md) | A schema, model, stored format, or published interface must change while the system keeps running. |
| [`refactor-with-care`](../skills/refactor-with-care/SKILL.md) | Cleaning up code that works, renaming for clarity, or untangling structure - without any intended behavior change. |
| [`run-the-postmortem`](../skills/run-the-postmortem/SKILL.md) | An incident is over or contained, a near-miss rattled the team, or the same incident keeps coming back. |
| [`tend-the-dependencies`](../skills/tend-the-dependencies/SKILL.md) | Updates are pending, a lockfile drifts, or a major bump is being pushed through in a hurry. |

## meta — the library itself (1)

| Skill | Fires when |
| :- | :- |
| [`fire-a-skill`](../skills/fire-a-skill/SKILL.md) | A craft is missing from the library and keeps being improvised. |

---

Generated by `make index` ([`scripts/gen_index.py`](../scripts/gen_index.py))
from the same inventory the Fire Test checks. CI regenerates and diffs
this page on every push — hand edits are overwritten, by design.
