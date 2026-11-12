# RCSA Challenge Report: Vendor Onboarding

- Generated: 2026-11-12 05:38
- Run status: **COMPLETED_WITH_WARNINGS**
- Data: synthetic demonstration data only
- Review: **human Second Line review required**. Approval: **Pending**
- This report supports a reviewer. It does not rate risk, approve controls or decide compliance.

## 1. Summary

- Process-risk pairs analysed: 7 (6 marked applicable by the First Line)
- High review priority: none
- Flags raised: NOT_APPLICABLE_ACCEPTED x1, NO_CONTROL x2, NO_KRI_COVERAGE x3, RCSA_GAP x3

## 2. Overview

| Pair | Process | Risk | Applicable | Loss events | KRI | Prev. RCSA | Control | Flags | Source expected result | Review priority |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Vendor Onboarding | R1 Process execution error | No | 0 (0 EUR) | - | N | n/a | NOT_APPLICABLE_ACCEPTED | Not applicable - accepted | low |
| P02 | Vendor Onboarding | R2 Third-party failure | Yes | 0 (0 EUR) | - | Y | None | NO_KRI_COVERAGE, NO_CONTROL | High - residual = inherent | medium |
| P03 | Vendor Onboarding | R3 System outage | Yes | 0 (0 EUR) | - | Y | Not effective | NO_KRI_COVERAGE | High - action required | medium |
| P04 | Vendor Onboarding | R4 Data quality error | Yes | 0 (0 EUR) | - | Y | Effective | NO_KRI_COVERAGE | Residual reduced, accepted | medium |
| P05 | Vendor Onboarding | R5 Unauthorized access or fraud | Yes | 0 (0 EUR) | Overdue access reviews | N | None | RCSA_GAP, NO_CONTROL | High - residual = inherent | medium |
| P06 | Vendor Onboarding | R6 Regulatory non-compliance | Yes | 0 (0 EUR) | Open regulatory findings | N | Not effective | RCSA_GAP | High - action required | medium |
| P07 | Vendor Onboarding | R7 Key person dependency | Yes | 0 (0 EUR) | Staff turnover % | N | Effective | RCSA_GAP | Residual reduced, accepted | medium |

## 3. Detailed challenges

### P01: Process execution error (Vendor Onboarding)

- NOT_APPLICABLE_ACCEPTED: Marked not applicable and no contradicting evidence was found.

