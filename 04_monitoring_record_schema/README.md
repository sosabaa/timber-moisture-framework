# Monitoring-record schema

This folder contains a template and schema files for structuring moisture-monitoring records in mass-timber buildings. It supports the transition from sensor deployment to interpretable lifecycle records by linking SOSA observations, QUDT quantity values, sensor metadata, element information, validation flags, moisture-event indicators, and lifecycle decision context.

The template is intended to be used after the risk-location classification and sensor-deployment steps. It does not prescribe a specific database format, software platform, or digital twin structure. Users should adapt the schema to the selected sensor system, project data environment, BIM model, building logbook, product passport, or other lifecycle information system.

## Folder contents

- `monitoring_record_schema_template.md`
  Human-readable template for documenting the fields required to preserve the meaning, quality, and later usability of moisture-monitoring records.

- `json_ld_schema/`
  JSON-LD schema files, including the compact JSON-LD graph, JSON-LD context, linked JSON time-series, validation and event logs, and JSON Schemas.

- `rdf_turtle_schema/`
  RDF/Turtle schema files, including an RDFS/OWL vocabulary, SHACL shapes, and a Turtle representation of the compact monitoring-record graph.

- `knowledge_graph_visualizer.html`
  Static browser visualizer for plotting the repository JSON-LD example or a user-supplied compacted monitoring-record graph.
  https://sosabaa.github.io/timber-moisture-framework/04_monitoring_record_schema/knowledge_graph_visualizer.html

## Using and validating the data artifacts

Use `monitoring_record_schema_template.md` to decide which location, sensor, measurement, validation, moisture-related event, lifecycle-event, and lifecycle-integration fields need to be retained for a project.

Use `json_ld_schema/` when creating and validating monitoring records as JSON/JSON-LD. The compact JSON-LD graph links persistent identifiers for locations, elements, sensors, installations, observations, validation records, moisture-related events, and lifecycle-integration records. Detailed time-series observations, validation checks, and event entries are stored as linked JSON files.

Use `rdf_turtle_schema/` when RDF-native schema files are needed. The vocabulary defines classes and properties, the SHACL shapes express core constraints, and the Turtle example expresses the compact semantic structure in a form that can be loaded into RDF tooling.

Open `knowledge_graph_visualizer.html` in a browser to inspect the compact graph visually. When opened through a local web server, the visualizer can load the JSON-LD example from `json_ld_schema/` directly. When opened from the file system, use the file picker to load the JSON-LD example, or paste a compacted JSON-LD graph into the text area. Nodes can be moved by dragging them, and `Reset view` restores the automatic layout.

Recommended workflow:

1. Complete the risk-location and sensor-deployment templates.
2. Define persistent IDs for locations, elements, sensors, installations, measurements, moisture-related events, and integration records.
3. Create a parent `MonitoringTimeSeries` node for the selected monitoring period, then store detailed per-property observations directly in a linked JSON observation data file.
4. Validate the compact JSON-LD graph against `json_ld_schema/monitoring_record_schema.schema.json`.
5. Validate linked JSON files against `json_ld_schema/monitoring_timeseries.schema.json`, `json_ld_schema/validation_log.schema.json`, and `json_ld_schema/event_log.schema.json` where those files are used.
6. Use the RDF/Turtle schema where RDF-native validation, ontology, or SPARQL-based workflows are required.
