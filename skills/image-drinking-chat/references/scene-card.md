# Scene Card Workflow

Build this internally before writing.

```yaml
bottle_visibility: clear | partial | none
visible_text: []
wine_candidates:
  - name: ""
    evidence: ""
confidence_level: A | B | C
scene: ""
dishes: []
safe_talk_points: []
forbidden_claims: []
```

## Confidence A

Use only when the image clearly shows enough evidence to name the wine:

- Readable brand and series text, or
- Distinctive bottle plus visible label evidence, or
- User explicitly confirms the wine name.

Allowed in chat:

- Specific wine name.
- General price-band talk if sourced or user-provided.
- Simple口感 only if user provided, searched, or framed as personal impression.

## Confidence B

Use when the image suggests a candidate but evidence is incomplete.

Allowed in chat:

- "像是...", "是不是...", "看不太清".
- Scene, dishes, dinner mood, whether the bottle looks formal or casual.

Forbidden:

- Writing the candidate as fact.
- Searching the guessed candidate and then treating search results as image truth.
- Specific price or口感 tied to the guessed wine.

## Confidence C

Use when no reliable bottle identity exists.

Allowed in chat:

- Dishes, cups, table scene, drinking mood, family/dinner context.
- "光看菜就知道这局不小", "酒没拍清".

Forbidden:

- Any brand, series, degree, price, authenticity, or market discussion.

## Generation Notes

The uncertainty should sound like real chat, not an audit note:

- Good: `无情：瓶标糊成这样你也敢认？`
- Good: `糯团子：菜倒是硬，酒先别瞎猜。`
- Bad: `经分析，该图片置信度为B。`
