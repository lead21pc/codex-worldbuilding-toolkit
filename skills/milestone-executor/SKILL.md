---
name: milestone-executor
description: Use when implementing one explicitly defined milestone, task, issue, or bounded feature in an existing repository. Enforce scope, minimal changes, verification, and a hard stop after the requested unit of work.
---

# Milestone Executor

Execute one bounded unit of work without expanding its scope.

## When to use

Use this skill when the user asks to:
- implement a named milestone;
- complete one issue or bounded feature;
- continue a staged development plan;
- modify an existing repository under explicit constraints.

Do not use it for open-ended architecture redesign, brainstorming, or repository-wide modernization unless that is itself the explicit milestone.

## Inputs and context

Before editing:
1. Read every applicable `AGENTS.md`.
2. Read the milestone/task source of truth named by the user.
3. Inspect repository status and relevant structure.
4. Identify:
   - required outcome;
   - explicit constraints;
   - acceptance conditions;
   - files/components likely in scope;
   - actions explicitly out of scope.
5. Treat existing project invariants as authoritative unless the task explicitly changes them.

If requirements conflict, stop before destructive or irreversible work and report the conflict.

## Procedure

1. Define the execution boundary.
   - Restate internally what must change and what must not change.
   - Do not create additional deliverables merely because they appear useful.

2. Inspect only the necessary code and tests.
   - Trace existing behavior before introducing new abstractions.
   - Reuse existing project patterns when they satisfy the requirement.

3. Plan the minimum coherent change.
   - Prefer modifying existing components over introducing parallel systems.
   - Avoid placeholder implementations.
   - Avoid speculative extensibility.
   - Do not add dependencies unless required by the milestone.

4. Implement the milestone.
   - Keep edits local to the required behavior.
   - Preserve public interfaces and unrelated behavior unless the milestone explicitly requires changes.
   - Do not refactor unrelated code while touching a file.

5. Verify incrementally.
   - Run focused checks after meaningful changes.
   - Fix failures caused by the milestone.
   - Do not absorb unrelated pre-existing failures into the milestone.

6. Inspect the final diff.
   - Remove accidental formatting churn, debug code, dead code introduced by the change, and unrelated edits.

7. Stop at milestone completion.
   - Do not begin the next milestone.
   - Do not merge, push, publish, deploy, or delete branches unless explicitly requested.

## Efficiency plan

- Read the task source before exploring the repo.
- Build a small working set of relevant files and reuse it.
- Prefer repository-native tests and scripts.
- Do not perform broad audits unless needed to satisfy acceptance conditions.
- Stop once acceptance conditions are met and the final diff is clean.

## Scope-drift guardrails

Never do the following unless explicitly required:
- repository-wide cleanup;
- architecture redesign;
- dependency upgrades;
- renaming unrelated symbols;
- replacing working subsystems;
- adding telemetry, analytics, SaaS infrastructure, account systems, cloud services, or placeholders;
- implementing future milestones;
- modifying documentation unrelated to the completed behavior.

## Pitfalls and fixes

- Symptom: implementation grows beyond the named milestone.
  - Fix: compare every pending edit against the acceptance conditions and remove non-required work.

- Symptom: a new abstraction exists only for hypothetical future needs.
  - Fix: prefer the simplest current implementation consistent with project invariants.

- Symptom: unrelated test failures trigger unrelated fixes.
  - Fix: determine whether the milestone caused them; otherwise report them separately.

- Symptom: working code is refactored because another style seems cleaner.
  - Fix: retain the existing structure unless it blocks the required behavior.

## Verification checklist

Confirm:
- the requested milestone is complete;
- all explicit constraints are satisfied;
- no future milestone was started;
- no placeholder remains;
- no unnecessary dependency was added;
- relevant tests/checks were run;
- failures are classified as caused-by-change or pre-existing where possible;
- the final diff is limited to required work;
- no merge, push, deploy, or destructive Git action occurred without explicit instruction.

## Final report

Return:
1. completed outcome;
2. files changed;
3. verification performed and results;
4. remaining known limitation or unverified risk, if any;
5. explicit statement that no next milestone was started.
