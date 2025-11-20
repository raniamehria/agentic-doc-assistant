import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from agent.rag import RAGPipeline
from agent.tools import (
    procedural_steps_tool,
    summarize_document_tool,
    generate_admin_letter_tool,
    checklist_tool,
    simplify_explanation_tool,
)

# Charger les variables d'environnement (.env)
load_dotenv()

# Modèle LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Config Streamlit
st.set_page_config(
    page_title="Agentic Document Assistant",
    layout="wide"
)

# ====== STYLE GLOBAL (look clean, Apple-like) ======
st.markdown("""
<style>
body {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text",
                 "Segoe UI", Roboto, sans-serif;
}
.main-title {
    font-size: 34px;
    font-weight: 600;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 4px;
}
.subtitle {
    font-size: 15px;
    text-align: center;
    color: #555;
    margin-bottom: 24px;
}
.section-title {
    font-size: 20px;
    font-weight: 500;
    margin-top: 10px;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Agentic Document Assistant</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>A simple assistant to help young people understand, prepare and manage administrative documents.</div>",
    unsafe_allow_html=True,
)

# ====== SIDEBAR : UPLOAD ======
st.sidebar.header("Upload your document")
uploaded = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

if "rag" not in st.session_state:
    st.session_state["rag"] = RAGPipeline()
    st.session_state["doc_loaded"] = False

if uploaded is not None:
    st.session_state["rag"].load_pdf(uploaded)
    st.session_state["doc_loaded"] = True
    st.sidebar.success("Document successfully processed.")
else:
    st.sidebar.info("Upload a PDF to unlock all actions.")

# ====== ONGLET PRINCIPAUX ======
tab_overview, tab_qa, tab_steps, tab_letter, tab_checklist, tab_simplify = st.tabs(
    [
        " Overview",
        "Q&A on the document",
        " Step-by-step guidance",
        " Generate administrative letter / email",
        " Checklist",
        " Simplified explanation / translation",
    ]
)

# ---------- 1. OVERVIEW / SYNTHÈSE ----------
with tab_overview:
    st.markdown("<div class='section-title'>Automatic overview of the document</div>", unsafe_allow_html=True)

    if not st.session_state["doc_loaded"]:
        st.info("Upload a document in the sidebar to see the overview.")
    else:
        if st.button("Generate overview", key="btn_overview"):
            full_text = st.session_state["rag"].search("")  # récupérer tout le contenu
            answer = summarize_document_tool(full_text, llm)

            st.subheader("Summary")
            st.write(answer.content)

# ---------- 2. Q&A ----------
with tab_qa:
    st.markdown("<div class='section-title'>Ask a question about the document</div>", unsafe_allow_html=True)

    question = st.text_input("Your question:", key="qa_question")

    if st.button("Answer my question", key="btn_qa"):
        if not st.session_state["doc_loaded"]:
            st.warning("Please upload a document first.")
        elif not question.strip():
            st.warning("Please enter a question.")
        else:
            context = st.session_state["rag"].search(question)
            prompt = f"""
You are an assistant specialised in French administrative documents.

Use ONLY the following document extract to answer the question.

CONTEXT:
{context}

QUESTION:
{question}

Give a clear, structured and concise answer.
"""
            answer = llm.invoke(prompt)

            st.subheader("Answer")
            st.write(answer.content)

            st.subheader("Document context used")
            st.write(context)

# ---------- 3. ÉTAPES / GUIDANCE ----------
with tab_steps:
    st.markdown("<div class='section-title'>Step-by-step guidance</div>", unsafe_allow_html=True)

    steps_question = st.text_input(
        "Describe what you need to do (for example: “What are the steps for this appointment?”)",
        key="steps_question"
    )

    if st.button("Generate steps", key="btn_steps"):
        if not st.session_state["doc_loaded"]:
            st.warning("Please upload a document first.")
        elif not steps_question.strip():
            st.warning("Please describe your request.")
        else:
            # On peut donner le texte du document en contexte au tool
            full_text = st.session_state["rag"].search("")
            answer = procedural_steps_tool(steps_question, llm, context=full_text)

            st.subheader("Step-by-step plan")
            st.write(answer.content)

# ---------- 4. LETTRE / MAIL ADMINISTRATIF ----------
with tab_letter:
    st.markdown("<div class='section-title'>Generate an administrative letter or email</div>", unsafe_allow_html=True)

    letter_goal = st.text_area(
        "Explain what you need (example: “Write an email to ask for a new appointment because I missed the first one.”)",
        key="letter_goal",
        height=120
    )

    if st.button("Generate letter / email", key="btn_letter"):
        if not st.session_state["doc_loaded"]:
            st.warning("Upload a document first, so the letter can reuse the right information.")
        elif not letter_goal.strip():
            st.warning("Please describe your situation.")
        else:
            full_text = st.session_state["rag"].search("")
            answer = generate_admin_letter_tool(letter_goal, full_text, llm)

            st.subheader("Proposed letter / email")
            st.write(answer.content)

# ---------- 5. CHECKLIST ----------
with tab_checklist:
    st.markdown("<div class='section-title'>Checklist of documents and actions</div>", unsafe_allow_html=True)

    checklist_goal = st.text_input(
        "For which administrative task do you want a checklist ?",
        key="checklist_goal"
    )

    if st.button("Generate checklist", key="btn_checklist"):
        if not st.session_state["doc_loaded"]:
            st.warning("Upload a document first.")
        elif not checklist_goal.strip():
            st.warning("Please describe the task.")
        else:
            full_text = st.session_state["rag"].search("")
            answer = checklist_tool(checklist_goal, full_text, llm)

            st.subheader("Checklist")
            st.write(answer.content)

# ---------- 6. EXPLICATION SIMPLIFIÉE / TRADUCTION ----------
with tab_simplify:
    st.markdown("<div class='section-title'>Simplified explanation or translation</div>", unsafe_allow_html=True)

    mode = st.selectbox(
        "Choose the style:",
        [
            "Simple French (young audience)",
            "Formal French",
            "English",
        ],
        key="simplify_mode"
    )

    if st.button("Generate simplified explanation", key="btn_simplify"):
        if not st.session_state["doc_loaded"]:
            st.warning("Upload a document first.")
        else:
            full_text = st.session_state["rag"].search("")
            answer = simplify_explanation_tool(full_text, llm, mode)

            st.subheader("Simplified explanation")
            st.write(answer.content)
