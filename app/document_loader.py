from pathlib import Path

from pypdf import PdfReader


def load_text_file(file_path):
    file_path = Path(file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def load_pdf_file(file_path):
    file_path = Path(file_path)
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_document(file_path):
    file_path = Path(file_path)
    extension = file_path.suffix.lower()

    if extension == ".txt":
        return load_text_file(file_path)
    elif extension == ".pdf":
        return load_pdf_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
   



