# Illustrative application: CLT kitchen-floor system

This example illustrates how the framework can be applied to a CLT floor system in a kitchen. The example focuses on moisture-risk zones associated with appliances, plumbing, panel junctions, fasteners, and floor-wall junctions. It follows the framework layers from lifecycle objective and moisture-risk mapping through sensor deployment, data capture, validation, interpretation, decision support, and lifecycle integration.

The example is illustrative and should be adapted to project-specific conditions. It does not prescribe sensor numbers, fixed spacing, universal thresholds, or a standard layout.

<table>
  <thead>
    <tr>
      <th>Layer</th>
      <th>Sub-layer</th>
      <th>Application</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lifecycle context</td>
      <td></td>
      <td>Operational monitoring for maintenance, post-event assessment, and future reuse-related evidence.</td>
    </tr>

<tr>
  <td rowspan="3">Moisture risk mapping</td>
  <td>Risk location</td>
  <td>Kitchen floor panels below appliance and plumbing zones, including refrigerator, sink/dishwasher area, inter-panel junctions, fasteners, and floor–wall junctions.</td>
</tr>
<tr>
  <td>Moisture source or mechanism</td>
  <td>Leakage from plumbing or appliances, repeated small leaks, cleaning water, condensation, moisture migration along panel junctions, and trapped moisture beneath finishes or cabinetry.</td>
</tr>
<tr>
  <td>Risk classification</td>
  <td>Leakage risk, restricted drying, concealed access, and possible moisture accumulation near junctions or fasteners.</td>
</tr>

<tr>
  <td rowspan="3">Sensor deployment</td>
  <td>Sensor strategy</td>
  <td>Local sensor groups at refrigerator–junction–fastener zone, sink/dishwasher zone, selected floor–wall junctions, and one or more reference locations.</td>
</tr>
<tr>
  <td>Sensor density and redundancy</td>
  <td>Increased sensor density and redundancy may be justified in the sink/dishwasher zone, with the number of MC measurement points and RH/T sensors determined by panel layout, junctions, access, and project-specific monitoring objectives.</td>
</tr>
<tr>
  <td>Measurement depth</td>
  <td>Shallow MC measurements for surface wetting, with deeper measurements at junctions, fastener zones, and possible moisture migration paths.</td>
</tr>

<tr>
  <td rowspan="2">Data and metadata capture</td>
  <td>Monitoring variables</td>
  <td>MC, RH, temperature, and relevant exposure data, such as room conditions, leakage events, appliance replacement, plumbing works, and maintenance records.</td>
</tr>
<tr>
  <td>Metadata</td>
  <td>Floor panel ID, BIM element ID, room function, appliance and plumbing locations, junction and fastener details, sensor position, measurement depth, installation date, risk class, and data-quality flags.</td>
</tr>

<tr>
  <td>Validation</td>
  <td></td>
  <td>Data-gap flags, drift checks, redundancy comparison, RH/T consistency checks, and comparison with reference locations.</td>
</tr>

<tr>
  <td>Interpretation</td>
  <td></td>
  <td>MC threshold exceedance, wetting duration, delayed drying, surface versus deeper moisture response, repeated anomalies, and risk-zone/reference comparison.</td>
</tr>

<tr>
  <td>Decision support</td>
  <td></td>
  <td>Inspect if MC remains above a project-defined threshold, drying is delayed, or redundant sensors show repeated anomalies in high-risk zones.</td>
</tr>

<tr>
  <td>Lifecycle integration</td>
  <td></td>
  <td>Link exposure history, interpreted indicators, metadata, and quality flags to the relevant BIM element or panel/junction record, with selected lifecycle information referenced in a building logbook, product passport, or other lifecycle information system.</td>
</tr>

  </tbody>
</table>

## Risk-location classification implementation

The first implementation step is to identify candidate moisture-risk locations in the CLT kitchen-floor system and classify them using the criteria in the risk-location classification template. The reusable template is available in [`02_risk_location_classification/risk_location_classification_template.md`](../02_risk_location_classification/risk_location_classification_template.md).

