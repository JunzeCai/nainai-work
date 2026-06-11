---
name: image-drinking-chat
description: "识图喝酒. Generate a short realistic white-liquor group chat from drinking-table images or image descriptions. Use when the user says 识图喝酒, 看图写群聊, uploads/describes a drinking photo, or wants image-based wine-friend chat. Must use scene-card confidence before naming a wine."
license: MIT
metadata:
  version: 2.0.0
---

# 识图喝酒

Turn a drinking-table image into a short, realistic wine-friend group chat. The main risk is hard-guessing a bottle from weak visual evidence, so always separate image understanding from chat generation.

## Required References

- Shared personas: `../nainai-skill-pack/references/personas.md`
- Shared tone rules: `../nainai-skill-pack/references/anti-ai-tone.md`
- Scene-card workflow: `references/scene-card.md`
- Quality gate: `references/quality-gate.md`
- Examples: `examples/good.md` and `examples/bad.md`

## Workflow

1. Inspect all images or the user's image description.
2. Build an internal `image_scene_card`.
3. Assign confidence:
   - A: safe to name the specific wine.
   - B: only say "像/是不是/看着有点像"; do not assert.
   - C: do not mention a specific brand or series.
4. If A and current price or recent market facts are needed, search or ask for confirmed source material before writing.
5. Select 4-6 personas.
6. Generate 6-10 lines in `网名：内容` format.
7. Run `references/quality-gate.md`; rewrite once if any hard gate fails.

## Output Contract

- Output final chat only unless the user asks for analysis.
- One line per message, format `网名：内容`.
- Default length: 6-10 lines.
- At least 4 roles.
- No title, explanation, role table, image placeholder, or internal card.
- Short, uneven, casual lines.

## Fact Boundaries

- Do not assert brand, series, degree, price, vintage, batch, or口感 from unclear visual evidence.
- Do not invent current prices, discounts, shop channels, gifts, or authenticity claims.
- If confidence is B or C, make the uncertainty part of the group chat naturally.
