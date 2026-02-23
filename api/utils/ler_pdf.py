
from pypdf import PdfReader

def ler_arquivo_pdf(file):
    reader = PdfReader(file.file)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text() + "\n"
    return texto.strip()
