# rag/vector_store.py

import os
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document as LCDocument

from rag.embeddings import get_embedding_model
from rag.text_splitter import DocumentChunk

VECTOR_STORE_PATH = "vectorstore/faiss_index"


def _convert_chunks_to_lc_docs(chunks: List[DocumentChunk]) -> List[LCDocument]:
    """
    Convert custom DocumentChunk objects into LangChain Documents
    """
    lc_docs = []

    for chunk in chunks:
        lc_docs.append(
            LCDocument(
                page_content=chunk.content,
                metadata=chunk.metadata
            )
        )

    return lc_docs


def index_documents(chunks: List[DocumentChunk]) -> None:
    """
    Create FAISS index and persist locally
    """
    embeddings = get_embedding_model()

    lc_documents = _convert_chunks_to_lc_docs(chunks)

    vector_store = FAISS.from_documents(
        lc_documents,
        embedding=embeddings
    )

    os.makedirs("vectorstore", exist_ok=True)
    vector_store.save_local(VECTOR_STORE_PATH)

    print("✅ FAISS index created and saved.")


def load_faiss_index() -> FAISS:
    """
    Load persisted FAISS index
    """
    embeddings = get_embedding_model()

    if not os.path.exists(VECTOR_STORE_PATH):
        raise FileNotFoundError("FAISS index not found. Run indexing first.")

    return FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )