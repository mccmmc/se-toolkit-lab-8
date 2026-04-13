# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Query:** "What is the agentic loop?"

**Response:** The agent explained the agentic loop as the core cycle that allows an AI agent to autonomously accomplish tasks:
1. **Perceive (Input)** — receives goal/instruction from user
2. **Think (Reasoning)** — LLM analyzes input and decides next action
3. **Act (Execution)** — performs the chosen action or calls a tool
4. **Observe (Feedback)** — receives result of the action
5. **Reflect & Iterate** — evaluates result, loops back if needed

**Query:** "What labs are available in our LMS?"

**Response:** The agent listed 8 labs from the live LMS backend (MCP was auto-connected via `uv run` inheriting the parent workspace):
- Lab 01 – Products, Architecture & Roles
- Lab 02 — Run, Fix, and Deploy a Backend Service
- Lab 03 — Backend API: Explore, Debug, Implement, Deploy
- Lab 04 — Testing, Front-end, and AI Agents
- Lab 05 — Data Pipeline and Analytics Dashboard
- Lab 06 — Build Your Own Agent
- Lab 07 — Build a Client with an AI Coding Agent
- Lab 08 — lab-08

## Task 1B — Agent with LMS tools

**Query:** "What labs are available?" — Agent returned real lab names from the backend via MCP tools.

**Query:** "Is the LMS backend healthy?" — Agent called `lms_health` and reported a healthy status with real item count from the backend.

## Task 1C — Skill prompt

**Query:** "Show me the scores" (without specifying a lab)

**Response:** The agent called `lms_labs` first, then fetched pass rates for each lab, and presented a summary table:

| Lab     | Avg Score (Core Tasks) | Completion Rate |
|---------|------------------------|-----------------|
| Lab 01  | ~63.4                  | 100.0%          |
| Lab 02  | ~63.6                  | 89.1%           |
| Lab 03  | ~56.0                  | 89.1%           |
| Lab 04  | ~63.2                  | 96.7%           |
| Lab 05  | ~70.7                  | 98.4%           |
| Lab 06  | ~59.3                  | 98.4%           |
| Lab 07  | ~67.2                  | 99.6%           |
| Lab 08  | N/A                    | 0.0%            |

Key takeaways: Highest scoring — Lab 05 (~70.7), Lowest scoring — Lab 03 (~56.0), Toughest completion — Lab 02 & Lab 03 (both 89.1%).

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
