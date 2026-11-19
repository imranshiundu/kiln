---
name: make-it-accessible
description: Builds interfaces everyone can use - semantic structure first, complete keyboard paths, labeled controls, contrast that passes, and a real assistive-technology pass before done. Use when building or changing anything a human will see, hear, or click.
license: MIT
metadata:
  phase: build
---

# Make It Accessible

## North Star

A user with a screen reader, a keyboard, low vision, or no mouse
completes the core journey unaided — not because someone audited it
after launch, but because accessibility was part of how the
interface was built. WCAG's POUR — perceivable, operable,
understandable, robust — describes the finished thing, not a
checklist bolted on at the end.

## When to fire

- Any interface is being built or changed: a page, a form, a
  component, an email, a terminal UI.
- Someone says "we'll add accessibility before launch" — that
  sentence has never once survived contact with a launch.
- A design decision touches contrast, motion, focus, or input
  modality.

## Workflow

1. **Semantics first, styling second.** Reach for elements that
   already mean the thing — button, label, nav, table — before
   building meaning out of divs and JavaScript. Native semantics
   are free, tested by millions of sites, and survive refactors.
2. **Keyboard the whole journey.** Every action reachable by Tab
   and Enter, focus order matching reading order, nothing trapping
   the cursor, a skip link past navigation. If it cannot be done
   without a mouse, it cannot be done.
3. **Name everything.** Every control has a visible label and a
   programmatic name that agrees with it. Placeholder text is not
   a label; an icon is not a name. Where native semantics exist,
   use them — ARIA is the spare key, not the front door.
4. **Meet the measurable bars.** Text contrast 4.5:1 (3:1 for
   large text), visible focus indicators, no information carried
   by color alone, and motion that respects the reduced-motion
   setting.
5. **Announce state changes** — errors, loading, new content — so
   assistive tech hears what sighted users see. Error messages sit
   next to their fields, in text, not in a red glow.
6. **Test with real tools, both kinds.** An automated scan (axe or
   equivalent) for the mechanical misses; then a keyboard-only and
   screen-reader pass over the core journey yourself. Automated
   checks are the floor — the rest only a human running the path
   will find.

Craft sources: WCAG 2.2 (W3C); Heydon Pickering's *Inclusive
Components*; Deque's axe rule set — the rules are public, and worth
reading as engineering literature.

## Red flags

- A clickable div doing a button's job.
- Focus outlines removed for aesthetics.
- Color as the only signal of success or failure.
- Accessibility queued for a "polish phase".
- An automated scan's green checkmark treated as a pass.

## Exit criteria

- Keyboard-only completion of the core journey, demonstrated.
- A screen-reader pass over the same journey, findings fixed.
- Automated scan clean of serious and moderate findings.
- Contrast pairs measured and passing, not eyeballed.
