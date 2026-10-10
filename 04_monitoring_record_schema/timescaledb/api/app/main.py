from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query

from .db import connect


app = FastAPI(
    title="Timber Moisture Time-Series API",
    version="0.1.0",
    description="HTTP access to live and historical measurements stored in TimescaleDB.",
)


@app.get("/api/v1/health")
def health() -> dict:
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(
            "SELECT extversion FROM pg_extension WHERE extname = 'timescaledb'"
        )
        row = cursor.fetchone()
    return {"status": "ok", "database": "connected", "timescaledb": row["extversion"]}


@app.get("/api/v1/series/{series_id}")
def get_series(series_id: str) -> dict:
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT s.*, COUNT(o.observation_id)::integer AS observation_count
            FROM tmf.monitoring_series s
            LEFT JOIN tmf.observation o ON o.series_id = s.series_id
            WHERE s.series_id = %s
            GROUP BY s.series_id
            """,
            (series_id,),
        )
        row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Monitoring series not found")
    return row


def _observations(
    field: str,
    identifier: str,
    property_id: str | None,
    start: datetime | None,
    end: datetime | None,
    limit: int,
) -> list[dict]:
    clauses = [f"{field} = %s"]
    parameters: list[object] = [identifier]
    if property_id:
        clauses.append("property_id = %s")
        parameters.append(property_id)
    if start:
        clauses.append("observed_at >= %s")
        parameters.append(start)
    if end:
        clauses.append("observed_at < %s")
        parameters.append(end)
    parameters.append(limit)

    query = f"""
        SELECT observed_at, observation_id, series_id, sensor_id, property_id,
               value, unit_iri, simple_result, quality_flag
        FROM tmf.observation
        WHERE {' AND '.join(clauses)}
        ORDER BY observed_at, property_id
        LIMIT %s
    """
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchall()


@app.get("/api/v1/series/{series_id}/observations")
def get_series_observations(
    series_id: str,
    property_id: str | None = None,
    start: datetime | None = None,
    end: datetime | None = None,
    limit: Annotated[int, Query(ge=1, le=10_000)] = 1_000,
) -> dict:
    rows = _observations("series_id", series_id, property_id, start, end, limit)
    return {"seriesId": series_id, "count": len(rows), "observations": rows}


@app.get("/api/v1/sensors/{sensor_id}/observations")
def get_sensor_observations(
    sensor_id: str,
    property_id: str | None = None,
    start: datetime | None = None,
    end: datetime | None = None,
    limit: Annotated[int, Query(ge=1, le=10_000)] = 1_000,
) -> dict:
    rows = _observations("sensor_id", sensor_id, property_id, start, end, limit)
    return {"sensorId": sensor_id, "count": len(rows), "observations": rows}


@app.get("/api/v1/series/{series_id}/summary")
def get_series_summary(
    series_id: str,
    bucket: Annotated[str, Query(pattern="^(15 minutes|1 hour|1 day)$")] = "1 hour",
) -> dict:
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT time_bucket(%s::interval, observed_at) AS bucket,
                   property_id,
                   COUNT(*)::integer AS sample_count,
                   AVG(value) AS average,
                   MIN(value) AS minimum,
                   MAX(value) AS maximum,
                   MIN(unit_iri) AS unit_iri
            FROM tmf.observation
            WHERE series_id = %s
            GROUP BY 1, property_id
            ORDER BY 1, property_id
            """,
            (bucket, series_id),
        )
        rows = cursor.fetchall()
    return {"seriesId": series_id, "bucket": bucket, "count": len(rows), "summary": rows}

