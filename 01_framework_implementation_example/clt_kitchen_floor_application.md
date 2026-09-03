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
  <td rowspan="4">Moisture risk mapping</td>
  <td>Risk location</td>
  <td>Kitchen floor panels below appliance and plumbing zones, including refrigerator, sink/dishwasher area, inter-panel junctions, fasteners, and floor–wall junctions.</td>
</tr>
<tr>
  <td>Moisture source or mechanism</td>
  <td>Leakage from plumbing or appliances, repeated small leaks, cleaning water, condensation, moisture migration along panel junctions, and trapped moisture beneath finishes or cabinetry.</td>
</tr>
<tr>
  <td>Moisture-risk classification</td>
  <td>Exposure and vulnerability are assessed separately and combined to assign a Low, Medium, or High moisture-risk class.</td>
</tr>
<tr>
  <td>Monitoring priority</td>
  <td>The moisture-risk class is considered together with inspection limitation, sensor failure risk, and decision relevance to assign a Low, Medium, High, or Critical monitoring priority.</td>
</tr>

<tr>
  <td rowspan="3">Sensor deployment</td>
  <td>Sensor strategy</td>
  <td>Local sensor groups at refrigerator–junction–fastener zone, sink/dishwasher zone, selected floor–wall junctions, and one or more reference locations.</td>
</tr>
<tr>
  <td>Sensor density and redundancy</td>
  <td>Sensor density, redundancy, measurement depth, and validation effort respond primarily to monitoring priority while remaining consistent with the underlying moisture-risk mechanism.</td>
</tr>
<tr>
  <td>Measurement depth</td>
  <td>Shallow MC measurements for surface wetting, with deeper measurements at junctions, fastener zones, and possible moisture migration paths.</td>
</tr>

<tr>
  <td rowspan="2">Data and metadata capture</td>
  <td>Monitoring variables</td>
  <td>MC, RH, temperature, and relevant moisture-event context, such as room conditions, leakage events, appliance replacement, plumbing works, and maintenance records.</td>
</tr>
<tr>
  <td>Metadata</td>
  <td>Floor panel ID, BIM element ID, room function, appliance and plumbing locations, junction and fastener details, sensor position, measurement depth, installation date, moisture-risk class, monitoring priority, and data-quality flags.</td>
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
  <td>Inspect if MC remains above a project-defined threshold, drying is delayed, or redundant sensors show repeated anomalies in higher-priority monitoring locations.</td>
</tr>

<tr>
  <td>Lifecycle integration</td>
  <td></td>
  <td>Link moisture-event history, interpreted indicators, metadata, and quality flags to the relevant BIM element or panel/junction record, with selected lifecycle information referenced in a building logbook, product passport, or other lifecycle information system.</td>
</tr>

  </tbody>
</table>

## Risk-location classification implementation

The first implementation step is to identify candidate moisture-risk locations in the CLT kitchen-floor system and classify them using the criteria in the risk-location classification template. The reusable template is available in [`02_risk_location_classification/risk_location_classification_template.md`](../02_risk_location_classification/risk_location_classification_template.md).

