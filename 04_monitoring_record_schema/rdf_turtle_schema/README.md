# RDF/Turtle schema

This folder contains RDF-native schema files and a Turtle example for the monitoring-record schema. Use these files when the model needs to be inspected, queried, constrained, or loaded with RDF tools, ontology editors, SPARQL engines, SHACL validators, or triple stores.

## Files

- `monitoring_record_vocabulary.ttl`
  RDFS/OWL vocabulary defining the main classes and properties used by the monitoring-record model.

- `monitoring_record_shapes.ttl`
  SHACL shapes expressing core constraints for RDF validation.

- `monitoring_record_schema_example.ttl`
  RDF/Turtle representation of the compact JSON-LD monitoring-record example.

The JSON-LD schema remains the primary authoring format for JSON-first workflows. The RDF/Turtle schema provides an RDF-native vocabulary and validation layer for semantic-web workflows.
