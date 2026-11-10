CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE SCHEMA IF NOT EXISTS tmf;

CREATE TABLE IF NOT EXISTS tmf.location (
  location_id TEXT PRIMARY KEY,
  iri TEXT NOT NULL UNIQUE,
  description TEXT
);

CREATE TABLE IF NOT EXISTS tmf.sensor (
  sensor_id TEXT PRIMARY KEY,
  iri TEXT NOT NULL UNIQUE,
  location_id TEXT NOT NULL REFERENCES tmf.location(location_id),
  data_endpoint TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tmf.sensor_installation (
  installation_id TEXT PRIMARY KEY,
  iri TEXT NOT NULL UNIQUE,
  sensor_id TEXT NOT NULL REFERENCES tmf.sensor(sensor_id),
  location_id TEXT NOT NULL REFERENCES tmf.location(location_id)
);

CREATE TABLE IF NOT EXISTS tmf.observed_property (
  property_id TEXT PRIMARY KEY,
  iri TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS tmf.monitoring_series (
  series_id TEXT PRIMARY KEY,
  iri TEXT NOT NULL UNIQUE,
  sensor_id TEXT NOT NULL REFERENCES tmf.sensor(sensor_id),
  installation_id TEXT NOT NULL REFERENCES tmf.sensor_installation(installation_id),
  location_id TEXT NOT NULL REFERENCES tmf.location(location_id),
  reference_location_id TEXT REFERENCES tmf.location(location_id),
  starts_at TIMESTAMPTZ NOT NULL,
  ends_at TIMESTAMPTZ,
  sampling_interval INTERVAL,
  data_endpoint TEXT NOT NULL,
  CHECK (ends_at IS NULL OR ends_at >= starts_at)
);

CREATE TABLE IF NOT EXISTS tmf.observation (
  observed_at TIMESTAMPTZ NOT NULL,
  observation_id TEXT NOT NULL,
  series_id TEXT NOT NULL REFERENCES tmf.monitoring_series(series_id),
  sensor_id TEXT NOT NULL REFERENCES tmf.sensor(sensor_id),
  property_id TEXT NOT NULL REFERENCES tmf.observed_property(property_id),
  value DOUBLE PRECISION NOT NULL,
  unit_iri TEXT NOT NULL,
  simple_result TEXT,
  quality_flag TEXT,
  raw_payload JSONB,
  ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (observed_at, observation_id)
);

SELECT create_hypertable(
  'tmf.observation',
  by_range('observed_at', INTERVAL '7 days'),
  if_not_exists => TRUE
);

CREATE INDEX IF NOT EXISTS observation_sensor_time_idx
  ON tmf.observation (sensor_id, observed_at DESC);

CREATE INDEX IF NOT EXISTS observation_series_property_time_idx
  ON tmf.observation (series_id, property_id, observed_at DESC);

CREATE OR REPLACE VIEW tmf.latest_observation AS
SELECT DISTINCT ON (sensor_id, property_id)
  sensor_id,
  property_id,
  observed_at,
  value,
  unit_iri,
  quality_flag,
  observation_id,
  series_id
FROM tmf.observation
ORDER BY sensor_id, property_id, observed_at DESC;

