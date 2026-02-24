# app.py

import streamlit as st
import os

import os
from dotenv import load_dotenv

load_dotenv()

print("GROQ KEY:", os.getenv("GROQ_API_KEY"))
print("TAVILY KEY:", os.getenv("TAVILY_API_KEY"))
from rag.document_loader import load_documents_from_directory
from rag.text_splitter import chunk_documents
from rag.vector_store import index_documents
from rag.retriever import semantic_search
from rag.query_router import classify_query
from rag.context_builder import build_context
from rag.rag_chain import generate_answer
from rag.summary import summarize_documents
from web_search.tavily_search import tavily_web_search


st.set_page_config(page_title="Hybrid RAG Search Engine", layout="wide")

st.title("🔀 Hybrid RAG Search Engine")

# =============================
# SIDEBAR – DOCUMENT MANAGEMENT
# =============================

st.sidebar.header("📂 Document Management")

uploaded_files = st.sidebar.file_uploader(
    "Upload Documents",
    accept_multiple_files=True
)

use_web = st.sidebar.toggle("Enable Tavily Web Search 🌐", value=True)


if st.sidebar.button("Index Documents"):
    if uploaded_files:
        os.makedirs("data/uploads", exist_ok=True)

        for file in uploaded_files:
            with open(f"data/uploads/{file.name}", "wb") as f:
                f.write(file.read())

        documents = load_documents_from_directory("data/uploads")
        chunks = chunk_documents(documents)
        index_documents(chunks)

        st.sidebar.success("✅ Documents indexed successfully.")
    else:
        st.sidebar.warning("Upload documents first.")


# =============================
# MAIN CHAT INTERFACE
# =============================

query = st.chat_input("Ask your question...")

if query:

    query_type = classify_query(query)

    doc_results = []
    web_results = []

    if query_type in ["document", "hybrid"]:
        doc_results = semantic_search(query)

    if query_type in ["web", "hybrid"] and use_web:
        web_results = tavily_web_search(query)

    context = build_context(doc_results, web_results)

    answer = generate_answer(query, context)

    # Visual Indicator
    if query_type == "document":
        st.markdown("📄 **Document-based Answer**")
    elif query_type == "web":
        st.markdown("🌐 **Web-based Answer**")
    else:
        st.markdown("🔀 **Hybrid Answer**")

    # =============================
    # TABS FOR TRANSPARENCY
    # =============================

    tab1, tab2, tab3 = st.tabs(["🧠 Answer", "📄 Document Evidence", "🌐 Web Evidence"])

    with tab1:
        st.write(answer)

    with tab2:
        if doc_results:
            for doc in doc_results:
                st.markdown(f"**{doc.metadata.get('title')} - Chunk {doc.metadata.get('chunk_index')}**")
                st.write(doc.page_content)
                st.divider()
        else:
            st.write("No document evidence used.")

    with tab3:
        if web_results:
            for web in web_results:
                st.markdown(f"**{web['title']}**")
                st.write(web["content"])
                st.markdown(f"[Source]({web['url']})")
                st.divider()
        else:
            st.write("No web evidence used.")

    # =============================
    # TOP-N SUMMARY
    # =============================

    if doc_results:
        st.subheader("📌 Top Document Summaries")

        doc_texts = [doc.page_content for doc in doc_results]
        summary = summarize_documents(query, doc_texts)

        st.write(summary)