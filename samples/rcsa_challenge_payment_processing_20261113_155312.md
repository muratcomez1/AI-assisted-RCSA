# RCSA Challenge Report: Payment Processing

- Generated: 2026-11-13 15:53
- Run status: **COMPLETED**
- Data: synthetic demonstration data only
- Review: **human Second Line review required**. Approval: **Pending**
- This report supports a reviewer. It does not rate risk, approve controls or decide compliance.

## 1. Summary

- Process-risk pairs analysed: 7 (7 marked applicable by the First Line)
- High review priority: P10
- Flags raised: ACTION_REQUIRED x5, CONTROL_CONFLICT x1, CONTROL_NOT_EFFECTIVE x2, LOSS_EVENTS_PRESENT x4, NO_CONTROL x3, NO_KRI_COVERAGE x4, RCSA_GAP x3

## 2. Overview

| Pair | Process | Risk | Applicable | Loss events | KRI | Prev. RCSA | Control | Flags | Scenario result (rules) | Review priority |
|---|---|---|---|---|---|---|---|---|---|---|
| P08 | Payment Processing | R1 Process execution error | Yes | 2 (5,800 EUR) | - | N | None | LOSS_EVENTS_PRESENT, RCSA_GAP, NO_KRI_COVERAGE, NO_CONTROL, ACTION_REQUIRED | High - residual = inherent | medium |
| P09 | Payment Processing | R2 Third-party failure | Yes | 3 (10,800 EUR) | - | N | Not effective | LOSS_EVENTS_PRESENT, RCSA_GAP, NO_KRI_COVERAGE, CONTROL_NOT_EFFECTIVE, ACTION_REQUIRED | High - action required | medium |
| P10 | Payment Processing | R3 System outage | Yes | 1 (4,300 EUR) | - | N | Effective | LOSS_EVENTS_PRESENT, RCSA_GAP, NO_KRI_COVERAGE, CONTROL_CONFLICT | Conflict - effectiveness downgraded, residual floor applied | high |
| P11 | Payment Processing | R4 Data quality error | Yes | 0 (0 EUR) | Data quality exceptions | Y | None | NO_CONTROL, ACTION_REQUIRED | High - residual = inherent | medium |
| P12 | Payment Processing | R5 Unauthorized access or fraud | Yes | 0 (0 EUR) | Overdue access reviews | Y | Not effective | CONTROL_NOT_EFFECTIVE, ACTION_REQUIRED | High - action required | medium |
| P13 | Payment Processing | R6 Regulatory non-compliance | Yes | 0 (0 EUR) | Open regulatory findings | Y | Effective | - | Residual reduced, accepted | low |
| P14 | Payment Processing | R7 Key person dependency | Yes | 2 (7,200 EUR) | - | Y | None | LOSS_EVENTS_PRESENT, NO_KRI_COVERAGE, NO_CONTROL, ACTION_REQUIRED | High - residual = inherent | medium |

## 3. Detailed challenges

