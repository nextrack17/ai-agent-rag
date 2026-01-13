import os
from pathlib import Path
from app.embeddings import build_faiss_index, embed_texts

BASE_DIR = Path(__file__).resolve().parent

def load_documents():
    docs_path = BASE_DIR / "documents"

    texts = []
    sources = []

    for file in docs_path.glob("*.txt"):
        texts.append(file.read_text(encoding="utf-8"))
        sources.append(file.name)

    return texts, sources

def retrieve_relevant_chunks(query, index, texts, top_k=2):
    query_embedding = embed_texts([query])
    distances, indices = index.search(query_embedding, top_k)
    return [texts[i] for i in indices[0]]
