# RCSA Challenge Report: Payment Processing

- Generated: 2026-11-12 13:33
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
- NO_KRI_COVERAGE: Loss events exist but no KRI is assigned to monitor this risk.
- NO_CONTROL: Risk is applicable but no control is described.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** The risk is marked applicable, but no control is described and the risk was not included in the previous RCSA; two loss events are also recorded, with no KRI assigned. These facts warrant clarification of the control environment and assessment completeness, but the loss events alone do not establish that a control failed.

**Questions for the process owner:**
- What controls, if any, address this risk, and what evidence supports their operation and effectiveness during the relevant periods?
- What were the causes of the recorded loss events, and what changed in the process, systems or environment—or was the earlier RCSA incomplete—that explains the risk’s omission?
- How is this risk currently monitored, and what is the rationale for having no assigned KRI?

**Suggested follow-up:** Ask the owner to document the loss-event analysis, relevant control evidence, monitoring approach and rationale for the prior RCSA omission. Refer the resulting explanation to the human reviewer for assessment.

Evidence cited: DATA:P08, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P09: Third-party failure (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Loss events exist but no KRI is assigned to monitor this risk.
- CONTROL_NOT_EFFECTIVE: The control is described as Not effective.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** The RCSA identifies third-party failure as applicable, records three loss events totalling €10,800, and describes the control as “Not effective”; no KRI is assigned. The risk was also absent from the previous RCSA, so the control status and assessment completeness merit clarification, without assuming the loss events prove control failure. [DATA:P09; G-rcsa_challenge_guidance#2; G-rcsa_challenge_guidance#4]

**Questions for the process owner:**
- What were the root causes of the loss events, and how do they relate to the control’s stated effectiveness?
- What evidence supports the “Not effective” assessment, and what actions or control testing are planned or completed?
- Why was no KRI assigned, and what changed—or was missed—that led to this risk being absent from the previous RCSA?

**Suggested follow-up:** Request the owner’s root-cause analysis, control testing evidence, rationale for the KRI gap, and explanation of the prior-RCSA omission. Have the reviewer assess the responses and whether the RCSA needs updating.

Evidence cited: DATA:P09, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P10: System outage (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Loss events exist but no KRI is assigned to monitor this risk.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** For Payment Processing, R3 is marked applicable and the control is described as effective, while one loss event (€4,300) is recorded and no KRI is assigned. The risk was not included in the previous RCSA; these facts warrant clarification but do not by themselves establish control failure or explain the earlier omission (DATA:P10; G-rcsa_challenge_guidance#2; G-rcsa_challenge_guidance#4).

**Questions for the process owner:**
- What was the loss event’s root cause, and what control testing evidence supports the effective assessment, including whether the event predated the control or had a different cause?
- What changed in the process, systems or environment—or was the earlier assessment incomplete—and how is this risk monitored without an assigned KRI?

**Suggested follow-up:** Request the root cause analysis, relevant control testing evidence, and an explanation for the prior RCSA omission. Ask the owner to consider documenting the risk’s monitoring approach and whether KRI coverage is appropriate.

Evidence cited: DATA:P10, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P11: Data quality error (Payment Processing)

- NO_CONTROL: Risk is applicable but no control is described.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** The assessment marks data quality error as applicable and lists no control, while the risk was also included in the previous RCSA (DATA:P11). Please clarify how validation at data entry, reconciliation between systems, and ownership of critical data are addressed; the scenario indicates residual exposure remains equal to inherent exposure until a control is defined (G-rcsa_challenge_guidance#10, G-rcsa_challenge_guidance#5).

**Questions for the process owner:**
- What controls, if any, validate data at entry or reconcile data between systems, and how are they assigned and evidenced?
- Who owns critical data, and how are data quality exceptions monitored and resolved? (DATA:P11; G-rcsa_challenge_guidance#10)

**Suggested follow-up:** Define and assign relevant controls, or document why the exposure is accepted and route that acceptance through appropriate governance (G-rcsa_challenge_guidance#5).

Evidence cited: DATA:P11, G-rcsa_challenge_guidance#10, G-rcsa_challenge_guidance#5 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#5 (Applicable risk without a control)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P12: Unauthorized access or fraud (Payment Processing)

- CONTROL_NOT_EFFECTIVE: The control is described as Not effective.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** DATA:P12 identifies unauthorized access or fraud as applicable, reports overdue access reviews, and describes the control as “Not effective.” Clarify the basis for that status and how the overdue reviews affect access-risk coverage; the absence of loss events does not by itself resolve these questions.

**Questions for the process owner:**
- What access reviews are overdue, what is their current status, and what is the plan and target date to complete them?
- What is the latest control testing or review evidence, and how do segregation of duties, monitoring and alerting, and authentication address this risk?
- Who owns the remediation, and how will its completion and effectiveness be evidenced?

**Suggested follow-up:** Request supporting review and testing evidence and a remediation plan from the owner, then have the human reviewer assess whether the RCSA description and action are adequately supported.

Evidence cited: DATA:P12, G-rcsa_challenge_guidance#11, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#6 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#6 (Control without supporting evidence)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P13: Regulatory non-compliance (Payment Processing)

- No flags

**Challenge:** The reduced, accepted residual and “Effective” control designation are not substantiated by control details or the status of the “Open regulatory findings” KRI in the evidence provided. The absence of recorded loss events does not by itself establish that the control is effective or that residual risk is reduced (DATA:P13).

**Questions for the process owner:**
- Which legal or supervisory requirements apply, and how are regulatory changes monitored and translated into process controls?
- What is the current status of open regulatory findings, and what evidence supports the control’s effectiveness, including audit or supervisory findings and staff training?
- What evidence supports the reduction in residual risk and its acceptance? 

**Suggested follow-up:** Provide the applicable requirements, regulatory-change monitoring arrangements, current KRI status, and evidence supporting control effectiveness and the residual-risk decision for reviewer assessment (G-rcsa_challenge_guidance#12).

Evidence cited: DATA:P13, G-rcsa_challenge_guidance#12 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P14: Key person dependency (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- NO_KRI_COVERAGE: Loss events exist but no KRI is assigned to monitor this risk.
- NO_CONTROL: Risk is applicable but no control is described.
- ACTION_REQUIRED: Action required: there is no control or the control is not effective.

**Challenge:** For Payment Processing, the risk is marked applicable and two loss events are recorded, but no control or KRI is described (DATA:P14). Please clarify the events’ causes and whether any controls or monitoring were in place; the events alone do not establish control failure (G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What were the root causes of the two loss events, and what control measures address key person dependency?
- What measurable indicator could monitor this exposure, who would own it, and what threshold would trigger escalation?

**Suggested follow-up:** Update the RCSA with the owner’s explanation of the events, relevant controls, and KRI decision. If a KRI is appropriate, document its owner and escalation threshold (G-rcsa_challenge_guidance#3).

Evidence cited: DATA:P14, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#3 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#3 (Missing KRI coverage)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

No external research was run.

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 13:33:23 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 13:33:23 | apply_rules | ok | Rules applied to 7 pairs; 1 high review priority |
| 13:33:23 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 13:33:23 | external_research | skipped | Disabled with --no-external |
| 13:33:55 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-6-luna); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
