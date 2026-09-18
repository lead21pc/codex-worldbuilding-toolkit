# Contributing

Keep changes narrow, evidence-based, and easy to review.

- Preserve each skill's semantic purpose and authorization boundaries.
- Do not broaden scope casually or add project-specific assumptions to generic skills.
- Do not add rules merely because they sound useful.
- Avoid duplicate semantic rules across an entrypoint and its references.
- Motivate behavioral changes with a concrete failure mode or demonstrated need.
- Update relevant tests and neutral examples when behavior changes.
- Run `python scripts/validate_repository.py` and applicable script checks before submitting changes.

For `worldbuilding-source-audit`:

- Keep it setting-neutral.
- Do not impose a universal source or canon model.
- Discover source authority from the target project.
- Preserve unresolved authority instead of inventing precedence.

Pull requests should state the motivating case, affected skill, semantic impact, and validation performed.
