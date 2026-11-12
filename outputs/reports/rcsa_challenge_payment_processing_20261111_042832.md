# RCSA Challenge Report: Payment Processing

- Generated: 2026-11-11 04:28
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

**Challenge:** Historical loss events exist for this process-risk pair. Risk is applicable but was not included in the previous RCSA. Risk is applicable but no KRI is assigned. Risk is applicable but no control is described.

**Questions for the process owner:**
- What were the root causes of the recorded loss events and have they been addressed?
- Why was this risk not covered in the previous RCSA, and what changed since?
- Which KRI could monitor this risk, and who would own it?
- Which control mitigates this risk, and who owns it?

**Suggested follow-up:** Review the loss events with the owner. Confirm the risk is added to the current RCSA.

Evidence cited: DATA:P08 (challenge source: deterministic_fallback)
Note: LLM not used in this run
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P09: Third-party failure (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.

**Challenge:** Historical loss events exist for this process-risk pair. Risk is applicable but was not included in the previous RCSA. Risk is applicable but no KRI is assigned.

**Questions for the process owner:**
- What were the root causes of the recorded loss events and have they been addressed?
- Why was this risk not covered in the previous RCSA, and what changed since?
- Which KRI could monitor this risk, and who would own it?

**Suggested follow-up:** Review the loss events with the owner. Confirm the risk is added to the current RCSA.

Evidence cited: DATA:P09 (challenge source: deterministic_fallback)
Note: LLM not used in this run
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA); G-rcsa_challenge_guidance#2 (Loss events and effective controls)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P10: System outage (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- RCSA_GAP: Risk is applicable but was not included in the previous RCSA.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- CONTROL_CONFLICT: Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Challenge:** Historical loss events exist for this process-risk pair. Risk is applicable but was not included in the previous RCSA. Risk is applicable but no KRI is assigned. Control is described as Effective although loss events exist. Not automatic proof of control failure; needs human review.

**Questions for the process owner:**
- What were the root causes of the recorded loss events and have they been addressed?
- Why was this risk not covered in the previous RCSA, and what changed since?
- Which KRI could monitor this risk, and who would own it?
- Why is the control rated Effective although loss events exist? What testing evidence supports the rating?

**Suggested follow-up:** Review the loss events with the owner. Confirm the risk is added to the current RCSA.

Evidence cited: DATA:P10 (challenge source: deterministic_fallback)
Note: LLM not used in this run
Guidance retrieved: G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#4 (Risk missing from the previous RCSA)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P11: Data quality error (Payment Processing)

- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** Risk is applicable but no control is described.

**Questions for the process owner:**
- Which control mitigates this risk, and who owns it?

**Suggested follow-up:** Ask the owner to define and assign a control.

Evidence cited: DATA:P11 (challenge source: deterministic_fallback)
Note: LLM not used in this run
Guidance retrieved: G-rcsa_challenge_guidance#10 (Data quality error); G-rcsa_challenge_guidance#5 (Applicable risk without a control); G-rcsa_challenge_guidance#6 (Control without supporting evidence)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P12: Unauthorized access or fraud (Payment Processing)

- No flags

**Challenge:** No challenge points were raised by the deterministic rules.

**Suggested follow-up:** No follow-up required beyond standard review.

Evidence cited: DATA:P12 (challenge source: deterministic_fallback)
Note: LLM not used in this run
Guidance retrieved: G-rcsa_challenge_guidance#11 (Unauthorized access or fraud); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P13: Regulatory non-compliance (Payment Processing)

- No flags

**Challenge:** No challenge points were raised by the deterministic rules.

**Suggested follow-up:** No follow-up required beyond standard review.

Evidence cited: DATA:P13 (challenge source: deterministic_fallback)
Note: LLM not used in this run
Guidance retrieved: G-rcsa_challenge_guidance#12 (Regulatory non-compliance)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

### P14: Key person dependency (Payment Processing)

- LOSS_EVENTS_PRESENT: Historical loss events exist for this process-risk pair.
- NO_KRI_COVERAGE: Risk is applicable but no KRI is assigned.
- NO_CONTROL: Risk is applicable but no control is described.

**Challenge:** Historical loss events exist for this process-risk pair. Risk is applicable but no KRI is assigned. Risk is applicable but no control is described.

**Questions for the process owner:**
- What were the root causes of the recorded loss events and have they been addressed?
- Which KRI could monitor this risk, and who would own it?
- Which control mitigates this risk, and who owns it?

**Suggested follow-up:** Review the loss events with the owner. Agree a suitable KRI with the owner.

Evidence cited: DATA:P14 (challenge source: deterministic_fallback)
Note: LLM not used in this run
Guidance retrieved: G-rcsa_challenge_guidance#1 (Challenging a not applicable response); G-rcsa_challenge_guidance#2 (Loss events and effective controls); G-rcsa_challenge_guidance#13 (Key person dependency)

Reviewer decision: [ ] accept  [ ] request evidence  [ ] escalate

## 4. External context (context only, not proof of internal control effectiveness)

No external research was run.

## 5. Run log

| Time | Node | Status | Detail |
|---|---|---|---|
| 04:28:32 | validate_input | ok | Loaded 7 process-risk pairs from data/rcsa_synthetic_data.csv |
| 04:28:32 | apply_rules | warning | P08: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 04:28:32 | apply_rules | warning | P09: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 04:28:32 | apply_rules | warning | P10: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 04:28:32 | apply_rules | warning | P11: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 04:28:32 | apply_rules | warning | P12: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 04:28:32 | apply_rules | warning | P13: source 'KRI flag'=Y differs from the computed KRI coverage gap (False) |
| 04:28:32 | apply_rules | warning | P14: source 'KRI flag'=N differs from the computed KRI coverage gap (True) |
| 04:28:32 | apply_rules | ok | Rules applied to 7 pairs; 1 high review priority |
| 04:28:32 | retrieve_evidence | ok | Retrieved guidance for 7 pairs from 13 chunks |
| 04:28:32 | external_research | skipped | Disabled with --no-external |
| 04:28:32 | llm_challenge | degraded | 0/7 challenges written by the LLM (gpt-4.1-mini); 7 deterministic fallback |

## 6. Limitations

- Synthetic data. No real bank records are used.
- No numeric inherent or residual risk scores are produced.
- A loss event alone does not prove a control failure.
- Challenge text from the LLM is a draft for human review.
