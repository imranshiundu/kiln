#!/usr/bin/env python3
"""Build the mini fixture library — a tiny valid KILN used by tests/run.sh.

Seven skills, one per phase, each passing every check. The test suite
mutates copies of this library and asserts the Fire Test catches it.
"""
from pathlib import Path

MINI = Path(__file__).resolve().parent / "fixtures" / "mini"

SKILLS = {
    "ask-the-question": ("gather", "Ask the Question",
        "Turns a vague request into testable acceptance criteria, one question at a time. "
        "Use when a request arrives with no definition of done."),
    "wedge-the-spec": ("spec", "Wedge the Spec",
        "Compresses an agreed idea into a one-page build contract with non-goals. "
        "Use when an idea has been agreed and code is about to be written."),
    "shape-the-design": ("design", "Shape the Design",
        "Models the entities, relations, and invariants that outlive the code. "
        "Use when persistent state or a public boundary is taking shape."),
    "fire-the-build": ("build", "Fire the Build",
        "Implements in thin vertical slices, each demonstrably working. "
        "Use when implementation starts on anything bigger than a one-liner."),
    "sound-the-verify": ("verify", "Sound the Verify",
        "Reproduces, reduces, and root-causes before any fix is applied. "
        "Use when behavior is wrong and the cause is unknown."),
    "open-the-release": ("ship", "Open the Release",
        "Ships deliberately - versioned, noted, staged, reversible. "
        "Use when verified work is about to meet real users."),
    "keep-the-tend": ("tend", "Keep the Tend",
        "Improves structure and documentation without changing behavior. "
        "Use when the system must stay alive and comprehensible."),
}

for name, (phase, title, description) in SKILLS.items():
    folder = MINI / "skills" / name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "SKILL.md").write_text(f"""---
name: {name}
description: {description}
license: MIT
metadata:
  phase: {phase}
---

# {title}

## North Star

The craft is done when its exit criteria hold — observable, not
felt. This fixture exists to be broken by the test suite; its
baseline is green.

## When to fire

- The situation matches the trigger in the description.

## Workflow

1. Restate the work in one sentence.
2. Do the craft, one gate at a time.

## Red flags

- Declaring the craft complete without evidence.

## Exit criteria

- The gate held; the evidence is written down.
""")

names = ", ".join(f"`{n}`" for n in SKILLS)
table = "\n".join(
    f"| {phase} | `{n}` | its trigger fires |"
    for n, (phase, _, _) in SKILLS.items())

(MINI / "README.md").write_text(f"""# Mini

Fixture library for the checker tests. All skills: {names}.

| Phase | Skill | Fires when |
| :- | :- | :- |
{table}
""")

(MINI / "AGENTS.md").write_text(f"""# Mini doctrine

Routing: {names}.
""")

(MINI / "docs").mkdir(exist_ok=True)
(MINI / "docs" / "lifecycle.md").write_text(f"""# Mini lifecycle

Phases and their skills: {names}.
""")

print(f"mini library built: {len(SKILLS)} skills, all phases crewed")
