# Dialogue Naturalization

Use this when a user provides many selling points, asks for multiple versions, or complains that a script sounds stiff.

## Selling Point Conversion

User-provided facts can appear in chat, but each fact should enter through a believable social move:

| Selling point type | Natural entry |
| --- | --- |
| Price/control | doubt, price math, "看页面", "到手价别绕" |
| Deadline/return event | calm timing context, not a command |
| Awards/honors | small supporting fact, not group chanting |
| Product story | someone asks "啥来头", another person explains briefly |
| Competitor | personal comparison, familiar reference, and correction by price tier |
| Specs | direct factual answer or correction, not praise |
| Taste | meal, family, aftertaste, throat feel, or next-day memory |

## Anti-Slogan Rule

One ordinary message should not stack multiple selling points, for example:

```text
北陌：官方控价799，今天返场最后一天，封藏大典权威感强
```

Split it into friction:

```text
北陌：页面写控价799，我主要看群里到手价
无情：控价是一回事，别把它说成神酒
糯团子：封藏大典可以当个由头，最后还得入口说话
```

## Replace Process Questions

Do not write ordinary shill roles asking whether the sale can still happen. Replace with action or lived context:

- Bad: `客服现在还能不能拍`
- Better: `我先拍一箱，截图发客服了`
- Better: `我不等晚上了，先锁一单`
- Better: `等到货我开了说`
- Better: `周末带出去试试`

## Taste Must Have Context

Avoid repeating only abstract adjectives such as "更柔", "更深", "更顺". Anchor taste in a scene:

- `老丈人说不冲`
- `配烧菜不抢味`
- `喝完嘴里不乱`
- `家宴能开，不会太冒头`
- `长辈喝着不皱眉`

## Expert Taste Detail

When a role is clearly a knowledgeable wine friend, let taste comments use more concrete tasting dimensions instead of only "顺口" or "好喝". Use these details sparingly, usually one or two per expert turn:

- 酒花: `这是六根还是五根`, `酒花能撑几秒`, `酒花散得快不快`
- 闻香: `闻香先看窖香`, `粮香在不在`, `花果香有没有`, `哪个香味占得最高`
- 入口: `入口有没有喷香感`, `第一口是不是冲`, `入口是炸开还是铺开`
- 中段: `中段有没有爆发力`, `酒体厚不厚`, `有没有塌下去`
- 咽后: `咽下去以后余味能留几秒`, `口腔里还有没有香`, `有没有回甜`
- 陈味: `有没有陈味`, `陈味是舒服的还是闷的`
- 尾味: `尾段有没有涩感`, `有没有苦感`, `收口干不干净`
- 对比: `比同价位浓香优势在哪`, `跟同价位比是香气强还是酒体厚`

Keep expert taste natural. Do not make one person deliver a full tasting note in one message. Spread details across questions, corrections, and lived reactions:

```text
糯团子：别光说顺，闻香先看窖香在不在
北陌：我那瓶窖香更明显，花果香有一点，但不是主调
无情：入口有点喷香感，中段没塌，这个价位算可以
```

Avoid fake precision unless the user provides it. Do not invent exact "几秒" numbers for酒花 or余味; phrase as a personal observation unless confirmed:

```text
谢二：酒花撑得住，不是两下就散
糯团子：咽下去嘴里还能留一会儿香，尾段没明显涩苦
```

## Explicit Old/New Group Handling

Only apply this when the user explicitly asks for old group, new group, or mixed group.

- Old group: fewer origin explanations; more prior drinking, repurchase, missed restock, and补货.
- New group: more "啥来头", "值不值", "跟谁比", and risk-reducing answers.
- Mixed group: old members answer new members; do not make everyone equally懂酒.

When new or next-new group is specified, give more room to "值不值", "喝过没", "跟熟悉酒比怎么样", and "我进群晚没见过" before conversion. When old group is specified, lean on "上次买少了", "喝完让再补", "上次链接没了", and "家里人喝着可以" as purchase reasons.

