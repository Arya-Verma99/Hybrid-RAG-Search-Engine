# rag/query_router.py

from typing import Literal


QueryType = Literal["document", "web", "hybrid"]


REALTIME_KEYWORDS = [
    "latest",
    "current",
    "recent",
    "today",
    "news",
    "update",
    "developments"
]


def classify_query(query: str) -> QueryType:
    """
    Classify query into:
    - document
    - web
    - hybrid
    """

    query_lower = query.lower()

    is_realtime = any(word in query_lower for word in REALTIME_KEYWORDS)

    if is_realtime and "compare" in query_lower:
        return "hybrid"

    if is_realtime:
        return "web"

    return "document"