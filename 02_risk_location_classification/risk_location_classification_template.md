# Risk-location classification template

This template supports Layer 2 of the framework: moisture-risk mapping and classification. It is used to identify candidate monitoring locations and classify them according to moisture risk and monitoring reliability.

The classification should be treated as structured engineering judgement. It is not a fixed scoring system.

## Classification criteria

| Criterion                    | Low                                                                                                          | Medium                                                                                             | High                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Exposure likelihood          | Unlikely moisture exposure under normal use.                                                                 | Possible intermittent exposure, leakage, condensation, or construction wetting.                    | Likely or repeated exposure due to plumbing, wet rooms, roof/façade interfaces, construction exposure, or known moisture-prone detailing.     |
| Drying capacity              | Open, ventilated, or easily dried if wetting occurs.                                                         | Partial drying capacity; drying may depend on finishes, cavities, or local detailing.              | Restricted drying due to membranes, finishes, concealed interfaces, low ventilation, or moisture-trapping details.                            |
| Inspection access            | Easy access for visual inspection, manual measurement, or repair.                                            | Limited access requiring partial opening or specialist inspection.                                 | Concealed or inaccessible after enclosure, with difficult inspection or repair.                                                               |
| Consequence                  | Low consequence if moisture occurs; limited effect on durability, serviceability, or later reuse assessment. | Moderate consequence; may affect maintenance planning, local durability, or documentation quality. | High consequence; may affect structural reliability, durability, repair decisions, warranty, or future reuse-related assessment.              |
| Environmental aggressiveness | Normal indoor environment.                                                                                   | Periodic high RH, temperature variation, or moderate moisture load.                                | Wet, high-humidity, chemically aggressive, or otherwise severe environment.                                                                   |
| Sensor survivability         | Sensors are likely to remain protected, accessible, and replaceable.                                         | Some risk of sensor damage, communication loss, corrosion, or access difficulty.                   | High risk of sensor damage, drift, communication failure, corrosion, or non-replaceability.                                                   |
| Decision relevance           | Data mainly provide background or reference information.                                                     | Data may support maintenance planning or post-event assessment.                                    | Data may support enclosure approval, targeted opening, repair decisions, warranty, durability evaluation, or future reuse-related assessment. |

## Field definitions

| Field | Explanation |
|---|---|
| Location ID | Unique identifier for each candidate monitoring location, for example L-01, L-02, or L-03. |
| Description | Short description of the monitored location so that the location can be understood without reading all other fields. |
| Lifecycle context | The stage and purpose of monitoring, such as construction, operational maintenance, post-event assessment, or future reuse-related evidence. |
| Building zone | The broad spatial, functional, or exposure-related area where the location occurs, such as kitchen, wet room, north façade, roof zone, service zone, basement, or exposed construction area. |
| Assembly/detail | The construction assembly or detail being assessed, such as CLT floor below sink, inter-panel junction, floor-wall junction, roof interface, or concealed connection. |
| Element/material feature | The specific timber element or material feature of interest, such as panel surface, panel edge, fastener zone, end grain, concealed interface, or deeper internal region. |
| Moisture source or mechanism | The expected way moisture may enter, accumulate, or remain in the location, such as leakage, condensation, construction wetting, cleaning water, trapped moisture, or moisture migration along joints. |
| Exposure likelihood | Qualitative rating of how likely moisture exposure is at the location. |
| Drying capacity | Qualitative rating of how easily the location can dry after wetting. Low drying capacity indicates greater concern. |
| Inspection access | Qualitative rating of how easily the location can be inspected, measured manually, repaired, or opened after enclosure. Low access indicates greater concern. |
| Consequence | Severity of the potential effect if moisture exposure occurs and drying is delayed, including implications for durability, structural reliability, repair needs, serviceability, or future reuse assessment. |
| Environmental aggressiveness | Severity of the surrounding environment, including high humidity, wet exposure, temperature variation, chemical exposure, or other conditions that may increase moisture-related risk or sensor degradation. |
| Sensor survivability | Likelihood that the sensor can remain functional, protected, accessible, and interpretable over time. Low survivability indicates higher risk of sensor damage, drift, corrosion, communication loss, or non-replaceability. |
| Decision relevance | Importance of monitoring data from this location for later decisions, such as enclosure approval, inspection, targeted opening, drying verification, repair, warranty, post-event assessment, or reuse-related assessment. |
| Risk class | Overall qualitative classification of the location, based on the combined interpretation of moisture risk, monitoring reliability, consequence, and decision relevance. |
| Monitoring reliability concern | Specific reason why data from this location may be uncertain, incomplete, or difficult to interpret, such as localised wetting, limited access, sensor damage, drift, missing data, or lack of reference measurements. |
| Suggested monitoring response | Proposed monitoring approach for the location, including sensor type, placement, depth, density, redundancy, RH/T context, reference locations, or validation needs. |
| Justification | Brief explanation of why the risk class and monitoring response were assigned. |