The implementation separates **physical moisture risk** from **monitoring priority**. First, the moisture source and pathway are described and the location is assessed in terms of exposure and vulnerability. These are combined to assign the moisture-risk class. Second, the moisture-risk class is considered together with inspection limitation, sensor failure risk, and decision relevance to assign the monitoring priority. This allows locations with similar physical moisture risk to receive different monitoring responses where observability or decision importance differs.

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
| Moisture source | Plumbing leakage, dishwasher leakage or failure, repeated small leaks, and cleaning water. |
| Moisture pathway/mechanism | Liquid water may enter beneath cabinetry or finishes and migrate towards panel surfaces, edges, junctions, or fastener zones, where drying may be restricted. |
| Exposure likelihood | High. |
| Exposure frequency/duration | Medium. Leakage is not continuous under normal operation, but repeated or prolonged events are credible. |
| Environmental moisture severity | Medium. The kitchen is normally an indoor environment, but local wetting and periods of elevated moisture can occur. |
| Exposure class | High. |
| Moisture uptake/retention potential | High. Panel edges, junctions, fastener zones, and concealed interfaces can absorb or retain localised moisture. |
| Drying limitation | High. Cabinetry, finishes, interfaces, and limited air movement may strongly restrict drying. |
| Consequence | High. Prolonged or concealed wetting may affect durability, repair scope, maintenance decisions, and later reuse-related assessment. |
| Vulnerability class | High. |
| Moisture-risk class | High. |
| Inspection limitation | High. The condition may be concealed beneath cabinetry or finishes and may require targeted opening for direct inspection. |
| Sensor failure risk | Medium. Sensors can be protected, but appliance movement, cleaning water, cabling, and restricted access create reliability concerns. |
| Decision relevance | High. Data may support leakage assessment, targeted opening, repair, drying verification, and future reuse-related assessment. |
| Monitoring priority | Critical. |
| Monitoring reliability concern | Moisture may be localised and concealed; drying may be delayed; single-point readings may miss wetting near plumbing, junctions, or panel edges. |
| Suggested monitoring response | Local MC sensor group with shallow and deeper measurements, RH/T context, redundancy at selected points, reference comparison, and manual or independent verification after suspected leakage where feasible. |
| Justification | High exposure and high vulnerability produce a High moisture-risk class. High inspection limitation and high decision relevance then elevate the location to Critical monitoring priority, justifying redundancy, depth variation, contextual measurements, and stronger validation. |

#### L-02: Refrigerator area near appliance base and adjacent panel/junction zone

| Field | Entry |
|---|---|
| Lifecycle context | Operational monitoring for maintenance and post-event assessment. |
| Building zone | Kitchen. |
| Assembly/detail | CLT floor below refrigerator area. |
| Element/material feature | Panel surface, local appliance support area, nearby junctions or fastening points. |
| Moisture source | Condensate, appliance leakage, cleaning water, or local wetting around the appliance base. |
| Moisture pathway/mechanism | Intermittent liquid water or condensate may wet the floor surface beneath or adjacent to the appliance and migrate towards a nearby joint or concealed region. |
| Exposure likelihood | Medium. |
| Exposure frequency/duration | Medium. Wetting is expected to be occasional rather than persistent. |
| Environmental moisture severity | Medium. The local environment can experience intermittent elevated moisture while remaining generally indoor and controlled. |
| Exposure class | Medium. |
| Moisture uptake/retention potential | Medium. Local moisture may enter the panel surface or nearby joint, depending on detailing and finishes. |
| Drying limitation | Medium. Drying may be partly restricted beneath the appliance or floor finish. |
| Consequence | Medium. Local wetting may require maintenance or event assessment but is generally less consequential than the sink/dishwasher zone. |
| Vulnerability class | Medium. |
| Moisture-risk class | Medium. |
| Inspection limitation | Medium. The appliance restricts direct access, but inspection is possible after moving or servicing it. |
| Sensor failure risk | Medium. Appliance movement, vibration, cleaning water, and access constraints may affect long-term sensor reliability. |
| Decision relevance | Medium. Data may support maintenance and post-event assessment. |
| Monitoring priority | Medium. |
| Monitoring reliability concern | Wetting may be intermittent and partly hidden beneath the appliance; sensor access may be affected by appliance position or replacement. |
| Suggested monitoring response | Representative MC measurement or small sensor group near the appliance/junction zone, RH/T context where feasible, and comparison with the reference location. |
| Justification | Medium exposure and Medium vulnerability produce a Medium moisture-risk class. Moderate inspection limitation, sensor failure risk, and decision relevance support a Medium monitoring priority. |

#### L-03: CLT floor panel-to-panel edge joint within the kitchen floor

