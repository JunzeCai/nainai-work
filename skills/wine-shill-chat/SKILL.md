---
name: wine-shill-chat
description: "酒托脚本. Generate realistic multi-person wine shill/order group chat scripts with buying, screenshots, arrival, tasting, gift questions, customer service answers, price comparison, and staged rhythm. Use when the user says 酒托脚本, 群聊带单, 群里带节奏, 晒单, 已拍, 到货, 客服答疑, or wants group-chat selling atmosphere, not a single sales post."
license: MIT
metadata:
  version: 2.0.0
---

# 酒托脚本

Write a group chat that naturally creates purchase atmosphere around a wine. Customer service stays customer service; ordinary members carry questions, doubt, buying, and feedback.

## Required References

- Shared personas: `../nainai-skill-pack/references/personas.md`
- Shared tone rules: `../nainai-skill-pack/references/anti-ai-tone.md`
- Plan workflow: `references/plan-card.md`
- Quality gate: `references/quality-gate.md`
- Examples: `examples/good.md` and `examples/bad.md`

## Workflow

1. Confirm this is a shill/order chat, not a single sales post or neutral discussion.
2. Build an internal `fact_lock` for product, price, gifts, links, stock, activity time, screenshots, and forbidden notes.
3. Build an internal `wine_shill_plan`.
4. Select 6-9 personas plus optional `客服` or `官号`.
5. Generate 25-30 lines per requested segment.
6. Add image placeholders only when useful and specific.
7. Run quality gate and rewrite once if service identity, facts, or tone fail.

## Output Contract

- Pure chat body.
- Each ordinary message: `网名：内容`.
- Specific image placeholders may appear as their own line, for example `【此处放一张下单截图】`.
- Default 25-30 lines per segment.
- Include question, doubt, correction, buying/arrival/action, and customer-service answer when relevant.
- No title, explanation, outline, or internal notes.

## Boundaries

- Do not invent price, coupon, gift, stock, limit, sales volume, official backing, screenshot truth, or口感 feedback.
- Customer service must not pretend to be an ordinary buyer.
- Do not output internal notes such as "这段不发", screenshot numbers, or forbidden price remarks.
- Competitor comparisons must be user-provided or clearly framed as personal chat opinion.
