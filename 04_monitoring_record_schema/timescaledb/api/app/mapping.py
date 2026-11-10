from __future__ import annotations

from datetime import datetime
from typing import Any


PREFIXES = {
    "tmf:": "https://sosabaa.github.io/timber-moisture-framework/",
    "unit:": "http://qudt.org/vocab/unit/",
}


def expand_iri(value: str) -> str:
    for prefix, base in PREFIXES.items():
        if value.startswith(prefix):
            return base + value[len(prefix) :]
    return value


def identifier(value: str) -> str:
    expanded = expand_iri(value).rstrip("/")
    return expanded.rsplit("/", 1)[-1].rsplit("#", 1)[-1]


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def map_observation(
    observation: dict[str, Any], series_id: str, sensor_id: str
) -> tuple[Any, ...]:
    return (
        parse_timestamp(observation["timestamp"]),
        observation["observationId"],
        series_id,
        sensor_id,
        identifier(observation["observedProperty"]),
        float(observation["resultValue"]),
        expand_iri(observation["resultUnit"]),
        observation.get("simpleResult"),
        observation.get("dataQualityFlag"),
        observation,
    )

