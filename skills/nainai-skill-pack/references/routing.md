# Routing

Use final use, not surface keywords, to choose the workflow.

| 中文命令 | Route | Key signal |
| --- | --- | --- |
| `识图喝酒` | `image-drinking-chat` | Image, table scene, bottle, dishes |
| `卖货话术` | `sales-official-copy` | Product, price, link, coupon, deadline, call to action |
| `水群脚本` | `natural-group-chat` | Topic, debate, wine friends, realistic group chat |
| `酒托脚本` | `wine-shill-chat` | Bought, arrived, screenshots, gift, customer service |
| `找话题` | `wine-topic-finder` | Find topic, recent news, Xiaohongshu, Weibo, industry signal |

Conflict rules:

- If there is a product link and the output is a single sendable post, choose `sales-official-copy`.
- If there are multiple chat roles and purchase behavior, choose `wine-shill-chat`.
- If the user asks for `官号+云中客`, `预热+中午+晚上`, old/new group卖货 versions,整点返场, or a sales event with group reactions, choose `wine-shill-chat`.
- If there is an uploaded drinking image, choose `image-drinking-chat` even if the result is group chat.
- If the user only asks for "make this more real", keep the previously active task type.
- If live/recent facts matter, search or ask for source material before writing factual claims.

Default lengths:

- `image-drinking-chat`: 6-10 lines.
- `sales-official-copy`: 12-28 lines unless the user requests short.
- `natural-group-chat`: 30-40 lines.
- `wine-shill-chat`: about 30 lines per `云中客` segment; multi-version or batch requests use the connected 3-day / 6-wave structure from the wine-shill skill.
- `wine-topic-finder`: 5-10 topic cards.
