# Fact Lock

Build this internally before writing:

```yaml
product_name: ""
product_type: ""
provided_facts:
  price: ""
  coupon_price: ""
  official_price: ""
  specs: ""
  gifts: ""
  stock: ""
  deadline: ""
  taste: ""
  origin: ""
  backing: ""
  action: ""
confirmed_facts: {}
links: []
missing_facts: []
forbidden_facts: []
```

## Rules

- Empty fields stay empty.
- If the user gives a link, preserve it exactly in `links`.
- Add to `forbidden_facts` anything tempting but unsupported, such as price, stock, gifts, or official awards.
- The final copy may only use `provided_facts`, `confirmed_facts`, and `links`.
- If a claim is useful but missing, either omit it or ask the user before writing.

## Common Failures

- Turning "活动不错" into a specific discount.
- Turning "库存不多" into a number.
- Turning "适合送礼" into an official gift-box claim.
- Reusing prices or gifts from examples.