| Field | Entry |
|---|---|
| Lifecycle context | Operational monitoring for maintenance, post-event assessment, and future reuse-related evidence. |
| Building zone | Kitchen. |
| Assembly/detail | Floor panel-to-panel edge joint. |
| Element/material feature | Panel edge, fasteners, joint interface, possible moisture path between panels. |
| Moisture source | Leakage or cleaning water originating from nearby appliance or plumbing zones. |
| Moisture pathway/mechanism | Water may migrate along the panel joint or fastening interface, enter panel edges or fastener zones, and remain concealed where drying is restricted. |
| Exposure likelihood | Medium. |
| Exposure frequency/duration | Medium. Exposure depends on wetting occurring elsewhere and reaching the joint. |
| Environmental moisture severity | Medium. The surrounding kitchen environment is normally controlled, but local joint wetting can occur. |
| Exposure class | Medium. |
| Moisture uptake/retention potential | High. Panel edges, joint interfaces, and fastening pockets can promote local uptake, redistribution, or retention. |
| Drying limitation | High. Moisture at concealed interfaces or fastening zones may have restricted drying paths. |
| Consequence | High. The condition of panel edges and connections may influence repair, durability, and future reuse-related assessment. |
| Vulnerability class | High. |
| Moisture-risk class | High. |
| Inspection limitation | High. Joint and fastening conditions may be concealed after completion and difficult to verify without opening finishes or the assembly. |
| Sensor failure risk | Medium. Sensors can be installed and protected, but joint geometry, finishes, cabling, and long-term access create reliability concerns. |
| Decision relevance | High. The record may support post-event assessment, repair decisions, and later evaluation of the panel or connection for reuse. |
| Monitoring priority | Critical. |
| Monitoring reliability concern | Joint behaviour may differ from panel-field behaviour; concealed fasteners and panel edges may retain moisture; local material variability may affect readings. |
| Suggested monitoring response | MC measurements at or near panel edge or fastener zone, shallow and deeper measurements where feasible, redundancy at selected points, and nearby reference comparison. |
| Justification | Medium exposure combined with High vulnerability produces a High moisture-risk class. High inspection limitation and High decision relevance elevate the joint to Critical monitoring priority. |

#### L-04: Floor-wall joint near kitchen perimeter

| Field | Entry |
|---|---|
| Lifecycle context | Operational monitoring for maintenance and post-event assessment. |
| Building zone | Kitchen. |
| Assembly/detail | Floor-wall joint. |
| Element/material feature | CLT panel edge, wall interface, possible skirting or finish-covered edge. |
| Moisture source | Cleaning water, migrated leakage from nearby appliance or plumbing zones, or local condensation. |
| Moisture pathway/mechanism | Water may migrate towards the floor-wall interface and enter the CLT panel edge or remain behind skirting and finishes where drying is restricted. |
| Exposure likelihood | Medium. |
| Exposure frequency/duration | Medium. Local wetting is plausible but is not expected to be continuous under normal operation. |
| Environmental moisture severity | Medium. The general indoor environment is controlled, but the interface may experience local moisture accumulation. |
| Exposure class | Medium. |
| Moisture uptake/retention potential | High. Panel edges and concealed interfaces can absorb and retain moisture. |
| Drying limitation | High. Skirting, finishes, wall build-up, and limited air movement may restrict drying. |
| Consequence | Medium. Local deterioration or repair may occur, but the generic floor-wall junction is less decision-critical than the inter-panel fastening zone. |
| Vulnerability class | High. |
| Moisture-risk class | High. |
| Inspection limitation | High. Moisture may be concealed behind skirting or finishes and direct inspection may require opening. |
| Sensor failure risk | Medium. Sensors can be protected, but concealed installation and limited later access create some reliability concern. |
| Decision relevance | Medium. Data may support maintenance, inspection, and post-event assessment. |
| Monitoring priority | High. |
| Monitoring reliability concern | Moisture may remain concealed behind finishes; access after completion may be limited; drying may depend strongly on the floor-wall build-up. |
| Suggested monitoring response | Selected MC measurement or small local group at the floor-wall junction, depth variation where justified, RH/T context where relevant, and comparison with nearby risk-zone and reference measurements. |
| Justification | Medium exposure and High vulnerability produce a High moisture-risk class. High inspection limitation but Medium decision relevance support a High, rather than Critical, monitoring priority. |

