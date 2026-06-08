import os
import re
from config import DOCS_PATH, CHUNK_SIZE, CHUNK_OVERLAP

def load_documents():
    """Load all .txt files from the documents folder."""
    docs = []
    for filename in os.listdir(DOCS_PATH):
        if filename.endswith(".txt") and filename != ".gitkeep":
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            docs.append({
                "source": filename,
                "text": text
            })
    print(f"Loaded {len(docs)} documents.")
    return docs

def clean_text(text):
    lines = text.split("\n")
    cleaned = []
    skip_patterns = [
        "upvote", "downvote", "award", "share", "promoted",
        "sign up", "reply", "more reply", "view more",
        "r/WGU_CompSci -", "u/", "•", "ago\n"
    ]
    for line in lines:
        line_lower = line.strip().lower()
        if any(p in line_lower for p in skip_patterns):
            continue
        if len(line.strip()) < 3:
            continue
        cleaned.append(line)
    
    text = "\n".join(cleaned)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def chunk_text(text, source):
    """Split text into chunks of CHUNK_SIZE with CHUNK_OVERLAP."""
    chunks = []
    start = 0
    chunk_id = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        if len(chunk.strip()) > 0:
            chunks.append({
                "chunk_id": f"{source}_{chunk_id}",
                "source": source,
                "text": chunk.strip()
            })
            chunk_id += 1
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks

def run_ingestion():
    """Full pipeline: load → clean → chunk."""
    docs = load_documents()
    all_chunks = []
    for doc in docs:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned, doc["source"])
        all_chunks.extend(chunks)
    
    print(f"Total chunks: {len(all_chunks)}")
    
    # Print 5 sample chunks
    print("\n--- Sample Chunks ---")
    for chunk in all_chunks[:5]:
        print(f"\n[{chunk['source']}]")
        print(chunk['text'])
        print("-" * 40)
    
    return all_chunks

if __name__ == "__main__":
    run_ingestion()