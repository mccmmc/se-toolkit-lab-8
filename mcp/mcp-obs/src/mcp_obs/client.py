"""HTTP clients for VictoriaLogs and VictoriaTraces APIs."""

from __future__ import annotations

import httpx


class VictoriaLogsClient:
    """Client for the VictoriaLogs HTTP API."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(base_url=self._base_url, timeout=30.0)

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> VictoriaLogsClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()

    async def query_logs(self, logsql: str, limit: int = 50) -> str:
        """Execute a LogsQL query and return raw response text."""
        resp = await self._client.get(
            "/select/logsql/query",
            params={"query": logsql, "limit": limit},
        )
        resp.raise_for_status()
        return resp.text

    async def count_errors(self, service: str | None, minutes: int) -> str:
        """Count error-level log entries in the last N minutes."""
        time_filter = f"_time:{minutes}m"
        parts = [time_filter, "severity:ERROR"]
        if service:
            parts.append(f'service.name:"{service}"')
        logsql = " ".join(parts)
        resp = await self._client.get(
            "/select/logsql/query",
            params={"query": logsql, "limit": 1000},
        )
        resp.raise_for_status()
        return resp.text


class VictoriaTracesClient:
    """Client for the VictoriaTraces Jaeger-compatible HTTP API."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url.rstrip("/")
        self._client = httpx.AsyncClient(base_url=self._base_url, timeout=30.0)

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> VictoriaTracesClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()

    async def list_traces(self, service: str, limit: int = 10) -> str:
        """List recent traces for a service."""
        resp = await self._client.get(
            "/select/jaeger/api/traces",
            params={"service": service, "limit": limit},
        )
        resp.raise_for_status()
        return resp.text

    async def get_trace(self, trace_id: str) -> str:
        """Fetch a specific trace by ID."""
        resp = await self._client.get(
            f"/select/jaeger/api/traces/{trace_id}",
        )
        resp.raise_for_status()
        return resp.text