## Risk-location classification table

| Location ID | Description | Lifecycle context | Building zone | Assembly/detail | Element/material feature | Moisture source or mechanism | Exposure likelihood | Drying capacity | Inspection access | Consequence     | Environmental aggressiveness | Sensor survivability | Decision relevance | Risk class               | Monitoring reliability concern | Suggested monitoring response | Justification |
| ----------- | ----------- | ----------------- | ------------- | --------------- | ------------------------ | ---------------------------- | ------------------- | --------------- | ----------------- | --------------- | ---------------------------- | -------------------- | ------------------ | ------------------------ | ------------------------------ | ----------------------------- | ------------- |
| L-01        |             |                   |               |                 |                          |                              | Low/Medium/High     | Low/Medium/High | Low/Medium/High   | Low/Medium/High | Low/Medium/High              | Low/Medium/High      | Low/Medium/High    | Low/Medium/High/Critical |                                |                               |               |
| L-02        |             |                   |               |                 |                          |                              | Low/Medium/High     | Low/Medium/High | Low/Medium/High   | Low/Medium/High | Low/Medium/High              | Low/Medium/High      | Low/Medium/High    | Low/Medium/High/Critical |                                |                               |               |
| L-03        |             |                   |               |                 |                          |                              | Low/Medium/High     | Low/Medium/High | Low/Medium/High   | Low/Medium/High | Low/Medium/High              | Low/Medium/High      | Low/Medium/High    | Low/Medium/High/Critical |                                |                               |               |


## Suggested interpretation of risk class

| Risk class | Typical interpretation                                                                                                                     | Possible monitoring response                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Low        | Low likelihood or consequence of moisture exposure, or easy inspection and drying.                                                         | Periodic inspection, manual measurement, or reference monitoring.                                                                              |
| Medium     | Some moisture likelihood, moderate consequence, or partial uncertainty in drying or access.                                                | Representative sensor group, RH/T context, and periodic checks.                                                                                |
| High       | Likely exposure, restricted drying, concealed access, high consequence, or strong decision relevance.                                      | Local MC sensor group, depth-specific measurements, RH/T context, and reference location.                                                      |
| Critical   | High-risk location where data may support enclosure approval, repair, warranty, post-event assessment, or future reuse-related assessment. | Redundant MC measurements, shallow and deeper measurement points, RH/T context, reference location, and independent validation where feasible. |

## Notes for use

* Assign the risk class based on the combined interpretation of the criteria, not by simply counting high ratings.
* Record the reasoning behind the classification in the justification column.
* Consider both moisture risk and monitoring reliability. A location may require stronger monitoring not only because wetting is likely, but also because later interpretation would be uncertain without redundant or contextual data.
* Revisit the classification if the design, construction sequence, finishes, access conditions, or monitoring objective changes.
