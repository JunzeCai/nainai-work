---
name: wine-shill-chat
description: "酒托脚本. Generate realistic multi-person wine shill/order group chat scripts and campaign packages with 官号+云中客, buying, screenshots, arrival, tasting, gift questions, customer-service answers, old/new group variants, preheat-sale-night rhythms, price comparison, and staged rhythm. Use when the user says 酒托脚本, 群聊带单, 群里带节奏, 官号+云中客, 预热+中午+晚上, 老群/次新群卖货, 晒单, 已拍, 到货, 客服答疑, 整点返场, or wants group-chat selling atmosphere rather than a single sales post."
license: MIT
metadata:
  version: 2.4.1
---

# 酒托脚本

Write a group chat that naturally creates purchase atmosphere around a wine. Customer service stays customer service; ordinary members carry questions, doubt, buying, and feedback. The chat must feel like one ongoing WeChat group with a believable timeline, not six disconnected sales drafts.

## Required References

- Shared personas: `../nainai-skill-pack/references/personas.md`
- Shared tone rules: `../nainai-skill-pack/references/anti-ai-tone.md`
- Plan workflow: `references/plan-card.md`
- Dialogue naturalization: `references/dialogue-naturalization.md`
- Campaign rhythm: `references/campaign-rhythm.md`
- Quality gate: `references/quality-gate.md`
- Examples: `examples/good.md` and `examples/bad.md`

## Workflow

1. Confirm this is a shill/order chat, not a single sales post or neutral discussion.
2. Build an internal `fact_lock` for product, price, gifts, links, stock, activity time, screenshots, awards/honors, old sales history, group feedback, and forbidden notes.
3. Decide mode:
   - Single segment: generate about 30 chat lines unless user specified another length.
   - Multi-version or batch: default to one connected 3-day / 6-wave chat plan: Day 1 noon, Day 1 afternoon, Day 2 noon, Day 2 afternoon, Day 3 noon, Day 3 afternoon.
   - Campaign package: when the user asks for `官号+云中客`, `预热+中午+晚上`, old/new group versions, or an event schedule, create the requested sections with official-account copy plus group-chat follow-up.
   - If the user asks for 600 total entries, split them evenly across the six waves unless they provide a different allocation. If the user asks for 200 entries in each of six waves, treat that as 1200 total or clarify the total before writing.
4. Build an internal `wine_shill_plan` with a timeline, topic progression, official/group split, and role rotation.
5. Decide campaign stage when the user specifies it or when multi-wave output needs progression: preheat, sale, afternoon reorder, return close, arrival feedback, or collection close.
6. Convert user-provided selling points into dialogue beats: question, doubt, correction, personal reason, service fact, or life scene. Do not stack selling points into one slogan line.
7. Select 6-9 personas plus optional `客服` or `官号`; rotate them across waves so one ordinary member does not keep reappearing as the main actor.
8. Track shill states across waves: bought, watching, waiting for price, waiting for taste, waiting for delivery, reordering. Do not convert every ordinary member in the first wave.
9. Generate the requested wave(s), keeping each wave connected to earlier events through natural callbacks.
10. Add image placeholders only when useful and specific.
11. Run quality gate and rewrite once if service identity, facts, role behavior, timeline, campaign rhythm, selling-point delivery, or tone fail.

## Default 3-Day / 6-Wave Rhythm

Use this when the user asks for multiple versions, six versions, multi-day execution, batch shill scripts, or 600 entries without a more specific structure:

| Wave | Time | Main writing focus | Continuity job |
| --- | --- | --- | --- |
| 1 | Day 1 noon | Taste curiosity, first reactions, meal scenes | Start with small questions and light personal interest |
| 2 | Day 1 afternoon | Questions, doubt, price/gift clarification | Let earlier questions get answered without pressure |
| 3 | Day 2 noon | Order screenshots, delivery expectation, family use | New buyers appear; earlier buyers do not dominate |
| 4 | Day 2 afternoon | Awards/honors if provided, reputation, cautious comparison | Use honors as a side note, not authority theater |
| 5 | Day 3 noon | Arrival, dinner/gift scenarios, lived feedback | Some callbacks to earlier orders or doubts |
| 6 | Day 3 afternoon | Loose wrap-up, individual buying decisions, remaining questions | Close the group story without deadline pressure |

The six waves should read like one virtual group over time. People may "round back" later if there is a reason, such as their delivery arriving or someone asking them a direct question. Do not make the same person repeatedly buy, photograph, praise, and explain across multiple waves.

## Explicit Group Variants

Do not infer old-group/new-group/mixed-group structure on your own. Only use these variants when the user explicitly asks for them.