**Challenge:** The not-applicable response has no contradicting evidence in the information provided, so the basis for it is not disproven. However, the absence of loss events, a KRI, a prior RCSA entry or a described control does not by itself establish that process execution error is not applicable; please confirm the process scope and rationale (DATA:P01; G-rcsa_challenge_guidance#1).

**Questions for the process owner:**
- Which Vendor Onboarding steps, if any, involve manual execution, handoffs or procedures, and how do these inform the not-applicable decision?
- Was the risk absent from the previous RCSA because the process or its scope changed, or should the earlier assessment be revisited?

**Suggested follow-up:** Document the owner’s scope-based rationale for the not-applicable response and revisit the assessment if the process includes relevant execution steps or the prior assessment was incomplete.

Evidence cited: DATA:P01, G-rcsa_challenge_guidance#1, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#7 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#7 (Process execution error)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P02: Third-party failure (Vendor Onboarding)

- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** R2 is marked applicable, but no control or KRI is described, despite the risk appearing in the previous RCSA (DATA:P02). Please clarify how third-party failure is managed, including whether critical vendors, service-level reporting, exit plans and provider concentration are considered (G-rcsa_challenge_guidance#8).

**Questions for the process owner:**
- Which controls address vendor outages, service-level breaches or insolvency, and who owns them?
- How is exposure monitored, including through service-level reporting or other indicators, and what is the rationale for having no KRI? 

**Suggested follow-up:** Document and assign the relevant control and monitoring approach, or explain why the exposure is accepted and route that acceptance through appropriate governance (G-rcsa_challenge_guidance#5).

Evidence cited: DATA:P02, G-rcsa_challenge_guidance#8, G-rcsa_challenge_guidance#5 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#8 (Third-party failure); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#5 (Applicable risk without a control)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P03: System outage (Vendor Onboarding)

- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.

**Challenge:** System outage is recorded as applicable, and the control is described as “Not effective”; clarify the basis for that assessment and how the process would recover from an outage. No KRI is assigned, so there is no identified indicator for monitoring changes in exposure between assessments (DATA:P03; G-rcsa_challenge_guidance#9; G-rcsa_challenge_guidance#3).

**Questions for the process owner:**
- What recovery time objectives, failover arrangements, and test evidence apply to Vendor Onboarding, and what dependencies or change-management risks could affect recovery?
- Which measurable indicator could signal changing outage exposure, who would own it, and what threshold would trigger escalation?
- What is the rationale for recording the control as “Not effective,” and what remediation or monitoring is planned?

**Suggested follow-up:** Ask the owner to clarify the control assessment and recovery arrangements, and propose an indicator with an owner and escalation threshold. Document the rationale and any agreed follow-up in the RCSA.

Evidence cited: DATA:P03, G-rcsa_challenge_guidance#9, G-rcsa_challenge_guidance#3 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#9 (System outage); G-rcsa_challenge_guidance#3 (Missing KRI coverage); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P04: Data quality error (Vendor Onboarding)

- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.

**Challenge:** Data quality error is identified as applicable, but no KRI is assigned, limiting monitoring between RCSAs (DATA:P04; G-rcsa_challenge_guidance#3). Please substantiate the “Effective” control assessment with evidence of data-entry validation, reconciliation, and ownership of critical data (G-rcsa_challenge_guidance#10).

**Questions for the process owner:**
- What measurable indicator could signal a change in data-quality exposure, who would own it, and what threshold would trigger escalation?
- What evidence supports the control assessment, including validation at data entry, reconciliation between systems, and ownership of critical data? Have there been any relevant data incidents to consider?

**Suggested follow-up:** Provide the control evidence and consider assigning an appropriate KRI, with an owner and escalation threshold. Document the rationale if no suitable indicator is identified.

Evidence cited: DATA:P04, G-rcsa_challenge_guidance#3, G-rcsa_challenge_guidance#10 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#3 (Missing KRI coverage); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P05: Unauthorized access or fraud (Vendor Onboarding)

- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** R5 is marked applicable but was not included in the previous RCSA, and no control is described. The overdue access reviews KRI warrants clarification of how access risks are managed; zero recorded loss events do not resolve these questions.

**Questions for the process owner:**
- What changed in the process, systems or environment, or was the previous RCSA incomplete?
- What controls address unauthorized access or fraud, including access reviews, segregation of duties, monitoring and alerting, and authentication strength?
- How are overdue access reviews identified and followed up?

**Suggested follow-up:** Clarify the prior RCSA omission and document the relevant controls and how the overdue access reviews KRI is managed. Reassess the RCSA entry based on the owner’s explanation.

Evidence cited: DATA:P05, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#11 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P06: Regulatory non-compliance (Vendor Onboarding)

- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.

**Challenge:** R6 is marked applicable but was absent from the previous RCSA; what changed in the process, systems or environment, or was the earlier assessment incomplete? The reported control status is “Not effective”; please clarify the basis for that assessment and how the risk is currently managed. Zero loss events do not by themselves establish that the risk is absent.

**Questions for the process owner:**
- Which legal or supervisory requirements apply to Vendor Onboarding, and who monitors regulatory change, audit or supervisory findings, and staff training?
- Why was R6 omitted from the previous RCSA, and what evidence supports the current control status and any planned response?

**Suggested follow-up:** Document the rationale for the prior RCSA omission and the current applicability assessment. Clarify the control-status basis and provide supporting evidence for the reviewer’s assessment.

Evidence cited: DATA:P06, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#12, G-rcsa_challenge_guidance#1 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#12 (Regulatory non-compliance); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P07: Key person dependency (Vendor Onboarding)

- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.

**Challenge:** R7 is marked applicable but was not included in the previous RCSA, so the completeness gap needs explanation (DATA:P07; G-rcsa_challenge_guidance#4). The control is recorded as effective, but the evidence provided does not show how dependency on key individuals is managed or how that conclusion was reached (DATA:P07; G-rcsa_challenge_guidance#13).

**Questions for the process owner:**
- What changed in the process, systems or environment, and was the earlier RCSA incomplete?
- What evidence supports the control’s effectiveness, including documented procedures, deputies, knowledge transfer, recent absences or departures, and concentration of access rights?

**Suggested follow-up:** Ask the owner to explain the prior RCSA omission and provide evidence supporting the current control assessment. Consider whether the RCSA documentation should be updated based on that explanation.

Evidence cited: DATA:P07, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#13 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#13 (Key person dependency); G-rcsa_challenge_guidance#1 (Challenging a not applicable response)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

No external research was run.

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 05:38:05 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 05:38:05 | apply_rules | warning | P02: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 05:38:05 | apply_rules | warning | P03: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 05:38:05 | apply_rules | warning | P04: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 05:38:05 | apply_rules | warning | P05: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 05:38:05 | apply_rules | warning | P06: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 05:38:05 | apply_rules | warning | P07: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 05:38:05 | apply_rules | ok | Rules applied to 7 pairs; 0 high review priority |
| 05:38:05 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 05:38:05 | external_research | skipped | Disabled with --no-external |
| 05:38:36 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-6-luna); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
