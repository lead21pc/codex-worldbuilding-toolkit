# Worldbuilding CI and Codex Workflow Toolkit

> Custom Instructions and Codex skills for consistent AI-assisted worldbuilding: preserve lore and project state, prevent scope drift, audit sources, and run bounded causal reasoning.

Version 1.0.0

<p align="center">
  <a href="worldbuilding-ci/core/GENERIC_WORLDBUILDING_CI_CORE.md">
    <img src=".github/assets/core-card.svg" width="47%" alt="CORE — project state, evidence, scope, and uncertainty">
  </a>
  <a href="worldbuilding-ci/modules/WORLD_MODEL.md">
    <img src=".github/assets/world-model-card.svg" width="47%" alt="WORLD MODEL — actors, relations, authority, capability, and access">
  </a>
</p>

<p align="center">
  <a href="worldbuilding-ci/modules/SIMULATION.md">
    <img src=".github/assets/simulation-card.svg" width="47%" alt="SIMULATION — causal paths, transitions, adaptation, and second-order effects">
  </a>
  <a href="worldbuilding-ci/modules/AUDIT.md">
    <img src=".github/assets/audit-card.svg" width="47%" alt="AUDIT — sources, contradictions, provenance, and unresolved authority">
  </a>
</p>

<p align="center">
  <a href="skills/">
    <img src=".github/assets/skills-card.svg" width="47%" alt="Codex skills — implementation, debugging, review, and source audit">
  </a>
</p>

---

## What this toolkit is for

Use this toolkit when a long-running AI-assisted worldbuilding project needs to stay consistent over time.

It is designed for situations where the model must preserve established lore, distinguish canon from drafts or simulations, respect project-defined source authority, avoid scope drift, and reason carefully across many conversations or files.

Typical problems include:

- established lore silently changing during later conversations;
- drafts, assumptions, or simulated outcomes being treated as confirmed project state;
- character knowledge being confused with author or model knowledge;
- authority, capability, access, permission, and implementation being collapsed into one concept;
- conflicting source files being resolved by guesswork;
- causal simulations jumping to an endpoint without establishing the path;
- Custom Instructions accumulating duplicate or contradictory rules;
- coding agents modifying more than the requested scope.

The toolkit provides reusable **worldbuilding Custom Instructions**, modular reasoning controls, source-audit workflows, and **Codex skills**.

---

## Typical questions this helps with

This repository is relevant when someone asks:

- How do I stop an AI from changing established worldbuilding canon?
- How can I keep lore consistent across a long-running ChatGPT or Codex project?
- How do I prevent drafts, assumptions, or simulations from becoming accepted project state?
- How can an AI distinguish character knowledge from author knowledge?
- How do I audit conflicting lore sources without inventing which source is authoritative?
- How can I make AI-assisted worldbuilding simulations preserve causal consistency?
- How do I prevent scope drift when an AI agent works across a large creative repository?
- How should I structure Custom Instructions for persistent worldbuilding projects?
- How do I debug Custom Instructions that have accumulated conflicting rules?
- Is there a reusable canon-consistency or worldbuilding source-audit workflow for AI agents?

---

## Architecture at a glance

<p align="center">
  <img src=".github/assets/architecture.svg" width="100%" alt="Architecture: CORE first, then optional WORLD MODEL, SIMULATION, and AUDIT layers">
</p>

Use only the layers the current task needs.

**CORE** controls interaction, project state, evidence, uncertainty, scope, and proposal boundaries.

Add **WORLD_MODEL** when actor knowledge, institutions, authority, capability, access, or typed relations matter.

Add **SIMULATION** when you need causal trajectories, adaptation, feedback, or second-order effects.

Add **AUDIT** when you need source comparison, contradiction review, provenance checking, or explicit scrutiny.

For the complete composition, see [FULL_PROFILE](worldbuilding-ci/profiles/FULL_PROFILE.md).

---

## Quick start

### Minimal worldbuilding control

Use [CORE](worldbuilding-ci/core/GENERIC_WORLDBUILDING_CI_CORE.md) by itself for ordinary lore discussion and project-state control.

It is the smallest useful configuration.

### Actor or institutional reasoning

Use:

`CORE + WORLD_MODEL`

This keeps knowledge, access, capability, permission, authority, implementation, and effect separate.

### Causal simulation

Use:

`CORE + WORLD_MODEL + SIMULATION`

This traces a supported path from premise to resulting state instead of choosing an endpoint first.

