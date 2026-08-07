# Monitoring-record schema

This folder contains a template for structuring moisture-monitoring records in mass-timber buildings. It supports the transition from sensor deployment to interpretable lifecycle records by linking SOSA observations, QUDT quantity values, sensor metadata, element information, validation flags, moisture-event indicators, and lifecycle decision context.

The template is intended to be used after the risk-location classification and sensor-deployment steps. It does not prescribe a specific database format, software platform, or digital twin structure. Users should adapt the schema to the selected sensor system, project data environment, BIM model, building logbook, product passport, or other lifecycle information system.

## Folder contents

- `monitoring_record_schema_template.md`
  Template for documenting the data fields required to preserve the meaning, quality, and later usability of moisture-monitoring records.
- `monitoring_record_schema_context.jsonld`
  JSON-LD context for the compacted monitoring-record graph.

- `monitoring_record_schema_example.jsonld`
  Example linked monitoring record for the CLT kitchen-floor application.

- `monitoring_timeseries_MS-L01-001.json`
  Linked observation data file containing the two-day one-sensor time series referenced from `MS-L01-001`.

- `validation_log_VAL-L01-001.json`, `event_log_EVT-L01-001.json`
  Linked JSON logs containing fuller validation checks, moisture-event interpretation details, and lifecycle-event entries referenced from the compact graph nodes.

- `knowledge_graph_visualizer.html`
  Static browser visualizer for plotting the repository JSON-LD example or a user-supplied compacted monitoring-record graph.
https://sosabaa.github.io/timber-moisture-framework/04_monitoring_record_schema/knowledge_graph_visualizer.html

- `monitoring_record_schema.schema.json`
  JSON Schema for checking the compacted JSON-LD graph structure, required identifiers, links, timestamps, SOSA observation fields, and QUDT quantity values.

- `logger_export_mapping_example.csv`
  Minimal logger-export table showing how raw logger rows can be mapped into per-property JSON-LD observation records.

- `logger_export_mapping.md`
  Short mapping note explaining how CSV columns become JSON-LD fields and linked identifiers.

## Using and validating the data artifacts

Use `monitoring_record_schema_template.md` to decide which location, sensor, measurement, validation, exposure, lifecycle-event, and lifecycle-integration fields need to be retained for a project. The Markdown template is the human-readable planning document.

Use `monitoring_record_schema_context.jsonld` when creating compacted JSON-LD records. The context defines the compact field names, identifier links, and datatypes used by the example graph.

Use `monitoring_record_schema.schema.json` to check whether a compacted JSON-LD file has the expected graph structure. A JSON Schema validator can be used to confirm that required nodes include identifiers, links, timestamps, observed properties, and QUDT quantity values where applicable.

Use `monitoring_record_schema_example.jsonld` as a minimal reference implementation. It shows how a risk location, reference location, timber elements, observable properties, sensors, installation, parent monitoring time series, a linked JSON observation data file, three illustrative timestamped observations, linked validation and event logs, and lifecycle-integration records are connected through persistent IDs.

Open `knowledge_graph_visualizer.html` in a browser to inspect the graph visually. When opened through a local web server, the visualizer can load `monitoring_record_schema_example.jsonld` directly. When opened from the file system, use the file picker to load the JSON-LD example, or paste a compacted JSON-LD graph into the text area. Nodes can be moved by dragging them, and `Reset view` restores the automatic layout.

Use `logger_export_mapping_example.csv` together with `logger_export_mapping.md` when converting raw logger exports into JSON-LD observations. Static entities such as locations, sensors, installations, and observable properties should be stored once and linked from each observation rather than repeated in every row.

Recommended workflow:

1. Complete the risk-location and sensor-deployment templates.
2. Define persistent IDs for locations, elements, sensors, installations, measurements, moisture-related events, and integration records. Record installation coordinates as compact WGS84 GPS-style DMS strings, for example `57°46'34.8" N`.
3. Create a parent `MonitoringTimeSeries` node for the logger series or selected time window, then store the detailed per-property observations in a linked observation data file. Format observation IDs as `M-{LocationID}-{PropertyCode}-{Timestamp}`, for example `M-L01-MC-20250626T002555202Z`. A compact JSON-LD graph can also include one or a few representative timestamped observations as examples.
4. Store validation outcomes as sensor and observation properties where quick interpretation is needed, and keep fuller validation checks in a linked JSON log referenced from the `ValidationRecord` through `hasValidationLog`. The validation log should state exactly which observations, sensor, and monitoring series were validated, when the validation happened, and what each target was validated against.
5. Add compact `LifecycleEvent` / `MoistureRelatedEvent` and `LifecycleIntegrationRecord` nodes where the monitoring record supports maintenance, post-event assessment, repair decisions, or future reuse-related assessment. Keep event-specific details such as threshold exceedance, moisture dose, drying behaviour, anomaly indicators, inspection actions, and outcomes in the linked event log referenced through `hasEventLog`.
6. Validate the resulting compacted JSON-LD graph against `monitoring_record_schema.schema.json`.
