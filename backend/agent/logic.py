from backend.agent.state import AgentState

required_field = ["client_name", "discussion_topic", "meeting_date", "action_item"]

def Agent_Logic(state : AgentState):
    if state.status == 'new' :
        state.status == 'processing'

        state.extracted = {
            "client_name" : "person or company",
            "discussion_topic" : "business",
            "meeting_date" : "date",
            "action_item" : "next_step or commitment"
        }

    state.missing_field = [
        field for field in required_field
        if field not in state.extracted
    ]

    state.status = 'done'
        
     
    return state
