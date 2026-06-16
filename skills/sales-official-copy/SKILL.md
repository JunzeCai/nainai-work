---
name: sales-official-copy
description: "卖货话术. Write private-domain official-account or WeChat sales copy for white liquor, tea, food, or daily goods. Use when the user says 卖货话术, 官号文案, 发群卖货, 朋友圈文案, coupon, restock, final-call, holiday stock-up, or link-based copy. Must lock facts before writing."
license: MIT
metadata:
  version: 2.0.0
---

# 卖货话术

Write one sendable private-domain sales post. The core rule is: no fact outside the fact lock.

## Required References

- Shared tone rules: `../nainai-skill-pack/references/anti-ai-tone.md`
- Fact lock: `references/fact-lock.md`
- Templates and voice modes: `references/templates.md`
- Quality gate: `references/quality-gate.md`
- Examples: `examples/good.md` and `examples/bad.md`

## Workflow

1. Classify final use. If the user wants multi-person chat, route to another skill.
2. Build an internal `fact_lock`.
3. Choose one template: `limited-drop`, `holiday-stockup`, `return-sale`, `final-call`, `trace-tail`, or `restock-tail`.
4. Choose one voice mode: `official-warm`, `service-notice`, `old-group-owner`, or `story-selling`.
5. Write one final post.
6. Run `references/quality-gate.md`; delete or rewrite any unsupported claim.

## Output Contract

- Output final copy only unless the user asks for audit.
- One version only.
- Default 3-4 short paragraphs, 12-28 lines.
- Keep user links exactly unchanged.
- Put action instruction near the end.
- If facts are sparse, write shorter copy instead of filling with invented benefits.

## Fact Boundary

Only write facts from:

- User-provided facts.
- User-provided links, preserved exactly.
- Facts confirmed by search or supplied source material.

Never invent price, coupon price, gift, stock, deadline, limit, sales volume, awards, official backing, year, batch, or channel rules.
