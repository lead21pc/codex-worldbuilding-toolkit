# Contributing

Keep changes narrow, evidence-based, and easy to review.

- Preserve each skill's semantic purpose and authorization boundaries.
- Preserve the behavioral CI core invariants and keep advanced modules optional.
- Do not broaden scope casually or add project-specific assumptions to generic components.
- Do not add rules merely because they sound useful.
- Avoid duplicate semantic rules across an entrypoint and its references.
- Motivate behavioral changes with a concrete failure mode or demonstrated need.
- Update relevant tests and neutral examples when behavior changes.
- Run `python scripts/validate_repository.py` and applicable script checks before submitting changes.

For `worldbuilding-ci`:

- Tie behavioral changes to a concrete failure mode.
- Keep CORE usable without WORLD_MODEL, SIMULATION, or AUDIT.
- Do not impose a universal source hierarchy or user-specific language preference.
- Keep FULL_PROFILE behavior aligned with the complete modular configuration.
- Treat structural checks as distinct from runtime semantic evidence.

For `worldbuilding-source-audit`:

- Keep it setting-neutral.
- Do not impose a universal source or canon model.
- Discover source authority from the target project.
- Preserve unresolved authority instead of inventing precedence.

Pull requests should state the motivating case, affected component, semantic impact, and validation performed.
