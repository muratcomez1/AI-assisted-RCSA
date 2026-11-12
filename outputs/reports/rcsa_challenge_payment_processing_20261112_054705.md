# RCSA Challenge Report: Payment Processing

- Generated: 2026-11-12 05:47
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

**Challenge:** The risk is marked applicable, but no control or KRI is described and it was absent from the previous RCSA; two loss events are also recorded. These events warrant inquiry but do not by themselves establish control failure.

**Questions for the process owner:**
- What process, system or environment changes explain the risk’s omission from the previous RCSA, or was that assessment incomplete?
- What were the loss-event causes, and what controls and monitoring address this risk now, including whether any control testing or KRI coverage is available?

**Suggested follow-up:** Ask the owner to explain the RCSA completeness gap and document the current control and monitoring approach, with supporting event analysis where available. Escalate the response for human reviewer assessment.

Evidence cited: DATA:P08, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#2 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P09: Third-party failure (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.

**Challenge:** The risk is marked applicable, but it was absent from the previous RCSA; clarify whether the process, systems or environment changed, or whether the earlier assessment was incomplete (DATA:P09; G-rcsa_challenge_guidance#4). Three loss events are recorded and the control is described as “Not effective”; explain the events’ causes and how they relate to the control without assuming causation. No KRI is assigned, so the monitoring rationale also needs clarification (DATA:P09).

**Questions for the process owner:**
- What changed in the process, systems or environment since the previous RCSA, or was the risk missed in that assessment?
- What were the causes of the recorded loss events, and what evidence supports the control’s current effectiveness status and any remediation?
- Why is no KRI assigned, and how is this risk monitored in its absence?

**Suggested follow-up:** Ask the owner to document the assessment rationale, event analysis, control status and monitoring approach. Refer the RCSA completeness and control-status questions to the human reviewer.

Evidence cited: DATA:P09, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P10: System outage (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** The risk is marked applicable but was not included in the previous RCSA, and no KRI is assigned; please explain the assessment coverage and monitoring approach (DATA:P10; G-rcsa_challenge_guidance#4). A loss event exists while the control is described as effective, which warrants review but does not by itself establish control failure (DATA:P10; G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What changed in the process, systems, or environment, or was the risk omitted from the previous RCSA?
- What was the loss event’s root cause, and what control testing evidence supports the control being described as effective?
- Why is no KRI assigned to this applicable risk?

**Suggested follow-up:** Ask the owner to provide the loss event root cause analysis and control testing evidence, and explain the prior RCSA omission and lack of KRI. Have the human reviewer consider whether the risk assessment and monitoring coverage are complete.

Evidence cited: DATA:P10, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P11: Data quality error (Payment Processing)

- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The RCSA marks data quality error as applicable, but describes no control (DATA:P11; G-rcsa_challenge_guidance#5). The absence of recorded loss events does not establish that the risk is mitigated; please clarify how data quality is managed, including validation, reconciliation and ownership of critical data (DATA:P11; G-rcsa_challenge_guidance#10).

**Questions for the process owner:**
- What controls address data quality errors in Payment Processing, including validation at data entry or reconciliation between systems?
- Who owns critical data and how are data quality exceptions monitored and resolved?

**Suggested follow-up:** Define and assign the relevant control, or document why the exposure is accepted and route that acceptance through the appropriate governance (G-rcsa_challenge_guidance#5).

Evidence cited: DATA:P11, G-rcsa_challenge_guidance#5, G-rcsa_challenge_guidance#10 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#5 (Applicable risk without a control); G-rcsa_challenge_guidance#6 (Control without supporting evidence)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P12: Unauthorized access or fraud (Payment Processing)

- No flags

**Challenge:** The RCSA identifies unauthorized access or fraud as applicable, records the control as not effective, and lists overdue access reviews, although no loss events are recorded (DATA:P12). Please explain the basis for the control assessment and how the access-review issue is being addressed; the absence of losses does not resolve these questions.

**Questions for the process owner:**
- Which access reviews are overdue, what access or roles are in scope, and what is the plan and timeline to complete and document them?
- How are segregation of duties, monitoring and alerting, and authentication strength addressed, and what evidence supports the control assessment?
- Have any recent fraud cases or other relevant incidents informed the assessment? If so, what was learned?

**Suggested follow-up:** Ask the owner to provide evidence supporting the control assessment and details of the overdue-review remediation plan. Use that information to clarify the RCSA rationale and any needed updates.

Evidence cited: DATA:P12, G-rcsa_challenge_guidance#11 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P13: Regulatory non-compliance (Payment Processing)

- No flags

**Challenge:** The risk is marked applicable and was included in the previous RCSA, while the control is recorded as effective; the evidence does not explain the basis for that assessment. Zero recorded loss events does not by itself establish that regulatory non-compliance risk is adequately managed, and the KRI is identified without its status or supporting detail (DATA:P13; G-rcsa_challenge_guidance#12).

**Questions for the process owner:**
- Which legal or supervisory requirements apply, and how are regulatory changes monitored and translated into the payment process?
- What is the current status of the “Open regulatory findings” KRI, and what evidence supports the control’s effective assessment, including relevant audit or supervisory findings and staff training?

**Suggested follow-up:** Provide the applicable requirements, regulatory-change monitoring evidence, KRI status and supporting control evidence for review. Explain any relevant findings and how they inform the control assessment.

Evidence cited: DATA:P13, G-rcsa_challenge_guidance#12 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P14: Key person dependency (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** Key person dependency is recorded as applicable, but no control or KRI is described (DATA:P14). Two historical loss events are recorded; this does not by itself establish that a control failed, so please explain their causes and relevance to the current risk and arrangements (DATA:P14; G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What caused the two loss events, and what root-cause analysis was completed?
- How does the process address reliance on key individuals, including documented procedures, deputies, knowledge transfer and concentration of access rights?
- Why is no control or KRI recorded, and how is key person dependency currently monitored or managed?

**Suggested follow-up:** Please clarify the event analysis and document the current arrangements for managing and monitoring key person dependency, including whether a control or KRI should be recorded. Provide supporting evidence for the human reviewer to assess.

Evidence cited: DATA:P14, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#13 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

No external research was run.

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 05:46:31 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 05:46:31 | apply_rules | warning | P08: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 05:46:31 | apply_rules | warning | P09: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 05:46:31 | apply_rules | warning | P10: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 05:46:31 | apply_rules | warning | P11: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 05:46:31 | apply_rules | warning | P12: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 05:46:31 | apply_rules | warning | P13: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 05:46:31 | apply_rules | warning | P14: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 05:46:31 | apply_rules | ok | Rules applied to 7 pairs; 1 high review priority |
| 05:46:31 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 05:46:31 | external_research | skipped | Disabled with --no-external |
| 05:47:05 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-6-luna); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
