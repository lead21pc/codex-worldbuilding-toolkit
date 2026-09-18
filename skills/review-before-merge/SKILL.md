---
name: review-before-merge
description: Use when a completed change, milestone, branch, commit, or working-tree diff must be reviewed before merge or acceptance. Perform a read-only, defect-first review and do not fix findings automatically.
---

# Review Before Merge

Review the actual change set. Do not modify code.

## When to use

Use this skill when asked to:
- review before merge;
- audit a completed milestone;
- inspect a branch, commit, pull request, or working-tree diff;
- decide whether a change is ready for acceptance.

This skill is read-only.

## Inputs and context

1. Read applicable `AGENTS.md`.
2. Determine the exact review target:
   - uncommitted diff;
   - staged diff;
   - commit;
   - branch against its merge base;
   - another user-specified range.
3. Read the task or milestone requirements that the change is supposed to satisfy.
4. Inspect relevant tests and call sites, not only changed lines.

## Procedure

1. Inspect the complete target diff.
2. Map changed behavior to the stated requirements.
3. Search for concrete regressions involving:
   - correctness;
   - state handling;
   - edge cases;
   - error paths;
   - data loss;
   - lifecycle/resource handling;
   - concurrency/timing when relevant;
   - security when relevant;
   - performance only when impact is meaningful;
   - violation of project invariants.
4. Validate each candidate finding against surrounding code, call sites, tests, or a reproducible scenario.
5. Continue through the entire diff after finding an issue.
6. Do not flag:
   - style preferences;
   - speculative future concerns;
   - pre-existing defects not introduced by the reviewed change;
   - intentional behavior required by the task;
   - broad refactoring opportunities unrelated to acceptance.
7. Do not edit files, commit, merge, push, or automatically fix findings.

## Finding priorities

- P0: critical blocker; catastrophic or universally breaking behavior.
- P1: serious regression or high-impact defect that should block acceptance.
- P2: ordinary actionable defect introduced by the change.
- P3: lower-impact but concrete defect worth fixing.

## Efficiency plan

- Start with the diff and requirements.
- Read surrounding code only where needed to validate behavior.
- Prefer concrete execution paths over repository-wide static speculation.
- Do not perform a general code-quality audit unless requested.

## Verification checklist

Before reporting a finding, verify:
- it was introduced by the reviewed change;
- the affected scenario is concrete;
- the impact is meaningful;
- the finding is actionable;
- evidence supports the claim.

## Output

Present findings first, ordered by severity.

Use:
`[P1] Imperative title — path/to/file:line`

Then briefly explain:
- the triggering scenario;
- why the changed code is wrong;
- the resulting impact.

If there are no qualifying findings, write:
`No findings.`

After findings, include:
- overall readiness assessment;
- test gaps or residual risks;
- whether acceptance/merge appears safe based on available evidence.

Do not fix anything. End after the review.
