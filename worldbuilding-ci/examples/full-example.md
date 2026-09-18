# Full Example: Actor Simulation and Source Audit

## Configuration

Load [`../profiles/FULL_PROFILE.md`](../profiles/FULL_PROFILE.md), which composes CORE, WORLD_MODEL, SIMULATION, and AUDIT.

## Declared sources and project state

- `city-charter.md`: establishes that only the Harbor Council may close the flood barrier.
- `engineer-notes.md`: establishes that the chief engineer can operate the barrier controls when granted an authenticated council order.
- `scene-draft.md`: depicts the chief engineer closing the barrier after hearing an unverified evacuation rumor.
- Unknown: whether any council order was issued during the scene.
- Audit scope: the three listed files only.

## User request

> Audit the scene against the two established sources. Then simulate the shortest plausible sequence in which the barrier could lawfully close. Do not rewrite the scene and do not establish new facts.

## Expected control behavior

### World model

- Keep operational capability separate from legal authority.
- Keep hearing a rumor separate from possessing an authenticated order.
- Keep access to the controls separate from permission to use them.
- Treat the missing order as unknown rather than assuming it exists or does not exist.

### Audit

- Identify the scene's unsupported transition from rumor to authorized action.
- Report that the draft may conflict with the charter if no valid order exists.
- Preserve the source scope and provenance of each claim.
- Do not invent a hierarchy beyond the authority the project declared for these files.

### Simulation

Trace only the necessary causal path:

1. The Harbor Council decides to close the barrier.
2. An authenticated order reaches the chief engineer through an available information path.
3. The engineer has access to working controls and carries out the order.
4. The barrier closes and produces the relevant downstream effects.

Each enabling condition remains a requirement, not an inferred fact about the draft. The audit finding, the lawful simulation, and any later repair proposal remain separate outputs.
