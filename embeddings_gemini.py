from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ---------- Load cleaned text ----------
with open("atomic_habits_cleaned.txt", encoding="utf-8") as f:
    text = f.read()

# ---------- Chunking ----------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
)
chunks = splitter.split_text(text)

print(f"Chunks created: {len(chunks)}")

# ---------- Offline Embedding Model ----------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------- Test embedding ----------
vector = embeddings.embed_query(chunks[0])

print("Embedding successful!")
print("Vector length:", len(vector))
print("First 10 values:", vector[:10])
