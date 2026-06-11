# Architecture

This pack has three layers.

## 1. Portable Core

`skills/` is the portable core. It can be copied into Codex, Claude, Kimi Work, or another agent that understands folder-based skills.

Stable skill IDs:

| Chinese command | Stable skill ID | Responsibility |
| --- | --- | --- |
| `识图喝酒` | `image-drinking-chat` | Image or scene description to short wine-friend chat |
| `卖货话术` | `sales-official-copy` | Fact-locked official/private-domain sales copy |
| `水群脚本` | `natural-group-chat` | Natural topic-driven multi-person group chat |
| `酒托脚本` | `wine-shill-chat` | Group chat selling rhythm with orders, screenshots, and service answers |
| `找话题` | `wine-topic-finder` | Wine-related topic and news discovery |

Keep skill IDs lowercase ASCII with hyphens for cross-agent compatibility. Put Chinese names in descriptions and `agents/openai.yaml`.

## 2. Codex Plugin Wrapper

`.codex-plugin/plugin.json` packages the whole `skills/` directory for Codex installation and sharing.

The plugin should not contain MCP servers until there is a real tool need such as saving feedback, running searches, or writing spreadsheets.

## 3. Repo Auto-Loader

`.agents/skills/nainai-work-router` exists only for this repository. It avoids duplicating the plugin router name and points Codex to the portable core.

## Maintenance Rules

- Keep `SKILL.md` under 100 lines unless the workflow truly needs more.
- Put detailed workflow, examples, and quality checks in `references/`, `examples/`, and `evals/`.
- When adding a new skill, add a row to `references/routing.md`, `references/architecture.md`, and `scripts/validate_pack.py`.
- Keep evals small and assertion-oriented. They are guardrails, not a benchmark suite.
- Keep trigger coverage in `evals/trigger_queries.json` with both positive and near-miss negative prompts.
- Do not reintroduce hard-coded host tools such as one specific browser bridge.
