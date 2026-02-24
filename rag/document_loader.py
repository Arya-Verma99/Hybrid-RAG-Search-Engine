# rag/document_loader.py

import os
from typing import List
from uuid import uuid4

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)


class Document:
    """
    Unified internal document schema.
    """

    def __init__(self, source_type: str, title: str, content: str, metadata: dict):
        self.source_id = str(uuid4())
        self.source_type = source_type
        self.title = title
        self.content = content
        self.metadata = metadata


def load_documents_from_directory(directory_path: str) -> List[Document]:
    """
    Load PDFs and text files from a directory.
    Normalize into unified Document schema.
    """

    documents = []

    for filename in os.listdir(directory_path):

        file_path = os.path.join(directory_path, filename)

        # Skip non-files
        if not os.path.isfile(file_path):
            continue

        # ===== PDF =====
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            pages = loader.load()

            for page in pages:
                documents.append(
                    Document(
                        source_type="pdf",
                        title=filename,
                        content=page.page_content,
                        metadata=page.metadata
                    )
                )

        # ===== TXT =====
        elif filename.endswith(".txt"):
            loader = TextLoader(file_path)
            docs = loader.load()

            for doc in docs:
                documents.append(
                    Document(
                        source_type="text",
                        title=filename,
                        content=doc.page_content,
                        metadata=doc.metadata
                    )
                )

    return documents