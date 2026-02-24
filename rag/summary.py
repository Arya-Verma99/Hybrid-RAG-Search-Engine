# rag/summary.py

from typing import List
from groq import Groq
import os


def summarize_documents(query: str, documents: List[str]) -> str:
    """
    Generate concise summaries of top documents
    """

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    combined_docs = "\n\n".join(documents)

    prompt = f"""
Summarize the following documents in relation to the query:

Query: {query}

Documents:
{combined_docs}

Provide concise bullet-point summaries with citations.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content