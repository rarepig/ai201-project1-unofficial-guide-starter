from ingest import run_ingestion
from store import embed_and_store, retrieve

def main():
    # Step 1: Load, clean, chunk
    chunks = run_ingestion()
    
    # Step 2: Embed and store in ChromaDB
    print("\nEmbedding and storing chunks...")
    embed_and_store(chunks)
    
    # Step 3: Test retrieval with 3 queries
    test_queries = [
        "How long does C950 typically take to complete?",
        "Which courses are the most difficult in BSCS?",
        "What study resources help for passing D427?",
    ]
    
    print("\n--- Retrieval Test ---")
    for query in test_queries:
        print(f"\nQuery: {query}")
        results = retrieve(query)
        for i, r in enumerate(results, 1):
            print(f"  [{i}] (distance: {r['distance']:.3f}) [{r['source']}]")
            print(f"      {r['text'][:150]}...")
        print()

if __name__ == "__main__":
    main()