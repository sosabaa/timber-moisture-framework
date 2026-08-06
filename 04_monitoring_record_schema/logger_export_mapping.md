# Logger export mapping example

This example shows how a simple logger export can be mapped into the compacted JSON-LD monitoring-record model. A raw logger row may contain several measured values, but the JSON-LD graph represents each measured property as its own `sosa:Observation`.

## Files

- `logger_export_mapping_example.csv` contains two hourly logger rows from one sensor channel.
- `monitoring_record_schema_example.jsonld` shows the linked graph that receives the generated observation records.
- `monitoring_record_schema.schema.json` provides a validation target for compacted JSON-LD records.

## Mapping pattern

Each CSV row is retained as a source logger record and expanded into one observation per property:

- `logger_mc_percent` becomes an MC observation with `observedProperty` set to `tmf:property/moisture-content`.
- `logger_rh_percent` becomes an RH observation with `observedProperty` set to `tmf:property/relative-humidity`.
- `logger_temperature_c` becomes a temperature observation with `observedProperty` set to `tmf:property/air-temperature`.

The generated observations share the same sensor, installation, location, timestamp, source record ID, and sampling interval. Each observation uses `madeBySensor` for the SOSA sensor link and carries both a simple SOSA result string and a QUDT `QuantityValue` with an explicit unit reference.

## Column mapping

| CSV column | JSON-LD field | Notes |
| --- | --- | --- |
| `logger_timestamp` | `timestamp` | Result time for each generated `sosa:Observation`. Use an ISO 8601 date-time with timezone. |
| `sensor_channel` | Logger-specific metadata | Retain in platform metadata or `rawSensorOutput` where useful. |
| `logger_mc_percent` | `resultQuantity.numericValue` | Used for the MC observation. Unit is `unit:PERCENT`. |
| `logger_temperature_c` | `resultQuantity.numericValue` | Used for the temperature observation. Unit is `unit:DEG_C`. |
| `logger_rh_percent` | `resultQuantity.numericValue` | Used for the RH observation. Unit is `unit:PERCENT`. |
| `data_quality_flag` | `dataQualityFlag` | Used on the generated observation when row-level quality is available and summarized in a separate `ValidationRecord` where a fuller quality check is retained. |
| `location_id` | `location` | Expanded as `tmf:location/{location_id}`. |
| `installation_id` | `installation` | Expanded as `tmf:installation/{installation_id}`. |
| `sensor_id` | `madeBySensor` | Expanded as `tmf:sensor/{sensor_id}` for generated observations. The installation record uses the same sensor ID as `deployedSystem`. |
| `source_record_id` | `sourceRecordId` | Preserves the original logger-row identifier shared by the generated observations. |
| `jsonld_mc_observation_id` | `id` and `measurementId` | Identifier for the generated MC observation. |
| `jsonld_rh_observation_id` | `id` and `measurementId` | Identifier for the generated RH observation. |
| `jsonld_temperature_observation_id` | `id` and `measurementId` | Identifier for the generated temperature observation. |
| `jsonld_mc_property` | `observedProperty` | Observable property for MC. |
| `jsonld_rh_property` | `observedProperty` | Observable property for RH. |
| `jsonld_temperature_property` | `observedProperty` | Observable property for temperature. |
| `jsonld_samplingInterval` | `samplingInterval` | ISO 8601 duration such as `PT1H`. |

## Minimal mapped JSON-LD observations

The first CSV row maps to three observation nodes like this:

```json
[
  {
    "id": "tmf:observation/M-L01-000001-MC",
    "type": ["MeasurementRecord", "Observation"],
    "measurementId": "M-L01-000001-MC",
    "sourceRecordId": "M-L01-000001",
    "madeBySensor": "tmf:sensor/MC-L01-01",
    "installation": "tmf:installation/INST-L01-01",
    "location": "tmf:location/L-01",
    "observedProperty": "tmf:property/moisture-content",
    "timestamp": "2026-08-07T13:00:00.000+02:00",
    "hasSimpleResult": "16.2 %",
    "resultQuantity": {
      "type": "QuantityValue",
      "numericValue": 16.2,
      "unitRef": "unit:PERCENT"
    },
    "samplingInterval": "PT1H"
  },
  {
    "id": "tmf:observation/M-L01-000001-RH",
    "type": ["MeasurementRecord", "Observation"],
    "measurementId": "M-L01-000001-RH",
    "sourceRecordId": "M-L01-000001",
    "madeBySensor": "tmf:sensor/MC-L01-01",
    "installation": "tmf:installation/INST-L01-01",
    "location": "tmf:location/L-01",
    "observedProperty": "tmf:property/relative-humidity",
    "timestamp": "2026-08-07T13:00:00.000+02:00",
    "hasSimpleResult": "62.0 %",
    "resultQuantity": {
      "type": "QuantityValue",
      "numericValue": 62.0,
      "unitRef": "unit:PERCENT"
    },
    "samplingInterval": "PT1H"
  },
  {
    "id": "tmf:observation/M-L01-000001-T",
    "type": ["MeasurementRecord", "Observation"],
    "measurementId": "M-L01-000001-T",
    "sourceRecordId": "M-L01-000001",
    "madeBySensor": "tmf:sensor/MC-L01-01",
    "installation": "tmf:installation/INST-L01-01",
    "location": "tmf:location/L-01",
    "observedProperty": "tmf:property/air-temperature",
    "timestamp": "2026-08-07T13:00:00.000+02:00",
    "hasSimpleResult": "21.4 degC",
    "resultQuantity": {
      "type": "QuantityValue",
      "numericValue": 21.4,
      "unitRef": "unit:DEG_C"
    },
    "samplingInterval": "PT1H"
  }
]
```

Static `Location`, `Sensor`, `SensorInstallation`, and `ObservableProperty` nodes should be stored once and linked from each observation by persistent IDs. Validation outcomes such as missing data, drift, implausible values, and communication gaps should be stored as separate `ValidationRecord` nodes. Sensors can link to the relevant validation record using `sensorValidationRecord`, while observations can carry `dataQualityFlag` and link to the supporting record using `qualityAssessmentRecord`.
