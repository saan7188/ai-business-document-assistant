from io import BytesIO
from pypdf import PdfReader

def read_document(name, data):
    if len(data) > 10_000_000:
        raise ValueError("File exceeds 10 MB")
    if name.lower().endswith(".pdf"):
        return [(i+1, page.extract_text() or "") for i, page in enumerate(PdfReader(BytesIO(data)).pages)]
    if name.lower().endswith(".txt"):
        return [(1, data.decode("utf-8"))]
    raise ValueError("Choose a PDF or text file")

def chunks(pages, size=180, overlap=30):
    if not 0 <= overlap < size:
        raise ValueError("Invalid overlap")
    result = []
    for page, text in pages:
        words = text.split()
        for start in range(0, len(words), size-overlap):
            result.append((page, " ".join(words[start:start+size])))
            if start+size >= len(words):
                break
    return result
