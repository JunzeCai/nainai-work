# Quality Gate

Check before final output:

- Every topic is wine-related or bridgeable to wine.
- Every topic has a concrete `entity_anchor`.
- Every topic has a chat-ready `opening_line`.
- Every topic has at least two `conflict_points`.
- Search-backed topics include source notes.
- If search was unavailable, output says so and avoids freshness claims.
- Batch angles are not repetitive; no more than two cards should share the same conflict pattern.
- The topic can feed directly into `natural-group-chat`.

Rewrite weak cards before final output.
