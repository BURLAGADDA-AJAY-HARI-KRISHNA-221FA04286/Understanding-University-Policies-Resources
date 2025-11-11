import os
from google import genai
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

# ✅ Ensure you have GOOGLE_API_KEY set in your .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)

# === Load FAISS Index ===
print("🔍 Loading FAISS index...")

# ✅ Use balanced, memory-efficient embedding model for Render free tier
embeddings = HuggingFaceEmbeddings(model_name="intfloat/e5-small-v2")

# Ensure 'faiss_index' folder exists in your working directory
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})


def get_relevant_context(query: str) -> str:
    """Retrieve relevant text chunks from FAISS index."""
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])


def generate_answer(prompt: str) -> str:
    """Generate a response using Gemini 2.5 Flash."""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text if hasattr(response, "text") else str(response)


def answer_question(query: str) -> str:
    """Pipeline: Retrieve context → Generate final answer."""
    print("🧠 Retrieving context...")
    context = get_relevant_context(query)

    prompt = f"""
You are a helpful and accurate university assistant.
Use the context below to answer concisely and factually.

Context:
{context}

Question:
{query}

Answer:
"""
    return generate_answer(prompt)


# Run interactively for testing
if __name__ == "__main__":
    print("\n🎓 University RAG Chatbot (Render Optimized) is ready!\nType your question below:\n")
    while True:
        question = input("> ").strip()
        if question.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        try:
            answer = answer_question(question)
            print("\n" + answer + "\n")
        except Exception as e:
            print(f"\n❌ Error: {e}\n")
