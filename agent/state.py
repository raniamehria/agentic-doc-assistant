from pydantic import BaseModel

class AgentState(BaseModel):
    """
    Structure de l'état partagé dans le workflow LangGraph.
    """
    input: str = ""
    rag: object = None
    tool: str = ""
    output: str = ""
    final_answer: str = ""
