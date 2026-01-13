import os
from app.embeddings import build_faiss_index, embed_texts

def load_documents(doc_path="app/documents"):
    texts = []
    sources = []

    for file in os.listdir(doc_path):
        if file.endswith(".txt"):
            with open(os.path.join(doc_path, file), "r", encoding="utf-8") as f:
                texts.append(f.read())
                sources.append(file)

    return texts, sources

def retrieve_relevant_chunks(query, index, texts, top_k=2):
    query_embedding = embed_texts([query])
    distances, indices = index.search(query_embedding, top_k)
    return [texts[i] for i in indices[0]]
