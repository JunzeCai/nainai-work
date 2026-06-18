# Wine Shill Plan Card

Build this internally:

```yaml
  fact_lock:
  product_name: ""
  price: ""
  coupon_price: ""
  specs: ""
  gifts: ""
  links: []
  stock: ""
  deadline: ""
  event_context: ""
  group_history: ""
  prior_feedback: []
  selling_points: []
  price_control_notes: []
  awards_honors: []
  competitor_refs: []
  forbidden_notes: []
wine_shill_plan:
  mode: single_segment | campaign_package | three_day_six_wave | batch_600
  rhythm:晒单起势 | 试喝反馈 | 赠品客服 | 争议纠偏 | 三天六波
  total_entries: ""
  stage_mode: none | preheat | sale | afternoon_reorder | return_close | arrival_feedback | collection_close
  explicit_group_variant: none | old_group | new_group | mixed_group
  delivery_package:
    needs_official_account: false
    needs_yunzhongke: false
    sections: []
    group_versions: []
    official_voice: official_notice | old_group_owner | literary_collection
    yunzhongke_density: normal | longer
  wave_allocation:
    day1_noon: ""
    day1_afternoon: ""
    day2_noon: ""
    day2_afternoon: ""
    day3_noon: ""
    day3_afternoon: ""
  opening_hook: ""
  timeline:
    day1_noon: "口感/饭局/轻兴趣"
    day1_afternoon: "提问/疑虑/客服事实"
    day2_noon: "下单/截图/等待到货"
    day2_afternoon: "奖项荣誉/谨慎对比/纠偏"
    day3_noon: "到货/家宴/送礼场景"
    day3_afternoon: "自然收束/个体决定/余问"
  roles:
    questioner: ""
    buyer: ""
    expert: ""
    skeptic: ""
    life_scene: ""
    customer_service: ""
  persona_fit:
    product_tier: ""
    role_purchase_fit: []
    names_to_separate: []
  role_rotation:
    main_actor_by_wave: []
    cooldown_names: []
    callback_reason: []
    fresh_questioners_reserved: []
  shill_states:
    bought: []
    watching: []
    waiting_for_price: []
    waiting_for_taste: []
    waiting_for_delivery: []
    reordering: []
    reserved_for_later: []
  official_group_split:
    official_account_facts: []
    official_scene_guidance: []
    official_account_structure: "three paragraphs + three image placeholders when user asks for HLY/Feishu-style official account content"
    official_account_angles: ["brand/product recognition", "story/craft/award/lineage trust", "value/taste/dignity with light activity tail"]
    group_reactions: []
    avoid_repeated_official_lines: []
  angle_ledger:
    used_phrases: []
    used_selling_points: []
    final_draft_anchor: ""
    selling_point_delivery:
      question: []
      doubt: []
      correction: []
      service_fact: []
      life_scene: []
    banned_repeats: ["更柔", "更深", "知名度", "神秘度", "权威感"]
  image_slots: []
  conflict: ""
  ending_action: ""
```

## Batch Allocation Rule

- Six-wave structure is the default for multi-version tasks.
- If the target is 600 total entries, allocate 100 entries to each of the six waves unless the user gives a different split.
- If the brief says "three days, noon and afternoon, 200 each", note internally that this equals 1200 entries. Do not silently call it 600.

## Explicit Group Variant Rule

- Do not infer old/new/mixed group. Set `explicit_group_variant` only when the user says 老群, 新群, 混合群, or gives equivalent direct wording.
- Old group: prior drinking, repurchase, missed restock,补货, family feedback, previous link/price memory.
- New group: product origin, why try it, competitor anchor, risk-reducing answers, "进群晚没见过" style questions.
- Mixed group: old members answer new members; keep knowledge uneven.

## Persona Fit Rule

- Match role behavior to product tier. Experienced or high-status roles can buy lower-priced wine only with a reason such as daily ration, gifting, family stock, or curiosity after group proof.
- Separate similar-looking names or roles in dense sections. If two names are easy to confuse, do not place them back-to-back as buyer/expert/closer.
- Do not make one role be expert, buyer, reorder buyer, screenshot poster, and closer unless the callback reason is clear.

## Campaign Stage Rule

