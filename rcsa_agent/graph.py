"""LangGraph workflow: validate -> rules -> retrieve -> external research -> LLM challenge -> report -> finalize.

If input validation fails, a conditional edge skips straight to finalize so a failure report is still saved.
"""
from langgraph.graph import END, START, StateGraph

from . import nodes
from .state import RCSAState


def build_graph():
    g = StateGraph(RCSAState)
    g.add_node("validate_input", nodes.validate_input)
    g.add_node("apply_rules", nodes.apply_rules)
    g.add_node("retrieve_evidence", nodes.retrieve_evidence)
    g.add_node("external_research", nodes.external_research)
    g.add_node("llm_challenge", nodes.llm_challenge)
    g.add_node("build_report", nodes.build_report)
    g.add_node("finalize", nodes.finalize)

    g.add_edge(START, "validate_input")
    g.add_conditional_edges("validate_input", nodes.route_after_validation,
                            {"continue": "apply_rules", "abort": "finalize"})
    g.add_edge("apply_rules", "retrieve_evidence")
    g.add_edge("retrieve_evidence", "external_research")
    g.add_edge("external_research", "llm_challenge")
    g.add_edge("llm_challenge", "build_report")
    g.add_edge("build_report", "finalize")
    g.add_edge("finalize", END)
    return g.compile()
