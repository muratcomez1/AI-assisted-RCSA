"""Shared LangGraph state. Every node reads from it and returns only the keys it changes."""
import operator
from typing import Annotated, TypedDict


class RCSAState(TypedDict, total=False):
    # inputs (set by the CLI)
    data_path: str
    process: str          # process name, or "ALL"
    use_llm: bool
    use_external: bool
    out_dir: str

    # produced by the nodes
    pairs: list           # normalised process-risk pairs
    findings: list        # one dict per pair: pair, flags, guidance, challenge ...
    external: dict        # results of the external tools (Wikipedia, Tavily)
    report_md: str
    report_path: str
    log_path: str
    status: str           # COMPLETED / COMPLETED_WITH_WARNINGS / FAILED
    fatal_error: str

    # append-only log: every node adds entries, nothing is overwritten
    run_log: Annotated[list, operator.add]
