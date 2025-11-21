# Agentic Document Assistant

An AI-powered assistant designed to help users understand, summarize, and process administrative documents in France.  
It supports RAG-based question answering, step-by-step guidance, automated letter generation, checklists, simplified explanations, and full conversation history.

---

## 1. Overview

The application allows a user to:

- Upload a PDF administrative document  
- Ask questions about its content (RAG-powered Q&A)  
- Generate summaries  
- Produce procedural step-by-step guidance  
- Create administrative letters/emails  
- Generate checklists (with checkbox formatting)  
- Request simplified explanations (Simple French, Formal French, English)  
- View the conversation history in a persistent sidebar  
- Visualize the internal agent workflow through a LangGraph diagram  

Built using **Streamlit**, **LangChain**, **OpenAI**, and **FAISS**.

---

## 2. Features

### **2.1 PDF Upload & Processing**
The uploaded PDF is parsed using **PyPDF2** and embedded into a **FAISS vector store**.

### **2.2 RAG Question Answering**
Retrieves relevant chunks from the vector database and uses an LLM to answer user questions.

### **2.3 Document Summary**
Provides a clean, structured summary of the uploaded document.

### **2.4 Step-by-Step Guidance**
Generates a procedural plan based on the user request and document context.

### **2.5 Administrative Letter / Email Generation**
Produces formal emails or letters using contextual information.

### **2.6 Checklist Generation**
Creates a checklist formatted like a to-do list (checkboxes included).

### **2.7 Simplified Explanation / Translation**
Outputs a simplified version of the document content:
- Simple French  
- Formal French  
- English  

### **2.8 Conversation History**
All interactions (Q&A, steps, checklists, etc.) are saved to `st.session_state` and displayed in the sidebar.

### **2.9 Agent Architecture Diagram**
A Jupyter Notebook (`agent_architecture.ipynb`) generates a LangGraph diagram showing:

- Start node  
- LLM reasoning  
- RAG retrieval  
- Tool routing  
- Branching logic (“continue” / “done”)  
- End node  

---

## 3. Project Structure

```
agentic-doc-assistant/
│
├── agent/
│   ├── rag.py               # RAG pipeline (FAISS + embeddings)
│   ├── tools.py             # Tools: steps, summary, letter, checklist…
│   ├── workflow.py          # Agent workflow logic
│   ├── state.py             # State object
│
├── ui/
│   ├── interface.py
│
├── agent_architecture.ipynb # Notebook generating the agent diagram
├── app.py                   # Streamlit application
├── requirements.txt
├── .env                     # API key (excluded from repo)
└── README.md
```

---

## 4. Installation

### **4.1 Clone the repository**
```bash
git clone https://github.com/raniamehria/agentic-doc-assistant.git
cd agentic-doc-assistant
```

### **4.2 Create and activate a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate     # macOS / Linux
# OR
.venv\Scripts\activate        # Windows
```

### **4.3 Install dependencies**
```bash
pip install -r requirements.txt
```

### **4.4 Configure environment variables**
Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

*(The `.env` file is ignored by GitHub for security.)*

---

## 5. Running the Application

### **5.1 Launch Streamlit**
```bash
streamlit run app.py
```

Then open the displayed local URL (usually `http://localhost:8501/`).

---

## 6. Agent Pipeline (Workflow Logic)

The internal flow follows:

1. **Start**  
2. **LLM node**  
3. **RAG retrieval tool**  
4. **Tool selection logic**  
5. **Branches** based on the output:  
   - continue → call additional tools  
   - done → terminate  
6. **End**

A visual diagram is generated in the notebook `agent_architecture.ipynb`.

---

## 7. Tech Stack

- **Python 3.10+**  
- **Streamlit** (UI)  
- **LangChain** (LLM orchestration & tools)  
- **FAISS CPU** (vector store)  
- **OpenAI API**  
- **PyPDF2** (PDF parsing)  
- **LangGraph** (agent workflow visualization)  

---

## 10. Business Value & Real-World Impact

The Agentic Document Assistant addresses a recurring challenge faced by students, young adults, and professionals in France: the complexity and opacity of administrative procedures.  
Its value proposition combines **automation**, **clarity**, and **accessibility**, transforming a traditionally time-consuming experience into an intuitive workflow.

### **10.1 Problem Addressed**
Administrative documents are often:
- Difficult to interpret
- Time-consuming to process manually
- Stressful for individuals unfamiliar with bureaucratic language
- Dependent on external help (associations, advisors, family members)

This creates delays, errors, and missed opportunities (appointments, deadlines, benefits).

### **10.2 Value Proposition**
The assistant provides **immediate, personalised, and actionable support** by automating document interpretation and procedural guidance.

Its main business value pillars are:

#### **✓ Efficiency**
- Reduces the time required to understand a document from *hours* to *seconds*.
- Produces structured outputs (summaries, steps, checklists) ready for action.
- Eliminates manual search for administrative requirements.

#### **✓ Accessibility**
- Makes administrative processes easier for young people, newcomers, non-native French speakers, and individuals with limited literacy or digital familiarity.

#### **✓ Reliability**
- Ensures consistency in interpretation thanks to RAG (retrieves only the document’s content).
- Decreases risk of administrative mistakes (missing documents, incomplete emails, forgotten steps).

#### **✓ Scalability**
The architecture is modular:
- Tools can be extended to support new document types (CAF, Préfecture, CPAM, universities…)
- Vector database can be enriched with reusable public resources (guides, templates)
- Could be integrated into institutions, student services, HR departments, or legal aid platforms.

### **10.3 Potential Use Cases**
- **Student services**: Help newcomers process enrollment documents, visa requirements, scholarships.
- **HR departments**: Contract explanations, onboarding checklists, administrative forms.
- **Public institutions**: Improve accessibility of citizen-facing documents.
- **Startups / SaaS tools**: Embedded administrative AI assistant for clients.
- **Associations / legal aid**: Support vulnerable populations without increasing workload.

### **10.4 Competitive Advantage**
Unlike generic chatbots or LLM assistants, this project leverages:
- **RAG** to guarantee document-grounded answers  
- **Specialized administrative tools** (letters, steps, checklists)  
- **Agentic routing logic**, not a single static LLM prompt  
- **A clean UI**, accessible to non-technical users  

This positions the tool as a **practical productivity assistant** rather than a generic conversational model.

---

## 11. Conclusion

The Agentic Document Assistant demonstrates how modern LLMs, combined with retrieval and structured agentic logic, can transform the way individuals interact with administrative documents.  
By providing clarity, guidance, and automation, the system significantly reduces the friction, stress, and time typically associated with bureaucratic tasks.

The project highlights:
- the practical value of agentic workflows,
- the efficiency of document-grounded reasoning (RAG),
- and the impact of a clear, user-friendly interface.

This assistant represents a solid foundation for future extensions such as multi-document workflows, enriched vector databases, specialized administrative knowledge bases, or integration into public and private services.  
It showcases how AI can meaningfully simplify everyday life and support users in handling essential but complex administrative procedures.




## Authors

- **Julia Randriatsimivony**  
- **Rania Mehria**  
- **Rym Belouahri**

ALBERT SCHOOL

---

## License

This project is provided for academic purposes.

