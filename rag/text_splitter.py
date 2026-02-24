# rag/text_splitter.py

from typing import List, Dict, Any
from uuid import uuid4
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.document_loader import Document


class DocumentChunk:
    """
    Represents a chunk of a parent document.
    """

    def __init__(
        self,
        source_id: str,
        source_type: str,
        title: str,
        content: str,
        metadata: Dict[str, Any],
        chunk_index: int,
    ):
        self.chunk_id = str(uuid4())
        self.source_id = source_id
        self.source_type = source_type
        self.title = title
        self.content = content
        self.chunk_index = chunk_index

        # Merge parent metadata with chunk-specific metadata
        self.metadata = {
            **metadata,
            "chunk_id": self.chunk_id,
            "chunk_index": chunk_index,
            "source_id": source_id,
            "source_type": source_type,
            "title": title,
        }

    def __repr__(self):
        return f"<DocumentChunk {self.chunk_id} | {self.title} | chunk {self.chunk_index}>"



def chunk_documents(
    documents: List[Document],
    chunk_size: int = 800,
    chunk_overlap: int = 150,
) -> List[DocumentChunk]:
    """
    Splits documents into overlapping chunks using RecursiveCharacterTextSplitter.

    Each chunk preserves:
    - source_id
    - source_type
    - title
    - parent metadata
    - chunk index
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks: List[DocumentChunk] = []

    for doc in documents:
        split_texts = splitter.split_text(doc.content)

        for idx, text in enumerate(split_texts):
            chunk = DocumentChunk(
                source_id=doc.source_id,
                source_type=doc.source_type,
                title=doc.title,
                content=text,
                metadata=doc.metadata,
                chunk_index=idx,
            )
            chunks.append(chunk)

    return chunks