from langgraph.graph import StateGraph
from orchestration.state import NeuroState
from orchestration.nodes import (
    planner_node,
    sleep_node,
    bio_node,
    analyst_node,
    guardrail_node,
    report_node
)

def build_graph():
    builder = StateGraph(NeuroState)

    # Nodes
    builder.add_node("planner", planner_node)
    builder.add_node("sleep", sleep_node)
    builder.add_node("bio", bio_node)
    builder.add_node("analyst", analyst_node)
    builder.add_node("guardrail", guardrail_node)
    builder.add_node("report", report_node)

    # Entry point
    builder.set_entry_point("planner")

    # Conditional routing
    builder.add_conditional_edges(
        "planner",
        route_sleep,
        {
            "sleep": "sleep",
            "bio": "bio"
        }
    )

    builder.add_edge("sleep", "bio")

    builder.add_conditional_edges(
        "bio",
        route_bio,
        {
            "bio": "bio",
            "analyst": "analyst"
        }
    )

    builder.add_edge("analyst", "guardrail")
    builder.add_edge("guardrail", "report")

    return builder.compile()
def route_sleep(state):
    if state["plan"].get("run_sleep"):
        return "sleep"
    return "bio"


def route_bio(state):
    return "analyst"
