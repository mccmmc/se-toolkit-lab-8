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
Nanobot deployed as a Docker Compose service via `nanobot gateway`. Startup log:

```
nanobot-1  | Using config: /app/nanobot/config.resolved.json
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
root@Toolkit004:~/se-toolkit-lab-8# docker compose --env-file .env.docker.secret logs nanobot --tail 50
nanobot-1  | Using config: /app/nanobot/config.resolved.json
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
nanobot-1  | 2026-04-14 15:02:55.322 | DEBUG    | nanobot.channels.registry:discover_all:64 - Skipping built-in channel 'matrix': Matrix dependencies not installed. Run: pip install nanobot-ai[matrix]
nanobot-1  | 2026-04-14 15:02:55.681 | INFO     | nanobot.channels.manager:_init_channels:58 - WebChat channel enabled
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | ✓ Heartbeat: every 1800s
nanobot-1  | 2026-04-14 15:02:55.683 | INFO     | nanobot.cron.service:_load_store:85 - Cron: jobs.json modified externally, reloading
nanobot-1  | 2026-04-14 15:02:55.684 | INFO     | nanobot.cron.service:start:202 - Cron service started with 0 jobs
nanobot-1  | 2026-04-14 15:02:55.684 | INFO     | nanobot.heartbeat.service:start:124 - Heartbeat started (every 1800s)
nanobot-1  | 2026-04-14 15:02:56.081 | INFO     | nanobot.channels.manager:start_all:91 - Starting webchat channel...
nanobot-1  | 2026-04-14 15:02:56.082 | INFO     | nanobot.channels.manager:_dispatch_outbound:119 - Outbound dispatcher started
nanobot-1  | 2026-04-14 15:02:56,084 INFO [nanobot_webchat.channel] [channel.py:178] [trace_id=0 span_id=0 resource.service.name=nanobot trace_sampled=False] - WebChat relay listening on 127.0.0.1:8766
nanobot-1  | 2026-04-14 15:02:56,084 INFO [nanobot_webchat.channel] [channel.py:91] [trace_id=0 span_id=0 resource.service.name=nanobot trace_sampled=False] - WebChat starting on 0.0.0.0:8765
nanobot-1  | 2026-04-14 15:02:56,087 INFO [websockets.server] [server.py:341] [trace_id=0 span_id=0 resource.service.name=nanobot trace_sampled=False] - server listening on 0.0.0.0:8765
nanobot-1  | 2026-04-14 15:02:59,084 INFO [mcp.server.lowlevel.server] [server.py:720] [trace_id=0 span_id=0 resource.service.name=mcp-lms trace_sampled=False] - Processing request of type ListToolsRequest
nanobot-1  | 2026-04-14 15:02:59.089 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.089 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.089 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.090 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.090 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.090 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.090 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.090 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.090 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
nanobot-1  | 2026-04-14 15:02:59.090 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
nanobot-1  | 2026-04-14 15:03:00,639 INFO [mcp.server.lowlevel.server] [server.py:720] [trace_id=0 span_id=0 resource.service.name=mcp-webchat trace_sampled=False] - Processing request of type ListToolsRequest
nanobot-1  | 2026-04-14 15:03:00.641 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_webchat_ui_message' from server 'webchat'
nanobot-1  | 2026-04-14 15:03:00.641 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'webchat': connected, 1 tools registered
nanobot-1  | 2026-04-14 15:03:00.642 | INFO     | nanobot.agent.loop:run:280 - Agent loop started
```

## Task 2B — Web client

<img width="1917" height="979" alt="image" src="https://github.com/user-attachments/assets/519c8916-bfe6-4668-9715-a276805ae064" />

## Task 3A — Structured logging

Happy-path log excerpt

```
backend-1  | 2026-04-14 15:18:33,777 INFO [lms_backend.main] [main.py:62] [trace_id=fea687cefc6f83013edaaaab86ab11f6 span_id=6d275b3947dea350 resource.service.name=Learning Management Service trace_sampled=True] - request_started
backend-1  | 2026-04-14 15:18:33,781 INFO [lms_backend.auth] [auth.py:30] [trace_id=fea687cefc6f83013edaaaab86ab11f6 span_id=6d275b3947dea350 resource.service.name=Learning Management Service trace_sampled=True] - auth_success
backend-1  | 2026-04-14 15:18:33,783 INFO [lms_backend.db.items] [items.py:16] [trace_id=fea687cefc6f83013edaaaab86ab11f6 span_id=6d275b3947dea350 resource.service.name=Learning Management Service trace_sampled=True] - db_query
backend-1  | 2026-04-14 15:18:33,859 INFO [lms_backend.main] [main.py:74] [trace_id=fea687cefc6f83013edaaaab86ab11f6 span_id=6d275b3947dea350 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
backend-1  | INFO:     172.19.0.9:50544 - "GET /items/ HTTP/1.1" 200 OK
backend-1  | INFO:     172.19.0.9:50544 - "GET /items/ HTTP/1.1" 200
```

Error-path log excerpt
```backend-1  | 2026-04-14 15:51:26,579 INFO [lms_backend.main] [main.py:74] [trace_id=ce494836f2e130e037d5e8c7d10a5f6d span_id=e19e9055e525ee07 resource.service.name=Learning Management Service trace_sampled=True] - request_completed
backend-1  | INFO:     172.19.0.9:56542 - "GET /items/ HTTP/1.1" 404
backend-1  | INFO:     172.19.0.9:56542 - "GET /items/ HTTP/1.1" 404 Not Found
```

<img width="1907" height="880" alt="image" src="https://github.com/user-attachments/assets/15798905-6339-42a5-b4b5-aae2097856cc" />



## Task 3B — Traces
Healthy trace

TraceID: `cc09ad81048d64bd65a3d2bbf2ef6015`
<img width="1897" height="938" alt="image" src="https://github.com/user-attachments/assets/a08c70de-a817-4036-8f90-cebcdade73e5" />

Error trace

TraceID: `9e5341cda63a8e79420171649482c714`
<img width="1280" height="309" alt="image" src="https://github.com/user-attachments/assets/2289fe1d-015a-4f44-8a0f-12e9535b0981" />


## Task 3C — Observability MCP tools

Normal conditions (PostgreSQL running)
Question: "Any LMS backend errors in the last 10 minutes?"

```
No LMS backend errors detected in the last 10 minutes. The Learning Management Service appears to be running cleanly. 🟢
```

Failure conditions (PostgreSQL stopped)
Question: "Any LMS backend errors in the last 10 minutes?"

```
Yes, there are **3 errors** in the LMS backend from the last 10 minutes. Here's what I found:

### Error Summary

| Time | Event | Details |
|------|-------|---------|
| 17:17:54 | `unhandled_exception` | Sync pipeline (`/pipeline/sync`) crashed |
| 17:17:50 | `db_query` error | SELECT on `item` table failed |
| 17:17:47 | `db_query` error | SELECT on `item` table failed |

### Root Cause

All errors share the same underlying issue: **`[Errno -2] Name or service not known`** — a DNS resolution failure. The LMS backend cannot resolve the database hostname, so it can't connect to PostgreSQL.

The stack trace shows the failure originates in `asyncpg` when trying to establish a connection:
```
socket.gaierror: [Errno -2] Name or service not known
```

This cascaded into an unhandled exception during the sync pipeline at `etl.py:230` → `load_items()`.

### Likely Causes
- Database hostname misconfigured in environment variables
- DNS service unavailable or misconfigured
- Network connectivity issue between the LMS service and the database

Would you like me to dig deeper into any specific trace or check the LMS health status?
```

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
