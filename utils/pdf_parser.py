import fitz  # PyMuPDF

def extract_sections_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                text = " ".join([span["text"] for line in block["lines"] for span in line["spans"]])
                if len(text.strip()) > 50:
                    sections.append({
                        "page_number": page_num,
                        "title": text.strip().split("\n")[0][:80],
                        "content": text.strip()
                    })
    return sections