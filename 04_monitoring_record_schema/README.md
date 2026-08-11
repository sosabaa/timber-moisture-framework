# Monitoring-record schema

This folder contains a template and implementation examples for structuring moisture-monitoring records in mass-timber buildings. It supports the transition from sensor deployment to interpretable lifecycle records by linking SOSA observations, QUDT quantity values, sensor metadata, element information, validation flags, moisture-event indicators, and lifecycle decision context.

The template is intended to be used after the risk-location classification and sensor-deployment steps. It does not prescribe a specific database format, software platform, or digital twin structure. Users should adapt the schema to the selected sensor system, project data environment, BIM model, building logbook, product passport, or other lifecycle information system.

## Folder contents

- `monitoring_record_schema_template.md`
  Human-readable template for documenting the fields required to preserve the meaning, quality, and later usability of moisture-monitoring records.

- `json_jsonld_implementation/`
  JSON and JSON-LD implementation files, including the compact JSON-LD graph, JSON-LD context, linked JSON time-series, validation and event logs, and JSON Schemas.

- `rdf_ttl_implementation/`
  RDF/Turtle implementation of the compact monitoring-record graph for RDF tools, SPARQL engines, ontology workflows, or triple stores.

- `knowledge_graph_visualizer.html`
  Static browser visualizer for plotting the repository JSON-LD example or a user-supplied compacted monitoring-record graph.
  https://sosabaa.github.io/timber-moisture-framework/04_monitoring_record_schema/knowledge_graph_visualizer.html

## Using and validating the data artifacts

Use `monitoring_record_schema_template.md` to decide which location, sensor, measurement, validation, moisture-related event, lifecycle-event, and lifecycle-integration fields need to be retained for a project.

Use `json_jsonld_implementation/` when creating and validating monitoring records as JSON/JSON-LD. The compact JSON-LD graph links persistent identifiers for locations, elements, sensors, installations, observations, validation records, moisture-related events, and lifecycle-integration records. Detailed time-series observations, validation checks, and event entries are stored as linked JSON files.

Use `rdf_ttl_implementation/` when an RDF-native serialization is needed. The Turtle file expresses the same compact semantic structure in a form that can be loaded into RDF tooling.

Open `knowledge_graph_visualizer.html` in a browser to inspect the compact graph visually. When opened through a local web server, the visualizer can load the JSON-LD example from `json_jsonld_implementation/` directly. When opened from the file system, use the file picker to load the JSON-LD example, or paste a compacted JSON-LD graph into the text area. Nodes can be moved by dragging them, and `Reset view` restores the automatic layout.

Recommended workflow:

1. Complete the risk-location and sensor-deployment templates.
2. Define persistent IDs for locations, elements, sensors, installations, measurements, moisture-related events, and integration records.
3. Create a parent `MonitoringTimeSeries` node for the selected monitoring period, then store detailed per-property observations directly in a linked JSON observation data file.
4. Validate the compact JSON-LD graph against `json_jsonld_implementation/monitoring_record_schema.schema.json`.
5. Validate linked JSON files against `json_jsonld_implementation/monitoring_timeseries.schema.json`, `json_jsonld_implementation/validation_log.schema.json`, and `json_jsonld_implementation/event_log.schema.json` where those files are used.
6. Use the Turtle implementation where RDF-native tooling or SPARQL-based workflows are required.
