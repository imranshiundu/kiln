---
name: observe-the-system
description: Installs the three signals - structured logs, metrics, traces - alongside the first feature, so the system explains itself before the first incident. Use when a service, queue, or long-running process is being built, someone debugs by print-statement, or an incident review says "we had no way to know".
license: MIT
metadata:
  phase: ship
---

# Observe the System

## North Star

When something breaks at 3am, the system already tells you what
happened — which request, which path, which boundary — without a
re-run, a guess, or a war room. The signals went in with the first
feature, so observability is a property of the system, not a patch
applied after the first incident.

## When to fire

- A new service, queue, or long-running process is being built — its
  signals ship with the first feature, not after the first pager.
- Someone is about to debug by print-statement archaeology.
- An incident review says "we had no way to know".
- Choosing what to log, measure, or trace, and the answer is
  "everything" or "nothing".

## Workflow

1. **Name the questions first.** Write the three questions you will
   need answered during the first bad night (*which request? which
   dependency? how often?*). Signals exist to answer questions; a
   signal that answers no question is noise with a schema.
2. **Give each signal one job** — structured logs for events with
   context (request id, actor, outcome), metrics for aggregates
   (counts, latencies, error rates), traces for one request's path
   across boundaries. This is the Google SRE book's monitoring
   discipline and OpenTelemetry's signal model; Sridharan's
   observability writing is the deeper read.
3. **Instrument the boundaries.** Every hop to another process, queue,
   or store gets a span and a log line carrying the same correlation
   id. The boundary is where the truth lives; the middle of your own
   function is not.
4. **Fail loud, sample smart.** Errors always logged; success sampled.
   Label cardinality is a budget — an unbounded label value is an
   outage you scheduled.
5. **Wire one alert per question** from step 1, each with a single
   runbook line saying what to do. An alert nobody can act on gets
   deleted in week two, deservedly.
6. **Verify black-box:** break a dependency in staging and answer your
   three questions from the signals alone. If you cannot, the
   observability does not exist yet — stop until it does.

## Red flags

- Debugging an incident by re-running code with print statements
  bolted on.
- Logs that describe only the happy path.
- Dashboards with no alert attached, alerts with no dashboard behind
  them, and neither with an owner.
- Tracing "planned for v2" while the system takes its first real
  traffic.
- User data or secrets in log lines.

## Exit criteria

- The three questions written down, and each answerable from logs and
  trace in one place — demonstrated, not asserted.
- Every external boundary emits a span and a correlated log event.
- One alert per question, each with its runbook line, visible in the
  alerting config.
- The black-box drill passed; the queries that answered the questions
  are saved and committed.
