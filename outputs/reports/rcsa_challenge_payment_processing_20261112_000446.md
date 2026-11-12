# RCSA Challenge Report: Payment Processing

- Generated: 2026-11-12 00:04
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

**Challenge:** The risk is marked applicable, but no control or KRI is described and it was absent from the previous RCSA, raising questions about assessment completeness and risk monitoring (DATA:P08; G-rcsa_challenge_guidance#4). Two loss events totaling €5,800 are recorded; these warrant inquiry but do not by themselves establish that a control failed (DATA:P08; G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What were the causes of the recorded events, and what controls were in place at the time or are now intended to address this risk?
- What changed in the process, systems or environment—or was the earlier assessment incomplete—and what is the rationale for having no KRI? 

**Suggested follow-up:** Ask the owner to document the event analysis, control arrangements, rationale for the missing KRI and prior RCSA omission. Refer the completeness and coverage questions to the human reviewer.

Evidence cited: DATA:P08, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P09: Third-party failure (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.

**Challenge:** The risk is marked applicable, but it was absent from the previous RCSA and has no assigned KRI; clarify whether the earlier assessment was incomplete or the process, systems, or environment changed (DATA:P09; G-rcsa_challenge_guidance#4). Three loss events are recorded and the control is described as “Not effective”; their causes and relationship to the control need clarification before the reviewer can assess the entry (DATA:P09).

**Questions for the process owner:**
- What changed in the process, systems, or environment, or was the risk omitted from the previous RCSA?
- What were the causes of the three loss events, how do they relate to the control, and what is the rationale for having no KRI assigned?

**Suggested follow-up:** Document the explanation for the RCSA gap and the loss-event/control relationship. Consider whether the risk entry, control description, and KRI coverage need updating.

Evidence cited: DATA:P09, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P10: System outage (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** System outage is marked applicable but was absent from the previous RCSA, and no KRI is assigned; please clarify the assessment’s completeness and monitoring rationale (DATA:P10; G-rcsa_challenge_guidance#4). A loss event is recorded while the control is described as effective, which warrants review but does not by itself establish control failure (DATA:P10; G-rcsa_challenge_guidance#2).

**Questions for the process owner:**
- What changed in the process, systems or environment since the previous RCSA, or was the risk omitted from that assessment?
- What is the rationale for having no KRI assigned to this applicable risk?
- What did the event root cause analysis identify, and what control testing evidence supports the control’s effectiveness, including whether the event predated or had a different cause from the control?

**Suggested follow-up:** Ask the owner to provide the rationale and supporting evidence, then have the human reviewer assess the RCSA completeness, monitoring approach and control description. Do not infer control failure from the loss event alone.

Evidence cited: DATA:P10, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#4 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P11: Data quality error (Payment Processing)

- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The risk is marked applicable and was included in the previous RCSA, but no control is described; the absence of recorded loss events does not establish that exposure is addressed (DATA:P11; G-rcsa_challenge_guidance#5). For this data quality risk, clarify how data entry validation, system reconciliations and ownership of critical data are addressed (G-rcsa_challenge_guidance#10).

**Questions for the process owner:**
- What controls address data quality errors, including validation at entry, reconciliation between systems and ownership of critical data?
- Who owns these controls, and what evidence or review demonstrates they operate as intended?

**Suggested follow-up:** Define and assign relevant controls, or document why the exposure is accepted and route that acceptance through the appropriate governance (G-rcsa_challenge_guidance#5).

Evidence cited: DATA:P11, G-rcsa_challenge_guidance#5, G-rcsa_challenge_guidance#10 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#5 (Applicable risk without a control); G-rcsa_challenge_guidance#6 (Control without supporting evidence)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P12: Unauthorized access or fraud (Payment Processing)

- No flags

**Challenge:** The RCSA records unauthorized access or fraud as applicable and the control as “Not effective,” with overdue access reviews identified as a KRI; the absence of recorded loss events does not establish that the risk is absent (DATA:P12). Please clarify the basis for the control assessment and how access reviews, segregation of duties, and monitoring address both external attacks and internal misuse (DATA:P12; G-rcsa_challenge_guidance#11).

**Questions for the process owner:**
- What is driving the overdue access reviews, which access populations are affected, and what is the plan and timeline to complete and evidence the reviews?
- What evidence supports the “Not effective” assessment, and what monitoring, segregation-of-duties, or authentication measures currently mitigate unauthorized access or fraud? 

**Suggested follow-up:** Update the RCSA rationale with the basis for the control assessment and current evidence, and document actions and ownership for addressing overdue reviews. Consider whether related safeguards and monitoring are adequately described.

Evidence cited: DATA:P12, G-rcsa_challenge_guidance#11 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P13: Regulatory non-compliance (Payment Processing)

- No flags

**Challenge:** The RCSA identifies regulatory non-compliance as applicable and the control as effective, but the evidence provided does not describe the control or substantiate its effectiveness. No recorded loss events do not establish that the risk is adequately controlled; the stated KRI, “Open regulatory findings,” has no reported status here (DATA:P13).

**Questions for the process owner:**
- Which legal or supervisory requirements apply to Payment Processing, and how are regulatory changes identified, assessed and implemented?
- What evidence supports the control’s effectiveness, including the status of open regulatory findings, relevant audit or supervisory findings, and staff training? 

**Suggested follow-up:** Provide the control description and supporting evidence, including current KRI status and relevant findings and training information, for Second Line review. Reassess the effectiveness rationale in light of that evidence.

Evidence cited: DATA:P13, G-rcsa_challenge_guidance#12 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P14: Key person dependency (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** The risk is recorded as applicable, with two historical loss events, but no control or KRI is described (DATA:P14). Please clarify the incidents’ causes and whether the current assessment reflects the process’s reliance on key individuals; the events alone do not establish control failure (DATA:P14; G-rcsa_challenge_guidance#2; G-rcsa_challenge_guidance#13).

**Questions for the process owner:**
- What were the causes of the two loss events, and what actions followed?
- How is key person dependency mitigated, including through documented procedures, deputies, knowledge transfer or access-rights management?
- Why is no KRI assigned, and how is ongoing exposure monitored?
- What evidence supports the current assessment of this risk?

**Suggested follow-up:** Ask the owner to clarify the loss-event causes and document relevant mitigations and monitoring, including the rationale for having no KRI. Refer the response and supporting evidence to the human reviewer for consideration.

Evidence cited: DATA:P14, G-rcsa_challenge_guidance#2, G-rcsa_challenge_guidance#13 (challenge source: llm)
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

No external research was run.

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 00:04:11 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 00:04:11 | apply_rules | warning | P08: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 00:04:11 | apply_rules | warning | P09: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 00:04:11 | apply_rules | warning | P10: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 00:04:11 | apply_rules | warning | P11: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 00:04:11 | apply_rules | warning | P12: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 00:04:11 | apply_rules | warning | P13: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 00:04:11 | apply_rules | warning | P14: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 00:04:11 | apply_rules | ok | Rules applied to 7 pairs; 1 high review priority |
| 00:04:11 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 00:04:11 | external_research | skipped | Disabled with --no-external |
| 00:04:46 | llm_challenge | ok | 7/7 challenges written by the LLM (gpt-6-luna); 0 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
