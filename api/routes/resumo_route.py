from fastapi import APIRouter
from schemas.texto_schema import Texto
from agentes.resumo_agente import executar_resumo
from logging_config import logger

router = APIRouter(prefix="/resumo")

@router.post("")
def resumir_json(dados: Texto):
    logger.info(f"Recebido JSON com {len(dados.conteudo)} chars")

    resumo = executar_resumo(dados.conteudo)

    logger.info(f"Resumo JSON gerado (primeiros 300 chars): {resumo[:300]}")
    return {"resumo": resumo}