#### L-05: Reference floor area away from appliance, plumbing, and junction risk zones

| Field | Entry |
|---|---|
| Lifecycle context | Operational reference monitoring. |
| Building zone | Kitchen. |
| Assembly/detail | Open CLT floor area outside main moisture-risk zones. |
| Element/material feature | Panel field away from appliances, plumbing, and junction concentrations. |
| Moisture source | General indoor-climate moisture and seasonal RH variation. |
| Moisture pathway/mechanism | Background hygroscopic moisture exchange between the indoor air and the accessible panel field. |
| Exposure likelihood | Low. |
| Exposure frequency/duration | Low. No recurring liquid-water source is expected at the selected reference location. |
| Environmental moisture severity | Low. The location represents normal indoor conditions. |
| Exposure class | Low. |
| Moisture uptake/retention potential | Low. The selected panel field is away from concentrated moisture-entry paths and retention-prone details. |
| Drying limitation | Low. The reference location is selected to have relatively open and reliable drying conditions. |
| Consequence | Low. Background moisture variation at this location has limited direct consequence. |
| Vulnerability class | Low. |
| Moisture-risk class | Low. |
| Inspection limitation | Low. The reference location should be readily interpretable and, where feasible, accessible for verification. |
| Sensor failure risk | Low. The location should be selected so the sensor can remain protected and stable. |
| Decision relevance | Medium. Although the physical risk is low, the data provide an important baseline for interpreting the higher-risk locations. |
| Monitoring priority | Low. |
| Monitoring reliability concern | Reference data do not represent local wetting but are needed to distinguish risk-zone behaviour from general indoor-climate effects. |
| Suggested monitoring response | One reference MC measurement, supported by RH/T context where feasible. |
| Justification | Low exposure and Low vulnerability produce a Low moisture-risk class. The location remains useful as a reference, but low inspection limitation and low sensor failure risk mean that intensive monitoring is not required. |
</details>

## Sensor deployment

The second implementation step is to translate the classified locations into practical sensor-deployment decisions. The reusable sensor-deployment template is located at [`03_sensor_deployment/sensor_deployment_template.md`](../03_sensor_deployment/sensor_deployment_template.md).

Both **moisture-risk class** and **monitoring priority** are carried forward from Layer 2. Moisture-risk class records the physical moisture concern, while monitoring priority is used more directly to guide sensor density, depth variation, redundancy, protection, and validation effort.

### Sensor deployment: CLT kitchen-floor example
<details>
<summary>Show completed sensor deployment example</summary>

### L-01: Sink/dishwasher zone below plumbing and appliance connections

| Field | Entry |
|---|---|
| Moisture-risk class | High. |
| Monitoring priority | Critical. |
| Monitoring objective | Operational monitoring for maintenance, leakage/post-event assessment, and future reuse-related evidence. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor for local environmental context. |
| Sensor placement | Local sensor group below or close to the sink/dishwasher plumbing and appliance connection zone, with points near likely leakage paths, nearby panel edges, junctions, or fastener areas where relevant. |
| Measurement depth | Shallow MC measurements for surface wetting, with deeper MC measurements where moisture may migrate into the CLT panel, joint, or concealed zone. |
| Sensor density | Local sensor group with more than one MC measurement point around the sink/dishwasher zone. The exact number should depend on plumbing layout, appliance position, nearby panel joints, access conditions, and monitoring objective. |
| Redundancy approach | Redundant MC measurements at selected points; paired shallow and deeper measurements where feasible. |
| Reference strategy | Compare with the reference floor area L-05 to distinguish local leakage or delayed drying from general indoor-climate behaviour. |
| Protection and access | Protect sensors, cables, and connectors from cleaning water, appliance movement, and maintenance disturbance. Access should be retained through cabinetry or service openings where feasible. |
| Validation approach | Data-gap checks, abrupt-change checks, redundancy comparison, RH/T consistency checks, and manual or independent verification after suspected leakage or maintenance events where feasible. |
| Metadata to record | Sensor ID, location ID, moisture-risk class, monitoring priority, appliance/plumbing relationship, installation date, sensor type, measurement depth, panel/junction relationship, protection measures, maintenance events, and data-quality flags. |
| Implementation note | Critical monitoring priority reflects the combination of High physical moisture risk, concealed observation conditions, and strong decision relevance. |

