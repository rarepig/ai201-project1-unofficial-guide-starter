import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_PATH, CHROMA_COLLECTION, EMBEDDING_MODEL, N_RESULTS

_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)

def embed_and_store(chunks):
    """Embed chunks and store in ChromaDB."""
    _collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )
    print(f"Stored {_collection.count()} total chunks.")

def retrieve(query, n_results=N_RESULTS):
    """Return top-k most relevant chunks for a query."""
    if _collection.count() == 0:
        return []
    results = _collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    output = []
    for text, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        output.append({
            "text": text,
            "source": meta["source"],
            "distance": dist
        })
    return output