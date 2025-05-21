import pdfplumber

def parse_pdfs(files):
    parsed_texts = []
    for file in files:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        parsed_texts.append({"name": file.name, "text": text})
    return parsed_texts