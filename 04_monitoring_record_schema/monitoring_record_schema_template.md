# Monitoring-record schema template

This template supports Layers 4, 5, 6, and 8 of the framework: data and metadata capture, validation, moisture-event interpretation, and lifecycle integration. It defines the information needed to convert sensor readings into interpretable moisture-related event records.

The schema should be adapted to the selected sensor system, data platform, BIM model, building logbook, product passport, or other lifecycle information system.

## Schema structure

The monitoring-record schema separates static, semi-static, dynamic, derived, and event-based information. This prevents time-series measurements from being mixed with location and element metadata, while preserving the links needed for later interpretation.

| Data table | Data type | Purpose | Main linking field |
|---|---|---|---|
| Location register | Static/contextual data | Defines the monitored risk location, building zone, assembly, timber element, and moisture-risk context. | Location ID |
| Sensor installation register | Semi-static sensor metadata | Defines the installed sensor or sensor channel, including sensor type, measurement depth, calibration basis, and installation context. | Sensor ID / Installation ID |
| Monitoring time-series register | Dynamic dataset metadata | Defines the whole time-series record for a location, sensor installation, observed properties, time span, sampling interval, and linked observation data file. | Series ID |
| Observation data file | Dynamic measurement data | Stores timestamped per-property observations for MC, RH, temperature, or raw sensor readings outside the compact JSON-LD graph. | Observation file URL / Observation ID |
| Validation log | Derived/quality data | Stores data-quality checks, missing-data flags, implausible values, drift concerns, communication gaps, and redundancy agreement in a linked JSON file. | Validation log URL / Validation ID |
| Moisture-related event log | Event-based and interpretation data | Stores threshold exceedance, duration, moisture dose, drying behaviour, anomaly indicators, leakage reports, inspection, maintenance, repair, sensor replacement, recalibration, and reuse-related assessment notes in a linked JSON file. | Event log URL / Event ID |
| Lifecycle integration register | Linkage data | Links the record to BIM objects, building logbooks, product passports, digital twins, or other lifecycle information systems. | Location ID / Element ID |

| Identifier | Definition |
|---|---|
| Location ID | Identifies the monitored risk location, for example L-01. |
| Sensor ID | Identifies the physical sensor or sensor channel. |
| Installation ID | Identifies a specific installation of a sensor at a location. Useful if a sensor is replaced or recalibrated. |
| Series ID | Identifies the whole monitoring time series for a location, sensor installation, and period. |
| Measurement ID | Identifies one timestamped per-property observation. Format observation IDs as `M-{LocationID}-{PropertyCode}-{Timestamp}`, for example `M-L01-MC-20260807T110000000Z`. When a timestamp contains several measured properties, use one observation ID per property. |
| Event ID | Identifies a moisture-related event, such as a threshold exceedance, leakage, inspection, repair, maintenance action, recalibration, or sensor replacement. |

## JSON-LD implementation

The schema can be implemented in JSON-LD by treating each table as a linked resource type. Static location data, sensor installation metadata, dynamic time-series observations, validation records, moisture-related lifecycle events, and lifecycle integration records are stored as separate entities in an `@graph`. These entities are connected through persistent identifiers such as `Location ID`, `Sensor ID`, `Installation ID`, `Measurement ID`, and `Event ID`.

This structure prevents hourly measurements from repeating static metadata while preserving traceability from each sensor reading to the monitored location, timber element, sensor installation, validation record, moisture-related event, and lifecycle information system.

The monitoring period should be represented by a parent `MonitoringTimeSeries` / `schema:Dataset` node. The parent stores the shared location, sensor installation, sensor, observed properties, start and end time, sampling interval, and links to the observation data file through `hasObservation`. This keeps the knowledge graph compact while the detailed time-series values remain in a linked JSON file.

For a more SOSA-idiomatic graph, each measured property is represented as its own `sosa:Observation`. A timestamp containing MC, RH, and temperature therefore contains three observation nodes, each with its own `observedProperty`, `hasSimpleResult`, and QUDT `resultQuantity`. Numeric values such as moisture content, relative humidity, temperature, and measurement depth are represented as `qudt:QuantityValue` objects with `numericValue` and `unitRef`.

