# Sensor deployment template

This template supports Layer 3 of the framework: sensor deployment. It translates the risk-location classification into practical sensor implementation decisions.

The primary sensor type in this framework is a wood moisture-content sensor, since MC is the measured material response most directly linked to timber moisture exposure and durability. RH and temperature sensors are treated as supporting measurements that provide environmental context for interpreting MC variation, drying behaviour, and potential mould or decay risk.

## Field definitions

| Field | Explanation |
|---|---|
| Location ID | Identifier carried over from the risk-location classification table. |
| Risk class | Risk class assigned during moisture-risk classification, such as low, medium, high, critical, or reference. |
| Monitoring objective | Intended purpose of monitoring at this location, such as maintenance, post-event assessment, drying verification, repair decision support, or future reuse-related evidence. |
| Primary sensor type | Main sensor type used at the location. In this framework, this will normally be a wood moisture-content sensor. |
| Supporting sensor type | Additional sensor type used to provide context, normally RH and temperature. |
| Sensor placement | Practical description of where the sensor should be installed relative to the risk location, assembly, joint, edge, fastener, or reference area. |
| Measurement depth | Whether measurements should be shallow, deep, or at multiple depths. |
| Sensor density | Indicative level of sensor density, such as single point, representative sensor group, local sensor group, or redundant sensor group. |
| Redundancy approach | Whether duplicate MC measurements, paired depths, nearby reference measurements, or manual verification are needed. |
| Reference strategy | How the location will be compared with a reference sensor or lower-risk baseline location. |
| Protection and access | Practical requirements for protecting sensors, cables, junction boxes, or access points during installation and operation. |
| Validation approach | Checks needed to confirm whether the data remain usable, such as data-gap flags, drift checks, RH/T consistency checks, redundancy comparison, or manual verification. |
| Metadata to record | Contextual information that must be retained so the sensor readings remain interpretable later. |
| Implementation note | Brief explanation of why this deployment approach is appropriate for the location. |

## Sensor deployment table

| Location ID | Risk class | Monitoring objective | Primary sensor type | Supporting sensor type | Sensor placement | Measurement depth | Sensor density | Redundancy approach | Reference strategy | Protection and access | Validation approach | Metadata to record | Implementation note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L-01 |  |  | MC sensor | RH/T sensor |  |  |  |  |  |  |  |  |  |
| L-02 |  |  | MC sensor | RH/T sensor |  |  |  |  |  |  |  |  |  |
| L-03 |  |  | MC sensor | RH/T sensor |  |  |  |  |  |  |  |  |  |
