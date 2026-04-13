---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to LMS (Learning Management System) tools that provide live data about courses, labs, learners, and performance metrics.

## Available tools

- **lms_health** — Check if the LMS backend is healthy. Returns item count. Use when the user asks about system status or health.
- **lms_labs** — List all available labs. Use when the user asks about labs without specifying which one, or when you need lab identifiers for other tools.
- **lms_learners** — List all registered learners.
- **lms_pass_rates** — Get pass rates (average score and attempt count per task) for a specific lab. Requires a `lab` parameter.
- **lms_timeline** — Get submission timeline (date + submission count) for a specific lab. Requires a `lab` parameter.
- **lms_groups** — Get group performance (average score + student count per group) for a specific lab. Requires a `lab` parameter.
- **lms_top_learners** — Get top learners by average score for a specific lab. Requires a `lab` parameter. Has an optional `limit` (default 5).
- **lms_completion_rate** — Get completion rate (passed / total) for a specific lab. Requires a `lab` parameter.
- **lms_sync_pipeline** — Trigger the LMS sync pipeline. Use when data seems stale or the user reports missing data.

## Strategy

- If the user asks for scores, pass rates, completion, groups, timeline, or top learners **without naming a lab**, call `lms_labs` first to get available labs.
- If multiple labs are available, ask the user to choose one. Use the `structured-ui` skill to present the choice on supported channels. When presenting lab choices, use each lab's title as the display label and the lab ID (e.g., `lab-01`) as the value to pass back.
- If the user specifies a lab name that doesn't match exactly, use `lms_labs` to find the closest match.
- When the user asks "what can you do?", explain that you can query live LMS data: list labs, check pass rates, view top learners, see group performance, check completion rates, and view submission timelines. Mention that most metrics require selecting a specific lab first.
- Format numeric results clearly: use percentages for rates (e.g., "75%"), counts for learners and groups, and keep tables concise.
- Keep responses concise. Don't repeat the same data in multiple formats.
- If the LMS backend appears unhealthy (lms_health fails), inform the user and suggest triggering `lms_sync_pipeline`.

## Response formatting

- Present scores and rates as percentages with one decimal place (e.g., "75.3%").
- When listing top learners, show rank, name, and score.
- When showing group performance, include group name, average score, and student count.
- For timeline data, summarize trends rather than listing every date.
