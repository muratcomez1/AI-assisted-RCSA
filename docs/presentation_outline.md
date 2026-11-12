# Presentation outline (6 to 7 minutes) and demo script

Rule: business first, little technical detail. Practise once with a timer. Stop at 6:30.

## Slides (6 slides, about 4.5 minutes) + live demo (about 1.5 minutes)

**1. The problem (0:45)**
RCSA is manual and slow: First Line owners self-assess, then Second Line has to check every answer against loss events, KRIs and the previous RCSA. Inconsistent, repetitive, months of meetings.

**2. The solution (0:45)**
An autonomous agent: one command, then it compares answers with evidence, raises flags, drafts challenge questions and writes a report. A human reviews at the end. The agent never rates risk or approves controls.

**3. How it works (1:00)**
Show the 7-node flow. Python decides the facts (flags from my 22 scenarios), the LLM only drafts the wording and must cite its sources. Local retrieval of guidance. Say one sentence on why LangGraph: shared state and a decision point.

**4. Reliability (0:45)**
Three tools: OpenAI, GDELT, Tavily. Timeouts, retries, validation, explicit status. No silent failures. Fallback if the LLM fails. Tests: the rules reproduce all 22 scenarios.

**5. Results (0:45)**
Two reports (Payment Processing, Vendor Onboarding). Example: P10, control "Effective" but a loss event exists. The agent flags it for review and says this does not prove control failure.

**6. Next steps / GTM (0:30)**
Sprint 1 interviews with risk teams, Sprint 2 pilot, Sprint 3 enterprise governance. Next feature: the owner enters only the process description and steps, and the agent proposes the risks.

## Live demo script (1:30)
1. Terminal: `python run_rcsa.py --process "Payment Processing" --no-external` (about 35 seconds, talk while it runs).
2. Open the new report. Show the Overview table and the P10 challenge.
3. Scroll to the Run log: every step has a status.
4. Optional: `python run_rcsa.py --data nope.csv` to show the failure report.

## Backup plan
If anything fails live: say "I will show the report from my earlier run" and open the saved report.
Do not debug in front of the group. Close `.env` and other windows before you start.

## Honest lines to say if asked
- "The data is synthetic."
- "The code was built with an AI assistant; I ran, tested and checked it."
- "GDELT can rate-limit; the agent reports that clearly instead of hiding it."
