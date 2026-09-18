---
name: systematic-debugging
description: Use when a bug, regression, test failure, runtime error, incorrect behavior, or unexplained mismatch must be diagnosed before editing. Do not use for ordinary feature implementation without a failure to investigate.
---

# Systematic Debugging

Diagnose before changing code. Prefer evidence over plausible guesses.

## When to use

Use this skill for:
- reproducible or intermittent bugs;
- regressions after a change;
- failing tests, crashes, exceptions, incorrect UI behavior, or state mismatches;
- behavior that differs from a stated specification;
- debugging requests where the root cause is not already demonstrated.

Do not use this skill merely because code is being edited.

## Inputs and context

Before editing:
1. Read the applicable `AGENTS.md` files.
2. Read the task, expected behavior, and any reproduction steps.
3. Inspect current Git status and relevant recent diff when the failure may be change-related.
4. Locate the smallest relevant execution path, tests, logs, and call sites.
5. Separate:
   - observed failure;
   - verified facts;
   - hypotheses;
   - unverified assumptions.

## Procedure

1. Reproduce or otherwise establish the failure.
   - Prefer an existing test or deterministic command.
   - If reproduction is impossible, state what evidence is available and keep conclusions provisional.

2. Bound the failure.
   - Identify the first known-good and first known-bad state when possible.
   - Narrow the affected component, input, state transition, or call path.
   - Do not scan or refactor unrelated areas without evidence.

3. Generate the minimum useful hypothesis set.
   - Rank hypotheses by evidence and diagnostic value.
   - Prefer checks that eliminate multiple hypotheses at once.

4. Test hypotheses before editing.
   - Inspect values, control flow, state transitions, ownership/lifetime, error paths, timing, and external assumptions as relevant.
   - Add temporary instrumentation only when existing evidence is insufficient.

5. Identify the root cause.
   - A root-cause claim must explain both the observed failure and why the current code produces it.
   - Do not treat correlation or a nearby suspicious line as proof.

6. Apply the smallest fix that addresses the demonstrated cause.
   - Preserve unrelated behavior.
   - Avoid opportunistic cleanup, dependency changes, architecture changes, or broad refactors.

7. Verify.
   - Re-run the original reproduction.
   - Run the narrowest relevant tests first, then broader tests when justified.
   - Inspect the final diff for unrelated changes.
   - Remove temporary instrumentation unless explicitly useful.

## Efficiency plan

- Start from the failure path, not the entire repository.
- Reuse already-read files and command output.
- Prefer one discriminating experiment over many speculative edits.
- Stop expanding the investigation once the root cause is demonstrated and the fix is verified.
- If evidence is insufficient, report the uncertainty rather than inventing a cause.

## Pitfalls and fixes

- Symptom: multiple files edited before the failure is reproduced.
  - Likely cause: solution-first debugging.
  - Fix: revert speculative edits and establish the failure first.

- Symptom: changing architecture to fix a local defect.
  - Likely cause: scope drift.
  - Fix: return to the demonstrated failure path and implement the minimum causal fix.

- Symptom: test passes but original behavior is still wrong.
  - Likely cause: verification did not match the reproduction.
  - Fix: verify against the original failure condition.

- Symptom: root cause is stated without direct evidence.
  - Likely cause: hypothesis promoted to conclusion.
  - Fix: identify the missing discriminating check and run it.

## Verification checklist

Before declaring success, confirm:
- the original failure was established;
- the causal mechanism is supported by evidence;
- the fix targets that mechanism;
- the original failure no longer reproduces;
- relevant tests pass;
- no temporary debug artifacts remain;
- the final diff contains no unrelated refactor or cleanup;
- remaining uncertainty or untested paths are stated explicitly.
