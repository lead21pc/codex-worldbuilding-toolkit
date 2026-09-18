# Contradiction handling

Declare a contradiction only when two claims cannot both be true under the same relevant conditions.

## Confirm matching conditions

Before using `CONFLICT`, check that the claims concern the same:

- entity or proposition;
- meaning of key terms;
- scope and preconditions;
- era or sequence point;
- continuity, edition, world layer, or viewpoint;
- authority context.

If one of these is unresolved, report a possible conflict or `UNKNOWN` rather than a confirmed contradiction.

## Common non-conflicts

- A rule changed at an established event or edition boundary.
- Two narrators have different knowledge or beliefs.
- A broad rule and a documented exception apply to different cases.
- An older source was explicitly superseded for the affected scope.
- A proposal differs from an authoritative source but was never adopted.
- Separate continuities or world layers intentionally diverge.

Preserve provenance for superseded material, but do not keep reporting an authorized historical replacement as an active contradiction.

## Active conflicts

For a confirmed conflict:

1. Cite both claims and their locations.
2. State the exact conditions that make them incompatible.
3. Record each source's authority status without inventing precedence.
4. Identify dependent claims that cannot safely use either branch as settled fact.
5. Present resolution options only as proposals until authorized.

Deferral does not resolve a conflict. Keep the conflict visible, record the deferral decision and scope, and avoid using either branch as a certain premise.

## Generated and derived material

If generated output conflicts with an input or authority source, first discover the project's declared relationship between them. The correct repair point might be an input, transformation, or output, but the audit must not assume which one controls. A behavioral instruction, tool configuration, or example does not become a world fact merely because it mentions one.
