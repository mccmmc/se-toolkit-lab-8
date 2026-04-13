# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Query:** "What is the agentic loop?"

**Response:**
```
The agentic loop is the core cycle that an AI agent follows to
accomplish tasks autonomously. Here's how it works:

 1 Perceive — The agent receives input (a user request, sensor
   data, or the result of a previous action) and understands the
   current state.
 2 Reason/Plan — The agent thinks about what to do next. It
   decides which tools to use, what steps to take, and in what
   order. This is where the LLM generates a plan or selects
   actions.
 3 Act — The agent executes its chosen actions — calling tools,
   running commands, reading/writing files, making API calls,
   etc.
 4 Observe — The agent receives feedback from the environment
   (tool outputs, command results, error messages).
 5 Reflect/Adapt — The agent evaluates whether it's making
   progress toward the goal. If not, it revises its plan and
   tries a different approach.

This loop repeats until the task is complete or a stopping
condition is met (max iterations, user intervention, etc.).

The key difference from a simple chatbot is that an agent can
take actions in the world (not just generate text) and iterate
based on feedback, rather than giving a single response and
stopping.
```

**Query:** "What labs are available in our LMS?"

**Response:**
```
Here are the available labs in the LMS:

 ID      Title
 ───────────────────────────────────────────────────────────────
 lab-01  Lab 01 – Products, Architecture & Roles
 lab-02  Lab 02 — Run, Fix, and Deploy a Backend Service
 lab-03  Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 lab-04  Lab 04 — Testing, Front-end, and AI Agents
 lab-05  Lab 05 — Data Pipeline and Analytics Dashboard
 lab-06  Lab 06 — Build Your Own Agent
 lab-07  Lab 07 — Build a Client with an AI Coding Agent
 lab-08  lab-08

There are 8 labs in total. Let me know if you'd like to see
metrics for any specific lab — I can check pass rates, completion
rates, top learners, group performance, or submission timelines.
```

## Task 1B — Agent with LMS tools

**Query:** "What labs are available?"

**Response:**
```
Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 – Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 Lab 08 – lab-08

Let me know if you'd like to check pass rates, completion stats,
top learners, group performance, or submission timelines for any
specific lab!
```

**Query:** "Is the LMS backend healthy?"

**Response:**
```
Yes, the LMS backend is healthy! It's running normally with 56
items in the system.
```

## Task 1C — Skill prompt

**Query:** "Show me the scores" (without specifying a lab)

**Response:**
```
I'll check what labs are available first.

Here are the available labs. Which one would you like to see
scores for?

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 Lab 08 — lab-08

Just let me know the lab number or name!
```

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
