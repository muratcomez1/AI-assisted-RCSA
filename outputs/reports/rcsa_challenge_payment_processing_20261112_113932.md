# RCSA Challenge Report: Payment Processing

- Generated: 2026-11-12 11:39
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

**Challenge:** The risk is marked applicable, but no control is described and no KRI is assigned; two historical loss events are also recorded for this process-risk pair (DATA:P08). Because the risk was absent from the previous RCSA, please clarify whether the earlier assessment was incomplete or the process, systems, or environment changed (G-rcsa_challenge_guidance#4). The loss events warrant inquiry but do not by themselves establish control failure (G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What changed in the process, systems, or environment, or was the risk omitted from the previous RCSA?
- What were the causes of the recorded loss events, and what controls and monitoring address this risk now? If none are in place, what is the rationale?

**Suggested follow-up:** Ask the owner to document the risk’s inclusion rationale, loss-event causes, and current control and monitoring arrangements. Have the reviewer consider whether the prior RCSA gap and absence of a described control or KRI need follow-up.

Evidence cited: DATA:P08, G-rcsa_challenge_guidance#4, G-rcsa_challenge_guidance#2 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P09: Third-party failure (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.

**Challenge:** Third-party failure is marked applicable, but it was absent from the previous RCSA and has no assigned KRI; clarify the assessment’s completeness and monitoring rationale. The record also reports three loss events totaling €10,800 and describes the control as “Not effective”; these facts warrant review but do not by themselves establish the events’ causes or the control’s role.

**Questions for the process owner:**
- What changed in the process, systems, or environment since the previous RCSA, or was the earlier assessment incomplete?
- What were the causes of the reported loss events, how do they relate to the control described as “Not effective,” and what monitoring or remediation is in place, including the rationale for having no KRI?

**Suggested follow-up:** Ask the owner to document the rationale for the RCSA change and lack of KRI, and provide event root-cause and control follow-up evidence for human review.

Evidence cited: DATA:P09, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P10: System outage (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** The risk is marked applicable, but it was not included in the previous RCSA and has no assigned KRI (DATA:P10). A loss event is recorded while the control is described as effective; this does not establish control failure, but warrants review of the event’s cause and control evidence (DATA:P10; G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What was the root cause of the loss event, and what control testing evidence supports the effectiveness assessment?
- What changed in the process, systems or environment, or was the earlier assessment incomplete; and how was the decision not to assign a KRI reached?

**Suggested follow-up:** Ask the owner to explain the RCSA gap and KRI decision, and provide the event analysis and relevant control testing evidence for human review.

Evidence cited: DATA:P10, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P11: Data quality error (Payment Processing)

- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The risk is marked applicable and was included in the previous RCSA, but no control is described for data quality errors (DATA:P11). The absence of reported loss events does not establish that the exposure is addressed; clarify how data errors are prevented or detected, including validation, reconciliation and ownership of critical data (G-rcsa_challenge_guidance#10).

**Questions for the process owner:**
- What controls address data quality errors, and who owns them?
- How are data quality exceptions identified, investigated and resolved, and what evidence supports this process?

**Suggested follow-up:** Define and assign the relevant controls, or document why the exposure is accepted and route that acceptance through the appropriate governance (G-rcsa_challenge_guidance#5).

Evidence cited: DATA:P11, G-rcsa_challenge_guidance#10, G-rcsa_challenge_guidance#5 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#5 (Applicable risk without a control); G-rcsa_challenge_guidance#6 (Control without supporting evidence)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P12: Unauthorized access or fraud (Payment Processing)

- No flags

**Challenge:** The RCSA identifies unauthorized access or fraud as applicable and records the control as “Not effective,” with overdue access reviews as the KRI; no loss events are recorded, but that does not establish whether exposure is adequately managed (DATA:P12). Please clarify the control issue and how access reviews, segregation of duties, and monitoring address external attacks and internal misuse (G-rcsa_challenge_guidance#11).

**Questions for the process owner:**
- What has caused access reviews to be overdue, and what remediation, interim safeguards, and completion evidence are in place?
- How are segregation of duties and monitoring and alerting applied to detect or prevent unauthorized access or fraud?

**Suggested follow-up:** Document the control gap, its cause, and the remediation and interim safeguards, with supporting evidence. Clarify how the KRI is monitored and escalated while reviews remain overdue.

Evidence cited: DATA:P12, G-rcsa_challenge_guidance#11 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P13: Regulatory non-compliance (Payment Processing)

- No flags

**Challenge:** R6 is marked applicable and was included in the previous RCSA, while the control is recorded as effective. Although no loss events are reported, the KRI is “Open regulatory findings” and its status and supporting evidence are not provided; absence of losses alone does not substantiate control effectiveness (DATA:P13).

**Questions for the process owner:**
- Which requirements apply to Payment Processing, and who monitors regulatory changes and communicates them to staff?
- What is the current status of the open-findings KRI, and what audit or supervisory findings, remediation evidence, and staff training support the effectiveness assessment? (DATA:P13; G-rcsa_challenge_guidance#12)

**Suggested follow-up:** Provide the current KRI status and evidence supporting the control assessment, including relevant findings, remediation, regulatory-change monitoring, and training. Clarify the RCSA assessment if that evidence does not support the recorded effectiveness.

Evidence cited: DATA:P13, G-rcsa_challenge_guidance#12 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P14: Key person dependency (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The risk is marked applicable, but no control or KRI is described, while two loss events totaling EUR 7,200 are recorded for this process-risk pair (DATA:P14). These events do not by themselves establish a control failure; please explain their causes and how key person dependency is managed, including procedures, deputies, knowledge transfer and access concentration (G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#13).

**Questions for the process owner:**
- What caused the two recorded loss events, and is there root-cause analysis or relevant control-testing evidence?
- How is reliance on key individuals mitigated—for example, through documented procedures, deputies, knowledge transfer or management of access rights?
- Why is no KRI assigned, and what monitoring is used to identify increasing key person dependency?

**Suggested follow-up:** Please document the event analysis, key person mitigants and rationale for the lack of a KRI, and update the RCSA or supporting evidence as appropriate for human review.

Evidence cited: DATA:P14, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#13 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

No external research was run.

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 11:39:00 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 11:39:00 | apply_rules | warning | P08: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:39:00 | apply_rules | warning | P09: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:39:00 | apply_rules | warning | P10: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:39:00 | apply_rules | warning | P11: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 11:39:00 | apply_rules | warning | P12: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 11:39:00 | apply_rules | warning | P13: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 11:39:00 | apply_rules | warning | P14: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 11:39:00 | apply_rules | ok | Rules applied to 7 pairs; 1 high review priority |
| 11:39:00 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 11:39:00 | external_research | skipped | Disabled with --no-external |
| 11:39:32 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-6-luna); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