## Buying Reason Rule

Every order, reorder, or conversion should have a visible reason. Use one of these before or near the action:

- prior taste: `上次喝着确实顺`
- family feedback: `我爸喝完让我再补`
- holiday meal: `端午家里吃饭开一瓶`
- gift or service rule: `赠品一起算的话我再补一箱`
- missed restock: `上次想补，点进去没了`
- price confirmation: `还是群里这个价就行`
- delivery/taste proof: `你这张到货图看着可以`

## Anti-Repetition Across Waves

When writing multiple segments for the same product or campaign, repeated selling points are allowed, but repeated chat mechanics are not. Each segment needs a distinct social event, opening hook, and role mix.

Do not start every segment with the same pattern such as:

```text
王晨：中午我又补了一箱
胡金记：你昨天不是拍了吗
```

Rotate openings across different conversation triggers:

- meal scene: `端午家宴酒我先备了`
- family feedback: `我爸上次喝完说这个不冲`
- missed restock: `上次喝完想补，链接没赶上`
- friend request: `朋友昨天问我这酒哪买的`
- taste proof: `昨晚开了一瓶，尾味确实干净`
- expert challenge: `别只说顺，闻香先看窖香在不在`
- comparison: `同价位浓香里，我更看它中段不塌`
- stock-up reason: `家里端午要来人，我按饭局算了一下`
- screenshot or image reaction: `这张开瓶图看着就不是摆拍`
- customer-service handoff: `截图我发客服了，等到货再开`

Rotate persona functions. The same person should not repeatedly be the buyer, photo poster, expert, skeptic, and closer across consecutive waves. Let different roles carry different jobs:

- buyer/rebuyer
- family-scene narrator
- expert taster
- skeptic or value-questioner
- comparator against familiar wines
- screenshot/photo poster
- customer-service registrar

Make multi-wave scripts feel like one living group over time. Earlier buyers can later mention delivery, family use, friend's request, or preparing for a meal; they should not simply "buy again" without a new reason. New buyers should enter through a different motivation than the prior wave.

Before finalizing a multi-segment output, check:

- no two adjacent segments start with the same character + same buying line
- no one persona dominates every wave
- repeated product facts enter through different topics
- each segment has a fresh reason to talk: holiday, family, taste proof, comparison, photo, missed restock, gift, delivery, or closeout

## Familiar Comparison Rule

Use a familiar provided reference such as K6 only as personal chat opinion. Good comparisons are concrete and imperfect:

- `K6名气大，封藏入口更顺一点`
- `香气舒服些，就是陈味差点`
- `不追求面子的话，这个饭桌上够用`

Avoid synchronized praise such as everyone saying "比K6好", "更柔", or "更有权威感".

## Official Account Handoff

When `官号` publishes a three-paragraph, three-image官号/卖货 narrative, ordinary members should not echo the prose or repeat its selling points. They should turn the official romance into lived chat moves:

- a price question: `这个上次也是这个价么`
- a value doubt: `外面价格怎么样`
- a proof request: `喝过的人出来说一句`
- a lived reason: `家里快喝完了`
- an order action: `先拍一箱，截图发客服`

Also vary the trigger so every section does not become the same question-answer-sales pattern. Useful cloud-member openings include:

- family budget: `我老婆最近管我买酒管得紧，我得看看到手`
- father or father-in-law taste: `我爸就认浓香，酱香摆他面前他不动`
- weekend meal: `周末小舅子来家里吃饭，我正愁开啥`
- gift hesitation: `送人我主要怕盒子寒酸，酒倒是其次再问问`
- delivery or photo talk: `你们谁到了发个实拍，别光看详情图`
- taste concern: `别讲那么多，我就问入口辣不辣喉`