- Use `stage_mode` when the user specifies preheat, sale, return, afternoon, next day, arrival, or when multi-wave progression needs it.
- Preheat: product identity, brand/story, previous price movement, price curiosity, wait-for-price roles.
- Sale: link, price, order screenshots,客服登记, first conversions.
- Afternoon reorder: missed buyers, second orders, friends/family stock, gift questions.
- Return close: previous sell-out, current favorable price, a few remaining hesitations, no hard pressure.
- Arrival feedback: delivery, packaging, taste, meal/family proof.
- Collection close: summarize the day's product map by use case, not by repeating every SKU detail; guide missed readers to choose by father, holiday meal, self-drinking, gifting, or daily ration.

## Campaign Package Rule

Use `campaign_package` when the user asks for 官号+云中客, old/new group versions, preheat plus sale times, or a full event day.

- In plain short-notice mode, `官号` may set product identity, timing, confirmed activity facts, and the next action. In HLY/Feishu-style官号内容, `官号` should instead build brand势能, product story, award/craft trust, taste imagination, and value desire; activity facts are only a light tail.
- For HLY/Feishu-style官号内容, `官号` uses three paragraphs plus three image placeholders. It should sell through brand story, awards, craft, lineage, taste, and value; the third paragraph is still selling copy and may only lightly carry price/rules/countdown at the tail.
- `云中客` makes the official facts believable through questions, remembered sales history, order screenshots, family scenes, comparisons, and客服登记.
- Old group and new/next-new group versions must differ in knowledge level, not only wording. Old group starts from "喝过/补货/上次没赶上"; new or next-new group starts from "啥来头/值不值/跟谁比/适合什么场景".
- For `预热+中午+晚上`, give each time a different social job: preheat builds recognition, noon starts orders and answers doubts, night uses missed buyers, family/gift calculation, or calm closeout.
- For event collections such as 618 all-day返场, `官号` should group wines by use case or香型 when helpful. Do not list every link unless the user asks; `云中客` should show people choosing different products for different reasons.

## Final Draft Calibration Rule

Use this after building the first plan, especially for products with prior group history.

- If the product has sold before, put the old-group official hook in this order: when it last sold, why it is back, what is different this time, and who should pay attention. Keep it to a few short mobile-friendly lines.
- If the product is in final-hours or closeout mode, use calm group evidence: holiday/use-case buying, many people in the group have tried it, repurchase, and missed补货. Avoid shouting scarcity.
- If an official paragraph becomes a dry encyclopedia list of grain, origin, brewing, awards, or brand history, mark it as education overflow. But literary sales copy may keep brand story, awards, craft, lineage, and taste in `官号` when those facts are turned into desire, status, memory, or value.
- For repeat campaigns, reserve several fresh questioners for later waves. Do not spend the same familiar shills on every question, screenshot, and reorder.
- Keep any user/internal production notes such as "留几个新托问问题" as planning state only. Never output them.

## Shill State Rule

- In multi-wave scripts, keep some roles in `watching`, `waiting_for_price`, `waiting_for_taste`, or `waiting_for_delivery` instead of making everyone buy immediately.
- Move reserved roles into `bought` or `reordering` in later waves only when there is a reason: price confirmed, taste proof, delivery proof, gift calculation, family stock, or missed previous restock.
- Do not output internal labels such as "找个新托", "留这里发", or "reserved_for_later".

## Wave Focus Rules

- Day 1 noon: mostly taste curiosity, meal fit, first-person hesitation. Avoid hard selling.
- Day 1 afternoon: questions and doubts. Customer service may answer provided facts, and ordinary members may naturally mention provided selling points. They should not ask "can I still buy/shoot/order".
- Day 2 noon: ordering and image placeholders. Do not let the same member post every screenshot.
- Day 2 afternoon: awards/honors, official price-control notes, or other provided selling points may appear. Mention them as small supporting facts, not repeated authority chants or hard-closing slogans.
- Day 3 noon: arrivals, family dinner, gift, budget, small corrections.
- Day 3 afternoon: natural wrap-up. Use personal decisions and callbacks, not deadline pressure.

## Image Placeholder Options

- `【此处放一张下单截图】`
- `【此处放一张到货图片】`
- `【此处放一张酒的图片】`
- `【此处放一张酒具图片】`
- `【此处放一张聚餐试喝图片】`
- `【此处放一张扫码红包截图】`

Use 3-7 placeholders only when the segment needs them. Put a lead-in before and a reaction after each placeholder.

For six-wave scripts, distribute image placeholders across people and days. One person should not repeatedly provide all order, arrival, and tasting photos unless the story gives a clear reason.
