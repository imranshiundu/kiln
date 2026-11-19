---
name: run-the-postmortem
description: Turns a finished incident into an owned learning loop - evidence-built timeline, blameless language, trigger separated from contributing factors, and action items with owners and dates. Use when an incident is over or contained, a near-miss rattled the team, or the same incident keeps coming back.
license: MIT
metadata:
  phase: tend
---

# Run the Postmortem

## North Star

The incident has been converted into an asset: a timeline built
from evidence, the factors that let it hurt — separated from what
merely set it off — and a short list of owned, dated action items.
The same class of incident cannot return silently, because last
time people were paid for the truth, not punished for it.

## When to fire

- An incident is contained or resolved — write it while it's warm.
- A near-miss came close enough to rattle someone.
- The same incident, or its cousin, arrives a third time.
- The last postmortem's action items were never reviewed.

## Workflow

1. **Write it blameless, from the first line.** Everyone acted
   reasonably given what they knew, saw, and had. Blame a person
   and you purchase silence next time — silence is how incidents
   compound. (Etsy's blameless postmortems; the SRE book's
   postmortem culture.)
2. **Build the timeline from artifacts** — alerts, logs, chats,
   timestamps. Memory smooths over exactly the minutes you need.
3. **Separate the trigger from the causes.** The trigger started
   the incident; the contributing factors made it hurt. "The
   deploy triggered it" is one line of the story, not the story.
4. **Interrogate the three properties:** what made it
   *detectable* (or slow to detect), *impactful* (or contained),
   and *recoverable* (or slow to recover)? Each answer is a
   factor.
5. **Action items: few, owned, dated, specific.** Each factor
   gets at most one item; "improve monitoring" is a confession,
   not an item. An item with no owner and no date is a wish.
6. **Review the previous postmortem's items before closing** —
   recurring incidents are unpaid invoices. If an item wasn't
   done, that fact is a finding too.
7. **Publish it** where the team can read it, and to affected
   users where trust demands it.

## Red flags

- "Human error" written as a cause. It's a symptom; ask what made
  the error possible and reasonable at the time.
- Names in fault positions; heroes in save positions.
- A timeline reconstructed from memory in a hallway.
- Action items that are all monitoring-shaped because monitoring
  is easiest to write down.
- The postmortem filed and never read again.

## Exit criteria

- Timeline citing artifacts, with timestamps.
- Trigger and contributing factors listed separately.
- Every factor carries an owned, dated action item — or a stated
  decision not to act.
- Blameless language verified by a second reader.
- The previous postmortem's items reviewed; overdue ones surfaced.
