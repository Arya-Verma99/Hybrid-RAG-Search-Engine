# web_search/tavily_search.py

import os
from typing import List, Dict
from tavily import TavilyClient


def tavily_web_search(query: str, max_results: int = 5) -> List[Dict]:
    """
    Perform real-time web search via Tavily
    """

    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    response = client.search(
        query=query,
        max_results=max_results
    )

    results = []

    for item in response["results"]:
        results.append({
            "title": item["title"],
            "content": item["content"],
            "url": item["url"],
            "source_type": "web"
        })

    return results