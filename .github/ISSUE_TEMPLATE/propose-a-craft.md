---
name: Propose a craft
description: Suggest a new skill for the KILN library
labels: ["new-skill"]
body:
  - type: markdown
    attributes:
      value: |
        KILN accepts crafts, not opinions with formatting. Before
        opening this issue, read [docs/format.md](../blob/main/docs/format.md)
        and [skills/fire-a-skill/SKILL.md](../blob/main/skills/fire-a-skill/SKILL.md) —
        they are the bar, and this form is the bar in question form.

  - type: textarea
    id: craft
    attributes:
      label: The craft
      description: One sentence. What is repeatedly being improvised, and what is the finished state when it is done well?
      placeholder: "e.g. evolving a database schema without downtime while the system keeps serving"
    validations:
      required: true

  - type: dropdown
    id: phase
    attributes:
      label: Lifecycle phase
      options:
        - gather — understand the terrain
        - spec — align on what and why
        - design — model data and interfaces
        - build — make it real, slice by slice
        - verify — prove the work
        - ship — face reality
        - tend — keep it alive
        - meta — the library itself
    validations:
      required: true

  - type: textarea
    id: trigger
    attributes:
      label: When it fires
      description: The concrete situations an agent can match against real requests. If you cannot name three, the trigger is not ready.
      placeholder: |
        - ...
        - ...
        - ...
    validations:
      required: true

  - type: textarea
    id: prior-art
    attributes:
      label: Where the craft comes from
      description: Named books, papers, libraries, or practice it distills. A skill that claims to have invented its craft is lying about its parents.
    validations:
      required: true

  - type: checkboxes
    id: firetest
    attributes:
      label: The Fire Test, in question form
      options:
        - label: One craft — the name does not need an "and"
          required: true
        - label: Triggerable — the description names concrete situations, not an abstract
          required: true
        - label: A workflow, not prose — steps with gates, not an essay
          required: true
        - label: Evidence over claims — exit criteria demand observable proof
          required: true
        - label: Lean — the body will land under ~500 words
          required: true
        - label: Not already here or better elsewhere — KILN, superpowers, addyosmani/agent-skills checked
          required: true