- Old group: reduce basic education; emphasize prior drinking, repurchase, missed restock, family feedback, and补货. Price-control, return, and link events should feel like remembered group history or a current small incident.
- New group: include more questions, product origin, why it is worth trying, competitor anchors, and risk-reducing explanations. New members can ask whether the product is worth trying, but they should not sound like they are reading specs.
- Mixed group: let old members answer new members instead of making everyone equally knowledgeable.

## Output Contract

- Pure chat body.
- Each ordinary message: `网名：内容`.
- Specific image placeholders may appear as their own line, for example `【此处放一张下单截图】`.
- Default about 30 ordinary chat lines per `云中客` segment.
- For six-wave output, separate waves with plain chat timestamps such as `第一天中午` only if the user wants the full multi-day script in one answer; otherwise output the requested wave as pure chat.
- Include question, doubt, correction, buying/arrival/action, and customer-service answer when relevant.
- When the user asks for official-account sales content with images, `官号` should usually be a three-paragraph, three-image selling narrative, not a short notice. Ordinary members must then react, ask, doubt, compare, or act; they should not repeat the announcement.
- For campaign packages, use only requested section labels such as `老群版`, `次新群版`, `前一天预热`, `中午`, `晚上`, or clock times. For a single segment, no title, explanation, outline, or internal notes.

## Boundaries

- Do not invent price, coupon, gift, stock, limit, sales volume, official backing, screenshot truth, or口感 feedback.
- User-provided selling points may be used, including official price-control notes, return-event timing, awards, specs, and product claims. The rule is not "avoid the selling point"; the rule is "make it sound like a real group member noticing or asking about it."
- Do not invent awards/honors. If awards are provided, members may mention them briefly as a remembered fact or discovery, not as a synchronized authority pitch.
- Customer service must not pretend to be an ordinary buyer.
- Ordinary shill members must not ask process questions like "还能不能拍", "客服能不能拍", "问客服还能拍吗", or any variant that makes the shill look like they are coordinating the sale.
- Replace process questions with actions: "已拍", "补了一箱", "截图发客服了", "等到货", "晚上开了说", or "周末带出去试".
- Deadline or return-event timing can appear if the user provided it, but do not write pressure lines like "最后一天抓紧", "不拍就没了", "今晚必须下手", or "错过没了". Keep it factual, casual, and non-commanding.
- Official price-control or channel-control notes such as "官方控价799" can appear if the user provided them. Do not pair them with hard-closing language or write them as an official slogan.
- Do not repeat detail-page parameters as praise, such as "52度浓香500毫升", "净含量500ml", or "标准浓香型白酒". If the user gives specs as selling points, use them sparingly inside questions, corrections, or customer-service answers instead of making ordinary members chant them.
- Do not make several people jointly emphasize "知名度", "神秘度", "权威感", "大厂背书", or similar abstract positioning. One grounded comment is enough if it is fact-supported.
- If one ordinary line contains two or more selling points, rewrite it unless the line is a natural question, doubt, correction, or customer-service factual answer.
- Ordinary buying or reordering must have a reason: prior taste, family feedback, holiday meal, gift calculation, friend/family request, missed last restock, price confirmation, or delivery/taste proof.
- Familiar-wine comparisons may be used only when the competitor/reference is provided or already in the brief. Keep them personal and slightly textured, including reasonable caveats when natural.
- Match persona to product tier and behavior. A high-status or experienced drinker should not suddenly scramble for a very cheap product without a believable reason; similar-looking names should not be placed so close that the group reads like one person talking to themselves.
- `官号` should be literary and selling-point-led when the user asks for官号内容, campaign copy, or the existing HLY official format. Use brand story, lineage, awards, craft, taste, and value as emotional sales material. Do not reduce it to "场景很清楚", "价格规则看页面", or other empty service notices.
- `云中客` carries realism: rotate people, keep some watching, let proof and callbacks move them, and avoid using the same few shill names in every section. Cloud-member lines should sound like middle-aged wine friends chatting, not official summaries. Do not over-compress into punchlines such as "反馈比空夸有用" or "品牌好比讲参数有用"; use messier lived speech with family, meals, budgets, hesitation, and small corrections.
- Final-draft calibration beats raw completeness. For plain short-notice mode, old-group repeat campaigns may use compact lines about prior sale,补货 reason, current price/event change, and old buyers' missed/restock memory. For HLY/Feishu-style官号内容, do not apply this compression rule: keep the three-paragraph selling narrative and fold group memory into brand story, awards, craft, taste, and value.
- Do not output internal notes such as "这段不发", screenshot numbers, or forbidden price remarks.
- Competitor comparisons must be user-provided or clearly framed as personal chat opinion.