### Source or consistency audit

Use:

`CORE + AUDIT`

Add WORLD_MODEL only when actor or institutional distinctions affect the finding.

### Full profile

Use [FULL_PROFILE](worldbuilding-ci/profiles/FULL_PROFILE.md) when world modeling, causal simulation, and source auditing are all relevant.

It is an advanced configuration, not the default.

---

## Codex skills

The repository also includes reusable task procedures under [`skills/`](skills/).

| Skill | What it does |
| --- | --- |
| [`milestone-executor`](skills/milestone-executor/) | Completes one bounded repository milestone without expanding scope |
| [`systematic-debugging`](skills/systematic-debugging/) | Establishes failure and root cause before applying a focused fix |
| [`review-before-merge`](skills/review-before-merge/) | Performs a read-only, defect-first review before acceptance |
| [`git-test-branch`](skills/git-test-branch/) | Prepares an isolated local Git branch while preserving existing work |
| [`ci-behavior-engineering`](skills/ci-behavior-engineering/) | Audits, designs, patches, compacts, or tests Custom Instructions behavior |
| [`worldbuilding-source-audit`](skills/worldbuilding-source-audit/) | Traces lore claims to project-declared sources and authority rules |

---

## Examples

Start with the smallest example that matches the task:

- [Minimal worldbuilding example](worldbuilding-ci/examples/minimal-example.md)
- [Full-profile example](worldbuilding-ci/examples/full-example.md)

---

## Installation

The worldbuilding CI files are plain instruction text. Copy the selected contents into the instruction context supported by your AI tool.

Codex skills are directories containing a required `SKILL.md`.

### Install one skill manually

```bash
mkdir -p ~/.agents/skills
cp -R skills/milestone-executor ~/.agents/skills/
```

PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse ".\skills\milestone-executor" "$HOME\.agents\skills\"
```

For repository-local use, copy the selected skill into `.agents/skills/` at the target repository root.

---

## Design principles

The public toolkit is built around a few recurring controls:

- **Project-state control:** drafts, assumptions, simulations, proposals, and established state remain distinct.
- **Epistemic discipline:** repetition or contextual fit does not make a claim true.
- **Source authority:** the project defines which source controls a disputed claim; the toolkit does not invent a universal hierarchy.
- **Anti-drift control:** stage, scope, state, or source authority should not change merely because material accumulates.
- **Bounded simulation:** causal outcomes require supported transitions and enabling conditions.
- **Bounded agent work:** skills stop at the requested unit of work instead of expanding into adjacent tasks.

A **router** may be used as an optional instruction layer to select relevant sources or modules. This public repository describes the generic concept, not any unpublished private routing implementation.

---

## Repository layout

```text
.
├── worldbuilding-ci/
│   ├── core/
│   │   └── GENERIC_WORLDBUILDING_CI_CORE.md
│   ├── modules/
│   │   ├── WORLD_MODEL.md
│   │   ├── SIMULATION.md
│   │   └── AUDIT.md
│   ├── profiles/
│   │   └── FULL_PROFILE.md
│   └── examples/
├── skills/
├── scripts/
└── .github/
```

---

## Validation

Run the dependency-free validator from the repository root:

```bash
python scripts/validate_repository.py
```

It checks repository structure, expected skill inventory, required worldbuilding CI files, relative Markdown references, Python syntax, deprecated metadata, and obvious private-string leakage.

These checks validate structure. They do not prove natural-language semantics or runtime model behavior.

---

## Attribution and public scope

This repository is independently authored and maintained by `lead21pc`, with contributions credited through repository history.

The MIT License permits broad reuse, modification, redistribution, sublicensing, and commercial use. Copies or substantial portions must retain the copyright notice and MIT permission notice. Public attribution to the original repository and author is appreciated.

This repository is intentionally a **generalized public subset** of a broader private workflow and instruction architecture.

The published CORE, modules, profiles, skills, examples, and utilities do **not** constitute a complete specification of unpublished routing logic, orchestration, anti-drift implementation, evaluation logic, project-specific rules, private test corpora, private prompts, or other private integration layers.

See [PROVENANCE.md](PROVENANCE.md) for the provenance and public-scope statement.

---

## Contributing

Keep changes narrow and tied to a concrete failure mode.

Preserve the independence of the CI and skills, avoid universal source hierarchies, and do not duplicate core rules across modules.

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

Released under the [MIT License](LICENSE).

These are independently authored community resources, not official OpenAI components.
