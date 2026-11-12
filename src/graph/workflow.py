from langgraph.graph import StateGraph, END

from src.graph.state import RCSAState
from src.graph.validate_input import validate_input


def build_graph():
    graph = StateGraph(RCSAState)

    graph.add_node("validate_input", validate_input)

    graph.set_entry_point("validate_input")
    graph.add_edge("validate_input", END)

    return graph.compile()
