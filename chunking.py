from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return splitter.split_text(text)




with open("atomic_habits_cleaned.txt", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)
print(len(chunks))
print(chunks[2][:300])
