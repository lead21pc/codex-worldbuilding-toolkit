---
name: worldbuilding-source-audit
description: Audit worldbuilding claims against a project's declared sources, authority model, and internal rules. Use for source tracing, contradiction review, provenance checks, or unresolved lore questions; remain read-only unless the user explicitly requests source changes.
---

# Worldbuilding source audit

Audit claims using the project's own source model. Do not assume a setting, file format, directory layout, status vocabulary, or universal hierarchy.

## Choose the lightest sufficient mode

- **LOOKUP:** Answer a narrow question from directly relevant sources. Do not build a full findings matrix unless a real issue appears.
- **BOUNDED_AUDIT:** Check one claim, entity, file, change, or named conflict and its direct dependencies.
- **FULL_AUDIT:** Review the requested source set comprehensively. Use only for an explicit full audit or when cross-project dependencies make a bounded result unreliable.

Default to `LOOKUP`. State the mode, target, expected sources, and stopping condition when scope is not obvious. Read [claim-audit-procedure.md](references/claim-audit-procedure.md) for `BOUNDED_AUDIT` and `FULL_AUDIT`.

## Discover the project's source model first

Before deciding which source controls a claim, inspect the smallest relevant set of:

1. explicit user instructions for this task;
2. applicable `AGENTS.md` files;
3. project documentation and contribution rules;
4. source indexes, manifests, provenance records, or equivalent registries;
5. repository structure and source contents.

Treat repository structure and filenames as clues, not authority. A file being newer, versioned, generated, archived, or named with words such as "current" or "official" does not establish its role by itself. A request to inspect a file does not automatically declare that file authoritative.

Read [source-authority-discovery.md](references/source-authority-discovery.md) when authority, status, supersession, or generated-source roles are not already explicit. Record the project's own terms and rules rather than replacing them with a fixed vocabulary.

If no hierarchy or authority rule can be established, say that source authority is unresolved. Collect and compare evidence, but do not choose a winning source or announce a definitive world fact.

## Work from current evidence

Open the actual source material needed for the claim. Do not substitute memory, prior summaries, search snippets, filenames, or generated indexes for source content. Read complete relevant sections; if content is truncated or unavailable, report the gap and do not certify it.

Keep a compact source register containing path or identifier, project-defined role, scope, version or era when known, and read status. Distinguish direct source statements from derived interpretations, proposals, notes, drafts, deprecated material, generated output, and behavioral instructions only when the project exposes those distinctions.

Use `scripts/collect_source_inventory.py` only when deterministic paths and hashes help identify the files examined. The script does not establish authority or interpret content.

## Evaluate claims without inventing lore

Trace each material conclusion to source evidence. Keep these separate:

- direct source statement;
- interpretation supported by stated premises;
- unresolved possibility;
- proposal or requested design;
- unsupported invention.

Do not fill gaps, create explanations, merge incompatible accounts, or treat missing evidence as permission to invent. A failed search does not prove that a claim is false or absent from all project sources.

Check definitions, scope, conditions, exceptions, chronology, viewpoint, continuity or world layer, relation type, causality, quantities, state transitions, and project-defined invariants when relevant. Use the project's internal rules; difference from the real world is not itself a logic error.

Read [contradiction-handling.md](references/contradiction-handling.md) before declaring sources contradictory. Read [uncertainty-handling.md](references/uncertainty-handling.md) when evidence is missing, ambiguous, deferred, or authority is unresolved. Neutral worked cases are in [neutral-examples.md](references/neutral-examples.md).

## Keep audit and modification separate

Audits are read-only by default. Report findings and possible resolutions, then stop. Do not edit sources merely to make a conflict disappear.

If the user explicitly requests modifications, identify the exact approved decisions and affected files before editing. Preserve unresolved items and unrelated source material. Follow any project-declared generation or publication workflow, then read the actual output again and compare it with the approved decisions. A successful build, hash check, or format check does not prove semantic correctness.

## Report with bounded confidence

For a lookup, report the sources read, answer or status, and limits. For an audit, give each material finding a stable neutral ID such as `WB-001`, evidence locations, claim conditions, authority status, reasoning, dependencies, and resolution state when the project or task defines one.

Useful analytical labels include `CONFLICT`, `UNKNOWN`, `DEFERRED`, and `LOGIC`, but do not present them as project-native statuses unless the project uses them. Separate issue type from workflow state such as `OPEN`, `PROPOSED`, `RESOLVED`, or `SUPERSEDED`.

Never claim exhaustive consistency beyond the sources and scope actually checked.