The completed example below shows how the kitchen-floor locations are classified before being translated into sensor-deployment decisions.

### Risk-location classification table: CLT kitchen-floor example
<details>
<summary>Show completed risk-location classification table</summary>

## Risk-location classification table: CLT kitchen-floor example

#### L-01: Sink/dishwasher area below plumbing and appliance connections

| Field | Entry |
|---|---|
| Lifecycle context | Operational monitoring for maintenance, post-event assessment, and future reuse-related evidence. |
| Building zone | Kitchen. |
| Assembly/detail | CLT floor below sink and dishwasher. |
| Element/material feature | Panel surface, possible junctions, local fastener areas, and concealed regions beneath cabinetry or finishes. |
| Moisture source or mechanism | Leakage from plumbing connections, dishwasher failure, repeated small leaks, cleaning water, or trapped moisture beneath finishes. |
| Exposure likelihood | High. |
| Drying capacity | Low/Medium. |
| Inspection access | Low/Medium. |
| Consequence | High. |
| Environmental aggressiveness | Medium/High. |
| Sensor survivability | Medium. |
| Decision relevance | High. |
| Risk class | High. |
| Monitoring reliability concern | Moisture may be localised and concealed; drying may be delayed; single-point readings may miss wetting near plumbing or junctions. |
| Suggested monitoring response | Local MC sensor group with shallow and deeper measurements, RH/T context sensor, redundancy at selected points, and comparison with a reference location. |
| Justification | This location is classified as high risk because leakage may occur near plumbing or appliance connections, drying may be restricted by finishes or cabinetry, and later inspection may require targeted opening. |

#### L-02: Refrigerator area near appliance base and adjacent panel/junction zone

| Field | Entry |
|---|---|
| Lifecycle context | Operational monitoring for maintenance and post-event assessment. |
| Building zone | Kitchen. |
| Assembly/detail | CLT floor below refrigerator area. |
| Element/material feature | Panel surface, local appliance support area, nearby junctions or fastening points. |
| Moisture source or mechanism | Condensate, appliance leakage, cleaning water, or local wetting around appliance base. |
| Exposure likelihood | Medium. |
| Drying capacity | Medium. |
| Inspection access | Medium. |
| Consequence | Medium. |
| Environmental aggressiveness | Medium. |
| Sensor survivability | Medium. |
| Decision relevance | Medium. |
| Risk class | Medium. |
| Monitoring reliability concern | Wetting may be intermittent and hidden beneath the appliance; sensor access may be affected by appliance position. |
| Suggested monitoring response | Representative MC measurement near appliance/junction zone, RH/T context where feasible, and comparison with reference location. |
| Justification | The refrigerator area has possible appliance-related wetting, but the risk is generally lower than the sink/dishwasher zone unless drainage, condensation, or access conditions increase the risk. |

#### L-03: CLT floor panel-to-panel edge joint within the kitchen floor

| Field | Entry |
|---|---|
| Lifecycle context | Operational monitoring for maintenance, post-event assessment, and future reuse-related evidence. |
| Building zone | Kitchen. |
| Assembly/detail | Floor panel-to-panel edge joint. |
| Element/material feature | Panel edge, fasteners, joint interface, possible moisture path between panels. |
| Moisture source or mechanism | Moisture migration along joints, leakage spreading from appliance zones, water accumulation around fasteners, or restricted drying at panel edges. |
| Exposure likelihood | Medium/High. |
| Drying capacity | Low/Medium. |
| Inspection access | Low. |
| Consequence | High. |
| Environmental aggressiveness | Medium. |
| Sensor survivability | Medium/High. |
| Decision relevance | High. |
| Risk class | High. |
| Monitoring reliability concern | Joint behaviour may differ from panel field behaviour; concealed fasteners and panel edges may retain moisture; local material variability may affect readings. |
| Suggested monitoring response | MC measurements at/near panel edge or fastener zone, deeper measurement where feasible, redundancy if used for later assessment, and nearby reference measurement. |
| Justification | CLT panel edges at inter-panel joints are risk locations because moisture may enter, accumulate, or migrate along the joint interface. Fasteners and fastening pockets may create additional local moisture-retention points, and the condition of these edge zones may influence repair decisions and future reuse-related assessment. |

