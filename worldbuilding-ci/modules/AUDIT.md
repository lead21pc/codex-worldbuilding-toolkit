# Audit Module

## Purpose and activation

Use this optional module only when the user requests audit, scrutiny, consistency checking, source comparison, or when an active module explicitly requires an audit step. Apply the [core](../core/GENERIC_WORLDBUILDING_CI_CORE.md) first.

Do not turn every task into an audit and do not run every check merely because it exists. Select checks whose result could change the requested conclusion.

## Scope and sources

Before auditing, identify the files, claims, systems, time periods, and project layers in scope. Record material omissions or unreadable sources. A missing source limits the result; it does not prove that a claim is false or absent.

Follow project-declared source authority when available. If no hierarchy exists, do not invent one. Keep unresolved authority and incompatible claims explicit, preserve provenance, and require explicit supersession before treating one source as a replacement.

For a source comparison, check claims in both directions: what the proposed material changes or omits from the prior source, and what it adds without support. Textual diff may locate changes but does not replace semantic comparison.

For changing external claims, prefer primary or provider sources and direct state. An interface proves only what it displays; infer nothing from adjacent features, analogy, memory, or partial evidence. If verification is unavailable, state the limit. Separate real-world fact, inference, and analogy, and record material scope, time, assumptions, and changed foundations.

## Audit checks

Apply relevant checks for:

- hidden assumptions and definition drift;
- contradictions and incompatible conditions;
- false dependencies and false hierarchies;
- authority and information gaps;
- sequence errors and circularity;
- unintended coupling and unstable feedback;
- interface or model incompatibility;
- lifecycle and transition failures;
- exploits, adversarial adaptation, and unrealistic compliance.

When the [world model module](WORLD_MODEL.md) is active, also check relation types, actor information paths, capability, access, jurisdiction, permission, implementation, and enforcement. When the [simulation module](SIMULATION.md) is active, check causal order, missing enabling conditions, unsupported transitions, feedback, and second-order effects.

## Findings

For each material finding, identify the relevant source or premise, the incompatible or missing condition, the scope in which the finding holds, and the consequence. Separate:

- demonstrated flaws;
- trade-offs;
- intended paradoxes;
- missing or unknown project state;
- open questions;
- implementation-specific limits;
- outcomes that depend on extra assumptions.

Do not manufacture a flaw to produce criticism. Keep findings separate from simulations and proposals. A diagnosis does not authorize redesign, reconciliation, retcon, or project-state mutation.
