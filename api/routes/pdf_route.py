
from fastapi import APIRouter, UploadFile, File
from utils.ler_pdf import ler_arquivo_pdf
from agentes.resumo_agente import executar_resumo
from logging_config import logger

router = APIRouter(prefix="/pdf")

@router.post("/resumir")
async def resumir_pdf(file: UploadFile = File(...)):
    logger.info(f"Recebido PDF: {file.filename}")
    texto = ler_arquivo_pdf(file)
    logger.info(f"Conteúdo PDF lido (primeiros 300 chars): {texto[:300]}")
    resumo = executar_resumo(texto)
    logger.info(f"Resumo gerado (primeiros 300 chars): {resumo[:300]}")
    return {"resumo": resumo}
