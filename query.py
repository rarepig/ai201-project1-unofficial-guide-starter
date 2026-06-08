import os
from groq import Groq
from dotenv import load_dotenv
from store import retrieve

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a helpful assistant that answers questions about WGU Computer Science courses.
Answer using ONLY the information provided in the context below.
Even if the information is partial or mentioned briefly, use it to form an answer.
If the context contains ANY relevant information, use it to answer.
Only say "I don't have enough information on that." if the context has absolutely nothing relevant.
Always cite which document(s) your answer comes from using the source names provided."""

def ask(question):
    chunks = retrieve(question)
    
    if not chunks:
        return {
            "answer": "I don't have enough information on that.",
            "sources": []
        }
    
    context = "\n\n".join([
        f"[Source: {c['source']}]\n{c['text']}"
        for c in chunks
    ])
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ],
        max_tokens=1000,
    )
    
    answer = response.choices[0].message.content
    sources = list(set(c["source"] for c in chunks))
    
    return {
        "answer": answer,
        "sources": sources
    }

if __name__ == "__main__":
    q = "How long does C950 typically take to complete?"
    result = ask(q)
    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['sources']}")