# JSON-LD schema

This folder contains the JSON-first schema files for the monitoring-record schema. The compact JSON-LD graph links static project context, sensor installations, representative observations, validation records, moisture-related events, and lifecycle-integration records. Detailed time-series observations, validation checks, and event entries are stored as linked JSON files.

## Files

- `monitoring_record_schema_context.jsonld`
  JSON-LD context for compact field names, identifiers, datatypes, and links.
- `monitoring_record_schema_example.jsonld`
  Compact JSON-LD graph for the CLT kitchen-floor framework implementation example.
- `monitoring_record_schema.schema.json`
  JSON Schema for validating the compact JSON-LD graph.
- `monitoring_timeseries_MS-L01-001.json`
  Linked JSON time-series observation file referenced from the compact graph.
- `monitoring_timeseries.schema.json`
  JSON Schema for validating linked time-series observation files.
- `validation_log_VAL-L01-001.json`
  Linked JSON validation log referenced from the compact graph.
- `validation_log.schema.json`
  JSON Schema for validating linked validation logs.
- `event_log_EVT-L01-001.json`
  Linked JSON moisture-related event log referenced from the compact graph.
- `event_log.schema.json`
  JSON Schema for validating linked event logs.

Use this folder when creating, validating, or adapting monitoring records as JSON/JSON-LD.
