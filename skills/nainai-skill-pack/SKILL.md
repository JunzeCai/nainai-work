---
name: nainai-skill-pack
description: "奶奶 Skill Pack router. Use for 识图喝酒, 卖货话术, 水群脚本, 酒托脚本, 找话题, image-based drinking group chats, official sales copy, natural group chat scripts, wine shill scripts, topic discovery, prompt optimization, quality checks, or routing among the nainai skills."
---

# 奶奶 Skill Pack

Use this skill as the first stop for the white-liquor private-domain writing workflows. It routes to one focused skill, loads shared references only when needed, and keeps generation structured before writing final copy.

## Route First

Read `references/routing.md` when the task type is unclear. The user-facing Chinese commands are:

- `识图喝酒`: use `image-drinking-chat`.
- `卖货话术`: use `sales-official-copy`.
- `水群脚本`: use `natural-group-chat`.
- `酒托脚本`: use `wine-shill-chat`.
- `找话题`: use `wine-topic-finder`.

## Shared References

Load only what the target workflow needs:

- `references/personas.md`: shared nickname pool and role mapping.
- `references/anti-ai-tone.md`: banned AI-ish wording and repair rules.
- `references/workflow-contracts.md`: common intermediate cards and audit fields.
- `references/feedback-tags.md`: tags for manual review and future iteration.
- `references/architecture.md`: naming, packaging, and maintenance rules.
- `references/host-adapters.md`: Codex/Kimi/Claude portability notes.
- `references/source-notes.md`: external sources and design decisions for maintainers.
- Target skill references under `../<skill>/references/`.

## Common Operating Contract

1. Classify the task by final use.
2. Extract facts and unknowns before writing.
3. Build the target intermediate card.
4. Generate one focused final output unless the user asks for variants.
5. Run the target quality gate.
6. If the quality gate fails, rewrite once before answering.

Do not expose internal cards unless the user asks for audit, debugging, or optimization. For ordinary writing requests, output the final artifact only.
