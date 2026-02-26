from langraph.graph import StateGraph, END
from backend.agent.logic import Agent_logic
from backend.agent.state import AgentState


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("logic_node", Agent_logic)
    graph.set_entry_point('logic_node')
    graph.add_edge('logic_node', END)

    graph.compile()


