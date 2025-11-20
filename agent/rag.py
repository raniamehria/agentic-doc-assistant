from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from PyPDF2 import PdfReader

class RAGPipeline:
    def __init__(self):
        self.vectorstore = None

    def load_pdf(self, file):
        """
        Charge un PDF et le transforme en base vectorielle
        """

        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        chunks = splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        self.vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

    def search(self, query):
        """
        Recherche les passages les plus pertinents via similarité vectorielle
        """

        if not self.vectorstore:
            return "Aucun document chargé."

        docs = self.vectorstore.similarity_search(query, k=3)
        return "\n\n".join([d.page_content for d in docs])
