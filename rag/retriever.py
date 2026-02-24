# rag/retriever.py

from typing import List
from langchain_core.documents import Document as LCDocument
from rag.vector_store import load_faiss_index


def semantic_search(query: str, top_k: int = 5) -> List[LCDocument]:
    """
    Perform semantic search across indexed documents
    """
    vector_store = load_faiss_index()

    results = vector_store.similarity_search(
        query,
        k=top_k
    )

    return results