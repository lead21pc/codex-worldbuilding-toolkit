---
name: git-test-branch
description: Use only when the user explicitly asks to create, switch to, prepare, or manage a temporary Git test branch for isolated milestone work. Keep destructive and externally visible Git actions gated behind explicit user instruction.
---

# Git Test Branch

Create and use an isolated local branch safely. Do not push, merge, delete, rewrite history, or discard work unless explicitly instructed.

## When to use

Invoke this skill explicitly for requests such as:
- create a test branch for this milestone;
- switch to an isolated branch before making changes;
- prepare a branch for testing;
- inspect whether it is safe to create a test branch.

Do not invoke implicitly for ordinary coding tasks.

## Inputs and context

Before any branch-changing command:
1. Read applicable `AGENTS.md`.
2. Inspect:
   - `git status --short --branch`;
   - current branch;
   - existing local branches;
   - worktree state.
3. Determine the requested base branch and branch name when provided.
4. Preserve all existing user work.

## Procedure

1. Check the working tree.
   - If tracked or untracked changes exist, do not discard, reset, clean, stash, or commit them automatically.
   - Determine whether switching branches can preserve them safely.
   - If the requested operation risks overwriting work, stop and report the exact blocker.

2. Confirm the base.
   - Use the current branch unless the user explicitly names another base.
   - Do not pull, fetch, rebase, or update the base unless requested or required by an explicit instruction.

3. Create or switch to the requested test branch.
   - Prefer a descriptive branch name tied to the task.
   - Never silently reuse an unrelated existing branch.

4. Verify branch state.
   - Confirm current branch.
   - Confirm the user's pre-existing work remains intact.
   - Report whether the working tree is clean or intentionally dirty.

5. Hand control back to the requested implementation workflow.

## Forbidden without explicit instruction

Do not:
- `git push`;
- merge;
- rebase;
- cherry-pick;
- delete branches;
- force anything;
- `reset --hard`;
- `clean -fd`;
- discard local modifications;
- rewrite commits;
- amend commits;
- create tags;
- publish releases.

If one of these becomes necessary, stop and ask for explicit instruction rather than inferring permission.

## Efficiency plan

- Use only the Git commands needed to establish safe branch state.
- Do not fetch remote history unless it affects the requested operation.
- Do not inspect unrelated branches.

## Pitfalls and fixes

- Symptom: branch switch would overwrite local changes.
  - Fix: stop; report conflicting paths and safe options without choosing one automatically.

- Symptom: requested branch already exists.
  - Fix: verify its purpose and state before switching; do not overwrite it.

- Symptom: test branch diverged from the intended base.
  - Fix: report the divergence; do not rebase or reset without instruction.

## Verification checklist

Confirm:
- current branch is the intended test branch;
- the intended base was used;
- no local work was discarded;
- no destructive command ran;
- no remote-visible action occurred;
- repository status is reported accurately.
