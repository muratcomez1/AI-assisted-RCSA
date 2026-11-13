# RCSA Challenge Report: Access Management

- Generated: 2026-11-13 15:52
- Run status: **COMPLETED_WITH_WARNINGS**
- Data: synthetic demonstration data only
- Review: **human Second Line review required**. Approval: **Pending**
- This report supports a reviewer. It does not rate risk, approve controls or decide compliance.

## 1. Summary

- Process-risk pairs analysed: 7 (1 marked applicable by the First Line)
- High review priority: P22, P24
- Flags raised: APPLICABILITY_CHALLENGE x1, CONTROL_CONFLICT x1, DATA_ANOMALY x1, LOSS_EVENTS_PRESENT x1, NOT_APPLICABLE_ACCEPTED x5

## 2. Overview

| Pair | Process | Risk | Applicable | Loss events | KRI | Prev. RCSA | Control | Flags | Scenario result (rules) | Review priority |
|---|---|---|---|---|---|---|---|---|---|---|
| P22 | Access Management | R1 Process execution error | Yes | 1 (2,200 EUR) | Error rate % | Y | Effective | LOSS_EVENTS_PRESENT, CONTROL_CONFLICT | Conflict - effectiveness downgraded, residual floor applied | high |
| P23 | Access Management | R2 Third-party failure | No | 0 (0 EUR) | - | N | n/a | NOT_APPLICABLE_ACCEPTED | Not applicable - accepted | low |
| P24 | Access Management | R3 System outage | No | 0 (0 EUR) | - | N | Effective | APPLICABILITY_CHALLENGE, DATA_ANOMALY | Not applicable - challenge needed | high |
| P25 | Access Management | R4 Data quality error | No | 0 (0 EUR) | - | N | n/a | NOT_APPLICABLE_ACCEPTED | Not applicable - accepted | low |
| P26 | Access Management | R5 Unauthorized access or fraud | No | 0 (0 EUR) | - | N | n/a | NOT_APPLICABLE_ACCEPTED | Not applicable - accepted | low |
| P27 | Access Management | R6 Regulatory non-compliance | No | 0 (0 EUR) | - | N | n/a | NOT_APPLICABLE_ACCEPTED | Not applicable - accepted | low |
| P28 | Access Management | R7 Key person dependency | No | 0 (0 EUR) | - | N | n/a | NOT_APPLICABLE_ACCEPTED | Not applicable - accepted | low |

## 3. Detailed challenges

### P22: Process execution error (Access Management)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** The control is described as Effective, while one loss event (€2,200) is recorded for this process-risk pair. This does not by itself establish control failure; please explain the event’s root cause and provide relevant control testing evidence for review (DATA:P22; G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What was the root cause of the loss event, and did it predate the control or arise from a cause outside its scope?
- What control testing evidence supports the Effective assessment, including any response to the event?

**Suggested follow-up:** Provide the root cause analysis and relevant control testing evidence, then explain whether the event changes the control assessment. Have the human reviewer consider the response before finalising the RCSA entry.

Evidence cited: DATA:P22, G-rcsa_challenge_guidance#2 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#3 (Missing KRI coverage (information only))

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P23: Third-party failure (Access Management)

- NOT_APPLICABLE_ACCEPTED: Marked not applicable and no contradicting evidence was found.