Do not make `官号` sound like客服. For HLY official account content, avoid empty administrative lines such as `这款适合的场景很清楚`, `价格规则看当前页面`, `拍完截图登记`, or `按页面为准` as the main message. The official paragraph should sell brand, story, awards, craft, taste, and value with literary language; activity details appear only as a light tail when provided.

## 云中客 Middle-Aged Voice

`云中客` is not a second official account. It should sound like middle-aged wine friends in a WeChat group: practical, a little loose, sometimes wordy, sometimes doubtful, and tied to home meals, fathers, fathers-in-law, work dinners, wife budgets, express delivery, and what people actually open on a table.

Do not over-tighten every line into a neat slogan or verdict. Avoid compressed "wise summary" lines such as:

```text
夕阳美：反馈比空夸有用
糯团子：品牌好比讲参数有用
无情：定位放准就舒服
```

Replace them with more ordinary speech:

```text
夕阳美：你们别光说盒子，等谁开了说两句，我主要听入口冲不冲
糯团子：长辈有时候不看你讲那么多参数，他就认这个牌子熟不熟、喝着别顶
无情：别把它吹成多高端，家里吃饭能开、送人不难看，这就差不多了
```

Let some lines be a little longer or less polished when the role fits:

- `我爸这人挑，酱香他不喝，浓香只要不辣喉他还能接受`
- `我先拍两瓶，周末小舅子来吃饭，开了不好喝我回来骂你们`
- `包装我看着可以，酒我没喝过，等你们老群喝过的先说`
- `别整那些大词，我就问一句，入口冲不冲，第二天嘴里难不难受`

Use short reactions too, but do not make every person speak in clipped seven-word lines. A believable section should mix short reactions, half-sentences, domestic details, mild disagreement, and one or two slightly rambling middle-aged lines.

Do not make every line carry sales progress. About 30 lines should feel like a group drifting around the topic, not a sales checklist. Allow a few lines that only add realism:

```text
快乐张：周末我家又要来人，厨房都懒得收拾了
陈学芳：你还好，我这边每次来客都先问喝啥酒
无情：别扯远了，先看这酒入口冲不冲
国国：我老婆刚还说家里酒别再堆了，我说这回先少拍
```

Good `云中客` rhythm is: a lived trigger, two or three natural replies, a doubt or correction, one action, then a small side comment or callback. Avoid a straight ladder of `问价 -> 解释 -> 下单 -> 客服 -> 夸酒 -> 再下单`.

## Collection And Holiday Voice

For holiday or full-day collection sections, make `官号` sound like a familiar group owner helping people choose, not a catalog:

- group by场景: 父亲节, 端午家宴, 日常口粮, 送礼, 自饮, 尝特色
- use warm but concrete selection lines such as `按家里缺什么选` or `白天漏看的不用往上翻`; registration lines such as `拍完截图我登记` belong to客服 or final收口群聊, not the main HLY官号内容 paragraph
- avoid per-product mini sales pages unless the user asks for every link

Then make `云中客` show actual selection behavior:

- one person fills a missed wave
- one person buys for父亲节 or长辈
- one person补口粮
- one person asks a taste or香型 question
- one person reminds others to开瓶反馈, not just晒盒子

## Mobile Final-Draft Compression

When converting a draft into final HLY copy, check how it reads on a phone.

- Prefer one short idea per line for `官号`; if a line feels like it cannot be read in one breath, split or cut it.
- Keep old-group official copy close to group memory, but still literary when the user asks for官号内容: prior sale,补货, repurchase, and family/holiday use should sit inside brand story and value, not replace it with a dry notice.
- Treat detailed product education as optional raw material. In final copy, use only the detail that creates a question, doubt, correction, or purchase reason.
- A phrase like "不是文案热闹，是群里喝过的人多、愿意回头补" is the right kind of old-group proof: it sounds earned by the group, not pasted from a product page.
- If the user has already approved a short final-draft style for a similar product, match its compression before adding new facts.