### L-02: Refrigerator area near appliance base and adjacent panel/junction zone

| Field | Entry |
|---|---|
| Moisture-risk class | Medium. |
| Monitoring priority | Medium. |
| Monitoring objective | Operational monitoring for maintenance and post-event assessment. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor where feasible. |
| Sensor placement | Representative MC measurement near the refrigerator base, especially close to possible appliance leakage, condensate, or adjacent panel/junction zones. |
| Measurement depth | Primarily shallow MC measurement; deeper measurement may be added where the floor build-up or joint position suggests possible moisture retention. |
| Sensor density | Representative sensor point or small sensor group, depending on appliance position and access. |
| Redundancy approach | Redundancy is optional; use an additional measurement where access is poor, appliance-related leakage risk is elevated, or data are needed for later assessment. |
| Reference strategy | Compare with L-05 reference floor area and, where relevant, with higher-risk kitchen locations such as L-01. |
| Protection and access | Sensors should be protected from appliance movement, vibration, cleaning water, and accidental disturbance during appliance replacement. |
| Validation approach | Data-gap checks, trend checks, RH/T consistency checks, and review after appliance replacement or suspected leakage. |
| Metadata to record | Sensor ID, location ID, moisture-risk class, monitoring priority, appliance position, installation date, sensor type, measurement depth, access condition, appliance replacement events, and data-quality flags. |
| Implementation note | Medium monitoring priority supports a representative monitoring approach rather than the redundancy used at Critical locations. |

### L-03: Fastened CLT floor panel-to-panel edge joint

| Field | Entry |
|---|---|
| Moisture-risk class | High. |
| Monitoring priority | Critical. |
| Monitoring objective | Operational monitoring for maintenance, post-event assessment, and future reuse-related evidence. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor for local context where feasible. |
| Sensor placement | MC measurements at or near the CLT panel edge, joint interface, fastener zone, or fastening pocket, especially where leakage from appliance zones may migrate along the joint. |
| Measurement depth | Shallow and deeper MC measurements where feasible, with attention to the panel edge and possible moisture path between adjacent panels. |
| Sensor density | Local sensor group at the joint, with higher density where the joint is concealed, fastened, or important for later assessment. |
| Redundancy approach | Redundant MC measurements or paired-depth measurements are recommended where the joint condition may influence repair or reuse-related assessment. |
| Reference strategy | Compare with L-05 reference floor area and with nearby appliance-zone sensors, especially L-01 if leakage migration is possible. |
| Protection and access | Protect cables and connectors at the joint from construction disturbance, floor finishing, cleaning water, and later maintenance activities. |
| Validation approach | Redundancy comparison, drift checks, data-gap checks, abrupt-change checks, and comparison with nearby panel-field or reference measurements. |
| Metadata to record | Sensor ID, location ID, moisture-risk class, monitoring priority, joint type, panel IDs, fastener or fastening-pocket details, measurement depth, installation date, access condition, and data-quality flags. |
| Implementation note | Critical monitoring priority reflects the combination of High vulnerability, concealed joint conditions, and high decision relevance for repair and future reuse assessment. |

### L-04: Floor-wall junction near kitchen perimeter

