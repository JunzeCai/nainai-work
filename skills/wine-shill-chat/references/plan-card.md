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
  awards_honors: []
  competitor_refs: []
  forbidden_notes: []
wine_shill_plan:
  mode: single_segment | three_day_six_wave | batch_600
  rhythm:晒单起势 | 试喝反馈 | 赠品客服 | 争议纠偏 | 三天六波
  total_entries: ""
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
  role_rotation:
    main_actor_by_wave: []
    cooldown_names: []
    callback_reason: []
  angle_ledger:
    used_phrases: []
    used_selling_points: []
    banned_repeats: ["更柔", "更深", "知名度", "神秘度", "权威感"]
  image_slots: []
  conflict: ""
  ending_action: ""
```

## Batch Allocation Rule

- Six-wave structure is the default for multi-version tasks.
- If the target is 600 total entries, allocate 100 entries to each of the six waves unless the user gives a different split.
- If the brief says "three days, noon and afternoon, 200 each", note internally that this equals 1200 entries. Do not silently call it 600.

## Wave Focus Rules

- Day 1 noon: mostly taste curiosity, meal fit, first-person hesitation. Avoid hard selling.
- Day 1 afternoon: questions and doubts. Customer service may answer provided facts, but ordinary members should not ask "can I still buy/shoot/order".
- Day 2 noon: ordering and image placeholders. Do not let the same member post every screenshot.
- Day 2 afternoon: awards/honors may appear if provided. Mention them as a small supporting fact, not a repeated authority chant.
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
