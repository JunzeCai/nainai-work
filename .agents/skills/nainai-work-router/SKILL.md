---
name: nainai-work-router
description: "Repo auto-loader for the nainai white-liquor Skill Pack. Use when the user asks for 识图喝酒, 卖货话术, 水群脚本, 酒托脚本, 找话题, private-domain content, or wants to route among those workflows."
---

# Nainai Work Router

This repo-scoped skill is the current-project entrypoint. It keeps Codex auto-discovery light and points to the portable core under `skills/`.

## Workflow

1. Read `skills/nainai-skill-pack/SKILL.md`.
2. Route the request using `skills/nainai-skill-pack/references/routing.md`.
3. Read only the target task skill and the shared references it asks for.
4. Generate the requested artifact directly unless the target skill requires missing facts, image inputs, or live search.

## Packaging

- Portable skill core: `skills/`
- Codex plugin wrapper: `.codex-plugin/plugin.json`
- Current repo auto-loader: `.agents/skills/nainai-work-router/SKILL.md`
