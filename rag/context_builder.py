# rag/context_builder.py

from typing import List, Dict
from langchain_core.documents import Document as LCDocument


MAX_CONTEXT_CHARS = 8000


def build_context(
    doc_chunks: List[LCDocument],
    web_results: List[Dict]
) -> str:
    """
    Combine document + web content into final RAG context
    """

    context_parts = []
    total_length = 0

    # Add document chunks
    for doc in doc_chunks:
        text = f"[Doc] {doc.metadata.get('title')} - Chunk {doc.metadata.get('chunk_index')}\n{doc.page_content}\n\n"

        if total_length + len(text) > MAX_CONTEXT_CHARS:
            break

        context_parts.append(text)
        total_length += len(text)

    # Add web results
    for web in web_results:
        text = f"[Web] Tavily: {web['title']}\n{web['content']}\nSource: {web['url']}\n\n"

        if total_length + len(text) > MAX_CONTEXT_CHARS:
            break

        context_parts.append(text)
        total_length += len(text)

    return "\n".join(context_parts)