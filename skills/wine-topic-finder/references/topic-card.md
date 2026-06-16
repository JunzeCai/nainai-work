# Topic Card Schema

```yaml
topic_card:
  title: ""
  entity_anchor: ""
  why_now: ""
  opening_line: ""
  conflict_points: []
  suggested_roles: []
  script_path: ""
  source_notes: []
```

## Requirements

- `entity_anchor` must be concrete: wine name, price band, channel, holiday, policy, company, social scene, dish, gift situation, or platform post pattern.
- `opening_line` must be something a group member could actually say.
- `conflict_points` should support disagreement, correction, and role friction.
- `script_path` should tell `natural-group-chat` what rhythm to use: debate, correction, life scene, price math, taste argument, gift decision, or news reaction.

## Bad Topic Shapes

- "白酒怎么选" with no entity anchor.
- "最近年轻人爱喝酒" with no source, scene, or conflict.
- "茅台新闻" with no angle or opening line.
