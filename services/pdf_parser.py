import PyPDF2

def parse_pdfs(files):
    parsed_texts = []
    for file in files:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        parsed_texts.append({"name": file.name, "text": text})
    return parsed_texts