#### L-04: Floor-wall joint near kitchen perimeter

| Field | Entry |
|---|---|
| Lifecycle context | Operational monitoring for maintenance and post-event assessment. |
| Building zone | Kitchen. |
| Assembly/detail | Floor-wall joint. |
| Element/material feature | CLT panel edge, wall interface, possible skirting or finish-covered edge. |
| Moisture source or mechanism | Cleaning water, leakage migration, condensation risk near interface, or trapped moisture behind finishes. |
| Exposure likelihood | Medium. |
| Drying capacity | Low/Medium. |
| Inspection access | Low/Medium. |
| Consequence | Medium/High. |
| Environmental aggressiveness | Medium. |
| Sensor survivability | Medium. |
| Decision relevance | Medium/High. |
| Risk class | Medium/High. |
| Monitoring reliability concern | Moisture may be concealed behind finishes; access after completion may be limited; drying may depend on floor and wall build-up. |
| Suggested monitoring response | Selected MC measurement at floor-wall junction, RH/T context where relevant, and inspection trigger if prolonged wetting or delayed drying is observed. |
| Justification | Floor-wall junctions may have limited drying and reduced inspection access, especially where finishes conceal the CLT edge or where water migrates from nearby appliance zones. |

#### L-05: Reference floor area away from appliance, plumbing, and junction risk zones

| Field | Entry |
|---|---|
| Lifecycle context | Operational reference monitoring. |
| Building zone | Kitchen. |
| Assembly/detail | Open CLT floor area outside main moisture-risk zones. |
| Element/material feature | Panel field away from appliances, plumbing, and junction concentrations. |
| Moisture source or mechanism | General indoor climate influence, seasonal RH variation, or background moisture behaviour. |
| Exposure likelihood | Low. |
| Drying capacity | Medium/High. |
| Inspection access | High. |
| Consequence | Low. |
| Environmental aggressiveness | Low/Medium. |
| Sensor survivability | High. |
| Decision relevance | Medium. |
| Risk class | Low/Reference. |
| Monitoring reliability concern | Reference data may not represent local wetting, but are needed to distinguish risk-zone behaviour from general indoor-climate effects. |
| Suggested monitoring response | One reference MC measurement, supported by RH/T context if feasible. |
| Justification | A reference location helps interpret whether moisture changes at L-01 to L-04 are localised events or part of broader indoor-climate behaviour. |
</details>

## Sensor deployment

The second implementation step is to translate the classified moisture-risk locations into practical sensor-deployment decisions. The reusable sensor-deployment template is located at [`03_sensor_deployment/sensor_deployment_template.md`](../03_sensor_deployment/sensor_deployment_template.md).

The implementation below shows how the L-01 to L-05 locations are carried forward from risk classification into sensor placement, measurement depth, density, redundancy, reference comparison, protection, validation, and metadata requirements.

### Sensor deployment: CLT kitchen-floor example
<details>
<summary>Show completed sensor deployment example</summary>

### L-01: Sink/dishwasher zone below plumbing and appliance connections