The compact graph may include one representative MC, RH, and temperature observation to show the SOSA pattern, while the full time series remains in the linked observation data file. Validation and moisture-related event details can follow the same compact-plus-linked-file pattern through `hasValidationLog` and `hasEventLog`.

## Location register
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Location ID | Required | L-01 | Links to risk classification, sensor deployment, and measurement records. |
| Description | Required | Sink/dishwasher zone below plumbing and appliance connections | Short location description. |
| Lifecycle context | Optional | Operational monitoring | Lifecycle stage or context for which monitoring is initiated. |
| Monitoring purpose | Optional | Maintenance; post-event assessment; future reuse-related evidence | Purpose of monitoring this location. |
| Building zone | Required | Kitchen | Broad spatial or functional zone. |
| Assembly/detail | Required | CLT floor below sink and dishwasher | Specific assembly or detail. |
| Element ID | Required | CLT-FP-01 | Timber element, panel, beam, column, or BIM element ID. |
| Element/material feature | Required | Panel surface, panel edge, local fastener areas, concealed regions beneath cabinetry | Specific feature being monitored. |
| Moisture source or mechanism | Required | Leakage, repeated small leaks, cleaning water, trapped moisture beneath finishes | Expected moisture mechanism. |
| Risk class | Required | High | Carried over from risk-location classification. |
| Decision relevance | Required | High | Explains why the location matters for later decisions. |
| Reference location ID | Optional | L-05 | Baseline or reference location used to interpret whether moisture behaviour is local or general. |
| Location notes | Optional | Near plumbing and appliance connection zone | Additional context. |

## Sensor installation register
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Installation ID | Required | INST-L01-01 | Unique installation record. |
| Location ID | Required | L-01 | Links sensor installation to the risk location. |
| Sensor ID | Required | MC-L01-01 | Unique sensor or sensor channel ID. |
| Sensor type | Required | MC sensor | Primary or supporting sensor type. |
| Measurement principle | Optional | Resistance-based MC | Depends on sensor system. |
| Sensor validation status | Optional | Validated / not assessed / requires review | Current validation state for the sensor or sensor output. |
| Sensor validation record | Optional | VAL-L01-001 | Links the sensor to the validation record supporting the stated status. |
| Measurement depth | Required | 20 mm | In JSON-LD, record as a QUDT quantity value such as `{"type": "QuantityValue", "numericValue": 20, "unitRef": "unit:MilliM"}`. |
| Installation coordinates | Required | 57°46'34.8" N; 14°09'34.2" E | Global GPS-style coordinates for the installed sensor point. In JSON-LD, record latitude and longitude as compact WGS84 DMS strings. |
| Sensor placement description | Required | Below sink/dishwasher connection zone, near panel edge | Descriptive placement. |
| Calibration basis | Required where available | Manufacturer timber MC calibration | Needed for later interpretation. |
| Correction method | Required where available | Temperature correction applied/not applied | Important for comparability. |
| Installation date | Required | 2026-08-06T07:00:00.000Z | Date of installation. |
| Installation condition | Required | Installed after floor enclosure, before cabinetry | Construction/use context. |
| Protection/access arrangement | Optional | Cable protected behind service access panel | Practical access and protection information. |
| Sensor status | Required | Active/replaced/failed/removed | Supports long-term traceability. |

