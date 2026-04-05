import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# In-memory DB
dimension = 384
index = faiss.IndexFlatL2(dimension)

# Store metadata
documents = []


def embed_text(text):
    return model.encode([text])[0]


def add_to_memory(text):
    vector = embed_text(text)
    index.add(np.array([vector]).astype("float32"))
    documents.append(text)


def retrieve_similar(query, k=3):
    if len(documents) == 0:
        return []

    query_vec = embed_text(query)
    D, I = index.search(np.array([query_vec]).astype("float32"), k)

    results = []
    for idx in I[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results
