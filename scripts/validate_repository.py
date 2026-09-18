#!/usr/bin/env python3
"""Validate the public skill repository without third-party dependencies."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
WORLD_BUILDING_CI_ROOT = ROOT / "worldbuilding-ci"
EXPECTED_SKILLS = {
    "ci-behavior-engineering",
    "git-test-branch",
    "milestone-executor",
    "review-before-merge",
    "systematic-debugging",
    "worldbuilding-source-audit",
}
EXPECTED_WORLD_BUILDING_CI_FILES = {
    "core/GENERIC_WORLDBUILDING_CI_CORE.md",
    "modules/AUDIT.md",
    "modules/SIMULATION.md",
    "modules/WORLD_MODEL.md",
    "profiles/FULL_PROFILE.md",
    "examples/full-example.md",
    "examples/minimal-example.md",
}


def forbidden_terms() -> list[str]:
    slash = chr(92)
    return [
        "aether" + "fire",
        "sheep" + "lark",
        "c:" + slash + "users" + slash,
        "/" + "users" + "/",
        "/" + "home" + "/",
        "chatgpt-" + "conversation",
        "memory_" + "summary",
        "rollout_" + "summaries",
        "viet" + "namese",
    ]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = read_text(path).splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing frontmatter delimiter") from exc

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key or not value:
            raise ValueError(f"empty frontmatter key or value: {line!r}")
        if key in data:
            raise ValueError(f"duplicate frontmatter key: {key}")
        data[key] = value
    return data


def parse_mapping_yaml(path: Path) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]

    for number, raw in enumerate(read_text(path).splitlines(), start=1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if "\t" in raw:
            raise ValueError(f"line {number}: tabs are not supported")
        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2:
            raise ValueError(f"line {number}: indentation must use two spaces")
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):(?:\s+(.*))?", raw.strip())
        if not match:
            raise ValueError(f"line {number}: unsupported YAML structure")

        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        key, scalar = match.groups()
        if key in parent:
            raise ValueError(f"line {number}: duplicate key {key!r}")

        if scalar is None:
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
            continue

        if scalar in {"true", "false"}:
            parent[key] = scalar == "true"
        elif len(scalar) >= 2 and scalar[0] == scalar[-1] and scalar[0] in {'"', "'"}:
            parent[key] = scalar[1:-1]
        else:
            raise ValueError(f"line {number}: strings must be quoted")
    return root


def validate_skill(skill_dir: Path, errors: list[str]) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
        return

    try:
        metadata = parse_frontmatter(skill_file)
    except ValueError as exc:
        errors.append(f"{skill_file.relative_to(ROOT)}: {exc}")
        return

    if metadata.get("name") != skill_dir.name:
        errors.append(f"{skill_file.relative_to(ROOT)}: name must match directory")
    if not metadata.get("description"):
        errors.append(f"{skill_file.relative_to(ROOT)}: description is required")
    deprecated_key = "disable-model-" + "invocation"
    if deprecated_key in metadata:
        errors.append(f"{skill_file.relative_to(ROOT)}: deprecated metadata remains")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if agent_file.exists():
        try:
            agent = parse_mapping_yaml(agent_file)
        except ValueError as exc:
            errors.append(f"{agent_file.relative_to(ROOT)}: {exc}")
        else:
            interface = agent.get("interface")
            if not isinstance(interface, dict):
                errors.append(f"{agent_file.relative_to(ROOT)}: interface mapping is required")
            else:
                for key in ("display_name", "short_description", "default_prompt"):
                    if not isinstance(interface.get(key), str) or not interface[key].strip():
                        errors.append(f"{agent_file.relative_to(ROOT)}: interface.{key} is required")
                prompt = interface.get("default_prompt", "")
                if isinstance(prompt, str) and f"${skill_dir.name}" not in prompt:
                    errors.append(f"{agent_file.relative_to(ROOT)}: default_prompt must name the skill")
            policy = agent.get("policy", {})
            if not isinstance(policy, dict) or not isinstance(
                policy.get("allow_implicit_invocation"), bool
            ):
                errors.append(
                    f"{agent_file.relative_to(ROOT)}: policy.allow_implicit_invocation must be boolean"
                )


def validate_worldbuilding_ci(errors: list[str]) -> None:
    if not WORLD_BUILDING_CI_ROOT.is_dir():
        errors.append("worldbuilding-ci directory is missing")
        return

    actual = {
        path.relative_to(WORLD_BUILDING_CI_ROOT).as_posix()
        for path in WORLD_BUILDING_CI_ROOT.rglob("*")
        if path.is_file()
    }
    if actual != EXPECTED_WORLD_BUILDING_CI_FILES:
        missing = sorted(EXPECTED_WORLD_BUILDING_CI_FILES - actual)
        extra = sorted(actual - EXPECTED_WORLD_BUILDING_CI_FILES)
        errors.append(
            f"worldbuilding CI inventory mismatch; missing={missing}, extra={extra}"
        )

    core_path = WORLD_BUILDING_CI_ROOT / "core" / "GENERIC_WORLDBUILDING_CI_CORE.md"
    if core_path.is_file():
        core = read_text(core_path)
        for module_name in ("WORLD_MODEL.md", "SIMULATION.md", "AUDIT.md"):
            if module_name in core:
                errors.append(f"{core_path.relative_to(ROOT)}: depends on {module_name}")

    profile_path = WORLD_BUILDING_CI_ROOT / "profiles" / "FULL_PROFILE.md"
    if profile_path.is_file():
        profile = read_text(profile_path)
        required = (
            "GENERIC_WORLDBUILDING_CI_CORE.md",
            "WORLD_MODEL.md",
            "SIMULATION.md",
            "AUDIT.md",
        )
        for component in required:
            if component not in profile:
                errors.append(
                    f"{profile_path.relative_to(ROOT)}: missing component {component}"
                )


def validate_markdown_links(errors: list[str]) -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in pattern.findall(read_text(path)):
            if re.match(r"^(?:https?://|mailto:|#)", target):
                continue
            if not (path.parent / target).exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link {target!r}")


def validate_python(errors: list[str]) -> None:
    for path in ROOT.rglob("*.py"):
        if ".git" in path.parts:
            continue
        try:
            ast.parse(read_text(path), filename=str(path))
        except SyntaxError as exc:
            errors.append(f"{path.relative_to(ROOT)}: Python syntax error: {exc}")


def scan_repository(errors: list[str]) -> None:
    secret_patterns = [
        re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
        re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
        re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    ]
    deprecated = "disable-model-" + "invocation"

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            errors.append(f"{path.relative_to(ROOT)}: unexpected non-UTF-8 file")
            continue
        lowered = text.casefold()
        for term in forbidden_terms():
            if term.casefold() in lowered:
                errors.append(f"{path.relative_to(ROOT)}: forbidden private string detected")
        if deprecated in lowered:
            errors.append(f"{path.relative_to(ROOT)}: deprecated metadata detected")
        for pattern in secret_patterns:
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: possible secret or personal identifier")


def main() -> int:
    errors: list[str] = []
    if not SKILLS_ROOT.is_dir():
        errors.append("skills directory is missing")
    else:
        actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
        if actual != EXPECTED_SKILLS:
            missing = sorted(EXPECTED_SKILLS - actual)
            extra = sorted(actual - EXPECTED_SKILLS)
            errors.append(f"skill inventory mismatch; missing={missing}, extra={extra}")
        for skill_dir in sorted(
            (path for path in SKILLS_ROOT.iterdir() if path.is_dir()),
            key=lambda path: path.name,
        ):
            validate_skill(skill_dir, errors)

    validate_worldbuilding_ci(errors)

    validate_markdown_links(errors)
    validate_python(errors)
    scan_repository(errors)

    if errors:
        print("VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "VALIDATION: PASS "
        f"({len(EXPECTED_SKILLS)} skills, "
        f"{len(EXPECTED_WORLD_BUILDING_CI_FILES)} worldbuilding CI files)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
