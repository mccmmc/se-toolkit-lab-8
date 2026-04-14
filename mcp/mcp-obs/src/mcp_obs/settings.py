"""Settings for the observability MCP server."""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    nanobot_victorialogs_url: str = Field(
        default="http://victorialogs:9428",
        alias="NANOBOT_VICTORIALOGS_URL",
    )
    nanobot_victoriatraces_url: str = Field(
        default="http://victoriatraces:10428",
        alias="NANOBOT_VICTORIATRACES_URL",
    )


def resolve_settings() -> Settings:
    return Settings.model_validate({})
