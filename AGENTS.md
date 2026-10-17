# KILN — Operating Doctrine for Agents

You have been pointed at (or installed) KILN. This file is your operating
manual. Read it once, then work by it.

## What you are holding

KILN is a library of crafts — one craft per `SKILL.md` — that together cover
the whole lifecycle of building software:

```
GATHER -> SPEC -> DESIGN -> BUILD -> VERIFY -> SHIP -> TEND
```

Each skill is a workflow with gates and evidence requirements, not an essay.
Skills are small on purpose: they load only when fired, so they cost almost
nothing until you need them.

## The operating loop

1. **Classify.** Look at the work in front of you. Which phase is it in?
   A request with no acceptance criteria is `gather` work. A verified fix
   about to be called done is `verify` work. Most tasks arrive mid-lifecycle —
   start where the work actually is, not at the beginning of the world.

2. **Find the skill.** Route by phase, then by the skill's `description`:

   | Phase | Skill | Fires when |
   | :- | :- | :- |
   | gather | `question-first` | the ask is vague or has no acceptance criteria |
   | gather | `ground-truth` | you must build on code, APIs, or claims you haven't verified |
   | spec | `write-the-spec` | an agreed idea needs to become a build contract |
   | spec | `decide-with-records` | a cross-cutting choice must be made once and recorded |
   | design | `model-the-data` | persistent state, entities, or invariants take shape |
   | design | `design-the-interface` | an API, module boundary, or public surface is born |
   | build | `cut-thin-slices` | implementation begins on anything bigger than a one-liner |
   | build | `test-first` | you are writing logic that must not break |
   | verify | `hunt-the-bug` | behavior is wrong and the cause is unknown |
   | verify | `review-the-work` | work is about to be presented as done |
   | ship | `harden-the-edges` | the work faces real users, real data, real attackers |
   | ship | `open-the-gates` | a release must go out and come back safely |
   | tend | `refactor-with-care` | structure improves without behavior changing |
   | tend | `document-the-why` | the next reader needs more than the code says |
   | meta | `fire-a-skill` | KILN itself needs a new skill |

3. **Fire it.** Load that skill's `SKILL.md` and follow its workflow exactly.
   One skill at a time. If two skills apply, run them in the order the
   lifecycle suggests.

4. **Honor the exit criteria.** A skill is not complete when you feel done;
   it is complete when its exit criteria are met *with evidence* — commands
   run, output shown, artifacts written.

## Rules of engagement

- **One craft at a time.** Load a skill, do the craft, move on. Do not hoard
  skills in context.
- **No silent phase-skipping.** You may be asked to jump straight to `build`.
  Comply — but name what is being skipped and what risk it carries, in one
  sentence.
- **Evidence over claims.** "Tests pass" means you ran them. "It works" means
  you saw it work. Never report a state you did not observe.
- **The skill is the floor, not the ceiling.** Follow the workflow; add your
  own judgment on top of it.
- **No invented skills.** If no skill fits the work, do the work plainly and
  say which craft was missing. If it is a craft KILN should have, say so —
  `fire-a-skill` describes how to propose it.
- **Respect the user's stack.** KILN is deliberately tool-agnostic. Never
  let a skill push a framework, library, or vendor the user didn't choose.

## When you are the one extending KILN

To author or modify a skill, read `docs/format.md` (the format and its
quality bar), then follow `skills/fire-a-skill/SKILL.md` end to end.

## The one-line summary

Build like a potter: understand the clay, shape it thin, fire it hot, and
never call it done until you have held the finished thing in your hands.
