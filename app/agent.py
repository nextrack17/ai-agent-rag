def decide_route(query: str) -> str:
    """
    Very simple routing logic.
    Later, this will be replaced by LLM-based reasoning.
    """
    keywords = [
        "policy", "leave", "remote", "work from home",
        "conduct", "company", "employee"
    ]

    query_lower = query.lower()
    for word in keywords:
        if word in query_lower:
            return "document"

    return "direct"
