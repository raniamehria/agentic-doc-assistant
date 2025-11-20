import streamlit as st

def layout():
    st.set_page_config(page_title="Agentic Document Assistant", layout="wide")

    st.markdown(
        "<h1 style='text-align:center;'>📄 Agentic Document Assistant</h1>",
        unsafe_allow_html=True
    )

    st.sidebar.header("📄 Upload your document")
    file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

    st.markdown("### ❓ Ask a question about the document")
    question = st.text_input("Your question:")

    run = st.button("Run Agent")

    return file, question, run
