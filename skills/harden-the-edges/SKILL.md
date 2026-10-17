---
name: harden-the-edges
description: "A security pass that enumerates every boundary - input, output, storage, privilege - and checks each one deliberately instead of hoping. Use when work faces real users, real data, or real attackers: before launch, before handling others' data, before exposing any new endpoint or surface."
license: MIT
metadata:
  phase: ship
---

# Harden the Edges

## North Star

Every boundary of the system — every place data crosses from the outside
world in, or from your system out — has been enumerated and deliberately
checked. Security was a pass you made, not a vibe you had.

## When to fire

- Before launch or exposure to real users.
- Any new endpoint, upload, import, webhook, or external input arrives.
- Authentication, authorization, secrets, payments, or personal data
  are involved.
- You catch yourself saying "it's just an internal tool" — every
  internal tool is one port-forward away from being external.

## Workflow

1. **Draw the boundary map.** List every place data enters the system
   (HTTP endpoints, CLI args, file uploads, env vars, queue messages,
   webhooks, third-party responses) and every place data leaves (logs,
   API responses, emails, exports). The map is the work; the checks are
   mechanical once the map is honest.
2. **For each entry point, validate the input deliberately:** type,
   size, shape, range — reject the rest. Validate at the boundary in
   one place, not in seventeen scattered places that each forget a case.
   The server validates; the client's validation is a courtesy.
3. **For storage, check the query construction.** Parameterized
   statements everywhere user-influenced text touches a query —
   concatenation is how injection happens, in every generation of every
   language, forever.
4. **For auth, check every access path:** can a user reach another
   user's object by changing an ID? Not "does the UI hide the link" —
   does the *check* happen server-side, per object, per request?
   Authorization is per-resource, not per-route.
5. **For secrets:** only in environment or a secrets store — never in
   code, config files, commit history, or logs. If a secret has been
   committed, rotating it is part of this pass; deleting the file is
   not.
6. **For outputs — logs and responses:** does the log leak tokens,
   passwords, or personal data? Does the error message expose stack
   traces or internals to the outside world?
7. **For dependencies:** run the lockfile's audit (the lockfile exists,
   right?); pin versions; check nothing you've installed is abandoned or
   already known-vulnerable.
8. **Record the residuals.** For each boundary: hardened, or
   explicitly-noted-and-accepted with a reason and an owner. Accepted
   risk written down is risk management; accepted risk silent is a
   surprise scheduled for later.

## Red flags

- "Temporarily" committed secrets — every temporary secret is
  permanent; rotate it.
- Trusting the client's validation, the browser's session, or the
  caller's honesty.
- Error messages that narrate internals to strangers.
- A pass that found nothing to fix — the boundary map wasn't drawn, it
  was imagined.
- Security checked only on the endpoints you're proud of.

## Exit criteria

- A written boundary map: entries, exits, storage, privileges,
  dependencies — each addressed or explicitly accepted with an owner.
- No secret material in code, config, history, or logs (verified by a
  scan, not by memory).
- Authorization demonstrated per-resource, not per-route, with the
  other-user's-object test shown to fail.
