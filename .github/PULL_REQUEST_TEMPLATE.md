<!--
The Fire Test runs in CI on this PR (python3 scripts/firetest.py).
Run it locally first; a red Fire Test is a closed PR, and that is
the point. If you changed a skill's metadata, regenerate the golden
snapshot in the same commit:

  python3 scripts/firetest.py --list --json > tests/golden/inventory.json
-->

## The craft

What repeatedly-improvised craft does this PR add or improve, and
what does "done well" look like?

## Phase

gather / spec / design / build / verify / ship / tend / meta — and
why it lives there.

## Evidence

- [ ] Fire Test green locally (`python3 scripts/firetest.py`)
- [ ] Golden snapshot regenerated if skill metadata changed
- [ ] For a new skill: a transcript (trimmed) of it firing in a real
      session — and of it staying silent in a session where it
      shouldn't fire
- [ ] For a change to an existing skill: what got tighter, and what
      stayed the same

## Sources

The books, papers, libraries, or practice the craft distills.
