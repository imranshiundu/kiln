# Contributing to KILN

KILN accepts crafts, not opinions with formatting. The bar is the
[Fire Test](docs/format.md#the-fire-test), and it applies to everyone —
including maintainers.

## Before you write anything

1. **Read [`docs/format.md`](docs/format.md).** The format is the roots;
   a PR that fights the format is a PR that will close.
2. **Check the map.** Does your craft already exist here? Does it exist
   in [superpowers](https://github.com/obra/superpowers),
   [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills),
   or the [skills.sh](https://skills.sh) directory? If yes, link it in
   your PR — KILN would rather credit and point than duplicate.
3. **Ask first for new phases.** Adding a skill under an existing phase is
   fair game. Adding an eight phase is a design discussion — open an
   issue.

## The path of a skill

Follow [`skills/fire-a-skill/SKILL.md`](skills/fire-a-skill/SKILL.md)
yourself — it is the contribution process, written as the very craft it
describes:

1. One craft. If the name needs an "and", split it.
2. Write the `description` as a trigger (see
   [format.md](docs/format.md#frontmatter-contract)).
3. Five sections: North Star, When to fire, Workflow, Red flags, Exit
   criteria.
4. Body under ~500 words. Cut prose, keep steps.
5. Credit your sources in the body.
6. Test it live: run a real agent session where the skill fires, and one
   where it doesn't. Include both transcripts (trimmed) in the PR.

## PR expectations

- One skill per PR (or a docs change).
- The PR description answers: *what craft is this, which phase, what does
  it replace or add, where did the craft come from?*
- Include evidence of the skill firing — a transcript, a screenshot, a
  session log. A skill that has never fired in a real agent is a draft.

## Improving existing skills

Tightening an existing skill is the most welcome contribution of all —
a removed sentence is a per-turn cost cut for every future load. Keep
the exit criteria, keep the gates, cut everything else that survives the
cut.

## Code of conduct

Be a good kiln-mate: assume competence, argue from sources, and treat
every maintainer's time as the scarce resource it is.

## License

By contributing you agree your work ships under the repo's
[MIT license](LICENSE).
