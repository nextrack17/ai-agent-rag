import faiss
import numpy as np
import hashlib

def fake_embedding(text: str, dim=384):
    # Deterministic fake embedding based on text hash
    hash_bytes = hashlib.sha256(text.encode()).digest()
    vector = np.frombuffer(hash_bytes, dtype=np.uint8).astype("float32")
    vector = np.pad(vector, (0, dim - len(vector)), mode="wrap")
    return vector[:dim]

def embed_texts(texts: list[str]) -> np.ndarray:
    return np.array([fake_embedding(t) for t in texts]).astype("float32")

def build_faiss_index(texts: list[str]):
    embeddings = embed_texts(texts)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index
