from typing import TypedDict


class ApplicabilityResult(TypedDict):
    pair_id: str
    decision: str
    rationale: str


class RCSAState(TypedDict):
    input_data: list[dict]
    applicability_results: list[ApplicabilityResult]
    scenario_results: list[dict]
    report: dict
    errors: list[str]
