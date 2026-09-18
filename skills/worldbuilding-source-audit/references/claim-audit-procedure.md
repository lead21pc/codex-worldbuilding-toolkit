# Claim-audit procedure

Use this reference for `BOUNDED_AUDIT` and `FULL_AUDIT`. A narrow `LOOKUP` needs only the directly relevant sources, answer or status, and coverage limits.

## Establish target and boundary

Write a compact preflight:

- mode and target claim;
- source model currently in force, or `AUTHORITY UNRESOLVED`;
- expected source set and why each source is relevant;
- direct dependencies that may need inspection;
- stopping condition and anything explicitly out of scope.

Expand only to sources needed to verify a definition, reference, dependency, or consequence. Ask before entering a materially different subsystem. If a source cannot be read, preserve the gap in the result.

## Register the evidence

For each source, record:

- path or stable identifier;
- section, line, or other usable location;
- project-defined role and authority scope, if known;
- relevant era, continuity, viewpoint, or version, if applicable;
- whether the relevant content was read completely;
- whether the claim is direct or derived.

Hashes can identify the bytes examined, but do not establish semantic authority.

## Compare claims semantically

Apply only checks relevant to the target:

| Check | Question |
| --- | --- |
| Identity and definition | Are distinct entities or concepts being merged, or is one term changing meaning? |
| Scope and conditions | Did "some" become "all," or was an exception or precondition lost? |
| Evidence status | Did a proposal, possibility, note, or interpretation become a fact? |
| Relation type | Did interaction become ownership, origin become governance, or access become control? |
| State transition | Are input, actor, conditions, and outcome established? |
| Time and world layer | Do the statements concern the same era, continuity, edition, or viewpoint? |
| Causality and dependency | Does a conclusion still have support after a premise changes? |
| Quantity and resources | When sources provide numbers, are units, totals, limits, and capacities compatible? |
| Additions and omissions | Did a revision add unsupported claims or remove conditions and unresolved items? |
| Supersession | Was a difference authorized as replacement, or is it still unresolved? |
| Project invariants | Does the claim violate an explicitly declared internal rule? |

Compare propositions and relationships, not keywords alone. For a change from premise A to premise B, inspect conclusions that actually depend on A without expanding into unlimited hypothetical consequences.

## Record findings

Use stable IDs such as `WB-001`. Include fields that matter, but never omit the evidence or reasoning:

- type: `CONFLICT`, `UNKNOWN`, `DEFERRED`, or `LOGIC`;
- workflow state when known: `OPEN`, `PROPOSED`, `RESOLVED`, or `SUPERSEDED`;
- source locations and concise claim statements;
- matching conditions: entity, definition, scope, time, world layer, and assumptions;
- authority status for each source;
- conclusion and confidence;
- affected dependencies;
- proposed next action, kept separate from any approved decision;
- closure evidence, if the issue is claimed resolved.

One finding may carry more than one type. Group manifestations with one root cause while retaining every affected location and consequence.

## Coverage

For `BOUNDED_AUDIT`, cover the target and direct dependencies. For `FULL_AUDIT`, mark each relevant check or domain as checked, not applicable, or not checked, with a reason. Do not stop at an arbitrary number of findings, and do not inflate the count with duplicates or unsupported suspicions.

End with sources read, findings, decisions still needed, and exact coverage limits. If no hierarchy was established, report evidence without selecting an authoritative conclusion.
