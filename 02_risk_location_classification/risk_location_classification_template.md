# Risk-location classification template

This template supports Layer 2 of the framework: moisture-risk mapping and classification. It is used to identify candidate monitoring locations, classify their **moisture risk**, and then determine their **monitoring priority**.

The implementation separates two questions that should not be conflated:

1. **Moisture risk:** How susceptible is the location to harmful moisture exposure?
2. **Monitoring priority:** Given that risk, how important is continuous or targeted monitoring at the location?

The classification is based on structured engineering judgement. It is not a fixed numerical scoring system. The descriptors and matrices below are intended to improve transparency and repeatability while allowing adaptation to project-specific conditions.

## Classification logic

The classification is carried out in two stages:

**Stage A — Moisture-risk classification**

`Moisture source/mechanism → Exposure → Vulnerability → Moisture risk`

**Stage B — Monitoring-priority classification**

`Moisture risk + Inspection access/observability + Sensor survivability + Decision relevance → Monitoring priority`

This organisation retains the decision factors used in the conceptual framework while distinguishing physical moisture risk from the need and feasibility of monitoring.

---

# Stage A — Moisture-risk classification

## A1. Moisture source and mechanism

Before assigning ratings, describe the moisture scenario that is being assessed. The description should identify, where relevant:

- the **moisture source**, such as leakage, precipitation, construction wetting, cleaning water, condensation, ground moisture, or sustained high RH;
- the **transport pathway**, such as direct wetting, capillary transport, joint/interface migration, vapour transport, or leakage through penetrations;
- the **susceptible location or feature**, such as surface, end grain, panel edge, fastener zone, concealed interface, connection, or deeper internal region; and
- the expected **retention or drying behaviour** after wetting.

The moisture mechanism should be recorded explicitly so that the later classification can be traced back to a physical scenario rather than to a rating alone.

## A2. Exposure classification

Exposure describes the likelihood and severity of moisture reaching the assessed location.

| Exposure criterion | Low | Medium | High |
|---|---|---|---|
| Exposure likelihood | Moisture exposure is unlikely under the intended lifecycle conditions. | Intermittent or accidental exposure is plausible. | Exposure is likely, repeated, or associated with a known moisture-prone detail or activity. |
| Exposure frequency/duration | No recurring source; any exposure is expected to be brief. | Occasional events or periods of elevated moisture may occur. | Repeated, prolonged, or persistent exposure may occur. |
| Environmental moisture severity | Normal dry indoor or otherwise well-controlled conditions. | Periodic high RH, temperature-driven condensation potential, construction wetting, or moderate moisture load. | Wet, persistently humid, externally exposed, or otherwise severe moisture environment. |

### Suggested exposure class

Assign **Low, Medium, or High exposure** from the combined interpretation of the exposure criteria. Do not simply count ratings. The moisture source, pathway, lifecycle stage, and duration should be considered together.

## A3. Vulnerability classification

Vulnerability describes how strongly the timber element or detail may be affected if exposure occurs.

| Vulnerability criterion | Low | Medium | High |
|---|---|---|---|
| Moisture uptake/retention potential | Detail has limited opportunity for water entry or retention. | Moisture can enter or remain locally, depending on geometry, interfaces, or finishes. | End grain, joints, penetrations, cavities, interfaces, horizontal surfaces, or other details can promote rapid uptake, trapping, or internal migration. |
| Drying capacity | Open, ventilated, and readily able to dry after wetting. | Partial drying capacity; drying depends on finishes, cavities, ventilation, or local detailing. | Restricted drying due to membranes, finishes, concealed interfaces, low ventilation, moisture-trapping geometry, or enclosure. |
| Consequence of moisture exposure | Limited effect on durability, serviceability, maintenance, or later assessment. | May cause local deterioration, maintenance need, documentation uncertainty, or reduced confidence in future assessment. | May affect structural reliability, durability, concealed damage, repair scope, warranty, or future reuse-related assessment. |

### Suggested vulnerability class

Assign **Low, Medium, or High vulnerability** from the combined interpretation of the vulnerability criteria.

For structural timber and mass-timber elements, **Low vulnerability should be used cautiously**, because timber is moisture-sensitive. A low rating is most defensible where moisture uptake and retention are limited, drying is reliable, and the consequence of short-term exposure is low.

