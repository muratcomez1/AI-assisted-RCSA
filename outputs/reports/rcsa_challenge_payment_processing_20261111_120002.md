# RCSA Challenge Report: Payment Processing

- Generated: 2026-11-11 12:00
- Run status: **COMPLETED_WITH_WARNINGS**
- Data: synthetic demonstration data only
- Review: **human Second Line review required**. Approval: **Pending**
- This report supports a reviewer. It does not rate risk, approve controls or decide compliance.

## 1. Summary

- Process-risk pairs analysed: 7 (7 marked applicable by the First Line)
- High review priority: P10
- Flags raised: CONTROL_CONFLICT x1, LOSS_EVENTS_PRESENT x4, NO_CONTROL x3, NO_KRI_COVERAGE x4, RCSA_GAP x3

## 2. Overview

| Pair | Process | Risk | Applicable | Loss events | KRI | Prev. RCSA | Control | Flags | Source expected result | Review priority |
|---|---|---|---|---|---|---|---|---|---|---|
| P08 | Payment Processing | R1 Process execution error | Yes | 2 (5,800 EUR) | - | N | None | LOSS_EVENTS_PRESENT, RCSA_GAP, NO_KRI_COVERAGE, NO_CONTROL | High - residual = inherent | medium |
| P09 | Payment Processing | R2 Third-party failure | Yes | 3 (10,800 EUR) | - | N | Not effective | LOSS_EVENTS_PRESENT, RCSA_GAP, NO_KRI_COVERAGE | High - action required | medium |
| P10 | Payment Processing | R3 System outage | Yes | 1 (4,300 EUR) | - | N | Effective | LOSS_EVENTS_PRESENT, RCSA_GAP, NO_KRI_COVERAGE, CONTROL_CONFLICT | Conflict - effectiveness downgraded, residual floor applied | high |
| P11 | Payment Processing | R4 Data quality error | Yes | 0 (0 EUR) | Data quality exceptions | Y | None | NO_CONTROL | High - residual = inherent | medium |
| P12 | Payment Processing | R5 Unauthorized access or fraud | Yes | 0 (0 EUR) | Overdue access reviews | Y | Not effective | - | High - action required | low |
| P13 | Payment Processing | R6 Regulatory non-compliance | Yes | 0 (0 EUR) | Open regulatory findings | Y | Effective | - | Residual reduced, accepted | low |
| P14 | Payment Processing | R7 Key person dependency | Yes | 2 (7,200 EUR) | - | Y | None | LOSS_EVENTS_PRESENT, NO_KRI_COVERAGE, NO_CONTROL | High - residual = inherent | medium |

## 3. Detailed challenges

### P08: Process execution error (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The RCSA indicates that there are two loss events associated with the process execution error in Payment Processing, yet no controls are described. This raises concerns about the adequacy of risk management in this area. Additionally, the absence of KRI coverage and the fact that this risk was not included in the previous RCSA warrant further investigation.

**Questions for the process owner:**
- What measures are in place to address the identified loss events, and why are there no controls described?
- What changes in the process, systems, or environment led to the inclusion of this risk in the current RCSA when it was absent previously?

**Suggested follow-up:** Consider implementing appropriate controls and KRI coverage for this risk. A thorough review of the loss events and their root causes should also be conducted.

Evidence cited: DATA:P08, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#2 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P09: Third-party failure (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.

**Challenge:** The RCSA indicates that the control for third-party failure is not effective despite the presence of three loss events totaling €10,800. This raises questions about the root cause analysis and whether the control was in place at the time of the loss events. Additionally, the risk was not included in the previous RCSA, which warrants further investigation into what changes occurred in the process or environment.

**Questions for the process owner:**
- What is the root cause analysis for the loss events related to third-party failure?
- What changes in the process, systems, or environment led to the inclusion of this risk in the current RCSA?

**Suggested follow-up:** Provide a detailed explanation regarding the effectiveness of the control and the circumstances surrounding the loss events. Additionally, clarify the rationale for the risk's absence in the previous RCSA.

Evidence cited: DATA:P09, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#2 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P10: System outage (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** The control is described as effective despite the presence of a loss event, which raises questions about its effectiveness. Additionally, the risk was not included in the previous RCSA, suggesting a potential gap in the assessment process.

