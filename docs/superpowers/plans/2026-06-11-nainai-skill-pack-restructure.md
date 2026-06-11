# Nainai Skill Pack Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure the five wine/private-domain writing skills into a portable Skill Pack with a Codex plugin wrapper and a repo-scoped auto entrypoint.

**Architecture:** Keep the portable core in `skills/`, add `skills/nainai-skill-pack` as the plugin router, and make each task skill thin with references, examples, and evals. Add `.codex-plugin/plugin.json` so the repository can be installed as a Codex plugin, and add `.agents/skills/nainai-work-router` as the current-repo auto-loader.

**Tech Stack:** Markdown Agent Skills, JSON plugin manifest, JSON eval fixtures.

---

### Task 1: Package Shape

**Files:**
- Create: `.codex-plugin/plugin.json`
- Create: `.agents/skills/nainai-work-router/SKILL.md`
- Create: `skills/nainai-skill-pack/SKILL.md`
- Create: `skills/nainai-skill-pack/references/*.md`

- [ ] Add the Codex plugin manifest with `skills` pointing at `./skills/`.
- [ ] Add the repo-scoped auto-loader under `.agents/skills/nainai-work-router`.
- [ ] Add shared routing, personas, anti-AI-tone, workflow contracts, and feedback tags.

### Task 2: High-Risk Skill Rewrites

**Files:**
- Modify: `skills/image-drinking-chat/SKILL.md`
- Create: `skills/image-drinking-chat/references/*.md`
- Modify: `skills/sales-official-copy/SKILL.md`
- Create: `skills/sales-official-copy/references/*.md`

- [ ] Rework image drinking chat around `scene_card -> confidence A/B/C -> final chat`.
- [ ] Rework sales copy around `fact_lock -> template -> voice -> audit`.
- [ ] Add good/bad examples and eval fixtures for both.

### Task 3: Remaining Skill Rewrites

**Files:**
- Modify: `skills/natural-group-chat/SKILL.md`
- Modify: `skills/wine-shill-chat/SKILL.md`
- Modify: `skills/wine-topic-finder/SKILL.md`
- Create: references, examples, evals for each.

- [ ] Move long procedural details into references.
- [ ] Add novelty and quality gates.
- [ ] Add eval fixtures that cover common failure modes.

### Task 4: Verification

**Files:**
- All files above.

- [ ] Parse all JSON files.
- [ ] Validate plugin manifest with plugin creator validation.
- [ ] Check Skill frontmatter exists for each `SKILL.md`.
- [ ] Report how to use the pack in Codex and other agents.