## A4. Moisture-risk matrix

Use exposure and vulnerability together to assign the initial moisture-risk class.

| Exposure ↓ / Vulnerability → | Low | Medium | High |
|---|---:|---:|---:|
| **Low** | Low | Low | Medium |
| **Medium** | Low | Medium | High |
| **High** | Medium | High | High |

The matrix provides a starting point for structured judgement. The assessor may deviate from the suggested class where project-specific evidence justifies doing so, but the reason should be recorded.

---

# Stage B — Monitoring-priority classification

Moisture risk alone does not determine how intensively a location should be monitored. Locations with similar physical moisture risk may require different monitoring strategies because they differ in accessibility, sensor reliability, or the importance of the resulting information.

## B1. Monitoring-priority criteria

| Criterion | Low | Medium | High |
|---|---|---|---|
| Inspection access / observability | Easy visual access and manual measurement; condition can be checked without opening the assembly. | Access is limited or requires minor intervention, equipment, or partial opening. | Concealed or inaccessible after enclosure; condition cannot be verified without disruptive opening. |
| Sensor survivability | Sensor is likely to remain protected, accessible, replaceable, and communicative. | Some risk of damage, drift, corrosion, communication loss, or access difficulty. | High risk of damage, drift, communication failure, corrosion, non-replaceability, or loss of interpretability. |
| Decision relevance | Data mainly provide background or reference information. | Data may support maintenance planning, event assessment, or drying verification. | Data may support enclosure approval, targeted opening, repair, warranty, durability evaluation, or future reuse-related assessment. |

### Interpreting sensor survivability

A **High sensor-survivability concern** does not necessarily mean that monitoring should be avoided. In a high-risk or decision-critical location, poor survivability may instead justify stronger protection, redundancy, replaceability, independent validation, or a different sensing method.

## B2. Monitoring priority

Assign a monitoring priority by considering the moisture-risk class together with inspection access, sensor survivability, and decision relevance.

| Monitoring priority | Typical interpretation | Possible monitoring response |
|---|---|---|
| **Low** | Low moisture risk and the condition can be readily inspected or verified by other means. | Periodic inspection, manual measurement, or reference monitoring. |
| **Medium** | Moderate moisture risk, partial uncertainty, or a useful but non-critical monitoring objective. | Representative MC measurement, RH/T context, and periodic checks. |
| **High** | High moisture risk, poor observability, restricted drying, or strong decision relevance. | Local MC sensor group, depth-specific measurements, RH/T context, and reference comparison. |
| **Critical** | Monitoring evidence is needed for a high-consequence or difficult-to-observe location and may directly support consequential lifecycle decisions. | Redundant MC measurements, shallow and deeper measurement points, RH/T context, reference location, protection/replaceability measures, and independent validation where feasible. |

A location can therefore have, for example, **Medium moisture risk but High monitoring priority** if it is concealed and the information is important for a later decision. Conversely, a physically high-risk location may not require permanent monitoring where it is continuously visible and can be inspected reliably by simpler means.

---

# Field definitions

