from typing import Dict, List

_session_memory: Dict[str, List[dict]] = {}

def get_memory(session_id: str):
    return _session_memory.get(session_id, [])

def update_memory(session_id: str, user_query: str, answer: str):
    _session_memory.setdefault(session_id, []).append({
        "user": user_query,
        "assistant": answer
    })
