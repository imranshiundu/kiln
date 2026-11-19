#!/usr/bin/env python3
"""firetest.py — the Fire Test, made mechanical.

Checks every skill in skills/ against the format contract in
docs/format.md: frontmatter fields, the five-section body anatomy,
the word budget, and cross-references in README.md, AGENTS.md and
docs/lifecycle.md.

Stdlib only. Exits non-zero on any failure. Run from the repo root:

    python3 scripts/firetest.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

PHASES = {"gather", "spec", "design", "build", "verify", "ship", "tend", "meta"}
SECTIONS = ["North Star", "When to fire", "Workflow", "Red flags", "Exit criteria"]
KEBAB = re.compile(r"^[a-z]+(-[a-z]+)*$")
WORD_BUDGET = 500      # format.md: body under ~500 words
WORD_HARD_FAIL = 600   # past this, "lean" is a lie

errors = []
warnings = []


def err(skill, msg):
    errors.append(f"{skill}: {msg}")


def warn(skill, msg):
    warnings.append(f"{skill}: {msg}")


def parse_frontmatter(text):
    """Parse the strict frontmatter KILN uses: top-level `key: value`
    lines, indented continuations, and a one-level `metadata:` block."""
    if not text.startswith("---\n"):
        return None, "no frontmatter found"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "frontmatter never closes"
    block = text[4:end].splitlines()
    body = text[end + 5:]
    fm, key = {}, None
    for line in block:
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z][\w-]*:", line):  # top-level key
            key, _, value = line.partition(":")
            key, value = key.strip(), value.strip()
            fm[key] = value
        elif line.startswith("  ") and key:      # continuation or nested
            stripped = line.strip()
            if ":" in stripped and not fm[key]:
                # nested key under an empty top-level (metadata: phase:)
                nkey, _, nvalue = stripped.partition(":")
                fm[f"{key}.{nkey.strip()}"] = nvalue.strip()
            elif fm[key]:
                fm[key] += " " + stripped
            else:
                fm[key] = stripped
    return fm, body


def sentence_count(text):
    return len([s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s])


def check_skill(folder):
    name = folder.name
    path = folder / "SKILL.md"
    if not path.is_file():
        err(name, "missing SKILL.md")
        return
    extra = [p.name for p in folder.iterdir() if p.name != "SKILL.md"]
    if extra:
        err(name, f"extra files in skill folder (plain markdown only): {extra}")

    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        err(name, body)
        return

    # --- frontmatter contract ---
    if fm.get("name") != name:
        err(name, f"frontmatter name {fm.get('name')!r} != folder name {name!r}")
    if not KEBAB.match(name):
        err(name, "name is not kebab-case")
    desc = fm.get("description", "")
    if not desc:
        err(name, "missing description")
    else:
        if len(desc) > 1024:
            err(name, f"description is {len(desc)} chars (max 1024)")
        if "use when" not in desc.lower():
            err(name, "description has no 'Use when' trigger — it must be a trigger, not an abstract")
        sentences = sentence_count(desc)
        if sentences > 3:
            err(name, f"description is {sentences} sentences (two max, plus a trailing trigger clause)")
    if fm.get("license") != "MIT":
        err(name, f"license must be MIT, got {fm.get('license')!r}")
    phase = fm.get("metadata.phase", "")
    if phase not in PHASES:
        err(name, f"metadata.phase {phase!r} not one of {sorted(PHASES)}")

    # --- body anatomy: exactly the five sections, in order ---
    h2s = re.findall(r"^## (.+)$", body, re.M)
    if h2s != SECTIONS:
        err(name, f"body sections {h2s} != {SECTIONS}")

    # --- workflow: numbered steps ---
    wf = re.search(r"^## Workflow\n+(.*?)^## ", body, re.M | re.S)
    if wf and not re.search(r"^\d+\.", wf.group(1), re.M):
        err(name, "Workflow has no numbered steps — a skill is a workflow, not prose")

    # --- lean: word budget ---
    words = len(body.split())
    if words > WORD_HARD_FAIL:
        err(name, f"body is {words} words (budget ~{WORD_BUDGET}, hard fail {WORD_HARD_FAIL})")
    elif words > WORD_BUDGET:
        warn(name, f"body is {words} words (budget ~{WORD_BUDGET})")

    # --- title present, matches the craft ---
    if not re.search(r"^# (.+)$", body, re.M):
        err(name, "missing H1 title")


def check_cross_references(skill_names):
    """Every skill must appear in the README table, the AGENTS.md routing
    table, and docs/lifecycle.md — docs that drift from reality lie."""
    for doc, label in [("README.md", "README"), ("AGENTS.md", "AGENTS.md"),
                       ("docs/lifecycle.md", "lifecycle map")]:
        path = ROOT / doc
        if not path.is_file():
            warn("_repo", f"{doc} missing")
            continue
        content = path.read_text(encoding="utf-8")
        for name in skill_names:
            if name not in content:
                err(name, f"not referenced in {label}")


def main():
    if not SKILLS.is_dir():
        print("fatal: skills/ not found — run from the repo root")
        return 2
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for folder in folders:
        check_skill(folder)
    check_cross_references([f.name for f in folders])

    print(f"Fire Test: {len(folders)} skills checked")
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  FAIL  {e}")
    verdict = "ALL GREEN" if not errors else f"{len(errors)} FAILURE(S)"
    print(f"Result: {verdict}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
