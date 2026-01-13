import numpy as np
import hashlib


def fake_embedding(text: str, dim: int = 384):
    hash_bytes = hashlib.sha256(text.encode()).digest()
    vector = np.frombuffer(hash_bytes, dtype=np.uint8).astype("float32")
    vector = np.pad(vector, (0, dim - len(vector)), mode="wrap")
    return vector[:dim]


def embed_texts(texts: list[str]) -> np.ndarray:
    return np.array([fake_embedding(t) for t in texts]).astype("float32")


def cosine_similarity(a: np.ndarray, b: np.ndarray):
    a_norm = a / np.linalg.norm(a)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    return np.dot(b_norm, a_norm)


def build_index(texts: list[str]):
    return embed_texts(texts)


def search_index(query_embedding, index_embeddings, top_k=2):
    scores = cosine_similarity(query_embedding[0], index_embeddings)
    top_indices = np.argsort(scores)[-top_k:][::-1]
    return top_indices
