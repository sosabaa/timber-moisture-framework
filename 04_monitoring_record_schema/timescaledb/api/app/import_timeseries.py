from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from psycopg.types.json import Jsonb

from .db import connect
from .mapping import expand_iri, identifier, map_observation, parse_timestamp


def import_timeseries(path: Path) -> tuple[str, int]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    base_url = os.getenv("API_PUBLIC_BASE_URL", "http://localhost:8000").rstrip("/")

    series_id = payload["seriesId"]
    series_iri = expand_iri(payload["seriesIri"])
    location_id = identifier(payload["location"])
    location_iri = expand_iri(payload["location"])
    reference_location = payload.get("hasReferenceLocation")
    reference_location_id = identifier(reference_location) if reference_location else None
    installation_id = identifier(payload["installation"])
    installation_iri = expand_iri(payload["installation"])
    sensor_id = identifier(payload["madeBySensor"])
    sensor_iri = expand_iri(payload["madeBySensor"])
    reference_sensor = payload.get("usesReferenceSensor")

    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tmf.location (location_id, iri)
                VALUES (%s, %s)
                ON CONFLICT (location_id) DO UPDATE SET iri = EXCLUDED.iri
                """,
                (location_id, location_iri),
            )

            if reference_location_id:
                cursor.execute(
                    """
                    INSERT INTO tmf.location (location_id, iri)
                    VALUES (%s, %s)
                    ON CONFLICT (location_id) DO UPDATE SET iri = EXCLUDED.iri
                    """,
                    (reference_location_id, expand_iri(reference_location)),
                )

            cursor.execute(
                """
                INSERT INTO tmf.sensor (sensor_id, iri, location_id, data_endpoint)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (sensor_id) DO UPDATE SET
                  iri = EXCLUDED.iri,
                  location_id = EXCLUDED.location_id,
                  data_endpoint = EXCLUDED.data_endpoint
                """,
                (
                    sensor_id,
                    sensor_iri,
                    location_id,
                    f"{base_url}/api/v1/sensors/{sensor_id}/observations",
                ),
            )

            if reference_sensor and reference_location_id:
                reference_sensor_id = identifier(reference_sensor)
                cursor.execute(
                    """
                    INSERT INTO tmf.sensor (sensor_id, iri, location_id, data_endpoint)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (sensor_id) DO UPDATE SET
                      iri = EXCLUDED.iri,
                      location_id = EXCLUDED.location_id,
                      data_endpoint = EXCLUDED.data_endpoint
                    """,
                    (
                        reference_sensor_id,
                        expand_iri(reference_sensor),
                        reference_location_id,
                        f"{base_url}/api/v1/sensors/{reference_sensor_id}/observations",
                    ),
                )

            cursor.execute(
                """
                INSERT INTO tmf.sensor_installation
                  (installation_id, iri, sensor_id, location_id)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (installation_id) DO UPDATE SET
                  iri = EXCLUDED.iri,
                  sensor_id = EXCLUDED.sensor_id,
                  location_id = EXCLUDED.location_id
                """,
                (installation_id, installation_iri, sensor_id, location_id),
            )

            properties = set(payload["observedProperty"])
            properties.update(item["observedProperty"] for item in payload["observations"])
            for property_ref in sorted(properties):
                cursor.execute(
                    """
                    INSERT INTO tmf.observed_property (property_id, iri)
                    VALUES (%s, %s)
                    ON CONFLICT (property_id) DO UPDATE SET iri = EXCLUDED.iri
                    """,
                    (identifier(property_ref), expand_iri(property_ref)),
                )

            cursor.execute(
                """
                INSERT INTO tmf.monitoring_series (
                  series_id, iri, sensor_id, installation_id, location_id,
                  reference_location_id, starts_at, ends_at, sampling_interval,
                  data_endpoint
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s::interval, %s)
                ON CONFLICT (series_id) DO UPDATE SET
                  iri = EXCLUDED.iri,
                  sensor_id = EXCLUDED.sensor_id,
                  installation_id = EXCLUDED.installation_id,
                  location_id = EXCLUDED.location_id,
                  reference_location_id = EXCLUDED.reference_location_id,
                  starts_at = EXCLUDED.starts_at,
                  ends_at = EXCLUDED.ends_at,
                  sampling_interval = EXCLUDED.sampling_interval,
                  data_endpoint = EXCLUDED.data_endpoint
                """,
                (
                    series_id,
                    series_iri,
                    sensor_id,
                    installation_id,
                    location_id,
                    reference_location_id,
                    parse_timestamp(payload["seriesStart"]),
                    parse_timestamp(payload["seriesEnd"]),
                    payload.get("samplingInterval"),
                    f"{base_url}/api/v1/series/{series_id}/observations",
                ),
            )

            rows = []
            for observation in payload["observations"]:
                mapped = map_observation(observation, series_id, sensor_id)
                rows.append((*mapped[:-1], Jsonb(mapped[-1])))

            cursor.executemany(
                """
                INSERT INTO tmf.observation (
                  observed_at, observation_id, series_id, sensor_id, property_id,
                  value, unit_iri, simple_result, quality_flag, raw_payload
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (observed_at, observation_id) DO UPDATE SET
                  value = EXCLUDED.value,
                  unit_iri = EXCLUDED.unit_iri,
                  simple_result = EXCLUDED.simple_result,
                  quality_flag = EXCLUDED.quality_flag,
                  raw_payload = EXCLUDED.raw_payload,
                  ingested_at = now()
                """,
                rows,
            )

    return series_id, len(payload["observations"])


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m app.import_timeseries PATH_TO_JSON")
    series_id, count = import_timeseries(Path(sys.argv[1]))
    print(f"Imported {count} observations for {series_id}.")


if __name__ == "__main__":
    main()

