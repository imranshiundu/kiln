---
name: hunt-the-bug
description: A four-step root-cause discipline - reproduce reliably, reduce to the smallest case, test one hypothesis at a time, fix the cause and post a permanent guard. Use when behavior is wrong and the cause is unknown, an error keeps resurfacing, or a fix "didn't take".
license: MIT
metadata:
  phase: verify
---

# Hunt the Bug

## North Star

The bug is reproduced on demand, reduced to its smallest case, explained
in one sentence of cause — not correlation — and a guard exists that
fails forever if it returns. The symptom may or may not be "fixed" yet;
the *cause* is already dead.

## When to fire

- Behavior is wrong and the cause is unknown.
- A "fixed" bug resurfaces. (It was never fixed — its symptom was
  redecorated.)
- An error report says "sometimes", "randomly", or "usually".
- You are about to change code without being able to say *why* the
  change would fix anything.

## Workflow

1. **Reproduce reliably.** Find the exact steps, data, and environment
   that make it happen. "Sometimes" means you haven't found the trigger
   yet. No reliable reproduction, no hunting — you would be shooting in
   the dark and calling it aim.
2. **Reduce.** Strip everything until the smallest possible case still
   fails — one input, one call, one config flag. The reduction is half
   the diagnosis: what you removed without killing the bug was never
   involved.
3. **Hypothesize one cause at a time.** State it as a sentence: "the
   cache never invalidates on delete." Then test *that* — with a probe,
   a log, or a targeted experiment, not with a hopeful edit. One
   hypothesis, one test, one observation. Shotgun edits that
   coincidentally make the error disappear are how bugs learn to hide.
4. **Fix the cause, not the symptom.** When the hypothesis survives its
   test, fix the mechanism — the invalidation, the race, the wrong
   invariant. Wrapping the symptom in a try/catch or a retry loop
   without understanding it is not a fix; it is a muzzle, and the bug
   still bites.
5. **Guard it.** Write the regression test from the reduction — the
   smallest case, asserting the correct behavior. Watch it fail against
   the broken code, pass against the fix. A bug without a guard is on
   its way back.
6. **Report the hunt in three lines:** trigger, cause, guard. The next
   hunter inherits your work instead of your confusion.

## Red flags

- Editing code to make an error message go away. The error was the
  messenger.
- Adding a catch-all around code whose failure you haven't explained.
- "Works on my machine" as a closing argument without a reproduction.
- Two fixes applied at once — now neither is falsifiable. One change,
  one observation, one commit.
- Declaring victory because the symptom vanished for one input. The
  reduction covers the whole class or the guard is decorative.

## Exit criteria

- Reproduction steps written down and demonstrated.
- The root cause stated in one sentence, evidenced by the probe or
  experiment that confirmed it.
- A regression test that demonstrably fails without the fix and passes
  with it, committed.
- The symptom-muzzle shortcut, if any temptation existed, explicitly
  rejected in the report.
