# rag/rag_chain.py

from groq import Groq
from config import GROQ_API_KEY


def generate_answer(query: str, context: str) -> str:
    """
    Generate grounded answer using Groq LLM
    """

    # Safety check
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

    # Initialize Groq client
    client = Groq(api_key=GROQ_API_KEY)

    system_prompt = """
You are a factual AI assistant.

STRICT RULES:
1. Use ONLY the provided context.
2. Do NOT use outside knowledge.
3. If answer is not in context, say:
   "The answer is not available in the provided documents."
4. Always cite sources like:
   [Doc] Title – ChunkX
   [Web] Source Title
"""

    user_prompt = f"""
Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
        max_tokens=1024
    )

    return response.choices[0].message.content.strip()