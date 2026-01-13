from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import decide_route
from app.rag import load_documents, retrieve_relevant_chunks
from app.memory import update_memory

app = FastAPI()

# Global storage (loaded on startup)
texts = []
sources = []


@app.on_event("startup")
def startup_event():
    global texts, sources
    texts, sources = load_documents()


class AskRequest(BaseModel):
    query: str
    session_id: str | None = "default"


@app.post("/ask")
def ask(req: AskRequest):
    decision = decide_route(req.query)

    if decision == "document":
        chunks = retrieve_relevant_chunks(req.query, texts)
        context = "\n".join(chunks)

        answer = (
            "Based on company documents:\n\n"
            f"{context}"
        )
        used_sources = sources
    else:
        answer = (
            "This is a general question. "
            "It does not require company documents."
        )
        used_sources = []

    update_memory(req.session_id, req.query, answer)

    return {
        "answer": answer,
        "source": used_sources
    }


@app.get("/")
def health_check():
    return {"status": "ok"}
