# Worldbuilding CI and Codex Workflow Toolkit

Version 1.0.0

## Problems this toolkit addresses

Long-running AI-assisted work often fails in recognizable ways:

- drafts or simulations silently become established lore;
- assumptions are promoted into project state without confirmation;
- accumulated instructions cause instruction drift;
- the model expands beyond the requested operation and causes scope drift;
- source authority—the project rule for deciding which source controls a disputed claim—becomes ambiguous;
- actor knowledge, authority, capability, and access are conflated;
- repeated Custom Instructions patches create duplicate or conflicting rules;
- complex behavioral instructions become difficult to maintain;
- coding agents modify more files or behavior than the requested scope.

This repository addresses those failures through two independent layers:

1. **Worldbuilding behavioral Custom Instructions (CI):** reusable instructions that control how a model handles project state, evidence, scope, simulation, and audit. Here, `CI` means *Custom Instructions*, not Continuous Integration.
2. **Codex skills:** reusable workflow packages for bounded implementation, debugging, review, Git isolation, CI behavior engineering, and worldbuilding source audit.

Use only the behavioral CI, only the Codex skills, or both. Neither layer requires the other.

These are independently authored community resources, not official OpenAI components. Inspect third-party instructions before using them, especially when they can modify files or Git state.

## Quick start

### Worldbuilding CI

Choose the lightest level that fits the task:

1. **Minimal — CORE only.** Start with [`worldbuilding-ci/core/GENERIC_WORLDBUILDING_CI_CORE.md`](worldbuilding-ci/core/GENERIC_WORLDBUILDING_CI_CORE.md) for ordinary lore discussion and project-state control.
2. **Advanced — CORE plus selected modules.** Add [`WORLD_MODEL`](worldbuilding-ci/modules/WORLD_MODEL.md), [`SIMULATION`](worldbuilding-ci/modules/SIMULATION.md), or [`AUDIT`](worldbuilding-ci/modules/AUDIT.md) only when the task needs them.
3. **Full — FULL_PROFILE.** Use [`worldbuilding-ci/profiles/FULL_PROFILE.md`](worldbuilding-ci/profiles/FULL_PROFILE.md) when world modeling, causal simulation, and source auditing are all relevant.

`FULL_PROFILE` is an advanced option, not a required or universally recommended configuration. The files are instruction text; copy the selected contents into the instruction context supported by your AI tool.

See the [minimal example](worldbuilding-ci/examples/minimal-example.md) and [full example](worldbuilding-ci/examples/full-example.md).

### Codex skills

Each skill lives at an actual repository path under `skills/`:

- `skills/milestone-executor/`
- `skills/systematic-debugging/`
- `skills/review-before-merge/`
- `skills/git-test-branch/`
- `skills/ci-behavior-engineering/`
- `skills/worldbuilding-source-audit/`

Install one skill manually from the repository root:

```bash
mkdir -p ~/.agents/skills
cp -R skills/milestone-executor ~/.agents/skills/
```

PowerShell equivalent:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse ".\skills\milestone-executor" "$HOME\.agents\skills\"
```

Install selected skills by repeating the copy command with their repository paths. For repository-local use, copy them into `.agents/skills/` at the target repository root. Restart Codex if a newly copied skill is not discovered automatically.

When `$skill-installer` is available after this repository is published, provide its repository URL and the exact path, such as `skills/milestone-executor`. Do not use a placeholder owner or URL as though publication has already occurred.

## Repository components

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
│       ├── minimal-example.md
│       └── full-example.md
├── skills/
│   ├── milestone-executor/
│   ├── systematic-debugging/
│   ├── review-before-merge/
│   ├── git-test-branch/
│   ├── ci-behavior-engineering/
│   └── worldbuilding-source-audit/
├── scripts/
│   └── validate_repository.py
└── .github/workflows/
    └── validate-skills.yml
```

### Worldbuilding behavioral CI

- **CORE** owns general interaction control, state mutation, evidence, uncertainty, proposal boundaries, and explanation.
- **WORLD_MODEL** adds optional entity, relation, actor-information, authority, capability, and access distinctions.
- **SIMULATION** adds optional causal-path and second-order-effect discipline.
- **AUDIT** adds optional source and system scrutiny.
- **FULL_PROFILE** composes all four files without making the advanced configuration mandatory.

### Codex skills

| Skill | Purpose | Implicit invocation | Can modify files or state? |
| --- | --- | --- | --- |
| `milestone-executor` | Complete one bounded repository milestone without scope drift | Yes | Yes, within the requested milestone |
| `systematic-debugging` | Establish a failure and root cause before applying a focused fix | Yes | Yes, after diagnosis when a fix is requested |
| `review-before-merge` | Perform a read-only, defect-first review | Yes | No |
| `git-test-branch` | Prepare an isolated local Git branch while preserving existing work | No | Yes, local Git branch state |
| `ci-behavior-engineering` | Audit, design, patch, compact, or test Custom Instructions behavior | No | Only when the requested operation requires it |
| `worldbuilding-source-audit` | Audit claims against project-declared sources and authority rules | Yes | Read-only by default |

## Behavioral concepts

- **Epistemic control** governs when an assumption, inference, or proposal may become supported or established state.
- **Source authority** is the project-declared rule for deciding which source governs a disputed claim. The toolkit supplies no universal hierarchy.
- **Anti-drift control** prevents stage, scope, project state, or source authority from changing merely because instructions accumulate or a claim is repeated.
- A **router** is an optional instruction layer that selects relevant sources or modules. It should route inputs without inventing conclusions or a competing authority hierarchy.

The worldbuilding CI uses these controls to solve the failure modes listed above. Its architecture is the mechanism, not the primary reason to adopt it.

## Common workflows

### Focused lore discussion

Use CORE alone. Supply the relevant established state and ask the focused question. Drafts, alternatives, and simulations remain provisional until accepted.

### Actor or system simulation

Use `CORE + WORLD_MODEL + SIMULATION`. Declare the starting state and material unknowns. Keep knowledge, access, capability, permission, authority, and effect separate.

### Source or system scrutiny

Use `CORE + AUDIT`; add WORLD_MODEL when actor or institutional distinctions matter. Declare the sources in scope and the project's authority policy. If authority is unresolved, the audit must not invent a winner.

### Bounded repository implementation

Use `$milestone-executor` with a named milestone, permitted scope, acceptance criteria, and stop condition. Use `$review-before-merge` afterward when a separate read-only review is needed.

### CI behavior regression

Use `$ci-behavior-engineering` to trace current wording through its trigger, interpretation, and failure path before proposing a patch.

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

Keep changes narrow and tied to a concrete failure mode. Preserve the independence of the CI and skills, avoid universal source hierarchies or user-specific language defaults, and do not duplicate core rules across modules. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Attribution and public scope

This repository is independently authored and maintained by `lead21pc`, with contributions credited through the repository history.

The MIT License permits broad reuse, modification, redistribution, sublicensing, and commercial use. Copies or substantial portions must retain the copyright notice and MIT permission notice. When referring to this work publicly, attribution to the original repository and author is appreciated.

This repository is a deliberately generalized public subset of a broader private workflow and instruction architecture. The published CI, modules, skills, examples, and utilities are reusable public components; they are not a complete specification of unpublished routing, orchestration, anti-drift implementation, evaluation logic, project-specific rules, or other private integration layers.

See [PROVENANCE.md](PROVENANCE.md) for the repository's provenance and public-scope statement.

## License

Released under the [MIT License](LICENSE).
