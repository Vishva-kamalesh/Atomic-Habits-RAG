import re

def clean_text_for_rag(text: str) -> str:
    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Remove page numbers (standalone numbers between lines)
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)

    # Fix words broken by line breaks (PDF issue)
    # Example: "improve-\nment" → "improvement"
    text = re.sub(r'-\n', '', text)

    # Join lines that are part of the same paragraph
    # Line break followed by lowercase letter = sentence continuation
    text = re.sub(r'\n(?=[a-z])', ' ', text)

    # Replace 3+ newlines with exactly 2 (paragraph separator)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Remove extra spaces
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()



with open("atomic_habits.txt", encoding="utf-8") as f:
    raw_text = f.read()

cleaned_text = clean_text_for_rag(raw_text)

with open("atomic_habits_cleaned.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("RAG-cleaned text saved successfully!")
