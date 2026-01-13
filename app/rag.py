from pathlib import Path
from app.embeddings import embed_texts

BASE_DIR = Path(__file__).resolve().parent

def load_documents():
    docs_path = BASE_DIR / "documents"

    texts = []
    sources = []

    if not docs_path.exists():
        print("documents folder not found")
        return texts, sources

    for file in docs_path.glob("*.txt"):
        try:
            texts.append(file.read_text(encoding="utf-8"))
            sources.append(file.name)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    return texts, sources


def retrieve_relevant_chunks(query, texts, top_k=2):
    if not texts:
        return []
    
    query_embedding = embed_texts([query])[0]
    text_embeddings = embed_texts(texts)

    scores = text_embeddings @ query_embedding
    top_indices = scores.argsort()[-top_k:][::-1]

    return [texts[i] for i in top_indices]
