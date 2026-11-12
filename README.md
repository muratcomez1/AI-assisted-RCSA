# AI-Assisted RCSA Evidence & Challenge Agent

An autonomous agent that supports Second Line Operational Risk reviewers. It takes a completed
First Line Risk and Control Self-Assessment (RCSA), compares the answers with the evidence
(loss events, KRIs, previous RCSA, controls), raises challenge flags with deterministic rules,
drafts challenge questions with an LLM, and writes a structured RCSA Challenge Report.

**Governance principle:** the agent supports the reviewer. It does not rate risk, approve controls
or decide compliance. No numeric risk scores are produced. Every report is marked
"Pending human review". All data in this repository is synthetic.

## How it works

One command starts a LangGraph workflow with seven nodes:

```
validate_input --(error)--> finalize
       |
apply_rules -> retrieve_evidence -> external_research -> llm_challenge -> build_report -> finalize
```

| Node | What it does |
|---|---|
| validate_input | Loads the CSV (or a Google Sheet published as CSV), checks columns, selects the process |
| apply_rules | Deterministic rules based on the 22-scenario matrix (flags, scenario result, review priority) |
| retrieve_evidence | Local retrieval of challenge guidance (`knowledge/`), every chunk has a citable source id |
| external_research | GDELT DOC API and Tavily Search with timeouts, retries and explicit status |
| llm_challenge | OpenAI drafts the challenge, questions and follow-up, citing only supplied evidence ids |
| build_report | Builds the Markdown report |
| finalize | Saves the report and a JSON run log, sets the run status |

**Reliability:** every tool call has a status (`ok`, `empty`, `failed`, `skipped`). If the LLM fails,
a labelled deterministic fallback is used. If the input is wrong, a failure report is still written.
Nothing fails silently.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env     # then add your keys
```

`.env` (never commit it):

```
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4o-mini
TAVILY_API_KEY=...            # optional
RCSA_SHEET_URL=...            # optional: Google Sheet published as CSV
```

## Run

```bash
python run_rcsa.py                                   # Payment Processing, LLM + external tools
python run_rcsa.py --process "Vendor Onboarding"
python run_rcsa.py --no-external                     # skip GDELT and Tavily
python run_rcsa.py --no-llm --no-external            # offline dry run
python run_rcsa.py --data path/to/file.csv           # or a published Google Sheet CSV link
```

Reports and run logs are saved in `outputs/reports/`.

## Input

One row per process-risk pair (`data/rcsa_synthetic_data.csv`). The business owner answers
`Applicable` and `Control`; loss events, KRI and previous RCSA come from company systems.

## Tests

```bash
python -m pytest -q tests/test_rcsa_agent.py
```

The tests include a check that the rules reproduce all 22 scenarios.

## Project structure

```
rcsa_agent/   state, loaders, rules, retrieval, external tools, LLM, report, nodes, graph
knowledge/    challenge guidance used for retrieval (synthetic, illustrative)
data/         synthetic RCSA data and scenarios
docs/         stack decision, GTM sprints
tests/        automated tests and fixtures
run_rcsa.py   one-command trigger
```

## Limitations

- Synthetic data only. The guidance corpus is illustrative, not an official methodology.
- No numeric inherent or residual scores. A loss event alone does not prove a control failure.
- A Google Sheet published to the web is readable by anyone with the link. Real data would need
  the Sheets API with a service account.
- External sources give context only. GDELT may rate-limit requests; the agent reports this.

## Documents

- `docs/stack_decision.md`
- `docs/gtm_future_sprints.md`