| Field | Explanation |
|---|---|
| Location ID | Unique identifier for each candidate monitoring location, for example L-01, L-02, or L-03. |
| Description | Short description of the monitored location so that it can be understood without reading all other fields. |
| Lifecycle context | Stage and purpose of monitoring, such as construction, operational maintenance, post-event assessment, or future reuse-related evidence. |
| Building zone | Broad spatial, functional, or exposure-related area, such as kitchen, wet room, north façade, roof zone, service zone, basement, or exposed construction area. |
| Assembly/detail | Construction assembly or detail being assessed, such as CLT floor below sink, inter-panel junction, floor-wall junction, roof interface, or concealed connection. |
| Element/material feature | Specific timber feature of interest, such as panel surface, panel edge, fastener zone, end grain, concealed interface, or deeper internal region. |
| Moisture source | Origin of moisture, such as leakage, precipitation, construction water, condensation, cleaning water, ground moisture, or sustained high RH. |
| Moisture pathway/mechanism | Expected route and mechanism by which moisture can reach, accumulate in, or remain at the location. |
| Exposure likelihood | Qualitative assessment of how likely moisture exposure is. |
| Exposure frequency/duration | Qualitative assessment of how often and for how long exposure may occur. |
| Environmental moisture severity | Severity of the moisture-related environment. This replaces the broader use of environmental aggressiveness for physical moisture-risk classification. |
| Exposure class | Overall Low/Medium/High classification of moisture exposure. |
| Moisture uptake/retention potential | Susceptibility of the detail to absorb, trap, or redistribute moisture. |
| Drying capacity | Ability of the location to dry after wetting. Low drying capacity increases vulnerability. |
| Consequence | Potential effect of moisture exposure on durability, serviceability, structural reliability, repair, documentation, or future reuse assessment. |
| Vulnerability class | Overall Low/Medium/High classification of the location's vulnerability if wetting occurs. |
| Moisture-risk class | Low/Medium/High classification derived primarily from exposure and vulnerability. |
| Inspection access / observability | Ability to inspect, manually measure, repair, or open the location after enclosure. |
| Sensor survivability | Likelihood that the sensor can remain functional, protected, accessible, replaceable, communicative, and interpretable over time. |
| Decision relevance | Importance of the information for later decisions such as enclosure approval, inspection, drying verification, repair, warranty, post-event assessment, or reuse-related assessment. |
| Monitoring priority | Low/Medium/High/Critical classification indicating the intensity and reliability of monitoring justified at the location. |
| Monitoring reliability concern | Specific reason why data may be uncertain, incomplete, or difficult to interpret, such as localised wetting, sensor damage, drift, missing data, limited access, or lack of reference measurements. |
| Suggested monitoring response | Proposed monitoring approach, including sensor type, placement, depth, density, redundancy, RH/T context, reference locations, protection, replaceability, or validation needs. |
| Justification | Brief explanation of the moisture-risk class and monitoring-priority assignment. |

---

# Risk-location classification table

| Location ID | Description | Lifecycle context | Building zone | Assembly/detail | Element/material feature | Moisture source | Moisture pathway/mechanism | Exposure likelihood | Exposure frequency/duration | Environmental moisture severity | Exposure class | Moisture uptake/retention potential | Drying capacity | Consequence | Vulnerability class | Moisture-risk class | Inspection access / observability | Sensor survivability | Decision relevance | Monitoring priority | Monitoring reliability concern | Suggested monitoring response | Justification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L-01 | | | | | | | | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High/Critical | | | |
| L-02 | | | | | | | | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High/Critical | | | |
| L-03 | | | | | | | | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High | Low/Medium/High/Critical | | | |

---

# Relationship to the original decision factors

The conceptual framework identifies exposure likelihood, drying capacity, inspection access, consequence, environmental aggressiveness, sensor survivability, and decision relevance as decision factors for risk-informed monitoring. This implementation retains those concepts but organises them more explicitly:

| Original decision factor | Refined implementation |
|---|---|
| Exposure likelihood | Exposure assessment |
| Drying capacity | Vulnerability assessment |
| Inspection access | Monitoring-priority assessment as inspection access / observability |
| Consequence | Vulnerability assessment |
| Environmental aggressiveness | Split into environmental moisture severity for physical risk and sensor survivability where the environment threatens the sensing system |
| Sensor survivability | Monitoring-priority assessment |
| Decision relevance | Monitoring-priority assessment |

This is an implementation refinement rather than a change to the eight-layer conceptual framework.

---

# Notes for use

- Classify a **defined moisture scenario**, not merely a room or generic building element.
- Record the source, pathway, susceptible feature, and expected drying behaviour before assigning ratings.
- Do not calculate the moisture-risk class by simply counting High ratings. Use the exposure-vulnerability logic and document the engineering judgement applied.
- Do not use moisture risk and monitoring priority interchangeably.
- Consider whether a location can be observed reliably without permanent sensing before increasing sensor density.
- Where data are intended to support consequential decisions, prioritise redundancy, contextual RH/T measurements, reference locations, validation, traceable metadata, and sensor replaceability where feasible.
- Revisit both classifications if the design, construction sequence, finishes, access conditions, lifecycle stage, sensor system, or monitoring objective changes.

## Practice alignment

The separation of moisture exposure and component vulnerability is consistent with risk-based moisture-management practice in timber construction, including the Danish Technological Institute's *Moisture Management for Timber Construction: A Practical Guide* (2025). The present framework extends that logic from moisture-management risk assessment to **monitoring priority**, lifecycle evidence, and reuse-oriented decision support.
