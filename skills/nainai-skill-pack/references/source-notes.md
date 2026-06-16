# Source Notes

These notes summarize external references used to shape the pack. Keep this file short; it is for maintainers, not runtime generation.

## Sources Reviewed

- OpenAI `openai/skills` catalog: treats skills as folders of instructions, scripts, and resources that agents can discover and reuse. It also documents installing curated or GitHub-hosted skills with `$skill-installer`.
- Agent Skills specification: requires `SKILL.md`, frontmatter `name` and `description`, lowercase hyphenated names, name matching the parent directory, optional `references/`, `scripts/`, and `assets/`, and progressive disclosure.
- Agent Skills best practices: favors real expertise, concise `SKILL.md`, coherent units, defaults over menus, gotchas, templates, checklists, validation loops, and bundled scripts when reusable logic would otherwise be rewritten.
- Agent Skills description optimization: emphasizes that `description` drives activation and should focus on user intent, include realistic trigger phrases, and be tested with should-trigger and should-not-trigger queries.
- Agent Skills evaluation guide: recommends realistic prompts, expected outputs, assertions, baseline comparison, and iteration.
- Agent Skills scripts guide: recommends self-contained scripts, helpful errors, `--help`, structured output, and moving complex repeated commands into scripts.

## Decisions Applied

- Stable skill IDs are English lowercase hyphen names; Chinese commands live in descriptions and UI metadata.
- Each task skill is a coherent unit with a short `SKILL.md` and focused `references/`.
- Output evals use `prompt`, `expected_output`, and `assertions`.
- Trigger evals live under `skills/nainai-skill-pack/evals/trigger_queries.json`.
- Reusable validation is in `scripts/validate_pack.py` and `scripts/run_evals.py`.
- No MCP server is bundled until there is an actual tool layer need.
