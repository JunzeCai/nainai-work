# Workflow Contracts

Use these intermediate structures internally. Do not show them unless the user asks for process, audit, or debugging.

## image_scene_card

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

Confidence rules:

- A: Complete brand/series or unmistakable bottle with readable evidence.
- B: Partial label, bottle shape, color, or user hint suggests a candidate but not enough to assert.
- C: No reliable bottle identification.

## fact_lock

```yaml
product_name: ""
provided_facts: {}
confirmed_facts: {}
links: []
missing_facts: []
forbidden_facts: []
```

Only `provided_facts`, `confirmed_facts`, and original `links` may appear in sales or shill copy.

## difference_contract

```yaml
opening: ""
scene: ""
stance: ""
tempo: ""
roles: []
ending: ""
must_differ_from: []
```

Use when producing variants or when the previous output feels repetitive.

## quality_audit

```yaml
fact_risk: pass | fail
voice_risk: pass | fail
format_risk: pass | fail
novelty_risk: pass | fail
fixes: []
```
