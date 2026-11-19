#!/usr/bin/env bash
# tests/run.sh — prove the Fire Test can fail.
#
# A checker that cannot fail is a rubber stamp. This suite builds a
# tiny valid library (tests/fixtures/mini), then breaks it one way at
# a time and asserts the Fire Test catches each break with the right
# complaint. Run from the repo root:  bash tests/run.sh
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
FIRETEST="$REPO/scripts/firetest.py"
MINI="$HERE/fixtures/mini"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

pass=0; fail=0

fresh_copy() {
  rm -rf "$WORK/lib"
  cp -r "$MINI" "$WORK/lib"
}

# expect_fail <label> <expected-substring> <python-mutation>
# The mutation runs with $WORK/lib bound to a pathlib Path "root".
expect_fail() {
  local label="$1"; local expect="$2"; local mutate="$3"
  fresh_copy
  python3 - "$WORK/lib" <<PYEOF
import sys
from pathlib import Path
root = Path(sys.argv[1])
$mutate
PYEOF
  local out
  out="$(python3 "$FIRETEST" --root "$WORK/lib" 2>&1)"
  if echo "$out" | grep -q "$expect"; then
    pass=$((pass + 1)); echo "  PASS: $label"
  else
    fail=$((fail + 1)); echo "  FAIL: $label — expected '$expect' in:"; echo "$out" | sed 's/^/        /'
  fi
}

# --- the baseline must be green, or every other result is a lie ---
fresh_copy
if python3 "$FIRETEST" --root "$WORK/lib" > /dev/null 2>&1; then
  pass=$((pass + 1)); echo "  PASS: baseline mini library is green"
else
  echo "  FAIL: baseline mini library is not green — fix fixtures first"
  python3 "$FIRETEST" --root "$WORK/lib"
  exit 1
fi

# --- one mutation per contract clause ---

expect_fail "name/folder mismatch" "name 'mini-skill' != folder" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
s.write_text(s.read_text().replace("name: ask-the-question", "name: mini-skill"))'

expect_fail "description without a trigger" "no 'Use when' trigger" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
s.write_text(s.read_text().replace("Use when", "Fires whenever"))'

expect_fail "unknown phase" "not one of" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
s.write_text(s.read_text().replace("phase: gather", "phase: banana"))'

expect_fail "sections out of order" "body sections" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
t = s.read_text().replace("## North Star", "## Northstar").replace("## Exit criteria", "## North Star").replace("## Northstar", "## Exit criteria")
s.write_text(t)'

expect_fail "workflow without numbered steps" "no numbered steps" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
t = s.read_text().replace("1. Restate", "First, restate").replace("2. Do the craft", "Then do the craft")
s.write_text(t)'

expect_fail "body over the hard budget" "hard fail" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
t = s.read_text().replace("## Exit criteria", "## Exit criteria\n\n" + ("word " * 560))
s.write_text(t)'

expect_fail "missing H1" "missing H1 title" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
s.write_text(s.read_text().replace("# Ask the Question", ""))'

expect_fail "title no longer carries the name" "does not carry the name" \
's = root / "skills" / "ask-the-question" / "SKILL.md"
s.write_text(s.read_text().replace("# Ask the Question", "# The Interview"))'

expect_fail "duplicate trigger openings" "routing needs distinct doors" \
'import shutil
src = root / "skills" / "ask-the-question"
dst = root / "skills" / "interview-the-user"
shutil.copytree(src, dst)
d = dst / "SKILL.md"
d.write_text(d.read_text().replace("ask-the-question", "interview-the-user").replace("# Ask the Question", "# Interview the User"))
for doc in ["README.md", "AGENTS.md", "docs/lifecycle.md"]:
    p = root / doc
    p.write_text(p.read_text().replace("ask-the-question", "ask-the-question, interview-the-user"))'

expect_fail "an empty phase" "empty fire" \
'import shutil
shutil.rmtree(root / "skills" / "open-the-release")
for doc in ["README.md", "AGENTS.md", "docs/lifecycle.md"]:
    p = root / doc
    p.write_text(p.read_text().replace("open-the-release", "harden-the-boundary"))'

expect_fail "skill missing from the indexes" "not referenced in" \
'p = root / "README.md"
p.write_text(p.read_text().replace("open-the-release", "harden-the-boundary"))'

expect_fail "extra files in a skill folder" "extra files" \
'(root / "skills" / "ask-the-question" / "helper.sh").write_text("# not allowed\n")'

# --- strict mode turns an over-budget body into a failure ---
fresh_copy
python3 - "$WORK/lib" <<'PYEOF'
import sys
from pathlib import Path
s = Path(sys.argv[1]) / "skills" / "ask-the-question" / "SKILL.md"
s.write_text(s.read_text().replace("## Exit criteria", "## Exit criteria\n\n" + ("word " * 420)))
PYEOF
if python3 "$FIRETEST" --root "$WORK/lib" > /dev/null 2>&1; then
  if python3 "$FIRETEST" --strict --root "$WORK/lib" > /dev/null 2>&1; then
    fail=$((fail + 1)); echo "  FAIL: strict mode lets an over-budget body pass"
  else
    pass=$((pass + 1)); echo "  PASS: strict mode fails an over-budget body"
  fi
else
  fail=$((fail + 1)); echo "  FAIL: soft mode rejected a 580-word body (should warn, not fail)"
fi

# --- golden inventory: metadata drift must be a conscious act ---
if python3 "$FIRETEST" --list --json > "$WORK/inventory.json" 2>/dev/null; then
  if diff -u "$HERE/golden/inventory.json" "$WORK/inventory.json" > "$WORK/diff.txt"; then
    pass=$((pass + 1)); echo "  PASS: inventory matches the golden snapshot"
  else
    fail=$((fail + 1)); echo "  FAIL: inventory drifted from the golden snapshot — skills changed without regenerating it:"
    sed 's/^/        /' "$WORK/diff.txt" | head -20
    echo "        regenerate with: python3 scripts/firetest.py --list --json > tests/golden/inventory.json"
  fi
else
  fail=$((fail + 1)); echo "  FAIL: --list --json did not run"
fi

echo ""
echo "checker tests: $pass passed, $fail failed"
[ "$fail" -eq 0 ]
