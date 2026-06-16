---
name: wine-topic-finder
description: "找话题. Discover wine-related topics, news signals, social-platform angles, and group-chat seeds. Use when the user says 找话题, 想话题, 选题, 热点, 酒类新闻, Xiaohongshu/Weibo style signals, industry discussion, or chat ideas. Search when recency or platform reality matters."
license: MIT
metadata:
  version: 2.0.0
---

# 找话题

Find wine-related topic cards that can become group chat scripts. The output is not a generic idea list; every topic needs an entity anchor, conflict, and opening line.

## Required References

- Search and fallback workflow: `references/search-workflow.md`
- Topic card schema: `references/topic-card.md`
- Quality gate: `references/quality-gate.md`
- Examples: `examples/good.md` and `examples/bad.md`

## Workflow

1. Determine whether the user needs live/recent/platform-backed topics.
2. If recent, latest, news, platform trend, stock, policy, or auto-topic is requested, search before generating. Use available search/browser tools; do not require one hard-coded bridge.
3. Convert source signals into `signal_cards`.
4. Generate 5-10 `topic_cards`.
5. Run quality gate.

## Output Contract

For each topic card include:

- `title`
- `entity_anchor`
- `why_now`
- `opening_line`
- `conflict_points`
- `suggested_roles`
- `script_path`
- `source_notes` when searched

## Boundaries

- All topics must be wine-related or naturally bridge to wine consumption, wine business, drinking scenes, gifting, channels, prices, or social discussion.
- For current facts, cite source title, date, and link when available.
- If search is unavailable, say the batch is based on evergreen/historical context and avoid claiming freshness.
- Do not force unrelated celebrity/political/social noise into wine topics.
