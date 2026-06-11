#!/usr/bin/env python3
"""Print eval coverage for manual or agent-assisted review."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    total = 0
    for eval_path in sorted((ROOT / "skills").glob("*/evals/evals.json")):
        skill = eval_path.parts[-3]
        data = json.loads(eval_path.read_text(encoding="utf-8"))
        evals = data["evals"]
        print(f"\n## {skill} ({len(evals)} evals)")
        for item in evals:
            total += 1
            assertions = "; ".join(item.get("assertions", []))
            print(f"- {item['id']}: {item['prompt']} -> {assertions}")
    print(f"\nTotal evals: {total}")
    trigger_path = ROOT / "skills" / "nainai-skill-pack" / "evals" / "trigger_queries.json"
    if trigger_path.exists():
        data = json.loads(trigger_path.read_text(encoding="utf-8"))
        queries = data["queries"]
        print(f"\n## trigger queries ({len(queries)} queries)")
        for item in queries:
            target = item["should_trigger"] or "<none>"
            print(f"- {item['id']}: {item['query']} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
