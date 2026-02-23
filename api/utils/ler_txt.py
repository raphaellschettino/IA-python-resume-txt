
def ler_arquivo_txt(file):
    conteudo_bytes = file.file.read()
    try:
        texto = conteudo_bytes.decode("utf-8")
    except:
        texto = conteudo_bytes.decode("latin-1")
    return texto.strip()
