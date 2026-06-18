#!/usr/bin/env python3
"""Validate the Nainai Skill Pack structure."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_SKILLS = {
    "nainai-skill-pack": "奶奶 Skill Pack",
    "image-drinking-chat": "识图喝酒",
    "sales-official-copy": "卖货话术",
    "natural-group-chat": "水群脚本",
    "wine-shill-chat": "酒托脚本",
    "wine-topic-finder": "找话题",
}

LEGACY_TERMS = [
    "baijiu-group-chat",
    "sales-copy",
    "group-chat-script",
    "group-chat-wine-shill",
    "topic-discovery-agent",
    "kimi-webbridge",
    "ReadMediaFile",
    "prompts/",
    "label_database",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter fence")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter fence")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_plugin(errors: list[str]) -> None:
    path = ROOT / ".codex-plugin" / "plugin.json"
    if not path.exists():
        fail(errors, "missing .codex-plugin/plugin.json")
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ["name", "version", "description", "author", "interface", "skills"]:
        if key not in data:
            fail(errors, f"plugin.json missing {key}")
    if data.get("skills") != "./skills/":
        fail(errors, "plugin.json skills must be ./skills/")


def validate_skills(errors: list[str]) -> None:
    for skill_id, chinese_name in EXPECTED_SKILLS.items():
        skill_dir = ROOT / "skills" / skill_id
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.exists():
            fail(errors, f"missing skill {skill_id}/SKILL.md")
            continue
        try:
            frontmatter = parse_frontmatter(skill_path)
        except ValueError as exc:
            fail(errors, f"{skill_path}: {exc}")
            continue
        if frontmatter.get("name") != skill_id:
            fail(errors, f"{skill_path}: name must be {skill_id}")
        if chinese_name not in skill_path.read_text(encoding="utf-8"):
            fail(errors, f"{skill_path}: missing Chinese command {chinese_name}")
        if skill_id != "nainai-skill-pack":
            for subdir in ["references", "examples", "evals", "agents"]:
                if not (skill_dir / subdir).exists():
                    fail(errors, f"{skill_id}: missing {subdir}/")
            eval_path = skill_dir / "evals" / "evals.json"
            if eval_path.exists():
                data = json.loads(eval_path.read_text(encoding="utf-8"))
                if data.get("skill_name") != skill_id:
                    fail(errors, f"{eval_path}: skill_name must be {skill_id}")
                evals = data.get("evals")
                if not isinstance(evals, list) or not evals:
                    fail(errors, f"{eval_path}: evals must be a non-empty list")
                for item in evals:
                    for key in ["id", "prompt", "expected_output", "assertions"]:
                        if key not in item:
                            fail(errors, f"{eval_path}: eval {item.get('id', '<missing id>')} missing {key}")
                    if not isinstance(item.get("assertions"), list) or not item.get("assertions"):
                        fail(errors, f"{eval_path}: eval {item.get('id', '<missing id>')} assertions must be non-empty")


def validate_router(errors: list[str]) -> None:
    router = ROOT / ".agents" / "skills" / "nainai-work-router" / "SKILL.md"
    if not router.exists():
        fail(errors, "missing .agents/skills/nainai-work-router/SKILL.md")
        return
    frontmatter = parse_frontmatter(router)
    if frontmatter.get("name") != "nainai-work-router":
        fail(errors, "repo auto-loader name must be nainai-work-router")
    trigger_path = ROOT / "skills" / "nainai-skill-pack" / "evals" / "trigger_queries.json"
    if not trigger_path.exists():
        fail(errors, "missing skills/nainai-skill-pack/evals/trigger_queries.json")
        return
    data = json.loads(trigger_path.read_text(encoding="utf-8"))
    queries = data.get("queries")
    if not isinstance(queries, list) or not queries:
        fail(errors, f"{trigger_path}: queries must be a non-empty list")
    valid_targets = set(EXPECTED_SKILLS) - {"nainai-skill-pack"}
    for item in queries or []:
        target = item.get("should_trigger")
        if target is not None and target not in valid_targets:
            fail(errors, f"{trigger_path}: invalid trigger target {target}")
        for key in ["id", "query", "should_trigger"]:
            if key not in item:
                fail(errors, f"{trigger_path}: query {item.get('id', '<missing id>')} missing {key}")


def scan_legacy_terms(errors: list[str]) -> None:
    targets = [ROOT / "skills", ROOT / ".agents", ROOT / ".codex-plugin"]
    for base in targets:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if path.name == ".DS_Store":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for term in LEGACY_TERMS:
                if term in text:
                    fail(errors, f"{path.relative_to(ROOT)} contains legacy term {term}")
            if re.search(r"TODO|TBD|\[TODO", text):
                fail(errors, f"{path.relative_to(ROOT)} contains placeholder text")


def main() -> int:
    errors: list[str] = []
    validate_plugin(errors)
    validate_skills(errors)
    validate_router(errors)
    scan_legacy_terms(errors)
    if errors:
        print("Nainai Skill Pack validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Nainai Skill Pack validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
