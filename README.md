# Codex Workflow Skills

Version 1.0.0

This repository contains six independently authored community skills for repeatable Codex workflows. Each skill is self-contained under `skills/` and includes its own instructions, invocation metadata, and any required references or scripts.

These are not official OpenAI skills. Inspect any third-party skill before installing or invoking it, especially when it can modify files, Git state, or other local resources.

## Included skills

| Skill | Purpose | Implicit invocation | Can modify files or state? | Typical use |
| --- | --- | --- | --- | --- |
| `milestone-executor` | Complete one bounded repository milestone without scope drift | Yes | Yes, within the requested milestone | Implement a named issue or acceptance-criteria block |
| `systematic-debugging` | Establish a failure and root cause before applying a focused fix | Yes | Yes, after diagnosis when a fix is requested | Diagnose a regression or failing test |
| `review-before-merge` | Perform a read-only, defect-first review of a completed change | Yes | No | Review a branch, commit, or working-tree diff before acceptance |
| `git-test-branch` | Prepare an isolated local Git branch while preserving existing work | No | Yes, local Git branch state | Create or switch to a temporary test branch |
| `ci-behavior-engineering` | Audit, design, patch, compact, or test Custom Instructions behavior | No | Only when the requested operation requires it | Trace a Custom Instructions regression before patching |
| `worldbuilding-source-audit` | Audit worldbuilding claims against project-declared sources and authority rules | Yes | Read-only by default; source changes require an explicit request | Trace a lore claim, contradiction, or unresolved source question |

## Installation

Codex skills are directories containing a required `SKILL.md`. See the [OpenAI skill documentation](https://developers.openai.com/docs/build-skills) for current discovery locations and invocation behavior.

### Install one skill manually

Clone this repository, then copy one skill into your user skill directory:

```bash
mkdir -p ~/.agents/skills
cp -R skills/milestone-executor ~/.agents/skills/
```

PowerShell equivalent:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse ".\skills\milestone-executor" "$HOME\.agents\skills\"
```

For repository-local use, copy the skill into `.agents/skills/` at the repository root instead.

### Install multiple skills manually

Copy only the directories you want:

```bash
mkdir -p ~/.agents/skills
cp -R skills/systematic-debugging skills/review-before-merge ~/.agents/skills/
```

PowerShell equivalent:

```powershell
$skills = @("systematic-debugging", "review-before-merge")
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
foreach ($skill in $skills) {
    Copy-Item -Recurse ".\skills\$skill" "$HOME\.agents\skills\"
}
```

Restart Codex if a newly copied skill is not discovered automatically.

### Install with Skill Installer

When `$skill-installer` is available, ask it to install one or more paths from the public GitHub repository after publication:

```text
$skill-installer
Install from https://github.com/OWNER/codex-workflow-skills using path skills/milestone-executor.
```

For multiple skills, provide multiple repository paths in the same request. Replace `OWNER` with the published repository owner. Skill Installer aborts when a destination directory already exists; inspect or remove the existing installation deliberately before retrying.

## Invocation

Skills with implicit invocation enabled may be selected when a task matches their `description`. Any skill can also be invoked explicitly by naming it with `$skill-name`.

`git-test-branch` is explicit-only because branch-changing operations should begin only when the user deliberately requests branch preparation. `ci-behavior-engineering` is explicit-only because it is a specialized Custom Instructions engineering workflow and should not activate during ordinary writing, debugging, or CI/CD work.

Examples:

```text
Use $milestone-executor to implement milestone 3 exactly as specified and stop after its acceptance checks pass.

Use $systematic-debugging to reproduce this failing test, identify the root cause, and apply the smallest verified fix.

Use $review-before-merge to review the current working-tree diff against the issue requirements.

Use $git-test-branch to create a local test branch from the current branch without discarding existing work.

Use $ci-behavior-engineering to audit why this Custom Instructions revision changes response behavior before proposing a patch.

Use $worldbuilding-source-audit to trace this claim to the project's declared sources and report unresolved authority or contradictions.
```

## AGENTS.md, skills, and task prompts

- `AGENTS.md` defines repository-specific rules, invariants, and working constraints.
- A skill defines a reusable procedure for a recognizable class of tasks.
- The task prompt states the work requested now, including its scope and authorization.

All three apply together. A skill does not override higher-priority instructions, repository invariants, or the current task's boundaries, and merely invoking a skill does not grant permission for unrelated or destructive actions.

## Validation

Run the dependency-free repository validator from the repository root:

```bash
python scripts/validate_repository.py
```

The validator checks skill structure, supported metadata, relative references, script syntax for Python files, the expected public skill inventory, and forbidden private strings. The GitHub workflow also asks PowerShell to parse `.ps1` scripts and runs basic smoke tests for the included utilities.

This validator intentionally implements the smallest checks needed by this repository. It does not replace semantic review or prove runtime behavior.

## License

Released under the [MIT License](LICENSE).
