# Codex Workflow Skills and Worldbuilding Control Toolkit

Version 1.0.0

**Reusable Codex workflow skills plus modular worldbuilding behavioral control.**

This toolkit grew out of a demanding, long-running AI-assisted worldbuilding workflow. The repository now contains two independent groups of components:

- **Generic Codex workflow skills** for ordinary software, repository, debugging, review, Git, bounded-task, and Custom Instructions work.
- **Worldbuilding-specific controls** for lore and project-state integrity, source provenance, simulation discipline, source authority, and anti-drift behavior.

You do not need the worldbuilding CI to use the generic Codex skills. Every skill and the worldbuilding CI package can be adopted independently.

These are independently authored community resources, not official OpenAI components. Inspect third-party instructions before using them, especially when they can modify files or Git state.

## Component matrix

| Component | Generic or worldbuilding-specific | Can be used independently? | Primary purpose |
| --- | --- | --- | --- |
| `milestone-executor` | Generic | Yes | Complete one bounded implementation task without scope drift |
| `systematic-debugging` | Generic | Yes | Establish a failure and root cause before applying a focused fix |
| `review-before-merge` | Generic | Yes | Keep pre-merge review read-only and defect-focused |
| `git-test-branch` | Generic | Yes | Prepare isolated local Git branches without discarding existing work |
| `ci-behavior-engineering` | Generic | Yes | Audit or repair Custom Instructions behavior and regressions |
| `worldbuilding-source-audit` | Worldbuilding-specific | Yes | Audit lore claims against declared sources and authority rules |
| `worldbuilding-ci/` | Worldbuilding-specific | Yes | Control state mutation, simulation, source handling, and instruction drift |

## Who this is for

The generic skills are for Codex users who want:

- bounded implementation with an explicit stop condition;
- systematic debugging before code changes;
- review separation between implementation and pre-merge assessment;
- safer Git branch isolation;
- evidence-based CI behavior auditing.

These workflows do not require a worldbuilding project.

The worldbuilding-specific components are for AI-assisted worldbuilders who additionally need:

- canon or project-state integrity;
- source provenance and unresolved-source handling;
- anti-drift controls for long-running projects;
- actor and causal simulation discipline;
- source auditing without an invented universal hierarchy.

## Problems this toolkit addresses

The generic skills address recognizable repository and agent-workflow failures:

- Codex scope drift causes an agent to modify more than the requested task;
- implementation, debugging, and review become mixed into one unbounded operation;
- fixes are attempted before the failure or root cause is established;
- branch changes risk disturbing existing work;
- a CI behavior regression accumulates patches without a controlled diagnosis.

The worldbuilding controls address a separate set of long-running project failures:

- drafts or simulations silently become established lore;
- assumptions are promoted into project state without confirmation;
- accumulated instructions cause instruction drift;
- source authority—the project rule for deciding which source controls a disputed claim—becomes ambiguous;
- actor knowledge, authority, capability, and access are conflated;
- repeated Custom Instructions patches create duplicate or conflicting rules;
- complex behavioral instructions become difficult to maintain.

Here, **CI** means *Custom Instructions*, not Continuous Integration.

## Quick start

The two paths below are independent. Path 1 does not require any file or setup from Path 2.

### Path 1: I only want reusable Codex workflow skills

Choose one or more generic skills from these real repository paths:

- `skills/milestone-executor/`
- `skills/systematic-debugging/`
- `skills/review-before-merge/`
- `skills/git-test-branch/`
- `skills/ci-behavior-engineering/`

Install one skill from the repository root:

```bash
mkdir -p ~/.agents/skills
cp -R skills/milestone-executor ~/.agents/skills/
```

PowerShell equivalent:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse ".\skills\milestone-executor" "$HOME\.agents\skills\"
```

Install several selected skills:

```bash
cp -R \
  skills/systematic-debugging \
  skills/review-before-merge \
  ~/.agents/skills/
```

Example uses:

```text
Use $milestone-executor for this bounded implementation and stop after its acceptance checks pass.

Use $systematic-debugging to establish the failure and root cause before editing.

Use $review-before-merge for a read-only pre-merge review.

Use $git-test-branch to prepare Git branch isolation for this test.

