# Search Workflow

Use current search when the user asks for:

- latest, recent, today, this week
- news, policy, stock, fund, price movement
- Xiaohongshu, Weibo, Douyin, platform trend
- "help me find a topic" with no seed and freshness implied

## Tool Policy

Use whatever current tool is available in the host agent:

- Codex web search or browser tools.
- Kimi Work search/browser bridge.
- User-provided screenshots, links, or notes.

Do not hard-code one required bridge. If a preferred platform is unavailable, degrade gracefully and label the limitation.

## Source Extraction

For each usable signal:

```yaml
signal_card:
  source: ""
  title: ""
  date: ""
  url: ""
  wine_relevance: direct | bridgeable
  core_signal: ""
  usable_angle: ""
```

Filter out unrelated politics, celebrity gossip, pure ads, and signals without a natural wine discussion angle.
