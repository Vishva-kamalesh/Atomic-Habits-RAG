from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ---------- STEP 1: Load cleaned text ----------
with open("atomic_habits_cleaned.txt", encoding="utf-8") as f:
    text = f.read()

# ---------- STEP 2: Chunking ----------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
)
chunks = splitter.split_text(text)

print(f"Chunks created: {len(chunks)}")

# ---------- STEP 3: Offline Embeddings ----------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------- STEP 4: Create FAISS DB ----------
db = FAISS.from_texts(chunks, embeddings)

# ---------- STEP 5: Save FAISS DB ----------
db.save_local("atomic_habits_faiss")

print("FAISS vector database saved successfully!")
