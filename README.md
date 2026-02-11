# Atomic Habits RAG

A simple Retrieval-Augmented Generation (RAG) project that answers questions from *Atomic Habits* by:
- extracting text from PDF,
- cleaning and chunking the text,
- building embeddings and a FAISS vector index,
- querying Gemini with retrieved context.

## Project Structure

- `pdftotext.py`: Converts `atomic_habits.pdf` to `atomic_habits.txt`.
- `cleaning.py`: Cleans extracted text and writes `atomic_habits_cleaned.txt`.
- `chunking.py`: Splits cleaned text into chunks (for inspection/testing).
- `embeddings_gemini.py`: Tests embedding generation on chunks.
- `fasiss.py`: Creates and saves FAISS index in `atomic_habits_faiss/`.
- `Rag_Query.py`: Interactive CLI for asking questions with RAG.

## Requirements

- Python 3.9+
- A Google Gemini API key

Install dependencies:

```bash
pip install pdfplumber langchain langchain-community langchain-text-splitters langchain-google-genai sentence-transformers faiss-cpu
```

Set environment variable (PowerShell):

```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

For persistent setup on Windows:

```powershell
setx GOOGLE_API_KEY "your_api_key_here"
```

## End-to-End Pipeline

Run scripts in this order:

1. Convert PDF to text
```bash
python pdftotext.py
```

2. Clean extracted text
```bash
python cleaning.py
```

3. (Optional) Check chunking output
```bash
python chunking.py
```

4. (Optional) Validate embedding generation
```bash
python embeddings_gemini.py
```

5. Build FAISS vector database
```bash
python fasiss.py
```

6. Start RAG question-answer CLI
```bash
python Rag_Query.py
```

Type `exit` to quit the interactive session.

## Notes

- The FAISS index is loaded from `atomic_habits_faiss` in `Rag_Query.py`.
- Retrieval currently uses `k=3` similar chunks.
- Embeddings model: `sentence-transformers/all-MiniLM-L6-v2`.
- LLM model: `gemini-2.0-flash`.

## Common Issues

- `GOOGLE_API_KEY` missing: set the environment variable before running `Rag_Query.py`.
- `atomic_habits_faiss` not found: run `python fasiss.py` first.
- Missing packages: reinstall dependencies with the `pip install` command above.

## Possible Improvements

- Add `requirements.txt` and virtual environment instructions.
- Add source citations in final answers (chapter/page/chunk metadata).
- Add evaluation script for retrieval quality.
