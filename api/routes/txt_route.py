
from fastapi import APIRouter, UploadFile, File
from utils.ler_txt import ler_arquivo_txt
from agentes.resumo_agente import executar_resumo
from logging_config import logger
router = APIRouter(prefix="/txt")

@router.post("/resumir")
async def resumir_txt(file: UploadFile = File(...)):
    logger.info(f"Recebido TXT: {file.filename}")
    texto = ler_arquivo_txt(file)
    logger.info(f"Conteúdo TXT lido (primeiros 300 chars): {texto[:300]}")
    resumo = executar_resumo(texto)
    logger.info(f"Resumo gerado (primeiros 300 chars): {resumo[:300]}")
    return {"resumo": resumo}