## Monitoring time-series register
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Series ID | Required | MS-L01-001 | Identifies the whole time-series dataset. |
| Location ID | Required | L-01 | Links the time series to the monitored risk location. |
| Reference location ID | Optional | L-05 | Links the time series to a baseline/reference location where relevant. |
| Installation ID | Required | INST-L01-01 | Links the time series to the sensor installation. |
| Sensor ID | Required | MC-L01-01 | Sensor or channel producing the time series. |
| Observed properties | Required | moisture content; relative humidity; air temperature | Properties contained in the time series. |
| Series start | Required | 2026-08-07T11:00:00.000Z | First timestamp represented in the time series. |
| Series end | Required | 2026-08-07T12:00:00.000Z | Last timestamp represented in the time series. |
| Sampling interval | Required | PT1H | Logging frequency as an ISO 8601 duration. |
| Observation data file | Required | `json_jsonld_implementation/monitoring_timeseries_MS-L01-001.json` | File containing the per-property observations for the time series. In JSON-LD, link this through `hasObservation`. |

## Observation data file
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Measurement ID | Optional | M-L01-MC-20260807T110000000Z | Optional if Sensor ID + Timestamp + Observed Property is used as the unique key. |
| Sensor ID | Required | MC-L01-01 | Sensor or channel producing the observation. |
| Observed property | Required | tmf:property/moisture-content | The property measured by this observation, such as moisture content, relative humidity, or temperature. |
| Timestamp | Required | 2026-08-06T14:40:11.633Z | Date and time of observation. |
| Simple result | Required | 16.2 % | Human-readable SOSA simple result. |
| Result quantity | Required | 16.2 unit:PERCENT | QUDT quantity value containing numeric value and unit reference. |
| Data-quality flag | Optional | Usable/uncertain/invalid | Quality status for this observation, copied or summarized from a validation record where available. |
| Quality assessment record | Optional | VAL-L01-001 | Links the observation to the validation record supporting the quality flag. |
| Raw sensor output | Optional | Resistance value/device output | Retain where available. |
| Sampling interval | Required | PT1H | Logging frequency as an ISO 8601 duration. |

## Validation and quality table
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Validation ID | Required | VAL-L01-001 | Unique validation entry. |
| Installation ID | Optional | INST-L01-01 | Identifies the installation context covered by the validation record. |
| Validation target observation ID(s) | Optional | M-L01-MC-20250626T002555202Z | Observation records assessed by the validation record. In JSON-LD, link these through `validationTargetObservation`. |
| Validation target sensor ID(s) | Optional | MC-L01-01 | Sensor records assessed by the validation record. In JSON-LD, link these through `validationTargetSensor`. |
| Validation target series ID(s) | Optional | MS-L01-001 | Whole monitoring series assessed by the validation record. In JSON-LD, link these through `validationTargetSeries`. |
| Validation performed at | Optional | 2026-08-08T14:40:11.633Z | Time at which the validation assessment was carried out. In JSON-LD, record as `validationPerformedAt`. |
| Validation basis | Optional | Unit consistency; plausibility range; drift review | What the target was checked against. Use this to distinguish observation checks, sensor checks, and whole-series checks. |
| Timestamp or period | Required | 2026-08-07T14:40:11.633Z or 2026-08-06T22:00:00.003Z to 2026-08-08T14:40:11.633Z | Can apply to one reading or a period. |
| Data-quality flag | Required | Usable/uncertain/invalid | Overall quality status. |
| Missing-data flag | Required | No gap detected | Data continuity check. |
| Implausible-value flag | Required | No implausible value detected | Physical/sensor plausibility check. |
| Drift or sensor-damage flag | Required | No drift suspected | Long-term reliability check. |
| Communication flag | Required | Normal transmission | Battery/logging/transmission check. |
| Redundancy agreement | Required where applicable | Shallow and deeper sensors show consistent trend | Comparison with duplicate, paired, or nearby sensors. |
| Quality notes | Optional | Manual verification recommended after leakage report | Additional interpretation note. |
| Validation log | Optional | `json_jsonld_implementation/validation_log_VAL-L01-001.json` | Linked JSON audit log containing target-specific checks for observations, sensors, and whole monitoring series. In JSON-LD, link this through `hasValidationLog`. |

