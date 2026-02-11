import pdfplumber

pdf_path = "atomic_habits.pdf"
txt_path = "atomic_habits.txt"

all_text = []

with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if text:
            all_text.append(text)

with open(txt_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_text))

print("PDF successfully converted to text!")
