# PostgreSQL and TimescaleDB implementation

This implementation keeps semantic metadata and relationships in GraphDB while storing timestamped sensor observations in PostgreSQL with the TimescaleDB extension. A small HTTP API provides stable links from RDF resources to live time-series data without exposing database credentials.

## Components

- `db`: PostgreSQL 17 with TimescaleDB and a persistent Docker volume.
- `api`: read-only HTTP endpoints for monitoring series, sensor observations, and time-bucket summaries.
- `import-sample`: repeatable importer for the existing monitoring time-series JSON document.
- `rdf/timeseries_api_links.local.ttl`: local GraphDB links to the API endpoints.

Both database and API ports are bound to `127.0.0.1`, so they are available only from this computer.

## Start the database and API

From this folder:

```powershell
Copy-Item .env.example .env
docker compose up -d --build db api
docker compose ps
```

For this repository checkout, a local `.env` has already been created and is ignored by Git. Change its password before using the implementation outside a local development computer.

Check the API and its interactive documentation:

- Health: <http://localhost:8000/api/v1/health>
- API documentation: <http://localhost:8000/docs>

## Import the example observations

```powershell
docker compose --profile tools run --rm import-sample
```

The import is idempotent: rerunning it updates the same observations instead of duplicating them.

Verify the imported monitoring series:

- Metadata: <http://localhost:8000/api/v1/series/MS-L01-001>
- All observations: <http://localhost:8000/api/v1/series/MS-L01-001/observations>
- Moisture content only: <http://localhost:8000/api/v1/series/MS-L01-001/observations?property_id=moisture-content>
- Hourly summary: <http://localhost:8000/api/v1/series/MS-L01-001/summary?bucket=1%20hour>

## Add the endpoint URLs to GraphDB

Import `rdf/timeseries_api_links.local.ttl` into the existing `timber-moisture` GraphDB repository using the default graph. The sensor and monitoring-series nodes will then have a `timeSeriesDataEndpoint` relationship pointing to the local API.

The `MC-L05-01` endpoint is intentionally present even when that sensor has no observations yet. It returns an empty observation collection until reference-sensor measurements are ingested.

## Inspect the database directly

```powershell
docker compose exec db psql -U tmf_app -d timber_moisture
```

Useful SQL checks:

```sql
SELECT * FROM timescaledb_information.hypertables;

SELECT series_id, count(*)
FROM tmf.observation
GROUP BY series_id;

SELECT *
FROM tmf.latest_observation
ORDER BY sensor_id, property_id;
```

Exit `psql` with `\q`.

## Stop the services

```powershell
docker compose down
```

This preserves the database volume. Deleting the volume with `docker compose down -v` removes all imported database data and should only be used when deliberately starting over.

