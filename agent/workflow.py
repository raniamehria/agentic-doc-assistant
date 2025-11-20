from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from agent.tools import rag_search_tool, procedural_steps_tool
from agent.state import AgentState

def create_workflow():
    """
    Nouveau workflow LangGraph (API 2024+)
    """

    graph = StateGraph(state_schema=AgentState)
    llm = ChatOpenAI(model="gpt-4o-mini")

    def analyze_intent(state):
        question = state.input

        if any(word in question.lower() for word in ["step", "procédure", "procedure", "comment faire", "étapes"]):
            state.tool = "steps"
        else:
            state.tool = "rag"

        return state

    def run_tool(state):
        question = state.input

        if state.tool == "rag":
            state.output = rag_search_tool(question, {"rag": state.rag})
        else:
            state.output = procedural_steps_tool(question, llm)

        return state

    def generate_answer(state):
        question = state.input
        context = state.output

        prompt = f"""
        Use the following context to answer the question:

        CONTEXT:
        {context}

        QUESTION:
        {question}

        Provide a clear and helpful answer:
        """

        response = llm.invoke(prompt)
        state.final_answer = response
        return state

    graph.add_node("analyze", analyze_intent)
    graph.add_node("tool", run_tool)
    graph.add_node("answer", generate_answer)

    graph.set_entry_point("analyze")
    graph.add_edge("analyze", "tool")
    graph.add_edge("tool", "answer")

    graph.set_finish_point("answer")

    return graph