## Moisture-related lifecycle event register
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Event ID | Required | EVT-L01-001 | Unique compact event record. |
| Location ID | Required | L-01 | Links event record to risk location. |
| Affected sensor ID(s) | Optional | MC-L01-01 | Sensor records associated with the event record. |
| Event monitoring series ID(s) | Optional | MS-L01-001 | Monitoring series used by the event log. In JSON-LD, link this through `eventMonitoringSeries`. |
| Event validation record ID(s) | Optional | VAL-L01-001 | Validation records used by the event log. In JSON-LD, link this through `eventValidationRecord`. |
| Event log | Required where event details are retained | `json_jsonld_implementation/event_log_EVT-L01-001.json` | Linked JSON file containing event type, time period, moisture interpretation, event timeline, inspection, action, and outcome entries. In JSON-LD, link this through `hasEventLog`. |

## Event log file
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Event type | Required | moisture-threshold-exceedance; leakage-detected; inspection | Event category or categories. |
| Event period | Required where known | Start: 2026-08-07T10:00:00.000Z; End: 2026-08-09T16:00:00.000Z | Time period of the interpreted moisture condition, reported event, intervention, or combined lifecycle event. |
| Evidence observation file URL | Optional | `json_jsonld_implementation/monitoring_timeseries_MS-L01-001.json` | Observations or linked observation file used as event evidence. |
| Threshold exceedance | Optional | MC above project-defined threshold | Thresholds are interpretation triggers, not standalone criteria. |
| Exceedance duration | Optional | 54 hours | Duration above threshold. |
| Moisture dose | Optional | Repeated short exceedances | Use only where a dose metric is defined. |
| Drying behaviour | Optional | Delayed drying | Interpreted drying response. |
| Anomaly indicator | Optional | Localised anomaly compared with L-05 reference | Helps distinguish local wetting from background behaviour. |
| Confidence or uncertainty | Optional | Medium confidence due to complete data but limited redundancy | Interprets reliability of the event interpretation. |
| Event entries | Required where a timeline is retained | threshold exceedance; leakage detected; inspection; decision recorded | Chronological event log entries with timestamps, entry types, and descriptions. |
| Outcome | Optional | Continued monitoring recommended | Decision or outcome. |

## Lifecycle integration register
| Field | Required/optional | Example entry | Notes |
|---|---|---|---|
| Integration ID | Required | LINK-L01-001 | Unique link record. |
| Location ID | Required | L-01 | Links digital system to monitored location. |
| Element ID | Required | CLT-FP-01 | Links to timber element or BIM object. |
| Linked sensor ID(s) | Optional | MC-L01-01; MC-L01-02 | Sensor records retained in the lifecycle information system. |
| Linked monitoring series ID(s) | Optional | MS-L01-001 | Whole time-series records retained in the lifecycle information system. |
| Linked observation ID(s) | Optional | M-L01-MC-20260807T110000000Z; M-L01-RH-20260807T110000000Z | Observation records retained in the lifecycle information system. |
| Linked validation record ID(s) | Optional | VAL-L01-001 | Validation records retained in the lifecycle information system. |
| Linked event ID | Optional | EVT-L01-001 | Moisture-related event retained in the lifecycle information system. |
| Generated-by lifecycle event ID | Optional | EVT-L01-001 | Event record that generated or motivated the integration record. |
| Linked lifecycle information system | Optional | BIM model / product passport | System where the record is stored or referenced. |
| Digital object reference | Optional | BIM object CLT-FP-01 | Object or database reference. |
| Decision use | Required | Maintenance, post-event assessment, future reuse-related assessment | Explains why the record is retained. |
| Notes | Optional | Selected event indicators retained for future recovery assessment | Additional lifecycle context. |
## Notes for use

- Keep the `Location ID` consistent across the risk-location classification, sensor-deployment, and monitoring-record schema files.
- Record both measured values and contextual metadata. A moisture reading without sensor depth, location, calibration basis, and data-quality information may be difficult to interpret later.
- Treat MC thresholds as interpretation triggers rather than standalone decision criteria.
- Preserve validation flags and uncertainty information, especially where the record may support later maintenance, repair, post-event assessment, durability evaluation, or reuse-related assessment.
