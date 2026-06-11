# Host Adapters

The workflows are portable. Tool use changes by host.

## Codex

- Skill discovery: use plugin install or repo `.agents/skills`.
- Explicit invocation: `$nainai-skill-pack`, `$image-drinking-chat`, `$sales-official-copy`, `$natural-group-chat`, `$wine-shill-chat`, `$wine-topic-finder`.
- Search: use available web/browser tools when recency matters.
- Validation: run `python3 scripts/validate_pack.py`.

## Kimi Work

- Load the relevant skill folder or the whole `skills/` directory.
- If Kimi has image reading, map image analysis to `image_scene_card`.
- If Kimi has search/browser bridge, use it for `wine-topic-finder` and current facts, but treat failures as a graceful degradation.

## Claude or Other Agents

- Load `skills/nainai-skill-pack/SKILL.md` first, then the routed skill.
- Use the same intermediate cards: `image_scene_card`, `fact_lock`, `beat_sheet`, `wine_shill_plan`, `topic_card`.
- If the host cannot read images, ask the user for a brief image description before using `image-drinking-chat`.

## Degradation Rules

- No image tool: ask for visible text, bottle visibility, dishes, and scene.
- No search tool: avoid freshness claims and label output as evergreen/contextual.
- No file writes: skip feedback persistence and provide tags inline only if requested.
