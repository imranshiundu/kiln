# The KILN Vocabulary — a small glossary

KILN uses a few words in exact senses. This page pins them, so a
newcomer reads the library the way it was written.

| Word | Sense |
| :- | :- |
| **fire** | One of the seven lifecycle phases — *gather, spec, design, build, verify, ship, tend*. The kiln metaphor: everything built passes through the same fires. |
| **craft** | A skill's subject: a repeatable discipline with a finished state, not a topic or a tool preference. One craft per skill. |
| **skill** | One folder, one `SKILL.md`: frontmatter plus the five sections. The unit of installation, loading, and memory cost. |
| **phase** | The lifecycle slot a craft lives in, carried in `metadata.phase`. Where to look when work arrives. |
| **trigger** | The `Use when…` clause of a description — the concrete situations that should make an agent load the skill. The skill's door. |
| **gate** | A stopping point inside a workflow: "stop until X". Skipping a gate silently is the one sin every skill names. |
| **North Star** | The first section: the finished state in one paragraph. What done looks like before the work begins. |
| **red flag** | The recognizable smell of doing the craft badly. Agents pattern-match well; red flags are patterns. |
| **exit criteria** | The evidence required to call the craft complete. Observable — commands run, output shown, files written — or it doesn't count. |
| **receipt** | Evidence attached to a claim. "Tests pass" with the command and output is a claim with a receipt; without them it is a rumor. |
| **the Fire Test** | The six-point quality bar every skill must pass: one craft; triggerable; a workflow, not prose; evidence over claims; lean; credited. Enforced mechanically by `scripts/firetest.py`. |
| **the map** | The seven fires and their skills ([lifecycle.md](lifecycle.md)). A compass, not a rail — work loops; what the map refuses is a fire skipped silently. |
| **seam** | A boundary where code crosses a process, network, disk, or queue. Where behavior lives and breaks; where the truth is. |
| **the bar** | Short for the standard of evidence the library runs on: claims carry receipts, done means exit criteria met. |

Words are cheap; shared words are not. If a term here drifts from
its use in the skills, that is a bug — fix the drift or fix the
glossary, but not neither.
