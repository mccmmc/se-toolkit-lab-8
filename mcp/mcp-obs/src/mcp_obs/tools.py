"""Tool schemas and handlers for the observability MCP server."""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass

from mcp.types import Tool
from pydantic import BaseModel, Field

from mcp_obs.client import VictoriaLogsClient, VictoriaTracesClient


ToolPayload = str


@dataclass(frozen=True, slots=True)
class ToolSpec:
    name: str
    description: str
    model: type[BaseModel]
    handler: Callable[
        [VictoriaLogsClient, VictoriaTracesClient, BaseModel],
        Awaitable[ToolPayload],
    ]

    def as_tool(self) -> Tool:
        schema = self.model.model_json_schema()
        schema.pop("$defs", None)
        schema.pop("title", None)
        return Tool(name=self.name, description=self.description, inputSchema=schema)


class LogsSearchParams(BaseModel):
    query: str = Field(
        description="LogsQL query, e.g. '_time:10m severity:ERROR service.name:\"Learning Management Service\"'"
    )
    limit: int = Field(default=50, ge=1, le=200, description="Max log entries to return")


class LogsErrorCountParams(BaseModel):
    service: str | None = Field(
        default=None,
        description='Service name to filter, e.g. "Learning Management Service". Omit for all services.',
    )
    minutes: int = Field(default=10, ge=1, le=1440, description="Time window in minutes")


class TracesListParams(BaseModel):
    service: str = Field(
        default="Learning Management Service",
        description="Service name to list traces for",
    )
    limit: int = Field(default=10, ge=1, le=50, description="Max traces to return")


class TracesGetParams(BaseModel):
    trace_id: str = Field(description="Trace ID to fetch, e.g. '9e5341cda63a8e79420171649482c714'")


async def _logs_search(
    logs: VictoriaLogsClient, _traces: VictoriaTracesClient, args: BaseModel
) -> ToolPayload:
    params = args if isinstance(args, LogsSearchParams) else LogsSearchParams.model_validate(args)
    return await logs.query_logs(params.query, params.limit)


async def _logs_error_count(
    logs: VictoriaLogsClient, _traces: VictoriaTracesClient, args: BaseModel
) -> ToolPayload:
    params = args if isinstance(args, LogsErrorCountParams) else LogsErrorCountParams.model_validate(args)
    return await logs.count_errors(params.service, params.minutes)


async def _traces_list(
    _logs: VictoriaLogsClient, traces: VictoriaTracesClient, args: BaseModel
) -> ToolPayload:
    params = args if isinstance(args, TracesListParams) else TracesListParams.model_validate(args)
    return await traces.list_traces(params.service, params.limit)


async def _traces_get(
    _logs: VictoriaLogsClient, traces: VictoriaTracesClient, args: BaseModel
) -> ToolPayload:
    params = args if isinstance(args, TracesGetParams) else TracesGetParams.model_validate(args)
    return await traces.get_trace(params.trace_id)


TOOL_SPECS: tuple[ToolSpec, ...] = (
    ToolSpec(
        "mcp_obs_logs_search",
        "Search VictoriaLogs using LogsQL. Use to find errors, debug issues, or extract trace IDs from logs. "
        "Example query: '_time:10m severity:ERROR service.name:\"Learning Management Service\"'",
        LogsSearchParams,
        _logs_search,
    ),
    ToolSpec(
        "mcp_obs_logs_error_count",
        "Count recent errors in VictoriaLogs. Returns error log entries for the specified service within the time window. "
        "Use this first when asked about errors or failures.",
        LogsErrorCountParams,
        _logs_error_count,
    ),
    ToolSpec(
        "mcp_obs_traces_list",
        "List recent distributed traces for a service. Each trace shows a request flowing through services with timing.",
        TracesListParams,
        _traces_list,
    ),
    ToolSpec(
        "mcp_obs_traces_get",
        "Fetch a full trace by trace ID. Use after finding a trace_id in the logs.",
        TracesGetParams,
        _traces_get,
    ),
)

TOOLS_BY_NAME = {spec.name: spec for spec in TOOL_SPECS}