| Field | Entry |
|---|---|
| Moisture-risk class | High. |
| Monitoring priority | High. |
| Monitoring objective | Operational monitoring for maintenance and post-event assessment. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor where relevant. |
| Sensor placement | Selected MC measurement at the CLT floor-wall junction, preferably near concealed panel edges, skirting, finishes, or likely water-migration paths. |
| Measurement depth | Shallow MC measurement at the junction, with deeper measurement where moisture may be trapped behind finishes or migrate into the panel edge. |
| Sensor density | Selected sensor point or small local group, depending on perimeter length, access, and proximity to appliance or plumbing zones. |
| Redundancy approach | Redundancy may be used where the junction is particularly difficult to inspect, close to a higher-risk wetting source, or important for later decisions. |
| Reference strategy | Compare with L-05 and nearby risk-zone sensors to distinguish local junction wetting from general indoor-climate variation. |
| Protection and access | Sensors and cable routes should be protected behind finishes or skirting, with access retained where feasible for inspection or replacement. |
| Validation approach | Data-gap checks, delayed-drying checks, RH/T consistency checks, and comparison with nearby reference or appliance-zone measurements. |
| Metadata to record | Sensor ID, location ID, moisture-risk class, monitoring priority, floor-wall junction description, finish/skirting condition, measurement depth, installation date, access condition, and data-quality flags. |
| Implementation note | High monitoring priority reflects High physical moisture risk and poor observability, but only Medium decision relevance in this generic example. |

### L-05: Reference floor area away from appliance, plumbing, and junction risk zones

| Field | Entry |
|---|---|
| Moisture-risk class | Low. |
| Monitoring priority | Low. |
| Monitoring objective | Operational reference monitoring. |
| Primary sensor type | Wood moisture-content sensor. |
| Supporting sensor type | RH/T sensor for indoor environmental context. |
| Sensor placement | Open CLT floor area away from appliance, plumbing, panel-junction, and floor-wall risk zones. |
| Measurement depth | Representative MC measurement depth, selected to provide baseline comparison with the risk-zone measurements. |
| Sensor density | Single reference point or small reference group, depending on the size of the kitchen floor and monitoring objective. |
| Redundancy approach | Redundancy is generally not required unless the reference location itself is used for consequential long-term decision support. |
| Reference strategy | Serves as the baseline location for interpreting L-01 to L-04. |
| Protection and access | Sensor should be placed where it is unlikely to be damaged by use, finishes, maintenance, or furniture movement. |
| Validation approach | Data-gap checks, trend checks, RH/T consistency checks, and comparison with expected indoor-climate behaviour. |
| Metadata to record | Sensor ID, location ID, moisture-risk class, monitoring priority, reference-location description, installation date, sensor type, measurement depth, access condition, and data-quality flags. |
| Implementation note | The reference location remains useful for interpretation even though its physical moisture risk and monitoring priority are both Low. |
</details>

## Monitoring-record schema implementation

The final implementation step is to structure the sensor readings and contextual information so that the monitoring record remains interpretable over time. The reusable monitoring-record schema template is located at [`04_monitoring_record_schema/monitoring_record_schema_template.md`](../04_monitoring_record_schema/monitoring_record_schema_template.md).

For the CLT kitchen-floor example, the monitoring record should retain the link between each location ID, moisture-risk class, monitoring priority, installed sensor, CLT panel or junction, measurement depth, measured values, validation flags, moisture-event indicators, and lifecycle decision context. This ensures that later users can interpret whether a recorded moisture event represents localised wetting, delayed drying, repeated moisture exposure, background indoor-climate behaviour, or uncertain data quality.

## Example interpretation

In this example, the sink/dishwasher zone has a **High moisture-risk class** and **Critical monitoring priority** because leakage may occur near plumbing or appliance connections, drying may be restricted by floor finishes or cabinetry, inspection is limited, and the data may support consequential later decisions. A suitable deployment response may therefore include shallow and deeper moisture-content measurements, RH/T context measurements, redundancy at selected points, and comparison with a reference location outside the immediate appliance zone.

The panel-to-panel edge joint also has High moisture risk and Critical monitoring priority, but for a different reason: its exposure is only Medium, while its vulnerability, inspection limitation, and decision relevance are High. This illustrates why the framework separates physical moisture risk from monitoring priority rather than treating all decision factors as a single risk score.

The resulting record is intended to support maintenance and post-event assessment during use. At future recovery, the same record may provide supporting evidence about whether the CLT panel or junction experienced isolated wetting with verified drying, repeated wetting, prolonged elevated moisture, or uncertain data quality. This information should support, rather than replace, broader reuse assessment involving structural condition, visible damage, connection condition, biological degradation, and deconstruction damage.