**Challenge:** The not-applicable response is recorded as accepted, with no contradicting evidence identified (DATA:P23). However, the absence of loss events and a KRI does not by itself establish that third-party failure is not applicable; the owner should explain whether vendors support any part of Access Management and why the risk is outside the process scope (G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#8).

**Questions for the process owner:**
- Do any third parties provide or support Access Management services, systems, or activities, and could their outage, service-level breach, or insolvency affect the process?
- If no relevant third parties are involved, what process-scope evidence supports marking this risk not applicable?

**Suggested follow-up:** Ask the owner to document the third-party scope assessment and basis for the not-applicable decision. Revisit the assessment if that explanation identifies relevant third-party dependencies.

Evidence cited: DATA:P23, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#8 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#8 (Third-party failure); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P24: System outage (Access Management)

- APPLICABILITY_CHALLENGE: Marked not applicable, but evidence exists (loss events, KRI, previous RCSA or a control). Applicability needs to be challenged.
- DATA_ANOMALY: The source data marks an anomaly for this pair.

**Challenge:** The risk is marked not applicable, but an effective control is recorded for Access Management and the source flags that control as unsupported by evidence; this requires clarification of the applicability decision and control record (DATA:P24; G-rcsa_challenge_guidance#1). No loss events are recorded, which alone does not establish that the risk is not applicable (DATA:P24; G-rcsa_challenge_guidance#1).

**Questions for the process owner:**
- Why is system outage not applicable to Access Management when a control is recorded for this risk?
- What evidence supports the control’s description and effectiveness, and how does the control address system outage risk?

**Suggested follow-up:** Ask the owner to explain the applicability decision and provide supporting control evidence. Update the RCSA entry as appropriate following the human reviewer’s assessment.

Evidence cited: DATA:P24, G-rcsa_challenge_guidance#1 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#3 (Missing KRI coverage (information only))

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P25: Data quality error (Access Management)

- NOT_APPLICABLE_ACCEPTED: Marked not applicable and no contradicting evidence was found.

**Challenge:** The not-applicable rationale is not supported by evidence about how Access Management handles data or why data quality error cannot arise in this process. The absence of loss events, a KRI, a control description, or a previous RCSA entry does not by itself establish that the risk is not applicable (DATA:P25; G-rcsa_challenge_guidance#1, #10).

**Questions for the process owner:**
- What data is created, changed, or used in Access Management, and why could errors in it not lead to wrong decisions or reports?
- What supports marking this risk not applicable, including consideration of data-entry validation, reconciliations, critical-data ownership, and any prior data incidents?

**Suggested follow-up:** Ask the owner to document the process-specific rationale for the not-applicable decision. Revisit applicability if the explanation identifies relevant data-quality exposures or controls.

Evidence cited: DATA:P25, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#10 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P26: Unauthorized access or fraud (Access Management)

- NOT_APPLICABLE_ACCEPTED: Marked not applicable and no contradicting evidence was found.

**Challenge:** The risk is marked not applicable for Access Management, with no control described (DATA:P26). The absence of loss events, a KRI, or a prior RCSA entry does not by itself establish that unauthorized access or fraud is outside the process scope (G-rcsa_challenge_guidance#1).

**Questions for the process owner:**
- Which Access Management activities or process boundaries support excluding unauthorized access or fraud from this assessment?
- Do access provisioning, access reviews, segregation of duties, monitoring, or authentication activities fall within this process, and if so, why are they outside the risk assessment?

**Suggested follow-up:** Ask the owner to document the process-scope rationale for the not-applicable decision and clarify whether any access-related activities are included. Revisit the applicability determination in light of that explanation.

Evidence cited: DATA:P26, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#11 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P27: Regulatory non-compliance (Access Management)

- NOT_APPLICABLE_ACCEPTED: Marked not applicable and no contradicting evidence was found.

**Challenge:** The record shows Regulatory non-compliance marked not applicable, with no loss events, KRI, prior RCSA entry, or described control; these absences alone do not establish that the risk is not applicable (DATA:P27; G-rcsa_challenge_guidance#1). Please substantiate how applicability was assessed for Access Management, including relevant requirements and regulatory-change monitoring (G-rcsa_challenge_guidance#12).

**Questions for the process owner:**
- Which legal or supervisory requirements were considered when determining whether this risk applies to Access Management?
- Who monitors relevant regulatory changes, and what supports the decision to mark this risk not applicable?

**Suggested follow-up:** Ask the owner to document the applicability rationale and the basis for the not-applicable response, including how relevant requirements and changes are monitored.

Evidence cited: DATA:P27, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#12 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P28: Key person dependency (Access Management)

- NOT_APPLICABLE_ACCEPTED: Marked not applicable and no contradicting evidence was found.

**Challenge:** The risk is marked not applicable for Access Management, with no control described; the supplied record does not explain the basis for that conclusion (DATA:P28). Please clarify whether the process relies on one or a few individuals and how that was assessed, including any relevant procedures, deputies, knowledge transfer, absences or departures, and concentration of access rights (G-rcsa_challenge_guidance#13).

**Questions for the process owner:**
- What process-specific factors support marking key person dependency not applicable?
- How are duties, knowledge and access managed if a key individual is unavailable or leaves?

**Suggested follow-up:** Ask the owner to document the rationale for the not-applicable decision and the relevant process evidence. Revisit the RCSA treatment after receiving that explanation.

Evidence cited: DATA:P28, G-rcsa_challenge_guidance#13, G-rcsa_challenge_guidance#1 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#13 (Key person dependency); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

**Wikipedia Search API**: status `ok`, attempts 1
- Third-party management (https://en.wikipedia.org/wiki/Third-party_management)
- Privileged access management (https://en.wikipedia.org/wiki/Privileged_access_management)
- Financial risk management (https://en.wikipedia.org/wiki/Financial_risk_management)
- Supply chain risk management (https://en.wikipedia.org/wiki/Supply_chain_risk_management)
- IT risk management (https://en.wikipedia.org/wiki/IT_risk_management)

**Tavily Search API**: status `ok`, attempts 1
- Operational Risk Management in Banking: ORM Framework (https://www.metricstream.com/learn/operational-risk-management-in-banking.html)
- Operational Risk Management Challenges for Banks in 2026 | 360factors (https://www.360factors.com/blog/top-operational-risk-management-challenges)
- Compliance And Risk Architecture For Banks: A Blueprint For Building Digital Asset Operations | Fireblocks (https://www.fireblocks.com/report/banks-digital-asset-compliance-blueprint)
- Full value: Mitigating operational risk to prevent value dilution on foreign equities (https://finance.yahoo.com/news/full-value-mitigating-operational-risk-230042101.html)
- Cyber and Data Security Policy - ICBA.org (https://www.icba.org/cyber-and-data-security-policy)

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 15:51:57 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 15:51:57 | apply_rules | warning | P24: source expected result 'Not applicable - accepted' differs from rule result 'Not applicable - challenge needed' |
| 15:51:57 | apply_rules | ok | Rules applied to 7 pairs; 2 high review priority |
| 15:51:57 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 15:51:58 | external_research | ok | Wikipedia Search API: ok, 5 items, 1 attempts |
| 15:51:58 | external_research | ok | Tavily Search API: ok, 5 items, 1 attempts |
| 15:52:27 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-6-luna); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
