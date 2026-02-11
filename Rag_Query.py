from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------- STEP 1: Load Embeddings ----------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------- STEP 2: Load FAISS Vector DB ----------
db = FAISS.load_local(
    "atomic_habits_faiss",
    embeddings,
    allow_dangerous_deserialization=True
)

print("FAISS database loaded successfully!")

# ---------- STEP 3: Initialize Gemini LLM ----------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# ---------- STEP 4: Build RAG Prompt ----------
def build_rag_prompt(context, question):
    return f"""
You are a helpful assistant.

Your behavior rules:
1. If the user's question is a greeting or casual message, respond politely like a chatbot.
3. If the answer is not found in the context, try to find it in the google and answer it and when the answer is fetched from the outside of book content say:
   "This answer is from outside the book."

Book Context:
{context}

User Question:
{question}

Answer:
"""

# ---------- STEP 5: RAG Query Function ----------
def ask_rag(question, k=3):
    docs = db.similarity_search(question, k=k)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = build_rag_prompt(context, question)

    response = llm.invoke(prompt)

    return response.content

# ---------- STEP 6: Test ----------
if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = ask_rag(question)
        print("\nAnswer:\n", answer)
