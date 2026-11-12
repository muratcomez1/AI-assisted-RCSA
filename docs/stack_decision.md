# Stack decision

## Orchestrator: LangGraph
The RCSA challenge process has several stages that share data (process, risk pairs, evidence, flags, external context, report). It also has a decision point: if the input is invalid, the workflow must stop and still produce a failure report. LangGraph fits this because the shared state, the nodes and the conditional edge are explicit, so every step can be tested and logged. n8n would suit simple trigger-and-notify flows, but not this stateful, rule-plus-LLM logic. n8n could be added later for notifications or the production trigger.

## Responsibilities
| Layer | Technology | Why |
|---|---|---|
| Orchestration | LangGraph (7-node graph, conditional edge) | Explicit state, testable steps |
| Facts and rules | Plain Python | Reproducible, testable, no numeric scores invented |
| Challenge drafting | OpenAI API (model configurable with OPENAI_MODEL) | Drafts wording only, cites supplied evidence ids |
| Retrieval (RAG) | Local retriever over knowledge/ (TF-IDF style, source ids) | Small corpus; no vector database needed |
| External research | GDELT DOC API and Tavily Search API | Public news and web context |
| Input | CSV file or Google Sheet published as CSV | Business owner fills a sheet |
| Output | Markdown report and JSON run log | Easy to review and audit |
| Version control | Git, GitHub | Daily pushes |

## RAG justification
RAG is used, locally. The corpus is a small set of challenge guidance written for this prototype, so a hosted vector database such as Pinecone would add setup and failure points without improving accuracy. Every retrieved chunk keeps a source id so the report can cite it. Retrieved guidance is illustrative, not an official methodology.

## Reliability design
- Required-input validation and a clear failure report when the input is wrong.
- External tools: timeout, up to 3 attempts, response validation, explicit status (ok, empty, failed, skipped).
- LLM: JSON validation, removal of cited ids that were not supplied, two attempts, then a deterministic fallback that is labelled in the report.
- No silent failures: every degraded step appears in the run log and the report.

## Governance
The agent never assigns numeric risk scores, approves controls or decides compliance. Every report is marked "Pending human review". Data is synthetic.
