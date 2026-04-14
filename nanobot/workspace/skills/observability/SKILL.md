# Observability Skill

When the user asks about errors, failures, or problems in the system:

1. **Search logs first** — call `mcp_obs_logs_error_count` with a narrow time window (e.g., `minutes: 10`) and `service: "Learning Management Service"` to check for recent errors.

2. **Inspect details** — if errors exist, call `mcp_obs_logs_search` with a LogsQL query like `_time:10m severity:ERROR service.name:"Learning Management Service"` to see the actual error messages. Look for `trace_id` fields in the results.

3. **Fetch the trace** — if you find a `trace_id` in the logs, call `mcp_obs_traces_get` with that ID to see the full request flow and where it failed.

4. **Summarize** — give a concise answer: what failed, when, and why. Don't dump raw JSON. Example: "There were 3 database connection errors in the last 10 minutes. The backend couldn't reach PostgreSQL — 'Name or service not known'. Trace 9e5341cd shows the failure at the db_query span."

When the user asks about system health or recent activity:

- Use `mcp_obs_logs_error_count` to check for errors first.
- If no errors, say so. If there are errors, follow the steps above.

**Important:** Always scope queries to the LMS backend and a recent time window unless the user asks otherwise. Use `_time:10m` and `service.name:"Learning Management Service"` by default.