| Field | Entry |
|---|---|
| Risk class | High. |
| Monitoring objective | Operational monitoring for maintenance, leakage/post-event assessment, and future reuse-related evidence. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor for local environmental context. |
| Sensor placement | Local sensor group below or close to the sink/dishwasher plumbing and appliance connection zone, with points near likely leakage paths, nearby panel edges, junctions, or fastener areas where relevant. |
| Measurement depth | Shallow MC measurements for surface wetting, with deeper MC measurements where moisture may migrate into the CLT panel, joint, or concealed zone. |
| Sensor density | Local sensor group with more than one MC measurement point around the sink/dishwasher risk zone. The exact number of measurement points should depend on the plumbing layout, appliance position, nearby panel joints, access conditions, and monitoring objective. |
| Redundancy approach | Redundant MC measurements at selected high-risk points; paired shallow and deeper measurements where feasible. |
| Reference strategy | Compare with the reference floor area L-05 to distinguish local leakage or delayed drying from general indoor-climate behaviour. |
| Protection and access | Protect sensors, cables, and connectors from cleaning water, appliance movement, and maintenance disturbance. Access should be retained through cabinetry or service openings where feasible. |
| Validation approach | Data-gap checks, abrupt-change checks, redundancy comparison, RH/T consistency checks, and manual verification after suspected leakage or maintenance events. |
| Metadata to record | Sensor ID, location ID, appliance/plumbing relationship, installation date, sensor type, measurement depth, panel/junction relationship, protection measures, maintenance events, and data-quality flags. |
| Implementation note | This location requires stronger monitoring because leakage may be localised, drying may be restricted by finishes or cabinetry, and later inspection may require targeted opening. |

### L-02: Refrigerator area near appliance base and adjacent panel/junction zone

| Field | Entry |
|---|---|
| Risk class | Medium. |
| Monitoring objective | Operational monitoring for maintenance and post-event assessment. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor where feasible. |
| Sensor placement | Representative MC measurement near the refrigerator base, especially close to possible appliance leakage, condensate, or adjacent panel/junction zones. |
| Measurement depth | Primarily shallow MC measurement; deeper measurement may be added where the floor build-up or joint position suggests possible moisture retention. |
| Sensor density | Representative sensor point or small sensor group, depending on appliance position and access. |
| Redundancy approach | Redundancy is optional; use additional measurement only where access is poor, appliance-related leakage risk is elevated, or data are needed for later assessment. |
| Reference strategy | Compare with L-05 reference floor area and, where relevant, with higher-risk kitchen locations such as L-01. |
| Protection and access | Sensors should be protected from appliance movement, vibration, cleaning water, and accidental disturbance during appliance replacement. |
| Validation approach | Data-gap checks, trend checks, RH/T consistency checks, and review after appliance replacement or suspected leakage. |
| Metadata to record | Sensor ID, location ID, appliance position, installation date, sensor type, measurement depth, access condition, appliance replacement events, and data-quality flags. |
| Implementation note | The refrigerator area is monitored as a medium-risk appliance zone because wetting may be intermittent and partly concealed beneath the appliance. |

### L-03: Fastened CLT floor panel-to-panel edge joint

| Field | Entry |
|---|---|
| Risk class | High. |
| Monitoring objective | Operational monitoring for maintenance, post-event assessment, and future reuse-related evidence. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor for local context where feasible. |
| Sensor placement | MC measurements at or near the CLT panel edge, joint interface, fastener zone, or fastening pocket, especially where leakage from appliance zones may migrate along the joint. |
| Measurement depth | Shallow and deeper MC measurements where feasible, with attention to the panel edge and possible moisture path between adjacent panels. |
| Sensor density | Local sensor group at the joint, with higher density if the joint is concealed, fastened, or important for later assessment. |
| Redundancy approach | Redundant MC measurements or paired depth measurements are recommended where the joint condition may influence repair or reuse-related assessment. |
| Reference strategy | Compare with L-05 reference floor area and with nearby appliance-zone sensors, especially L-01 if leakage migration is possible. |
| Protection and access | Protect cables and connectors at the joint from construction disturbance, floor finishing, cleaning water, and later maintenance activities. |
| Validation approach | Redundancy comparison, drift checks, data-gap checks, abrupt-change checks, and comparison with nearby panel-field or reference measurements. |
| Metadata to record | Sensor ID, location ID, joint type, panel IDs, fastener or fastening-pocket details, measurement depth, installation date, access condition, and data-quality flags. |
| Implementation note | CLT panel edges at inter-panel joints are risk locations because moisture may enter, accumulate, or migrate along the joint interface. Fasteners and fastening pockets may create additional local moisture-retention points. |

### L-04: Floor-wall junction near kitchen perimeter

