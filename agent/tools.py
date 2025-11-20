from langchain_openai import ChatOpenAI


def procedural_steps_tool(question: str, llm: ChatOpenAI | None = None, context: str | None = None):
    """
    Génère des étapes claires pour une démarche administrative.
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4o-mini")

    base_context = context or ""
    prompt = f"""
You are an assistant specialised in French administrative processes.

CONTEXT (optional, from the document):
{base_context}

USER REQUEST:
{question}

Write a clear, numbered step-by-step plan to help the user.
Each step should be short and actionable.
"""
    return llm.invoke(prompt)


def summarize_document_tool(full_text: str, llm: ChatOpenAI | None = None):
    """
    Synthèse du document : résumé + points essentiels.
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are an assistant specialised in French administrative letters and convocations.

Summarize the following document in French:
- Give a short global summary.
- Then list 3 to 7 key points (date, place, obligations, deadlines, etc.).
- Finish with a short sentence: "What should the user do now?"

DOCUMENT:
{full_text}
"""
    return llm.invoke(prompt)


def generate_admin_letter_tool(goal: str, full_text: str, llm: ChatOpenAI | None = None):
    """
    Génère une lettre / un mail administratif en français.
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are an assistant that writes formal French administrative letters and emails.

DOCUMENT CONTEXT (optional, convocations, appointments, etc.):
{full_text}

USER GOAL:
{goal}

Write a complete letter or email in French:
- polite and formal
- with the right structure (object, introduction, body, polite closing formula)
- adapt the content to the user's goal.
"""
    return llm.invoke(prompt)


def checklist_tool(goal: str, full_text: str, llm: ChatOpenAI | None = None):
    """
    Génère une checklist (documents à fournir, actions à faire).
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are an assistant helping a young person prepare an administrative task.

DOCUMENT CONTEXT:
{full_text}

TASK:
{goal}

Create a checklist in French with bullets:
- documents to bring or prepare
- online steps (if any)
- things to check before the appointment
- things to do after the appointment (if relevant)
"""
    return llm.invoke(prompt)


def simplify_explanation_tool(full_text: str, llm: ChatOpenAI | None = None, mode: str = "Simple French (young audience)"):
    """
    Explique le document avec un ton différent (simple FR, formel, anglais).
    """
    if llm is None:
        llm = ChatOpenAI(model="gpt-4o-mini")

    if mode == "Formal French":
        style = "formal French, as in an official letter, but still clear."
        language = "French"
    elif mode == "English":
        style = "clear and simple English."
        language = "English"
    else:
        style = "very simple French, like you explain to a teenager, with short sentences."
        language = "French"

    prompt = f"""
Explain the following administrative document in {language}.

Use this style: {style}

DOCUMENT:
{full_text}
"""
    return llm.invoke(prompt)