Use $ci-behavior-engineering to audit this CI behavior regression before proposing a patch.
```

For repository-local use, copy selected skills into `.agents/skills/` at the target repository root. Restart Codex if a newly copied skill is not discovered automatically.

### Path 2: I want stronger AI-assisted worldbuilding control

Choose the lightest behavioral CI configuration that fits the task:

1. **Minimal — CORE only.** Start with [`worldbuilding-ci/core/GENERIC_WORLDBUILDING_CI_CORE.md`](worldbuilding-ci/core/GENERIC_WORLDBUILDING_CI_CORE.md) for general interaction and project-state control.
2. **Advanced — CORE plus selected modules.** Add [`WORLD_MODEL`](worldbuilding-ci/modules/WORLD_MODEL.md), [`SIMULATION`](worldbuilding-ci/modules/SIMULATION.md), or [`AUDIT`](worldbuilding-ci/modules/AUDIT.md) only when needed.
3. **Full — FULL_PROFILE.** Use [`worldbuilding-ci/profiles/FULL_PROFILE.md`](worldbuilding-ci/profiles/FULL_PROFILE.md) when world modeling, causal simulation, and source auditing are all relevant.

`FULL_PROFILE` is an advanced option, not a required or universally recommended configuration. The files are instruction text; copy the selected contents into the instruction context supported by your AI tool.

Optionally install [`skills/worldbuilding-source-audit/`](skills/worldbuilding-source-audit/) when Codex should trace claims against a project's declared sources. The skill and behavioral CI can also be used separately.

See the [minimal example](worldbuilding-ci/examples/minimal-example.md) and [full example](worldbuilding-ci/examples/full-example.md).

When `$skill-installer` is available, provide the published repository URL and an exact skill path. Skill Installer is optional; manual copying works for either path.

## Repository components

```text
.
├── skills/
│   ├── milestone-executor/
│   ├── systematic-debugging/
│   ├── review-before-merge/
│   ├── git-test-branch/
│   ├── ci-behavior-engineering/
│   └── worldbuilding-source-audit/
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
│       ├── minimal-example.md
│       └── full-example.md
├── scripts/
│   └── validate_repository.py
└── .github/workflows/
    └── validate-skills.yml
```

### Generic Codex workflow skills

| Skill | Purpose | Implicit invocation | Can modify files or state? |
| --- | --- | --- | --- |
| `milestone-executor` | Complete one bounded repository milestone without scope drift | Yes | Yes, within the requested milestone |
| `systematic-debugging` | Establish a failure and root cause before applying a focused fix | Yes | Yes, after diagnosis when a fix is requested |
| `review-before-merge` | Perform a read-only, defect-first review | Yes | No |
| `git-test-branch` | Prepare an isolated local Git branch while preserving existing work | No | Yes, local Git branch state |
| `ci-behavior-engineering` | Audit, design, patch, compact, or test Custom Instructions behavior | No | Only when the requested operation requires it |

### Worldbuilding-specific components

- **`worldbuilding-source-audit`** audits worldbuilding claims against project-declared sources and authority rules. It is read-only by default.
- **CORE** owns general worldbuilding interaction control, state mutation, evidence, uncertainty, proposal boundaries, and explanation.
- **WORLD_MODEL** adds optional entity, relation, actor-information, authority, capability, and access distinctions.
- **SIMULATION** adds optional causal-path and second-order-effect discipline.
- **AUDIT** adds optional source and system scrutiny.
- **FULL_PROFILE** composes all four CI files without making the advanced configuration mandatory.

## Behavioral concepts

- **Epistemic control** governs when an assumption, inference, or proposal may become supported or established state.
- **Source authority** is the project-declared rule for deciding which source governs a disputed claim. The toolkit supplies no universal hierarchy.
- **Anti-drift control** prevents stage, scope, project state, or source authority from changing merely because instructions accumulate or a claim is repeated.
- A **router** is an optional instruction layer that selects relevant sources or modules. It should route inputs without inventing conclusions or a competing authority hierarchy.

These concepts belong primarily to the worldbuilding controls. Generic Codex skills remain usable without adopting this terminology or architecture.

## AGENTS.md, skills, and task prompts

- `AGENTS.md` defines repository-specific rules and constraints.
- A skill defines a reusable procedure for a recognizable task.
- The task prompt states the work authorized now.

All three apply together. Invoking a skill does not authorize unrelated, destructive, or externally visible actions.

## Validation

Run the dependency-free validator from the repository root:

```bash
python scripts/validate_repository.py
```

It checks the six-skill inventory, skill metadata, required worldbuilding CI files, relative Markdown references, Python syntax, deprecated metadata, and forbidden private strings. The GitHub workflow also parses PowerShell scripts and smoke-tests the included utilities.

These checks validate structure and obvious leakage. They do not prove natural-language semantics or runtime model behavior; those remain manual review tasks.

## Contributing

Generic skills must remain domain-neutral. Worldbuilding-specific assumptions must not leak into them, and specialization inside worldbuilding modules must not change generic skill semantics. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE).
