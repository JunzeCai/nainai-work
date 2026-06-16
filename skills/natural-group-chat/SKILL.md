---
name: natural-group-chat
description: "水群脚本 / 群聊脚本. Generate realistic multi-person wine-friend group chat scripts around a topic, wine, event, or social discussion. Use when the user says 水群, 群聊脚本, 多人聊天, 酒友群聊天, debate, banter, correction, and topic-driven scripts, not direct sales posts or shill/order flows."
license: MIT
metadata:
  version: 2.0.0
---

# 水群脚本

Write a realistic wine-friend group chat. It should feel like watching a live group, not reading an essay split across names.

## Required References

- Shared personas: `../nainai-skill-pack/references/personas.md`
- Shared tone rules: `../nainai-skill-pack/references/anti-ai-tone.md`
- Workflow: `references/workflow.md`
- Quality gate: `references/quality-gate.md`
- Examples: `examples/good.md` and `examples/bad.md`

## Workflow

1. Confirm this is a discussion script, not sales copy or shill/order chat.
2. If the user asks for latest, recent, stock, fund, price, news, or auto topic, search before writing and cite sources after the chat.
3. Build an internal `beat_sheet` with opening heat, mistake, correction, change of mind, and ending action.
4. Select 6-9 personas.
5. Generate 30-40 lines.
6. Run the quality gate and rewrite once if the chat feels like one person or a host script.

## Output Contract

- Each line: `网名：内容`.
- Default 30-40 lines.
- At least 6 roles.
- First 5 lines must create heat.
- Include disagreement, correction, a wrong take, and a small change of mind.
- No title, explanation, outline, or placeholders.
- If sources were used, add a short `素材参考` section after the chat.

## Boundaries

- Do not invent prices, current events, stock movement, fund movement, or industry news.
- For finance topics, stay within white-liquor stocks, funds, base liquor, or liquor industry signals.
- If the topic is a specific wine, discuss more than口感: scene, price band, brand story, packaging, or buying caution when supported.
