
import streamlit as st
from pypdf import PdfReader
from docx import Document
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

load_dotenv()

# UI 
st.set_page_config(page_title="RAG Chat App", layout="wide")
st.title("📄 RAG Chat App (Chat + History)")

# Session State 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Helpers 
def read_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def read_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def read_txt(file):
    return file.read().decode("utf-8")

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

# Vector DB 
@st.cache_resource
def load_vector_db():
    client = chromadb.Client()
    embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    collection = client.get_or_create_collection(
        name="rag_collection",
        embedding_function=embedder
    )
    return collection

collection = load_vector_db()

# Upload 
st.sidebar.header("📂 Upload Documents")
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF, TXT, DOCX",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

if uploaded_files and st.sidebar.button("Process Documents"):
    with st.spinner("Processing documents..."):
        doc_id = collection.count()
        for file in uploaded_files:
            if file.type == "application/pdf":
                text = read_pdf(file)
            elif file.type == "text/plain":
                text = read_txt(file)
            else:
                text = read_docx(file)

            chunks = chunk_text(text)
            for chunk in chunks:
                collection.add(
                    documents=[chunk],
                    ids=[f"doc_{doc_id}"]
                )
                doc_id += 1
    st.sidebar.success("Documents indexed successfully!")

# Chat Display 
st.subheader("💬 Chat")

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Chat Input 
query = st.chat_input("Ask a question from your documents...")

if query:
    
    st.session_state.chat_history.append({"role": "user", "content": query})

    
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])

    answer = f"Based on the uploaded documents, here is the relevant information:\n\n{context}"

    st.session_state.chat_history.append({"role": "assistant", "content": answer})

    st.rerun()