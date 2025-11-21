# Agentic Document Assistant

## 1. Introduction
The Agentic Document Assistant is an end-to-end AI system designed to help users analyze administrative documents, understand procedures, extract key information, and generate relevant administrative content.  
It combines Retrieval-Augmented Generation (RAG), LLM-based reasoning, and an agentic workflow with specialized tools.

The project is fully implemented in Python using Streamlit for the user interface.

This work meets all requirements of the assignment:
- Chat interface with LLM
- Hot RAG with PDF upload
- Source-based answers
- Multi-tool agentic reasoning
- Conversation history
- Clean repository structure
- Professional documentation
- Reproducible execution instructions

---

## 2. Features

### 2.1 Document Upload and RAG
- PDF upload through the sidebar
- Automatic extraction and splitting
- Embedding and vector search (FAISS)
- Context-aware answers using retrieved chunks

### 2.2 Question Answering
- Ask any question related to the uploaded document
- Structured answer from the LLM
- Display of the exact document chunks used

### 2.3 Automatic Document Summary
- Global overview of the PDF
- Concise and structured summarization

### 2.4 Step-by-Step Guidance
- Generates a procedural plan related to the user’s goal
- Uses both the document context and the user’s instructions

### 2.5 Administrative Letter or Email Generator
- Generates formal letters and emails
- Automatically reuses data extracted from the document

### 2.6 Checklist Generator
- Produces an itemized administrative checklist
- Designed as a to-do list (checkbox-style)

### 2.7 Simplified Explanation or Translation
- Reformulation in simple French
- Reformulation in formal French
- Translation to English

### 2.8 Conversation History
- Full interaction history saved in `st.session_state`
- Displayed in real time in the sidebar

### 2.9 Agent Architecture Diagram
A notebook (`agent_architecture.ipynb`) generates an agentic workflow graph, representing:
- initial LLM reasoning
- routing logic
- tool selection branches
- termination conditions

---
## 4. Installation

### 4.1 Clone the repository
```bash
git clone https://github.com/raniamehria/agentic-doc-assistant.git
cd agentic-doc-assistant