**Questions for the process owner:**
- What is the root cause analysis for the loss event that occurred?
- What evidence do you have to support the effectiveness of the control given the loss event?
- What changes in the process, systems, or environment led to the inclusion of this risk in the current RCSA?

**Suggested follow-up:** Please provide a detailed explanation addressing the questions raised and any supporting documentation regarding the control's effectiveness and the loss event.

Evidence cited: DATA:P10, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P11: Data quality error (Payment Processing)

- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The RCSA identifies a data quality error risk in payment processing but does not describe any controls to mitigate this risk. This raises concerns about the potential for significant residual exposure, as there are no measures in place to manage the inherent risk. Additionally, while there are no recorded loss events, the absence of controls could lead to undetected data quality issues.

**Questions for the process owner:**
- What measures are in place to validate data quality at entry and ensure reconciliation between systems?
- Can you explain why no controls have been defined for this applicable risk, and how the acceptance of this exposure has been documented?

**Suggested follow-up:** Please define and assign appropriate controls for the identified risk or document the rationale for accepting the exposure. Ensure this is routed through the necessary governance channels.

Evidence cited: DATA:P11, G-rcsa_challenge_guidance#10, G-rcsa_challenge_guidance#5 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#5 (Applicable risk without a control); G-rcsa_challenge_guidance#6 (Control without supporting evidence)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P12: Unauthorized access or fraud (Payment Processing)

- No flags

**Challenge:** The control for unauthorized access or fraud is noted as 'not effective.' Given that there have been no loss events reported, how does the First Line justify the effectiveness of the current controls in mitigating this risk? Additionally, the KRI of overdue access reviews raises concerns about the adequacy of monitoring and alerting mechanisms.

**Questions for the process owner:**
- What specific measures are in place to address the noted ineffectiveness of the control?
- How frequently are access reviews conducted, and what steps are taken to remediate overdue reviews?

**Suggested follow-up:** Consider conducting a thorough review of the access control measures and implementing a plan to enhance their effectiveness. Additionally, ensure that overdue access reviews are addressed promptly to mitigate potential risks.

Evidence cited: DATA:P12, G-rcsa_challenge_guidance#11 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P13: Regulatory non-compliance (Payment Processing)

- No flags

**Challenge:** The RCSA identifies regulatory non-compliance as a risk in the Payment Processing process, yet there are no recorded loss events or findings. This raises questions about the effectiveness of the controls in place and whether they adequately address potential regulatory changes.

**Questions for the process owner:**
- What specific regulatory requirements are applicable to the Payment Processing process?
- How is the monitoring of regulatory changes conducted, and who is responsible for this oversight?
- Can you provide details on any past findings from audits or supervisory reviews related to this risk?

**Suggested follow-up:** Consider providing additional context on how regulatory compliance is maintained and monitored. This could include details on training programs for staff and any recent changes in regulations that may impact the process.

Evidence cited: DATA:P13, G-rcsa_challenge_guidance#12 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P14: Key person dependency (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The RCSA identifies key person dependency as a risk with two historical loss events totaling €7,200, yet no controls are described. This raises concerns about the adequacy of risk management in this area. Additionally, the absence of Key Risk Indicators (KRIs) further complicates the assessment of this risk.

**Questions for the process owner:**
- What measures are in place to mitigate the key person dependency risk?
- Can you provide a rationale for the absence of controls despite the historical loss events?

**Suggested follow-up:** It is recommended to document any existing procedures or knowledge transfer mechanisms related to key person dependency. Additionally, consider implementing appropriate controls and KRIs to better manage this risk.

Evidence cited: DATA:P14, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#13 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

No external research was run.

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 11:59:43 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 11:59:43 | apply_rules | warning | P08: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:59:43 | apply_rules | warning | P09: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:59:43 | apply_rules | warning | P10: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:59:43 | apply_rules | warning | P11: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 11:59:43 | apply_rules | warning | P12: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 11:59:43 | apply_rules | warning | P13: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 11:59:43 | apply_rules | warning | P14: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:59:43 | apply_rules | ok | Rules applied to 7 pairs; 1 high review priority |
| 11:59:43 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 11:59:43 | external_research | skipped | Disabled with --no-external |
| 12:00:02 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-4o-mini); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