### P08: Process execution error (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Information only: loss events exist but no KRI is assigned. A missing KRI says nothing about control effectiveness; the owner may not have needed one.
- NO_CONTROL: Risk is applicable but no control is described.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** The risk is marked applicable but was not included in the previous RCSA, and no control is described; please explain the omission and how the risk is currently managed (DATA:P08). Two loss events are recorded for this process-risk pair, but their presence alone does not establish control failure; clarify their causes and whether they inform the current assessment (DATA:P08; G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- Why was this applicable risk omitted from the previous RCSA, and what control or other risk-management measures currently address process execution errors?
- What were the causes of the two recorded loss events, and what follow-up or control testing, if any, was performed?
- Would a KRI add value for monitoring this risk, or is other monitoring considered sufficient?

**Suggested follow-up:** Ask the owner to document the rationale for the RCSA omission, the current control environment, and the event analysis. Consider KRI coverage as an optional monitoring question, not as a control finding (G-rcsa_challenge_guidance#3).

Evidence cited: DATA:P08, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#3 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#3 (Missing KRI coverage (information only)); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P09: Third-party failure (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Information only: loss events exist but no KRI is assigned. A missing KRI says nothing about control effectiveness; the owner may not have needed one.
- CONTROL_NOT_EFFECTIVE: The control is described as Not effective.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** R2 is marked applicable but was not included in the previous RCSA; the current record also describes the control as “Not effective” and records three loss events totaling EUR 10,800. The events do not by themselves establish the cause or demonstrate how the control operated, so clarification is needed on their relationship to the control and the RCSA omission. [DATA:P09; G-rcsa_challenge_guidance#2]

**Questions for the process owner:**
- What were the causes of the recorded loss events, and how did the control operate in response to them?
- Why was this applicable risk omitted from the previous RCSA, and what remediation or control testing evidence supports the current assessment?
- Would a KRI add value for monitoring this risk, given none is currently assigned? [G-rcsa_challenge_guidance#3]

**Suggested follow-up:** Ask the owner to document the rationale for the RCSA omission, the event root-cause analysis, and any remediation or testing evidence. Consider whether a KRI would add value as an optional monitoring measure.

Evidence cited: DATA:P09, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#3 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#3 (Missing KRI coverage (information only)); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P10: System outage (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Information only: loss events exist but no KRI is assigned. A missing KRI says nothing about control effectiveness; the owner may not have needed one.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** For Payment Processing, System outage is marked applicable and the control is described as effective, while one loss event of EUR 4,300 is recorded and the risk was absent from the previous RCSA (DATA:P10). The event does not by itself establish control failure; please explain its cause and timing and provide relevant control testing evidence (G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What was the root cause of the loss event, and what does control testing show about the control’s operation at that time?
- Why was this applicable risk not included in the previous RCSA, and would a KRI add value for ongoing monitoring?

**Suggested follow-up:** Review the owner’s root cause analysis, control testing evidence, and explanation for the RCSA omission. Consider KRI coverage only as an optional monitoring observation, not as evidence of control effectiveness (G-rcsa_challenge_guidance#3).

Evidence cited: DATA:P10, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#3 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#3 (Missing KRI coverage (information only)); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P11: Data quality error (Payment Processing)

- NO_CONTROL: Risk is applicable but no control is described.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** The risk is marked applicable, but no control is described; the scenario states that residual exposure equals inherent exposure (DATA:P11, G-rcsa_challenge_guidance#5). The recorded absence of loss events does not establish that the risk is adequately controlled; please clarify how data quality errors are prevented or detected (DATA:P11, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#10).

**Questions for the process owner:**
- What controls validate data at entry or reconcile data between systems, and who owns the critical data and control operation?
- How are “Data quality exceptions” monitored, and if no control is in place, what is the rationale for accepting the exposure and how will that acceptance be routed through governance?

**Suggested follow-up:** Document and assign relevant preventive or detective controls, including their ownership and operation, or document the rationale for accepting the exposure and route it through appropriate governance (G-rcsa_challenge_guidance#5, G-rcsa_challenge_guidance#10).

Evidence cited: DATA:P11, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#5, G-rcsa_challenge_guidance#10 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#5 (Applicable risk without a control)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P12: Unauthorized access or fraud (Payment Processing)

- CONTROL_NOT_EFFECTIVE: The control is described as Not effective.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** For Payment Processing, the risk is marked applicable and the control is described as “Not effective”; the KRI is “Overdue access reviews.” Please clarify the nature and extent of the overdue reviews and how access risks are being managed; the absence of recorded loss events does not resolve this control concern. (DATA:P12; G-rcsa_challenge_guidance#11)

**Questions for the process owner:**
- Which access reviews are overdue, what systems or user populations do they cover, and what is the remediation plan and timeline?
- What evidence supports the current assessment of access controls, including any relevant segregation-of-duties, monitoring, alerting, or authentication measures?

**Suggested follow-up:** Ask the owner to provide the review backlog, remediation evidence and relevant control-testing results for human review. Consider whether the RCSA description should clarify interim safeguards and follow-up monitoring.

Evidence cited: DATA:P12, G-rcsa_challenge_guidance#11 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#3 (Missing KRI coverage (information only))

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P13: Regulatory non-compliance (Payment Processing)

- No flags

**Challenge:** The RCSA records regulatory non-compliance as applicable and previously included, with the control marked “Effective” and residual risk reduced and accepted, but provides no supporting detail for that assessment (DATA:P13). Please substantiate how applicable requirements, regulatory change, findings, and staff training are addressed; the absence of recorded loss events alone does not resolve this risk (DATA:P13; G-rcsa_challenge_guidance#12).

**Questions for the process owner:**
- Which legal and supervisory requirements apply to Payment Processing, and who monitors and implements regulatory changes?
- What evidence supports the control’s effectiveness and residual-risk reduction, including relevant audit or supervisory findings and staff training? 

**Suggested follow-up:** Provide evidence supporting the control assessment and residual-risk decision, and update the RCSA rationale or control description as needed for reviewer consideration.

Evidence cited: DATA:P13, G-rcsa_challenge_guidance#12 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P14: Key person dependency (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- NO_KRI_COVERAGE: Information only: loss events exist but no KRI is assigned. A missing KRI says nothing about control effectiveness; the owner may not have needed one.
- NO_CONTROL: Risk is applicable but no control is described.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** The RCSA marks key person dependency as applicable and records two loss events, but describes no control; this warrants clarification of how the risk is currently managed, without concluding that the events prove a control failure (DATA:P14; G-rcsa_challenge_guidance#2). No KRI is assigned, which is an optional monitoring point rather than evidence about control effectiveness (G-rcsa_challenge_guidance#3).

**Questions for the process owner:**
- What were the causes of the recorded loss events, and what has changed in response to them?
- What arrangements currently address key person dependency, such as backup coverage or knowledge transfer, and how is their operation evidenced?

**Suggested follow-up:** Clarify and document any current controls and supporting evidence, and consider whether a KRI would add value for monitoring this risk.

Evidence cited: DATA:P14, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#3 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#3 (Missing KRI coverage (information only)); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

**Wikipedia Search API**: status `ok`, attempts 1
- Delivery versus payment (https://en.wikipedia.org/wiki/Delivery_versus_payment)
- Straight-through processing (https://en.wikipedia.org/wiki/Straight-through_processing)
- Payment card number (https://en.wikipedia.org/wiki/Payment_card_number)
- Payment Card Industry Data Security Standard (https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)
- Banking software (https://en.wikipedia.org/wiki/Banking_software)

**Tavily Search API**: status `ok`, attempts 1
- Operational Risk Management in Banking: ORM Framework (https://www.metricstream.com/learn/operational-risk-management-in-banking.html)
- Operational Resilience in Digital Payments: Experiences and Issues, WP/21/288, December 2021 (https://www.imf.org/-/media/files/publications/wp/2021/english/wpiea2021288-print-pdf.pdf)
- Payment Systems | Comptroller's Handbook (https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/payment-sys-funds-transfer-activities/pub-ch-payment-systems.pdf)
- Operational Risk Management Challenges for Banks in 2026 | 360factors (https://www.360factors.com/blog/top-operational-risk-management-challenges)
- Operational Risk Management in Banking: What It Is & Why It Matters | Auditive (https://auditive.io/blog/operational-risk-management-overview-for-the-banking-industry)

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 15:52:36 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 15:52:36 | apply_rules | ok | Rules applied to 7 pairs; 1 high review priority |
| 15:52:36 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 15:52:38 | external_research | ok | Wikipedia Search API: ok, 5 items, 1 attempts |
| 15:52:38 | external_research | ok | Tavily Search API: ok, 5 items, 1 attempts |
| 15:53:12 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-6-luna); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