| Field | Entry |
|---|---|
| Risk class | Medium/High. |
| Monitoring objective | Operational monitoring for maintenance and post-event assessment. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor where relevant. |
| Sensor placement | Selected MC measurement at the CLT floor-wall junction, preferably near concealed panel edges, skirting, finishes, or likely water-migration paths. |
| Measurement depth | Shallow MC measurement at the junction, with deeper measurement where moisture may be trapped behind finishes or migrate into the panel edge. |
| Sensor density | Selected sensor point or small local group, depending on perimeter length, access, and proximity to appliance or plumbing zones. |
| Redundancy approach | Redundancy may be used where the junction is concealed, difficult to inspect, or close to a higher-risk wetting source. |
| Reference strategy | Compare with L-05 and nearby risk-zone sensors to distinguish local junction wetting from general indoor-climate variation. |
| Protection and access | Sensors and cable routes should be protected behind finishes or skirting, with access retained where feasible for inspection or replacement. |
| Validation approach | Data-gap checks, delayed-drying checks, RH/T consistency checks, and comparison with nearby reference or appliance-zone measurements. |
| Metadata to record | Sensor ID, location ID, floor-wall junction description, finish/skirting condition, measurement depth, installation date, access condition, and data-quality flags. |
| Implementation note | This location is monitored because moisture may remain concealed at the panel edge or behind finishes, and drying may depend strongly on the floor-wall build-up. |

### L-05: Reference floor area away from appliance, plumbing, and junction risk zones

| Field | Entry |
|---|---|
| Risk class | Low/Reference. |
| Monitoring objective | Operational reference monitoring. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor for indoor environmental context. |
| Sensor placement | Open CLT floor area away from appliance, plumbing, panel-junction, and floor-wall risk zones. |
| Measurement depth | Representative MC measurement depth, selected to provide baseline comparison with the risk-zone measurements. |
| Sensor density | Single reference point or small reference group, depending on the size of the kitchen floor and monitoring objective. |
| Redundancy approach | Redundancy is generally not required unless the reference location is used for long-term decision support. |
| Reference strategy | Serves as the baseline location for interpreting L-01 to L-04. |
| Protection and access | Sensor should be placed where it is unlikely to be damaged by use, finishes, maintenance, or furniture movement. |
| Validation approach | Data-gap checks, trend checks, RH/T consistency checks, and comparison with expected indoor-climate behaviour. |
| Metadata to record | Sensor ID, location ID, reference-location description, installation date, sensor type, measurement depth, access condition, and data-quality flags. |
| Implementation note | The reference location helps determine whether moisture changes in the risk zones are localised wetting events or part of broader indoor-climate behaviour. |
</details>

## Monitoring-record schema implementation

The final implementation step is to structure the sensor readings and contextual information so that the monitoring record remains interpretable over time. The reusable monitoring-record schema template is located at [`04_monitoring_record_schema/monitoring_record_schema_template.md`](../04_monitoring_record_schema/monitoring_record_schema_template.md).

For the CLT kitchen-floor example, the monitoring record should retain the link between each location ID, installed sensor, CLT panel or junction, measurement depth, measured values, validation flags, exposure indicators, and lifecycle decision context. This ensures that later users can interpret whether a recorded moisture event represents localised wetting, delayed drying, repeated exposure, background indoor-climate behaviour, or uncertain data quality.

## Example interpretation

In this example, the sink/dishwasher zone is treated as a higher-risk location because leakage may occur near plumbing or appliance connections, drying may be restricted by floor finishes or cabinetry, and later inspection may require targeted opening. A suitable deployment response may therefore include shallow and deeper moisture-content measurements, RH/T context measurements, redundancy at selected points, and comparison with a reference location outside the immediate appliance zone.

The resulting record is intended to support maintenance and post-event assessment during use. At future recovery, the same record may provide supporting evidence about whether the CLT panel or junction experienced isolated wetting with verified drying, repeated wetting, prolonged elevated moisture, or uncertain data quality. This information should support, rather than replace, broader reuse assessment involving structural condition, visible damage, connection condition, biological degradation, and deconstruction damage.
